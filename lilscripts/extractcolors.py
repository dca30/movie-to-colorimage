import cv2

def extract_average_colors(input_file, output_file):
    # Open the input MP4 file
    video = cv2.VideoCapture(input_file)

    # Open the output text file for writing
    with open(output_file, "w") as f:
        # Loop through all frames in the video
        while True:
            # Read the next frame from the video
            success, frame = video.read()

            # If there are no more frames, break out of the loop
            if not success:
                break

            # Convert the frame to the HSV color space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Calculate the average color of the frame
            average_color = cv2.mean(hsv)[:3]

            # Write the average color to the output file
            f.write("{}\n".format(average_color))

    # Release the video capture object
    video.release()

# Extract the average colors from the input file and save them to the output file
extract_average_colors("Matrix.mp4", "output.txt")