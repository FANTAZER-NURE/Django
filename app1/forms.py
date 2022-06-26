from django.forms import ModelForm, TextInput, DateInput, NumberInput, TimeInput, Select

from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name',
                  'last_name',
                  'patronymic',
                  'phone_number',
                  'time_of_settlement',
                  'date_of_settlement',
                  'room_type']

        text_input = TextInput(attrs={'class': 'content'})
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'First Name'
            }),
            'last_name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'Last Name'
            }),
            'patronymic': TextInput(attrs={
                'class': 'input',
                'placeholder': 'Partomymic'
            }),
            'phone_number': NumberInput(attrs={
                'class': 'input',
                'placeholder': 'Phone number'
            }),
            'time_of_settlement': TimeInput(attrs={
                'class': 'input',
                'placeholder': 'Time',
                'type': 'time'
            }),
            'date_of_settlement': DateInput(attrs={
                'class': 'input',
                'placeholder': 'Date',
                'type': 'date'
            }),
            'room_type': Select(attrs={
                'class': 'input',
                'placeholder': 'Room_type'
            }),


        }
