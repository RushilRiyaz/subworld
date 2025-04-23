from feed.models import Post

class Cart():
	def __init__(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		# Make sure cart is available on all pages of site
		self.cart = cart

	def cart_total(self):
		# Get product IDS
		product_ids = self.cart.keys()
		# lookup those keys in our products database model
		products = Post.objects.filter(id__in=product_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for product in products:
				if product.id == key:
					total = total + (product.price * value)
				#! TODO: Possible place to implement premium member offer. 
		return total


	def add(self, product, quantity):
		product_id = str(product.id)
		product_qty = str(quantity)
		# Logic
		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

	def __len__(self):
		return len(self.cart)
	
	def get_prods(self):
		# Get ids from cart
		product_ids = self.cart.keys()
		# use ids to lookup sandwiches in db
		products = Post.objects.filter(id__in=product_ids)

		return products
	
	def get_quants(self):
		quantities = self.cart
		return quantities
	
	def update(self, product, quantity):
		product_id = str(product)
		product_qty = int(quantity)

		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[product_id] = product_qty

		self.session.modified = True

	def delete(self, product):
		product_id = str(product)
		# Delete from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True