import argparse
import subprocess
from utils.exercise_utils import Exercise

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', "--video", required=False, default=int(0),
                        help="Path to video source file", type=str)
    parser.add_argument('-e', "--exercise", required=False, default="pushup",
                        help="Type of exercise in video source",
                        type=str, choices=['predict', 'pushup', 'plank', 'squat', 'jumpingjack'])
    parser.add_argument('-n', "--nao", required=False, default="level1",
                        help="Type of exercise in video source",
                        type=str, choices=['level1', 'level2', 'level3'])
    args = parser.parse_args()

    video = args.video
    exercise = args.exercise
    encouragement = args.nao

    python27_path = "C:\Python27\python.exe  naoqi_demo.py"
    subprocess.run("C:\Python27\python.exe  headTouch.py")
    subprocess.run(python27_path + " --movement wake_up")
    subprocess.run(python27_path + " --speech \"“Hi my name is Jaunty and I’m a NAO robot. Today I will be assisting you with pushups Tap my head when you’re ready to start”\"")
    subprocess.run("C:\Python27\python.exe  headTouch.py")

    subprocess.run(python27_path + " --speech \"Do five pushups with me! To do a pushup, get on the ground, raise your torso off the ground, and move your arms back and forth like this.\" --movement pushup")


    pose = Exercise(video, "pushup")
    pose.estimate_exercise(encouragement)
    pose = Exercise(video, "plank")
    pose.estimate_exercise(encouragement)

    # subprocess.run(python27_path + " --speech \"Good job! You did great! I hope I was able to help you with exercise today!\"")
    # subprocess.run(python27_path + " --movement rest")