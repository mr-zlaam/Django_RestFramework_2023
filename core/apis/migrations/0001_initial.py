# Generated by Django 5.0 on 2023-12-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('company_type', models.CharField(choices=[('IT', 'IT'), ('non_IT', 'non_IT'), ('Mobiles_phone', 'Mobiles_phone')], max_length=100)),
                ('create_At', models.DateTimeField(auto_now=True)),
                ('is_Active', models.BooleanField(default=True)),
            ],
        ),
    ]