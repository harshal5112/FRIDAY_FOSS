# **Project Description: Friday - AI Voice Assistant**

## **Overview**
Friday is an AI-powered voice assistant designed to automate tasks, control applications, and assist users with various daily activities through voice commands. The assistant leverages speech recognition, text-to-speech synthesis, and automation libraries to provide an interactive and hands-free experience.

---

## **Key Features**

### **1. Voice Interaction**
- Uses `pyttsx3` for text-to-speech output.
- Uses `speech_recognition` for processing user commands.

### **2. System Operations**
- Provides greetings based on the time of day.
- Controls system functionalities such as:
  - **Shutdown, Restart, Lock, Hibernate** the system.
  - **Open/Close applications** like Notepad, Paint, Command Prompt, and Calculator.
  - **Adjust volume** (increase, decrease).
  - **Take notes** in Notepad and Sticky Notes.

### **3. Web Automation**
- Performs Google searches and summarizes results using `BeautifulSoup`.
- Searches and plays videos on YouTube using `pywhatkit`.
- Opens and controls browser windows (`Google Chrome`, `Microsoft Edge`).

### **4. Media Control**
- Plays music from YouTube.
- Opens a local music directory and plays random songs.
- Takes screenshots and saves them with a user-defined name.

### **5. Camera & Image Processing**
- Opens the system's webcam using `OpenCV` (`cv2`).
- Captures live video and displays the feed in a separate window.

### **6. Automation & Navigation**
- Uses `pyautogui` to perform keyboard and mouse automation:
  - Open/Close applications.
  - Minimize/Maximize windows.
  - Handle browser tabs (open, close, switch).
- Retrieves the **system’s IP address** using `requests`.

### **7. Chrome Automation**
- Opens Chrome and automates Google and YouTube searches.
- Creates and manages multiple tabs and windows.

---

## **Technology Stack**
- **Programming Language:** Python
- **Libraries Used:**
  - `pyttsx3` (Text-to-Speech)
  - `speech_recognition` (Voice Commands)
  - `pyautogui` (GUI Automation)
  - `webbrowser` (Opening Web Pages)
  - `BeautifulSoup` (Web Scraping)
  - `requests` (Fetching IP Addresses)
  - `cv2` (OpenCV for Camera Control)
  - `os` and `time` (System Operations)
  - `pywhatkit` (YouTube and Google Searches)

---

## **Use Case Scenarios**
- Hands-free interaction with the computer.
- Automating repetitive tasks (searching, opening/closing apps).
- Controlling music and video playback.
- Quick system actions like shutdown, restart, or locking the PC.
- Enhancing productivity through voice-based note-taking.

---
