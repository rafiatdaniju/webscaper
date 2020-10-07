import dj_database_url
from decouple import config

def gen_db(debug):
    if debug:
        return {
            'default': {
            'ENGINE': config('ENGINE'),
            'NAME': config('NAME'),
            'USER': config('USER'),
            'PASSWORD': config('PASSWORD'),
            'HOST': config('HOST'),
            'PORT': config('PORT', cast=int),
        }
    }

    else:
        return {
            "default": {
                "ENGINE": config("ENGINE"),
                **dj_database_url.parse(config("DATABASE_URL")),
            }
        }