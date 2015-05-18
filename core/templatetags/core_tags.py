# -*- coding: utf-8 -*-
from django import template

from core.controller.utils import module

register = template.Library()

@register.simple_tag
def start_string(slug):
    for reg in module._registry:
        if unicode(reg.SLUG) == unicode(slug):
            return reg.view_results
    return ''
