# -*- coding: utf-8 -*-


class IdentificationModule(object):

    def __init__(self, module):
        self.MODULE = module

    def get_module_results(self):
        return self.MODULE.view_results()