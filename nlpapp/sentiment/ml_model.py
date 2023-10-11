from django.conf import settings
import joblib
import os
import re
import contractions

class MLConfig():
    def __init__(self):
        '''
            This initializes the model and its variables.
        '''
        # Load from joblib
        self.model = joblib.load(os.path.join(settings.BASE_DIR, "models/sentiment_clf.joblib"))
        self.vectorizer = joblib.load(os.path.join(settings.BASE_DIR, "models/vectorizer.save"))
        self.spcy = joblib.load(os.path.join(settings.BASE_DIR, "models/spacy.save"))
        self.nlp = joblib.load(os.path.join(settings.BASE_DIR, "models/nlp.save"))

        # Initialize other variables
        self.targets = ['negative', 'neutral', 'positive']
        self.colors = ['danger', 'warning', 'success'] # for UI

    def preprocess_text(self, text):
        '''
            This function preprocesses the text.

            How it works:
                1. Convert the text to lowercase
                2. Remove links
                3. Expand contractions
                4. Tokenize and lemmatize
                5. Remove punctuations and non-ordinal numbers
                6. Remove select stopwords
                7. Return preprocessed text

        '''
        to_lower = text.lower() # make text lowercase
        no_link = re.sub('http[^\s]+', '', to_lower) # remove links (starts with http)
        no_contractions = contractions.fix(no_link) # remove contractions by expanding them
        doc = self.spcy(no_contractions) # tokenize

        # lemmatize and remove punctuation and non-ordinal numbers
        processed_tokens = [
            token.lemma_ for token in doc 
            if not token.is_punct and (
                token.is_alpha or token.text.endswith(("st", "nd", "rd", "th"))
            )
        ]
        processed_text = " ".join(processed_tokens) # join the processed tokens to form the preprocessed text

        after_nlp = self.nlp.process(processed_text) # remove stopwords using NLP

        return after_nlp