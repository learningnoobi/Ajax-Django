from django import forms 
from .models import Student
class StudentForm(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'input-form','placeholder':'add name ...'}))
    hobby = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'input-form','placeholder':'add hobby ...'}))

    class Meta:
        model = Student
        fields = ('name','hobby')
