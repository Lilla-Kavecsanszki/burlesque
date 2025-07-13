from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.timezone import now
from .models import Profile

# View to handle subscription selection
@login_required
def choose_subscription(request):
    if request.method == 'POST':
        selected_plan = request.POST.get('plan')

        # Validate selected plan
        if selected_plan in dict(Profile.SUBSCRIPTION_CHOICES):
            profile = request.user.profile
            profile.subscription = selected_plan
            profile.subscribed_at = now()
            profile.save()

            # TODO: Redirect to Stripe checkout in the future
            return redirect('subscription_success')  # Ensure this URL name exists

    return redirect('subscription_page')  # Fallback if POST invalid

# View to display the subscription page
def subscription_page(request):
    return render(request, 'subscription/subscription_page.html')
