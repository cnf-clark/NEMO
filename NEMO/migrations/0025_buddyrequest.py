# Generated by Django 2.2.13 on 2020-11-05 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0024_contactinformation_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuddyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time when the request was created.')),
                ('start', models.DateTimeField(help_text='The start date and time the user is requesting a buddy.')),
                ('end', models.DateTimeField(help_text='The end date and time the user is requesting a buddy.')),
                ('description', models.TextField(help_text='The description of the request.')),
                ('expired', models.BooleanField(default=False, help_text="Indicates the request has expired and won't be shown anymore.")),
                ('deleted', models.BooleanField(default=False, help_text="Indicates the request has been deleted and won't be shown anymore.")),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NEMO.Tool')),
                ('user', models.ForeignKey(help_text='The user who is submitting the request.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_replies', models.ManyToManyField(blank=True, help_text='Users who have responded to the request.', related_name='user_replies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]