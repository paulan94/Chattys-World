import MalmoPython
import os
import sys
import time

def base_command(command_list):
    '''
    Base command for all implementation
    The command should be based off the following:
            Action + adverb + noun
    Given actions are move|strafe|pitch|turn|jump|crouch|attack|use|stop
    '''



def force_stop(agent_host):
    #Command: "stop"
    #Forces agent to stop all continous actions
    agent_host.sendCommand("move 0")
    agent_host.sendCommand("strafe 0")
    agent_host.sendCommand("pitch 0")
    agent_host.sendCommand("turn 0")
    agent_host.sendCommand("jump 0")
    agent_host.sendCommand("crouch 0")
    agent_host.sendCommand("attack 0")
    agent_host.sendCommand("use 0")
    return

def walk(agent_host, speed=0):
    """
    walk command:
    'walk' - continously walk at speed 1
    'walk 10' - continously walk at 10x speed
    """
    #Make agent walk, speed varies based on speed parameter
    if (speed == 0):
        agent_host.sendCommand("move 1")
    else:
        agent_host.sendCommand("move " + str(speed))
    return

def stop_walk(agent_host):
    """
    simply stop agent from walking
    not necessary tbh
    """
    #stop agent from walking
    agent_host.sendCommand("move 0")
    return

def walk_step(agent_host, steps):
    """
    walk command:
    'walk 10' - agent walks 10 steps
    """
    #Get agent to walk discrete steps
    #Time.sleep is called to allow agent to walk a single step
    steps = int(steps)
    for i in range(steps):
        agent_host.sendCommand("move 1")
        time.sleep(0.25)
        agent_host.sendCommand("move 0")
    return

def strafe(agent_host, direction=.5):
    """
    strafe command:
    'strafe right' - agent continously strafes in given direction
    """
    #Agent strafes: 1 = right, -1 = left
    #autos as right turn
    agent_host.sendCommand("strafe " + str(direction))
    return

def turn(agent_host, direction=1, angle=0):
    '''
    turn command: - used to turn agent discrete or continously
    'turn' - agent turns to the right continously
    'turn right 90' - agent turns to the right 90 degrees
    '''
    #Agent turns based off direction
    #If no direction given, autos at 1
    #Current turnDegSpeed is 180
    if angle == 0:
        agent_host.sendCommand("turn " + str(direction))
    else:
        agent_host.sendCommand("turn " + str(direction))
        #Agent turn speed is 180 degrees per second
        #Divide angle given by 180 to get specific angle
        time.sleep(angle/180)
        agent_host.sendCommand("turn 0")
    return

def pitch(agent_host, direction=1, angle=0):
    '''
    pitch command - used to pitch agent discrete/continously
    "pitch up 90" - agen pitches up by 90 degrees
    '''
    #Agent turns based off direction
    #If no direction given, autos at 1
    #Current turnDegSpeed is 180
    if angle == 0:
        #Used with "pitch" command
        #Used to test mobility
        agent_host.sendCommand("pitch 1")
        time.sleep(1)
        agent_host.sendCommand("pitch 0")
        time.sleep(.25)
        agent_host.sendCommand("pitch -1")
        time.sleep(1)
        agent_host.sendCommand("pitch 0")
        time.sleep(.25)
        agent_host.sendCommand("pitch 1")
        time.sleep(.5)
        agent_host.sendCommand("pitch 0")


    else:
        agent_host.sendCommand("pitch " + str(direction))
        #Agent turn speed is 180 degrees per second
        #Divide angle given by 180 to get specific angle
        time.sleep(angle/180)
        agent_host.sendCommand("pitch 0")
    return

def jump(agent_host):
    #used to get agent to jump
    agent_host.sendCommand("jump 1")
    time.sleep(.5)
    agent_host.sendCommand("jump 0")
