import MalmoPython
import os
import sys
import time
import random
import json
import MalmoCommands
import CommandReader


sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

randomSpawnNums = []
for i in range(8):
    x = random.randint(10, 65)
    z = random.randint(10, 65)
    tup = (x,z)
    randomSpawnNums.append(tup)

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
            <DrawCuboid x1="0" y1="50" z1="0" x2="76" y2="60" z2="76" type="grass" />
            
            <DrawCuboid x1="9" y1="50" z1="0" x2="9" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="19" y1="50" z1="0" x2="19" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="28" y1="50" z1="0" x2="28" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="32" y1="50" z1="0" x2="32" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="38" y1="50" z1="0" x2="38" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="45" y1="50" z1="0" x2="45" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="57" y1="50" z1="0" x2="57" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="66" y1="50" z1="0" x2="66" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="38" x2="76" y2="50" z2="38" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="32" x2="76" y2="50" z2="32" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="9" x2="76" y2="50" z2="9" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="19" x2="76" y2="50" z2="19" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="57" x2="76" y2="50" z2="57" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="66" x2="76" y2="50" z2="66" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="28" x2="76" y2="50" z2="28" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="45" x2="76" y2="50" z2="45" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="0" x2="76" y2="50" z2="0" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="76" x2="76" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="0" y1="50" z1="0" x2="0" y2="50" z2="76" type="glowstone" />
            <DrawCuboid x1="76" y1="50" z1="0" x2="76" y2="50" z2="76" type="glowstone" />
            
            <!--water and lava-->
            <DrawCuboid x1="67" y1="50" z1="1" x2="75" y2="50" z2="75" type="water" />
            
            <!--air-->
            <DrawCuboid x1="0" y1="51" z1="0" x2="76" y2="60" z2="76" type="air" />
            <DrawCuboid x1="66" y1="51" z1="0" x2="66" y2="51" z2="76" type="glass_pane"/>

           
            <!--ceiling-->
            <DrawCuboid x1="0" y1="60" z1="0" x2="76" y2="60" z2="76" type="glowstone" />          
              <!--house-->
 <!--           <DrawBlock type="planks" x="71" y="41" z="70"/>
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
          
            <DrawBlock type="planks" x="71" y="44" z="71"/>-->
            
            <!-- place mobs -->
            <DrawEntity x="{}"  y="51" z="{}" type="Pig" />
            <DrawEntity x="{}"  y="51" z="{}" type="Pig" />
            <DrawEntity x="{}"  y="51" z="{}" type="Sheep" />
            <DrawEntity x="{}"  y="51" z="{}" type="Sheep" />
            <DrawEntity x="{}"  y="51" z="{}" type="Cow" />
            <DrawEntity x="{}"  y="51" z="{}" type="Cow" />
            <DrawEntity x="{}"  y="51" z="{}" type="EntityHorse" />
            <DrawEntity x="{}"  y="51" z="{}" type="Wolf" />


            
            <!--spawners-->
            <!--DrawCuboid x1="29" y1="40" z1="29" x2="29" y2="40" z2="29" type="mob_spawner" variant="Pig"/-->
            <!--DrawCuboid x1="31" y1="40" z1="31" x2="31" y2="40" z2="31" type="mob_spawner" variant="Chicken"/-->
            <!--DrawCuboid x1="29" y1="40" z1="31" x2="29" y2="40" z2="31" type="mob_spawner" variant="Cow"/-->
            <!--DrawCuboid x1="31" y1="40" z1="29" x2="31" y2="40" z2="29" type="mob_spawner" variant="Sheep"/-->

        </DrawingDecorator>
      <ServerQuitFromTimeUp timeLimitMs="5000000"/>
      <ServerQuitWhenAnyAgentFinishes/>
    </ServerHandlers>
  </ServerSection>
  <AgentSection mode="Survival">
    <Name>Chatty</Name>
    <AgentStart>
      <Placement x="4" y="53" z="4" pitch="30" yaw="270"/>
      <Inventory>
        <InventoryItem slot="0" type="diamond_pickaxe"/>
        <InventoryItem slot="1" type="diamond_sword"/>
        <InventoryItem slot="2" type="fishing_rod"/>
        <InventoryItem slot="3" type="golden_apple" quantity="64"/>
        <InventoryItem slot="4" type="bone" quantity="20"/>
        <InventoryItem slot="5" type="carrot" quantity="64"/>
        <InventoryItem slot="6" type="wheat" quantity="64"/>

      </Inventory>
    </AgentStart>
    <AgentHandlers>
      <DiscreteMovementCommands/>
      <ContinuousMovementCommands turnSpeedDegs="180"/>
      <AbsoluteMovementCommands/>
      <ObservationFromFullStats/>
      <ObservationFromRay/>
      <ObservationFromNearbyEntities>
        <Range name="Entities" xrange="75" yrange="10" zrange="75"/>
      </ObservationFromNearbyEntities>
      <InventoryCommands/>
      <!--RewardForSendingCommand reward="-1"/-->
    </AgentHandlers>
  </AgentSection>
</Mission>
'''.format(randomSpawnNums[0][0],randomSpawnNums[0][1],randomSpawnNums[1][0],
           randomSpawnNums[1][1],randomSpawnNums[2][0],randomSpawnNums[2][1],
           randomSpawnNums[3][0],randomSpawnNums[3][1],randomSpawnNums[4][0],
           randomSpawnNums[4][1],randomSpawnNums[5][0],randomSpawnNums[5][1],
           randomSpawnNums[6][0],randomSpawnNums[6][1],randomSpawnNums[7][0],
           randomSpawnNums[7][1])



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

    time.sleep(0.5)
    sys.stdout.write(".")

    actions = MalmoCommands.MalmoCommands(agent_host)
    nlp = CommandReader.CommandReader()

    while True:
        userInput = nlp.tagger()
        for command in userInput:
            if command[0] == "walk":
                if command[1] == None:
                    actions.walk_step(1)
                elif (isinstance(command[1], int)):
                    actions.walk_step(command[1])
                elif command[1] in ["pig", "sheep", "horse", "cow", "wolf"]:
                    animal = command[1].title()
                    actions.findAnimal(animal)
                elif command[1] == "water":
                    actions.findWater()

            elif command[0] == "turn":
                if command[1] == None or command[1] == "right":
                    actions.turn()
                elif command[1] == "left":
                    actions.turn("left")
                elif command[1] in ["pig", "sheep", "horse", "cow", "wolf"]:
                    animal = command[1].title()
                    actions.findAnimal(animal)
                elif command[1] == "water":
                    actions.findWater()

            elif command[0] == "jump":
                actions.jump()
                
            elif command[0] == "crouch":
                actions.crouch()

            elif command[0] == "find":
                if command[1] == None:
                    continue
                elif command[1] in ["pig", "sheep", "horse", "cow", "wolf"]:
                    animal = command[1].title()
                    actions.findAnimal(animal)
                elif command[1] == "water":
                    actions.findWater()

            elif command[0] == "kill":
                if command[1] == None:
                    continue
                elif command[1] in ["pig", "sheep", "horse", "cow", "wolf"]:
                    animal = command[1].title()
                    actions.kill(animal)

            elif command[0] == "fish":
                actions.fish()

            elif command[0] == "ride":
                if command[1] == "horse":
                    print "To Get Down, type \"stop\"\n"
                    actions.ride()
                    
                elif command[1] in ["pig", "sheep", "cow", "wolf"]:
                    animal = command[1].title()
                    actions.findAnimal(animal)

            elif command[0] == "stop":
                commands.stopRide()
  
            elif command[0] == "feed":
                if command[1] in ["pig", "sheep", "horse", "cow", "wolf"]:
                    animal = command[1].title()
                    actions.feed(animal)

    for error in world_state.errors:
        print "Error:",error.text


print
print "Mission ended"
# Mission has ended.

