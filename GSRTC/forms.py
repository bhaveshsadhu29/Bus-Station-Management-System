from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser,Schedule

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['bus', 'route', 'departure_time', 'arrival_time']
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }