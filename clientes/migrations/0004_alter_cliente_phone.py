# Generated by Django 5.0.2 on 2024-03-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_address_cliente_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='phone',
            field=models.CharField(max_length=2555, null=True),
        ),
    ]
