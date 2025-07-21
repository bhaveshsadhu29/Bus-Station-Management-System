from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from .views import RegisterView, CustomLoginView
app_name = 'account'
urlpatterns = [
    path("",Home.as_view(),name="home"),
    # path("login/",Login.as_view(),name="login"),
    path("charts/",Charts.as_view(),name="charts"),
    path("icons/",BoxIcons.as_view(),name="icons"),
    path("charts-apexcharts/",ChartsApexcharts.as_view(), name="charts_apexcharts"),
    path("charts-echarts/", ChartsEcharts.as_view(), name="charts_echarts"),
    path("forms-layouts/", FormsLayouts.as_view(), name="forms_layouts"),
    path("components-alerts/", ComponentsAlerts.as_view(), name="components_alerts"),
    path("components-buttons/",ComponentsButtons.as_view(),name="ponents_buttons"),
    path("components-tooltips/",ComponentsTooltips.as_view(),name="components_tooltips"),
    path("tables-general/", TablesGeneral.as_view(), name="tables_general"),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('register/', UserRegisterView.as_view(), name='register'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path("profile/", Profile.as_view(), name="Profile"),
    path("forms-validation/", FormsValidation.as_view(), name="forms_validation"),
    path("users-profile/",UserProfile.as_view(), name="users_profile"),
    path("pages-register/",PagesRegister.as_view(), name="pages_register"),
    path("pages-login/", PagesLogin.as_view(), name="pages_login"),
    path("tables-data/", TablesData.as_view(), name="tables_data"),
    path("pages-error-404/", PagesError404.as_view(), name="pages_error_404"),
    path("pages-blank/", PagesBlank.as_view(), name="pages_blank"),
    path("charts-chartjs/", ChartsChartjs.as_view(), name="charts_chartjs"),
    path("pages-faq/", PagesFaq.as_view(), name="pages_faq"),
    path("forms-elements/", FormsElements.as_view(), name="forms_elements"),
    path("components-accordion/", ComponentsAccordion.as_view(), name="components_accordion"),
    path("components-badges/", ComponentsBadges.as_view(), name="components_badges"),
    path("components-breadcrumbs/", ComponentsBreadcrumbs.as_view(), name="components_breadcrumbs"),
    path("components-cards/", ComponentsCards.as_view(), name="components_cards"),
    path("components-carousel/", ComponentsCarousel.as_view(), name="components_carousel"),
    path("components-list-group/", ComponentsListGroup.as_view(), name="components_list_group"),
    path("components-modal/", ComponentsModal.as_view(), name="components_modal"),
    path("components-tabs/", ComponentsTabs.as_view(), name="components_tabs"),
    path("components-pagination/", ComponentsPagination.as_view(), name="components_pagination"),
    path("components-progress/", ComponentsProgress.as_view(), name="components_progress"),
    path("components-spinners/", ComponentsSpinners.as_view(), name="components_spinners"),
    path("forms-editors/", FormsEditors.as_view(), name="forms_editors"),
    path("icons-bootstrap/", IconsBootstrap.as_view(), name="icons_bootstrap"),
    path("icons-remix/", IconsRemix.as_view(), name="icons_remix"),
    path("pages-contact/", PagesContact.as_view(), name="pages_contact"),
    path("station-list/", StationList.as_view(), name="station_list"),
    path("station-form/", StationForm.as_view(), name="station_form"),
    #booking
    path('login/', CustomLoginView.as_view(), name='pages_login'),
    path('register/', RegisterView.as_view(), name='pages_register'),
    path('logout/', LogoutView.as_view(next_page='account:pages_login'), name='logout'),



    # crud of bus
    path('buses/', BusListView.as_view(), name='bus_list'),
    path('buses/add/', BusCreateView.as_view(), name='bus_add'),
    path('buses/<int:pk>/edit/', BusUpdateView.as_view(), name='bus_edit'),
    path('buses/<int:pk>/delete/', BusDeleteView.as_view(), name='bus_delete'),
    path('buses/<int:pk>/', BusDetailView.as_view(), name='bus_detail'),


    # Route CRUD
    path('routes/', RouteListView.as_view(), name='route_list'),
    path('routes/add/', RouteCreateView.as_view(), name='route_add'),
    path('routes/<int:pk>/edit/', RouteUpdateView.as_view(), name='route_edit'),
    path('routes/<int:pk>/delete/', RouteDeleteView.as_view(), name='route_delete'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route_detail'),
#   CRUD schedules
    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/add/', ScheduleCreateView.as_view(), name='schedule_add'),
    path('schedules/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedules/<int:pk>/edit/', ScheduleUpdateView.as_view(), name='schedule_edit'),
    path('schedules/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
]   
