from django.urls import path    # grabs urls from main urls.py to access them

from .views import HomePageView, AboutView, InfoView # imports views into urls

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),   # designates home route
  path('about/', AboutView.as_view(), name='about'),
  path('info/', InfoView.as_view(), name='info'),
]