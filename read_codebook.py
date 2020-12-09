import socket
import json
import datetime
import traceback
import sys

if len(sys.argv) < 5:
    sector_idx = 0
else:
    sector_idx = int(sys.argv[4])
if len(sys.argv) < 4:
    sector_type = 1
else:
    sector_type = int(sys.argv[3])
if len(sys.argv) < 3:
    rf_modules_idx = 1
else:
    rf_modules_idx = int(sys.argv[2])
if len(sys.argv) < 2:
    sparrow_address = '192.168.137.1'
else:
    sparrow_address = '192.168.137.' + str(sys.argv[1])



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connect the socket to the port where the server is listening
    #server_address = ('localhost',8000)
    server_address = (sparrow_address, 8000)
    print 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    buf_len = 10240
    
    # Send data
    data = {}
    # data['cmd'] = 'tx_sin'
    # data['args'] = {}
    
    data['cmd'] = 'get_pattern'
    data['args'] = {'sector_idx':sector_idx,'sector_type':sector_type, 'rf_modules_idx':rf_modules_idx}
    
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
            print(response)
#            ret = str(bin(response['rf_current_status'.encode()]))[-18:]
#            gain = ret[-12:-8]
#            sector = ret[-7:]
#            if ret[-18] == '1' and ret[-17] == '0':
#                print 'tx mode, gain index {}, sector {}'.format(int(gain, 2), int(sector, 2))
#            if ret[-18] == 'b' and ret[-17] == '1':
#                print 'rx mode, gain index {}, sector {}'.format(int(gain, 2), int(sector, 2))
            
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




