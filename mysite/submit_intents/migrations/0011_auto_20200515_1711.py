# Generated by Django 3.0.6 on 2020-05-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit_intents', '0010_auto_20200515_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='intentslot',
            name='excempt_shuffle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='intentslot',
            name='excempt_stemmify',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='intentslot',
            name='excempt_synonym',
            field=models.BooleanField(default=False),
        ),
    ]
