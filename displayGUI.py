import Tkinter as tk
from Tkinter import END
import gensim
import tagger
import threading
#import tkfont
# model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)
# move_list = ['move', 'strafe', 'pitch', 'turn', 'jump', 'crouch', 'attack', 'use', 'stop']
class commandWindow:

    def __init__(self, agent_host, switcherCommand):
        '''load agent settlers'''
        self.agent_host = agent_host
        self.switcherCommand = switcherCommand
        self.userInput = "Null"
        self.move_list = ['move', 'strafe', 'pitch', 'turn', 'jump', 'crouch', 'attack', 'use', 'stop']
        self.model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)

        self.window = tk.Tk(className="Malmo Command:")
        topFrame = tk.Frame(self.window)
        midFrame = tk.Frame(self.window)
        bottomFrame = tk.Frame(self.window)
        labelWidget = tk.Label(topFrame,text="Please Enter Your Command:")
        self.textWidget = tk.Text(midFrame, width=40, height = 1)
        okWidget = tk.Button(bottomFrame, text= "Ok", command = self.okClicked)
        cancelWidget = tk.Button(bottomFrame, text="Cancel", command = self.cancelClicked)
        self.restartWidget = tk.Button(topFrame, text="Restart", command=self.restartMission)

        self.textWidget.insert('1.0',"")
        labelWidget.pack(side="left")
        cancelWidget.pack(side="right")
        okWidget.pack(side="left")
        self.textWidget.pack()
        self.restartWidget.pack(side="right")
        self.textWidget.bind('<Return>', self.okClicked)

        topFrame.pack(side="top")
        bottomFrame.pack(side="bottom")
        midFrame.pack(side="bottom")


    #TODO: i think these changes work
    def okClicked(self, event):
        '''Get the edited values and write them to the file then quit'''
        #TODO: get values and write them to the file!
        self.userInput = self.textWidget.get("1.0", END)
        #user tagger here
        command = tagger.tagger(self.userInput) #POS tagging
        threshold = 0.26                        #threshold for gensim word2vec
        malmo_command = tagger.find_closest_command(command[0], self.model, self.move_list, threshold) #command
        # command = self.userInput.split()
        self.switcherCommand.commandList.append(malmo_command)
        if command[1] != "none":
            self.switcherCommand.commandList.append(command[1])
        if command[2] != "none":
            self.switcherCommand.commandList.append(command[2])

        print("command: {}".format(self.switcherCommand.commandList))
        self.switcherCommand.interpretCommand()
        self.textWidget.delete('1.0', END)
        self.switcherCommand.commandList = []


    def cancelClicked(self):
        '''Cancel edits and quit'''
        self.switcherCommand.commandList = ["stop"]
        self.switcherCommand.interpretCommand()
    def restartMission(self):
        '''restart mission after pressing restart button'''
        self.agent_host.sendCommand("quit")
        self.agent_host.startMission(self.my_mission, self.my_mission_record)

        # try:
        #     self.agent_host.startMission( self.my_mission, self.my_mission_record)
        # except RuntimeError as e:
        #     print "Error starting mission:",e
        #     exit(1)
        return

# def okClicked():
#     '''Get the edited values and write them to the file then quit'''
#     #TODO: get values and write them to the file!
#     return(textWidget.get('1.0', END))
#
# def cancelClicked():
#     '''Cancel edits and quit'''
#     exit()
# c = commandWindow
