Friday: AI-Powered Coding Assistant

Project Description

Friday is an AI-powered voice assistant tailored specifically for coders. It assists with coding-related challenges such as:

Finding syntax for basic pages or applications.

Providing guidance on folder structure for projects.

Allowing users to copy code snippets from lectures for easy implementation.

Automating coding tasks to enhance productivity.

Overview

Friday leverages speech recognition, text-to-speech synthesis, and automation libraries to offer an interactive and hands-free coding assistant. It aims to streamline development by minimizing repetitive tasks and providing quick access to essential coding resources.

Key Features

Voice Interaction

Uses pyttsx3 for text-to-speech output.

Uses speech_recognition for processing user commands.

Coding Assistance

Provides syntax for commonly used programming constructs.

Suggests folder structures for different projects (web, app, machine learning, etc.).

Enables copying code from lectures for direct implementation.

System Operations

Provides greetings based on the time of day.

Controls system functionalities such as:

Shutdown, Restart, Lock, Hibernate the system.

Open/Close coding applications like VS Code, Terminal, and Notepad++.

Adjust volume (increase, decrease).

Take notes in Notepad and Sticky Notes.

Web Automation for Coding Resources

Searches for code snippets and syntax references on Stack Overflow and documentation sites.

Summarizes search results using BeautifulSoup.

Opens and controls browser tabs for coding resources.

Media Control

Plays coding tutorial videos from YouTube.

Opens saved local tutorials.

Takes screenshots and saves them with a user-defined name.

Automation & Navigation

Uses pyautogui for:

Navigating between applications.

Automating typing for repetitive code.

Handling browser tabs (open, close, switch).

Retrieves system’s IP address using requests.

Chrome Automation

Opens Chrome and automates searches for coding-related topics.

Creates and manages multiple tabs and windows.

Technology Stack

Programming Language: Python
Libraries Used:

pyttsx3 (Text-to-Speech)

speech_recognition (Voice Commands)

pyautogui (GUI Automation)

webbrowser (Opening Web Pages)

BeautifulSoup (Web Scraping)

requests (Fetching IP Addresses)

cv2 (OpenCV for Camera Control)

os and time (System Operations)

pywhatkit (YouTube and Google Searches)

'selenium'

Use Case Scenarios.

Hands-free coding assistance for faster development.

Quick access to syntax references and code snippets.

Automating repetitive coding tasks.

Controlling IDEs and terminals via voice commands.

Enhancing productivity by reducing manual search efforts.
