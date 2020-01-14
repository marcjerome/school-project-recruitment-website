from .models import Membership
from django.forms import ModelForm, HiddenInput

class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = ['user', 'project', 'proposal_text']
        widgets = {
            'user': HiddenInput(),
            'project': HiddenInput(),
        } 
        exclude = ['is_approve']