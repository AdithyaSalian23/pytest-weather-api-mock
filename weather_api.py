import requests

def get_weather(city):
    url = f"https://api.weather.com/v1/{city}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("temperature", "No temp data")
    except requests.RequestException as e:
        return f"Error: {e}"
