package rpi;

public class Plant {

	String name;
	double currentMoisture;
	double moistureRangeLo;
	double moistureRangeHi;
	static final double MOISTURE_MIN = 0;
	static final double MOISTURE_MAX = 100;
	
	//default plant constructor
	public Plant() {
		this.name = "default plant";
		this.currentMoisture = 0;
		this.moistureRangeLo = 0;
		this.moistureRangeHi = 100;
	}
	
	//plant constructor with info from database
	public Plant(String name,double moistureRangeLo,double moistureRangeHi) {
		this.name = name;
		this.moistureRangeLo = moistureRangeLo;
		this.moistureRangeHi = moistureRangeHi;
	}
	
	//store moisture level every time server pings
	
	//calculate average moisture level

	public double getCurrentMoisture() {
		return currentMoisture;
	}

	public void setCurrentMoisture(double currentMoisture) {
		this.currentMoisture = currentMoisture;
	}
	
}
