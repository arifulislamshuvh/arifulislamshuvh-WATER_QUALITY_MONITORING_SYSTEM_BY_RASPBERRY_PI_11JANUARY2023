// Arduino code to read pH sensor and send data to Raspberry Pi via serial

// Define the pin for pH sensor
const int phSensorPin = A0;
// Define the pin for output to Raspberry Pi
const int outputPin = 6;

void setup() {
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  // Read the analog value from pH sensor
  int sensorValue = analogRead(phSensorPin);
  
  // Convert analog value to pH value (you need to calibrate this based on your sensor)
  float pHValue = analogToPH(sensorValue);

  // Print pH value to serial
  Serial.print("pH: ");
  Serial.println(pHValue);

  // Output pH value to Raspberry Pi via digital pin
  digitalWrite(outputPin, pHValue); // You might need to scale the pH value to fit within the acceptable range for a digital output
  delay(1000); // Adjust delay as needed
}

// Function to convert analog value to pH value (you need to calibrate this based on your sensor)
float analogToPH(int value) {
  // Example conversion function, you need to replace this with your actual conversion logic
  // This is just a placeholder
  return map(value, 0, 1023, 0, 14); // Assumes pH range from 0 to 14
}
