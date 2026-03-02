#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

const int buz = 8;
const int led = 9;
const int aqsensor = A0;
int threshold = 250;
unsigned long last = 0;
unsigned long interval = 1000;

void setup() {
  pinMode(buz, OUTPUT);
  pinMode(led, OUTPUT);
  pinMode(aqsensor, INPUT);
  
  Serial.begin(9600);
  
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Air Quality Init");
  delay(1000);
  lcd.clear();
  
  Serial.println("BOOT");
}

void loop() {
  if (millis() - last >= interval) {
    last = millis();
    int ppm = analogRead(aqsensor);

    lcd.setCursor(0,0);
    lcd.print("Air Quality:");
    lcd.setCursor(13,0);
    lcd.print(ppm);
    
    if(ppm > threshold){
      lcd.setCursor(0,1);
      lcd.print("AQ Level HIGH ");
      tone(buz,1000,300);
      digitalWrite(led,HIGH);
      Serial.println("AQ Level HIGH");
    } else {
      lcd.setCursor(0,1);
      lcd.print("AQ Level GOOD ");
      noTone(buz);
      digitalWrite(led,LOW);
      Serial.println("AQ Level GOOD");
    }

    Serial.print("Air Quality: ");
    Serial.println(ppm);
  }
}
