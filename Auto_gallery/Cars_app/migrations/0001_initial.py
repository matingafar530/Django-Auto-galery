# Generated by Django 4.1.3 on 2022-12-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarsName', models.CharField(max_length=50, verbose_name='نام ماشین')),
                ('CarsImage', models.ImageField(default='E:/Auto_gallery/media/1.jpg', upload_to='CarsImage/', verbose_name='عکس ماشین')),
                ('CarsDescription', models.CharField(max_length=500, verbose_name='توضیحات ماشین')),
                ('Carsfuel', models.IntegerField(verbose_name=(('benzin', 'بنزینی'), ('gaz', 'گازویل'), ('electronic', 'برقی'), ('hybrid', 'دو گانه سوز ')))),
            ],
            options={
                'verbose_name': 'ماشین',
                'verbose_name_plural': 'CAR',
            },
        ),
    ]
