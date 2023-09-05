# Hpcl-Project-New
﻿<h1><img align="center" height="30" src="https://user-images.githubusercontent.com/88069082/225035704-464df7f6-031c-472d-b03b-6374c5991023.jpeg"> Security Hooter at HPCL Bengaluru Terminal</h1>

## Contents
- Abstract and Introduction / Executive Summary
- Description of the Components
    - Raspberry Pi 3 B+ 
    - 5 inch LCD Display
    - Jumper Wires
    - Breadboard
    - IR Sensors
    - Speaker
 - Connections in the Circuit
 - Working Principle

## Abstract and Introduction / Executive Summary

 HPCL is having Terminal Automation system for complete plant            operation. As the location is handling hydrocarbons, which is a hazardous material, it is also required to keep the plant in the safest manner to eliminate any accidents.
 As a part of safety plant has installed below instruments which are already integrated with safety PLC : 

1. Hydrocarbon detector (HCD ACTIVATED) : These are sensors which detect any hydrocarbon vapour and give (4-20)mA signal to indicate vapour percentage in air. As these vapours are prone to catch fire, this helps in early detection of hydrocarbon exposure and plants can take immediate action.

2. Emergency Shutdown (PLANT ESD ACTIVATED) : This is a feature by which plant complete shutdown can be done through push buttons available across the plant in strategic location.This buttons can be operated by any person inside plants if they find any fire/leak/any emergency.

3. Dyke Valve (DYKE VALVE OPENED) : This is valve positioning indicator, which indicates the dyke valve OPEN/CLOSE status.Dyke is the compound walls available around tanks,meant for containing the tank product in case the tank collapse/leak/punctured.However during rain this dyke area get filled with water and few floating roof tanks also conceive water.To drain this water it has to be supervised as there is chance of passing product outside.

4. Fire Activation Panel (SMOKE DETECTOR ACTIVATED) : There are smoke detectors installed in the control room to detect Smoke/Fire in panels. As these panels are having lots of hardware/power cables etc, there is a chance of short circuit/overheating/burning due to electrical surge,hence it is the most important to detect smoke/fire during its initial stage.

5. Emergency Gate Open : There is a emergency gate near the pant, which is used to vacate people during alerting situations

All these instruments give signals and produce audio visual alarms in the control room.

## Connections in the Circuit 

<img width="705" alt="image" src="https://user-images.githubusercontent.com/88069082/225034091-b2da7506-48f6-434a-a5e7-70254b69be45.png">
