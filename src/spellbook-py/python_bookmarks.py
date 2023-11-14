import base64
import datetime
import hashlib
import json
import os
import re
import requests
from time import sleep

from requests.auth import AuthBase, HTTPBasicAuth
from requests_oauthlib import OAuth2Session

import importlib  
spellbook = importlib.import_module("spellbook-py")

credentials = {
"client_id": os.environ["TWITTER_CLIENT_ID"],
"client_secret": os.environ["TWITTER_CLIENT_SECRET"],
"redirect_uri": os.environ["TWITTER_REDIRECT_URI"]
}

print(credentials)