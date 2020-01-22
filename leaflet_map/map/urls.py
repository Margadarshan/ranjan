from django.urls import path,include
# from .views import HomePageView,contact
from .views import homepage,databaseshow


urlpatterns = [
    # path('', HomePageView.as_view(),name='home'),
    # path('', contact,name='contact'),
    path('',homepage,name='home'),
    path('databasemap/',databaseshow,name='dbshow'),
    
]