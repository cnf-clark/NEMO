# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-15 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def add_and_set_default_interlock_category(apps, schema_editor):
    InterlockCardCategory = apps.get_model("NEMO", "InterlockCardCategory")
    InterlockCard = apps.get_model("NEMO", "InterlockCard")
    stanford_category = InterlockCardCategory.objects.create(name="Stanford", key="stanford")
    InterlockCardCategory.objects.create(name="WebRelayHttp", key="web_relay_http")
    for interlock_card in InterlockCard.objects.all():
        interlock_card.category = stanford_category
        interlock_card.save()

class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0009_version_1_19_0'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterlockCardCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, help_text="The name for this interlock category")),
                ('key', models.CharField(max_length=100, help_text="The key to identify this interlock category by in interlocks.py")),
            ],
            options={
                'verbose_name_plural': 'Interlock card categories',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='interlockcard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='NEMO.InterlockCardCategory'),
        ),
        migrations.AddField(
            model_name='interlockcard',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='interlockcard',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='interlockcard',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='interlockcard',
            name='even_port',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interlockcard',
            name='odd_port',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interlockcard',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interlock',
            name='channel',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Channel/Relay'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='grant_physical_access_level_upon_qualification',
            field=models.ForeignKey(blank=True,
                                    help_text='The designated physical access level is granted to the user upon qualification for this tool.',
                                    null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='NEMO.PhysicalAccessLevel'),
        ),
        migrations.AlterField(
            model_name='door',
            name='interlock',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='NEMO.Interlock'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='descendant',
            field=models.OneToOneField(blank=True,
                                       help_text='Any time a reservation is moved or resized, the old reservation is cancelled and a new reservation with updated information takes its place. This field links the old reservation to the new one, so the history of reservation moves & changes can be easily tracked.',
                                       null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ancestor',
                                       to='NEMO.Reservation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       to='NEMO.UserPreferences'),
        ),
        migrations.RunPython(add_and_set_default_interlock_category),
    ]
