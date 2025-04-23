from django.shortcuts import render, get_object_or_404
from .cart import Cart
from feed.models import Post
from django.http import JsonResponse

def cart_summary(request):
	return render(request, "cart/cart_summary.html", {})

def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))

		# lookup product in DB
		product = get_object_or_404(Post, id=product_id)
		
		# Save to session
		cart.add(product=product)

		# Get cart quantity
		cart_quanity = cart.__len__()

		# Return resonse
		#response = JsonResponse({'Product Name: ': product.sandwich})
		response = JsonResponse({'qty':cart_quanity})
		return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
