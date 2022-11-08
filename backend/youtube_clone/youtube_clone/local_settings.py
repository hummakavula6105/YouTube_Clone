# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^h=nbawb(s)xq4cojm8^ik9vu6897n($+h)m150u302le@4zz1'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'youtube_clone',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '@StarGazing13',
    }
}