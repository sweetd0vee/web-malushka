from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    # def clean(self):
    #     username = self.changed_data.get("username")
    #     password = self.changed_data.get("password")

    def clean_username(self):
        username = self.cleaned_data["username"]
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is as invalid username")
        return username
