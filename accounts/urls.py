from django.urls import path
from accounts.views import (
    UserProfileView, SignUpView, LoginUserView, LogoutUserView
)

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),        # Sign-up view
    path('login/', LoginUserView.as_view(), name='login'),       # Login view
    path('logout/', LogoutUserView.as_view(), name='logout'),    # Logout view
    path('profile/', UserProfileView.as_view(), name='profile'), # Profile view
]
