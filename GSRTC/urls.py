from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from .views import RegisterView, CustomLoginView
app_name = 'account'
urlpatterns = [
    path("",Home.as_view(),name="home"),
    # path("login/",Login.as_view(),name="login"),
    path("charts/",Charts.as_view(),name="charts"),
    path("icons/",Icons.as_view(),name="icons"),
    path("charts-apexcharts/",ChartsApexcharts.as_view(), name="charts_apexcharts"),
    path("charts-echarts/", ChartsEcharts.as_view(), name="charts_echarts"),
    path("forms-layouts/", FormsLayouts.as_view(), name="forms_layouts"),
    path("components-alerts/", ComponentsAlerts.as_view(), name="components_alerts"),
    path("components-buttons/",ComponentsButtons.as_view(),name="ponents_buttons"),
    path("components-tooltips/",ComponentsTooltips .as_view()),
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

    #booking
    path('login/', CustomLoginView.as_view(), name='pages_login'),
    path('register/', RegisterView.as_view(), name='pages_register'),
    path('logout/', LogoutView.as_view(next_page='account:pages_login'), name='logout'),
]   
