const int dirPin=2;
const int stepPin=3;
const int stepsPerRev=1600;
const float degPerStep = 360 / stepsPerRev;
int current_value = 0;
int value;

void setup() {
  
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    value = Serial.parseInt();

    if (value != current_value){
//      if (value > current_value){
//        digitalWrite(dirPin, LOW);
//      }
//      else if (value < current_value){
//        digitalWrite(dirPin, HIGH);
//      }
      int rotationAngle = abs(value - current_value);       // rotation à faire en degré
      
//      if (rotationAngle > 0) {
//        digitalWrite(dirPin, HIGH);                       // clockwise
//      }
//      else if (rotationAngle < 0) {
//        digitalWrite(dirPin, LOW);                        // counter clockwise
//        rotationAngle = rotationAngle * -1;
//      }

     float steps = rotationAngle / degPerStep;           // nombre de steps à faire en décimal
     int roundSteps = round(steps);                      // nombre de steps arrondi 
     
      for(int x=0;x<value; x++)
        {
          digitalWrite(stepPin, LOW);
          delayMicroseconds(4000);
          digitalWrite(stepPin, HIGH);
          delayMicroseconds(4000);
        }
      current_value = value;
      delay(10);
    }
    }
  }
