import os
import argparse
import multiprocessing as mp
from tqdm import tqdm
from utils import check_availability, unpickle_wordlist

dir_path = os.path.dirname(os.path.realpath(__file__))

default_pickle_path = os.path.join(dir_path,
                                   os.pardir,
                                   'data',
                                   'preprocessed', 
                                   'word_list_1.pickle')

avaliable_names_path = os.path.join(dir_path,
                                    os.pardir,
                                    'data',
                                    'available_usernames.csv')

def worker(word, queue):
    '''
    Receives a word and checks the availability
    of that word as a username
    '''
    if check_availability(word):
        result = (word, True)
    else:
        result = (word, False)
    queue.put(result)
    return result

def writer(queue):
    with open(avaliable_names_path, "r") as fd:
        while True:
            message = queue.get()
            if message == 'kill':
                tqdm.write('Writer process killed')
                break
            else:
                word, result = message
                fd.write('{},{}\n'.format(word, result))
                fd.flush()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check availability of usernames')
    parser.add_argument('--picklefile', dest='picklefile')
    args = parser.parse_args()

    pickle_path = args.picklefile
    if pickle_path is None:
        pickle_path = default_pickle_path

    # Unpickle our preprocessed list of words
    word_list = unpickle_wordlist(pickle_path)
    num_process = 4
    print('Running {} processes'.format(num_process))

    manager = mp.Manager()
    queue = manager.Queue()
    pool = mp.Pool(num_process)
    file_writer = pool.apply_async(writer, (queue,))

    jobs = []
    for word in word_list:
        job = pool.apply_async(worker, (word, queue))
        jobs.append(job)

    for job in tqdm(jobs, smoothing=0.1):
        job.get()

    queue.put('kill')
    pool.close()
    pool.join