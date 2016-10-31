#
#       VALIDATIONS
#

# IMPORTS
import re, bcrypt
import datetime
from six import string_types

#
# DATE & TIME
# DJANGO's & BOOTSTRAP's DATE FORMAT --> YYYY-MM-DD
#
# now = datetime.datetime.now()
# d = datetime.datetime(now.year, now.month, now.day)

# CHECK AGAINST TODAYS DATE
def date_today(date_text):
    #today or in the future
    return date_text >= datetime.datetime.now().strftime('%Y-%m-%d')
# VALID DATE STRING?
def validate_date(date_text):
    try:
        # HTML5 DATE PICKER FORMAT
        date = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False
# PASSWORD
def gen_password(password):
    print('*'*20)
    print('PASSWORD ENCRYPTION IN PROCESS...')
    print('*'*20)
    print('PASSWORD CREATED: ',bcrypt.hashpw(password.encode(),bcrypt.gensalt()))
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())
# EMAIL
def validate_email(email):
    print('*'*20)
    print('VALIDATING EMAIL...')
    print('*'*20)
    if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
        print('*'*20)
        print('EMAIL VALID!!')
        print('*'*20)
        return(True)
    else:
        print('*'*20)
        print('EMAIL FAIL!!')
        print('*'*20)
        return(False)
# STRING AND ITS LENGTH
def validate_length(strng,length=1):
    print('*'*20)
    print('VALIDATING STRING LENGTH...')
    print('*'*20)
    if len(strng) >= length:
        print('*'*20)
        print('LENGTH VALID!!')
        print('*'*20)
        return(True)
    else:
        print('*'*20)
        print('LENGTH NOT VALID!!')
        print('*'*20)
        return(False)
# LETTERS AND LENGTH
def validate_letters(strng,length=3):
    print('WHHHSKSKSKSKSKSKSKSKSKSKSKSK')
    return True
    print('*'*20)
    # print('VALIDATING STRING...')
    print('*'*20)
    if len(strng) > length:
        print('WHHHSKSKSKSKSKSKSKSKSKSKSKSK')
        try:
          basestring
        except NameError:
          basestring = str
        if isinstance(s, basestring):
            print('*'*20)
            print('CHARS VALID!!')
            print('*'*20)
            return(True)
        else:
            print('*'*20)
            print('CHARS TEST FAIL!!')
            print('*'*20)
            return(False)
    else:
        print('*'*20)
        print('CHARS TEST FAIL!!')
        print('*'*20)
        return(False)
# MATCH TWO STRINGS
def match_strings(s1,s2):
    print('*'*20)
    print('MATCHING STRINGS...',s1,s2)
    print('*'*20)
    if str(s1) == str(s2):
        print('STRINGS MATCH!')
        return True
    else:
        print('STRINGS DONT MATCH!')
        return False
