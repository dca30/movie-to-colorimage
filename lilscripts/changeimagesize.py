from PIL import Image

# Open the original image
with Image.open('Matrix2.jpg') as original_image:
    # Resize the original image to fit within the 1920x1080 resolution
    resized_image = original_image.resize((10000, 5000))
    
    # Create a blank image with the desired resolution
    image = Image.new('RGB', (10000, 5000))
    pixels = image.load()
    
    # Iterate through the pixels and set the color for each pixel
    for i in range(10000):
        for j in range(5000):
            # Get the color for the current pixel from the resized image
            r, g, b = resized_image.getpixel((i, j))
            pixels[i, j] = (r, g, b)
    
    # Save the image
    image.save('Matrix2resizeada.jpg')
