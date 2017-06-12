import gensim
import numpy as np
import scipy as sp

class GensimHelper:

    def __init__(self):
        #model to train on
        self.model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)
        self.move_list = ['walk', 'turn', 'jump','crouch','find','kill', 'feed', 'ride']
        self.noun_list = ['pig', 'cow', 'sheep', 'wolf', 'horse', 'water']
        self.verbWordnet = {}
        self.nounWordnet = {}

        self.verbWordnet["mount"] = "ride"
        self.verbWordnet["sit"] = "ride"
        self.verbWordnet["spot"] = "find"
        self.verbWordnet["move"] = "walk"
        self.verbWordnet["hit"] = "kill"
        self.verbWordnet["pivot"] = "turn"
        self.verbWordnet["duck"] = "crouch"
        self.verbWordnet["cast"] = "fish"
        self.verbWordnet["tame" = "feed"

        self.nounWordnet["sow"] = "pig"
        self.nounWordnet["piggy"] = "pig"
        self.nounWordnet["calf"] = "cow"
        self.nounWordnet["ox"] = "cow"
        self.nounWordnet["cattle"] = "cow"
        self.nounWordnet["dog"] = "wolf"
        self.nounWordnet["puppy"] = "wolf"
        self.nounWordnet["pup"] = "wolf"



    def getVerb(self, verb):
        if verb[1] != "VB":
            return None

        if verb[0].lower() in ["pig", "cow", "sheep", "wolf", "horse", "water"]:
            return None

        if verb[0] in self.verbWordnet:
            return self.verbWordnet[verb[0]]
        
        try:
            verb_sim = []
            #append in same order as self.move_list to for later indexing
            verb_sim.append(self.model.similarity(verb[0], 'walk'))    
            verb_sim.append(self.model.similarity(verb[0], 'turn'))    
            verb_sim.append(self.model.similarity(verb[0], 'jump'))    
            verb_sim.append(self.model.similarity(verb[0], 'crouch'))  
            verb_sim.append(self.model.similarity(verb[0], 'find'))  
            verb_sim.append(self.model.similarity(verb[0], 'kill'))     
            verb_sim.append(self.model.similarity(verb[0], 'feed'))     
            verb_sim.append(self.model.similarity(verb[0], 'ride'))     

            bestVerb = max(verb_sim)
            bestVerbIndex = verb_sim.index(bestVerb)

            if bestVerb >= 0.3:
                return self.move_list[bestVerbIndex].lower()
            else:
                return None
        except:
            return None
            

    def getNoun(self, noun):
        
        if noun == None:
            return None

        if noun[0] in self.nounWordnet:
            return self.nounWordnet[noun[0]]
        
        if noun[1] == "JJ":
            return noun[0].lower()

        elif noun[1] == "CD":
            return noun[0]

        try:
            noun_sim = []
            
            noun_sim.append(self.model.similarity(noun[0], 'pig'))
            noun_sim.append(self.model.similarity(noun[0], 'cow'))
            noun_sim.append(self.model.similarity(noun[0], 'sheep'))
            noun_sim.append(self.model.similarity(noun[0], 'wolf'))    
            noun_sim.append(self.model.similarity(noun[0], 'horse'))    
            noun_sim.append(self.model.similarity(noun[0], 'water'))


            
            bestNoun = max(noun_sim)
            bestNounIndex = noun_sim.index(bestNoun)

            if bestNoun >= 0.3:
                return self.noun_list[bestNounIndex].lower()
            else:
                return None
        except:
            return None

##        
##        print ("Most similar verb is: {}\n".format(move_list[bestVerb]))
##
##        #to test
##        print ("Move similarity:{}".format(model.similarity(split[0], 'move')))
##        print ("Turn similarity:{}".format(model.similarity(split[0], 'turn')))
##        print ("Jump similarity:{}".format(model.similarity(split[0], 'jump')))
##        print ("Crouch similarity:{}".format(model.similarity(split[0], 'crouch')))
##        print ("Find similarity:{}".format(model.similarity(split[0], 'find')))
##        print ("Kill similarity:{}".format(model.similarity(split[0], 'kill')))
##        print ("Fish similarity:{}".format(model.similarity(split[0], 'fish')))
##        print ("Feed similarity:{}".format(model.similarity(split[0], 'feed')))
##        print ("Ride similarity:{}".format(model.similarity(split[0], 'ride')))
##        print ("Stop similarity:{}".format(model.similarity(split[0], 'stop')))
##
##        print ("Most similar noun is: {}\n".format(noun_list[bestNoun]))
##
##        #to test
##        print ("Pig similarity:{}".format(model.similarity(split[1], 'pig')))
##        print ("Cow similarity:{}".format(model.similarity(split[1], 'cow')))
##        print ("Sheep similarity:{}".format(model.similarity(split[1], 'sheep')))
##        print ("Wolf similarity:{}".format(model.similarity(split[1], 'wolf')))
##        print ("Horse similarity:{}".format(model.similarity(split[1], 'horse')))
##        print ("Water similarity:{}".format(model.similarity(split[1], 'water')))


