# Decision Tree Algorithm:

A decision Tree is a hierarchial structure made up of root, branches, internal and leaf nodes. It is a supervised learning approach used for classification and regression of applications.

The decision tree starts with a root node and feed into the internal nodes known as decision nodes. The leaf nodes represents all possible outcomes within the dataset. The tree like structure is used to make predictions by asking series of questions and each branch represents possible answer and final leaf nodes represents the predicted outcome.

[Decision Tree](./images/decision_tree.jpg)

Hences steps are

* Start with root node
* Ask the best questions
* Based on the answer, divide data into small subsets. Each branch represents a possible route through the tree.
* Repeat the process till the leaf node is encountered.

## Examples

### Decisionng we play or not by using decision Tree:

Decision trees are simple if else statements. If it is true/false,  go to next node attached to the decision.

In the above diagram the tree will first ask what is the weather? Is it sunny, cloudy, or rainy? If yes then it will go to the next feature which is humidity and wind. It will again check if there is a strong wind or weak, if it’s a weak wind and it’s rainy then the person may go and play.

[Determining to play or not](./images/play_or_not_decision.jpg)


### Determining to accept offer or not based on different features.

[Determining to play or not](./images/Accept_offer_or_not_decision_tree.jpg)


## Factors to be considered in decision Tree

### Entropy:
Entropy refers to uncertainity within the dataset of a given node which helps the algorithm to choose the best feature to split on, aiming to minimize the entropy, creating purer subsets in each split.This leads to more accurate predictions. Essentially, lower entropy indicates certain classification at a node and homogenous class distribution.

Consider a dataset where we want to classify if someone will buy a product based on income level.

If the node contains a mix of high and low income individuals with equal probability, the entropy at that node is high.

Hence, by splitting on the income level feature, the tree can create child nodes with more homogenous class distributions, resulting in a lower entropy at the each child node helps in better classification accuracy.

### Information Gain:
A measure of the decrease in the entropy after the data set is split is the information gain.

Information gain is a measure used to determine which feature should be used to split the data at each internal node of the decision tree.

Essentially measuring how much uncertainty is reduced by splitting the data based on that feature, allowing the decision tree to make more informed classifications; a higher information gain indicates a better split and more effective feature for prediction.

 Information gain helps the decision tree determine which features best separate the classes, reducing uncertainty and improving classification accuracy. Entropy measures the amount of uncertainty in your data using the formula that captures that uncertainty for a binary classification problem. Information gain is then used to find splits in the decision tree that reduce that uncertainty as much as possible.

 ### Pruning:
 Pruning is a process of deleting the unnecessary nodes from a tree in order to get the optimal decision tree.

A too-large tree increases the risk of overfitting, and a small tree may not capture all the important features of the dataset. Therefore, a technique that decreases the size of the learning tree without reducing accuracy is known as Pruning. 