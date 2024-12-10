import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import csv

# Initialize variables
points = []  # To store selected points
angles1 = []
angles2 = []
angles = []
timestamps = []

frame_increment = 20

def select_points(event, x, y, flags, param):
    """Callback function to capture mouse clicks."""
    global points
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
        points.append((x, y))
        print(f"Point selected: {x, y}")
        if len(points) == 3:
            # Draw lines between the selected points
            cv2.line(frame, points[0], points[1], (255, 0, 0), 2)
            cv2.line(frame, points[1], points[2], (255, 0, 0), 2)
            calculate_angles()
            cv2.imshow('Frame', frame)

def calculate_angles():
    """Calculate and display angles between points."""
    global points
    p1, p2, p3 = points

    # Calculate angles
    angle1 = 90-np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))
    angle2 = 90-np.degrees(np.arctan2(p3[1] - p2[1], p3[0] - p2[0]))

    print(f"Angle between first two points: {angle1:.2f} degrees")
    print(f"Angle between last two points: {angle2:.2f} degrees")
    # Calculate timestamp
    current_time = frame_count / fps

    angles1.append((angle1, current_time))
    angles2.append((angle2, current_time))


# Load video
filename = r"C:\Users\caima\Downloads\largeθ1-smallθ1-θ2.mp4"
cap = cv2.VideoCapture(filename)
fps = cap.get(cv2.CAP_PROP_FPS)

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', select_points)

frame_count = 0

while True:
    # Skip to the next 10 frames
    for _ in range(frame_increment):
        ret, frame = cap.read()
        if not ret:
            break
    if not ret:
        break

    frame_count += frame_increment
    points = []  # Reset points for the current frame

    # Scale the frame down by a factor of 0.5 (for example)
    scale_factor = 0.5
    frame = cv2.resize(frame, (0, 0), fx=scale_factor, fy=scale_factor)
    
    # Display the frame and wait for three points to be selected
    while len(points) < 3:
        # Draw vertical lines through each selected point
        for point in points:
            cv2.line(frame, (point[0], 0), (point[0], frame.shape[0]), (0, 255, 0), 1)
        
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == 27:  # ESC to exit
            break
    
    # Wait for 2 seconds before moving on to the next frame
    time.sleep(0.5)
    
    # Reset points for the next frame
    points = []

    if key == 27:  # ESC to exit
        break






# Get the current time
current_time_str = time.strftime("%Y%m%d-%H%M%S")

# Create filenames with the current time
angles1_filename = f'angles1_{current_time_str}.csv'
angles2_filename = f'angles2_{current_time_str}.csv'

# Write angles and timestamps to CSV files
with open(angles1_filename, 'w', newline='') as file1, open(angles2_filename, 'w', newline='') as file2:
    writer1 = csv.writer(file1)
    writer2 = csv.writer(file2)
    writer1.writerow(['Angle1', 'Timestamp'])
    writer2.writerow(['Angle2', 'Timestamp'])
    writer1.writerows(angles1)
    writer2.writerows(angles2)