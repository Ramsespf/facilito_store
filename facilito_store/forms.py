from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,min_length=4, required=True,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'username'
                            }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class':'form-control',
                                    'id':'email',
                                    'placeholder':'example@codigofacilito.com'
                                }))
    password = forms.CharField(min_length=4, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                    'id':'password'
                                }))
    