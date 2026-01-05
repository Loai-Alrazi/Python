# SMS Spam Detection (NLP) 📩
This project uses Natural Language Processing to classify messages as 'Spam' or 'Ham'.

### Key Features:
- **Text Vectorization**: Used `CountVectorizer` to convert text into numerical data.
- **Model**: Multinomial Naive Bayes (`MultinomialNB`).
- **Persistence**: Saved the model and vectorizer using `joblib` for production use.

### Dataset:
Sourced from Kaggle (SMS Spam Collection).