import os
import sys
import argparse

try:
    from week08.favorites import FavoritesManager
    from week08.weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = "favorites.json"

def load_api_key():
    """Load the API key from the environment or config.py."""
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
        
    try:
        import config
        return config.WEATHER_API_KEY
    except (ImportError, AttributeError):
        try:
            from week08 import config
            return config.WEATHER_API_KEY
        except (ImportError, AttributeError):
            return None

def build_parser():
    """Build and return the argparse CLI parser."""
    parser = argparse.ArgumentParser(description="Weather CLI application")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # 'current' command
    current_parser = subparsers.add_parser("current", help="Get current weather")
    current_parser.add_argument("location", help="Location or favorite name")
    
    # 'forecast' command
    forecast_parser = subparsers.add_parser("forecast", help="Get weather forecast")
    forecast_parser.add_argument("location", help="Location or favorite name")
    forecast_parser.add_argument("--days", type=int, default=3, help="Days of forecast (1-3)")
    
    # 'favorites' command
    fav_parser = subparsers.add_parser("favorites", help="Manage favorites")
    fav_subparsers = fav_parser.add_subparsers(dest="favorites_command", required=True)
    
    fav_add = fav_subparsers.add_parser("add", help="Add a favorite location")
    fav_add.add_argument("name", help="Favorite name")
    fav_add.add_argument("location", help="Location string")
    
    fav_subparsers.add_parser("list", help="List all favorites")
    
    fav_remove = fav_subparsers.add_parser("remove", help="Remove a favorite")
    fav_remove.add_argument("name", help="Favorite name")
    
    return parser

def main(argv=None) -> int:
    """Main CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    
    # 1. Load API Key
    api_key = load_api_key()
    if not api_key:
        print("Error: API key not found.", file=sys.stderr)
        return 1
        
    api = WeatherAPI(api_key)
    fav_manager = FavoritesManager(FAVORITES_FILE)
    
    # 2. Handle 'favorites' subcommands
    if args.command == "favorites":
        if args.favorites_command == "add":
            success = fav_manager.add(args.name, args.location)
            if not success:
                print(f"Error: Favorite '{args.name}' already exists.", file=sys.stderr)
                return 1
            print(f"Added {args.name} as {args.location}")
            return 0
            
        elif args.favorites_command == "list":
            all_favs = fav_manager.list_all()
            if not all_favs:
                print("No favorites saved.")
            else:
                for name, loc in all_favs.items():
                    print(f"{name}: {loc}")
            return 0
            
        elif args.favorites_command == "remove":
            success = fav_manager.remove(args.name)
            if not success:
                print(f"Error: Favorite '{args.name}' not found.", file=sys.stderr)
                return 1
            print(f"Removed favorite: {args.name}")
            return 0

    # 3. Handle 'current' and 'forecast' commands
    location_query = args.location
    saved_location = fav_manager.get_location(location_query)
    if saved_location:
        location_query = saved_location
        
    if args.command == "current":
        data = api.get_current_weather(location_query)
        if not data:
            print("Error: Failed to fetch current weather.", file=sys.stderr)
            return 1
        print(format_current_weather(data))
        return 0
        
    elif args.command == "forecast":
        try:
            data = api.get_forecast(location_query, args.days)
            if not data:
                print("Error: Failed to fetch forecast.", file=sys.stderr)
                return 1
            print(format_forecast(data))
            return 0
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

if __name__ == "__main__":
    sys.exit(main())