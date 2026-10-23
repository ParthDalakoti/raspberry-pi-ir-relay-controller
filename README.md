# Raspberry Pi 3B Linux GPIO Infrared Remote Appliance Switch

[![Microcontroller](https://img.shields.io/badge/MCU-Raspberry_Pi_3B-E7352C.svg?style=for-the-badge)](https://www.espressif.com/)
[![Protocols](https://img.shields.io/badge/Protocols-Linux_sysfs_GPIO,_38kHz_IR_Pulse_Decoding-blue.svg?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Tested_%26_Verified-success.svg?style=for-the-badge)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Embedded Hardware & Firmware Project | Graphic Era Hill University (B.Tech ECE 2023–2027)**  
> **Author:** Parth Dalakoti (*President, Robotics & Automation Club, GEHU*)  
> **Contact:** `parthdalakoti482@gmail.com` | [LinkedIn](https://linkedin.com/in/parthdalakoti)

---

## ⚡ Executive Engineering Summary
Embedded Linux IR Remote Receiver and Relay Switch Daemon using Python RPi.GPIO on Raspberry Pi 3B. This project is an independent engineering system designed, built, and tested by **Parth Dalakoti** during his B.Tech in Electronics & Communication Engineering.

---

## 🛠️ Hardware Stack & Specifications
* **Target Microcontroller:** `Raspberry Pi 3B`
* **Primary Protocols & Interfaces:** `Linux sysfs GPIO, 38kHz IR Pulse Decoding`
* **Firmware Location:** [`firmware/`](firmware/)
* **Technical Documentation & Reports:** [`docs/`](docs/)
* **Hardware Wiring & Schematics:** [`hardware/`](hardware/)

---

## 🔌 Hardware Connections & Architecture

```mermaid
graph LR
    Sensors[Sensors / Input Interface] -->|Linux sysfs GPIO, 38kHz IR Pulse Decoding| MCU[Raspberry Pi 3B]
    MCU -->|PWM / Driver Control| Actuator[Actuator / Load Output]
    MCU -->|Status / Telemetry| Display[Status Output / Feedback]
```

---

## 🚀 How to Build & Flash
1. Open the source code in [`firmware/`](firmware/) using **Arduino IDE** or **VS Code PlatformIO**.
2. Select target board: `Raspberry Pi 3B`.
3. Configure serial baud rate (115200 or 9600 baud as defined in firmware).
4. Connect board and flash.

---

## 👨‍💻 Engineering Author
**Parth Dalakoti**  
*President, Robotics & Automation Club*  
*B.Tech in Electronics & Communication Engineering (2023–2027)*  
*Graphic Era Hill University (GEHU), Bhimtal Campus*  
*Contact:* `parthdalakoti482@gmail.com` • [GitHub Profile](https://github.com/ParthDalakoti)
