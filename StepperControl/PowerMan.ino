void Shutdown() {
  bool Pi;
  Pi = digitalRead(powercheck);
  if (Pi = false){
    delay(4);
    digitalWrite(sigMainPin,LOW);
  }
}


void PowerStep(int Count){
  switch (Count){ 
        case 0: 
            digitalWrite(sigStepPin, HIGH);
            break; 
        case 1: 
            digitalWrite(sigStepPin, LOW);
            break; 
         
    };
}
