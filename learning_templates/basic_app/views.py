from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'name':'Summa Lumma', 'number':7}
    return render(request,'basic_app/index.html', dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_urls_template.html')
