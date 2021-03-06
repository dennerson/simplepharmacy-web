# Generated by Django 3.2.7 on 2022-06-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SANITARYPRODUCTS', 'Sanitary Products'), ('BEAUTYPRODUCTS', 'Beauty Products'), ('HYGIENEPRODUCTS', 'Hygiene Products'), ('MEDICINES', 'Medicines'), ('VITAMINSKIDS', 'Vitamins Kids'), ('VITAMINSADULT', 'Vitamins Adult')], max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('New', 'primary'), ('Limited only', 'secondary'), ('Hot', 'danger')], max_length=15),
        ),
    ]
