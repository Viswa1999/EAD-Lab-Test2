# Generated by Django 3.2.2 on 2021-06-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0003_alter_voters_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
