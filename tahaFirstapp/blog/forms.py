from django import forms


#ticket form
class TicketForm(forms.ModelForm):
    SUBJECT_CHOICEs = (
    ('گزارش', 'گزارش'),
    ('انتقاد', 'انتقاد'),
    ('پیشنهاد', 'پیشنهاد'),
    )
    message = forms.CharField(widget=forms.Textarea , required=True)
    name = forms.CharField(max_length=250 , required=True)
    email = forms.CharField(max_length=250)
    phone = forms.CharField(max_length=11 , required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICEs)

