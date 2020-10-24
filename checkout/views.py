from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hft6nIrCbRkxyvzaGlrpbZ6wfMG3Zi1CL4769bmsk8XLzYDs34KSRvRcJ8Ge6h5E1PpB8foTmSLE425WVlNyQxp00REMBpLfP',
        'client_secret': 'test client secreet',
    }

    return render(request, template, context)