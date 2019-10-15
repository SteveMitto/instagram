from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Profile

class UpdateProfile(ModelForm):

    class Meta:
        model = Profile
        fields = ['name','bio','website']
class UpdateProfilePhoto(ModelForm):

    class Meta:
        model=Profile
        exclude = ['user','name','bio','website','acount_stauts']
