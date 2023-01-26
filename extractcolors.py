import cv2
import os
import numpy as np
# from PIL import Image, ImageDraw, ImageFont

input = '/home/dcalvo/Descargas/pel/'
output = '/home/dcalvo/code/movie-timeline-colors/files/'
filenames = [file for file in os.listdir(input) if file.endswith('.mp4')]

for filename in filenames:
    # Open the video file
    print(filename)
    path_input = os.path.join(input, filename)
    path_output = os.path.join(output, filename)
    video = cv2.VideoCapture(path_input)
    # Get the total number of frames in the video and the frame rate
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video.get(cv2.CAP_PROP_FPS)

    # Calculate the total number of seconds in the video
    total_seconds = total_frames / frame_rate

    # Open a file to write the average colors to
    colors_file = open(os.path.splitext(path_output)[0]+'.txt', 'w')

    # Iterate over each second in the video
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
        colors_file.write(str(avg_color_per_second[0]) + ' ' + str(
            avg_color_per_second[1]) + ' ' + str(avg_color_per_second[2]) + '\n')

    # Close the file and video capture
    print(filename+' done')
    colors_file.close()
    video.release()
