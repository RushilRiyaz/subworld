from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
import json
from cart.cart import Cart
from django.contrib.auth.views import LoginView
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            wants_premium = cleaned_data.get('premium', False)

            form.cleaned_data['premium'] = False
            user = form.save()

            messages.success(
                request, f'Your account has been created! You are now able to log in.')

            if wants_premium:
                return redirect(reverse('checkout') + '?type=premium')

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        post_data = request.POST.copy()
        if 'premium' in post_data:
            del post_data['premium']

        p_form = ProfileUpdateForm(
            post_data, request.FILES, instance=request.user.profile)

        was_premium = request.user.profile.premium

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()

            # Check actual checkbox value from original post
            if request.POST.get('premium') == 'on' and not was_premium:
                return redirect(reverse('checkout') + '?type=premium&from=profile')

            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        current_user = Profile.objects.get(user=self.request.user)

        saved_cart = current_user.old_cart
        if saved_cart:
            converted_cart = json.loads(saved_cart)
            cart = Cart(self.request)
            for key, value in converted_cart.items():
                cart.db_add(product=key, quantity=value)

        if self.request.session.pop('premium_paid_pending', False):
            current_user.premium = True
            current_user.save()
            messages.success(
                self.request, "Your premium membership is now active!")

        return response
