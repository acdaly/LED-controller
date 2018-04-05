
String serial_buffer;
const int pin13 = 13;


void setup() {
  Serial.begin(115200);
  pinMode(pin13, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    serial_buffer = Serial.readStringUntil('\n');
    if (serial_buffer.equals("1"))
        digitalWrite(pin13, HIGH);
    }
    else if (serial_buffer.equals("0"))
    {
        digitalWrite(pin13, LOW);
    }
  }
