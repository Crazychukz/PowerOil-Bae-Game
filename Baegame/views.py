from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import TemplateView
import operator
from django.http import HttpResponseRedirect
from django.views.decorators.http import condition
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from Baegame.models import *
from django.contrib.auth.models import User
from django.template import Context, Template
from Baegame.forms import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from django.core import signing
from django.views import View
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.debug import sensitive_post_parameters
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
import datetime
from django_modalview.generic.edit import ModalFormView
from django_modalview.generic.component import ModalResponse
import random

class HomeViews(View):


    template_name = 'index.html'


    def get(self, request, *args, **kwargs):
        form1 = RequestInviteForm()

        return render(request, 'index.html' , {'form' : form1})

    def post(self, request, *args, **kwargs):
        form = RequestInviteForm(data = request.POST)
        if form.is_valid():
            ans01 = request.POST.get('ans01', '')
            ans02 = request.POST.get('ans02', '')
            ans03 = request.POST.get('ans03', '')
            store = Test(ans01=ans01 , ans02=ans02, ans03=ans03)
            store.save()
            modal01 = 'modal01'
            return render(request, 'index.html', {'modal01': modal01})
        variables ={
            'form' : form
        }

        return render(request, 'index.html', variables)




