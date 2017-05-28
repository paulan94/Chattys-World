import MalmoPython
import os
import sys
import time
from itertools import chain
from nltk.corpus import wordnet
#A class that defines our movements based on the format
#The command should be based off the following:
#        Action + adverb + noun
def isInt(s):
    '''
    check to see if possible to convert to an int
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False

def getSynonyms(text):
    '''
    Returns a set of synonyms through the use of nltk
    '''
    synonyms = wordnet.synsets(text)
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    return lemmas

commandDict={ 'move': getSynonyms('move'),
    'strafe': getSynonyms('strafe'),
    'pitch': getSynonyms('pitch'),
    'turn': getSynonyms('turn'),
    'jump': getSynonyms('jump'),
    'crouch': getSynonyms('crouch'),
    'attack': getSynonyms('attack'),
    'use': getSynonyms('use'),
    'stop': getSynonyms('stop')
    }
class switcherCommand:


    def __init__(self, agent_host):
        self.agent_host = agent_host
        self.commandList = []
        self.crouchStatus = False
        self.validFirstWord = False

    def setCommandList(commandList):
        self.commandList = commandList

    def interpretCommand(self):
        '''
        Alternates between commands first string in command:ist
        Executes method in dictionary
        '''
        commandWord = 'stop'
        for key, value in commandDict.iteritems():
            if self.commandList[0] in value:
                commandWord = key
                self.validFirstWord = True
        print(commandWord)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, commandWord, lambda: "nothing")
        # Call the method as we return it
        return method();

    def stop(self):
        #Command: "stop"
        #Forces agent to stop all continous actions
        self.agent_host.sendCommand("move 0")
        self.agent_host.sendCommand("strafe 0")
        self.agent_host.sendCommand("pitch 0")
        self.agent_host.sendCommand("turn 0")
        self.agent_host.sendCommand("jump 0")
        self.agent_host.sendCommand("crouch 0")
        self.agent_host.sendCommand("attack 0")
        self.agent_host.sendCommand("use 0")
        return

    def move(self):
        """
        walk command:
        'walk' - continously walk at speed 1
        'walk 10' - continously walk at 10x speed
        """
        print(self.commandList)
        #Make agent walk, speed varies based on speed parameter
        if (len(self.commandList) == 1):
            self.agent_host.sendCommand("move 1")
        # else:
        #     self.agent_host.sendCommand("move " + self.commandList[1])
        return

    #TODO: finish a discrete movement command

    def strafe(self):
        '''
        Send command to strafe around
        '''
        if (len(self.commandList) == 2 and self.commandList[1] == "right"):
            self.agent_host.sendCommand("strafe 1")
        elif(len(self.commandList) == 2 and self.commandList[1] == "left"):
            self.agent_host.sendCommand("strafe -1")
        return

    def pitch(self):
        '''
        pitch command for discrete or continous movement

        For the given commands:
        "pitch" = looks up down and back at the same angle
        "pitch {up/down} {degrees}" = pitches up or down based on varying degrees

        '''
        if len(self.commandList) == 1:
            self.agent_host.sendCommand("pitch 1")
            time.sleep(1)
            self.agent_host.sendCommand("pitch 0")
            time.sleep(.25)
            self.agent_host.sendCommand("pitch -1")
            time.sleep(1)
            self.agent_host.sendCommand("pitch 0")
            time.sleep(.25)
            self.agent_host.sendCommand("pitch 1")
            time.sleep(.5)
            self.agent_host.sendCommand("pitch 0")
        elif (self.commandList[1] == "up"):
            #command to look up
            if(len(self.commandList) == 2):
                self.agent_host.sendCommand("pitch -1")
            if(len(self.commandList) == 3 and isInt(self.commandList[2]) == True):
                #Agent turn speed is 180 degrees per second
                #Divide angle given by 180 to get specific angle
                self.agent_host.sendCommand("pitch -1")
                time.sleep(float(self.commandList[2])/ 180)
                self.agent_host.sendCommand("pitch 0")
        elif(self.commandList[1] == "down"):
            if(len(self.commandList) == 2):
                self.agent_host.sendCommand("pitch 1")
            if(len(self.commandList) == 3 and isInt(self.commandList[2]) == True):
                self.agent_host.sendCommand("pitch 1")
                time.sleep(float(self.commandList[2])/ 180)
                self.agent_host.sendCommand("pitch 0")

        return

    def turn(self):
        '''
        turn command used to turn agent
        "turn" agent turns to the right continously
        "turn" (right/left) (degrees) = agent turns to the left or right based on degrees
        '''
        if len(self.commandList) == 1:
            self.agent_host.sendCommand("turn 1")

        elif (self.commandList[1] == "right"):
            if(len(self.commandList) == 3 and isInt(self.commandList[2]) == True):
                self.agent_host.sendCommand("turn 1")
                time.sleep(float(self.commandList[2])/ 180)
                self.agent_host.sendCommand("turn 0")
            else:
                self.agent_host.sendCommand("turn 1")
                time.sleep(float(90)/180)
                self.agent_host.sendCommand("turn 0")

        elif(self.commandList[1] == "left"):
            if(len(self.commandList) == 3 and isInt(self.commandList[2]) == True):
                self.agent_host.sendCommand("turn -1")
                time.sleep(float(self.commandList[2])/ 180)
                self.agent_host.sendCommand("turn 0")
            else:
                self.agent_host.sendCommand("turn -1")
                time.sleep(float(90)/180)
                self.agent_host.sendCommand("turn 0")

        return

    def jump(self):
        '''
        Agent jump command:
        "jump" defaults to jump once
        "jump n": jumps n times

        '''
        #Defaults to jump once
        if(len(self.commandList) == 1):
            self.agent_host.sendCommand("jump 1")
            time.sleep(.5)
            self.agent_host.sendCommand("jump 0")

        #Appears to jump twice for every second. Can vary based on hardware
        elif(len(self.commandList)==2 and isInt(self.commandList[1])):

            self.agent_host.sendCommand("jump 1")
            if int(self.commandList[1]) > 5: #Appears to be a system lag if number of jump > 5
                time.sleep((float(self.commandList[1])/2)+.5)
            else:
                time.sleep(float(self.commandList[1])/2)
            self.agent_host.sendCommand("jump 0")
        return

    def crouch(self):
        '''
        Crouch command:
        "crouch": crouches/uncrouch depending on crouch status
        '''
        if(len(self.commandList) == 1):
            if(self.crouchStatus == False):
                self.agent_host.sendCommand("crouch 1")
                self.crouchStatus = True
            elif(self.crouchStatus == True):
                self.agent_host.sendCommand("crouch 0")
                self.crouchStatus = False

        return

    def attack(self):
        '''
        attack command:
        "attack": defaults to attack once
        "attack n": attack n times
        '''
        if (len(self.commandList) == 1):
            self.agent_host.sendCommand("attack 1")
        elif(len(self.commandList)==2 and isInt(self.commandList[1])):
            for i in range(int(self.commandList[1])):
                self.agent_host.sendCommand("attack 1")
                time.sleep(.5)
        return

    def use(self):
        return
