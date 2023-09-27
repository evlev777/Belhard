from django.db import models
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=24, blank=False, null=False, unique=True)

    slug = models.SlugField(max_length=24, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория',
        verbose_name_plural = 'категории'
        ordering = ['name']


class Studios(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'студия'
        verbose_name_plural = 'студии'
        ordering = ['name']




class Genre(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    slug = models.SlugField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
        ordering = ['name']


class Anime(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)
    sub_title = models.CharField(max_length=128, blank=False, null=False)
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, db_index=True)
    date_created = models.DateTimeField(default=now)
    duration = models.CharField(max_length=28, blank=False, null=False)
    views = models.IntegerField(default=0)
    quality = models.CharField(max_length=28, blank=False, null=False)
    studios = models.ForeignKey(to='Studios', on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)





    @property
    def date(self):
        return self.date_created.strftime('%H:%M %d %m %Y')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'аниме',
        verbose_name_plural = 'аниме'
        ordering = ['title']


class Episode(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True)
    episode = models.ForeignKey(to='Anime', on_delete=models.CASCADE, db_index=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'эпизод'
        verbose_name_plural = 'эпизоды'
        ordering = ['title']
