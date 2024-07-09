# Generated by Django 4.2.5 on 2024-07-09 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=255)),
                ('month_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurer', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('clubbed_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transform.category')),
            ],
        ),
    ]
