# Generated by Django 3.0.3 on 2020-04-05 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Series_app', '0012_auto_20200404_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='season_pics',
            name='web_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Web_Series_app.Web_series'),
        ),
    ]
