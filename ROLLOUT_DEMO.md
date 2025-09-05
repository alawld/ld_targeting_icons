# LaunchDarkly Progressive Rollout Demo

This script demonstrates LaunchDarkly's progressive rollout capabilities by automatically controlling your feature flag percentage from 0% to 100% over 45 seconds.

## 🎯 What It Does

The `rollout-demo.sh` script will:

1. **Turn flag OFF** (0% - no image visible)
2. **Wait 5 seconds** (setup time)
3. **Set to 25%** rollout (quarter of image visible)
4. **Wait 10 seconds**
5. **Set to 50%** rollout (half of image visible) 
6. **Wait 10 seconds**
7. **Set to 75%** rollout (three-quarters visible)
8. **Wait 10 seconds**
9. **Set to 100%** rollout (full image visible)

**Total demo time: ~45 seconds**

## 🔧 Setup

### 1. Get Your LaunchDarkly API Token

1. Log into your LaunchDarkly dashboard
2. Go to **Account Settings** > **Authorization** > **Personal API tokens**
3. Click **Create token**
4. Give it a name like "Targeting Visualization Demo"
5. Set role to **Writer** or **Admin**
6. Copy the token

### 2. Find Your Project and Environment Keys

**Project Key:**
1. Go to **Projects** in LaunchDarkly
2. Click on your project
3. Go to **Settings** tab
4. Copy the **Project key** (usually `default`)

**Environment Key:**
1. Go to **Environments** in LaunchDarkly  
2. Click on your environment (e.g., Production, Test)
3. Go to **Settings** tab
4. Copy the **Environment key**

### 3. Update Your .env File

Add these lines to your `.env` file:

```bash
# LaunchDarkly API Configuration
LD_API_TOKEN=your-api-token-here
LD_PROJECT_KEY=default
LD_ENVIRONMENT_KEY=production
```

## 🚀 Usage

### Basic Demo
```bash
./rollout-demo.sh
```

### During a Live Demo
1. **Start your visualization**: Make sure Docker is running (`docker-compose up`)
2. **Open the visualization**: Visit `http://localhost:8080`
3. **Run the script**: `./rollout-demo.sh`
4. **Watch the magic**: Your image will progressively reveal itself!

## 📊 Perfect for Demos

This script is ideal for:
- **Sales demonstrations** - Show progressive rollouts in real-time
- **Customer presentations** - Demonstrate LaunchDarkly's targeting power
- **Team training** - Teach progressive rollout concepts
- **Conference talks** - Live feature flag demonstrations

## 🎨 Visual Impact

- **0%**: Clean white grid (no users targeted)
- **25%**: Your image starts appearing in scattered squares
- **50%**: Half your image is visible, creating anticipation
- **75%**: Most of the image revealed, building excitement  
- **100%**: Complete image reveal - dramatic finish!

## 🔍 Troubleshooting

### "Missing required environment variables"
- Check that your `.env` file has all the required variables
- Ensure there are no spaces around the `=` signs
- Verify your API token has the correct permissions

### "Failed to update flag (HTTP 401)"
- Your API token may be invalid or expired
- Check that the token has Writer or Admin permissions
- Regenerate the token if needed

### "Failed to update flag (HTTP 404)"
- Verify your `FLAG_KEY` matches exactly (case-sensitive)
- Check that `LD_PROJECT_KEY` and `LD_ENVIRONMENT_KEY` are correct
- Ensure the flag exists in the specified project/environment

### Script runs but visualization doesn't change
- Verify your visualization is using the same flag key
- Check that your SDK key in `.env` matches the environment
- Refresh your browser page

## 🛠 Customization

You can modify the script to:
- **Change timing**: Adjust the `sleep` values
- **Different percentages**: Modify the rollout percentages
- **Add more steps**: Include additional rollout phases
- **Custom messages**: Update the echo statements

## 🔐 Security Notes

- Never commit your `.env` file with real API tokens
- Use environment-specific API tokens (don't use production tokens for demos)
- Rotate API tokens regularly
- Consider using read-only tokens for view-only demos
