const int dirPin=2;
const int stepPin=3;
const int stepsPerRev=1600;

void setup()
{
  pinMode(stepPin,OUTPUT);
  pinMode(dirPin,OUTPUT);
}

void loop()
{
  digitalWrite(dirPin,HIGH); //clockwise

  for(int x=0;x<(stepsPerRev/4); x++)
  {
    digitalWrite(stepPin, LOW);
    delayMicroseconds(4000);
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(4000);
  }
  delay(1000);
  
  digitalWrite(dirPin,LOW); //counter clockwise
  for(int x=0;x<(stepsPerRev/4); x++)
  {
    digitalWrite(stepPin, LOW);
    delayMicroseconds(4000);
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(4000);
  }
    delay(1000);
}
