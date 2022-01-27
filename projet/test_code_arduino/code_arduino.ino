const int dirPin=2;
const int stepPin=3;
const int stepsPerRev=1600;
const float degPerStep = 360 / stepsPerRev;

void setup() {
  current_value = 0;
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  value = Serial.read();

  if value != current_value{
    rotationAngle = value - current_value;              // rotation à faire en degré
    if rotationAngle > 0 {
      digitalWrite(dirPin, HIGH);                       // clockwise
    }
    if rotationAngle < 0 {
      digitalWrite(dirPin, LOW);                        // counter clockwise
      rotationAngle = rotationAngle * -1;
    }
    steps = rotationAngle / degPerStep;                 // nombre de steps à faire en décimal
    int roundSteps = round(steps);                      // nombre de steps arrondi 
    
    for(int x=0;x<roundSteps; x++)
      {
        digitalWrite(stepPin, LOW);
        delayMicroseconds(4000);
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(4000);
      }
    current_value = value;
    delay(1000);
    
  }
}
