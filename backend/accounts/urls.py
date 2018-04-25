from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from .views import UserListView, CurrentUserView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('verify/', verify_jwt_token),
    path('users/', UserListView.as_view()),
    path('users/current/', CurrentUserView.as_view())
]
