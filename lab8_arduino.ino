#include


Servo servo1;
Servo servo2;
const int servo1PotPin = A0;
const int servo1Pin = 5; 
const int servo2PotPin = A1;
const int servo2Pin = 3; 

int servo1_test;
int servo2_test;

void setup() {
servo1.attach(servo1Pin);
servo2.attach(servo2Pin);
}

void loop() {
servo1_test = analogRead(servo1PotPin);
servo1_test = map(servo1_test, 0, 1023, 65, 0); 
servo1.write(servo1_test);
servo2_test = analogRead(servo2PotPin);
servo2_test = map(servo2_test, 0, 1023, 80 , 0);
servo2.write(servo2_test);
delay(5);

}
