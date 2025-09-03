from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import json
import ldclient
from ldclient.config import Config
import os
import threading
import time
from utils.create_context import create_multi_context

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
socketio = SocketIO(app, cors_allowed_origins="*")

# LaunchDarkly configuration
sdk_key = os.environ.get('SDK_KEY')
feature_flag_key = os.environ.get('FLAG_KEY')

if sdk_key:
    ldclient.set_config(Config(sdk_key, send_events=False))
else:
    print("Warning: SDK_KEY not found in environment variables")

# Global variables
contexts_data = []
current_state = []

def create_contexts():
    """Create fake contexts for visualization"""
    num_contexts = 2000
    contexts_array = []
    for i in range(num_contexts):
        context = create_multi_context()
        contexts_array.append(context)
    return contexts_array

def evaluate_contexts(contexts):
    """Evaluate all contexts against the feature flag"""
    if not sdk_key or not feature_flag_key:
        # Return dummy data if no LaunchDarkly config
        return [i % 2 == 0 for i in range(len(contexts))]
    
    results = []
    for context in contexts:
        try:
            feature = ldclient.get().variation(feature_flag_key, context, False)
            results.append(feature)
        except Exception as e:
            print(f"Error evaluating context: {e}")
            results.append(False)
    return results

def background_polling():
    """Background thread to poll for flag changes"""
    global current_state
    
    while True:
        try:
            new_state = evaluate_contexts(contexts_data)
            if new_state != current_state:
                current_state = new_state
                # Emit the new state to all connected clients
                socketio.emit('flag_update', {'data': current_state})
        except Exception as e:
            print(f"Error in background polling: {e}")
        
        time.sleep(0.5)  # Poll every 500ms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/initial-data')
def get_initial_data():
    """Get initial flag evaluation data"""
    global contexts_data, current_state
    
    if not contexts_data:
        contexts_data = create_contexts()
        current_state = evaluate_contexts(contexts_data)
    
    return jsonify({
        'data': current_state,
        'total_contexts': len(contexts_data),
        'flag_key': feature_flag_key or 'Not configured'
    })

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Send initial data to the newly connected client
    emit('flag_update', {'data': current_state})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # Initialize contexts
    contexts_data = create_contexts()
    current_state = evaluate_contexts(contexts_data)
    
    # Start background polling thread
    polling_thread = threading.Thread(target=background_polling, daemon=True)
    polling_thread.start()
    
    # Run the Flask app
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)

