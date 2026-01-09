Restaurant Reviews Sentiment Analysis 🍽️
Project Overview
This project uses Natural Language Processing (NLP) to classify restaurant reviews as Positive or Negative. It helps restaurant owners understand customer satisfaction automatically.

Key Steps Performed:
Text Preprocessing: Cleaned the text by removing punctuation and converting to lowercase.

Stopwords Removal: Removed common words that don't add meaning (except words like 'not').

Stemming: Reduced words to their root form (e.g., "loved" to "love").

Feature Extraction: Used CountVectorizer to convert text into a Bag-of-Words model.

Model Training: Trained a Naive Bayes classifier.

Results
The model achieved a high accuracy in predicting customer sentiment.

Included a function to test any new custom review.