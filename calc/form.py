from django import forms
class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name",max_length=20)
    lastname = forms.CharField(label="Enter Last Name",max_length=20)
    email = forms.EmailField(label="Enter Email")
    file = forms.FileField()