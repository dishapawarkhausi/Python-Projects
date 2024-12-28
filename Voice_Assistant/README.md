# Python-based Voice Assistant

This is a Python-based voice assistant that performs various tasks, including weather reporting, note-taking, joke-telling, playing music, and web browsing. It uses speech recognition and text-to-speech capabilities to interact with users.

---

## Features

- **Speech-to-Text (STT):** Converts user speech into text.
- **Text-to-Speech (TTS):** Responds to user commands with a synthesized voice.
- **Weather Information:** Provides current weather updates for a specified city.
- **Music Playback:** Plays songs from a local directory.
- **Note-Taking:** Saves dictated notes to a text file.
- **Jokes:** Tells a random joke.
- **Web Browsing:** Opens popular websites like YouTube, Google, and LinkedIn.
- **Exit Command:** Gracefully shuts down the assistant.

---

## Requirements

Ensure you have the following installed:

- **Python 3.7+**
- **Required Libraries:**
  ```bash
  pip install pyttsx3 speechrecognition pyjokes requests
  ```

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/dishapawarkhausi/Python-Projects/Voice_Assistant.git
   cd voice-assistant
   ```

2. Replace the placeholder for the OpenWeather API key in the `get_weather` function:
   ```python
   api_key = "your_openweather_api_key"
   ```
   Get your API key from [OpenWeather](https://openweathermap.org/api).

3. Ensure you have a folder named `Music` in the project directory with some audio files.

4. Run the script:
   ```bash
   python voice_assistant.py
   ```

---

## Usage

- Start the assistant by running the script.
- Speak commands such as:
  - **"What's the weather in New York?"**
  - **"Play music."**
  - **"Tell me a joke."**
  - **"Take a note."**
  - **"Open YouTube."**
  - **"What time is it?"**
  - **"Exit."**

---

## File Structure

- `voice_assistant.py`: Main script for the assistant.
- `notes.txt`: File where notes are saved.

---

## Limitations

- Requires an active internet connection for certain features like weather updates and web browsing.
- The accuracy of speech recognition depends on the microphone quality and background noise.

---

## Future Enhancements

- Add support for multiple languages.
- Enhance natural language understanding.
- Integrate more APIs for diverse functionalities.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
