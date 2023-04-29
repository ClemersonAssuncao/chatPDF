from django import forms
from django.core.validators import FileExtensionValidator

# class PostForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = '__all__'

class PostForm(forms.Form):
    pdf = forms.FileField(
        label='Arquivo: ',
        # widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'})
        # validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
        )
