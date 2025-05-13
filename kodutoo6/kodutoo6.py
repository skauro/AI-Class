import csv
import math
import json
from collections import defaultdict


def preprocess_text(text):
    """Tokenize and preprocess text by lowercasing and removing short words."""
    return [word.lower() for word in text.split() if len(word) > 3]


def train_naive_bayes(train_file):
    """Train a Naive Bayes model on the given dataset."""
    class_counts = defaultdict(int)  # P(c)
    word_counts = defaultdict(lambda: defaultdict(int))  # P(w|c)
    total_words_per_class = defaultdict(int)
    vocabulary = set()
    total_articles = 0

    # Read and preprocess training data
    with open(train_file, encoding="utf-8") as f:
        reader = csv.reader(f)
        for topic, text in reader:
            words = preprocess_text(text)
            class_counts[topic] += 1
            total_articles += 1
            for word in words:
                word_counts[topic][word] += 1
                total_words_per_class[topic] += 1
                vocabulary.add(word)

    vocab_size = len(vocabulary)

    # Calculate probabilities with Laplace smoothing
    model = {
        "class_probs": {c: math.log(class_counts[c] / total_articles) for c in class_counts},
        "word_probs": {}
    }

    for c in word_counts:
        model["word_probs"][c] = {}
        for word in vocabulary:
            model["word_probs"][c][word] = math.log(
                (word_counts[c].get(word, 0) + 1) / (total_words_per_class[c] + vocab_size)
            )

    # Save trained model
    with open("nb_model.json", "w") as f:
        json.dump(model, f)

    return model


def classify_article(model, text):
    """Classify a single article using the trained model."""
    words = preprocess_text(text)
    max_prob = float('-inf')
    best_class = None

    for c in model["class_probs"]:
        log_prob = model["class_probs"][c]  # Start with P(c)
        for word in words:
            if word in model["word_probs"][c]:
                log_prob += model["word_probs"][c][word]  # Add log(P(w|c))

        if log_prob > max_prob:
            max_prob = log_prob
            best_class = c

    return best_class


def evaluate_model(model, test_file):
    """Evaluate model accuracy on test dataset."""
    correct = 0
    total = 0

    print(f"{'Actual Topic':<15} {'Predicted Topic'}")
    print("-" * 30)


    with open(test_file, encoding="utf-8") as f:
        reader = csv.reader(f)
        for actual_topic, text in reader:
            predicted_topic = classify_article(model, text)
            print(f"{actual_topic:<15} {predicted_topic}")

            if predicted_topic == actual_topic:
                correct += 1
            total += 1

    accuracy = correct / total
    print(f"Accuracy: {accuracy:.2%}")
    return accuracy


# Train and evaluate
train_file = "bbc_train.csv"
test_file = "bbc_test.csv"
model = train_naive_bayes(train_file)
evaluate_model(model, test_file)
