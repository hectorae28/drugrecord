from django.urls import path,include
from users import views

urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path('<str:username>/',views.UserDetailsView.as_view(),name='details'),
]