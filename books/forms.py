from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = ("title","content")
        fields = "__all__"
        exclude=("isbn",)
    

        def clean_title(self):
            title = self.cleaned_data.get("title")
        #categories=self.cleaned_data.get(" categories")
            if len(title)>50 or len(title)<10 :
                raise ValidationError("title length should be between 10 - 50")


