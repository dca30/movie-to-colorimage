import cv2
import numpy as np

# Open the file with the RGB colors
colors_file = open('colors.txt', 'r')

# Read the colors from the file and store them in a list
colors = []
for line in colors_file:
    r, g, b = map(float, line.strip().split())
    colors.append((b, g, r))

# Close the file
colors_file.close()

# Create an image with one vertical bar for each color
height = 1080
width = len(colors)
image = np.zeros((height, width, 3), dtype=np.uint8)
for i, color in enumerate(colors):
    image[:, i] = color

# Save the image to a file
cv2.imwrite('image.jpg', image)