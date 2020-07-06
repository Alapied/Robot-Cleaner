
//Argparsing
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing

      // variables to hold the parsed data
char messageFromPC[numChars] = {0};
int count = 0;
float floatFromPC = 0.0;

boolean newData = false;

//============
//Stepper 
const int stepleftPin = 3; 
const int dirleftPin = 5; 
const int steprightPin = 4; 
const int dirrightPin = 6; 



void recv() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();
        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}
void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index

    strtokIndx = strtok(tempChars,",");      // get the first part - the string
    strcpy(messageFromPC, strtokIndx); // copy it to messageFromPC
 
    strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
    count = atoi(strtokIndx);     // convert this part to an integer

    strtokIndx = strtok(NULL, ",");
    floatFromPC = atof(strtokIndx);     // convert this part to a float

    return messageFromPC;
}
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
void Left90(int Count) {
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
void Right90(int Count) {
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
void stepper(String messageFromPC, int Count) {
    if (messageFromPC == "Forward"){
          Forward(Count);
    }else if (messageFromPC == "Right90") {
      Right90();
    }else if (messageFromPC == "Left90") {
     Left90();
    }
    
}
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepleftPin,OUTPUT); 
  pinMode(dirleftPin,OUTPUT);
  pinMode(steprightPin,OUTPUT); 
  pinMode(dirrightPin,OUTPUT);
}
void loop() {
    recv();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        newData == false;
        stepper(messageFromPC,count);
}
}
