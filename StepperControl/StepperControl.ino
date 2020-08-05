
//Include Libaries
#include <Adafruit_NeoPixel.h>

//BootChecks
bool PiBoot;
bool confirm;
const int powercheck = 7;
const int sigMainPin = 9;
const int sigStepPin = 10;
const int Errorpin = 13;
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

//NeoPixels
#define PIN 8
#define NUM_LEDS 8
//create a NeoPixel strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

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

}
void PiBootCheck(){
  //tests serial comms and determines if Pi is running
  String Pi;
  
  recv();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        newData == false;
  Pi = messageFromPC;
    if (Pi == "Pi ON"){
      PiBoot = true;
      Serial.println("Connected");
      while (confirm == false){
        recv();
        if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        newData == false;
        Pi = messageFromPC;
          if (Pi == "confirm"){
            confirm = true;
            break;
          }
        }
      }
      //if (Errorpin == true){
        //PiBoot = false;
      //}
      }
      
    }
}
void recieveOther(String messageFromPC, int Count) {
  if (messageFromPC = "Led"){
    led(messageFromPC, Count);
  }else if (messageFromPC = "PowerStep"){
    PowerStep(Count);
  }else if (messageFromPC = "PowerPi")
    Shutdown();
}

void stepper(String messageFromPC, int Count) {
    if (messageFromPC == "Forward"){
          Forward(Count);
    }else if (messageFromPC == "Right90") {
      RightStill(Count);
    }else if (messageFromPC == "Left90") {
     LeftStill(Count);
    }
    else{
      recieveOther(messageFromPC, Count);
      }
}
void setup() {
  Serial.begin(9600);
  PiBoot = false;
  // start the Pixel strip and blank it out
  strip.begin();
  strip.show();
  // Sets the two stepper pin pairs as Outputs
  pinMode(stepleftPin,OUTPUT); 
  pinMode(dirleftPin,OUTPUT);
  pinMode(steprightPin,OUTPUT); 
  pinMode(dirrightPin,OUTPUT);

  // Sets the controls for power relays
  pinMode(sigMainPin,OUTPUT); 
  pinMode(sigStepPin,OUTPUT);
  digitalWrite(sigMainPin,HIGH); //Turns on the raspberry pi and keeps the power on Like a flip flop switch
}
void loop() {
    //do not continue with anything until Pi is cofirmed to be booted (and show lights)
    while (PiBoot == false and confirm == false){
       LEDBOOT();
       PiBootCheck();
    }
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
