# Generated by Django 4.1.2 on 2022-10-16 19:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('alt', models.CharField(blank=True, max_length=200, null=True)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'abstract': False,
            },
        ),
    ]
