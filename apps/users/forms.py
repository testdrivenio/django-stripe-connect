from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomAdminUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomAdminUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
