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

# Tutorial sample #2: Run simple mission using raw XML

import MalmoPython
import os
import sys
import time
import text_movement

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

              <About>
                <Summary>Hello world!</Summary>
              </About>

              <ServerSection>
                <ServerInitialConditions>
                    <Time>
                        <StartTime>10000</StartTime>
                        <AllowPassageOfTime>false</AllowPassageOfTime>
                    </Time>
                    <Weather>rain</Weather>
                </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"/>
                  <DrawingDecorator>
                    <DrawSphere x='-27' y='70' z='0' radius='30' type='air'/>
                  </DrawingDecorator>

                </ServerHandlers>
              </ServerSection>

              <AgentSection mode="Survival">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x='0' y='56' z='0' yaw='90'/>
                </AgentStart>
                <AgentHandlers>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

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

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

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
#Region the text command code
while True:
    user_input = raw_input("Command: ")
    if user_input == "":
        continue;
    command = user_input.split()
    #Treating texts in format: verb - range||pace
    if len(command) == 1:
        if command[0] == "quit":
            break
        if command[0] == "walk":
            text_movement.walk(agent_host)
        if command[0] == "stop":
            text_movement.force_stop(agent_host)
        if command[0] == "turn":
            text_movement.turn(agent_host)
        if command[0] == "pitch":
            text_movement.pitch(agent_host)
        if command[0] == "jump":
            text_movement.jump(agent_host)



    #Command given is length of 2, so action are changed
    if len(command) == 2:
        #Walk variations
        if command[0] == "walk":
            if command[1] == "fast":
                text_movement.walk(agent_host, 3)
            elif command[1] == "slow":
                text_movement.walk(agent_host, 0.5)
            elif type(int(command[1])) is int:
                text_movement.walk_step(agent_host, command[1])

        #Strafe variations
        if command[0] == "strafe":
            if command[1] == "left":
                text_movement.strafe(agent_host, -.5)
            elif command[1] == "right":
                text_movement.strafe(agent_host)

        #Turn command
        if command[0] == "turn":
            if command[1] == "left":
                text_movement.turn(agent_host, -1)
            elif command[1] == "right":
                text_movement.turn(agent_host)

    if len(command) == 3 and command[0] == "turn":
        if command[1] == "left":
            text_movement.turn(agent_host, -1, float(command[2]))
        if command[1] == "right":
            text_movement.turn(agent_host, 1, float(command[2]))
    if len(command) == 3 and command[0] == "pitch":
        if command[1] == "down":
            text_movement.pitch(agent_host, 1, float(command[2]))
        if command[1] == "up":
            text_movement.pitch(agent_host, -1, float(command[2]))
#EndRegion
# Loop until mission ends:
while world_state.is_mission_running:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission ended"
# Mission has ended.
