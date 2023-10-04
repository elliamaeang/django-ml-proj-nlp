from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from sentiment.forms import SentimentForm
from sentiment.ml_model import MLConfig
import numpy as np

# Create your views here.
def index(request):
    '''
        This is the landing page of the website.
    '''

    template = loader.get_template("sentiment/index.html")
    form = SentimentForm()
    context = {'form': form}

    return HttpResponse(template.render(context, request))

def analyze(request):
    '''
        This is where the sentiment analysis is performed.

        How it works:
            1. Retrieve form input text
            2. Preprocess the text
            3. Vectorize the text
            4. Pass the text to model for prediction
    '''
    
    # Load model
    ml = MLConfig() # load model by calling MLConfig class
    targets = ml.targets # get targets
    colors = ml.colors # get colors (for UI)

    # Check if view accessed through form submission
    if request.method == 'POST':

        # Pass form results
        form = SentimentForm(request.POST)

        # If form contains valid input
        if form.is_valid(): 

            # Get the input
            text = form.cleaned_data.get('text')
            print("Input:", text)

            # Preprocess the text
            preprocessed = ml.preprocess_text(text)
            print("Preprocessed:", preprocessed)

            # Vectorize
            vectorized = ml.vectorizer.transform([preprocessed])

            # Get predictions
            prediction = ml.model.predict(vectorized)[0]
            probas = ml.model.predict_proba(vectorized)
            probas = np.round(probas * 100, 2)[0] # convert probabilities to percentage values with 2 decimal places
            print("Prediction:", prediction)
            print("Probabilities:")
            for target, percentage in zip(targets, probas):
                print(f"{target}: {percentage}%")

            # Get classes
            proba_classes = zip(targets, probas, colors) # zip() used to combine the parameters into one list of tuples
            proba_classes = sorted(proba_classes, key=lambda x: x[1], reverse=True) # sort from highest to lowest

    else: # If view accessed through URL

        # Redirect to index
        return HttpResponseRedirect('/')

    # This part of the code is only reached if form submitted and valid
    template = loader.get_template('sentiment/index.html')
    context = {
        'form': form,
        'text': text,
        'prediction': prediction,
        'probas': list(probas),
        'classes': proba_classes
    }

    return HttpResponse(template.render(context, request))