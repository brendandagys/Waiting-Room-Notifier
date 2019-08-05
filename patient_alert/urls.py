"""patient_alert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from schedule.views import handle_patient_responses, check_for_status_update

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'.*confirm.*', handle_patient_responses, name='handle_patient_responses'),
    re_path(r'.*update.*', check_for_status_update, name='check_for_status_update'),
    path('schedule/', include('schedule.urls')),
    path('', RedirectView.as_view(url='/schedule/', permanent=True)), # Add URL maps to redirect the base URL to 'schedule' application
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
