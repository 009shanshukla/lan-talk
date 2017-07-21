#some comments are same as server program comments
import sys,socket,select
print "enter your name :"
name=raw_input()  
def writeinterminal(a):  
	if a=='fromuser':
		sys.stdout.write(name +': ')  #print the writtem msg on terminal initiated with your name
	else:
		sys.stdout.write(':->')  #print the writtem msg on terminal initiated with client name
		
	sys.stdout.flush()  #flush the buffer

if __name__=="__main__":  
	host='127.0.0.1'
	port=5000

	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.settimeout(2)  #wait for 2 unit time

	try:    
		client_socket.connect((host,port))  #try to connect client to server
		print "connected to server\n"
	except:
		print "unable to connect\n"   #in case of failure
		sys.exit()	

	client_socket.send('this is '+name+'\n')	



	writeinterminal('fromclient')   #function call

	while 1:    #infine loop to exit press ctrl +c
		socket_list=[sys.stdin,client_socket]   #this list will contain client in read or write mode

		read,write,error=select.select(socket_list,[],[])    #we call the select function passing it the list. The select function returns a list of arrays that are readable, writable or had an error

		for sock in read:    #search if socket is in readable mode
			if sock == client_socket:      # incoming message from remote server
				data=sock.recv(4096)      #recieve that msg from server
				if not data:              #if data is not found that means connection is broken
					print "disconnected from server\n"
					sys.exit()
				else:
					sys.stdout.write(data)    #print that msg coming from server
					writeinterminal('fromuser')         
			else:
				msg=sys.stdin.readline()   #user entered any msg
				client_socket.send(name+":->"+msg)    #send that msg to server
				writeinterminal('fromclient')
					
					

		


    



