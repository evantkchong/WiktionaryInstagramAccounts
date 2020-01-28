import pickle
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Website to query
url = 'https://www.instagram.com/'

# We create a retry object with a large backoff factor to try and
# get around Instagram's request limits
retries = Retry(total = 9,
                backoff_factor = 30,
                status_forcelist = [104, 500, 502, 503, 504])

def check_availability(username:str):
    '''
    Makes a request to instagram's website.
    If a 200 response is returned, the username is taken.
    Otherwise, if a 404 reponse is returned, the username is available.
    '''
    # We make a get request to
    # https://www.instagram.com/{username}/?__a=1
    webpage = 'https://www.instagram.com/{}/?__a=1'.format(username)

    sess = requests.Session()
    sess.mount(url, HTTPAdapter(max_retries=retries))
    response = sess.get(webpage)
    status = response.status_code

    # We then use the returned status code to determine
    # if the username is still availble for use
    if status == 404:
        return True
    elif status in [200, 302]:
        return False

def unpickle_wordlist(path):
    with open(path, 'rb') as fd:
        wordlist = pickle.load(fd)
    return wordlist

def split_list(word_list, num_splits):

    def slicer(index, num_splits):
        start = (index*len(word_list))//num_splits
        stop = ((index+1)*len(word_list))//num_splits
        return slice(start, stop)

    new_list = [word_list[slicer(i, num_splits)] for i in range(num_splits)]
    return new_list