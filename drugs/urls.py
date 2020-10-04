from django.urls import path
from drugs import views

urlpatterns = [
    path('add/',views.AddView.as_view(),name='add'),
    #path('<str:username>/',views.UserDetailsView.as_view(),name='details'),
]