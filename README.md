# Adrian: Ethical AI Companion Robot 🤖💫

**Adrian** is a Raspberry Pi–powered robot companion designed with systems thinking, ethical AI principles, and emotional intelligence at its core. Built with voice interaction, touchscreen GUI, and hardware-driven expression, Adrian is your thoughtful lab partner and friend.

---

## 🧠 Features
- 🗣️ **Voice Interaction** via USB Lavalier Mic + Vosk
- 🖼️ **Vision System** with Arducam Camera Module
- 🖐️ **Servo Control** (10x SG90 micro servos)
- 👂 **Ultrasonic Sensing** (5x HC-SR04 modules)
- 📱 **Touch Interface** using 7" Raspberry Pi Display
- 🌈 (Upcoming) Emotion display via RGB LEDs
- 💬 (Upcoming) Ethical conversation layer

---

## 🔩 Hardware
| Component                      | Notes                                   |
|-------------------------------|-----------------------------------------|
| Raspberry Pi 4 (8GB)          | Main compute unit                       |
| Vilros Power Supply           | 5.1V 3A USB-C                           |
| Vilros Aluminum Case + Fan    | Cooling and protection                  |
| Arducam IMX708 Camera         | Autofocus, 75° FoV                      |
| 7" Raspberry Pi Touch Display | On-screen GUI                           |
| 10x SG90 Micro Servos         | Gestures, mechanical expression         |
| L298N Motor Driver            | Drives servo/DC motors (power split)   |
| HC-SR04 Ultrasonic Sensors    | Proximity awareness                     |
| Maono USB Lavalier Microphone | Voice input                             |
| Samsung/SanDisk microSD Cards | 32–64GB, Class 10                       |

---

## 📦 Software Stack
- Raspberry Pi OS (64-bit)
- Python 3
- Key Libraries:
  - `gpiozero`, `RPi.GPIO`, `OpenCV`, `speech_recognition`, `vosk`, `flask`, `pygame`

---

## 🚀 Getting Started
1. Flash Raspberry Pi OS using Raspberry Pi Imager
2. Boot Pi with touchscreen + connect to Wi-Fi
3. Run initial setup from [`docs/setup.md`](docs/setup.md)
4. Test mic, camera, servos, and GUI
5. Build, bond, and grow 🌱

---

## 📁 Project Structure
