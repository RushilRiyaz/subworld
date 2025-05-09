# Generated by Django 5.2 on 2025-04-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0020_alter_post_about_alter_post_sandwich'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bread',
            field=models.CharField(choices=[('White Italian', 'White Italian'), ('9 Grain Wheat', '9 Grain Wheat'), ('Multigrain Flatbread', 'Multigrain Flatbread'), ('Italian Herbs & Cheese', 'Italian Herbs & Cheese'), ('Flatbread', 'Flatbread'), ('Gluten Free', 'Gluten Free')], default='White Italian', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='meat',
            field=models.CharField(choices=[('Grilled Chicken', 'Grilled Chicken'), ('Turkey', 'Turkey'), ('Ham', 'Ham'), ('Roast Beef', 'Roast Beef'), ('Tuna', 'Tuna'), ('Spicy Italian', 'Spicy Italian'), ('Bacon', 'Bacon'), ('Pepperoni', 'Pepperoni'), ('Salami', 'Salami'), ('None', 'No Meat')], default='Grilled Chicken', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='sauce_1',
            field=models.CharField(choices=[('Mayonnaise', 'Mayonnaise'), ('Mustard', 'Mustard'), ('Honey Mustard', 'Honey Mustard'), ('Chipotle Southwest', 'Chipotle Southwest'), ('Ranch', 'Ranch'), ('Sweet Onion', 'Sweet Onion'), ('BBQ Sauce', 'BBQ Sauce'), ('Buffalo', 'Buffalo'), ('Oil', 'Oil'), ('Vinegar', 'Vinegar'), ('Salt', 'Salt'), ('Pepper', 'Pepper'), ('None', 'No Sauce')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='sauce_2',
            field=models.CharField(choices=[('Mayonnaise', 'Mayonnaise'), ('Mustard', 'Mustard'), ('Honey Mustard', 'Honey Mustard'), ('Chipotle Southwest', 'Chipotle Southwest'), ('Ranch', 'Ranch'), ('Sweet Onion', 'Sweet Onion'), ('BBQ Sauce', 'BBQ Sauce'), ('Buffalo', 'Buffalo'), ('Oil', 'Oil'), ('Vinegar', 'Vinegar'), ('Salt', 'Salt'), ('Pepper', 'Pepper'), ('None', 'No Sauce')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='sauce_3',
            field=models.CharField(choices=[('Mayonnaise', 'Mayonnaise'), ('Mustard', 'Mustard'), ('Honey Mustard', 'Honey Mustard'), ('Chipotle Southwest', 'Chipotle Southwest'), ('Ranch', 'Ranch'), ('Sweet Onion', 'Sweet Onion'), ('BBQ Sauce', 'BBQ Sauce'), ('Buffalo', 'Buffalo'), ('Oil', 'Oil'), ('Vinegar', 'Vinegar'), ('Salt', 'Salt'), ('Pepper', 'Pepper'), ('None', 'No Sauce')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='vegan',
            field=models.CharField(choices=[('Non Vegan', 'Non Vegan'), ('Vegan', 'Vegan')], default='Non Vegan', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='veggie_1',
            field=models.CharField(choices=[('Lettuce', 'Lettuce'), ('Spinach', 'Spinach'), ('Tomato', 'Tomato'), ('Cucumber', 'Cucumber'), ('Green Pepper', 'Green Pepper'), ('Onion', 'Onion'), ('Banana Pepper', 'Banana Pepper'), ('Jalapeño', 'Jalapeño'), ('Pickle', 'Pickle'), ('Olive', 'Olivs'), ('None', 'No Vegtables')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='veggie_2',
            field=models.CharField(choices=[('Lettuce', 'Lettuce'), ('Spinach', 'Spinach'), ('Tomato', 'Tomato'), ('Cucumber', 'Cucumber'), ('Green Pepper', 'Green Pepper'), ('Onion', 'Onion'), ('Banana Pepper', 'Banana Pepper'), ('Jalapeño', 'Jalapeño'), ('Pickle', 'Pickle'), ('Olive', 'Olivs'), ('None', 'No Vegtables')], default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='veggie_3',
            field=models.CharField(choices=[('Lettuce', 'Lettuce'), ('Spinach', 'Spinach'), ('Tomato', 'Tomato'), ('Cucumber', 'Cucumber'), ('Green Pepper', 'Green Pepper'), ('Onion', 'Onion'), ('Banana Pepper', 'Banana Pepper'), ('Jalapeño', 'Jalapeño'), ('Pickle', 'Pickle'), ('Olive', 'Olivs'), ('None', 'No Vegtables')], default='None', max_length=20),
        ),
    ]
