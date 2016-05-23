float tempC;
int reading;
int tempPin = 0;

void setup() {
  analogReference(INTERNAL1V1);
  Serial.begin(9600);
}

void loop() {
  reading = analogRead(tempPin);
  tempC = reading / 9.31;
  Serial.println(tempC);
  delay(100);
}
