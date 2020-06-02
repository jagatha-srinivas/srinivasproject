from django.shortcuts import render
from testapp import forms

# Create your views here.

def thankyou_view(request):
    return  render(request,'test/thankyou.html')




def you_view(request):
    return  render(request,'test/you.html')



def index_view(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            print("studentname",form.cleaned_data['name'])
            print("marks",form.cleaned_data['marks'])
            form.save(commit=True)
            # print("rollno",form.cleaned_data['rollno'])
            # print("email",form.cleaned_data['email'])
            return you_view(request)

    return render(request,'test/index.html',{'form':form})
