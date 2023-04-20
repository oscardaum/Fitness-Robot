# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.92])
keys.append([[-0.15651, [3, -0.32, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.92])
keys.append([[0.0152981, [3, -0.32, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.92])
keys.append([[0.0889301, [3, -0.32, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.92])
keys.append([[-0.108872, [3, -0.32, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.92])
keys.append([[-1.50635, [3, -0.32, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.92])
keys.append([[-1.61534, [3, -0.32, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.92])
keys.append([[0.0172, [3, -0.32, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.92])
keys.append([[0.124296, [3, -0.32, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.92])
keys.append([[0.121228, [3, -0.32, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.92])
keys.append([[-0.170232, [3, -0.32, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.92])
keys.append([[-0.096684, [3, -0.32, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.92])
keys.append([[0.174834, [3, -0.32, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.92])
keys.append([[0.951038, [3, -0.32, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.92])
keys.append([[-1.51103, [3, -0.32, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.92])
keys.append([[0.0859461, [3, -0.32, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.92])
keys.append([[0.112024, [3, -0.32, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.92])
keys.append([[1.53864, [3, -0.32, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.92])
keys.append([[1.8561, [3, -0.32, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.92])
keys.append([[0.0208, [3, -0.32, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.92])
keys.append([[0.133416, [3, -0.32, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.92])
keys.append([[-0.125746, [3, -0.32, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.92])
keys.append([[-0.170232, [3, -0.32, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.92])
keys.append([[-0.0935321, [3, -0.32, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.92])
keys.append([[0.266958, [3, -0.32, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.92])
keys.append([[-1.07998, [3, -0.32, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.92])
keys.append([[1.37749, [3, -0.32, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
