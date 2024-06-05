from typing import Any
from django import forms
from .models import Tweet, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweerForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
            "placeholder": "Compartilhe seus pensamentos aqui...",
            "class": "form-control", "rows": 5, "cols": 2}),
            label="",
            )
    
    class Meta:
        model = Tweet
        exclude = ("user",)
        

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'label':'E-mail'}))
    username = forms.CharField(label="", max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "Nome do usuário"})
        self.fields["username"].label = 'Nome do usuário'
        self.fields["username"].help_text = "<span><small>Obrigatório. 150 caracteres ou menos. Apenas letras, dígitos e @/./+/-/_ são permitidos.</small></span>"

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email"})
        self.fields["email"].label = 'E-mail'

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Senha"})
        self.fields["password1"].label = 'Senha'
        self.fields["password1"].help_text = "<ul> <li> Sua senha deve conter pelo menos 8 caracteres.</li> <li> Sua senha não pode ser muito semelhante às suas outras informações pessoais. </li> <li> Sua senha não pode ser uma senha que é frequentemente utilizada. </li> <li> A sua senha não pode ser completamente numérica. </li> </ul>"

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirme sua senha"})
        self.fields["password2"].label = 'confirme a sua senha'
        self.fields["password2"].help_text = "<span class='form-text text-muted'><small>Digite a mesma senha novamente, para verificação.</small></span>"


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "image"]