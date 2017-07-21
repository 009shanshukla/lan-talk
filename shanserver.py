import socket,select,sys #import all important module

def broadcast_msg(sock,msg): #broadcast msg to all sockets which are in read mode 
	for socket in list:      #check socket in connection list which socket is in read mode 
		if socket!=server_socket and socket!=sock :   #do not broadcast msg to the server socket and socket which sends the msg
			try:
				socket.send(msg)   #try to send the msg
			except:                #if can't send to that perticular socket that means socket goes offline
				socket.close()     #close that socket
				list.remove(socket)   #remove that socket from connection list

				
if __name__ == "__main__":         #this will show program is running independently not in import mode
	list=[]                        #this set will have all sockets which are connected
	port=5000 
	host='127.0.0.1'

	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #it creates a socket for server and 1st parameter shows IPv4 and 2nd shows TCP connection 
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	server_socket.bind((host,port))   #server socket is connected to its ip and port

	server_socket.listen(10)        #server is in listening mode that means waiting for connection and upcoming connection will not exceed more than 10 otherwise that socket will be rejected

	list.append(server_socket)      #server socket is added to connection list 

	print "chat server started on port "+str(port)

	while 1:                   #infinite loop for upcoming connection 
		read,write,error=select.select(list,[],[])      #this function will divide socket in read,write and error mode

		for sock in read:        #check socket which are in read mode
			if sock==server_socket:   #if that socket is  server socket
				newconn,addr=server_socket.accept()       #accept the message from that socket
				list.append(newconn)             #add that socket in connection list
				print "client "+str(addr[0])+" connected"   #print in server that client is connected to it

				broadcast_msg(newconn,"client "+str(addr[0])+" entered in the group\n")  #broadcast above msg to all connected socket
			else:     #if that socket is not server socket
				try:
					data=sock.recv(4096)   #try to recieve msg from that socket
					if data:             #if that socket sends some msg to server
						broadcast_msg(sock,data) #broadcast its msg to other socket
				except:      #if data is not recieved or broken
					broadcast_msg(sock,"client "+str(addr[0])+"is offline")  #that means client goes offline in between
					print "client "+str(addr[0])+"is offline"  #print that msg in server
					sock.close()   #close that socket
					list.remove(sock)  #remove that socket from connection list
					continue 
	server_socket.close()			#close the server 	
						

            		

            			



