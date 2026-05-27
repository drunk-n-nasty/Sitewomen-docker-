from multiprocessing import  cpu_count
from dotenv import load_dotenv
import os 
load_dotenv()

def max_workers():
    return cpu_count()

bind = '0.0.0.0:' + os.getenv('PORT', '8000')
max_requsets = 1000 
worker_class = 'gevent'
workers = max_workers()

env = {
    'DJANGO_SETTINGS_MODULE' : 'sitewomen.settings'
}
reload = True 
name = 'sitewomen'