from django import forms
from .models import ResumeModel


GENDER_CHOICE = (
    ("Male","Male"),
    ('Female',"Female")
)

JOB_CITY = [
    ("Delhi","Delhi"),
    ("Mumbai","Mumbai"),
    ("Gujrat","Gujrat"),
    ("Bangalore","Bangalore"),
    ("Hyderabad","Hyderabad"),
    ("Pune","Pune")
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label="Preferred Job Location",choices=JOB_CITY, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = ResumeModel
        fields = "__all__"

        labels = {"name":"Full Name", "dob":"Date of Birth", "pin": "Pin Code", 
                  "mobile_number": "Mobile No.", "email":"Email ID",  
                  "profilephoto":"Profile Image", "my_file":"Document"
                  }
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.SelectDateWidget(),
            "locality":forms.TextInput(attrs={"class":"form-control"}),
            "city":forms.TextInput(attrs={"class":"form-control"}),
            "pin":forms.NumberInput(attrs={"class":"form-control"}),
            "state":forms.Select(attrs={"class":"form-select"}),
            "mobile_number":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})

        }