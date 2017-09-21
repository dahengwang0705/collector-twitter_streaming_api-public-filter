"""
Main collector to get public statuses that match one or more filter predicates
from statuses/filter endpoint of Public streams of Twitter Streaming APIs.

Author: Daheng Wang
Last modified: 2017-09-20
"""
import json
import time

from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterConnectionError
from TwitterAPI import TwitterRequestError

import config as config

if __name__ == '__main__':
    api = TwitterAPI(config.CONSUMER_TOKEN,
                     config.CONSUMER_SECRET,
                     config.ACCESS_TOKEN,
                     config.ACCESS_SECRET)

    while True:
        try:
            iterator = api.request('statuses/filter', {'track': config.TRACK}).get_iterator()
            for item in iterator:
                if 'text' in item:
                    # IMPORTANT: use 'append' mode when opening output file
                    with open(config.OUTPUT_FILE, 'a') as f:
                        f.write(json.dumps(item) + '\n')
                    print(item['id_str'])
                elif 'disconnect' in item:
                    '''
                    Streams may be shut down for a variety of reasons. The streaming API will attempt to 
                    deliver a message indicating why a stream was closed. Note that if the disconnect was 
                    due to network issues or a client reading too slowly, it is possible that this message 
                    will not be received.
                    REF: https://dev.twitter.com/streaming/overview/messages-types#public_stream_messages
                    '''
                    event = item['disconnect']
                    if event['code'] in [2, 5, 6, 7]:
                        '''
                        Client side issues
                        '''
                        raise Exception(event['reason'])
                    else:
                        '''
                        Server side issues. Temporary interruption, re-try request.
                        '''
                        print('Server accidentally closed connection. Sleep 3 seconds and re-connect.')
                        time.sleep(3)
                        break
        except TwitterRequestError as e:
            '''
            The Twitter API attempts to return appropriate HTTP status codes for every request.
            REF: https://dev.twitter.com/overview/api/response-codes
            '''
            if e.status_code < 500:
                '''
                Client side issues
                '''
                raise
            else:
                '''
                Server side issues. Temporary interruption, re-try request.
                '''
                print('Server accidentally closed connection. Sleep 3 seconds and re-connect.')
                time.sleep(3)
                pass
        except TwitterConnectionError:
            '''
            The Twitter API attempts to return appropriate HTTP status codes for every request.
            REF: https://dev.twitter.com/overview/api/response-codes
            '''
            '''
            Server side issues. Temporary interruption, re-try request.
            '''
            print('Server accidentally closed connection. Sleep 3 seconds and re-connect.')
            time.sleep(3)
            pass
