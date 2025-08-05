from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

from .models import student_details
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save() 
                return render(request, "templates/index.html")
    else:
            form = StudentForm()
            return render(request, 'templates/index.html', {'form': form})
    
   
def process_contactus(request):

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        branch = request.POST['branch']
        bio = request.POST['bio']
        contactusform1 = student_details.objects.create(fname=name, email=email,branch=branch,bio=bio)
        messages.success(request,'Your message has been successfully sent')
        return render(request,"templates/index.html",{'name':name})
    else:
        return HttpResponse("Invalid request method.")