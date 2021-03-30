# Generated by Django 2.2.12 on 2020-08-10 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classassignment',
            name='student',
            field=models.ManyToManyField(related_name='assignment', to='classroom.Student'),
        ),
        migrations.AlterField(
            model_name='classassignment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='classroom.Teacher'),
        ),
        migrations.AlterField(
            model_name='submitassignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submit', to='classroom.Student'),
        ),
        migrations.AlterField(
            model_name='submitassignment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submit', to='classroom.Teacher'),
        ),
    ]