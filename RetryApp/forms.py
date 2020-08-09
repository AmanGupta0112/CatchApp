from django import  forms
from .models import ContactModel,FeedBackModel

class ContactForm(forms.ModelForm):

    class Meta():
        fields = "__all__"
        model = ContactModel

class FeedBackForm(forms.ModelForm):

    class Meta():
        fields = "__all__"
        model = FeedBackModel
