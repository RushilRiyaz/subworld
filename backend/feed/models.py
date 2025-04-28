from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    VEGAN_CHOICES = [
        ('Non Vegan', 'Non Vegan'),
        ('Vegan', 'Vegan'),
    ]

    TEMP_CHOICES = [
        ('Hot', 'Hot'),
        ('Cold', 'Cold'),
    ]

    SIZE_CHOICES = [
        ('6-inch', '6-inch'),
        ('Footlong', 'Footlong'),
    ]

    BREAD_CHOICES = [
        ('White Italian', 'White Italian'),
        ('9 Grain Wheat', '9 Grain Wheat'),
        ('Multigrain Flatbread', 'Multigrain Flatbread'),
        ('Italian Herbs & Cheese', 'Italian Herbs & Cheese'),
        ('Flatbread', 'Flatbread'),
        ('Gluten Free', 'Gluten Free'),
    ]

    MEAT_CHOICES = [
        ('None', 'No Meat'),
        ('Grilled Chicken', 'Grilled Chicken'),
        ('Turkey', 'Turkey'),
        ('Ham', 'Ham'),
        ('Roast Beef', 'Roast Beef'),
        ('Tuna', 'Tuna'),
        ('Spicy Italian', 'Spicy Italian'),
        ('Bacon', 'Bacon'),
        ('Pepperoni', 'Pepperoni'),
        ('Salami', 'Salami'),
    ]

    CHEESE_CHOICES = [
        ('None', 'No Cheese'),
        ('American', 'American'),
        ('Cheddar', 'Cheddar'),
        ('Pepper Jack', 'Pepper Jack'),
        ('Provolone', 'Provolone'),
        ('Swiss', 'Swiss'),
        ('Mozzarella', 'Mozzarella'),
        ('Vegan Cheese', 'Vegan Cheese'),
    ]

    SAUCE_CHOICES = [
        ('None', 'No Sauce'),
        ('Mayonnaise', 'Mayonnaise'),
        ('Mustard', 'Mustard'),
        ('Honey Mustard', 'Honey Mustard'),
        ('Chipotle Southwest', 'Chipotle Southwest'),
        ('Ranch', 'Ranch'),
        ('Sweet Onion', 'Sweet Onion'),
        ('BBQ Sauce', 'BBQ Sauce'),
        ('Buffalo', 'Buffalo'),
    ]

    VEGGIE_CHOICES = [
        ('None', 'No Vegtables'),
        ('Lettuce', 'Lettuce'),
        ('Spinach', 'Spinach'),
        ('Tomato', 'Tomato'),
        ('Cucumber', 'Cucumber'),
        ('Green Pepper', 'Green Pepper'),
        ('Onion', 'Onion'),
        ('Banana Pepper', 'Banana Pepper'),
        ('Jalapeno', 'Jalapeno'),
        ('Pickle', 'Pickle'),
        ('Olive', 'Olive'),
    ]

    sandwich = models.CharField(max_length=20)
    about = models.CharField(max_length=100, null=True, blank=True)
    vegan = models.CharField(
        max_length=20, choices=VEGAN_CHOICES, default='Non Vegan')
    size = models.CharField(
        max_length=20, choices=SIZE_CHOICES, default='6-inch')
    bread = models.CharField(
        max_length=25, choices=BREAD_CHOICES, default='White Italian')
    meat = models.CharField(
        max_length=20, choices=MEAT_CHOICES, default='None')
    cheese = models.CharField(
        max_length=20, choices=CHEESE_CHOICES, default='None')
    sauce_1 = models.CharField(
        max_length=20, choices=SAUCE_CHOICES, default='None')
    sauce_2 = models.CharField(
        max_length=20, choices=SAUCE_CHOICES, default='None')
    sauce_3 = models.CharField(
        max_length=20, choices=SAUCE_CHOICES, default='None')
    veggie_1 = models.CharField(
        max_length=20, choices=VEGGIE_CHOICES, default='None')
    veggie_2 = models.CharField(
        max_length=20, choices=VEGGIE_CHOICES, default='None')
    veggie_3 = models.CharField(
        max_length=20, choices=VEGGIE_CHOICES, default='None')
    temp = models.CharField(max_length=20, choices=TEMP_CHOICES, default='Hot')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    sandwich_image = models.ImageField(
        default='default_sandwich.jpg', upload_to='sandwich_pics')

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    def __str__(self):
        return self.sandwich

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def number_of_likes(self):
        return self.likes.count()

    def get_sandwich_attributes(self):
        attributes = []
        if self.vegan != 'Non Vegan':
            attributes.append(self.vegan)
        attributes.extend(
            [self.size, self.bread, self.temp])

        if self.meat != 'None':
            attributes.append(self.meat)

        if self.cheese != 'None':
            attributes.append(self.cheese)

        for sauce in [self.sauce_1, self.sauce_2, self.sauce_3]:
            if sauce != 'None':
                attributes.append(sauce)

        for veggie in [self.veggie_1, self.veggie_2, self.veggie_3]:
            if veggie != 'None':
                attributes.append(veggie)

        attributes.append("€" + str(self.price))
        return attributes
