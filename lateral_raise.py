import cv2
import mediapipe as mp
import math
import time
import subprocess 

# Load the Mediapipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Define the threshold angle for a lateral raise
THRESHOLD_ANGLE = 45

# Initialize the frame count and lateral raise count
frame_count = 0
raise_count = 0
# isLatRaise = False

# Open a video capture device
cap = cv2.VideoCapture(0)

#Define naoqi execution path, could be different for different people, maybe pass this in as an argument idk
python27_path = "C:\Python27\python.exe  naoqi_demo.py"

subprocess.run(python27_path + " --movement wake_up")
subprocess.run(python27_path + " --speech \"“Hi my name is Jaunty and I’m a NAO robot. Today I will be assisting you with a lateral raise exercise. Tap my head when you’re ready to start”\"")

subprocess.run(python27_path + " --speech \"Do five lat raises with me!\" --movement lat_raise")
#Now do 5 lat raises

# Loop over the frames in the video
while True:
    # Read the next frame from the video capture device
    ret, image = cap.read()

    # If there are no more frames, break out of the loop
    if not ret:
        break

    # Convert the image to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get the pose landmarks for the current image
    results = pose.process(image)

    # Check if a pose is detected
    if results.pose_landmarks is not None:
        # Get the landmarks for the shoulders, elbows, and wrists
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
        right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

        # Calculate the angle between the upper arm and the torso for each arm
        left_angle = math.degrees(
            math.atan2(left_wrist.y - left_elbow.y, left_wrist.x - left_elbow.x) -
            math.atan2(left_elbow.y - left_shoulder.y, left_elbow.x - left_shoulder.x)
        )
        right_angle = math.degrees(
            math.atan2(right_wrist.y - right_elbow.y, right_wrist.x - right_elbow.x) -
            math.atan2(right_elbow.y - right_shoulder.y, right_elbow.x - right_shoulder.x)
        )

        # Check if either angle exceeds the threshold for a lateral raise
        if (left_angle > THRESHOLD_ANGLE or right_angle > THRESHOLD_ANGLE):
            # Increment the lateral raise count
            # isLatRaise = True
            raise_count += 1
            print(raise_count, "lat raises detected, the angles were: ", left_angle, right_angle)
            subprocess.run(python27_path + " --speech \"" + str(raise_count) + " lat raises. Good job!\"")

            time.sleep(3)

            if(raise_count==5):
                subprocess.run(python27_path + "--movement rest")

        # Draw the pose detection lines on the image
        mp_drawing = mp.solutions.drawing_utils
        annotated_image = image.copy()
        mp_drawing.draw_landmarks(
            annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Show the image with pose detection lines
        cv2.imshow("Lateral Raise Detector", annotated_image)

    # Wait for a key press and check if the "q" key was pressed to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    # Increment the frame count
    frame_count += 1

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()

# Print the number of lateral raises detected
print("Detected {} lateral raises.".format(raise_count))