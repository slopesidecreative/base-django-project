from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.core.urlresolvers import reverse

# IMPORT VALIDATIONS LIB FROM LOGINREG
from ..loginreg import validations
# IMPORT THE USER FROM LOGINREG
from ..loginreg.models import User

# IMPORT MODELS FROM THIS APP
# from . models import Trip

# ENSURE THERE IS A A LOGGED IN USER ---------------------
# Usage:
#
# if lockdown(request):
#       code to protect.....
# else:
#     return redirect(reverse('user:index'))
def lockdown(request):
    if 'user_id' in request.session:
        return True
    else:
        return False

# Query Reminder ----------------------------------------
# .filter() returns a dict, can be empty or one or many.
# .get() will return an object, errors on not found.
# Query Reminder ----------------------------------------


# CONTROLLERS -------------------------------------------

def show(request):
    if lockdown(request):
        errors = {}

        # CUSTOM ROUTE SPECIFIC VALIDATIONS
        # 1 -
        #errors['any new error'] = 'the new error'

        # then....
        # GRAB ALL FROM MODELS AND GET THEM DISPLAYED

        if bool(errors):
            context = { errors: errors }
            return render(request,'baseapp/index.html',context)
        else:
            # DO IT, ALL IS WELL.....
            context = {}
        return render(request,'baseapp/index.html',context)
    else:
        return redirect(reverse('user:index'))
