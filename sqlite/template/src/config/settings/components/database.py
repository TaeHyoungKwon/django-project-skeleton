if ENV == 'development':
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "ttobongee",
            'USER': 'ttobongee',
            'PASSWORD': 'ttobongee1234!',
            'PORT': '5432',
            'HOST': "ttobongee.cow90dnrnqjv.ap-northeast-2.rds.amazonaws.com"
        }
    }