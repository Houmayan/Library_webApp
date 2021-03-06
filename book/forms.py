from dataclasses import fields
from msilib.schema import Class
from pyexpat import model
from .models import Book
from django import forms

class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
