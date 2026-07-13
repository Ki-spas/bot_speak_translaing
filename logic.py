import pyttsx3
import requests
from  deep_translator import GoogleTranslator 

def get_fact()  :
    base_url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        russ_fact = data.get("text" ,"problem")
        r_fact = GoogleTranslator(source='auto' , target= 'ru').translate(russ_fact)
        return r_fact
    else:
        return "не получилось"


def speak(text : str) -> None:
    russ_fact = GoogleTranslator(source='auto' , target= 'ru').translate(text)
    engine = pyttsx3.init()
    engine.say(russ_fact)
    engine.runAndWait()



if __name__ == "__main__" :
    text = get_fact()
    print(text)