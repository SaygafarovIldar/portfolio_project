# Generated by Django 4.1.3 on 2022-11-09 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('link', models.URLField(verbose_name='Ссылка на проект')),
                ('photo', models.ImageField(upload_to='photos/', verbose_name='Скриншот проекта')),
                ('project_type', models.CharField(max_length=255, verbose_name='Тип проекта')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('position', models.CharField(max_length=300, verbose_name='Должность')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('created_at', models.DateTimeField(verbose_name='Когда оставлена рекомендация')),
            ],
            options={
                'verbose_name': 'Рекомандацию',
                'verbose_name_plural': 'Рекомандации',
            },
        ),
        migrations.CreateModel(
            name='ResumeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок в резюме')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255, verbose_name='Навык')),
                ('progress', models.IntegerField(default=0, verbose_name='Процент владения навыком')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_place', models.CharField(max_length=255, verbose_name='Место работы')),
                ('working_period_from', models.DateField(verbose_name='Год начала работы')),
                ('working_period_to', models.DateField(verbose_name='Год окончания работы')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('resume_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.resumecategory', verbose_name='Заголовок в резюме')),
            ],
        ),
    ]