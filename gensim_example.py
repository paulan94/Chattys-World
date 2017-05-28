import nltk
import gensim
import pandas as pd
from gensim import corpora, models, similarities
import numpy as np
import scipy as sp

# df = pd.read_csv('jokes.csv');
#
# x = df['Question'].values.tolist()
# y = df['Answer'].values.tolist()
#
# corpus = x + y
#
# tok_corp = [nltk.word_tokenize(sent.decode('utf-8')) for sent in corpus]

# model = gensim.models.Word2Vec(tok_corp, min_count=1, size=32)

#model to train on
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)

move_list = ['move', 'strafe', 'pitch', 'turn', 'jump','crouch','attack','use', 'stop']


while True:
    try:
        similarity_list = []
        user_input = raw_input("Model word test\n")
        if (user_input == 'fuckit'):
            break

        similarity_list.append(model.similarity(user_input, 'move'))    #0
        similarity_list.append(model.similarity(user_input, 'strafe'))  #1
        similarity_list.append(model.similarity(user_input, 'pitch'))   #2
        similarity_list.append(model.similarity(user_input, 'turn'))    #3
        similarity_list.append(model.similarity(user_input, 'jump'))    #4
        similarity_list.append(model.similarity(user_input, 'crouch'))  #5
        similarity_list.append(model.similarity(user_input, 'attack'))  #6
        similarity_list.append(model.similarity(user_input, 'use'))     #7
        similarity_list.append(model.similarity(user_input, 'stop'))    #8

        num_to_beat = 0
        for num in similarity_list:
            if num > num_to_beat:
                num_to_beat = num
        # print num_to_beat
        if num_to_beat < 0.3:
            print("Could not find a close match")
            break
        else:
            x = similarity_list.index(max(similarity_list))
        # print x
            print ("Most similar word is: {}\nX: {}".format(move_list[x],x))
        # print (similarity_list[x])

        #to test
        print ("Move similarity:{}".format(model.similarity(user_input, 'move')))
        print ("Strafe similarity:{}".format(model.similarity(user_input, 'strafe')))
        print ("Pitch similarity:{}".format(model.similarity(user_input, 'pitch')))
        print ("Turn similarity:{}".format(model.similarity(user_input, 'turn')))
        print ("Jump similarity:{}".format(model.similarity(user_input, 'jump')))
        print ("Crouch similarity:{}".format(model.similarity(user_input, 'crouch')))
        print ("Attack similarity:{}".format(model.similarity(user_input, 'attack')))
        print ("Use similarity:{}".format(model.similarity(user_input, 'use')))
        print ("Stop similarity:{}".format(model.similarity(user_input, 'stop')))

    except KeyError:
        print ("word not found")




# model.save('testmodel')
# model = gensim.models.Word2Vec.load('test_model')
# model.most_similar('word')
# model.most_similar([vector])