package rpi;

import java.net.*;
import java.util.*;

public class PeriodicPing extends TimerTask {

	private final static int PACKETSIZE = 100;
	InetAddress host;
	int port;
	
	public PeriodicPing(InetAddress host, int port) {
		this.host = host;
		this.port = port;
	}

	public void run() {

		try {
			
			DatagramSocket socket = new DatagramSocket();


			String message = null;

			//sending a request message to the headless pi
			System.out.println("Requesting moisture level...");
			message = "request";
			byte [] data = message.getBytes() ;
			DatagramPacket packet = new DatagramPacket(data, data.length, this.host, this.port) ;
			socket.send(packet);

			//getting a moisture int back from the headless pi after it receives a request
			DatagramPacket returnPacket = new DatagramPacket(new byte[PACKETSIZE], PACKETSIZE) ;
			socket.receive(returnPacket);

			//TODO: figure out how to get int value from datagram packet
			//TODO: Compare int value to see if it's within plant's ideal range
			System.out.println("Current moisture level is " + new String(returnPacket.getData()) + "%.");
			//}
		}
		
		catch(Exception e) {
			System.out.println(e) ;
		}
	}

}
