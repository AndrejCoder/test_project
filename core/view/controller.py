# -*- coding: utf-8 -*-
from django.contrib.admin.helpers import AdminForm
from django.shortcuts import render


def index(request):
    AdminForm
    return render(request, "index.html")

