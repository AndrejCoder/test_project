# -*- encoding: utf-8 -*-
from django.contrib import admin

from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created']
    search_fields = ['name', 'slug']
    list_per_page = 100
    list_max_show_all = 3000

admin.site.register(Report, ReportAdmin)
