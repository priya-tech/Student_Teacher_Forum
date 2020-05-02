# Generated by Django 2.2.5 on 2020-03-13 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0006_addquestionsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAnswersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumapp.AddQuestionsModel')),
            ],
        ),
    ]