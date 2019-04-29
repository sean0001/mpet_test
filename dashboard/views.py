from django.shortcuts import render
from django.db import transaction
from django.urls import utils
from django.template import Context, Template

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



def testpage(request):
    c = {'home_link': 'home_link_Context',"home_title":"home_title_Context","name":"seanmoo"}
    return render(request,"dashboard/view/testpage.html",c)



def test_partial(request):
    c ={"project_name":"django框架","project_version":"12.0.1"}
    return render(request, "dashboard/partial/test4.html", c)