import time
import board
import adafruit_charlcd as charlcd
import Adafruit_DHT

# Initialize LCD
lcd_columns = 16
lcd_rows = 2
i2c = board.I2C()
lcd = charlcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# Initialize DHT22 sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the DHT22 sensor is connected

try:
    while True:
        # Read temperature and humidity from DHT22 sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        # Clear LCD display
        lcd.clear()

        if humidity is not None and temperature is not None:
            # Display temperature and humidity on LCD
            lcd.message('Temp: {0:0.1f} C\n'.format(temperature))
            lcd.message('Humidity: {0:0.1f}%'.format(humidity))
        else:
            # Display error message if sensor reading fails
            lcd.message('Failed to read\nsensor data.')

        time.sleep(2)  # Delay between readings

except KeyboardInterrupt:
    lcd.clear()
