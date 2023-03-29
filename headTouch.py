import time
import sys
import argparse


from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

HeadTouch = None
memory = None

class HeadTouchModule(ALModule):
    def __init__(self, name):
        ALModule.__init__(self,name)
        self.tts = ALProxy("ALTextToSpeech")

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("MiddleTactilTouched", "HeadTouch", "onHeadTouch")

    def onHeadTouch(self, *_args):
        memory.unsubscribeToEvent("MiddleTactilTouched", "HeadTouch")

        self.tts.say("Hello! Let's start with some lateral raises!")
        memory.subscribeToEvent("MiddleTactilTouched", "HeadTouch", "onHeadTouch")

def run():
    while True:
        time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

def main():
    IP = "192.168.1.147"
    myBroker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559)

    global HeadTouch
    HeadTouch = HeadTouchModule("HeadTouch")
    run()



if __name__ == "__main__":
    main()
