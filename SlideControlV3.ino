.
// This example shows basic use of a Pololu High Power Stepper Motor Driver.
//
// It shows how to initialize the driver, configure various settings, and enable
// the driver.  It shows how to send pulses to the STEP pin to step the motor
// and how to switch directions using the DIR pin.
//
// Before using this example, be sure to change the setCurrentMilliamps36v4 line
// to have an appropriate current limit for your system.  Also, see this
// library's documentation for information about how to connect the driver:
//   http://pololu.github.io/high-power-stepper-driver

#include <SPI.h>

// Search for HighPowerStepperDriver in Tools>Manage Libraries to get this file
#include <HighPowerStepperDriver.h>


const uint8_t DirPin1 = 2;
const uint8_t StepPin1 = 3;
const uint8_t DirPin2 = 6;
const uint8_t StepPin2 = 5;

const uint8_t CSPin1 = 9;
const uint8_t CSPin2 = 10;
// This period is the length of the delay between steps, which controls the
// stepper motor's speed.  You can increase the delay to make the stepper motor
// go slower.  If you decrease the delay, the stepper motor will go faster, but
// there is a limit to how fast it can go before it starts missing steps.
const uint16_t StepPeriodUs = 500;

int baud_rate = 4800;


float currentStrain = 0;
char sort;
bool slideMove = false;
char slideMode = 'c';
bool slideDir = true;

HighPowerStepperDriver sd;
DRV8711SPI dr;
//SPISettings settings = SPISettings(500000, MSBFIRST, SPI_MODE0);

void setup()
{
  
  SPI.begin();
  
  pinMode(StepPin1, OUTPUT);
  digitalWrite(StepPin1, LOW);
  pinMode(DirPin1, OUTPUT);
  digitalWrite(DirPin1, LOW);

  pinMode(StepPin2, OUTPUT);
  digitalWrite(StepPin2, LOW);
  pinMode(DirPin2, OUTPUT);
  digitalWrite(DirPin2, LOW);
  
 // Initialize 1st Motor Driver
  sd.setChipSelectPin(CSPin1);
  delay(1);

  // Reset the driver to its default settings and clear latched status
  // conditions.
  sd.resetSettings();
  sd.clearStatus();

  // Select auto mixed decay.  TI's DRV8711 documentation recommends this mode
  // for most applications, and we find that it usually works well.
  sd.setDecayMode(HPSDDecayMode::AutoMixed);

  // Set the current limit. You should change the number here to an appropriate
  // value for your particular system.
  sd.setCurrentMilliamps36v4(1000);

  // Set the number of microsteps that correspond to one full step.
  sd.setStepMode(HPSDStepMode::MicroStep16);

  // Enable the motor outputs.
  sd.enableDriver();
  SPI.endTransaction();
  digitalWrite(CSPin2,LOW);

// Initialize 2nd motor driver
  sd.setChipSelectPin(CSPin2);
  // Reset the driver to its default settings and clear latched status
  // conditions.
  sd.resetSettings();
  sd.clearStatus();

  // Select auto mixed decay.  TI's DRV8711 documentation recommends this mode
  // for most applications, and we find that it usually works well.
  sd.setDecayMode(HPSDDecayMode::AutoMixed);

  // Set the current limit. You should change the number here to an appropriate
  // value for your particular system.
  sd.setCurrentMilliamps36v4(1000);

  // Set the number of microsteps that correspond to one full step.
  sd.setStepMode(HPSDStepMode::MicroStep16);

  // Enable the motor outputs.
  sd.enableDriver();
  SPI.endTransaction();
  digitalWrite(CSPin2,LOW);
//  digitalWrite(CSPin2,LOW);
  Serial.begin(baud_rate);
}

void loop()
{

  if (Serial.available()>=3){
    slideMove = Serial.read();
    slideDir = Serial.read(); 
    slideMode = Serial.read();
    SetDir(slideDir); 
    while(slideMove == true){

      // moves both motors
      if (slideMode == 'c'){
        digitalWrite(StepPin1, HIGH);
        digitalWrite(StepPin2, HIGH);
        delayMicroseconds(3);
        digitalWrite(StepPin1, LOW);
        digitalWrite(StepPin2, LOW);
        delayMicroseconds(3);
      }

      // moves only left motor
      else if (slideMode == 'l'){
        digitalWrite(StepPin2,HIGH);
        delayMicroseconds(3);
        digitalWrite(StepPin2,LOW);
        delayMicroseconds(3);
      }
      // moves only right motor
      else if (slideMode == 'r'){
         digitalWrite(StepPin1,HIGH);
        delayMicroseconds(3);
        digitalWrite(StepPin1,LOW);
        delayMicroseconds(3);
      }
      delayMicroseconds(StepPeriodUs);

      if (Serial.available() >= 3){
      slideMove = Serial.read();
      slideDir = Serial.read();
      slideMode = Serial.read();
      SetDir(slideDir);
      }
      
      
    }
    
  }
  delay(5);
  digitalWrite(StepPin1, LOW);
  digitalWrite(StepPin2, LOW);
}

// Sets the direction of both motors
void SetDir(bool dir){
  if (dir == 1){
    digitalWrite(DirPin1,1);
    digitalWrite(DirPin2,1);
  }
  else {
    digitalWrite(DirPin1,0);
    digitalWrite(DirPin2,0);
  }
}
