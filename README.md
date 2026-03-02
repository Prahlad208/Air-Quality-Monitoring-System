# Air Quality Monitoring System

## Project Overview

The Air Quality Monitoring System is an Arduino-based project designed to measure and display air pollution levels using a gas sensor.

The system continuously monitors air quality and alerts the user when pollution levels exceed a predefined threshold using a buzzer and LED indicator.

---

## Components Used

- Arduino Uno
- MQ Gas Sensor (Air Quality Sensor)
- 16x2 LCD Display (I2C Module)
- Buzzer
- LED
- Breadboard
- Jumper Wires
- 5V Power Supply

---

## System Working

1. The MQ gas sensor detects the concentration of gases in the air.
2. The sensor outputs an analog voltage based on gas concentration.
3. Arduino reads this analog value through pin A0.
4. The air quality value is displayed on the LCD screen.
5. If the value exceeds the threshold:
   - Buzzer turns ON
   - LED turns ON
   - "AQ Level HIGH" message is displayed
6. If the value is below threshold:
   - System displays "AQ Level GOOD"
   - Buzzer and LED remain OFF

---

## Threshold Logic

The system uses a predefined threshold value to determine air quality status.

Example:

Threshold = 250

If sensor value > 250 → Air Quality HIGH  
If sensor value ≤ 250 → Air Quality GOOD  

This threshold can be adjusted based on calibration requirements.

---

## Pin Configuration

| Component   | Arduino Pin |
|-------------|------------|
| Gas Sensor  | A0         |
| Buzzer      | 8          |
| LED         | 9          |
| LCD (I2C)   | SDA, SCL   |
| VCC         | 5V         |
| GND         | GND        |

---

## Output

### LCD Display:

Air Quality: <value>  
AQ Level GOOD / AQ Level HIGH  

### Serial Monitor Output:

Air Quality: <value>  

---

## Working Principle

The MQ gas sensor changes its internal resistance when exposed to different gas concentrations.

The Arduino reads the analog voltage variation (0–1023) and interprets it as air quality level.

Higher value → Higher gas concentration  
Lower value → Cleaner air  

---

## Applications

- Indoor air quality monitoring
- Industrial safety systems
- Pollution detection
- Smart home automation systems

---

## Possible Improvements

- Add real-time graph plotting using Python
- Calibrate sensor for accurate PPM measurement
- Store data using SD card module
- Add IoT integration for remote monitoring

---

## Learning Outcomes

- Analog sensor interfacing
- LCD communication using I2C
- Threshold-based alert system
- Serial communication
- Embedded system design
