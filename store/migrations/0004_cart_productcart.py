# Generated by Django 2.2.2 on 2019-07-26 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_categoryimgpath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cartID', models.ForeignKey(db_column='cartID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='store.Cart')),
                ('productID', models.ForeignKey(db_column='productID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='store.Product')),
            ],
        ),
    ]
