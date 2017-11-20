package rpiclient;

import java.net.*;
import java.io.*;

public class UDPReceiver {

	private final static int PACKETSIZE = 100 ;
	
	public UDPReceiver() {
		
	}
	
	public static void main(String args[]) { 
		
		UDPReceiver test = new UDPReceiver();
		
		
		// Check the arguments
		if(args.length != 1) {
			System.out.println("usage: UDPReceiver port") ;
			return ;
		}
		
		try {
			// Convert the argument to ensure that is it valid
			int port = Integer.parseInt(args[0]);

			// Construct the socket
			//NOTE: if it doesn't work take socket out of the loop

			//TODO: end the for loop somehow
			for(;;) {
				
				DatagramSocket socket = new DatagramSocket(port);
				
				System.out.println("Waiting for moisture request on port " + port) ;
				DatagramPacket packet = new DatagramPacket(new byte[PACKETSIZE], PACKETSIZE) ;
				socket.receive(packet);
				
				//taking the string data from the datagram packet and cleaning it up
				String checkOne = new String(packet.getData());
				String checkTwo = checkOne.trim();

				//if the client successfully receives a request from the server to check the moisture 
				//it prints this message
				if (checkTwo.equals("request")) {
					System.out.println("Moisture check requested from " + packet.getAddress() + " " + packet.getPort());
					
					try {
						
						InetAddress returnHost = packet.getAddress();
				        int returnPort = packet.getPort() ;
				         socket = new DatagramSocket();
				         
				         //TODO: to be replaced by actual data/file reader
				         //String moistureLevel = "30";
				         String moistureLevel = test.read();
				         
				         
				         byte [] moist = moistureLevel.getBytes();
				         
				         DatagramPacket returnPacket = new DatagramPacket(moist, moist.length, returnHost, returnPort) ;
				         socket.send(returnPacket) ;
				         
				         System.out.println("Current moisture data sent.");
					}
					 catch(Exception e)
				      {
				         System.out.println(e) ;
				      }
					
				}
				else {
					System.out.println("Error during request.");
				}
			}


		}
		
		catch (Exception e) {
			System.out.println(e) ;
		}



	}
	
	//this method reads one moisture level from a text file that the
	//arduino will be populating
	public String read() {
		
		String filename = "moistureData.txt";
		
		String moistureLevel = null;
		
		try {
			FileReader fileReader = new FileReader(filename);
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			
			moistureLevel = bufferedReader.readLine();
		
			bufferedReader.close();
		}
		
		catch (FileNotFoundException e) {
			
		}
		catch (IOException e) {
			
		}
		
		return moistureLevel;
		
	}

}
