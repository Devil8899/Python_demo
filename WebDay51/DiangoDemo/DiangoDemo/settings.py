"""
Django settings for DiangoDemo project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pg@qnz_422)77pvss+y4a12%=ytf$(k&uf3l7mghn-nwz2%ewt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#默认创建的表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DiangoDemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], #模板路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DiangoDemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，
# 而且体积很小，所以，经常被集成到各种应用程序中，
# 甚至在iOS和Android的App中都可以集成。
#Python就内置了SQLite3，所以，在Python中使用SQLite，
# 不需要安装任何东西，直接使用。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#配置文件 固定变量
#1.STATIC_URL  指定了公共文件访问路径 创建即存在
# STATIC_URL = '/statics/'
STATIC_URL='/abc/'  #STATIC_URL作用也可以认为是一个别名/abc/=/statics/
#2.告诉giango下的静态文件夹在BASE_DIR 下
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "statics"),  # 实际名 ,即实际文件夹的名字
)


TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

'''

     #静态文件交由Web服务器处理，Django本身不处理静态文件。简单的处理逻辑如下(以nginx为例)：

     #          URI请求-----> 按照Web服务器里面的配置规则先处理，以nginx为例，主要求配置在nginx.
                             #conf里的location

                         |---------->如果是静态文件，则由nginx直接处理

                         |---------->如果不是则交由Django处理，Django根据urls.py里面的规则进行匹配

    # 以上是部署到Web服务器后的处理方式，为了便于开发，Django提供了在开发环境的对静态文件的处理机制，方法是这样：

    #1、在INSTALLED_APPS里面加入'django.contrib.staticfiles',

    #2、在urls.py里面加入
       if settings.DEBUG:  
           urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 
           'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),   
            url(r'^static/(?P<path>.*)$',
          'django.views.static.serve',{'document_root':settings.STATIC_ROOT}), )  

    # 3、这样就可以在开发阶段直接使用静态文件了。

二、MEDIA_ROOT和MEDIA_URL

        #而静态文件的处理又包括STATIC和MEDIA两类，这往往容易混淆，在Django里面是这样定义的：

        #MEDIA:指用户上传的文件，比如在Model里面的FileFIeld，ImageField上传的文件。如果你定义

        #MEDIA_ROOT=c:\temp\media，那么File=models.FileField(upload_to="abc/")＃，上传的文件就会被保存到c:\temp\media\abc  
        #eg：
            class blog(models.Model):  
                   Title=models.charField(max_length=64)  
                   Photo=models.ImageField(upload_to="photo") 
        #     上传的图片就上传到c:\temp\media\photo，而在模板中要显示该文件，则在这样写
        #在settings里面设置的MEDIA_ROOT必须是本地路径的绝对路径，一般是这样写:
                 BASE_DIR= os.path.abspath(os.path.dirname(__file__))  
                 MEDIA_ROOT=os.path.join(BASE_DIR,'media/').replace('\\','/') 

        #MEDIA_URL是指从浏览器访问时的地址前缀，举个例子：
            MEDIA_ROOT=c:\temp\media\photo  
            MEDIA_URL="/data/"
        #在开发阶段,media的处理由django处理：

        #    访问http://localhost/data/abc/a.png就是访问c:\temp\media\photo\abc\a.png

        #    在模板里面这样写<img src="{{MEDIA_URL}}abc/a.png">

        #    在部署阶段最大的不同在于你必须让web服务器来处理media文件，因此你必须在web服务器中配置，
        #  以便能让web服务器能访问media文件
        #    以nginx为例，可以在nginx.conf里面这样：

                 location ~/media/{
                       root/temp/
                       break;
                    }

        #    具体可以参考如何在nginx部署django的资料。

三、STATIC_ROOT和STATIC_URL、
    STATIC主要指的是如css,js,images这样文件，在settings里面可以配置STATIC_ROOT和STATIC_URL,
    配置方式与MEDIA_ROOT是一样的，但是要注意

    #STATIC文件一般保存在以下位置：

    #1、STATIC_ROOT：在settings里面设置，一般用来放一些公共的js,css,images等。

    #2、app的static文件夹，在每个app所在文夹均可以建立一个static文件夹，然后当运行collectstatic时，
    #    Django会遍历INSTALL_APPS里面所有app的static文件夹，将里面所有的文件复制到STATIC_ROOT。因此，
    #   如果你要建立可复用的app，那么你要将该app所需要的静态文件放在static文件夹中。

    # 也就是说一个项目引用了很多app，那么这个项目所需要的css,images等静态文件是分散在各个app的static文件的，比
    #  较典型的是admin应用。当你要发布时，需要将这些分散的static文件收集到一个地方就是STATIC_ROOT。

    #3、STATIC文件还可以配置STATICFILES_DIRS，指定额外的静态文件存储位置。
    #  STATIC_URL的含义与MEDIA_URL类似。

    # ----------------------------------------------------------------------------
    #注意1:
        #为了后端的更改不会影响前端的引入，避免造成前端大量修改

        STATIC_URL = '/static/'               #引用名
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR,"statics")  #实际名 ,即实际文件夹的名字
        )

        #django对引用名和实际名进行映射,引用时,只能按照引用名来,不能按实际名去找
        #<script src="/statics/jquery-3.1.1.js"></script>
        #------error－－－－－不能直接用，必须用STATIC_URL = '/static/':
        #<script src="/static/jquery-3.1.1.js"></script>

    #注意2(statics文件夹写在不同的app下,静态文件的调用):

        STATIC_URL = '/static/'

        STATICFILES_DIRS=(
            ('hello',os.path.join(BASE_DIR,"app01","statics")) ,
        )

        #<script src="/static/hello/jquery-1.8.2.min.js"></script>

    #注意3:
        STATIC_URL = '/static/'
        {% load staticfiles %}
       # <script src={% static "jquery-1.8.2.min.js" %}></script>
'''
