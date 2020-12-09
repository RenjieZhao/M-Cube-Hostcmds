sshpass -p '123456' ssh root@192.168.137.$1 ifconfig wlan0 up 
sshpass -p '123456' ssh root@192.168.137.$1 ifconfig 
sshpass -p '123456' scp wil6210_server root@192.168.137.$1:/tmp
#sshpass -p '123456' ssh root@192.168.137.$1 python /tmp/wil6210_server 8000
