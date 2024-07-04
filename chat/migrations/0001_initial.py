# Generated by Django 4.1 on 2024-06-04 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tech_check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('access_token', models.TextField(null=True)),
                ('refresh_token', models.TextField(null=True)),
                ('access_token_expires_at', models.DateTimeField(null=True)),
                ('user_id', models.CharField(max_length=255)),
                ('peer_id', models.CharField(max_length=255)),
                ('supplier_id', models.CharField(max_length=255)),
                ('demand_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_sessions', to='tech_check.post')),
            ],
        ),
    ]