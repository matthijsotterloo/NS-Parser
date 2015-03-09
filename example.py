import zmq, gzip, ns_gps_parser, cStringIO

server_socket = zmq.Context().socket(zmq.SUB)
server_socket.connect('tcp://vid.openov.nl:6701')
server_socket.setsockopt(zmq.SUBSCRIBE, '')
server_socket.setsockopt(zmq.RCVHWM, 0)

while True:
    multipart = server_socket.recv_multipart()
    content = gzip.GzipFile('', 'r', 0 , cStringIO.StringIO(''.join(multipart[1:]))).read()

    for location in ns_gps_parser.parse_xml(content):
        print location
