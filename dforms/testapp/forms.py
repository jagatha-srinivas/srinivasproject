from django import forms
# from django.core import validators
from testapp.models import Student


# def start_with_d(value):
#     if value[0]!='D':
#         raise forms.ValidationError("start with D")


class StudentForm(forms.ModelForm):
    # name=forms.CharField(validators=[start_with_d])
    # rollno=forms.IntegerField()
    # email=forms.EmailField(validators=[validators.MaxLengthValidator(40)])
    class Meta:
        model=Student
        fields='__all__'







    #
    # def clean_name(self):
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError("name issue")
    #     return inputname
    #
    #
    # def clean_email(self):
    #     mail=self.cleaned_data['email']
    #     if len(mail)<4:
    #         raise forms.ValidationError("mail issue")
    #     return mail
    #
    #
    # def clean_rollno(self):
    #     rno=self.cleaned_data['rollno']
    #     if len(str(rno))<4:
    #         raise forms.ValidationError("number issue")
    #     return rno
