# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #1: Run simple mission

import MalmoPython
import os
import sys
import time
import random
import json
import math

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

items = {'red_flower':'flower',
         'apple':'apple',
         'iron_sword':'sword',
         'iron_pickaxe':'pickaxe',
         'diamond_sword':'sword'
         }

MOB_TYPE = "Pig"
spawn_end_tag = ' type="mob_spawner" variant="' + MOB_TYPE + '"/>'

obj_id = items.keys()[random.randint(0, len(items)-1)]

mission_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <About>
    <Summary>Name the first item you see.</Summary>
  </About>

  <ServerSection>
      <ServerInitialConditions>
            <Time>
                <StartTime>6000</StartTime>
                <AllowPassageOfTime>false</AllowPassageOfTime>
            </Time>
            <Weather>clear</Weather>
            <AllowSpawning>true</AllowSpawning>   <!-- CHANGED TO TRUE --> 
      </ServerInitialConditions>
    <ServerHandlers>
      <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1"/>
      <DrawingDecorator>
        <!-- coordinates for cuboid are inclusive -->
        <DrawCuboid x1="0" y1="46" z1="0" x2="10" y2="52" z2="7" type="grass" /> <!-- limits of our arena -->
        <DrawCuboid x1="1" y1="47" z1="1" x2="10" y2="52" z2="6" type="air" /> <!-- limits of our arena -->
        <DrawCuboid x1="1" y1="52" z1="1" x2="10" y2="51" z2="6" type="glowstone" />            <!-- limits of our arena -->
        <DrawCuboid x1="1" y1="48" z1="1" x2="1" y2="49" z2="3" ''' + spawn_end_tag + '''
        <DrawItem    x="4"   y="47"  z="2" type="'''+obj_id+'''" />
      </DrawingDecorator>
      <ServerQuitFromTimeUp timeLimitMs="300000"/>
      <ServerQuitWhenAnyAgentFinishes/>
    </ServerHandlers>
  </ServerSection>
  <AgentSection mode="Survival">
    <Name>Chatty</Name>
    <AgentStart>
      <Placement x="3" y="47.0" z="3" pitch="30" yaw="270"/>
    </AgentStart>
    <AgentHandlers>
      <ObservationFromFullStats/>
      <ObservationFromRay/>
      <ObservationFromNearbyEntities>
        <Range name="Entities" xrange="10" yrange="10" zrange="10"/>
      </ObservationFromNearbyEntities>
      <VideoProducer want_depth="false">
          <Width>640</Width>
          <Height>480</Height>
      </VideoProducer>
      <ContinuousMovementCommands/>
      <ChatCommands />
      <RewardForSendingCommand reward="-1"/>
    </AgentHandlers>
  </AgentSection>
</Mission>
'''
# <RewardForSendingMatchingChatMessage>
#   <ChatMatch reward="100.0" regex="'''+items[obj_id]+'''" description="Anything that matches the object."/>
# </RewardForSendingMatchingChatMessage>

# Create default Malmo objects:



agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

my_mission = MalmoPython.MissionSpec(mission_xml, True)
my_mission_record = MalmoPython.MissionRecordSpec("chat_reward.tgz")

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print "Error starting mission:",e
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print "Waiting for the mission to start ",
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission running ",


# Loop until mission ends:
while world_state.is_mission_running:
    str_command = raw_input()

    time.sleep(0.5)
    print "\nSending action: chat %s" % str_command
    agent_host.sendCommand("chat %s" % str_command)

    agent_host.sendCommand(str_command)


    #TODO: USE NLP TO CONVERT STR_COMMAND TEXT INTO VALID ACTION
    # action = str_command
    # action_list = []
    # if action in action_list:
    #     agent_host.sendCommand(str_command)
    # else:
    #     #if command not in list of functionality, print error
    #     agent_host.sendCommand("chat %s", "invalid move or unsupported function!")

    sys.stdout.write(".")

    world_state = agent_host.getWorldState()

    # print world_state.observations[-1].text
    #kill pig

    if len(world_state.observations) > 0:
        #JSON OBJECT: observation
        observation = json.loads(world_state.observations[-1].text)
        chatty = None
        closest_pig = None
        distanceToChattyFromPig = -999
        if 'Entities' in observation:
            entities = observation['Entities']
            pigList = []
            #get the pig and chatty entities
            #chatty is the user
            for ent in entities:
                if ent["name"] == 'Pig':
                    pigList.append(ent)
                if ent["name"] == "Chatty":
                    chatty = ent
            #if chatty is not None, get the x and z coordinates
            if chatty != None:
                chatty_x = chatty["x"]
                chatty_z = chatty["z"]
                # print chatty_x, chatty_z
                chatty_sum = chatty_x+chatty_z
                # print pigList[0]
                #TODO: change way to find shortest distance to pig
                distanceList = []
                #TODO: change this
                for pig in pigList:
                    pig_x = pig["x"]
                    pig_z = pig["z"]

                    # print "values are"
                    # print (chatty_x, chatty_z, pig_x, pig_z)
                    # x_distance = (abs(chatty_x - pig_x))**2
                    # print x_distance
                    # z_distance = (abs(chatty_z - pig_z))**2
                    # print z_distance
                    #distance formula to get distance from any pig to chatty
                    distanceToChattyFromPig = math.sqrt(abs((abs(chatty_x - pig_x)**2) - (abs(chatty_z - pig_z)**2)))
                    distanceList.append(distanceToChattyFromPig)

                print distanceList
                #Check if the pig's distance is the smallest one in distanceList, if true, set the pig to the closest.
                for pig in pigList:
                    pig_x = pig["x"]
                    pig_z = pig["z"]
                    distanceToChattyFromPig = math.sqrt(abs((abs(chatty_x - pig_x) ** 2) - (abs(chatty_z - pig_z) ** 2)))
                    if distanceToChattyFromPig == min(distanceList):
                        #set closest pig here.
                        closest_pig = pig
                        #stop checking the piglist
                        break
                        # print distanceToChattyFromPig
                        # print "closest"
                        # print closest_pig


        #ObsFromRay usage here
        #TODO: use the observation to possiobly get direction object is facing
        if 'LineOfSight' in observation:
            los = observation['LineOfSight']
            print chatty
            print closest_pig
            print distanceToChattyFromPig
            # print los["inRange"]
            # if the closest piggy is not in sight, use the coordinates to pitch and turn accordingly
            while (los["x"] != closest_pig["x"]) and los["z"] != closest_pig["z"]:
                chatty_x = chatty["x"]
                chatty_z = chatty["z"]
                closest_pig_x = closest_pig["x"]
                closest_pig_z = closest_pig["z"]

                agent_host.sendCommand("turn 0.5")
                time.sleep(1)
                agent_host.sendCommand("turn 0")

                agent_host.sendCommand("pitch -0.5")
                time.sleep(1)
                agent_host.sendCommand("pitch 0")

                agent_host.sendCommand("pitch 0.5")
                time.sleep(1)
                agent_host.sendCommand("pitch 0")

                #turn the other way
                agent_host.sendCommand("turn -0.5")
                time.sleep(2)
                agent_host.sendCommand("turn 0")

                agent_host.sendCommand("pitch -0.5")
                time.sleep(1)
                agent_host.sendCommand("pitch 0")

                agent_host.sendCommand("pitch 0.5")
                time.sleep(1)
                agent_host.sendCommand("pitch 0")
                time.sleep(1)

                if los["type"] == "Pig" and los["x"] == closest_pig_x:
                    print los["x"], closest_pig_x
                    print los["z"], closest_pig_z
                    break
                #do something with these coordinates
            if los["inRange"] and los["type"] == "Pig" and los["x"] == closest_pig["x"]:
                print "found the piggy, lets hit it"
                agent_host.sendCommand("attack 1")
                time.sleep(0.5)
                agent_host.sendCommand("attack 0")


        #     #TODO:while not in range, move to closest pig
        #     # print los["x"], los["z"], closest_pig["x"], closest_pig["x"]
        #     #if the object in line of sight has same x and z value as closest pig, we found the right one, if its in range,
        #     #kill IT!!!!
        #     if (los["x"] == closest_pig["x"]) and los["z"] == closest_pig["z"]:
        #         print "found the closest piggy"
        #         if los["inRange"] and los["type"] == "Pig":
        #             agent_host.sendCommand("attack 1")
        #             time.sleep(0.5)
        #             agent_host.sendCommand("attack 0")
        #         else:
        #             pass

            #TODO: pan until we find closest pig in line of sight and until it is in range, move toward it


    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission ended"
# Mission has ended.

