import json
import re

palabras = {
    "bueno": 1, "excelente": 2, "mejor": 1, "fantástico": 2, "increíble": 2,
    "feliz": 1, "genial": 1, "positivo": 1, "amor": 1, "me encanta": 1,
    "maravilloso": 2, "agradable": 1, "perfecto": 2, "fácil": 1, "rápido": 1,
    "bien": 1, "mal": -1, "malo": -1, "peor": -1, "terrible": -2, "horrible": -2, "triste": -1,
    "negativo": -1, "odio": -1, "decepcionante": -2, "difícil": -1, "lento": -1,
    "problema": -1, "error": -1, "fallo": -2, "nunca": -1, "nada": -1
}


def lambda_handler(event, context=None):
    text = event.get("text", "")

    if not text:
        return {"statusCode": 400, "body": json.dumps({"error": "No text provided"})}

    text_cleaned = text.lower()
    words = text_cleaned.split()

    score = 0

    for word in words:
        if word in palabras:
            score += palabras[word]

    if score > 0:
        sentiment = "POSITIVE"
        mood = "Maluma feliz"
        link = "https://co.pinterest.com/pin/18366310959520290"
    elif score < 0:
        sentiment = "NEGATIVE"
        mood = "Maluma triste"
        link = "https://co.pinterest.com/pin/263671753177061319"
    else:
        sentiment = "NEUTRAL"
        mood = "Maluma neutro"
        link = "https://co.pinterest.com/pin/289215607340550271"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "input": text,
            "sentiment": sentiment,
            "score": score,
            "mood": mood,
            "link": link
        })
    }