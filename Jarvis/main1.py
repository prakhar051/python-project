# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import musicLiberary  # Ensure this is defined properly
# import requests
# from openai import OpenAI  # Ensure OpenAI package is installed
# from gtts import gTTS
# import pygame
# import os
# # Initialize the recognizer and text-to-speech engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "8f85265174de41b5ab66f6de0c88daaa"


# def speak(text):
#     """Function to speak the given text using pyttsx3."""
#     engine.say(text)
#     engine.runAndWait()

# # def speak(text):
    
# #      tts = gTTS(text)
# #      tts.save('temp.mp3')

    


# #      # Initialize Pygame
# #      pygame.init()
     
# #      # Initialize the mixer
# #      pygame.mixer.init()
     
# #      # Load the MP3 file
# #      pygame.mixer.music.load('your_song.mp3')  # Replace with your MP3 file path
     
# #      # Play the music
# #      pygame.mixer.music.play()
     
# #      # Keep the program running while the music is playing
# #      try:
# #          while pygame.mixer.music.get_busy():  # Wait until the music finishes playing
# #              pygame.time.Clock().tick(10)  # Limit the loop to 10 times per second
# #      except KeyboardInterrupt:
# #          # Stop the music and quit if you press Ctrl+C
# #          pygame.mixer.music.stop()
# #      finally:
# #          pygame.quit()
     
     

# def aiProcess(command):
#     client = OpenAI(
#         api_key="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"
#     )

#     completion = client.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give Short responses please"},
#             {
#                 "role": "user",
#                 "content": command}
#         ]
#     )

#     return completion.choices[0].message['content']  # Ensure to return only the content


# def processCommand(c):
#     """Process recognized voice command."""
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")
#     elif "open samsung" in c.lower():
#         webbrowser.open("https://samsung.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLiberary.music.get(song, None)
#         if link:
#             webbrowser.open(link)
#         else:
#             speak(f"Sorry, I don't have the song {song} in my library.")
#     elif "news" in c.lower():
#         # Corrected request to fetch news
#         url = "https://newsapi.org/v2/top-headlines"
#         params = {
#             "country": "in",  # Change the country code as per your preference
#             "apiKey": newsapi
#         }
#         r = requests.get(url, params=params)
#         if r.status_code == 200:
#             # Parse the JSON response
#             data = r.json()

#             # Extract the headlines
#             articles = data.get("articles", [])
            
#             if articles:
#                 # Speak each article's title
#                 for article in articles[:5]:  # Limiting to 5 headlines for brevity
#                     title = article.get('title', 'No title available')
#                     speak(title)
#             else:
#                 speak("No news articles available right now.")
#         else:
#             speak(f"Sorry, I couldn't fetch the news. Error: {r.status_code}")
#     else:
#         # Let OpenAI handle the request
#         response = aiProcess(c)
#         speak(response)  # Speak the AI response


# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
    
#     # Print list of available microphones (for troubleshooting)
#     print("Available microphones:")
#     print(sr.Microphone.list_microphone_names())

#     while True:
#         try:
#             # Use microphone to listen for audio
#             with sr.Microphone() as source:
#                 print("Adjusting for ambient noise...")
#                 recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
#                 print("Listening....")
#                 audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)

#             # Recognize speech using Google API
#             command = recognizer.recognize_google(audio)  # You can use recognize_sphinx for offline

#             if "jarvis" in command.lower():  # Changed to check for "jarvis" in command
#                 speak("Yes?")
#                 with sr.Microphone() as source:
#                     print("Adjusting for ambient noise...")
#                     recognizer.adjust_for_ambient_noise(source)
#                     print("Jarvis Active....")
#                     audio = recognizer.listen(source)
#                     command = recognizer.recognize_google(audio)
#                     processCommand(command)

#             print(f"You said: {command}")

#         except sr.UnknownValueError:
#             print("Could not understand audio.")
#             speak("Sorry, I could not understand that.")

#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")
#             speak("There was an error connecting to the speech recognition service.")
