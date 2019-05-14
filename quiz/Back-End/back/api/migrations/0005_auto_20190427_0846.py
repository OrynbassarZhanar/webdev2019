# Generated by Django 2.2 on 2019-04-27 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20190418_0639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelOptions(
            name='tasklist',
            options={'verbose_name': 'TaskList', 'verbose_name_plural': 'TaskLists'},
        ),
        migrations.AddField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
