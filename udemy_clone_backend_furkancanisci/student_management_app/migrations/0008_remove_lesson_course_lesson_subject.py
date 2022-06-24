# Generated by Django 4.0.5 on 2022-06-12 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(default=33.7, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='student_management_app.subjects'),
            preserve_default=False,
        ),
    ]
