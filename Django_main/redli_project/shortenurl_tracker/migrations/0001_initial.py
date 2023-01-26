# Generated by Django 4.0.2 on 2022-12-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entered_url', models.CharField(default='', max_length=50)),
                ('end_url', models.CharField(default='', max_length=50)),
                ('safe', models.CharField(default='', max_length=50)),
                ('domain', models.CharField(default='', max_length=50)),
                ('ip_address', models.CharField(default='', max_length=50)),
                ('spamming', models.CharField(default='', max_length=50)),
                ('Malware', models.CharField(default='', max_length=50)),
                ('Phishing', models.CharField(default='', max_length=50)),
                ('Server', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='s_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_original', models.CharField(default='', max_length=30)),
                ('shorted_url', models.CharField(default='', max_length=30)),
            ],
        ),
    ]