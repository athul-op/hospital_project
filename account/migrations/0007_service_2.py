# Generated by Django 4.2.2 on 2023-07-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_service_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_2',
            fields=[
                ('heading', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('subheading', models.CharField(max_length=100, null=True)),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
            ],
        ),
    ]