# SYSC3010PlantPals
SYSC 3010 Plant Pals project repository

Plant Pals - Plant Monitoring and Watering made easy
	SYSC 3010
	Group M6

Caleb Gryfe            [101009798]

Tareq Muhammad         [----------]

Emma Maddock           [----------]

Steven Nash            [----------]

12/07/2017

------------------------------------------------------------------------------------------------------------------------------
To operate this system in a similar fashion as we have done, you will require 2 Raspberry pi's and an Arduino
Additional Hardware used:
moisture sensors and accompanying Detector Modules
DC Stepper motor & motor shield
DC water pump
(An additional rig was used to hold plants and move the pump nozzle)

How to Set-up Headless pi
--------------------------
1.  Plug Arduino into raspberry pi using USB A/B serial cable
2.  Open Terminal and run the following commands:
      $ sudo apt-get update
      $ sudo apt-get install arduino
3.  Once these have finished
4.  Download Rpi_headless
5.  Unzip contents to Desktop
6.  Navigate to the Libraries Folder of the Arduino IDE and the ArduinoJson file in Rpi_headless, use the "Extract to"
    function to move ArduinoJson into the library folder
7.  Navigate to Rpi_headless -> plantMoisture.ino and open using the Arduino IDE
8.  At the top left of the Arduino ide click the forward arrow "Upload"
9.  Open terminal and run the following commands:
      cd \home\pi\Desktop\Rpi_headless
      python main.py
  