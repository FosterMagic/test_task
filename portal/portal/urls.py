"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from company_event.views import CompanyAPIVIew, EventAPIVIew, CompanyAPIUpdate, EventAPIUpdate, CompanyAPIDetailView, EventAPIDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from company_event.views import page_not_found, index, about
from portal import settings

# from .views import CompanyAPIVIew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),

    path('api/v1/companies', CompanyAPIVIew.as_view()),
    path('api/v1/companies/<int:pk>/', CompanyAPIUpdate.as_view()),
    path('api/v1/companies_details/<int:pk>/', CompanyAPIDetailView.as_view()),

    path('api/v1/events', EventAPIVIew.as_view()),
    path('api/v1/events/<int:pk>/', EventAPIUpdate.as_view()),
    path('api/v1/event_details/<int:pk>/', EventAPIDetailView.as_view()),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = page_not_found
