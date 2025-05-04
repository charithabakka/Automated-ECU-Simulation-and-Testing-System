# Automated ECU Simulation and Testing System

## Objective
To simulate and validate automotive ECU behavior through sensor data emulation, CAN message generation, and visual feedback using LabVIEW.

## Overview
This project replicates ECU responses to driving conditions like speed, temperature, and RPM using:
- Python for sensor simulation and CAN message generation
- LabVIEW for real-time visualization
- Git for version control

## Technologies Used
- Python 3.x (`python-can`, `pytest`, `pandas`)
- LabVIEW 2021+
- Git (GitHub)
- Optional: Docker, Visual Studio

## Target Outcome
- Run predefined automotive test scenarios
- Simulate sensor data & CAN messaging
- Display parameters in LabVIEW
- Evaluate test pass/fail logic

## Test Case Table

| Test Case ID | Description | Input Simulated | Expected Behavior |
|--------------|-------------|------------------|--------------------|
| TC_01 | Vehicle Speed Ramp-Up Test | Speed from 0 to 120 km/h | Speed updates, CAN messages sent |
| TC_02 | Overheat Shutdown Test | Engine temp to 130°C | Warning at 110°C, shutdown at 125°C |
| TC_03 | Sudden Braking Test | Speed drop 100 to 0 | Brake pressure increase, CAN signal |
| TC_04 | High RPM Cutoff | RPM up to 7000 | Cutoff/warning at 6500 RPM |
| TC_05 | CAN Message Timeout | Pause CAN messages | Fallback mode triggered |
| TC_06 | Sensor Noise Test | Inject noisy signal | System filters or flags it |
