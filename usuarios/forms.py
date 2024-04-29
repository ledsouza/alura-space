from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Usuário',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )