# Generated by Django 4.0.1 on 2022-01-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_class_ka',
            field=models.CharField(default='ಕನ್ನಡ', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='prod_desc_ka',
            field=models.CharField(default='ಕನ್ನಡ', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='prod_name_ka',
            field=models.CharField(default='ಕನ್ನಡ', max_length=50),
            preserve_default=False,
        ),
    ]
