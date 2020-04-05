from linkedin import linkedin
from os import environ

def get_environ(name):
    if name not in environ:
        raise KeyError(f"Environment variable {name} is not set")
    return environ.get(name)


API_KEY = get_environ('LINKEDIN_API_KEY')
API_SECRET = get_environ('LINKEDIN_API_SECRET')
TOKEN = get_environ('LINKEDIN_TOKEN')

app = linkedin.LinkedInApplication(token=TOKEN)

profile = app.get_profile()
print(profile)