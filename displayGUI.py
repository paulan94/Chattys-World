import Tkinter as tk
#import tkfont
class commandWindow:

    def __init__(self, agent_host, my_mission, my_mission_record):
        '''load agent settlers'''
        self.agent_host = agent_host
        self.my_mission = my_mission
        self.my_mission_record = my_mission_record

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

        topFrame.pack(side="top")
        bottomFrame.pack(side="bottom")
        midFrame.pack(side="bottom")



    def okClicked(self):
        '''Get the edited values and write them to the file then quit'''
        #TODO: get values and write them to the file!
        return(self.textWidget.get('1.0', "end"))

    def cancelClicked(self):
        '''Cancel edits and quit'''
        exit()
    def restartMission(self):
        '''restart mission after pressing agent host button'''
        self.agent_host.sendCommand("quit")
        # try:
        #     self.agent_host.startMission( self.my_mission, self.my_mission_record)
        # except RuntimeError as e:
        #     print "Error starting mission:",e
        #     exit(1)
        return

def okClicked():
    '''Get the edited values and write them to the file then quit'''
    #TODO: get values and write them to the file!
    return(textWidget.get('1.0', END))

def cancelClicked():
    '''Cancel edits and quit'''
    exit()
