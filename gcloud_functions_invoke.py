import os

import google.auth.transport.requests
import google.oauth2.id_token

'''
Environment variable setup that holds the principal json credential
https://cloud.google.com/functions/docs/securing/authenticating#authenticating_function_to_function_calls
'''

key_path = "json-auth-path/account-id.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

service_url = "https://gcp-region-projectid.cloudfunctions.net/my_function_to_run"
req = urllib.request.Request(service_url)

auth_req = google.auth.transport.requests.Request()
id_token = google.oauth2.id_token.fetch_id_token(auth_req, service_url)

req.add_header("Authorization", f"Bearer {id_token}")
response = urllib.request.urlopen(req)

print(response.read())
