from django.shortcuts import render
from django.db import transaction

# Create your views here.
@transaction.non_atomic_requests
def testtrans(request):
## test for  django transaction
    try:
        pass
    except Exception:
        pass
    finally:
        pass

    with transaction.on_commit():
        pass