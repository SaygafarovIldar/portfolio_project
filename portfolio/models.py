from django.db import models
from django.utils.html import mark_safe

from . import utils


# Create your models here.
class Recommendation(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    position = models.CharField(verbose_name="Должность", max_length=300)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    address = models.CharField(verbose_name="Адрес", max_length=255)
    avatar = models.ImageField(upload_to="photos/avatars/", null=True, blank=True, default=None)
    created_at = models.DateTimeField(
        verbose_name="Когда оставлена рекомендация")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекомандацию"
        verbose_name_plural = "Рекомандации"


class ResumeCategory(models.Model):
    title = models.CharField(verbose_name="Заголовок в резюме", max_length=255)

    def __str__(self):
        return self.title


class ResumeItem(models.Model):
    working_place = models.CharField(verbose_name="Место работы", max_length=255)
    working_period_from = models.IntegerField(
        verbose_name="Год начала работы",
        choices=utils.year_choices(),
        default=utils.current_year())
    working_period_to = models.IntegerField(
        verbose_name="Год окончания работы",
        choices=utils.year_choices(),
        default=utils.current_year())
    position = models.CharField(verbose_name="Должность", max_length=255)
    resume_category = models.ForeignKey(
        ResumeCategory, on_delete=models.CASCADE, verbose_name="Заголовок в резюме")
    
    def is_current_year(self):
        return self.working_period_to == utils.current_year()
    
    def __str__(self):
        return self.working_place

    class Meta:
        ordering = ["-working_period_to"]


class Skill(models.Model):
    language = models.CharField(verbose_name="Навык", max_length=255)
    progress = models.IntegerField(
        verbose_name="Процент владения навыком", default=0)

    def __str__(self):
        return self.language


class PortfolioProject(models.Model):
    name = models.CharField(verbose_name="Название проекта", max_length=255)
    link = models.URLField(verbose_name="Ссылка на проект")
    photo = models.ImageField(
        verbose_name="Скриншот проекта", upload_to="photos/")
    project_type = models.CharField(verbose_name="Тип проекта", max_length=255)

    @property
    def thumbnail_preview(self):
        if self.photo:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.photo.url))
        return ""

    def __str__(self):
        return self.name
