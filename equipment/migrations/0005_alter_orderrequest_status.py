# Generated by Django 4.2.10 on 2024-07-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_remove_orderrequest_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrequest',
            name='status',
            field=models.CharField(choices=[('Pending', '承認待ち'), ('Approved', '承認済み')], default='Pending', max_length=100),
        ),
    ]