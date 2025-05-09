# Generated by Django 5.2 on 2025-04-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_remove_post_bread_type_post_bread_post_meat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(choices=[('<5', 'Under $5'), ('5-10', '$5 - $10'), ('10-15', '$10 - $15'), ('>15', 'Above $15')], default='10-15', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='vegan',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='sauces',
            field=models.ManyToManyField(blank=True, to='feed.sauce'),
        ),
    ]
