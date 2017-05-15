import nltk

#performs POS-tagging on one command at a time
#TODO: expand tagger to handle mutliple commands in one sentence, e.g., find the pig AND/THEN kill it
def tagger():
    verb = "none"
    noun = "none"
    num = "none"
    arg = "none"
    direction = "none"

    #append command to existing command (ensures tagger treats first word as verb)
    command = "I want you to "
    command += input("Enter command: ")

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


tagger()
