# Generated by Django 5.0.2 on 2024-02-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_organizer', '0003_alter_recipe_recipe_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_picture',
            field=models.ImageField(upload_to='recipes_images/'),
        ),
    ]
