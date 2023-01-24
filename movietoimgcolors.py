import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from progress.bar import Bar

#filename ="SpiderMan"
filenames = ["video"]

for filename in filenames:


    homepath ='/home/diego/MovieToColorsImage/'
    # Open the video file
    video_path = homepath+'movies/'+filename+'.mp4'
    video = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video and the frame rate
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video.get(cv2.CAP_PROP_FPS)

    # Calculate the total number of seconds in the video
    total_seconds = total_frames / frame_rate

    # Open a file to write the average colors to
    colors_file = open(homepath+'colors/'+filename+'colors.txt', 'w')

    # Create a progress bar
    bar = Bar('Processing', max=int(total_seconds), suffix='%(percent)d%%' , width=50)

    # Iterate over each second in the video
    #for i in tqdm(range(int(total_seconds))):
    for i in range(int(total_seconds)):
        # Initialize a list to store the frame colors for this second
        frame_colors = []

        # Iterate over each frame in this second
        for j in range(int(frame_rate)):
            # Read the frame
            _, frame = video.read()

            # Convert the frame to the BGR color space
            bgr = frame
            
            # Calculate the average color of the frame
            avg_color_per_row = np.average(bgr, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            
            # Add the average color to the list of frame colors
            frame_colors.append(avg_color)

        # Calculate the average color for the second
        avg_color_per_second = np.average(frame_colors, axis=0)

        # Write the average color to the file
        colors_file.write(str(avg_color_per_second[0]) + ' ' + str(avg_color_per_second[1]) + ' ' + str(avg_color_per_second[2]) + '\n')

        # Update the progress bar
        bar.next()

    # Close the file and video capture
    colors_file.close()
    video.release()

    # Finish the progress bar
    bar.finish()
    print("\033[92m\033[1mColors successfully extracted\033[0m")


    # Open the file with the RGB colors
    colors_file = open(homepath+'colors/'+filename+'colors.txt', 'r')

    # Read the colors from the file and store them in a list
    colors = []
    for line in colors_file:
        r, g, b = map(float, line.strip().split())
        colors.append((b, g, r))

    # Close the file
    colors_file.close()

    # Create an image with one vertical bar for each color
    height = 100
    width = len(colors)
    image = np.zeros((height, width, 3), dtype=np.uint8)
    for i, color in enumerate(colors):
        image[:, i] = color

    # Create specific folder for each movie
    if not os.path.exists(homepath+'images/'+filename):
        # Create the directory if it does not exist
        os.mkdir(homepath+'images/'+filename)
    # Save the image to a file
    cv2.imwrite(homepath+'images/'+filename+'/'+filename+'Line.jpg', image)

    bar = Bar('Processing', max=int(total_seconds), suffix='%(percent)d%%' , width=50)

    # Open the original image
    with Image.open(homepath+'images/'+filename+'/'+filename+'Line.jpg') as original_image:

        # Resize the original image to fit within the 10000x7000 resolution
        resized_image = original_image.resize((10000, 7000))
        
        # Create a blank image with the desired resolution
        image = Image.new('RGB', (10000, 7000))
        pixels = image.load()
        



        # Iterate through the pixels and set the color for each pixel
        for i in range(10000):
            for j in range(7000):
                # Get the color for the current pixel from the resized image
                r, g, b = resized_image.getpixel((i, j))
                pixels[i, j] = (r, g, b)

            # Update the progress bar
            bar.next()
            
        bar.finish()
        print("\033[92m\033[1mPicture successfully oversized\033[0m")
        # Save the image
        #Imagen girada y agrandada
        image.save(homepath+'images/'+filename+'/'+filename+'Colors.jpg')

        #Add frame
        def add_frame_and_rotate(image, width, height, background_color):
            # Create a new image with a white background
            image = image.transpose(Image.ROTATE_270)
            new_image = Image.new('RGB', (image.width + width, image.height + height + 200), background_color)

            # Paste the original image onto the new image
            new_image.paste(image, (width // 2, height // 2))
            return new_image
        #TITLE ADD
        def add_title(image, title, font_path, font_size, x, y, text_color):
            # Create a drawing context
            draw = ImageDraw.Draw(image)

            # Choose a font and font size
            font = ImageFont.truetype(font_path, font_size)

            # Draw the text on the image
            draw.text((x, y), title, font=font, fill=text_color)

        

        # Open the image file
        image = Image.open(homepath+'images/'+filename+'/'+filename+'Colors.jpg')

        # Add a frame to the image
        image = add_frame_and_rotate(image, 1000, 1500, (255, 255, 255))

        # Get the width and height of the image
        width, height = image.size

        # Choose a font and font size
        font = ImageFont.truetype('fonts/DidotLTPro-Roman.ttf', 300)

        # Get the width of the text in pixels
        text_width, text_height = font.getsize(filename.upper())

        # Calculate x and y coordinates for the text
        x = width // 2 - text_width // 2
        y = height - 650

        # Add a title to the image
        add_title(image, filename.upper(), 'fonts/DidotLTPro-Roman.ttf', 300, x, y, (1,1,1))

        # Save the modified image
        image.save(homepath+'images/'+filename+'/'+filename+'Final.jpg')
        print(filename+" done")