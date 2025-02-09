from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import requests
import os
import math

load_dotenv()
API_KEY = os.getenv("API_KEY", None)

if API_KEY is None:
    raise RuntimeError("Missing API_KEY, cannot start server!")

app = FastAPI()


def calculate_price(items: list):
    min = math.inf
    max = 0

    for item in items:
        price = item.get("price", None)
        if price is None:
            continue

        if price < min:
            min = price
        if price > max:
            max = price

    if len(items) == 0 or min == max:
        return f"${min}"
    else:
        return f"${min} - ${max}"


def format_features(features_str):
    features = []
    for feature in features_str.split("\r\n"):
        feature = str(feature)
        if feature.startswith("- "):
            feature = feature[2:]

        features.append(feature)

    return features


@app.get("/current-deal")
def get_current_deal():
    data = requests.get(f"https://api.meh.com/1/current.json?apikey={API_KEY}")
    deal = data.json().get("deal", None)

    if deal is None:
        return HTTPException(status_code=500)

    return {
        "title": deal.get("title"),
        "price": calculate_price(deal.get("items", [])),
        "soldOut": deal.get("soldOut", False) is True,
        "features": format_features(deal.get("features", "")),
        "photos": deal.get("photos", []),
        "theme": deal.get("theme", {}).get("foreground", "light")
    }
