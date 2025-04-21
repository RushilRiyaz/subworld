from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    VEGAN_CHOICES = [
    ('Vegan', 'Vegan'),
    ('Non Vegan', 'Non Vegan'),
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
        ('White Bread', 'White Bread'),
        ('Brown Bread', 'Brown Bread'),
    ]
    
    MEAT_CHOICES = [
    ('Turkey', 'Turkey'),
    ('Chicken', 'Chicken'),
    ('Ham', 'Ham'),
    ('Beef', 'Beef'),
    ('Tuna', 'Tuna'),
    ('Salami', 'Salami'),
    ('None', 'No Meat'),
    ]

    PRICE_CHOICES = [
        ('Under $5', 'Under $5'),
        ('$5 - $10', '$5 - $10'),
        ('$10 - $15', '$10 - $15'),
        ('Above $15', 'Above $15'),
    ]

    SAUCE_CHOICES = [
        ('Mayonnaise', 'Mayonnaise'),
        ('Mustard', 'Mustard'),
        ('Ketchup', 'Ketchup'),
        ('BBQ Sauce', 'BBQ Sauce'),
        ('Ranch', 'Ranch'),
        ('Sweet Onion', 'Sweet Onion'),
        ('Chipotle Southwest', 'Chipotle Southwest'),
        ('Honey Mustard', 'Honey Mustard'),
        ('Hot Sauce', 'Hot Sauce'),
        ('None', 'No Sauce'),
    ]

    VEGGIE_CHOICES = [
        ('Lettuce', 'Lettuce'),
        ('Tomato', 'Tomato'),
        ('Onion', 'Onion'),
        ('Cucumber', 'Cucumber'),
        ('Pickle', 'Pickle'),
        ('Olive', 'Olivs'),
        ('Jalapeno', 'Jalapeno'),
        ('Green Pepper', 'Green Pepper'),
        ('None', 'No Vegtables'),
    ]

    sandwich = models.CharField(max_length=100)
    about = models.CharField(max_length=300, null=True, blank=True)
    vegan = models.CharField(max_length=20, choices=VEGAN_CHOICES, default='Non Vegan')
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='6-inch')
    bread = models.CharField(max_length=20, choices=BREAD_CHOICES, default='White Bread')
    meat = models.CharField(max_length=20, choices=MEAT_CHOICES, default='Chicken')
    sauce_1 = models.CharField(max_length=20, choices=SAUCE_CHOICES, default='None')
    sauce_2 = models.CharField(max_length=20, choices=SAUCE_CHOICES, default='None')
    sauce_3 = models.CharField(max_length=20, choices=SAUCE_CHOICES, default='None')
    veggie_1 = models.CharField(max_length=20, choices=VEGGIE_CHOICES, default='None')
    veggie_2 = models.CharField(max_length=20, choices=VEGGIE_CHOICES, default='None')
    veggie_3 = models.CharField(max_length=20, choices=VEGGIE_CHOICES, default='None')
    temp = models.CharField(max_length=20, choices=TEMP_CHOICES, default='Hot')
    price = models.CharField(max_length=20, choices=PRICE_CHOICES, default='$10 - $15')
    sandwich_image = models.ImageField(default='default_sandwich.jpg', upload_to='sandwich_pics')

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
        attributes.extend([self.size, self.bread, self.temp, self.meat])
        
        for sauce in [self.sauce_1, self.sauce_2, self.sauce_3]:
            if sauce != 'None':
                attributes.append(sauce)
                
        for veggie in [self.veggie_1, self.veggie_2, self.veggie_3]:
            if veggie != 'None':
                attributes.append(veggie)
        
        attributes.append(self.price)
        return attributes