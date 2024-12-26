import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import requests

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {e}")

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            return recognizer.recognize_google(audio).lower()
        except sr.WaitTimeoutError:
            print("No speech detected within the time limit.")
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
        except Exception as e:
            print(f"Speech recognition error: {e}")
    return ""

def get_weather(city="New York"):
    api_key = "your_openweather_api_key"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            return f"The temperature in {city} is {temp} degrees Celsius with {description}."
        else:
            return "I couldn't fetch the weather information."
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return "An error occurred while fetching the weather information."

def play_music():
    music_dir = "Music"  # Update this directory to where your music is stored
    try:
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[2]))
            return "Playing music from your library."
        else:
            return "No songs found in your Music directory."
    except Exception as e:
        print(f"Error playing music: {e}")
        return "An error occurred while trying to play music."

def take_note():
    text_to_speech("What should I note down?")
    note = speech_to_text()
    if note:
        try:
            with open("notes.txt", "a") as file:
                file.write(f"{note}\n")
            return "Note saved successfully."
        except Exception as e:
            print(f"Error saving note: {e}")
            return "An error occurred while saving the note."
    return "No note was provided to save."

def tell_joke():
    try:
        joke = pyjokes.get_joke(language="en", category="neutral")
        print(joke)
        return joke
    except Exception as e:
        print(f"Error fetching joke: {e}")
        return "I couldn't fetch a joke right now."

def main():
    text_to_speech("Hello! How can I assist you today?")
    while True:
        try:
            user_input = speech_to_text()
            if not user_input:
                continue

            if "your name" in user_input:
                text_to_speech("My name is GPT, your assistant.")
            
            elif "time" in user_input:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                text_to_speech(f"The current time is {current_time}.")

            elif "weather" in user_input:
                text_to_speech("Which city do you want the weather for?")
                city = speech_to_text()
                if city:
                    weather_info = get_weather(city)
                    text_to_speech(weather_info)

            elif "youtube" in user_input:
                webbrowser.open("https://www.youtube.com/")
                text_to_speech("Opening YouTube.")

            elif "google" in user_input:
                webbrowser.open("https://www.google.com/")
                text_to_speech("Opening Google.")

            elif "linkedin" in user_input:
                webbrowser.open("https://www.linkedin.com/jobs/")
                text_to_speech("Opening LinkedIn Jobs.")

            elif "joke" in user_input:
                joke = tell_joke()
                text_to_speech(joke)

            elif "play music" in user_input:
                response = play_music()
                text_to_speech(response)

            elif "note" in user_input:
                response = take_note()
                text_to_speech(response)

            elif "exit" in user_input or "quit" in user_input:
                text_to_speech("Goodbye! Have a great day.")
                break

            else:
                text_to_speech("I didn't understand that. Could you please repeat?")
        except Exception as e:
            print(f"Error in main loop: {e}")

if __name__ == "__main__":
    main()

