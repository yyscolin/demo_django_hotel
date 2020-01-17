from django import forms
from. models import Message

class Message_Form(forms.ModelForm):
    # first_name = forms.CharField(max_length=48)
    # last_name = forms.CharField(max_length=48, required=False)
    # email = forms.CharField(max_length=120)
    # country_code = forms.IntegerField(required=False)
    # phone = forms.IntegerField(required=False)
    # content = forms.CharField()

    class Meta:
        model = Message
        # fields = ('first_name', 'last_name', 'email', 'country_code', 'phone', 'content')
        exclude = ['timestamp',]
        widgets = {
            'country_code': forms.NumberInput(attrs={'placeholder': 65}),
            'content': forms.Textarea(attrs={'placeholder': 'Let us know what you have in mind...', 'rows': 5})
        }
