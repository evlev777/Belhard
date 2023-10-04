from django.db import models
from django.utils.timezone import now
from django.db.models import Q
from django.db.models.functions import Length

models.CharField.register_class_lookup(Length)


class Category(models.Model):
    name = models.CharField(max_length=24, blank=False, null=False, unique=True, verbose_name='категория')

    slug = models.SlugField(max_length=24, blank=False, null=False, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("категория",)
        verbose_name_plural = "категории"
        ordering = ["name"]
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name="category-length"),
            models.CheckConstraint(check=Q(slug__length__gte=2), name="category_slug-length"),
        )


class Studio(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True, verbose_name='студия')
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "студия"
        verbose_name_plural = "студии"
        ordering = ["name"]
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name='studio-length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='studio_slug-length'),
        )


class Genre(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True, verbose_name='жанр')
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "жанр"
        verbose_name_plural = "жанры"
        ordering = ["name"]
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name='genre-length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='genre_slug-length')
        )


class Quality(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name='качество')
    slug = models.SlugField(max_length=50, blank=False, null=False, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "качество"
        verbose_name_plural = "качество"
        ordering = ["name"]
        constraints = (
            models.CheckConstraint(check=Q(name__length__gte=2), name='quality-length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='quality_slug-length')
        )


class Anime(models.Model):

    title = models.CharField(max_length=128, blank=False, null=False, unique=True, verbose_name='название аниме')
    sub_title = models.CharField(max_length=128, blank=False, null=False, verbose_name='подназвание аниме')
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    image = models.ImageField()

    date_created = models.DateTimeField(default=now, verbose_name='дата опубликования')
    duration = models.IntegerField(default=0, verbose_name='продолжительность аниме')

    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, db_index=True)
    studio = models.ForeignKey(to="Studio", on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)
    quality = models.ManyToManyField(Quality)

    @property
    def date(self):
        return self.date_created.strftime("%H:%M %d %m %Y")

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("аниме",)
        verbose_name_plural = "аниме"
        ordering = ["title"]
        constraints = (
            models.CheckConstraint(check=Q(title__length__gte=2), name='anime_title-length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='anime_slug-title')
        )


class Episode(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=128, blank=False, null=False, unique=True)
    episode = models.ForeignKey(to="Anime", on_delete=models.CASCADE, db_index=True)
    video = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "эпизод"
        verbose_name_plural = "эпизоды"
        ordering = ["title"]
        constraints = (
            models.CheckConstraint(check=Q(title__length__gte=2), name='episode_title-length'),
            models.CheckConstraint(check=Q(slug__length__gte=2), name='episode_slug-length')
        )
