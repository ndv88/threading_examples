import requests

# from multiprocessing.dummy import Pool

from multiprocessing.pool import Pool

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  ]


def do_request(url):
    print("start request to - {0}".format(url))
    response = requests.get(url)
    print("end request to - {0}".format(url))

# make the Pool of workers
pool = Pool(4)

# open the urls in their own threads
# and return the results
results = pool.map(do_request, urls)

# close the pool and wait for the work to finish
pool.close()
pool.join()

