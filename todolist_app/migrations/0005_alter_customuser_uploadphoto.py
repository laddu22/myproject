# Generated by Django 3.2.16 on 2023-01-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0004_remove_customuser_initialinvestmentamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='UploadPhoto',
            field=models.ImageField(help_text='Please upload recent color photo', upload_to='pics'),
        ),
    ]