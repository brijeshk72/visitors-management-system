# Generated by Django 2.2.4 on 2019-08-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('ptm', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='pics')),
                ('signature', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
