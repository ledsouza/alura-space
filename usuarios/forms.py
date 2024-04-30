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
    senha = forms.CharField(
        label='Senha',
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )

class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome completo',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: JoãoSilva'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
   )
    senha_1 = forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )
    senha_2 = forms.CharField(
        label='Confirmação de senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data['nome_cadastro']
        if nome:
            if " " in nome:
                raise forms.ValidationError('O nome não pode conter espaços em branco')
            else:
                return nome