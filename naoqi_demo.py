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

def wake_up(motionProxy):
    motionProxy.wakeUp()

def rest(motionProxy):
    motionProxy.rest()

def main(IP, port, movement, speech):
    motionProxy = ALProxy("ALMotion", IP, port)
    speechProxy = ALProxy("ALTextToSpeech", IP, port)

    if speech!=None:
        speechProxy.say(speech)
    
    
    if movement=="latRaise":
        lat_raise(motionProxy)
    elif movement=="wakeUp":
        wake_up(motionProxy)
    elif movement=="rest":
        rest(motionProxy)


    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.147",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--movement", type=str, default=None)
    parser.add_argument("--speech", type=str, default=None)

    args = parser.parse_args()
    main(args.ip, args.port, args.movement, args.speech)