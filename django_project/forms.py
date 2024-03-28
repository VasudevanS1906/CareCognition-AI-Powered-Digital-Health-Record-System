from django import forms
from .models import Health
from django.utils.translation import gettext_lazy as _

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ['patient_id', 'patient_name', 'age', 'sex', 'reason_for_visit','image']

    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop('language', None)
        super().__init__(*args, **kwargs)

        if self.language == 'hindi':
            self.fields['patient_id'].label = _('रोगी आईडी')
            self.fields['patient_name'].label = _('रोगी का नाम')
            self.fields['age'].label = _('आयु')
            self.fields['sex'].label = _('लिंग')
            self.fields['reason_for_visit'].label = _('यात्रा का कारण')
            self.fields['image'].label = _('छवि')
        elif self.language == 'tamil':
            self.fields['patient_id'].label = _('நோயாளி ஐடி')
            self.fields['patient_name'].label = _('நோயாளி பெயர்')
            self.fields['age'].label = _('வயது')
            self.fields['sex'].label = _('பாலினம்')
            self.fields['reason_for_visit'].label = _('வருகைக்கான காரணம்')
            self.fields['image'].label = _('படம்')
        elif self.language == 'marathi':
            self.fields['patient_id'].label = _('रुग्ण_आयडी')
            self.fields['patient_name'].label = _('रुग्णाचे_नाव')
            self.fields['age'].label = _('वय')
            self.fields['sex'].label = _('लिंग')
            self.fields['reason_for_visit'].label = _('भेटीसाठी_कारण')
            self.fields['image'].label = _('प्रतिमा')





class InputForm(forms.Form):
    patient_id = forms.CharField(label='Patient ID', max_length=100)
    patient_name = forms.CharField(label='Patient Name', max_length=100)
    age = forms.IntegerField(label='Age')
    sex = forms.CharField(label='Sex', max_length=100)
    reason_for_visit = forms.CharField(label='Reason for visit', max_length=100)
    image = forms.ImageField(label='Image')