# Generated by Django 3.2.2 on 2021-05-10 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_cart_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Владелец'),
        ),
    ]
