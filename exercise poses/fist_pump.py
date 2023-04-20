# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.96, 2.48])
keys.append([[-0.213268, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.293036, [3, -0.506667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.96, 2.48])
keys.append([[0.0168321, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.01845, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.96, 2.48])
keys.append([[0.0919981, [3, -0.333333, 0], [3, 0.506667, 0]], [0.0919981, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.96, 2.48])
keys.append([[-0.110406, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.110406, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.96, 2.48])
keys.append([[-0.469362, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.469362, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.96, 2.48])
keys.append([[-1.08918, [3, -0.333333, 0], [3, 0.506667, 0]], [-1.08918, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.96, 2.48])
keys.append([[0.3664, [3, -0.333333, 0], [3, 0.506667, 0]], [0.3664, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.96, 2.48])
keys.append([[0.131966, [3, -0.333333, 0], [3, 0.506667, 0]], [0.131966, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.96, 2.48])
keys.append([[0.115092, [3, -0.333333, 0], [3, 0.506667, 0]], [0.115092, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.96, 2.48])
keys.append([[-0.171766, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.171766, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.96, 2.48])
keys.append([[-0.09515, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.0844119, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.96, 2.48])
keys.append([[1.60606, [3, -0.333333, 0], [3, 0.506667, 0]], [1.60606, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.96, 2.48])
keys.append([[0.115008, [3, -0.333333, 0], [3, 0.506667, 0]], [0.115008, [3, -0.506667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.96, 2.48])
keys.append([[-0.469446, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.469446, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.96, 2.48])
keys.append([[0.09515, [3, -0.333333, 0], [3, 0.506667, 0]], [0.09515, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.96, 2.48])
keys.append([[0.112024, [3, -0.333333, 0], [3, 0.506667, 0]], [0.112024, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.96, 2.48])
keys.append([[1.53404, [3, -0.333333, 0], [3, 0.506667, 0]], [0.131966, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.96, 2.48])
keys.append([[1.24096, [3, -0.333333, 0], [3, 0.506667, 0]], [0.539926, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.96, 2.48])
keys.append([[0.0732, [3, -0.333333, 0], [3, 0.506667, 0]], [0.0732, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.96, 2.48])
keys.append([[0.122678, [3, -0.333333, 0], [3, 0.506667, 0]], [0.121144, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.96, 2.48])
keys.append([[-0.122678, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.122678, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.96, 2.48])
keys.append([[-0.171766, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.171766, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.96, 2.48])
keys.append([[-0.0873961, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.0873961, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.96, 2.48])
keys.append([[-0.110406, [3, -0.333333, 0], [3, 0.506667, 0]], [-1.46953, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.96, 2.48])
keys.append([[-1.2027, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.0629361, [3, -0.506667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.96, 2.48])
keys.append([[0.558334, [3, -0.333333, 0], [3, 0.506667, 0]], [-0.30991, [3, -0.506667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
