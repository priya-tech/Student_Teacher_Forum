# Generated by Django 2.2.5 on 2020-03-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addusermodel',
            name='usertype',
            field=models.CharField(choices=[('S', 'Student'), ('F', 'Faculty')], default='S', max_length=2),
        ),
    ]