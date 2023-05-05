from django import forms
class StudentRegistration(forms.Form):
    # Create a class and id in HTML input tag using attrs.
    # and this id overrides the default id 
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'somecss1', 'id': 'uniqueid'}))

    # Change name field to FileInput filed
    # name = forms.CharField(widget=forms.FileInput)

    # Change name field to CheckboxInput filed
    # name = forms.CharField(widget=forms.CheckboxInput)

    # Change name field to textarea filed
    # name = forms.CharField(widget=forms.Textarea)

    # Make name field password input field
    # name = forms.CharField(widget=forms.PasswordInput())

