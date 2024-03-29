# Generated by Django 2.2.2 on 2019-06-14 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACTIVITY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityName', models.CharField(max_length=50)),
                ('activityCost', models.IntegerField(default=-2147483647)),
                ('activityImages', models.ImageField(upload_to='allImages/')),
            ],
        ),
        migrations.CreateModel(
            name='CITY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to='allImages/')),
            ],
        ),
        migrations.CreateModel(
            name='GROUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GUIDE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(blank=True, max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='allImages/')),
                ('About', models.CharField(blank=True, max_length=50)),
                ('Gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PREFERENCE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferenceNanme', models.CharField(max_length=50)),
                ('preferenceImages', models.ImageField(upload_to='allImages/')),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(blank=True, max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='allImages/')),
                ('About', models.CharField(blank=True, max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('cityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.CITY')),
            ],
        ),
        migrations.CreateModel(
            name='TOURISTSPOT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotName', models.CharField(max_length=75)),
                ('spotInfo', models.CharField(max_length=2000)),
                ('touristSpotImages', models.ImageField(upload_to='allImages/')),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('cityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.CITY')),
            ],
        ),
        migrations.CreateModel(
            name='HOTEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='allImages/')),
                ('longitude', models.CharField(blank=True, max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=30)),
                ('cityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.CITY')),
            ],
        ),
        migrations.CreateModel(
            name='BLOG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogCaption', models.CharField(max_length=200)),
                ('blogPostDate', models.DateField(auto_now_add=True)),
                ('blogData', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='allImages/')),
                ('guideID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planner.GUIDE')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planner.USER')),
            ],
        ),
    ]
