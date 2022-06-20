import logging
import datetime
import os
import socket

if 'PYTHON_ENV' not in os.environ:
    python_env = 'local'
else:
    python_env = os.environ['PYTHON_ENV']

ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
  if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
  s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
  socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

class Logger:
    def setup_logger(self, logger_name, log_file, level=logging.INFO):
        l = logging.getLogger(logger_name)
        if str(level) == '20':
            level_name = 'INFO'
        elif str(level) == '10':
            level_name = 'DEBUG'
        elif str(level) == '40':
            level_name = 'ERROR'
        formatter = logging.Formatter(str(datetime.datetime.now()) + ' ' + str(level_name) + ' -> ' + logger_name + ' @ ' + str(python_env) + ' FROM ' + str(ip) + ' %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='w')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        l.setLevel(level)
        l.addHandler(fileHandler)
        l.addHandler(streamHandler)



