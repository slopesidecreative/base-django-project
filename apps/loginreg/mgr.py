
from django.db import models
import re
import validations

# NOTE: THIS IS NOT IN USE AS I WAS NOT ABLE TO ACCESS THE USER OBJECT HERE
# SO IT HAS BEEN MOVED TO MODELS.py BUT I WANTED TO KEEP THIS FILE TO SEE IF
# IT CAN BE MADE TO WORK LATER...

class UserManager(models.Manager):
    # TODO: why is self have to be passed in?
    def register(self,params):
        print('REGISTRATION IN PROCESS...')
        errors = {}

        if not validations.validate_email(params.get('email')):
            errors['email'] = 'Invalid Email.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('first_name'),2):
            errors['first_name'] = 'Invalid First Name.'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('last_name'),2):
            errors['last_name'] = 'Invalid Last Name.'
            print('REGISTRATION ERRORS', errors)

        if not validations.match_strings(params.get('pw1'),params.get('pw2')):
            errors['password'] = 'Passwords do not match!'
            print('REGISTRATION ERRORS', errors)

        if not validations.validate_letters(params.get('pw1'),8) and not validations.validate_letters(params.get('pw2'),8):
            errors['password'] = 'Passwords need to be 8 characters!'
            print('REGISTRATION ERRORS', errors)

        if errors:
            print('-> FAILED REGISTRATION <-', errors)
            result = {'result': False, 'errors': errors}
            return {'result': False, 'errors': errors}

        else:
            print('USER INFO VALIDATED! CREATING USER...')
            result = {'result': True}
            return result

    def login(self,email,password):
        print('LOGIN IN PROCESS....')
        if validations.validate_email(email):
            errors = {}
            # find returns a list, can be empty
            u = User.objects.find(email=email)
            if u[0]:
                print('USER FOUND. NOW MATCHING PASSWORDS.....')
                # compare hashed pw entered against hashed pw stored
                print(bcrypt.hashpw(password))
                print(u[0].password)
                if bcrypt.hashpw(password) == u[0].password:
                    return {'self': u[0]}
                else:
                    print('PASSWORD NOT MATCH'')
                    return False
            else:
                print('DID NOT FIND A USER TO LOGIN!!'')
                # ERROR INVALID EMAIL
                return False
        else:
            return False
