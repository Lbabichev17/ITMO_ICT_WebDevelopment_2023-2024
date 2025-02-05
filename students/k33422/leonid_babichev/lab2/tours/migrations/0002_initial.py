# Generated by Django 4.0.5 on 2023-11-05 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tourists',
            field=models.ManyToManyField(through='tours.Reservation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tours.reservation'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tours.tour'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='tourist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
