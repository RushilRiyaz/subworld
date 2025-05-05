from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from feed.models import Post
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm


@login_required
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart/cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Post, id=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_quanity = cart.__len__()

        response = JsonResponse({'qty': cart_quanity})
        messages.success(request, ("Sandwich has been added to cart!"))
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        messages.success(request, ("Sandwich has been deleted from cart!"))
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        messages.success(request, ("Your cart has been updated!"))
        return response


def checkout_view(request):
    checkout_type = request.GET.get('type', 'cart')
    form = CheckoutForm(request.POST or None, checkout_type=checkout_type)
    cart = Cart(request)

    if request.method == 'POST':
        if form.is_valid():
            if checkout_type == "premium":
                if request.user.is_authenticated:
                    request.user.profile.premium = True
                    request.user.profile.save()
                    messages.success(
                        request, "Premium membership purchased successfully!")
                    return redirect('feed-home')
                else:
                    request.session['premium_paid_pending'] = True
                    messages.success(
                        request, "Premium membership purchased! Please log in to start enjoying your benefits.")
                    return redirect('login')
            else:
                cart.clear()
                messages.success(request, "Order placed successfully!")
                return redirect('feed-home')

    cart_products = cart.get_prods()
    quantities = cart.get_quants()

    for product in cart_products:
        product.quantity = quantities.get(str(product.id), 0)
        product.subtotal = product.quantity * product.price

    context = {
        'form': form,
        'cart_products': cart_products,
        'totals': cart.cart_total(),
        'checkout_type': checkout_type,
    }
    return render(request, 'cart/checkout.html', context)
