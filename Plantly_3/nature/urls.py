from django.urls import path
from . import views

urlpatterns = [
    path('earth',views.earth, name='earth')
] 