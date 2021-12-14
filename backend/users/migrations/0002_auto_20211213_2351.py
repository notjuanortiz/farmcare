# Generated by Django 3.2.10 on 2021-12-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0002_auto_20211213_2351'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='usercrop',
            name='unique_user_crop',
        ),
        migrations.AlterField(
            model_name='farmcareuser',
            name='crops',
            field=models.ManyToManyField(related_name='crops', through='users.UserCrop', to='crops.Crop'),
        ),
        migrations.AlterField(
            model_name='usercrop',
            name='user_submitted_image',
            field=models.CharField(max_length=255),
        ),
        migrations.AddConstraint(
            model_name='usercrop',
            constraint=models.UniqueConstraint(fields=('user', 'crop'), name='user_crop_id'),
        ),
    ]