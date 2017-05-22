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
import text_movement

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

items = {'red_flower':'flower',
         'apple':'apple',
         'iron_sword':'sword',
         'iron_pickaxe':'pickaxe',
         'diamond_sword':'sword'
         }

#MOB_TYPE = "Pig"
#spawn_end_tag = ' type="mob_spawner" variant="' + MOB_TYPE + '"/>'

#obj_id = items.keys()[random.randint(0, len(items)-1)]

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
       <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" forceReset="true"/>
        <DrawingDecorator>
            <!-- coordinates for cuboid are inclusive -->
            <!--floor-->
            <DrawCuboid x1="0" y1="40" z1="0" x2="76" y2="50" z2="76" type="grass" /> <!-- limits of our arena -->
            
            <DrawCuboid x1="9" y1="40" z1="0" x2="9" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="19" y1="40" z1="0" x2="19" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="28" y1="40" z1="0" x2="28" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="32" y1="40" z1="0" x2="32" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="38" y1="40" z1="0" x2="38" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="45" y1="40" z1="0" x2="45" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="57" y1="40" z1="0" x2="57" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="66" y1="40" z1="0" x2="66" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="38" x2="76" y2="40" z2="38" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="32" x2="76" y2="40" z2="32" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="9" x2="76" y2="40" z2="9" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="19" x2="76" y2="40" z2="19" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="57" x2="76" y2="40" z2="57" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="66" x2="76" y2="40" z2="66" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="28" x2="76" y2="40" z2="28" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="45" x2="76" y2="40" z2="45" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="0" x2="76" y2="40" z2="0" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="76" x2="76" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="0" y1="40" z1="0" x2="0" y2="40" z2="76" type="glowstone" />
            <DrawCuboid x1="76" y1="40" z1="0" x2="76" y2="40" z2="76" type="glowstone" />
            
            <!--water and lava-->
            <DrawCuboid x1="67" y1="40" z1="1" x2="75" y2="50" z2="8" type="water" /> 
            <DrawCuboid x1="1" y1="40" z1="67" x2="8" y2="50" z2="75" type="lava" /> 
            
            
            <!--air-->
            <DrawCuboid x1="0" y1="41" z1="0" x2="76" y2="50" z2="76" type="air" /> <!-- limits of our arena -->
           
            <!--ceiling-->
            <DrawCuboid x1="0" y1="50" z1="0" x2="76" y2="50" z2="76" type="glowstone" />            <!-- limits of our arena -->   
              <!--house-->
            <DrawBlock type="planks" x="71" y="41" z="70"/>
            <DrawBlock type="planks" x="71" y="41" z="72"/>
            <DrawBlock type="planks" x="70" y="41" z="70"/>
            <DrawBlock type="planks" x="70" y="41" z="72"/>
            <DrawBlock type="planks" x="72" y="41" z="70"/>
            <DrawBlock type="planks" x="72" y="41" z="71"/>
            <DrawBlock type="planks" x="72" y="41" z="72"/>
          
            <DrawBlock type="planks" x="71" y="42" z="70"/>
            <DrawBlock type="planks" x="71" y="42" z="72"/>
            <DrawBlock type="planks" x="70" y="42" z="70"/>
            <DrawBlock type="planks" x="70" y="42" z="72"/>
            <DrawBlock type="planks" x="72" y="42" z="70"/>
            <DrawBlock type="planks" x="72" y="42" z="71"/>
            <DrawBlock type="planks" x="72" y="42" z="72"/>        
          
            <DrawBlock type="planks" x="71" y="43" z="70"/>
            <DrawBlock type="planks" x="71" y="43" z="71"/>
            <DrawBlock type="planks" x="71" y="43" z="72"/>
            <DrawBlock type="planks" x="70" y="43" z="70"/>
            <DrawBlock type="planks" x="70" y="43" z="71"/>
            <DrawBlock type="planks" x="70" y="43" z="72"/>
            <DrawBlock type="planks" x="72" y="43" z="70"/>
            <DrawBlock type="planks" x="72" y="43" z="71"/>
            <DrawBlock type="planks" x="72" y="43" z="72"/>
          
            <DrawBlock type="planks" x="71" y="44" z="71"/>
            
            <!-- place mobs -->
            <DrawEntity x="20"  y="41" z="20" type="Pig" />
            <DrawEntity x="2"  y="41" z="25" type="Cow" />
            <DrawEntity x="25"  y="41" z="2" type="Chicken" />
            
            <!--spawners-->
            <DrawCuboid x1="29" y1="40" z1="29" x2="29" y2="40" z2="29" type="mob_spawner" variant="Pig"/>
            <DrawCuboid x1="31" y1="40" z1="31" x2="31" y2="40" z2="31" type="mob_spawner" variant="Chicken"/>
            <DrawCuboid x1="29" y1="40" z1="31" x2="29" y2="40" z2="31" type="mob_spawner" variant="Cow"/>
            <DrawCuboid x1="31" y1="40" z1="29" x2="31" y2="40" z2="29" type="mob_spawner" variant="Sheep"/>

        </DrawingDecorator>
      <ServerQuitFromTimeUp timeLimitMs="300000"/>
      <ServerQuitWhenAnyAgentFinishes/>
    </ServerHandlers>
  </ServerSection>
  <AgentSection mode="Survival">
    <Name>Chatty</Name>
    <AgentStart>
      <Placement x="4" y="43" z="4" pitch="30" yaw="270"/>
      <Inventory>
        <InventoryItem slot="0" type="diamond_pickaxe"/>
        <InventoryItem slot="1" type="diamond_sword"/>
      </Inventory>
    </AgentStart>
    <AgentHandlers>
      <DiscreteMovementCommands/>
      <!--ContinuousMovementCommands turnSpeedDegs="180"/-->
      <AbsoluteMovementCommands/>
      <!--ObservationFromFullStats/-->
      <ObservationFromRay/>
      <ObservationFromNearbyEntities>
        <Range name="Entities" xrange="75" yrange="10" zrange="75"/>
      </ObservationFromNearbyEntities>
      <!--InventoryCommands/-->
      <!--RewardForSendingCommand reward="-1"/-->
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

def get_chatty(observation):
    if 'Entities' in observation:
        entities = observation["Entities"]
        for ent in entities:
            if ent["name"] == "Chatty":
                chatty = ent
    return chatty

def find_closest_pig(observation, chatty):
    distanceToChattyFromPig = -999

    if 'Entities' in observation:
        entities = observation['Entities']
        pigList = []
        # get the pig and chatty entities
        # chatty is the user
        for ent in entities:
            if ent["name"] == 'Pig':
                pigList.append(ent)
        # if chatty is not None, get the x and z coordinates
        if chatty != None:
            chatty_x = chatty["x"]
            chatty_z = chatty["z"]
            distanceList = []

            for pig in pigList:
                pig_x = pig["x"]
                pig_z = pig["z"]

                # distance formula to get distance from any pig to chatty
                distanceToChattyFromPig = math.sqrt(abs((abs(chatty_x - pig_x) ** 2) + (abs(chatty_z - pig_z) ** 2)))
                distanceList.append(distanceToChattyFromPig)
                if distanceToChattyFromPig == min(distanceList):
                    closest_pig = pig

    return closest_pig

def tester(pig, chatty):

        # distance formula to get distance from any pig to chatty
    distance = math.sqrt(abs((abs(chatty["x"] - pig["x"]) ** 2) + (abs(chatty["z"] - pig["z"]) ** 2)))
    return distance

def found_pig(los_type, los_x, closest_pig_x):
    return ((los_type == "Pig") and (los_x == closest_pig_x))

def piggy_in_range(in_range, los_type, los_x, closest_pig_x):
    return in_range and los_type == "Pig" and los_x == closest_pig_x

def attack_once():
    agent_host.sendCommand("attack 1")
    time.sleep(0.5)
    agent_host.sendCommand("attack 0")

def turn_pitch_discrete_move(command, number):
    agent_host.sendCommand(command + " " + number)
    time.sleep(1)
    agent_host.sendCommand(command + " 0")

def load_grid(chatty):
    """
    Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

    Args
        world_state:    <object>    current agent world state

    Returns
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
    """
    returnGrid = []
    grid = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    cx = chatty["x"]
    cz = chatty["z"]
    for x,z in grid:
        returnGrid.append((cx+x,cz+z))


    return returnGrid

# Loop until mission ends:
while world_state.is_mission_running:
    str_command = raw_input()

    time.sleep(0.5)
 #   print "\nSending action: chat %s" % str_command
 #   agent_host.sendCommand("chat %s" % str_command)
  #  agent_host.sendCommand(str_command)

    sys.stdout.write(".")

    world_state = agent_host.getWorldState()


    if len(world_state.observations) > 0:
        observation = json.loads(world_state.observations[-1].text)
        chatty = get_chatty(observation)
        closest_pig = find_closest_pig(observation, chatty)
        x = int(chatty["x"])
        z = int(chatty["z"])
        a = int(closest_pig["x"])
        b = int(closest_pig["z"])
        yaw = int(chatty["yaw"])
        if yaw%360 != 270:
            print("reset")
            if yaw%360 == 90:
                print("90")
                agent_host.sendCommand("turn 1")
                time.sleep(1)
                agent_host.sendCommand("turn 0")
            elif yaw%360 == 180:
                print("180")
                agent_host.sendCommand("turn 1")
                time.sleep(0.5)
                agent_host.sendCommand("turn 0")
            elif yaw%360 == 0:
                print("360")
                agent_host.sendCommand("turn -1")
                time.sleep(0.5)
                agent_host.sendCommand("turn 0")
            yaw = 270
            print("end reset")

        if (x <= a):
            if yaw%360 != 270:
                agent_host.sendCommand("turn 1")
                time.sleep(1)
                agent_host.sendCommand("turn 0")
                yaw = 270
                ("never")
            for i in range(x, a):
                agent_host.sendCommand("tp {} 41 {}".format(i, z))
                time.sleep(0.15)
            agent_host.sendCommand("turn 1")
            time.sleep(0.5)
            agent_host.sendCommand("turn 0")
            if yaw == 90:
                yaw = 180
            elif yaw == 270:
                yaw = 0
        else:
            if yaw%360 != 90:
                agent_host.sendCommand("turn 1")
                time.sleep(1)
                agent_host.sendCommand("turn 0")
                yaw = 90
            for i in range(a, x):
                agent_host.sendCommand("tp {} 41 {}".format(i, z))
                time.sleep(0.15)

            agent_host.sendCommand("turn 1")
            time.sleep(0.5)
            agent_host.sendCommand("turn 0")
            if yaw == 90:
                yaw = 180
            elif yaw == 270:
                yaw = 0

        if (z <= b):
            if yaw%360 != 0:
                agent_host.sendCommand("turn 1")
                time.sleep(1)
                agent_host.sendCommand("turn 0")
                yaw = 0

            for i in range(z, b-1):
                agent_host.sendCommand("tp {} 41 {}".format(a, i))
                time.sleep(0.15)
        else:
            if yaw%360 != 180:
                agent_host.sendCommand("turn 1")
                time.sleep(1)
                agent_host.sendCommand("turn 0")
                yaw = 180

            for i in range(b, z-1):
                agent_host.sendCommand("tp {} 41 {}".format(a, i))
                time.sleep(0.15)


        print("lol")

        #while True:

            # yaw = int(chatty["yaw"])
            # if x < closest_pig["x"]:
            #     if yaw%360 != 270:
            #         agent_host.sendCommand("turn 1")
            #         agent_host.sendCommand("turn 1")
            #         yaw = 270
            #     #while x != closest_pig["x"]:
            #         agent_host.sendCommand("movewest 1")
            #         agent_host.sendCommand("movewest 1")
            #         agent_host.sendCommand("movewest 1")
            #         agent_host.sendCommand("movewest 1")
            #
            #         #x += 1
            # elif x > closest_pig["x"]:
            #     if yaw%360 != 90:
            #         agent_host.sendCommand("turn 1")
            #         agent_host.sendCommand("turn 1")
            #         yaw = 90
            #     while x != closest_pig["x"]:
            #         agent_host.sendCommand("movewest 1")
            #        # x -= 1
            #
            # if z < closest_pig["z"]:
            #     if yaw == 270:
            #         agent_host.sendCommand("turn 1")
            #     elif yaw == 90:
            #         agent_host.sendCommand("turn -1")
            #     while z != closest_pig["z"]:
            #         agent_host.sendCommand("movewest 1")
            #         z += 1
            # elif z > closest_pig["z"]:
            #     if yaw == 270:
            #         agent_host.sendCommand("turn -1")
            #     elif yaw == 90:
            #         agent_host.sendCommand("turn 1")
            #     while z != closest_pig["z"]:
            #         agent_host.sendCommand("movewest 1")
            #         z -= 1
            # print(x,z)
            # break




        # while True:
        #     dist = tester(closest_pig,chatty)
        #     if dist < bestDist:
        #         bestDist = dist
        #         agent_host.sendCommand("move 1")
        #         time.sleep(0.1)
        #         agent_host.sendCommand("move 0")
        #         world_state = agent_host.getWorldState()
        #         if len(world_state.observations) > 0:
        #             observation = json.loads(world_state.observations[-1].text)
        #         chatty = get_chatty(observation)
        #     elif dist == bestDist:
        #         world_state = agent_host.getWorldState()
        #         if len(world_state.observations) > 0:
        #             observation = json.loads(world_state.observations[-1].text)
        #         chatty = get_chatty(observation)
        #     else:
        #         agent_host.sendCommand("turn 1")
        #         time.sleep(0.1)
        #         agent_host.sendCommand("turn 0")
        #         agent_host.sendCommand("move 1")
        #         time.sleep(0.5)
        #         agent_host.sendCommand("move 0")
        #












            # while True:
        #     agent_host.sendCommand("move 1")
        #     world_state = agent_host.getWorldState()
        #     observation = json.loads(world_state.observations[-1].text)
        #     chatty = get_chatty(observation)
        #     new = tester(closest_pig, chatty)
          #  if tester(closest_pig, chatty)











            #ObsFromRay usage here
        #TODO: use the observation to possiobly get direction object is facing
        # if 'LineOfSight' in observation:
        #     los = observation['LineOfSight']
        #     print chatty
        #     print closest_pig
        #
        #     # if the closest piggy is not in sight, use the coordinates to pitch and turn accordingly
        #     while (los["x"] != closest_pig["x"]) and los["z"] != closest_pig["z"]:
        #         chatty_x = chatty["x"]
        #         chatty_z = chatty["z"]
        #         closest_pig_x = closest_pig["x"]
        #         closest_pig_z = closest_pig["z"]
        #
        #         if not found_pig(los["type"], los["x"], closest_pig_x):
        #             #update los and closest_pig
        #             observation = json.loads(world_state.observations[-1].text)
        #             turn_pitch_discrete_move("turn", "0.5")
        #
        #         elif piggy_in_range(los["inRange"], los["type"], los["x"], closest_pig_x):
        #             attack_once()
        #
        #         if not found_pig(los["type"], los["x"], closest_pig_x):
        #             turn_pitch_discrete_move("pitch", "0.5")
        #         elif piggy_in_range(los["inRange"], los["type"], los["x"], closest_pig_x):
        #             attack_once()
        #
        #         if not found_pig(los["type"], los["x"], closest_pig_x):
        #             turn_pitch_discrete_move("pitch", "-0.5")
        #         elif piggy_in_range(los["inRange"], los["type"], los["x"], closest_pig_x):
        #             attack_once()
        #
        #         #turn the other way
        #         if not found_pig(los["type"], los["x"], closest_pig_x):
        #             turn_pitch_discrete_move("turn", "-2")
        #         elif piggy_in_range(los["inRange"], los["type"], los["x"], closest_pig_x):
        #             attack_once()
        #
        #         if not found_pig(los["type"], los["x"], closest_pig_x):
        #             turn_pitch_discrete_move("pitch", "0.5")
        #         elif piggy_in_range(los["inRange"], los["type"], los["x"], closest_pig_x):
        #             attack_once()
        #
        #         if not found_pig(los["type"], los["x"], closest_pig_x):
        #             turn_pitch_discrete_move("pitch", "-0.5")
        #         elif piggy_in_range(los["inRange"], los["type"], los["x"], closest_pig_x):
        #             attack_once()
        #
        #         time.sleep(1)


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

