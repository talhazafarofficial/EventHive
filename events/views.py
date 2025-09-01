from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from .models import Event, Booking
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm


def home(request):
    events = Event.objects.order_by('-date')[:3]  # Show latest 3 events
    return render(request, 'home.html', {'events': events})
def events_list(request):
    events = Event.objects.all().order_by('date')
    query = request.GET.get('q') or ''
    category = request.GET.get('category') or 'all'
    location = request.GET.get('location') or 'all'

    filtered = events

    if query:
        filtered = filtered.filter(title__icontains=query)

    if category != 'all':
        filtered = filtered.filter(category__iexact=category)

    if location != 'all':
        filtered = filtered.filter(location__icontains=location)

    return render(request, 'events_list.html', {
        'events': filtered,
        'search': query,
        'category': category,
        'location': location,
    })

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.seats_available > 0:
        Booking.objects.create(user=request.user, event=event)
        event.seats_available -= 1
        event.save()

        # Send email confirmation
        send_mail(
            subject='Event Booking Confirmation',
            message=f'Thank you {request.user.username}, your booking for "{event.title}" has been received! Our team will contact you shortly with further details.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
        )

    return redirect('dashboard')

@login_required
def dashboard(request):
    user = request.user
    bookings = Booking.objects.filter(user=user).select_related('event').order_by('-booked_at')[:5]

    return render(request, 'dashboard.html', {
        'user': user,
        'bookings': bookings,
    })
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def profile(request):
    user = request.user
    profile = request.user.profile
    bookings = Booking.objects.filter(user=user).select_related('event')

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'bookings': bookings,
        'is_editing': request.method == 'POST' or request.GET.get('edit') == '1',
    })
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_subject = f"Contact Form: {subject}"
        email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, ['Enter your Email'])

        # Redirect back or render a success template
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})