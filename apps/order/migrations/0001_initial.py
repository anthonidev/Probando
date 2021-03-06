# Generated by Django 3.2.5 on 2022-06-27 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('No Procesado', 'Not Processed'), ('Procesado', 'Processed'), ('Enviado', 'Shipping'), ('Entregado', 'Delivered'), ('Cancelado', 'Cancelled')], default='No Procesado', max_length=50)),
                ('transaction_id', models.CharField(max_length=255, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=20)),
                ('city', models.CharField(choices=[('Amazonas', 'Amazonas'), ('Áncash', 'Áncash'), ('Apurímac', 'Apurímac'), ('Arequipa', 'Arequipa'), ('Ayacucho', 'Ayacucho'), ('Cajamarca', 'Cajamarca'), ('Callao', 'Callao'), ('Cusco', 'Cusco'), ('Huancavelica', 'Huancavelica'), ('Huánuco', 'Huánuco'), ('Ica', 'Ica'), ('Junín', 'Junín'), ('La Libertad', 'Lalibertad'), ('Lambayeque', 'Lambayeque'), ('Lima', 'Lima'), ('Loreto', 'Loreto'), ('Madre de Dios', 'Madrededios'), ('Moquegua', 'Moquegua'), ('Pasco', 'Pasco'), ('Piura', 'Piura'), ('Puno', 'Puno'), ('San Martín', 'Sanmartín'), ('Tacna', 'Tacna'), ('Tumbes', 'Tumbes'), ('Ucayali', 'Ucayali')], default='Lima', max_length=255)),
                ('postal_zip_code', models.CharField(max_length=20)),
                ('telephone_number', models.CharField(max_length=255)),
                ('shipping_name', models.CharField(max_length=255)),
                ('shipping_time', models.CharField(max_length=255)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('enterprise', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('count', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='product.product')),
            ],
        ),
    ]
