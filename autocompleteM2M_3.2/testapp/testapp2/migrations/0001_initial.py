# Generated by Django 3.2.8 on 2022-02-04 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('finding_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.finding')),
                ('extra', models.CharField(max_length=200)),
            ],
            bases=('testapp.finding',),
        ),
    ]
