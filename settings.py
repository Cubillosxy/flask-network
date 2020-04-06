# sttings

BLOG_NAME = 'Blog FlasK'
WELCOME_MESSAGE = 'Latest news'

LIMIT_PREVIEW_POST = 100

try:
    from local_settings import *
    #print "using localsettings %s" , ( REDIRECT_URI )
except ImportError:
    print ("not localsettings")