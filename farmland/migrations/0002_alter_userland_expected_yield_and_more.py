# Generated by Django 4.1 on 2022-10-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmland', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userland',
            name='expected_yield',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userland',
            name='gross_income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userland',
            name='net_income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userland',
            name='plant',
            field=models.CharField(choices=[('PD', 'Rice'), ('JG', 'Corn'), ('KT', 'Peanut'), ('SK', 'Cassava'), ('UJ', 'Sweet Potato'), ('KE', 'Potato'), ('WO', 'Carrot'), ('BW', 'Onion'), ('TM', 'Tomato'), ('PS', 'Banana'), ('JR', 'Orange')], max_length=2),
        ),
    ]