# -*- coding: utf-8 -*-
from django.apps import AppConfig

from core.controller.utils import module
from reports.utils import ReportModuleSettings, ReportModule
from reports import meta

default_app_config = 'reports.ReportsConfig'

module.register(ReportModule, ReportModuleSettings)


class ReportsConfig(AppConfig):
    name = 'reports'
    verbose_name = "Отчётница"