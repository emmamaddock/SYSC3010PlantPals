#include <Arduino.h>


unsigned long time;
double runTime; // Variable input from main
runTime = runTime*1000;
void setup() {
  Serial.begin(9600);// Set Baud Rate, Bit/Sec

}

void loop() {
  while(time<runTime){ // Run for 10 Seconds
       int humidityRaw0 = analogRead(A0); // 1023 to 0 ===> 0 to 100%
       int humidityRaw1 = analogRead(A1);
       int humidityRaw2 = analogRead(A2);


       int humidityReal0 = map(humidityRaw0, 1023, 0, 0, 100); //Re-map 1023 to 0 and 0 to 100
       int humidityReal1 = map(humidityRaw1, 1023, 0, 0, 100);
       int humidityReal2 = map(humidityRaw2, 1023, 0, 0, 100);

       Serial.print("Time: ");
       time = millis();
       Serial.println(time/1000);
       Serial.print("------------------");
       Serial.println();

	  // use json for sending data ##
      Serial.print("Plant 1: ");
      Serial.println(humidityReal0); // Print live results
      Serial.print("Plant 2: ");
      Serial.println(humidityReal1);
      Serial.print("Plant 3: ");
      Serial.println(humidityReal2);
      Serial.println();
      delay(2000); // Delay between readings (2 second)
  }

}
