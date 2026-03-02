import serial
import time

# --- Configuration ---
PORT = 'COM7'      
BAUD = 9600
THRESHOLD = 250
DELAY = 1          # Seconds between readings

# --- Precaution messages ---
def give_precaution(value):
    if value <= THRESHOLD:
        print("✅ Air Quality Good — No action needed.")
    elif value <= 400:
        print("⚠️ Moderate Pollution — Consider wearing a mask outdoors.")
    elif value <= 600:
        print("🚨 Poor Air Quality — Caution advised, ventilate the room.")
    else:
        print("☠️ Very High Pollution — Avoid going outside!")
    print("-" * 50)

# --- Main program ---
try:
    print("Connecting to Arduino...")
    arduino = serial.Serial(PORT, BAUD, timeout=2)
    time.sleep(2)  # wait for Arduino to reset
    print("Connected successfully!\n")

    while True:
        # Read one line from Arduino
        line = arduino.readline().decode('utf-8', errors='ignore').strip()

        # For debugging: show all lines from Arduino
        if line:
            print(f"Raw data: {line}")

        # Process only valid air quality data
        if line.startswith("Air Quality:"):
            try:
                # Extract number after colon
                value_str = line.split(":")[1].strip()
                value = int(value_str)
                print(f"\n📊 Air Quality Value = {value}")

                # Show warnings and precautions
                if value > THRESHOLD:
                    print("⚠️ Warning: Air Quality is above safe limit!")

                give_precaution(value)
                time.sleep(DELAY)

            except ValueError:
                print("❌ Could not parse number:", line)

except serial.SerialException:
    print("❌ Could not connect to Arduino. Check your COM port and cable.")
except KeyboardInterrupt:
    print("\n🛑 Program stopped by user.")
finally:
    try:
        arduino.close()
        print("Serial connection closed.")
    except:
        pass
