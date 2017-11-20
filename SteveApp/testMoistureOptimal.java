package com.example.steve.plantpals;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import static com.example.steve.plantpals.R.id.textView;

public class testMoistureOptimal extends AppCompatActivity {

    private receiveData receive;
    private sendData send;
    private TextView optimalTest;
    private Plant currentPlant;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_test_moisture_optimal);

        receive = new receiveData();
        send = new sendData();
        optimalTest = (TextView) findViewById(R.id.textOptimalTest);
        currentPlant = (Plant) LocalStorage.plantList.get(0);

        if(receive.getMoistureActual() == currentPlant.getMoisture()) {
            send.sendMoisture(currentPlant.getMoisture());
            send.sendBool(false);
            optimalTest.setText("Moisture level is optimal: telling server to not water");
        }
        else {
            send.sendMoisture(currentPlant.getMoisture());
            send.sendBool(false);
            optimalTest.setText("Moisture is not optimal.");
        }

    }
}