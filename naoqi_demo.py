from naoqi import ALProxy 

print("test")

IP = "192.168.1.147"
tts = ALProxy("ALTextToSpeech", IP, 9559)


# Example: Sends a string to the text-to-speech module
tts.say("Hello World!")