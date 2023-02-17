import stripe
from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.views import generic
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.

class OrdersPageView(generic.TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        permission = Permission.objects.get(codename='special_status')
        request.user.user_permissions.add(permission)
        charge = stripe.Charge.create(
            amount='3900',
            currency='usd',
            description='Purchase all books',
            source = request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')