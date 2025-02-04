from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from accounts.forms import SignUpForm, ProfileForm
from accounts.models import Profile
from django.http import HttpResponseForbidden

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/change_profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:profile')

class SignUpView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully')
        return super().form_valid(form)

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy

class LoginUserView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user

        # Email content
        subject = 'Welcome to Asenwi ElectroWorld!'
        main_page_url = self.request.build_absolute_uri(reverse_lazy('shop:home'))  # Generate the absolute URL for the main page
        message = (
            f"Hi {user.username},\n\n"
            f"Thank you for logging in to Asenwi ElectroWorld.\n"
            f"You can explore our products and services by visiting our main page: {main_page_url}\n\n"
            f"We are thrilled to have you with us!\n\n"
            f"Best Regards,\n"
            f"The Asenwi ElectroWorld Team"
        )
        from_email = 'salah10saeed@gmail.com'
        recipient_list = [user.email]

        # Send email
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Success message
        messages.success(self.request, 'You have been logged in successfully. A welcome email has been sent.')
        return response


    def get_success_url(self):
        return reverse_lazy('shop:home')

from django.contrib.auth.views import LogoutView
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('shop:home')

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            messages.warning(self.request, 'You have been logged out')
            return super().dispatch(request, *args, **kwargs)
        elif request.method == 'GET':
            # Display a confirmation page before logging out
            return render(request, 'accounts/logout_confirmation.html')
        return HttpResponseForbidden("Invalid request method. Please use POST for logging out.")

