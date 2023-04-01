import time
import sys
import argparse


from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

HeadTouch = None
memory = None
touched = False

class HeadTouchModule(ALModule):
    def __init__(self, name):
        ALModule.__init__(self,name)
        self.tts = ALProxy("ALTextToSpeech")

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("MiddleTactilTouched", "HeadTouch", "onHeadTouch")

    def onHeadTouch(self, *_args):
        global touched

        touched = True
        memory.unsubscribeToEvent("MiddleTactilTouched", "HeadTouch")

def main():
    IP = "192.168.1.147"
    myBroker = ALBroker("myBroker", "0.0.0.0", 0, IP, 9559)

    global HeadTouch, touched
    HeadTouch = HeadTouchModule("HeadTouch")
    
    while True:
        time.sleep(1)
        if(touched):
            myBroker.shutdown()
            sys.exit(0)



if __name__ == "__main__":
    main()
