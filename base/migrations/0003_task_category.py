# Generated by Django 4.2.6 on 2023-10-30 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category_rename_desc_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default=3213, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
            preserve_default=False,
        ),
    ]
