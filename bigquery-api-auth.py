import os
from google.cloud import bigquery

key_path = "json-auth-path/account-id.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

'''
Client() auth only runs if GOOGLE_APPLICATION_CREDENTIALS was set.

You can also set the client service account like this:
client = storage.Client.from_service_account_json(
        'service_account.json')
        
or via pydata_google_auth(very good for notebook/one off usecases):

import pydata_google_auth

credentials = pydata_google_auth.get_user_credentials(
  ['https://www.googleapis.com/auth/bigquery'],
)
client = bigquery.Client(project = project_id, credentials = credentials)
'''

client = bigquery.Client()

query_job = client.query("SELECT * FROM `my-project-id.dataset_name.table_name` LIMIT 5")

results = query_job.result()

for row in results:
    print(row)
    
'''    
job_config = bigquery.LoadJobConfig(
    autodetect=True
)
job_config.write_disposition = "WRITE_TRUNCATE"
job = client.load_table_from_dataframe(
   in_df, table_id, job_config=job_config
)
job.result()
'''
