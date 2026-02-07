# Import render function to render templates with context data
from django.shortcuts import render
# Import reverse_lazy for lazy URL reversing (evaluates URL at runtime, not import time)
from django.urls import reverse_lazy
# Import Django's built-in form for creating new users with username and password
from django.contrib.auth.forms import UserCreationForm
# Import generic class-based views module
from django.views import generic

# Define a class-based view for handling user signup/registration
class SignUpView(generic.CreateView):
    # Specify the form class to use for creating new users
    form_class = UserCreationForm
    # Define the URL to redirect to after successful form submission (goes to login page)
    success_url = reverse_lazy('login')
    # Specify the template file to render for displaying the signup form
    template_name = 'signup.html'