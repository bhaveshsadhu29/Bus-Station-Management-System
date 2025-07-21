from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView,TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm,ScheduleForm
from .models import CustomUser,Bus,Route,Schedule
# from .models import Driver
# from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.shortcuts import redirect
# Create your views here.
class Home(LoginRequiredMixin,TemplateView):
    template_name = "admin/index.html"
    
      # Optional: controls the redirect field name in the query string


class Charts(LoginRequiredMixin,TemplateView):
    template_name = "admin/charts-apexcharts.html"
    
      # Optional: controls the redirect field name in the query string

class BoxIcons(LoginRequiredMixin,TemplateView):
    template_name = "admin/icons-boxicons.html"
    
      # Optional: controls the redirect field name in the query string

class ChartsApexcharts(LoginRequiredMixin,TemplateView):
    template_name ="admin/charts-apexcharts.html"
    
      # Optional: controls the redirect field name in the query string


class ChartsEcharts(LoginRequiredMixin,TemplateView):
    template_name = "admin/charts-echarts.html"
    
      # Optional: controls the redirect field name in the query string

class FormsLayouts(LoginRequiredMixin,TemplateView):
    template_name = "admin/forms-layouts.html"
    
      # Optional: controls the redirect field name in the query string


class ComponentsAlerts(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-alerts.html"
    
      # Optional: controls the redirect field name in the query string

class ComponentsButtons(LoginRequiredMixin,TemplateView):
    template_name="admin/components-buttons.html"
    
      # Optional: controls the redirect field name in the query string

class ComponentsTooltips(LoginRequiredMixin,TemplateView):
    template_name="admin/components-tooltips.html"
    
      # Optional: controls the redirect field name in the query string

class TablesGeneral(LoginRequiredMixin,TemplateView):
    
      # Optional: controls the redirect field name in the query string
    template_name = "admin/tables-general.html"

class FormsValidation(LoginRequiredMixin,TemplateView):
    
      # Optional: controls the redirect field name in the query string
    template_name = "admin/forms-validation.html"

class UserProfile(LoginRequiredMixin,TemplateView):
    template_name = "admin/users-profile.html"

class PagesRegister(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages-register.html"

class PagesLogin(LoginRequiredMixin,TemplateView):
    template_name= "admin/pages-login.html"

class TablesData(LoginRequiredMixin,TemplateView):
    template_name= "admin/tables-data.html"

class PagesError404(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages-error-404.html"

class PagesBlank(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages-blank.html"

class ChartsChartjs(LoginRequiredMixin,TemplateView):
    template_name = "admin/charts-chartjs.html"

class PagesFaq(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages-faq.html"

class FormsElements(LoginRequiredMixin,TemplateView):
    template_name = "admin/forms-elements.html"

class ComponentsAccordion(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-accordion.html"

class ComponentsBadges(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-badges.html"    

class ComponentsBreadcrumbs(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-breadcrumbs.html"
class ComponentsCards(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-cards.html"

class ComponentsListGroup(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-list-group.html"

class ComponentsCarousel(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-carousel.html"

class ComponentsModal(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-modal.html"

class ComponentsTabs(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-tabs.html"

class ComponentsPagination(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-pagination.html"

class ComponentsProgress(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-progress.html"

class ComponentsSpinners(LoginRequiredMixin,TemplateView):
    template_name = "admin/components-spinners.html"
    
class FormsEditors(LoginRequiredMixin,TemplateView):
    template_name = "admin/forms-editors.html"

class IconsBootstrap(LoginRequiredMixin,TemplateView):
    template_name = "admin/icons-bootstrap.html"

class IconsRemix(LoginRequiredMixin,TemplateView):
    template_name = "admin/icons-remix.html"

class PagesContact(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages-contact.html"
class StationList(LoginRequiredMixin,TemplateView):
    template_name = "admin/station-list.html"

class StationForm(LoginRequiredMixin,TemplateView):
    template_name = "admin/station-form.html"

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'admin/booking/page-register.html'
    success_url = reverse_lazy('account:pages_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'admin/booking/page-login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account:home')  # or your desired success page





class BusListView(LoginRequiredMixin,ListView):
    model = Bus
    template_name = 'admin/transport/bus_list.html'
    context_object_name = 'buses'

class BusCreateView(LoginRequiredMixin,CreateView):
    model = Bus
    fields = ['number_plate', 'driver_name', 'capacity']
    template_name = 'admin/transport/bus_form.html'
    success_url = reverse_lazy('account:bus_list')

class BusUpdateView(LoginRequiredMixin,UpdateView):
    model = Bus
    fields = ['number_plate', 'driver_name', 'capacity']
    template_name = 'admin/transport/bus_form.html'
    success_url = reverse_lazy('account:bus_list')

class BusDeleteView(LoginRequiredMixin,DeleteView):
    model = Bus
    template_name = 'admin/transport/bus_confirm_delete.html'
    success_url = reverse_lazy('account:bus_list')

class BusDetailView(LoginRequiredMixin,DetailView):
    model = Bus
    template_name = 'admin/transport/bus_detail.html'



class RouteListView(LoginRequiredMixin,ListView):
    model = Route
    template_name = 'admin/transport/route_list.html'
    context_object_name = 'routes'


class RouteCreateView(LoginRequiredMixin,CreateView):
    model = Route
    fields = ['origin', 'destination', 'distance_km']
    template_name = 'admin/transport/route_form.html'
    success_url = reverse_lazy('account:route_list')


class RouteUpdateView(LoginRequiredMixin,UpdateView):
    model = Route
    fields = ['origin', 'destination', 'distance_km']
    template_name = 'admin/transport/route_form.html'
    success_url = reverse_lazy('account:route_list')


class RouteDeleteView(LoginRequiredMixin,DeleteView):
    model = Route
    template_name = 'admin/transport/route_confirm_delete.html'
    success_url = reverse_lazy('account:route_list')


class RouteDetailView(LoginRequiredMixin,DetailView):
    model = Route
    template_name = 'admin/transport/route_detail.html'


class ScheduleListView(LoginRequiredMixin,ListView):
    model = Schedule
    context_object_name = 'schedules'
    template_name = 'admin/transport/schedule_list.html'  # adjust as needed

class ScheduleDetailView(LoginRequiredMixin,DetailView):
    model = Schedule
    template_name = 'admin/transport/schedule_detail.html'

class ScheduleCreateView(LoginRequiredMixin,CreateView):
    model = Schedule
    form_class = ScheduleForm
    # fields = ['bus', 'route', 'departure_time', 'arrival_time']
    template_name = 'admin/transport/schedule_form.html'
    success_url = reverse_lazy('account:schedule_list')

class ScheduleUpdateView(LoginRequiredMixin,UpdateView):
    model = Schedule
    form_class = ScheduleForm
    # fields = ['bus', 'route', 'departure_time', 'arrival_time']
    template_name = 'admin/transport/schedule_form.html'
    success_url = reverse_lazy('account:schedule_list')

class ScheduleDeleteView(LoginRequiredMixin,DeleteView):
    model = Schedule
    template_name = 'admin/transport/schedule_confirm_delete.html'
    success_url = reverse_lazy('account:schedule_list')