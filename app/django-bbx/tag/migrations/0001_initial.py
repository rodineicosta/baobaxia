# Generated by Django 2.1.4 on 2018-12-20 20:08

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, default='', max_length=60)),
                ('note', models.TextField(blank=True, max_length=300)),
                ('name', models.CharField(max_length=26)),
                ('policies', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('priorize', 'priorize'), ('postSave_copyToTaina', 'postSave_copyToTaina'), ('sync', 'sync')], max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('namespace', 'name')},
        ),
    ]
