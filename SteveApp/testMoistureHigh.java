package com.example.steve.plantpals;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import static com.example.steve.plantpals.R.id.textView;

public class testMoistureHigh extends AppCompatActivity {

    private receiveData receive;
    private sendData send;
    private TextView highTest;
    private Plant currentPlant;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_test_moisture_high);

        receive = new receiveData();
        send = new sendData();
        highTest = (TextView) findViewById(R.id.textHighTest);
        currentPlant = (Plant) LocalStorage.plantList.get(0);

        if(receive.getMoistureActual() > currentPlant.getMoisture()) {
            send.sendMoisture(currentPlant.getMoisture());
            send.sendBool(false);
            highTest.setText("System must not increase water output.");
        }
        else {
            send.sendMoisture(currentPlant.getMoisture());
            send.sendBool(false);
            highTest.setText("Moisture is not too high.");
        }

    }
}