# -*- coding: utf-8 -*-

from core.controller.utils import BaseModule, BaseModuleSettings
from reports.meta import SLUG


class ReportModuleSettings(BaseModuleSettings):
    pass

class ReportModule(BaseModule):

    SETTINGS_CLASS = ReportModuleSettings
    SLUG = SLUG

    @property
    def view_results(self):
        view_list = [u'Фильтр', u'Отчёт', u'Экспорт']
        return view_list
