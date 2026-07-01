from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views import View

from .forms import RegisterForm

class LoginView(View):
    template_name = "users/login.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "username_value": "",
                "errors": {},
                "non_field-errors": {}
            }
        )
    
    def post(self, request):
        return render(
            request,
            self.template_name,
            {
                "username_value": ,
                "errors": {},
                "non_field-errors": {}
            }              
        )
        
class RegisterView(View):
    template_name = "users/register.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "username_value": "",
                "email_value": "",
                "errors": {},
                "non_field-errors": {}
            }
        )
    def post(self, request):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    "username_value": request.POST.get("username","").strip(),
                    "email_value":request.POST.get("email", "").strip(),
                    "errors": form.errors,
                    "non_field_errors": form.non_field_errors
                }
            )
        
    user = form.save()
    login(request, user)
    messages.success(request,"Регистрация выполнена")
    return redirect("/")