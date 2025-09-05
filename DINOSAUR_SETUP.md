# Adding Your Dinosaur Image

To use your original dinosaur PNG image in the visualization:

## Step 1: Add Your Image
1. Copy your dinosaur PNG image to: `static/images/original-dinosaur.png`
2. Replace the placeholder file that's currently there

## Step 2: Optimal Image Size
For best results, your image should be:
- **Aspect ratio**: 5:4 (width:height)
- **Recommended size**: 750x600 pixels or larger
- **Format**: PNG with transparent background (optional)

## Step 3: How It Works
- Your image gets scaled to 750x600 pixels (50 columns × 15px by 40 rows × 15px)
- Each square in the grid shows a 15x15 pixel piece of your image
- When users are targeted (flag returns `true`), their square reveals that piece
- When not targeted (flag returns `false`), the square shows red instead

## Step 4: Test
1. Rebuild the Docker container: `docker-compose up --build`
2. Visit `http://localhost:8080`
3. Adjust your LaunchDarkly flag targeting to see your dinosaur appear!

## Troubleshooting
- If the image looks stretched, make sure it has a 5:4 aspect ratio
- If pieces don't align properly, try using an image that's exactly 750x600 pixels
- The image will be automatically scaled, so larger images work fine
