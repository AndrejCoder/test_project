# -*- coding: utf-8 -*-
from django.db import models


class Report(models.Model):

    name = models.CharField(
        u'Наименование отчёта', max_length=255,
        null=True, blank=True, db_index=True)

    slug = models.CharField(
        u'Код отчёта', max_length=100,
        null=True, blank=True, db_index=True)

    created = models.DateField(
        u'Дата отчёта',
        null=True, blank=True, db_index=True)

    class Meta:
        app_label = u'reports'
        db_table = u'reports_report'
        verbose_name = u'Отчёт'
        verbose_name_plural = u'Отчёты'