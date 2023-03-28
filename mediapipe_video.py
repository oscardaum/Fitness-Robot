import cv2
import mediapipe as mp
import subprocess

# Initialize the MediaPipe Pose model
mp_pose = mp.solutions.pose

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Set the minimum number of frames to detect a squat
min_frames = 10

# Initialize the counter for consecutive correct frames
correct_frames = 0

# Loop through each frame of the video capture
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        # Read the next frame from the video capture
        ret, frame = cap.read()

        # Convert the frame to RGB for processing by MediaPipe
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame using MediaPipe Pose
        results = pose.process(frame)

        # Check if a pose was detected
        if results.pose_landmarks is not None:
            # Extract the landmark positions for the left knee, right knee, and hips
            left_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE]
            right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE]
            left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
            right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

            # Calculate the angle between the knees and hips
            angle = abs((left_knee.y - left_hip.y) / (left_knee.x - left_hip.x)) - abs((right_knee.y - right_hip.y) / (right_knee.x - right_hip.x))
            
            # Determine if the angle indicates a squat
            if angle < 0.2:
                # Increment the counter for consecutive correct frames
                correct_frames += 1
                
                # Check if enough consecutive correct frames have been detected to consider it a valid squat
                if correct_frames >= min_frames:
                    subprocess.run("C:\Python27\python.exe naoqi_demo.py")
                    print("Squat detected!")
                    # Reset the counter for consecutive correct frames
                    correct_frames = 0
            else:
                # Reset the counter for consecutive correct frames if the angle is not indicative of a squat
                correct_frames = 0

        # Convert the frame back to BGR for display
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Display the frame
        cv2.imshow('MediaPipe Pose', frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
