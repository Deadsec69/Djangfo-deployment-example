from django.shortcuts import render

def index(request):
    context_dict={"text":"helloasdfgdsf","number":1000}
    return render(request,'basic_app/index.html',context_dict)

# Create your views here.
def other(request):
    return render(request,'basic_app/other.html')

def relative_path_template(request):
    return render(request,'basic_app/relative_path_template.html')
