from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserApp
from django.contrib.auth import authenticate, login

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserApp
        fields = ['nickname', 'username', 'surname', 'password', 'email_address']

    def save(self, commit=True):
        print("wywołanie metody save na formie")
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email_address = forms.EmailField()
    password = forms.CharField(max_length=200)

    def __init__(self, request=None, *args, **kwargs):
        '''
            Constructor is obligated during executing LoginView if we will not
            initialize a construcor we have a fail __init__ beacuse during executing
            to form is passed argument request
        '''
        self.request = request
        super().__init__(*args, **kwargs)
        self.fields['email_address'].widget.attrs['name'] = 'email_address'
        self.fields['password'].widget.attrs['name'] = 'password'

    def clean(self):
        """
            Funkcja is ivnokking on evey field and check data validation if
            something is wrong function raise exception, return cleaned_data
        """
        cleaned_data = super().clean()  # we invoke this to check data valid
        email_address = self.request.POST.get('email_address')
        password = self.request.POST.get('password')
        print(self.fields)
        print(self.request.POST)
        print("czyszczenie danych ")
        if email_address and password:
            print("sprawdzamy dane")
            user = authenticate(username=email_address, password=password)
            print(user)
            if user is None or not user.is_active:
                raise forms.ValidationError('Invalid email address or password')
        return cleaned_data

    def login_user(self):
        data = self.cleaned_data
        print("proba zalogowania")
        try:
            user = authenticate(username=data.get('email_address'),
                                password=data.get('password'))
            login(self.request, user)
            print("zalogowano uzytkownika")
        except Exception as e:
            print("something is wrong with login:{}".format(str(e)))
            raise forms.ValidationError("An error occurred during login.")
