package rpi;

import java.io.*;
import java.net.*;

public class Server {
	
	public void main(String[] args) throws Exception {
        
		DatagramSocket serverSocket = new DatagramSocket(666);
		byte[] receiveData = new byte[1024];
		byte[] sendData = new byte[1024];
		
		while(true) {
			
			DatagramPacket receivePacket = new DatagramPacket(receiveData,receiveData.length);
			serverSocket.receive(receivePacket);
			
			//reading the received data from the client
			String moistureData = new String(receivePacket.getData());
			System.out.println("RECEIVED: " + moistureData);
			
			InetAddress IPAddress = receivePacket.getAddress();
			int port = receivePacket.getPort();
			
			//modifying the received data and sending it back
			String received = moistureData + " modified";
			sendData = received.getBytes();
			
			DatagramPacket sendPacket = new DatagramPacket(sendData,sendData.length,IPAddress,port);
			serverSocket.send(sendPacket);
			
		}
		
	}
	
	public Boolean isMoist() {
		
		return true;
	}
		
	
}
