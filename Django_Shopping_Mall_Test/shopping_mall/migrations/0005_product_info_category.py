# Generated by Django 5.0.7 on 2024-08-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_mall', '0004_alter_product_info_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_info',
            name='category',
            field=models.CharField(choices=[('Clothing', '의류'), ('Beauty', '뷰티'), ('Food', '식품'), ('Kitchenware', '주방 용품'), ('Daily_Supplies', '생활 용품'), ('Electronic_devices', '전자 기기'), ('Sports', '스포츠 용품')], default='Clothing', max_length=50),
            preserve_default=False,
        ),
    ]
