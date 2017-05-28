---
layout: default
title:  Status
---
# Chatty's World

## Project Summary

The goal of our project is to implement a Natural Language Processing (NLP) system in Minecraft that will accept and interpret user input, and have the Minecraft agent act accordingly. To understand varying user input, we will make use of language processing tools, such as the NLTK and Gensim libraries. The agent actions will be implemented through the use of the Microsoft's Malmo API. Of course, not all inputs can be handled, as there are an infinite number of possible inputs that a user can give, as well as limitations on the actions a Minecraft agent can actually perform. Therefore, we will start by implementing basic commands (moving, turning, attacking, etc.), then use these, along with world state observations, to build more intricate commands, including (but not limited to) locating entities, killing mobs, fishing, and finding shelter.  

For this current milestone, we have implemented a working version of POS(Part of Speech) tagging using the nltk library. We used the gensim library to get a word2vector model using Google's GoogleNews-vectors-negative300.bin file. The load time was quite long, so we set a limit to speed things up. We also added a threshold for word similarity, so that if there wasn't a close synonym to a user-inputted word, we would ignore it completely and ask for new input. When calculating the word similarity, we compute the cosine similarity between the user input against all of the available valid Malmo commands. We are able to locate and attack entities. By the end, we wish to implement more functionality, such as finding shelter, fishing, digging. 

◦ Approach: Give a detailed description of your approach, in a few paragraphs. You should summarize the
main algorithm you are using, such as by writing out the update equation (even if it is off-the-shelf). You
should also give details about the approach as it applies to your scenario. For example, if you are using
reinforcement learning for a given scenario, describe the MDP in detail, i.e. how many states/actions you
have, what does the reward function look like. A good guideline is to incorporate sufficient details so that
most of your approach is reproducible by a reader. I encourage you to use figures, as appropriate, for this,
as I provided in the writeup for the first assignment (available here: http://sameersingh.org/courses/
aiproj/sp17/assignments.html#assignment1). I recommend at least 2-3 paragraphs.

## Approach

Our big milestone was to be able to compute the distance to the closest entity, and do something interesting with it. We first experimented with Pig entities, by trying to kill them. We decided to compute the Euclidean distance given a list of entities to find the closest one, and then currently move towards it using the Manhattan distance. We wish to implement a working version of approaching the nearest entity using the Euclidean distance in the future.

_distance = math.sqrt(abs((abs(chatty["x"] - entity["x"]) ** 2) + (abs(chatty["z"] - entity["z"]) ** 2)))_

To approach the entity, we first locate it, and then move on the x and z axis. The world state is then updated to make any sort of correction if the entity has since moved during our initial travel time. There was an issue with the 'yaw' value of our agent exceeding 360, so we worked around that problem by adding a modulo to the yaw to get our agent to turn accordingly.
	

◦ Evaluation: An important aspect of your project, as we mentioned in the beginning, is evaluating your
project. Be clear and precise about describing the evaluation setup, for both quantitative and qualitative
results. Present the results to convince the reader that you have a working implementation. Use plots, charts,
tables, screenshots, figures, etc. as needed. I expect you will need at least a few paragraphs to describe each
type of evaluation that you perform.

## Evaluation

A big part of our evaluation was to make sure our system was functional. In this milestone, we wanted to make sure that we could approach entities and do some sort of interaction with them. We want to implement a number of commands we could feed our agent, and make sure they execute in a sensible way.

The next chunk of our evaluation is in our word pairing. We want to ensure the closeness of pairing words that are synonymous with the valid Malmo commands. The gensim library helped us for this, but there are a few edge cases we would like to handle in the future. 


◦ Remaining Goals and Challenges: In a few paragraphs, describe your goals for the next 2-3 weeks, when
the final report is due. At the very least, describe how you consider your prototype to be limited, and what
you want to add to make it a complete contribution. Note that if you think your algorithm is quite good,
but have not performed sufficient evaluation, doing them can also be a reasonable goal. Similarly, you may
propose some baselines (such as a hand-coded policy) that you did not get a chance to implement, but
want to compare against for the final submission. Finally, given your experience so far, describe some of the
challenges you anticipate facing by the time your final report is due, how crippling you think it might be,
and what you might do to solve them.

## Remaining Goals and Challenges



