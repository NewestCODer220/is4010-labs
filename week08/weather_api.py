import requests

class WeatherAPI:
    """Client for fetching data from the WeatherAPI service."""

    def __init__(self, api_key: str, base_url: str = "https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def get_current_weather(self, location: str) -> dict | None:
        """Fetch current weather for a location, returning None on failure."""
        url = f"{self.base_url}/current.json"
        params = {"key": self.api_key, "q": location}
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_forecast(self, location: str, days: int = 3) -> dict | None:
        """Fetch weather forecast for 1-3 days, returning None on failure."""
        if not (1 <= days <= 3):
            raise ValueError("Forecast days must be between 1 and 3.")
            
        url = f"{self.base_url}/forecast.json"
        params = {"key": self.api_key, "q": location, "days": days}
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

def format_current_weather(data: dict) -> str:
    """Format current weather as 'CITY, COUNTRY: TEMP°F, CONDITION'."""
    city = data['location']['name']
    country = data['location']['country']
    temp = data['current']['temp_f']
    condition = data['current']['condition']['text']
    
    return f"{city}, {country}: {temp}°F, {condition}"

def format_forecast(data: dict) -> str:
    """Format forecast data into a newline-separated string for each day."""
    lines = []
    for day_data in data['forecast']['forecastday']:
        date = day_data['date']
        high = day_data['day']['maxtemp_f']
        low = day_data['day']['mintemp_f']
        condition = day_data['day']['condition']['text']
        lines.append(f"{date}: high {high}°F, low {low}°F, {condition}")
        
    return "\n".join(lines)