from django.shortcuts import render

# Create your views here.
def homePage(request):
    context={}
    return render(request,template_name='index.html',context=context)