#include "esphome.h"
#include "FastAccelStepper.h"

FastAccelStepperEngine engine = FastAccelStepperEngine();
FastAccelStepper *my_stepper = NULL;

void init_fast_stepper() {
  engine.init();
  my_stepper = engine.stepperConnectToPin(33); // STEP
  if (my_stepper) {
    my_stepper->setDirectionPin(32); // DIR
    my_stepper->setEnablePin(13, true); // EN
    my_stepper->setAutoEnable(true); 
    my_stepper->setDelayToDisable(200); 
    
    my_stepper->setSpeedInHz(3600); 
    my_stepper->setAcceleration(1600);
  }
}