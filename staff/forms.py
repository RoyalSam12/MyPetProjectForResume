from django import forms

from .models import Employee, Detail


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'post',
            'salary'
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name[0].isupper():
            return first_name
        else:
            raise forms.ValidationError('Имя должно начитнатся с большой буквы')

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name[0].isupper():
            return last_name
        else:
            raise forms.ValidationError('Фамилия должно начитнатся с большой буквы')


class DetailForm(forms.ModelForm):
    detail_text = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'text__area',
                'rows': 20,
                'cols': 120
            }
        )
    )

    class Meta:
        model = Detail
        fields = [
            'detail_text',
            'address',
            'e_mail'
        ]
