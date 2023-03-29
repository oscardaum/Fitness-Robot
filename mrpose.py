import argparse
import subprocess
from utils.exercise_utils import Exercise

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', "--video", required=False, default=int(0),
                        help="Path to video source file", type=str)
    parser.add_argument('-e', "--exercise", required=False, default="predict",
                        help="Type of exercise in video source",
                        type=str, choices=['predict', 'pushup', 'plank', 'squat', 'jumpingjack'])
    args = parser.parse_args()

    python27_path = "C:\Python27\python.exe  naoqi_demo.py"
    subprocess.run(python27_path + " --movement wake_up")
    subprocess.run(python27_path + " --speech \"“Hi my name is Jaunty and I’m a NAO robot. Today I will be assisting you with squats. Tap my head when you’re ready to start”\"")

    subprocess.run(python27_path + " --speech \"Do five squats with me!\" --movement lat_raise")


    video = args.video
    exercise = args.exercise
    pose = Exercise(video, exercise)
    pose.estimate_exercise()
