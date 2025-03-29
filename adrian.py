# adrian.py
import requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import config

# Load tokenizer and model for emotion detection
tokenizer = AutoTokenizer.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")
model = AutoModelForSequenceClassification.from_pretrained("bhadresh-savani/distilbert-base-uncased-emotion")
emotion_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Function to fetch a joke
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    return "Sorry, I couldn't find a joke right now."

# Function to fetch a fact based on topic
def get_fact(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['extract']
    return "Sorry, I couldn't find information on that topic."

# Function to choose response based on emotion or command
def choose_response(emotion, text):
    if "adrian" in text.lower():
        return "Yes, I'm here! How can I assist you today?"
    if "tell me a joke" in text.lower():
        return get_joke()
    if "fact about" in text.lower():
        topic = text.split("fact about")[1].strip()
        return get_fact(topic)

    responses = {
        'joy': "It's great to see you happy! What's making you feel good?",
        'sadness': "I'm here if you need to talk. What's making you sad?",
        # Add other emotions and responses as needed
    }
    return responses.get(emotion, "I'm here to help! Can you tell me more?")

def main():
    print("Hello! I'm Adrian. How can I assist you today?")
    while True:
        text = input("You: ")
        if text.lower() == "exit":
            print("Adrian: Goodbye!")
            break

        results = emotion_classifier(text)
        emotion = results[0]['label']
        response = choose_response(emotion.lower(), text)
        print(f"Adrian: {response}")

if __name__ == "__main__":
    main()

