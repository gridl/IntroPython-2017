
import zmq
import logging
import optparse
import os

parser = optparse.OptionParser()
parser.add_option("-s", "--server", dest="server", help="URI of the server")
parser.add_option("-d", "--debug", dest="debug", action="store_true", help="Print debug information to the screen")

(options, args) = parser.parse_args()

#print("ARGS",args)
if not args:
    message="echo_test"
else:
    message=args[0]

if options.server is None:
    options.server = "tcp://127.0.0.1:5561"

if options.debug is None:
    options.stream_log_level = logging.INFO
else:
    options.stream_log_level = logging.DEBUG

# look up process name, pid
scriptname = os.path.basename(__file__).split(".py")[0]
pid = os.getpid()

# define where to write the logs
log_path = 'log/{}.log'.format(scriptname)

# define a stream and file handler
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(options.stream_log_level)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(filename = log_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.addHandler(stream_handler)

# Prepare our context and sockets
context = zmq.Context()

#log.debug("connecting to {}".format(options.server))

me = context.socket(zmq.REQ)
me.connect(options.server)

# Process messages from both sockets
#message = "hello world"
me.send_string(message)
log.info("{} sent {} to {}".format(pid, message, options.server))
in_message = me.recv_string()
log.debug("{} received: ".format(pid) + str(in_message))
