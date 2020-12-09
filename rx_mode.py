import socket
import sys
import json
import datetime
import traceback

if len(sys.argv) < 4:
    sector_id = 2
else:
    sector_id = int(sys.argv[3])
if len(sys.argv) < 3:
    bb_gain = 9
else:
    bb_gain = int(sys.argv[2])
if len(sys.argv) < 2:
    rf_gain = 10
else:
    rf_gain = int(sys.argv[1])

print rf_gain, bb_gain, sector_id

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connect the socket to the port where the server is listening
    #server_address = ('localhost', 8000)
    server_address = ('192.168.137.2', 8000)
    print 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    buf_len = 10240
    
    # Send data
    data = {}
    data['cmd'] = 'rx_mode'
    data['args'] = {'rf_gain_index':bb_gain, 'rx_bb_gain_row_num':rf_gain, 'rf_sector_id':sector_id}
    
    message = json.dumps(data).encode('utf-8')
    print data
    
    a = datetime.datetime.now()
    while True:
    # for i in range(0, 64):
        sock.sendall(message)
        
        # Look for the response
        d = b''
        while True:
            d_tmp = sock.recv(buf_len)
            d += d_tmp
            if not d_tmp or d_tmp[-1] == '}' or d_tmp[-1] == ')' or d_tmp[-1] == ']':
                break
            
        if d:
            response = json.loads(d.decode('utf-8'))
            print response
            
        break
        # time.sleep(1)
        # time.sleep(20)
    
    b = datetime.datetime.now()
    delta = b - a
    print delta

except Exception as e:
    traceback.print_exc()
    print e
    print 'exiting'
finally:
    print 'connection close'
    sock.close()




