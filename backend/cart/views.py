from django.shortcuts import render, get_object_or_404
from .cart import Cart
from feed.models import Post
from django.http import JsonResponse

def cart_summary(request):
	# get cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	return render(request, "cart/cart_summary.html", {"cart_products":cart_products, "quantities":quantities})

def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Post, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get cart quantity
		cart_quanity = cart.__len__()

		# Return resonse
		#response = JsonResponse({'Product Name: ': product.sandwich})
		response = JsonResponse({'qty':cart_quanity})
		return response

def cart_delete(request):
    pass

def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		return response
		#return redirect('cart_summary')
		
		
