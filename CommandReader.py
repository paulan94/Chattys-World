import nltk
import re
from GensimHelper import GensimHelper

#performs POS-tagging on one command at a time
#TODO: expand tagger to handle mutliple commands in one sentence, e.g., find the pig AND/THEN kill it

class CommandReader:

    def __init__(self):
        self.gensim = GensimHelper()

    def tagger(self):

        commandsToGensim = []
        finalCommands = []
        prefix = "I want you to "
        #append command to existing command (ensures tagger treats first word as verb)
        command = raw_input("Enter command: ")
        command = command.lower()
        commandList = re.split("and|then|[^a-zA-Z0-9 ]+", command)

        for command in commandList:
            if "to" in command:
                command = command.replace("to", "")
            command = prefix + command
            verb = None
            noun = None
            
            tokens = nltk.word_tokenize(command)
            tags = nltk.pos_tag(tokens)
            desiredTags = tags[4:]
            for word, pos in desiredTags:
                #grabs first verb
                if "VB" in pos and verb == None:
                    verb = (word,pos)
                
                if "NN" in pos and noun == None:
                    noun = (word,pos)

                elif "CD" in pos and noun == None:
                    noun = (word,pos)

                elif "JJ" in pos and noun == None:
                    noun = (word,pos)

            if verb != None:
                commandsToGensim.append((verb, noun))
                
        for each in commandsToGensim:
            finalVerb = self.gensim.getVerb(each[0])
            finalNoun = self.gensim.getNoun(each[1])

            finalCommands.append((finalVerb, finalNoun))

        return finalCommands
