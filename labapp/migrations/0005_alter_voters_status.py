# Generated by Django 3.2.2 on 2021-06-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0004_alter_voters_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
    ]