import datetime


def year_choices():
    return [(r, r) for r in range(2000, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


def get_project_types(projects_queryset):
    return set([project.project_type for project in projects_queryset])
