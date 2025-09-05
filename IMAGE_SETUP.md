# Adding Your Custom Reveal Image

To use your own PNG image in the visualization:

## Step 1: Add Your Image
1. Copy your PNG image to: `static/images/reveal-image.png`
2. Replace the placeholder file that's currently there

## Step 2: Optimal Image Size
For best results, your image should be:
- **Aspect ratio**: 4:5 (width:height) - matches the 40×50 grid
- **Recommended size**: 600x750 pixels or larger
- **Format**: PNG with transparent background (optional)

## Step 3: How It Works
- Your image gets scaled to 600x750 pixels (40 columns × 15px by 50 rows × 15px)
- Each square in the grid shows a 15x15 pixel piece of your image
- When users are targeted (flag returns `true`), their square reveals that piece
- When not targeted (flag returns `false`), the square shows white instead

## Step 4: Test
1. Rebuild the Docker container: `docker-compose up --build`
2. Visit `http://localhost:8080`
3. Adjust your LaunchDarkly flag targeting to see your image appear!

## Step 5: Image Ideas
Your reveal image could be:
- Company logo
- Product image
- Character or mascot
- Abstract art
- Photo
- Any image that works well when revealed piece by piece!

## Troubleshooting
- If the image looks stretched, make sure it has a 4:5 aspect ratio
- If pieces don't align properly, try using an image that's exactly 600x750 pixels
- The image will be automatically scaled, so larger images work fine
