# Generated by Django 2.2.10 on 2020-05-25 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grinder_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Playlist',
        ),
        migrations.AddField(
            model_name='grinderuser',
            name='spid',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='grinder_api.grinderuser'),
        ),
        migrations.AddField(
            model_name='track',
            name='spid',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]