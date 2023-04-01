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

    video = args.video
    exercise = args.exercise

    nao_exercise = exercise
    if exercise=="jumpingjack":
        nao_exercise="jumping_jack"


    python27_path = "C:\Python27\python.exe  naoqi_demo.py"
    subprocess.run("C:\Python27\python.exe  headTouch.py")
    subprocess.run(python27_path + " --movement wake_up")
    subprocess.run(python27_path + " --speech \"“Hi my name is Jaunty and I’m a NAO robot. Today I will be assisting you with " + nao_exercise + ". Tap my head when you’re ready to start”\"")
    subprocess.run("C:\Python27\python.exe  headTouch.py")

    if(nao_exercise=="squat"):
        subprocess.run(python27_path + " --speech \"Do five "+ nao_exercise + " with me! This is what a " + nao_exercise + " looks like! Keep your arms out front and bend your legs.\" --movement " + nao_exercise)
    elif (nao_exercise=="jumping_jack"):
        subprocess.run(python27_path + " --speech \"Do five jumping jacks with me! This is what a " + nao_exercise + " looks like! Jump up, spreading your legs apart while raising your arms above your head.\" --movement " + nao_exercise)
 

    pose = Exercise(video, exercise)
    pose.estimate_exercise()

    subprocess.run(python27_path + " --speech \"Good job! You did great! I hope I was able to help you with exercise today!\"")
    subprocess.run(python27_path + " --movement rest")