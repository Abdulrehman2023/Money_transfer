from atexit import register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', loginview, name="login"),
    path('login2/', login2, name="login2"),
    path('dashboard/', dashboard, name="dashboard"),
    path('add_employee_view/', add_employee_view, name="add_employee_view"),
    path('add_agent_view/', add_agent_view, name="add_agent_view"),
    path('otp/', otp, name="otp"),
    path('resend_otp/', resend_otp, name="resend_otp"),
    path('employee_details/', employee_details, name="employee_details"),
    path('expenses/', expenses, name="expenses"),
    path('balance/', balance, name="balance"),
    path('Balance_details/', Balance_details, name="Balance_details"),







]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
