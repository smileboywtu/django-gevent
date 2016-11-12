from django.shortcuts import render

# Create your views here.

import json
from models import NotesType, Notes
from django.http import HttpResponse


def notes(request):
    """
    return all notes

    :param request:
    :return:
    """
    notes = Notes.objects.all().values('title', 'content', 'type')
    return HttpResponse(json.dumps({
        "result": list(notes)
    }))


def types(request):
    """
    return all node type
    :param request:
    :return:
    """
    types = NotesType.objects.all().values('name', 'desc')
    return HttpResponse(json.dumps({
        "result": list(types)
    }))
