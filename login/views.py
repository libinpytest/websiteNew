from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homeland')
        else:
            # Authentication failed, show an error message or redirect back to the login page
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    
    return render(request, 'login')

def profile_view(request):
    # Logic to handle the profile page
    return render(request, 'profile.html')