import os

def setDefaultEnv():
    if os.getenv("HOST_NAME") is None:
        settings = "iCrawl.settings.dev"
    else:
        settings = "iCrawl.settings.prod"
    return os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
