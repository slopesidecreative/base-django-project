from __future__ import unicode_literals
from django.db import models
# from ..trips.models import Trip

import re
import bcrypt
from . import validations

# MODELS --------------------------------------

class UserManager(models.Manager):
    def register(self,params):
        print('REGISTRATION IN PROCESS...')
        errors = {}

        if not validations.validate_email(params.get('email')):
            errors['email'] = 'Invalid Email.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('first_name'),2):
            errors['first_name'] = 'Invalid First Name.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('last_name'),3):
            errors['last_name'] = 'Invalid Last Name.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_length(params.get('first_name'),1):
            errors['first_name_len'] = 'First name invalid.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_length(params.get('last_name'),1):
            errors['last_name_len'] = 'Last name invalid.'
            print('REGISTRATION ERRORS', errors)



        if not validations.match_strings(params.get('pw1'),params.get('pw2')):
            errors['password'] = 'Passwords do not match.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_length(params.get('pw1'),8) and not validations.validate_length(params.get('pw2'),8):
            errors['password'] = 'Password invalid.'
            print('REGISTRATION ERRORS', errors)
        # validate this to be a valid date, just in case......
        if params.get('hiredate'):
            if not validations.validate_date(params.get('hiredate')):
                errors['start_date_validation'] = 'Not a valid date.'
                print('DATE MUST BE TODAY OR IN THE FUTURE')
            else:
                pass
        else:
            pass

        print('CHECK IF EMAIL ALREADY REGISTERED!',params.get('email'))

        u = self.filter(email = params.get('email'))
        if u:
            errors['already registered'] = "User already registered."
        else:
            print('CHECK PASSED, EMAIL NOT REGISTRED.')
            pass

        # validations done....

        if bool(errors):
            print('-> FAILED REGISTRATION <-', errors)
            result = {'result': False, 'errors': errors}
            return {'result': False, 'errors': errors}

        else:
            print('USER INFO VALIDATED! CREATING USER...',params['pw1'])
            print('NEW USERS PW: ',validations.gen_password(params['pw1']))
            if params['hiredate']:
                new_user = User.objects.create(start_date = params['hiredate'],first_name=params['first_name'],last_name=params['last_name'],email=params['email'],password=validations.gen_password(params['pw1']))
            else:
                new_user = User.objects.create(first_name=params['first_name'],last_name=params['last_name'],email=params['email'],password=validations.gen_password(params['pw1']))

            print('NEW USER:',new_user)
            return {'result': True,'user':new_user}

    def login(self,email,password):
        if validations.validate_email(email):
            errors = {}
            u = self.filter(email=email)
            if u[0]:
                print('LOGGING IN: ',u[0])
                print('USER FOUND, CHECKING PASSWORD... ',u[0].password)
                if bcrypt.hashpw(password.encode(),u[0].password) == u[0].password:
                    return {'self': u[0]}
                else:
                    print('INVALID PASSWORD')
                    return {'errors':'Password incorrect.'}
            else:
                print('INVALID PASSWORD')
                return {'errors':'User not found.'}
        else:
            print('INVALID EMAIL')
            return {'errors':'Invalid email.'}

class User(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    password = models.TextField(max_length=300,default='password error')
    start_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
