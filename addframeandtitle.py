from PIL import Image, ImageDraw, ImageFont

def add_title(image, title, font_path, font_size, x, y, text_color):
  # Create a drawing context
  draw = ImageDraw.Draw(image)

  # Choose a font and font size
  font = ImageFont.truetype(font_path, font_size)

  # Draw the text on the image
  draw.text((x, y), title, font=font, fill=text_color)

def add_frame(image, width, height, background_color):
  # Create a new image with a white background
  new_image = Image.new('RGB', (image.width + width, image.height + height), background_color)

  # Paste the original image onto the new image
  new_image.paste(image, (width // 2, height // 2))
  return new_image

def rotate_image(image, angle):
  return image.transpose(Image.ROTATE_270)

# Open the image file
image = Image.open('MatrixGS.jpg')

# Rotate the image
image = rotate_image(image, 270)

# Add a frame to the image
image = add_frame(image, 1000, 1500, (255, 255, 255))

# Get the width and height of the image
width, height = image.size

# Choose a font and font size
font = ImageFont.truetype('DidotLTPro-Roman.ttf', 400)

# Get the width of the text in pixels
text_width, text_height = font.getsize('THE MATRIX')

# Calculate x and y coordinates for the text
x = width // 2 - text_width // 2
y = height - 600

# Add a title to the image
add_title(image, 'THE MATRIX', 'DidotLTPro-Roman.ttf', 300, x, y, (1,1,1))

# Save the modified image
image.save('finalImage.jpg')