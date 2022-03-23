from dataclasses import fields
from django.forms import ModelForm
from .models import *

class CourseForm(ModelForm):
    class meta:
        model=Courses
        fields="_all_"