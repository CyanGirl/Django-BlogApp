from django.conf.urls import include
from django.urls import path
from .views import register, deleteAccount, accountDetails, editAccount

app_name = "usermanage"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("account/delete/<int:pk>/", deleteAccount, name="delete_account"),
    path("account/details/<int:pk>/", accountDetails, name="account_details"),
    path("account/update/<int:pk>/", editAccount, name="edit_account"),
]
