package com.example.steve.plantpals;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import static com.example.steve.plantpals.R.id.textView;

public class testMoistureLow extends AppCompatActivity {

    private receiveData receive;
    private sendData send;
    private TextView lowTest;
    private Plant currentPlant;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_test_moisture_low);

        receive = new receiveData();
        send = new sendData();
        lowTest = (TextView) findViewById(R.id.textLowTest);
        currentPlant = (Plant) LocalStorage.plantList.get(0);

        if(receive.getMoistureActual() < currentPlant.getMoisture()) {
            send.sendMoisture(currentPlant.getMoisture());
            send.sendBool(true);
            lowTest.setText("System must increase water output.");
        }
        else {
            send.sendMoisture(currentPlant.getMoisture());
            send.sendBool(false);
            lowTest.setText("Moisture is not too low.");
        }

    }
}
