#!/usr/bin/env python
from time import sleep
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import stomp
import json
import uuid

#connect to bigquery
#  Grab the application's default credentials from the environment.
credentials = GoogleCredentials.get_application_default()

# Construct the service object for interacting with the BigQuery API.
bigquery = discovery.build('bigquery', 'v2', credentials=credentials)

#network rail API credentials
NETWORK_RAIL_AUTH = ('Alexfrancisross@hotmail.com', 'P@ssw0rd')

#function to stream a new row of data to bigquery
def stream_row_to_bigquery(bigquery, project_id, dataset_id, table_name, row,
                           num_retries=5):
    insert_all_data = {
        'rows': [{
            'json': row,
            # Generate a unique id for each row so retries don't accidentally
            # duplicate insert
            'insertId': str(uuid.uuid4()),
        }]
    }
    return bigquery.tabledata().insertAll(
        projectId=project_id,
        datasetId=dataset_id,
        tableId=table_name,
        body=insert_all_data).execute(num_retries=num_retries)

#streams data from network rail API and writes to big query
class Listener(object):

    def __init__(self, mq):
        self._mq = mq

    def on_message(self, headers, message):
        message_array = json.loads(message)

        for s in message_array:
            if s['header']['msg_type'] == '0003': #if message type is 0003 (Train Movement)
                row = s['body']
                num_retries = 5
                project_id ='ancient-episode-126117'
                print row

                #format datetime fields
                if row['planned_timestamp'] == '':
                    row['planned_timestamp'] = 0
                else:
                    row['planned_timestamp'] = float(row['planned_timestamp']) / 1000

                if row['actual_timestamp'] == '':
                    row['actual_timestamp'] = 0
                else:
                    row['actual_timestamp'] = float(row['actual_timestamp']) / 1000

                if row['gbtt_timestamp'] == '':
                    row['gbtt_timestamp'] = 0
                else:
                    row['gbtt_timestamp'] = float(row['gbtt_timestamp']) / 1000

                if row['original_loc_timestamp'] == '':
                    row['original_loc_timestamp'] = 0
                else:
                    row['original_loc_timestamp'] = float(row['original_loc_timestamp']) / 1000

                #insert data into database
                response = stream_row_to_bigquery(
                    bigquery, project_id, 'tableau', 'networkraillive', row, num_retries)
                print(json.dumps(response))

        self._mq.ack(id=headers['message-id'], subscription=headers['subscription'])

#loop to keep streaming data
while True:
    try:
        mq = stomp.Connection(host_and_ports=[('datafeeds.networkrail.co.uk', 61618)],
                              keepalive=True,
                              vhost='datafeeds.networkrail.co.uk',
                              heartbeats=(100000, 50000))

        mq.set_listener('', Listener(mq))

        mq.start()
        mq.connect(username=NETWORK_RAIL_AUTH[0],
                   passcode=NETWORK_RAIL_AUTH[1],
                   wait=True)

        mq.subscribe('/topic/TRAIN_MVT_ALL_TOC', 'test-vstp', ack='client-individual')

        while mq.is_connected():
            sleep(1)

    except:
        # Oh well, reconnect and keep going
        continue


