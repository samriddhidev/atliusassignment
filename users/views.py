from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .forms import UserRegisterForm,ProfileUpdateform

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('profile')
        
        else:
            form =UserRegisterForm()
        
        return render(request, 'users/register.html',{'form':form})
@login_required
def profile(request):
    if request.method=='POST':
        p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if p_form.isvalid():
            p_form.save()
            return redirect('profile')
    
    else:
        p_form= ProfileUpdateForm()
    return render(request, 'users/profile.html',{'p_form':p_form})
