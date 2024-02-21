import speech_recognition as sr
import urllib.parse
import subprocess

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Error connecting to Google Speech Recognition service; {0}".format(e))
        return None

def search_youtube(query):
    base_url = "https://www.youtube.com/results?"
    query_string = urllib.parse.urlencode({"search_query": query})
    url = base_url + query_string

    # Adjust the Brave browser executable path if necessary
    brave_executable_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    # Open the URL with Brave
    subprocess.run([brave_executable_path, url])

    print(f"Searching YouTube for: {query}")

if __name__ == "__main__":
    while True:
        command = recognize_speech()

        if command:
            if "search for" in command:
                # Extract the search query after "search for"
                query = command.split("search for", 1)[-1].strip()
                search_youtube(query)
            elif "exit" in command:
                print("Exiting the program.")
                break
            else:
                print("Command not recognized. Try saying 'search for [video]' or 'exit'.")
