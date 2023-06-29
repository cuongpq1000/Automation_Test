from shareplum import Site
from shareplum import Office365
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
import json, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([ROOT_DIR, 'config.json'])

# read config file
with open(config_path) as config_file:
    config = json.load(config_file)
    config = config['share_point']

USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']
SHAREPOINT_DOC = config['doc_library']

user_credentials = UserCredential(USERNAME, PASSWORD)
ctx = ClientContext(SHAREPOINT_URL).with_credentials(user_credentials)

web = ctx.web.get().execute_query()
print(web.url)

        