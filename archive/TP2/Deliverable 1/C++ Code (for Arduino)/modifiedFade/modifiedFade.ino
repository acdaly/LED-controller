/*
 Fade
 (original) example code is in the public domain.

 modified version works for multi colored LEDs, using a for loop
 to do each
 */

int ledr = 5;           // the PWM pin the LED is attached to
int ledg = 3; 
int ledb = 6; 
int ledw = 9; 
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

// the setup routine runs once when you press reset:
void setup() {
  // declare pin 9 to be an output:
  pinMode(ledr, OUTPUT);
  pinMode(ledg, OUTPUT);
  pinMode(ledb, OUTPUT);
  pinMode(ledw, OUTPUT);
    
}

// the loop routine runs over and over again forever:
void loop() {
  oneFade(ledg);
  oneFade(ledr);
  oneFade(ledb);
  oneFade(ledw);

}

void oneFade(int lenPin) {
  for (int k=0;k<255; k++) {
      analogWrite(lenPin, k);
      delay(5);
  }
  analogWrite(lenPin, 0);

}


