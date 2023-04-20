# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.84])
keys.append([[-0.243948, [3, -0.293333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.84])
keys.append([[0.105804, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.84])
keys.append([[-0.474048, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.84])
keys.append([[-0.102736, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.84])
keys.append([[-0.858998, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.84])
keys.append([[-0.57069, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.84])
keys.append([[0.0112, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.84])
keys.append([[-0.542994, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.84])
keys.append([[0.1335, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.84])
keys.append([[-0.271476, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.84])
keys.append([[1.0983, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.84])
keys.append([[0.882008, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.84])
keys.append([[0.421808, [3, -0.293333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.84])
keys.append([[0.737812, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.84])
keys.append([[-0.417206, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.84])
keys.append([[0.101286, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.84])
keys.append([[0.875956, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.84])
keys.append([[0.404934, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.84])
keys.append([[0.0112, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.84])
keys.append([[-0.477116, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.84])
keys.append([[-0.0475121, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.84])
keys.append([[-0.271476, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.84])
keys.append([[1.00021, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.84])
keys.append([[0.765508, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.84])
keys.append([[-0.37127, [3, -0.293333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.84])
keys.append([[-0.382008, [3, -0.293333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
