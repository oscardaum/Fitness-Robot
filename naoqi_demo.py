from naoqi import ALProxy 
import time
import argparse

def lat_raise(motionProxy):
    #RShoulderRoll 

    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.150374, [3, -0.08, 0], [3, 0.453333, 0]], [-0.158044, [3, -0.453333, 0], [3, 0.48, 0]], [-0.150374, [3, -0.48, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.2, 1.56, 3])
    keys.append([[0.00302601, [3, -0.08, 0], [3, 0.453333, 0]], [0.00302601, [3, -0.453333, 0], [3, 0.48, 0]], [0.00302601, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.2, 1.56, 3])
    keys.append([[0.0873961, [3, -0.08, 0], [3, 0.453333, 0]], [0.0858622, [3, -0.453333, 0], [3, 0.48, 0]], [0.0873961, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.110406, [3, -0.08, 0], [3, 0.453333, 0]], [-0.102736, [3, -0.453333, 0], [3, 0.48, 0]], [-0.110406, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.406468, [3, -0.08, 0], [3, 0.453333, 0]], [-0.056716, [3, -0.453333, 0], [3, 0.48, 0]], [-0.389594, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.2, 1.56, 3])
    keys.append([[-1.18582, [3, -0.08, 0], [3, 0.453333, 0]], [-1.18582, [3, -0.453333, 0], [3, 0.48, 0]], [-1.18582, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.2, 1.56, 3])
    keys.append([[0.2968, [3, -0.08, 0], [3, 0.453333, 0]], [0.2876, [3, -0.453333, 0], [3, 0.48, 0]], [0.2968, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[0.122762, [3, -0.08, 0], [3, 0.453333, 0]], [0.12583, [3, -0.453333, 0], [3, 0.48, 0]], [0.122762, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[0.098218, [3, -0.08, 0], [3, 0.453333, 0]], [0.096684, [3, -0.453333, 0], [3, 0.48, 0]], [0.098218, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.179436, [3, -0.08, 0], [3, 0.453333, 0]], [-0.1733, [3, -0.453333, 0], [3, 0.48, 0]], [-0.179436, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.092082, [3, -0.08, 0], [3, 0.453333, 0]], [-0.092082, [3, -0.453333, 0], [3, 0.48, 0]], [-0.092082, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[1.44345, [3, -0.08, 0], [3, 0.453333, 0]], [1.46646, [3, -0.453333, 0], [3, 0.48, 0]], [1.46339, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[0.199378, [3, -0.08, 0], [3, 0.453333, 0]], [1.26091, [3, -0.453333, 0], [3, 0.48, 0]], [0.217786, [3, -0.48, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.2, 1.56, 3])
    keys.append([[0.121144, [3, -0.08, 0], [3, 0.453333, 0]], [0.11961, [3, -0.453333, 0], [3, 0.48, 0]], [0.121144, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.2, 1.56, 3])
    keys.append([[0.0997519, [3, -0.08, 0], [3, 0.453333, 0]], [0.090548, [3, -0.453333, 0], [3, 0.48, 0]], [0.0997519, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[0.11049, [3, -0.08, 0], [3, 0.453333, 0]], [0.11049, [3, -0.453333, 0], [3, 0.48, 0]], [0.11049, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[0.412688, [3, -0.08, 0], [3, 0.453333, 0]], [0.0537319, [3, -0.453333, 0], [3, 0.48, 0]], [0.395814, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.2, 1.56, 3])
    keys.append([[1.18114, [3, -0.08, 0], [3, 0.453333, 0]], [1.18267, [3, -0.453333, 0], [3, 0.48, 0]], [1.18114, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.2, 1.56, 3])
    keys.append([[0.2936, [3, -0.08, 0], [3, 0.453333, 0]], [0.2876, [3, -0.453333, 0], [3, 0.48, 0]], [0.2936, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[0.124212, [3, -0.08, 0], [3, 0.453333, 0]], [0.122678, [3, -0.453333, 0], [3, 0.48, 0]], [0.124212, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.0705221, [3, -0.08, 0], [3, 0.453333, 0]], [-0.0674541, [3, -0.453333, 0], [3, 0.48, 0]], [-0.0705221, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.179436, [3, -0.08, 0], [3, 0.453333, 0]], [-0.1733, [3, -0.453333, 0], [3, 0.48, 0]], [-0.179436, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.0889301, [3, -0.08, 0], [3, 0.453333, 0]], [-0.0904641, [3, -0.453333, 0], [3, 0.48, 0]], [-0.0889301, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.2, 1.56, 3])
    keys.append([[1.45427, [3, -0.08, 0], [3, 0.453333, 0]], [1.45888, [3, -0.453333, 0], [3, 0.48, 0]], [1.45427, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.2, 1.56, 3])
    keys.append([[-0.204064, [3, -0.08, 0], [3, 0.453333, 0]], [-1.26866, [3, -0.453333, 0], [3, 0.48, 0]], [-0.224006, [3, -0.48, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.2, 1.56, 3])
    keys.append([[0.076658, [3, -0.08, 0], [3, 0.453333, 0]], [0.075124, [3, -0.453333, 0], [3, 0.48, 0]], [0.076658, [3, -0.48, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def squat(motionProxy):
    # Choregraphe bezier export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.170316, [3, -0.746667, 0], [3, 1.12, 0]], [-0.518534, [3, -1.12, 0], [3, 1.22667, 0]], [-0.191792, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.00157595, [3, -0.746667, 0], [3, 1.12, 0]], [-0.098218, [3, -1.12, 0], [3, 1.22667, 0]], [-0.0153821, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.082794, [3, -0.746667, 0], [3, 1.12, 0]], [-1.21804, [3, -1.12, 0], [3, 1.22667, 0]], [0.082794, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.12728, [3, -0.746667, 0], [3, 1.12, 0]], [-0.113474, [3, -1.12, 0], [3, 1.22667, 0]], [-0.124212, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.408002, [3, -0.746667, 0], [3, 1.12, 0]], [-0.839056, [3, -1.12, 0], [3, 1.22667, 0]], [-0.401866, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-1.17815, [3, -0.746667, 0], [3, 1.12, 0]], [-1.20116, [3, -1.12, 0], [3, 1.22667, 0]], [-1.18276, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.2944, [3, -0.746667, 0], [3, 1.12, 0]], [0.4364, [3, -1.12, 0], [3, 1.22667, 0]], [0.3028, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.119694, [3, -0.746667, 0], [3, 1.12, 0]], [-0.920358, [3, -1.12, 0], [3, 1.22667, 0]], [0.121228, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.150374, [3, -0.746667, 0], [3, 1.12, 0]], [0.020944, [3, -1.12, 0], [3, 1.22667, 0]], [0.139636, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.162562, [3, -0.746667, 0], [3, 1.12, 0]], [-0.214676, [3, -1.12, 0], [3, 1.22667, 0]], [-0.151824, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.0997519, [3, -0.746667, 0], [3, 1.12, 0]], [2.15523, [3, -1.12, 0], [3, 1.22667, 0]], [-0.09515, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[1.45726, [3, -0.746667, 0], [3, 1.12, 0]], [0.377322, [3, -1.12, 0], [3, 1.22667, 0]], [1.44652, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.214718, [3, -0.746667, 0], [3, 1.12, 0]], [-0.046062, [3, -1.12, 0], [3, 1.22667, 0]], [0.228524, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.076658, [3, -0.746667, 0], [3, 1.12, 0]], [-0.544612, [3, -1.12, 0], [3, 1.22667, 0]], [0.0628521, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.092082, [3, -0.746667, 0], [3, 1.12, 0]], [-1.20722, [3, -1.12, 0], [3, 1.22667, 0]], [0.098218, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.131966, [3, -0.746667, 0], [3, 1.12, 0]], [0.00771189, [3, -1.12, 0], [3, 1.22667, 0]], [0.130432, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.406552, [3, -0.746667, 0], [3, 1.12, 0]], [0.598302, [3, -1.12, 0], [3, 1.22667, 0]], [0.403484, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([2.2, 5.56, 9.24])
    keys.append([[1.19341, [3, -0.746667, 0], [3, 1.12, 0]], [1.26704, [3, -1.12, 0], [3, 1.22667, 0]], [1.20108, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.3004, [3, -0.746667, 0], [3, 1.12, 0]], [0.3004, [3, -1.12, 0], [3, 1.22667, 0]], [0.3004, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.116542, [3, -0.746667, 0], [3, 1.12, 0]], [-0.889762, [3, -1.12, 0], [3, 1.22667, 0]], [0.124212, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.139552, [3, -0.746667, 0], [3, 1.12, 0]], [0.019984, [3, -1.12, 0], [3, 1.22667, 0]], [-0.115008, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.162562, [3, -0.746667, 0], [3, 1.12, 0]], [-0.214676, [3, -1.12, 0], [3, 1.22667, 0]], [-0.151824, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.0935321, [3, -0.746667, 0], [3, 1.12, 0]], [2.14151, [3, -1.12, 0], [3, 1.22667, 0]], [-0.0966001, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([2.2, 5.56, 9.24])
    keys.append([[1.44814, [3, -0.746667, 0], [3, 1.12, 0]], [0.24088, [3, -1.12, 0], [3, 1.22667, 0]], [1.43126, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([2.2, 5.56, 9.24])
    keys.append([[-0.219404, [3, -0.746667, 0], [3, 1.12, 0]], [0.0168321, [3, -1.12, 0], [3, 1.22667, 0]], [-0.222472, [3, -1.22667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([2.2, 5.56, 9.24])
    keys.append([[0.076658, [3, -0.746667, 0], [3, 1.12, 0]], [0.099668, [3, -1.12, 0], [3, 1.22667, 0]], [0.076658, [3, -1.22667, 0], [3, 0, 0]]])

    try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # motion = ALProxy("ALMotion", IP, 9559)
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def jumping_jack(motionProxy):
    # Choregraphe bezier export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.170316, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.239346, [3, -0.426667, 0.0181316], [3, 0.56, -0.0237977]], [-0.296104, [3, -0.56, 0], [3, 0.52, 0]], [-0.253152, [3, -0.52, -0.0141162], [3, 0.666667, 0.0180978]], [-0.199462, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.00157595, [3, -0.333333, 0], [3, 0.426667, 0]], [0.0183661, [3, -0.426667, 0], [3, 0.56, 0]], [-0.105888, [3, -0.56, 0], [3, 0.52, 0]], [-0.00310993, [3, -0.52, 0], [3, 0.666667, 0]], [-0.00310993, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.082794, [3, -0.333333, 0], [3, 0.426667, 0]], [0.0889301, [3, -0.426667, 0], [3, 0.56, 0]], [0.0889301, [3, -0.56, 0], [3, 0.52, 0]], [0.0966001, [3, -0.52, 0], [3, 0.666667, 0]], [0.075124, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.12728, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.130348, [3, -0.426667, 0], [3, 0.56, 0]], [-0.130348, [3, -0.56, 0], [3, 0.52, 0]], [-0.128814, [3, -0.52, 0], [3, 0.666667, 0]], [-0.128814, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.408002, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.0183661, [3, -0.426667, 0], [3, 0.56, 0]], [-0.958708, [3, -0.56, 0], [3, 0.52, 0]], [-0.030638, [3, -0.52, 0], [3, 0.666667, 0]], [-0.400332, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-1.17815, [3, -0.333333, 0], [3, 0.426667, 0]], [0.713268, [3, -0.426667, 0], [3, 0.56, 0]], [-0.0521979, [3, -0.56, 0], [3, 0.52, 0]], [0.696394, [3, -0.52, 0], [3, 0.666667, 0]], [-1.16281, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.2944, [3, -0.333333, 0], [3, 0.426667, 0]], [0.324, [3, -0.426667, 0], [3, 0.56, 0]], [0.3112, [3, -0.56, 0], [3, 0.52, 0]], [0.3112, [3, -0.52, 0], [3, 0.666667, 0]], [0.3012, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.119694, [3, -0.333333, 0], [3, 0.426667, 0]], [0.11816, [3, -0.426667, 0], [3, 0.56, 0]], [0.11816, [3, -0.56, 0], [3, 0.52, 0]], [0.119694, [3, -0.52, 0], [3, 0.666667, 0]], [0.119694, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.150374, [3, -0.333333, 0], [3, 0.426667, 0]], [0.158044, [3, -0.426667, 0], [3, 0.56, 0]], [0.151908, [3, -0.56, 0], [3, 0.52, 0]], [0.153442, [3, -0.52, 0], [3, 0.666667, 0]], [0.153442, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.162562, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.162562, [3, -0.426667, 0], [3, 0.56, 0]], [-0.162562, [3, -0.56, 0], [3, 0.52, 0]], [-0.159494, [3, -0.52, 0], [3, 0.666667, 0]], [-0.170232, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.0997519, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.0828779, [3, -0.426667, 0], [3, 0.56, 0]], [-0.0844119, [3, -0.56, 0], [3, 0.52, 0]], [-0.07214, [3, -0.52, 0], [3, 0.666667, 0]], [-0.10282, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[1.45726, [3, -0.333333, 0], [3, 0.426667, 0]], [-1.50183, [3, -0.426667, 0.0455816], [3, 0.56, -0.0598259]], [-1.56165, [3, -0.56, 0], [3, 0.52, 0]], [-1.47575, [3, -0.52, -0.0859041], [3, 0.666667, 0.110134]], [1.42811, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.214718, [3, -0.333333, 0], [3, 0.426667, 0]], [1.14586, [3, -0.426667, 0], [3, 0.56, 0]], [0.285282, [3, -0.56, 0], [3, 0.52, 0]], [1.13052, [3, -0.52, 0], [3, 0.666667, 0]], [0.223922, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.076658, [3, -0.333333, 0], [3, 0.426667, 0]], [-1.20423, [3, -0.426667, 0.202196], [3, 0.56, -0.265382]], [-1.46961, [3, -0.56, 0], [3, 0.52, 0]], [-1.17048, [3, -0.52, -0.221379], [3, 0.666667, 0.283819]], [0.0459781, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.092082, [3, -0.333333, 0], [3, 0.426667, 0]], [0.09515, [3, -0.426667, 0], [3, 0.56, 0]], [0.090548, [3, -0.56, 0], [3, 0.52, 0]], [0.093616, [3, -0.52, 0], [3, 0.666667, 0]], [0.093616, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.131966, [3, -0.333333, 0], [3, 0.426667, 0]], [0.131966, [3, -0.426667, 0], [3, 0.56, 0]], [0.131966, [3, -0.56, 0], [3, 0.52, 0]], [0.135034, [3, -0.52, 0], [3, 0.666667, 0]], [0.135034, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.406552, [3, -0.333333, 0], [3, 0.426667, 0]], [0.016916, [3, -0.426667, 0], [3, 0.56, 0]], [1.00941, [3, -0.56, 0], [3, 0.52, 0]], [0.0276539, [3, -0.52, 0], [3, 0.666667, 0]], [0.397348, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[1.19341, [3, -0.333333, 0], [3, 0.426667, 0]], [0.757754, [3, -0.426667, 0.0917636], [3, 0.56, -0.12044]], [0.5568, [3, -0.56, 0], [3, 0.52, 0]], [0.774628, [3, -0.52, -0.0909714], [3, 0.666667, 0.11663]], [1.1796, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.3004, [3, -0.333333, 0], [3, 0.426667, 0]], [0.3476, [3, -0.426667, 0], [3, 0.56, 0]], [0.3388, [3, -0.56, 0], [3, 0.52, 0]], [0.3432, [3, -0.52, 0], [3, 0.666667, 0]], [0.3096, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.116542, [3, -0.333333, 0], [3, 0.426667, 0]], [0.122678, [3, -0.426667, 0], [3, 0.56, 0]], [0.11961, [3, -0.56, 0], [3, 0.52, 0]], [0.12728, [3, -0.52, 0], [3, 0.666667, 0]], [0.11194, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.139552, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.156426, [3, -0.426667, 0.00233749], [3, 0.56, -0.00306796]], [-0.159494, [3, -0.56, 0], [3, 0.52, 0]], [-0.147222, [3, -0.52, 0], [3, 0.666667, 0]], [-0.147222, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.162562, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.162562, [3, -0.426667, 0], [3, 0.56, 0]], [-0.162562, [3, -0.56, 0], [3, 0.52, 0]], [-0.159494, [3, -0.52, 0], [3, 0.666667, 0]], [-0.170232, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.0935321, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.0889301, [3, -0.426667, -0.000884461], [3, 0.56, 0.00116086]], [-0.0873961, [3, -0.56, -0.000530266], [3, 0.52, 0.00049239]], [-0.0858622, [3, -0.52, 0], [3, 0.666667, 0]], [-0.099668, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[1.44814, [3, -0.333333, 0], [3, 0.426667, 0]], [-0.684122, [3, -0.426667, 0.407077], [3, 0.56, -0.534288]], [-1.37596, [3, -0.56, 0], [3, 0.52, 0]], [-0.639636, [3, -0.52, -0.409371], [3, 0.666667, 0.524835]], [1.42666, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[-0.219404, [3, -0.333333, 0], [3, 0.426667, 0]], [-1.2073, [3, -0.426667, 0], [3, 0.56, 0]], [-0.200996, [3, -0.56, 0], [3, 0.52, 0]], [-1.19043, [3, -0.52, 0], [3, 0.666667, 0]], [-0.230142, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.96, 2.24, 3.92, 5.48, 7.48])
    keys.append([[0.076658, [3, -0.333333, 0], [3, 0.426667, 0]], [0.604354, [3, -0.426667, 0], [3, 0.56, 0]], [0.54146, [3, -0.56, 0], [3, 0.52, 0]], [0.573674, [3, -0.52, 0], [3, 0.666667, 0]], [0.099668, [3, -0.666667, 0], [3, 0, 0]]])

    try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # motion = ALProxy("ALMotion", IP, 9559)
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def arms_up(motionProxy):
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
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def fist_pump(motionProxy):
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
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def front_flex(motionProxy):
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
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def push_up(motionProxy):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.00762796, [3, -0.36, 0], [3, 0.333333, 0]], [0.00762796, [3, -0.333333, 0], [3, 0.306667, 0]], [0.0137641, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.00149202, [3, -0.36, 0], [3, 0.333333, 0]], [0.00149202, [3, -0.333333, 0], [3, 0.306667, 0]], [0.00149202, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.00762796, [3, -0.36, 0], [3, 0.333333, 0]], [-0.357464, [3, -0.333333, 0], [3, 0.306667, 0]], [0.00302601, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.00771189, [3, -0.36, 0], [3, 0.333333, 0]], [0.00771189, [3, -0.333333, 0], [3, 0.306667, 0]], [4.19617e-05, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.0659201, [3, -0.36, 0], [3, 0.333333, 0]], [-1.41124, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.05825, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.0291879, [3, -0.36, 0], [3, 0.333333, 0]], [-1.32849, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.046062, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.0144, [3, -0.36, 0], [3, 0.333333, 0]], [0.268, [3, -0.333333, 0], [3, 0.306667, 0]], [0.0292, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[4.19617e-05, [3, -0.36, 0], [3, 0.333333, 0]], [-0.447886, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.00609398, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00149202, [3, -0.36, 0], [3, 0.333333, 0]], [-0.00149202, [3, -0.333333, 0], [3, 0.306667, 0]], [0.024586, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00302601, [3, -0.36, 0], [3, 0.333333, 0]], [0.00771189, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.00609398, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00924587, [3, -0.36, 0], [3, 0.333333, 0]], [0.705598, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.00771189, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.082794, [3, -0.36, 0], [3, 0.333333, 0]], [1.19034, [3, -0.333333, 0], [3, 0.306667, 0]], [0.168698, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-4.19617e-05, [3, -0.36, 0], [3, 0.333333, 0]], [1.22409, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.00310993, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.01845, [3, -0.36, 0], [3, 0.333333, 0]], [0.11194, [3, -0.333333, 0], [3, 0.306667, 0]], [0.00302601, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.0061779, [3, -0.36, 0], [3, 0.333333, 0]], [-0.351244, [3, -0.333333, 0], [3, 0.306667, 0]], [4.19617e-05, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00609398, [3, -0.36, 0], [3, 0.333333, 0]], [-0.00609398, [3, -0.333333, 0], [3, 0.306667, 0]], [0.00157595, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.07214, [3, -0.36, 0], [3, 0.333333, 0]], [1.53097, [3, -0.333333, 0], [3, 0.306667, 0]], [0.0583339, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.029104, [3, -0.36, 0], [3, 0.333333, 0]], [0.736278, [3, -0.333333, 0], [3, 0.306667, 0]], [0.0429101, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.0112, [3, -0.36, 0], [3, 0.333333, 0]], [0.0108, [3, -0.333333, 0], [3, 0.306667, 0]], [0.02, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-4.19617e-05, [3, -0.36, 0], [3, 0.333333, 0]], [-0.446436, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.0061779, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.00310993, [3, -0.36, 0], [3, 0.333333, 0]], [0.00310993, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.02757, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00302601, [3, -0.36, 0], [3, 0.333333, 0]], [0.00771189, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.00609398, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00609398, [3, -0.36, 0], [3, 0.333333, 0]], [0.70875, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.0122299, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.0890141, [3, -0.36, 0], [3, 0.333333, 0]], [0.7471, [3, -0.333333, 0], [3, 0.306667, 0]], [0.181054, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1.04, 2.04, 2.96])
    keys.append([[0.00455999, [3, -0.36, 0], [3, 0.333333, 0]], [-1.15514, [3, -0.333333, 0], [3, 0.306667, 0]], [-0.00157595, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.04, 2.04, 2.96])
    keys.append([[-0.00924587, [3, -0.36, 0], [3, 0.333333, 0]], [-0.0153821, [3, -0.333333, 0], [3, 0.306667, 0]], [0.00762796, [3, -0.306667, 0], [3, 0, 0]]])

    try:
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err

def get_mood(moodProxy):
    emotion = moodProxy.getEmotionalReaction()
    return emotion

def wake_up(motionProxy):
    motionProxy.wakeUp()

def rest(motionProxy):
    motionProxy.rest()

def main(IP, port, movement, speech, mood):
    motionProxy = ALProxy("ALMotion", IP, port)
    speechProxy = ALProxy("ALTextToSpeech", IP, port)
    moodProxy = ALProxy("ALMood", IP, port)
    # autonomousProxy = ALProxy("ALAutonomousProxy", IP, port)

    # autonomousProxy.setState("safeguard")

    if speech!=None:
        speechProxy.say(speech)    
    
    if movement=="lat_raise":
        lat_raise(motionProxy)
    elif movement=="squat":
        squat(motionProxy)
    elif movement=="jumping_jack":
        jumping_jack(motionProxy)
    elif movement=="wake_up":
        wake_up(motionProxy)
    elif movement=="rest":
        rest(motionProxy)
    elif movement=="push_up":
        push_up(motionProxy)
    elif movement=="fist_pump":
        fist_pump(motionProxy)
    elif movement=="front_flex":
        front_flex(motionProxy)
    elif movement=="arms_up":
        arms_up(motionProxy)
    
    if mood:
        return get_mood(moodProxy)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.146",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--movement", type=str, default=None)
    parser.add_argument("--speech", type=str, default=None)
    parser.add_argument("--mood", type=bool, default=False)

    args = parser.parse_args()
    main(args.ip, args.port, args.movement, args.speech, args.mood)