from django.shortcuts import render
from django.db import transaction
from django.urls import utils

# Create your views here.
@transaction.non_atomic_requests
def testtrans(request):

    try:
        pass
    except Exception:
        pass
    finally:
        pass

    with transaction.on_commit():
        pass