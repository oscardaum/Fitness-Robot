import cv2
import mediapipe as mp

# Load the Mediapipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load the image
image = cv2.imread("path/to/image.jpg")

# Convert the image to RGB format
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get the pose landmarks for the current image
results = pose.process(image)

# Check if a squat is being performed
if results.pose_landmarks is not None:
    # Get the y-coordinate of the left hip and left knee landmarks
    left_hip_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
    left_knee_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y
    
    # Calculate the angle between the left hip, left knee, and left ankle landmarks
    left_hip_knee_angle = mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.LEFT_KNEE, mp_pose.PoseLandmark.LEFT_ANKLE
    left_hip_knee_angle = mp_pose.utils.angle_degrees(
        results.pose_landmarks.landmark[left_hip_knee_angle[0]],
        results.pose_landmarks.landmark[left_hip_knee_angle[1]],
        results.pose_landmarks.landmark[left_hip_knee_angle[2]]
    )
    
    # Check if the angle is within the correct range for a squat
    if left_hip_y > left_knee_y and left_hip_knee_angle >= 90 and left_hip_knee_angle <= 140:
        print("Correct squat!")
    else:
        print("Incorrect squat.")
else:
    print("No pose detected.")