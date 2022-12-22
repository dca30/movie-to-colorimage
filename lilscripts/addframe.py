from PIL import Image, ImageDraw, ImageFont

# Open the image file
image = Image.open('MatrixGS.jpg')
image = image.transpose(Image.ROTATE_270)

# Create a new image with a white background
new_image = Image.new('RGB', (image.width + 1000, image.height + 1500), (255, 255, 255))

# Paste the original image onto the new image
new_image.paste(image, (500, 500))

# Save the final image
#new_image.save('modified_image.jpg')
new_image.show()



draw = ImageDraw.Draw(new_image)

# Choose a font and font size
font = ImageFont.truetype('arial.ttf', 300)

# Get the width and height of the image
width, height = image.size

# Calculate the width of the text in pixels
text_width, text_height = font.getsize('The Matrix')

# Calculate x and y coordinates for the text
x = width // 2 - text_width // 2
y = height - 600

# Set the text color to white
text_color = (1,1,1)

# Draw the text on the image
draw.text((x, y), 'The Matrix', font=font, fill=text_color)

# Save the modified image
new_image.show()
#image.save('title_image.jpg')
