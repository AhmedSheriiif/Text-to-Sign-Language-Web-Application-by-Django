from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Word(models.Model):
    spelling = models.CharField(max_length=50, unique=True)
    video_path = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.spelling


class Translations(models.Model):
    translated_by = models.ForeignKey(User, related_name='translations', on_delete=models.CASCADE)
    word_translated = models.ForeignKey(Word, related_name='translations', on_delete=models.CASCADE)
    translated_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Word: {self.word_translated}, Translated By: {self.translated_by}"


