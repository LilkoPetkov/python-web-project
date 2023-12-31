# Generated by Django 4.2.3 on 2023-07-20 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0007_logs_website_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robo.websites'),
        ),
        migrations.AlterField(
            model_name='websites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
