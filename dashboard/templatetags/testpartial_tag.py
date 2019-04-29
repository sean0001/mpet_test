from django import template
from django.template.loader import get_template

TEMPLATE="dashboard/partial/test1.html"

register = template.Library()

@register.inclusion_tag(TEMPLATE)
def show_partial_test1():
    list1 = ("11111","22222","333333","44444")
    return {"data1" : list1};






def show_partial_test2():
    list1 = ("11111","22222","333333","44444")
    return {"data1" : list1};

t = get_template(TEMPLATE)
register.inclusion_tag(t)(show_partial_test2)


#使用主页中的变量
@register.inclusion_tag("dashboard/partial/test3.html", takes_context=True)
def show_partial_test3(context):
    ss = context
    list1 ={"link" : context["home_link"],"title" : context["home_title"],"path" : context["request"].path}
    return list1
