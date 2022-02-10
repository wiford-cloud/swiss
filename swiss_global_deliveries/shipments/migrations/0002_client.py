# Generated by Django 3.2.11 on 2022-02-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_item', models.CharField(max_length=100)),
                ('Supplier', models.TextField(max_length=100)),
                ('Description_notes', models.TextField(max_length=100)),
                ('Expected_Date_Delivery', models.DateField()),
                ('Status', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('Name_of_item', 'Supplier', 'Description_notes', 'Expected_Date_Delivery', 'Status'),
            },
        ),
    ]