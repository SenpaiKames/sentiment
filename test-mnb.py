from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample training data
documents = ["lowkey missing online classes",
             "hello online classes",
             "When will the face-to-face classes come back? I don't want to enroll in an online class.",
             "After watching recorded live online classes, I realized even more that I don't want to teach. HAHA"]

# Corresponding labels for the training data
labels = [1, 1, 0, 0]

# Create an instance of CountVectorizer for feature extraction
vectorizer = CountVectorizer()

# Convert the text documents to a matrix of token counts
X = vectorizer.fit_transform(documents)

# Create an instance of Multinomial Naive Bayes classifier
classifier = MultinomialNB()

# Train the classifier using the training data
classifier.fit(X, labels)

# Sample test data
test_documents = ["i really dont miss online class",
                  "i hate online classes"]

# Convert the test documents to a matrix of token counts
X_test = vectorizer.transform(test_documents)

# Predict the labels for the test data
predictions = classifier.predict(X_test)

# Print the predicted labels
for doc, label in zip(test_documents, predictions):
    print(f"{doc} -> {label}")

# Measure the accuracy of the classifier
accuracy = accuracy_score(labels, classifier.predict(X))
print("Accuracy:", accuracy)
