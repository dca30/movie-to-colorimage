import cv2
import numpy as np
import sys
from progress.bar import Bar
from PIL import Image

def extract_colors(filename, homepath):
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

def create_color_image(filename, homepath, width, height):
  # Open the file with the RGB colors
  colors_file = open(homepath+'colors/'+filename+'colors.txt', 'r')

  # Read the colors from the file and store them in a list
  colors = []
  for line in colors_file:
      r, g, b = map(float, line.strip().split())
      colors.append((b, g, r))

  # Close the file
  colors_file.close()

  # Create
