# Generated by Django 3.0.3 on 2020-02-14 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit_intents', '0004_auto_20200211_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intentcategory',
            options={'ordering': ('intent_label',)},
        ),
        migrations.AlterModelOptions(
            name='intentslot',
            options={'ordering': ('slot_name',)},
        ),
    ]