# Generated by Django 4.1 on 2024-03-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictapi',
            name='ApprovalFY',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='predictapi',
            name='Term',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='predictapi',
            name='Zip',
            field=models.IntegerField(max_length=5),
        ),
    ]
