from django.urls import path
from .views import InvitationListView, CreateInvitationView, ResolveInvitationView

urlpatterns = [
    path("invitations/", InvitationListView.as_view()),
    path("invitations/create/", CreateInvitationView.as_view()),
    path("invitations/resolve/", ResolveInvitationView.as_view()),
]