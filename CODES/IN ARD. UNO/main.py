import smbus
import time

# Define I2C address of Arduino
ARDUINO_ADDRESS = 8

# Define digital pins for Arduino
PH_OUTPUT_PIN = 6
TDS_OUTPUT_PIN = 5

# Define I2C bus
bus = smbus.SMBus(1)

def read_sensor(pin):
    try:
        bus.write_byte(ARDUINO_ADDRESS, pin)
        time.sleep(0.1)  # Delay to allow Arduino to process
        data = bus.read_i2c_block_data(ARDUINO_ADDRESS, 0)
        sensor_value = int.from_bytes(data, byteorder='little')
        return sensor_value
    except Exception as e:
        print("Error reading sensor:", e)
        return None

def main():
    try:
        while True:
            # Read pH value from Arduino
            ph_value = read_sensor(PH_OUTPUT_PIN)
            if ph_value is not None:
                print("pH Value:", ph_value)

            # Read TDS value from Arduino
            tds_value = read_sensor(TDS_OUTPUT_PIN)
            if tds_value is not None:
                print("TDS Value:", tds_value)

            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        bus.close()

if __name__ == "__main__":
    main()
