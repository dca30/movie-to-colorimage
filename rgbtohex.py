file_name = "/home/dcalvo/code/movie-timeline-colors/files/adastra1.txt"

with open(file_name, 'r') as file:
    lines = file.readlines()

with open(file_name, 'w') as file:
    for line in lines:
        file.write(line[1:])

'''
#transform rgb into hexadecimal
import os

def float_to_hex(float_rgb):
    int_rgb = [round(x) for x in float_rgb]
    hex_rgb = ''.join([format(x, '02X') for x in int_rgb])
    return hex_rgb


directory = '/home/dcalvo/code/movie-timeline-colors/files'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as f:
            lines = f.readlines()
        hex_colors = [float_to_hex(
            [float(x) for x in line.split()]) + '\n' for line in lines]
        with open(os.path.join(directory, filename), 'w') as f:
            f.writelines(hex_colors)


import cv2
import numpy as np
import sys
from progress.bar import Bar


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


# Open the video file
video_path = 'the+tree+of+life.mp4'
video = cv2.VideoCapture(video_path)

# Get the total number of frames in the video and the frame rate
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = video.get(cv2.CAP_PROP_FPS)

# Calculate the total number of seconds in the video
total_seconds = total_frames / frame_rate

# Open a file to write the average colors to
colors_file = open('the+tree+of+life.txt', 'w')

# Create a progress bar
bar = Bar('Processing', max=int(total_seconds), suffix='%(percent)d%%')

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

    # Convert the average color from RGB to hexadecimal
    avg_color_hex = rgb_to_hex(avg_color_per_second)

    # Write the average color to the file
    colors_file.write(avg_color_hex + '\n')

    # Update the progress bar
    bar.next()

# Close the file and video capture
colors_file.close()
video.release()

# Finish the progress bar
bar.finish()
'''
