String serial_buffer;
const int red = 3;
const int green = 5;
const int blue = 6;
const int white = 9;
int brightness = 0;
void setup() {
  Serial.begin(230400);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(white, OUTPUT); 
}
void loop() {
  if (Serial.available() > 0) {
    serial_buffer = Serial.readStringUntil(' ');
    brightness = Serial.parseInt();
    if (serial_buffer.equals("r"))
         analogWrite(red, brightness);
    if (serial_buffer.equals("g"))
         analogWrite(green, brightness);
    if (serial_buffer.equals("b"))
         analogWrite(blue, brightness);
    if (serial_buffer.equals("w"))
         analogWrite(white, brightness);
    delay(10);
  }
}
