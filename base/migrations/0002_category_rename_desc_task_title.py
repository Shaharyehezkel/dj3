# Generated by Django 4.2.6 on 2023-10-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='desc',
            new_name='title',
        ),
    ]
