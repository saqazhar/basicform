from django.shortcuts import render
from . import froms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_name(request):
    form = froms.FormName()

    if request.method == 'post':
        form = forms.FormName(request.post)

        if form.is_valid:
            print('Validation is success you can move forward')

            print('UserName:'+form.cleaned_data['User_Name'])
            print('Email:' + form.cleaned_data['Email'])
            print('Text:' + form.cleaned_data['Text'])

    return render(request, 'form_page.html', {'form': form})