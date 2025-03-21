# importing libraries
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies
# the name of a file that contains
# client_id and client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This scope allows for full read/write
# access to the authenticated user's account
# and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com / auth / youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def print_response(response):
    print(response)


# Build a resource based on a list of
# properties given as key-value pairs.
# Leave properties with empty values out
# of the inserted resource.
def build_resource(properties):
    resource = {}


    for p in properties:

        # Given a key like "snippet.title", split
        # into "snippet" and "title", where
        # "snippet" will be an object and "title"
        # will be a property in that object.
        prop_array = p.split('.')


        ref = resource

        for pa in range(0, len(prop_array)):
            is_array = False
            key = prop_array[pa]

            # For properties that have array values, convert a
            # name like "snippet.tags[]" to snippet.tags, and set
            # a flag to handle the value as an array.
            if key[-2:] == '[]':
                key = key[0:len(key) - 2:]
                is_array = True

            if pa == (len(prop_array) - 1):

                # Leave properties without values
                # out of inserted resource.
                if properties[p]:

                    if is_array:
                        ref[key] = properties[p].split(', ')

                    else:
                        ref[key] = properties[p]

            elif key not in ref:
                ref[key] = {}
                ref = ref[key]

            else:
                ref = ref[key]
    return resource


# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}


    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value

    return good_kwargs


def search_list_forMine(client, **kwargs):
    kwargs = remove_empty_kwargs(**kwargs)
    response = client.search().list(**kwargs).execute()
    return print_response(response)

if __name__ == '__main__':
    # When running locally, disable OAuthlib's
    # HTTPs verification. When running in production
    # * do not * leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = get_authenticated_service()


    search_list_forMine(client,
                    part='snippet',
                    maxResults=5,
                    forMine=True,
                    q='Geeksforgeeks',
                    type='video')
