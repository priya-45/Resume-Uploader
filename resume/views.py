from django.shortcuts import render
from django.views import View
# Create your views here.
from .froms import ResumeForm
from .models import ResumeModel


class Homeview(View):
    def get(self, request):
        form = ResumeForm()
        candidates = ResumeModel.objects.all()
        return render (request, "home.html",{ "form":form, "candidate":candidates })
    
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render (request, "home.html", {"form":form})
        else:               
            print("Error")
        

class CandidateView(View):
    def get(self, request,pk):
        candidate = ResumeModel.objects.get(pk = pk)
        return render (request, "candidate.html", {"candidate" : candidate})
    
    
