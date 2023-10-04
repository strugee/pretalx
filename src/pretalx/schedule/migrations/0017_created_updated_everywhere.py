# Generated by Django 4.2.4 on 2023-10-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0016_talkslot_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="availability",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="availability",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="room",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="room",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="schedule",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="talkslot",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="talkslot",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]