# sttings

BLOG_NAME = 'Blog FlasK'
WELCOME_MESSAGE = 'Latest news'

LIMIT_PREVIEW_POST = 100


MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True

MAIL_USERNAME = ''
MAIL_PASSWORD = ''


try:
    from local_settings import *
    #print "using localsettings %s" , ( REDIRECT_URI )
except ImportError:
    print ("not localsettings")