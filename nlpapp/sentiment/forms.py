from django import forms
from sentiment.models import Text

class SentimentForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = "__all__"