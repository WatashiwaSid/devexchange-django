from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stackbase.models import Question

# Create your views here.
def register(request):
    if(request.method=='POST'):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"User {username} registered successfully.")
            return redirect("stackbase:home")
    else:
        form = UserRegisterForm()
    return render(request, "./register.html", {"form":form})

@login_required
def profile(request):
    user = request.user
    # Query to get questions asked by the user
    user_questions = Question.objects.filter(user=user).order_by('-date_created')

    # Context to pass to the template
    context = {
        'user': user,
        'user_questions': user_questions
    }

    return render(request, "./profile.html", context)

@login_required
def profileUpdate(request):
    if(request.method=='POST'):
        usrupdtform = UserUpdateForm(request.POST, instance=request.user)
        profileupdtform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if usrupdtform.is_valid() and profileupdtform.is_valid():
            usrupdtform.save()
            profileupdtform.save()
            messages.success(request, f"Profile Updated Successfully")
            return redirect("profile")
    else:
        usrupdtform = UserUpdateForm(request.POST, instance=request.user)
        profileupdtform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    context = {
        'usrupdtform' : usrupdtform,
        'profileupdtform': profileupdtform
    }
    return render(request, "./profileUpdate.html", context)