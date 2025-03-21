# Python Program To Use IBM Watson
# Studio's Speech To Text Below Code
# Accepts only .mp3 Format of Audio
# File


import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Insert API Key in place of
# 'YOUR UNIQUE API KEY'
authenticator = IAMAuthenticator('YOUR UNIQUE API KEY')
service = SpeechToTextV1(authenticator=authenticator)

# Insert URL in place of 'API_URL'
service.set_service_url('API_URL')

# Insert local mp3 file path in
# place of 'LOCAL FILE PATH'
with open(join(dirname('__file__'), r'LOCAL FILE PATH'),
          'rb') as audio_file:
    dic = json.loads(
        json.dumps(
            service.recognize(
                audio=audio_file,
                content_type='audio/flac',
                model='en-US_NarrowbandModel',
                continuous=True).get_result(), indent=2))

# Stores the transcribed text
str = ""

while bool(dic.get('results')):
    str = dic.get('results').pop().get('alternatives').pop().get('transcript') + str[:]

print(str)
