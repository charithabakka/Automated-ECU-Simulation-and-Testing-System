# Automated ECU Simulation and Testing System

This project simulates automotive ECU behavior by generating sensor data, sending simulated CAN messages, and visualizing vehicle parameters in a LabVIEW dashboard.

## Features
- Simulated sensor data
- CAN message generation using `python-can`
- Test scenarios (e.g., overheat, brake test)
- Visualization in LabVIEW

## Technologies Used
- Python
- LabVIEW
- GitHub

## How to Run
- Run the simulation with: `python sensor_simulator.py`
- Run tests with: `pytest tests/test_cases.py`
