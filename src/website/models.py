from django.db import models
from django.core.exceptions import ValidationError
import os
import zipfile

def validate_file_type(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov', '.avi', '.mkv']
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are: {", ".join(valid_extensions)}')

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media_files = models.ManyToManyField('ProjectMedia', blank=True, related_name='projects')

    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    file = models.FileField(upload_to='project_media/', blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media {self.id}"

class GalleryMedia(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='gallery_media/', blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery Media {self.id}"

class GalleryUpload(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    zip_file = models.FileField(upload_to='gallery_zips/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Gallery Upload"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.zip_file:
            self.extract_zip()

    def extract_zip(self):
        if self.zip_file:
            zip_path = self.zip_file.path
            extract_path = os.path.join('media', 'gallery_media', str(self.id))
            os.makedirs(extract_path, exist_ok=True)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            # Save extracted media files to GalleryMedia model
            for filename in os.listdir(extract_path):
                file_path = os.path.join(extract_path, filename)
                GalleryMedia.objects.create(file=file_path)