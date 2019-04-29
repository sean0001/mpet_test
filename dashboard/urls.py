from django.urls import path
import dashboard.views


USERS_URL_PATTERNS = [
path("testpage", dashboard.views.testpage, name='testpage'),
path("test_partial", dashboard.views.test_partial, name='test_partial'),
#path("users/login2", apps.msite.users.login, name='login2')
]