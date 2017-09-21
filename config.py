"""
Global configurations

Author: Daheng Wang
Last modified: 2017-09-20
"""
import os

"""
Twitter credential information
"""
'''
SET 1
    Owner: adamwang0705
    Owner ID: 3341673561
    Twitter App: tcollector0705
    Twitter App Link: https://apps.twitter.com/app/13194850/show
'''
CONSUMER_TOKEN = "AiDQuuiS4WVOiaDjbN8ybJ7jT"
CONSUMER_SECRET = "t3gHGOnCuDI2Wm3EXUryUXu9B3on7BwIxuxr6ludLY4OE6qgxI"
ACCESS_TOKEN = "3341673561-WCrIFoIPELG9XihGMW2zKOxzaNk3WD9oLx9KQZV"
ACCESS_SECRET = "SyAgzw7GCLyFUapp8nZNA3u79kKfObkH9wgtVWKVoyhHc"

'''
SET 2
    Owner: adamwang0705
    Owner ID: 3341673561
    Twitter App: tcollector0705-2
    Twitter App Link: https://apps.twitter.com/app/13360904/show
'''
# CONSUMER_TOKEN = "3aqIbSNh1uGfPNkLPgumy9rCA"
# CONSUMER_SECRET = "9x9uwtHaz8Nw8kg4zezGn46A3fim4wdYgG0jr2h4GEkBzB5Ixv"
# ACCESS_TOKEN = "3341673561-ZuTFSNJOtWxLWXGEXuRlOhJ5TLrJhOLg6WiyE8w"
# ACCESS_SECRET = "XulcCVhpCwPSL1JVdaoHAftnnyQdz4UAizAQAsfGWRjbV"

"""
Request parameters
"""
'''
REF: https://dev.twitter.com/streaming/overview/request-parameters#track
'''
TRACK = ['snopes']

"""
Dirs
"""
DATA_DIR = os.path.join('.', 'data')

"""
Files
"""
OUTPUT_FILE = 'tweets.json'
