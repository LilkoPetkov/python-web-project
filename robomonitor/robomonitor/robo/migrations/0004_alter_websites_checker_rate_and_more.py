# Generated by Django 4.2.3 on 2023-07-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0003_websites_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='checker_rate',
            field=models.CharField(choices=[('5', 'Every 5 Minutes'), ('15', 'Every 15 Minutes'), ('30', 'Every 30 Minutes'), ('60', 'Every 60 Minutes'), ('24', 'Once a day')], default='24', max_length=15),
        ),
        migrations.AlterField(
            model_name='websites',
            name='verification_status',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
