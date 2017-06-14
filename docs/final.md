---
layout: default
title: Final Report
---

## Video 

## Project Summary
Welcome to Chatty’s World! Chatty is our Minecraft agent, who is placed in a world full of animals, and given a handful of items to interact with his environment. The objective of Chatty’s World is to allow a human user (like you) to control Chatty’s actions through a command prompt. To succeed in this goal, we focused on two areas: the Natural Language Processing (NLP), which interprets user input, and the implementation of agent actions, where we wrote code to carry out specific tasks.
 
The challenge that comes with interpreting user input is that there are an infinite number of possible queries that a human can request. Within the NLP section of our project, we strive to make sense of the English language to the best of our ability. The goal of our NLP system is to identify the verb that corresponds with the user’s desired action, along with the subject or any other information that makes the query more specific. For example, a user may want Chatty to “walk”, and can further specify how far Chatty should walk or even where he should walk to. Thus, we must focus on the keywords of the user input to accurately predict the action that the user intended.
 
After interpreting user input, the next step is to perform the predicted action. There are several basic movement commands that are provided by Microsoft’s Malmo API that we used to create more complex and interactive commands, such as walking to or killing entities. Our goals in relation to Chatty’s actions are to maximize the number of action-functions, so that the user has more options to do as he or she wishes, and also to make these functions as efficient and human-like as possible. The challenges behind these problems are that we are limited to what we can do by what is possible through the Malmo API. This required us to be as creative in coming up with action-ideas relevant to Chatty’s Minecraft environment, and knowledgeable in Minecraft/Malmo to discover if and how these ideas were possible.

## Approaches

### Natural Language Processing
 
Within our NLP system, we are making use of two external libraries to help us interpret language: the Natural Language Toolkit (NLTK) and Gensim. The first thing that we do upon receiving user input is split it by commas, as well as the conjunctions “and” and “then”. We do so to handle compound sentences, such as “kill a pig, kill a cow, and kill a sheep” or “find the water, then go fishing”. Splitting the input in this way creates a queue of commands to be interpreted in order, which will also be executed in order in the future.
 
For each command in the queue, we use NLTK functions to tokenize and perform Part-of-Speech tagging on it. With the tagged tokens, we then select the verb and any optional subsequent information, such as a noun (e.g., “pig”, “water”), direction (e.g., “right”, “left”), or number (for example, to specify number of steps to walk). If a verb is not specified before an argument, or not specified at all, the comman will be considered inavlid. Otherwise, the verb will be linked to a specific action-function, and the additional information will be passed into this function as an argument. Below is a table listing all of the verbs that are linked to actions-functions and all of the words/values that are linked to valid arguments.

![Chart](words.png)
 
In our approach thus far, our NLP system will successfully interpret commands like “find a pig”, but is unable to do so for commands like “locate a boar”. These two have the same meaning, but our system does not yet account for synonyms. The Gensim library will help us with NLP through the use of word vectors, so that each word that we examine from the user input will have its own unique vector representation. This requires the use Gensim to train/build a word2vector model, from which we can find a word’s associated vector. We build our model using Google's GoogleNews-vectors-negative300.bin file. With this, we can now compare the keywords of the user input to the words that our system already recognizes, by finding the cosine similarities between them. Doing so, a verb like “locate” will be linked to “find”, as the cosine similarities between these two words will be the highest, while those between pairs like “locate” and “kill” would be relatively low. In the same way, the word “boar” would be linked to “pig”. We also set a threshold, so that if a token does not have at least a 0.3 cosine similarity with its best match, then it will not be considered valid. We determined this value to be appropriate after lots of trial and error. Our NLP system can now interpret a much wider range of queries, as different verbs and arguments can be used to perform actions.

### Action Functions

To create actions for our agent to perform, we make use of Malmo's InventoryCommands and movement commands (AbsoluteMovementCommands, ContinouousMovementCommands), as well as Malmo's ObservationFromRay, ObservationFromNearbyEntities, and ObservationFromFullStats. Malmo provides several commands for simple movement, such as walking and turning, which we use to create more specific and complex commands. Receiving the Malmo world state observations is extremely crucial to the success of our created commands, as observing the world is necessary to complete tasks such as finding entities (ObservationFromNearbyEntities). In order to find a pig, we must check for the pig entities within our observation, grab their coordinates, and compare them with our agent's coordinates. In our “find” function, we calculate the Euclidian Distances to see which pig is the closest, then use movement commands to walk to the location, until the pig is observed to be in our LineOfSight and in range (for striking or feeding) from ObservationFromRay. In a simple example of how this works, observe the figure below.

![Chart](findPig.jpg)
 
Here, Chatty is represented by the smiling face and the pig is represented by the pig face. Each square in this grid represents a block on the map. As denoted by the red lines, we find the differences between Chatty’s and the pig’s  x and z coordinates, and use these lengths to calculate the hypotenuse of the triangle (Euclidian Distance), which is denoted by the blue line. With knowledge of the triangle’s side lengths, we can also perform a simple SOHCAHTOA calculation to find the angle that Chatty must turn to face the pig (denoted in yellow). Through the “setYaw” command found in the AbsoluteMovementCommands, we can position Chatty in the correct direction, and simply walk the length of the hypotenuse to reach the pig, using a walk function that we defined using the “move” command found in the ContinuousMovementCommands. 
 
The “find” function is the most important, as many of our other created functions, such as “kill”, “feed”, “ride”, and “fish” make use of it. For the “kill” function, our agent must continously call upon the “find” function to locate an entity, and strike until the ObservationFromFullStats updates to reflect that Chatty has killed a mob. Similarly, “feed” will require the finding of the targeted entity, followed by the selection of the correct food from Chatty’s inventory (using InventoryCommands) to be used on it. “Ride” will require the finding of a horse before attempting to mount it. Lastly, our “fish” function will first need to find water, then have Chatty cast his fishing rod until ObservationFromNearbyEntities tells us that the fishing hook’s y-coordinate has dropped significantly (representing a bite) or after 30 seconds have passed, at which point Chatty reels in his line. 

## Evaluation

### Quantitative Evaluation
While the success of our action-functions is discrete, in which the results that they produce are essentially the same upon each call, we focused our quantitative evaluation on our project’s ability to find synonyms/similar words with Gensim, and make the correct action-function calls with the correct arguments. To do so, we found several synonyms for each of the recognized verbs and nouns/arguments, and checked if these synonyms were interpreted correctly, by matching with their intended meaning. In the tables below, you can view the results of this evaluation, where the cosine similarity between each subject and synonym is provided.

![Chart](verbEval.png)
![Chart](nounEval.png)

Within these tables, the results in green represent those which were successful (cosine similarity above 0.24 threshold and closest-matched with target word), and those in red represent results that were unsuccessful (the reason behind its failure is also provided). Though it may not include every single synonym for each word, we did our best to evaluate realistic lists of the terms that a user could use. Through our results, we can see that our Gensim model did a fairly good job at interpreting the synonyms correctly. [23 out of the 32] verbs and [33 out of the 40] nouns that we tested were successful, with ~72% and ~83% accuracies, respectively. With this success rate, commands such as “find the horse and kill the pig” can now be worded in different ways like “pinpoint the pony then pwn the pork”, “locate the stallion then murder the boar”, or “discover the steed then attack the swine”. We also placed the unsuccessful synonyms in a word net, so that if the word is inputted by the user, the Gensim results will be overridden, and the correct action will be performed. With the word net in place, each synonym within the tables above will be interpreted correctly, with a 100% success rate. Any synonyms that were not found in the tables above will be evaluated and interpreted by its cosine score, which we are confident in, given the success of our Gensim model.

## References

Here are the links to the external libraries/APIs that were used for Chatty's World:<br><br>
<a href="http://www.nltk.org/">Natural Language Toolkit</a><br>
<a href="https://radimrehurek.com/gensim/models/word2vec.html">Gensim Word2Vec</a><br>
<a href="https://www.microsoft.com/en-us/research/project/project-malmo/">Project Malmo</a><br>
