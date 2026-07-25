
from django import forms
from .models import *


#ticket form
class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
    ('گزارش', 'گزارش'),
    ('انتقاد', 'انتقاد'),
    ('پیشنهاد', 'پیشنهاد'),
    )
    message = forms.CharField(widget=forms.Textarea , required=True)
    name = forms.CharField(max_length=250 , required=True)
    email = forms.CharField(max_length=250)
    phone = forms.CharField(max_length=11 , required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("شماره شما به صورت عددی وارد نشده است ")
            elif len(phone) != 11:
                raise forms.ValidationError("مقدار وارد شده برای شماره تلفن صحیح نمیباشد (11) کاراکتر!!")
            else:
                return phone
        return None
