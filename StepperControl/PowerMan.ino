void Shutdown() {
  bool Pi;
  Pi = digitalRead(powercheck);
  if (Pi = 0){
    digitalWrite(sigMainPin,LOW);
  }
}


void PowerStep(){
  
}
