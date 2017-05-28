import nltk
import gensim

#performs POS-tagging on one command at a time
#TODO: expand tagger to handle mutliple commands in one sentence, e.g., find the pig AND/THEN kill it
def tagger(user_input):
    verb = "none"
    noun = "none"
    num = "none"
    arg = "none"
    direction = "none"

    #append command to existing command (ensures tagger treats first word as verb)
    command = "I want you to " + user_input
    # command += raw_input("Enter command: ")

    tokens = nltk.word_tokenize(command.lower())
    tags = nltk.pos_tag(tokens)
    desiredTags = tags[4:]
    print(desiredTags)

    for word, pos in desiredTags:
        #grabs first verb
        if "VB" in pos and verb == "none":
            verb = word
        if "CD" in pos and num == "none":
            num = word
        if "NN" in pos and noun == "none":
            noun = word
        if "JJ" in pos and direction == "none":
            direction = word

    if verb == "none":
        return ("none", "none", "none")
    else:
        if noun != "none":
            arg = noun
            direction = "none"
            num = "none"
        elif direction != "none" and num == "none":
            arg = direction
        elif num != "none" and direction == "none":
            arg = num
            num = "none"
        elif num != "none" and direction != "none":
            arg = direction

    print("Verb: {}\nSubject: {}\nNumber: {}".format(verb, arg, num))
    returnTup = (verb, arg, num)

    return returnTup


def find_closest_command(user_input, model, move_list, threshold):

    try:
        similarity_list = []

        # print ("Move similarity:{}".format(model.similarity(user_input, 'move')))
        # print ("Strafe similarity:{}".format(model.similarity(user_input, 'strafe')))
        # print ("Pitch similarity:{}".format(model.similarity(user_input, 'pitch')))
        # print ("Turn similarity:{}".format(model.similarity(user_input, 'turn')))
        # print ("Jump similarity:{}".format(model.similarity(user_input, 'jump')))
        # print ("Crouch similarity:{}".format(model.similarity(user_input, 'crouch')))
        # print ("Attack similarity:{}".format(model.similarity(user_input, 'attack')))
        # print ("Use similarity:{}".format(model.similarity(user_input, 'use')))
        # print ("Stop similarity:{}".format(model.similarity(user_input, 'stop')))

        similarity_list.append(model.similarity(user_input, 'move'))  # 0
        similarity_list.append(model.similarity(user_input, 'strafe'))  # 1
        similarity_list.append(model.similarity(user_input, 'pitch'))  # 2
        similarity_list.append(model.similarity(user_input, 'turn'))  # 3
        similarity_list.append(model.similarity(user_input, 'jump'))  # 4
        similarity_list.append(model.similarity(user_input, 'crouch'))  # 5
        similarity_list.append(model.similarity(user_input, 'attack'))  # 6
        similarity_list.append(model.similarity(user_input, 'use'))  # 7
        similarity_list.append(model.similarity(user_input, 'stop'))  # 8

        num_to_beat = 0
        for num in similarity_list:
            if num > num_to_beat:
                num_to_beat = num
        # print num_to_beat
        if num_to_beat < threshold:
            print("Could not find a close match!")
        else:
            x = similarity_list.index(max(similarity_list)) #index of malmo command that is closest to input word
        # print ("Most similar word is: {}\n".format(move_list[x]))
            return move_list[x]


    except KeyError:
        print ("word not found")

if __name__ == "__main__":
    #load model
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, limit=500000)
    move_list = ['move', 'strafe', 'pitch', 'turn', 'jump', 'crouch', 'attack', 'use', 'stop']
    while True:
        user_input = raw_input("Input a command: ")
        tagger_tuple = tagger(user_input)
        threshold = 0.26
        malmo_command = find_closest_command(tagger_tuple[0], model, move_list, threshold)
        print malmo_command
