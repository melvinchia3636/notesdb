from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import uuid

def notes_path(instance, filename):
	return f"{instance.subject.id}/{instance.id}.{filename.split('.')[-1]}"

class Grade(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

class Subject(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256)
	short_name = models.CharField(max_length=16)

	def __str__(self):
		return self.name

class Note(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256)
	subject = models.ForeignKey(to="Subject", related_name="notes", on_delete=models.CASCADE)
	grade = models.ForeignKey(to="Grade", related_name="notes", on_delete=models.SET_NULL, null=True)
	author = models.ForeignKey(to=User, related_name="notes", on_delete=models.SET_NULL, null=True)
	published = models.DateTimeField(auto_now_add=True)
	file = models.FileField(upload_to=notes_path, validators=[FileExtensionValidator(['pdf'])])

	def __str__(self):
		return self.name