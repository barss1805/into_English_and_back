from django.db import models


class Sentence(models.Model):
    time = models.ForeignKey('Time', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    eng_lang = models.CharField(max_length=1000)
    rus_lang = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.eng_lang


class Time(models.Model):
    name_time = models.CharField(max_length=100)
    parent_time = models.ForeignKey('self', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_time


class Success(models.Model):
    RESULTS = (
        ("-1","Fail"),
        ("0","Not started yet"),
        ("1","Correct"),
    )

    sentence =models.ForeignKey(Sentence,on_delete=models.PROTECT)
    date_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=3, choices=RESULTS, default="0")