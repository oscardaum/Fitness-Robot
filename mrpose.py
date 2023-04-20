import argparse
import subprocess
from utils.exercise_utils import Exercise
from PIL import Image
import time

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

    intro_speech = "Hi my name is Jaunty and today I’ll lead you through a small workout. We’re going to be doing 5 pushups. To do a pushup, lay on the ground, raise your torso off the ground, and move your arms back and forth like this."
    subprocess.run(python27_path + " --speech "+intro_speech + " --movement push_up")
    subprocess.run("C:\Python27\python.exe  headTouch.py")

    pre_pushup = "Now it’s your turn. Start whenever you’re ready and I’ll count down your reps. After your 5th push up, enter a plank position. You’ll now be shown a picture of what a proper plank looks like."
    subprocess.run(python27_path + " --speech "+pre_pushup)

    img = Image.open("plank.jpeg")
    img.show()
    time.sleep(5)
    img.close()

    pose = Exercise(video, "pushup")
    pose.estimate_exercise(encouragement)

    pre_plank = "You’ve completed 5 pushups, good job! Once my head is tapped by one of the experiment conductors, I’ll start to time your plank. Please notify one of the experiment conductors when you’re ready to start your plank!"
    subprocess.run("C:\Python27\python.exe  headTouch.py")

    pose = Exercise(video, "plank")
    pose.estimate_exercise(encouragement)

    subprocess.run(python27_path + " --speech \"That’s all! Thank you for participating in this round of the experiment\"")
    subprocess.run(python27_path + " --movement rest")