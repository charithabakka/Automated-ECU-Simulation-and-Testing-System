# 🚗 Automated ECU Simulation and Testing System

This project simulates automotive ECU behavior by generating sensor data, sending simulated CAN messages, and visualizing vehicle parameters in a LabVIEW dashboard. It’s aimed at testing and validating ECUs in an automotive system using software automation.

## 📝 Project Overview

This system provides the following capabilities:
- Simulate various automotive sensor data (e.g., speed, temperature, RPM)
- Generate and transmit CAN messages to simulate ECU communication
- Define test scenarios (such as overheating, sudden braking, and high RPM)
- Visualize simulated parameters in a LabVIEW dashboard for real-time monitoring
- Implement test automation with `pytest` for automated verification of ECU behavior

## 🧰 Technologies Used

- **Python**: For simulating sensor data and CAN bus communication
- **LabVIEW**: For real-time data visualization in the dashboard
- **Git/GitHub**: For version control and project collaboration
- **`python-can`**: Python library for CAN bus simulation
- **`pytest`**: Framework for automating and validating test scenarios
- **Visual Studio**: IDE for Python development and testing

## 🗂️ Project Structure
AETF/
├── docs/
│ └── Project_Brief.md # Project scope and test cases
├── simulation/
│ └── sensor_simulator.py # Main simulation script
├── tests/
│ └── test_cases.py # Automated test cases
├── Road map.txt # Project planning notes
├── Project_Idea.txt # Idea summary
└── README.md # This file

## 🧪 Test Scenarios

Example test cases:
- **Speed Ramp Test**: Accelerate from 0 to 120 km/h.
- **Engine Overheat**: Trigger engine shutdown after reaching 125°C.
- **Sudden Braking Test**: Simulate a sudden stop from 100 km/h to 0.
- **High RPM Cutoff**: Trigger cutoff/warning at 6500 RPM.
- **CAN Message Timeout**: Simulate dropped CAN messages.

These test cases can be expanded further based on additional requirements.

## 🚀 How to Run

1. **Install dependencies** (if not already installed):
   ```bash
   pip install python-can pytest

2. Run the Simulation:
To simulate sensor data and CAN messages, execute the following:
bash
python simulation/sensor_simulator.py

3. Run Tests:
Run automated tests to verify the simulation's accuracy:

bash
pytest tests/test_cases.py

4. View Dashboard:
Open LabVIEW and load the dashboard VI to monitor the simulated parameters in real-time.

📈 Roadmap
 Add GUI controls to the LabVIEW dashboard for real-time adjustments.

 Simulate additional sensors (e.g., GPS, battery voltage).

 Integrate Docker to create a self-contained testing environment.

 Add more complex test cases and validation logic.

🤝 Contributions
Feel free to contribute by submitting pull requests. If you have any suggestions or feature requests, please open an issue.

