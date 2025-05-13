This project implements a Naive Bayes text classifier to categorize BBC news articles into topics like tech, politics, business, entertainment, and sport.

The text preprocessing step involves lowercasing all words and removing short words (length ≤ 3).

During training, the model counts word occurrences for each class and stores the log-probabilities with Laplace smoothing in a JSON file (nb_model.json).

For classification, the model sums the log-probabilities of the words and selects the class with the highest total score. 

The classifier achieved an accuracy of 96.00% on the provided test dataset.


output of comparison : 

Actual Topic    Predicted Topic
------------------------------
tech            tech
politics        politics
business        business
entertainment   entertainment
tech            tech
tech            tech
politics        politics
tech            tech
business        business
entertainment   entertainment
business        business
entertainment   entertainment
politics        politics
business        business
sport           sport
tech            tech
business        business
politics        politics
tech            tech
politics        entertainment
business        business
entertainment   entertainment
tech            tech
tech            tech
sport           sport
entertainment   entertainment
politics        politics
politics        politics
business        business
politics        politics
tech            tech
entertainment   entertainment
politics        politics
business        business
politics        politics
sport           sport
politics        politics
sport           sport
tech            tech
business        business
sport           politics
politics        politics
tech            tech
politics        politics
politics        politics
politics        politics
entertainment   entertainment
business        business
sport           sport
politics        politics
tech            tech
business        business
entertainment   entertainment
business        business
politics        politics
tech            tech
sport           sport
business        business
business        business
tech            tech
politics        politics
entertainment   entertainment
entertainment   entertainment
sport           sport
politics        politics
entertainment   entertainment
politics        politics
tech            tech
entertainment   entertainment
sport           sport
business        business
sport           sport
sport           sport
tech            tech
entertainment   entertainment
business        business
tech            tech
entertainment   entertainment
sport           sport
business        business
business        business
tech            tech
business        business
sport           sport
entertainment   entertainment
business        business
sport           sport
politics        business
entertainment   entertainment
sport           sport
entertainment   entertainment
business        business
tech            tech
politics        politics
tech            tech
tech            politics
sport           sport
entertainment   entertainment
business        business
sport           sport
Accuracy: 96.00%