# Generated by Django 5.1.4 on 2024-12-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
