package rpi;

import java.net.*;
import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

public class UDPSender {

	public static void main(String[] args) throws UnknownHostException {
		// setting a timer to periodically ping the moisture sensor
		
		InetAddress host = InetAddress.getByName(args[0]) ;
		int port = Integer.parseInt(args[1]) ;
		
		TimerTask task = new PeriodicPing(host,port);
		
		//main runs the ping to the client every 2 minutes, 120000 milliseconds
		Timer timer = new Timer();
		timer.schedule(task, 1000, 120000);
		
	}
}

