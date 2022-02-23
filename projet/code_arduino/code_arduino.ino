const int dirPin=2;
const int stepPin=3;
int value;
int steps;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    value = Serial.parseInt();
    //value = -100;
    
    if (value < 0)
    {
      digitalWrite(dirPin, LOW);
      steps = abs(value);
    }
    
    else if (value > 0)
    {
      digitalWrite(dirPin, HIGH);
      steps = abs(value);
    }

    for(int x=0;x<steps; x++)
    {
      digitalWrite(stepPin, LOW);
      delayMicroseconds(4000);
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(4000);
    }
    
      delay(100);
  }
}
  
