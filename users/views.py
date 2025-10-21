from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register new user."""
    if request.method != 'POST':
        # Display form for user refistration.
        form = UserCreationForm()
    else:
        # Managing filled form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Login user and redirect him to the main page.
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Displaying empty form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)