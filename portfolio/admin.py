from django.contrib import admin

from . import models



class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "phone")
    list_display_links = ("id", "name")
    list_filter = ("position",)


class ResumeCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ("id", "working_place", "working_period_from",
                    "working_period_to", "position", "resume_category")
    list_display_links = ("id", "working_place")
    list_editable = ("working_period_from",
                     "working_period_to", "position")
    list_filter = ("position", "resume_category")


class SkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "language", "progress")
    list_display_links = ("id", "language")
    list_editable = ("progress", )


class PortfolioProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "link", "thumbnail_preview", "project_type")
    list_display_links = ("id", "name", "thumbnail_preview")
    list_editable = ("link",)
    
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    
    thumbnail_preview.short_description = 'Превью'

# Register your models here.
admin.site.register(models.Recommendation, RecommendationsAdmin)
admin.site.register(models.ResumeCategory, ResumeCategoryAdmin)
admin.site.register(models.ResumeItem, ResumeItemAdmin)
admin.site.register(models.Skill, SkillsAdmin)
admin.site.register(models.PortfolioProject, PortfolioProjectsAdmin)

