import os
import numpy as np
from PIL import Image

path = '/home/dcalvo/code/movie-timeline-colors'

# Create a variable to store the input and output directories
input_dir = os.path.join(path, 'files')
output_dir = os.path.join(path, 'images')

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Get the base name of the file (without the .txt extension)
        base_name = os.path.splitext(filename)[0]

        # Open the file with the RGB colors
        with open(os.path.join(input_dir, filename), 'r') as colors_file:
            # Read the colors from the file and store them in a list
            colors = []
            for line in colors_file:
                r, g, b = map(float, line.strip().split())
                colors.append((r, g, b))

        # Create an image with one vertical bar for each color
        height = 100
        width = len(colors)
        image = np.zeros((height, width, 3), dtype=np.uint8)
        for i, color in enumerate(colors):
            image[:, i] = color

        # Open the image with the RGB colors using the Image module
        img = Image.fromarray(image)

        # Resize the image
        resized_image = img.resize((1920, 1080))

        # Create a blank image with the desired resolution
        final_image = Image.new('RGB', (1920, 1080))
        pixels = final_image.load()

        # Iterate through the pixels and set the color for each pixel
        for i in range(1920):
            for j in range(1080):
                # Get the color for the current pixel from the resized image
                r, g, b = resized_image.getpixel((i, j))
                pixels[i, j] = (r, g, b)

        final_image = final_image.transpose(Image.ROTATE_270)

        # Save the modified image if not exists
        output_file = os.path.join(output_dir, f'{base_name}.jpg')
        if os.path.isfile(output_file):
            print(f'{output_file} already exists, skipping...')
            continue
        final_image.save(output_file)
        print(f'{base_name} done')
'''
import os
import numpy as np
from PIL import Image

path = '/home/dcalvo/code/movie-to-colorimage'

# Create a variable to store the input and output directories
input_dir = os.path.join(path, 'colors')
output_dir = os.path.join(path, 'images')

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Get the base name of the file (without the .txt extension)
        base_name = os.path.splitext(filename)[0]

        # Open the file with the RGB colors
        with open(os.path.join(input_dir, filename), 'r') as colors_file:
            # Read the colors from the file and store them in a list
            colors = []
            for line in colors_file:
                hex_color = line.strip()
                #r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                r, g, b = tuple(int(line[1:][i:i+2], 16) for i in (0, 2, 4))



                colors.append((r, g, b))

        # Create an image with one vertical bar for each color
        height = 100
        width = len(colors)
        image = np.zeros((height, width, 3), dtype=np.uint8)
        for i, color in enumerate(colors):
            image[:, i] = color

        # Open the image with the RGB colors using the Image module
        img = Image.fromarray(image)

        # Resize the image
        resized_image = img.resize((1920, 1080))

        # Create a blank image with the desired resolution
        final_image = Image.new('RGB', (1920, 1080))
        pixels = final_image.load()

        # Iterate through the pixels and set the color for each pixel
        for i in range(1920):
            for j in range(1080):
                # Get the color for the current pixel from the resized image
                r, g, b = resized_image.getpixel((i, j))
                pixels[i, j] = (r, g, b)

        final_image = final_image.transpose(Image.ROTATE_270)

        # Save the modified image if not exists
        output_file = os.path.join(output_dir, f'{base_name}.jpg')
        if os.path.isfile(output_file):
            print(f'{output_file} already exists, skipping...')
            continue
        final_image.save(output_file)
        print(f'{base_name} done')
'''
