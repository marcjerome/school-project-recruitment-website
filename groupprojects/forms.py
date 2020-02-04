from .models import Membership, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, HiddenInput, Textarea, CharField

class MembershipForm(ModelForm):
    proposal_text = CharField( widget=Textarea(attrs={'placeholder': 'Coverletter'}), label='', help_text='')

    class Meta:
        model = Membership
        fields = ['user', 'project', 'proposal_text']
        widgets = {
            'user': HiddenInput(),
            'project': HiddenInput(),                       
        } 
        exclude = ['is_approve']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')