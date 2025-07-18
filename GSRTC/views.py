from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView,TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
# from .models import Driver
# from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.shortcuts import redirect
# Create your views here.
class Home(TemplateView):
    template_name = "admin/index.html"
    
      # Optional: controls the redirect field name in the query string


class Charts(TemplateView):
    template_name = "admin/charts-apexcharts.html"
    
      # Optional: controls the redirect field name in the query string

class Icons(TemplateView):
    template_name = "admin/icons-boxicons.html"
    
      # Optional: controls the redirect field name in the query string

class ChartsApexcharts(TemplateView):
    template_name ="admin/charts-apexcharts.html"
    
      # Optional: controls the redirect field name in the query string


class ChartsEcharts(TemplateView):
    template_name = "admin/charts-echarts.html"
    
      # Optional: controls the redirect field name in the query string

class FormsLayouts(TemplateView):
    template_name = "admin/forms-layouts.html"
    
      # Optional: controls the redirect field name in the query string


class ComponentsAlerts(TemplateView):
    template_name = "admin/components-alerts.html"
    
      # Optional: controls the redirect field name in the query string

class ComponentsButtons(TemplateView):
    template_name="admin/components-buttons.html"
    
      # Optional: controls the redirect field name in the query string

class ComponentsTooltips(TemplateView):
    template_name="admin/components-tooltips.html"
    
      # Optional: controls the redirect field name in the query string

class TablesGeneral(TemplateView):
    
      # Optional: controls the redirect field name in the query string
    template_name = "admin/tables-general.html"

class FormsValidation(TemplateView):
    
      # Optional: controls the redirect field name in the query string
    template_name = "admin/forms-validation.html"

class UserProfile(TemplateView):
    template_name = "admin/users-profile.html"

class PagesRegister(TemplateView):
    template_name = "admin/pages-register.html"

class PagesLogin(TemplateView):
    template_name= "admin/pages-login.html"

class TablesData(TemplateView):
    template_name= "admin/tables-data.html"

class PagesError404(TemplateView):
    template_name = "admin/pages-error-404.html"

class PagesBlank(TemplateView):
    template_name = "admin/pages-blank.html"

class ChartsChartjs(TemplateView):
    template_name = "admin/charts-chartjs.html"

class PagesFaq(TemplateView):
    template_name = "admin/pages-faq.html"

class FormsElements(TemplateView):
    template_name = "admin/forms-elements.html"
    
class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:pages_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')  # or your desired success page
