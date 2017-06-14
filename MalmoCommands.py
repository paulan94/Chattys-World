import MalmoPython
import json
import time
import math


class MalmoCommands:

    def __init__(self, agentHost):
        self.agent = agentHost
        self.crouch = False

    def walk_step(self, steps):
        """
        walk command:
        'walk 10' - agent walks 10 steps
        """
        #Get agent to walk discrete steps
        #Time.sleep is called to allow agent to walk a single step
        steps = int(steps)
        for i in range(steps):
            self.agent.sendCommand("move 1")
            time.sleep(0.25)
            self.agent.sendCommand("move 0")

    def turn(self, direction="right"):
        if direction == "right":
            self.agent.sendCommand("turn 1")
            time.sleep(0.5)
            self.agent.sendCommand("turn 0")
        elif direction == "left":
            self.agent.sendCommand("turn -1")
            time.sleep(0.5)
            self.agent.sendCommand("turn 0")

    def jump(self):
        #used to get agent to jump
        self.agent.sendCommand("jump 1")
        self.agent.sendCommand("move 1")
        time.sleep(.5)
        self.agent.sendCommand("jump 0")
        self.agent.sendCommand("move 0")

    def crouch(self):
   
        if self.crouch:
            self.agent.sendCommand("crouch 0")
            self.crouch = False
        else:
            self.agent.sendCommand("crouch 1")
            self.crouch = True

    def get_chatty(self,observation):
        if 'Entities' in observation:
            entities = observation["Entities"]
            for ent in entities:
                if ent["name"] == "Chatty":
                    chatty = ent
        return chatty

    def find_closest_animal(self,observation, chatty, animal):
        closest_animal = None
        distanceToChattyFromAnimal = -999

        if 'Entities' in observation:
            entities = observation['Entities']
            animalList = []
            # get the pig and chatty entities
            # chatty is the user
            for ent in entities:
                if ent["name"] == animal:
                    animalList.append(ent)
            # if chatty is not None, get the x and z coordinates
            if chatty != None:
                chatty_x = chatty["x"]
                chatty_z = chatty["z"]
                distanceList = []

                for a in animalList:
                    animal_x = a["x"]
                    animal_z = a["z"]

                    # distance formula to get distance from any pig to chatty
                    distanceToChattyFromAnimal = math.sqrt(abs((abs(chatty_x - animal_x) ** 2) + (abs(chatty_z - animal_z) ** 2)))
                    distanceList.append(distanceToChattyFromAnimal)
                    if distanceToChattyFromAnimal == min(distanceList):
                        closest_animal = a
        
        return closest_animal

    def piggy_in_range(self, obs, animal):
        return obs['inRange'] and obs['type'] == animal

    def findAnimal(self, animal):
        counter = 0
        self.agent.sendCommand('setPitch 30')

        while True:
            counter += 1
            latest_ws = self.agent.peekWorldState()

            if latest_ws.number_of_observations_since_last_state > 0:
                observation = json.loads(latest_ws.observations[-1].text)

                if 'LineOfSight' in observation:
                    if self.piggy_in_range(observation['LineOfSight'], animal):
                        return True

            if counter % 500 == 0:
                return False
            
            chatty = self.get_chatty(observation)
            closest_animal = self.find_closest_animal(observation, chatty, animal)

            if closest_animal == None:
                return False
        
            x = int(chatty["x"])
            z = int(chatty["z"])
            a = int(closest_animal["x"])
            b = int(closest_animal["z"])
            diffX = x-a
            diffZ = z-b
            hypotenuse = math.sqrt((diffX**2) + (diffZ**2))

            if diffZ == 0:
                diffZ = 0.000000001
            if hypotenuse == 0:
                hypotenuse = 0.000000001
                
            if (x <= a and z <= b):
                angle = math.acos(((diffZ**2) + (hypotenuse**2) - (diffX**2)) / (2*abs(diffZ)*abs(hypotenuse)))
                angle = abs(math.degrees(angle))
     #           print(angle, diffX, diffZ, hypotenuse)
                self.agent.sendCommand("setYaw {}".format(360-angle))
                self.walk_step(round(hypotenuse)-3)
                
            elif (x >= a and z <= b):
                angle = math.acos(((diffZ**2) + (hypotenuse**2) - (diffX**2)) / (2*abs(diffZ)*abs(hypotenuse)))
                angle = abs(math.degrees(angle))
     #           print(angle, diffX, diffZ, hypotenuse)
                self.agent.sendCommand("setYaw {}".format(0+angle))
                self.walk_step(round(hypotenuse)-3)
                
            elif (x >= a and z >= b):
                angle = math.acos(((diffZ**2) + (hypotenuse**2) - (diffX**2)) / (2*abs(diffZ)*abs(hypotenuse)))
                angle = abs(math.degrees(angle))
     #           print(angle, diffX, diffZ, hypotenuse)
                self.agent.sendCommand("setYaw {}".format(180-angle))
                self.walk_step(round(hypotenuse)-3)

            elif (x <= a and z >= b):
                angle = math.acos(((diffZ**2) + (hypotenuse**2) - (diffX**2)) / (2*abs(diffZ)*abs(hypotenuse)))
                angle = abs(math.degrees(angle))
     #           print(angle, diffX, diffZ, hypotenuse)
                self.agent.sendCommand("setYaw {}".format(180+angle))
                self.walk_step(round(hypotenuse)-3)

    def findWater(self):
        latest_ws = self.agent.peekWorldState()

        if latest_ws.number_of_observations_since_last_state > 0:
            observation = json.loads(latest_ws.observations[-1].text)

        chatty = self.get_chatty(observation)

        x = int(chatty["x"])
        waterX = 65

        diffX = waterX - x

        if diffX > 0:
            self.agent.sendCommand("setYaw 270")
            self.walk_step(diffX)

    def attack(self):
        self.agent.sendCommand("attack 1")
        time.sleep(0.5)
        self.agent.sendCommand("attack 0")
                
    def kill(self, animal):
        self.agent.sendCommand('hotbar.2 1')
        self.agent.sendCommand('hotbar.2 0')

        latest_ws = self.agent.peekWorldState()

        if latest_ws.number_of_observations_since_last_state > 0:
            observation = json.loads(latest_ws.observations[-1].text)

            killed = observation['MobsKilled']

        counter = 0           
        while True:
            if counter >= 5:
                break
            if not self.findAnimal(animal):
                counter += 1
            else:
                self.attack()
                time.sleep(0.5)
                self.agent.sendCommand("jump 0")
                latest_ws = self.agent.peekWorldState()

                if latest_ws.number_of_observations_since_last_state > 0:
                    observation = json.loads(latest_ws.observations[-1].text)

                    if observation['MobsKilled'] > killed:
                        break

    def fish(self):
        self.agent.sendCommand('hotbar.3 1')
        self.agent.sendCommand('hotbar.3 0')

        self.agent.sendCommand('setPitch 15')
        self.findWater()

        start = time.time()
        self.agent.sendCommand('use 1')
        self.agent.sendCommand('use 0')
        time.sleep(3)
        latest_ws = self.agent.peekWorldState()
            
        if latest_ws.number_of_observations_since_last_state > 0:
            observation = json.loads(latest_ws.observations[-1].text)

        while True:
            current = time.time()
            latest_ws = self.agent.peekWorldState()

            if current-start >= 30:
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                break
            
            if latest_ws.number_of_observations_since_last_state > 0:
                last = observation
                observation = json.loads(latest_ws.observations[-1].text)
                
            if abs(filter(lambda ent: ent[u'name'] == u'unknown', observation['Entities'])[0][u'y'] - filter(lambda ent: ent[u'name'] == u'unknown', last['Entities'])[0][u'y']) > 0.02:
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                break

    def ride(self):
        counter = 0
        self.agent.sendCommand("hotbar.8 1")
        self.agent.sendCommand("hotbar.8 0")
        time.sleep(1)
        self.agent.sendCommand("discardCurrentItem")
        
        while True:
            if not self.findAnimal("Horse"):
                counter += 1
            else:
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                latest_ws = self.agent.peekWorldState()
                if latest_ws.number_of_observations_since_last_state > 0:
                    observation = json.loads(latest_ws.observations[-1].text)
                    chatty = self.get_chatty(observation)
                    if chatty['y'] != "41":
                        break
                
            if counter >= 5:
                break

    def stopRide(self):
        latest_ws = self.agent.peekWorldState()
        if latest_ws.number_of_observations_since_last_state > 0:
            observation = json.loads(latest_ws.observations[-1].text)
            chatty = self.get_chatty(observation)
            x = chatty['x']
            z = chatty['z']
            self.agent.sendCommand('tp {} 51 {}'.format(x+1, z))

    def feed(self, animal):
        counter = 0
        while True:
            if counter >= 5:
                break
            if self.findAnimal(animal):
                if animal == "Pig":
                    self.agent.sendCommand("hotbar.6 1")
                    self.agent.sendCommand("hotbar.6 0")
                elif animal =="Horse":
                    self.agent.sendCommand("hotbar.4 1")
                    self.agent.sendCommand("hotbar.4 0")
                elif animal == "Wolf":
                    self.agent.sendCommand("hotbar.5 1")
                    self.agent.sendCommand("hotbar.5 0")
                elif animal == "Cow" or animal == "Sheep":
                    self.agent.sendCommand("hotbar.7 1")
                    self.agent.sendCommand("hotbar.7 0")
                    
                self.agent.sendCommand('use 1')
                self.agent.sendCommand('use 0')
                break
            else:
                counter += 1


