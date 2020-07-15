void Forward(int Count) {
          while (Count > 0){
          digitalWrite(dirleftPin,HIGH); // Enables the motor to move in a particular direction
          digitalWrite(dirrightPin,HIGH); // Enables the motor to move in a particular direction
          digitalWrite(stepleftPin,HIGH); 
          digitalWrite(steprightPin,HIGH); 
          delayMicroseconds(500); 
          digitalWrite(stepleftPin,LOW); 
          digitalWrite(steprightPin,LOW); 
          delayMicroseconds(500);
          Count = Count -1;
      }
}
void LeftStill(int Count) {
          //On the spot rotation 
          digitalWrite(dirleftPin,LOW); // Enables the motor to move in a particular direction
          digitalWrite(dirrightPin,HIGH); // Enables the motor to move in a particular direction
          digitalWrite(stepleftPin,HIGH); 
          digitalWrite(steprightPin,HIGH); 
          delayMicroseconds(500); 
          digitalWrite(stepleftPin,LOW); 
          digitalWrite(steprightPin,LOW); 
          delayMicroseconds(500);
          
}
void RightStill(int Count) {
         //On the spot rotation
          digitalWrite(dirleftPin,HIGH); // Enables the motor to move in a particular direction
          digitalWrite(dirrightPin,LOW); // Enables the motor to move in a particular direction
          digitalWrite(stepleftPin,HIGH); 
          digitalWrite(steprightPin,HIGH); 
          delayMicroseconds(500); 
          digitalWrite(stepleftPin,LOW); 
          digitalWrite(steprightPin,LOW); 
          delayMicroseconds(500);
}
