from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import CustomerProfile

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            # Ensure the customer profile exists for the current user
            if hasattr(request.user, 'customerprofile'):
                service_request.customer = request.user.customerprofile
                service_request.save()
                return redirect('track_requests')  # Redirect after successful submission
            else:
                # Return an error page if customer profile doesn't exist
                return render(request, 'customer_service/error.html', {
                    'message': 'Customer profile does not exist. Please contact support.'
                })
    else:
        form = ServiceRequestForm()
    
    # Render the form for GET requests
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    # Check if the user already has a CustomerProfile
    if not CustomerProfile.objects.filter(user=request.user).exists():
        CustomerProfile.objects.create(user=request.user)
    
    requests = ServiceRequest.objects.filter(customer=request.user.customerprofile)
    return render(request, 'customer_service/track_request.html', {'requests': requests})


@login_required
def manage_requests(request):
    if request.user.is_staff:
        all_requests = ServiceRequest.objects.all()
        return render(request, 'customer_service/manage_requests.html', {'all_requests':all_requests})
    else:
        return redirect('home')



def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('track_requests')
    else:
        form = AuthenticationForm()
    return render(request, 'customer_service/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            # Only create a CustomerProfile if it doesn't already exist
            CustomerProfile.objects.get_or_create(user=user)
            
            login(request, user)  # Log the user in after registration
            return redirect('track_request')  # Redirect to tracking page
    else:
        form = UserRegistrationForm()
    
    return render(request, 'customer_service/register.html', {'form': form})