// Libraries
#include <Wire.h>

// Define the analog pins
#define PH_SENSOR_PIN A0
#define TDS_SENSOR_PIN A1

// Define the digital pins
#define PH_OUTPUT_PIN 6
#define TDS_OUTPUT_PIN 5

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  // Initialize I2C communication
  Wire.begin();
}

void loop() {
  // Read pH sensor value
  int phValue = analogRead(PH_SENSOR_PIN);
  // Read TDS sensor value
  int tdsValue = analogRead(TDS_SENSOR_PIN);
  
  // Send pH value to Raspberry Pi
  Wire.beginTransmission(8); // Address of Raspberry Pi
  Wire.write(PH_OUTPUT_PIN);
  Wire.write((uint8_t*)&phValue, sizeof(phValue));
  Wire.endTransmission();

  // Send TDS value to Raspberry Pi
  Wire.beginTransmission(8); // Address of Raspberry Pi
  Wire.write(TDS_OUTPUT_PIN);
  Wire.write((uint8_t*)&tdsValue, sizeof(tdsValue));
  Wire.endTransmission();

  // Delay for stability
  delay(1000);
}
