# Weather Text-to-Speech (TTS) Python Project

This Python project fetches the **current weather** of any city using the **OpenWeatherMap API** and reads it aloud using **Windows Text-to-Speech (TTS)**.

---

## Features

- Get the current temperature of any city in Celsius.
- Windows TTS reads the temperature aloud.
- Handles invalid city names or API errors gracefully.
- Secure usage of API key via `.env` file.

---

## Requirements

- Python 3.x
- Windows OS (for TTS via `win32com.client`)
- Python packages:
  - `requests`
  - `pywin32`

### Install Dependencies

```bash
pip install requests python-dotenv pywin32
