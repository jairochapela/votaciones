# Generated by Django 4.2.2 on 2023-07-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='available_from',
            field=models.DateTimeField(null=True, verbose_name='available from'),
        ),
        migrations.AlterField(
            model_name='question',
            name='available_until',
            field=models.DateTimeField(null=True, verbose_name='available until'),
        ),
    ]
