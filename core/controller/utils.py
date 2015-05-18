# -*- coding: utf-8 -*-


class BaseModuleSettings(object):
    pass

class BaseModule(object):

    SETTINGS_CLASS = BaseModuleSettings

    def view_results(self):
        pass


class ModuleSite(object):

    def __init__(self):
        self._registry = {}

    def register(self, model, settings_class):
        self._registry[model] = settings_class

module = ModuleSite()