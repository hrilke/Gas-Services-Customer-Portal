from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm, UserRegistrationForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = Customer.objects.get(email=request.user.email)
            service_request.save()
            return redirect('track_request', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def track_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'service_requests/track_request.html', {'service_request': service_request})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Customer.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                phone_number=''
            )
            return redirect('submit_request')
    else:
        form = UserRegistrationForm()
    return render(request, 'service_requests/register.html', {'form': form})