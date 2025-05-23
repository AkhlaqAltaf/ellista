# Generated by Django 4.2.17 on 2025-02-10 08:44

from django.db import migrations, models
import src.website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='gallery_media/', validators=[src.website.models.validate_file_type])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='project_media/', validators=[src.website.models.validate_file_type])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='GalleryImage',
        ),
        migrations.RemoveField(
            model_name='galleryupload',
            name='images',
        ),
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
        migrations.AddField(
            model_name='project',
            name='media_files',
            field=models.ManyToManyField(blank=True, related_name='projects', to='website.projectmedia'),
        ),
    ]
