import json

class FavoritesManager:
    """Manages favorite locations stored in a JSON file."""

    def __init__(self, filename="favorites.json"):
        self.filename = filename
        self.favorites = self._load()

    def _load(self) -> dict:
        """Load favorites from JSON file, returning empty dict if missing or corrupted."""
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return data if isinstance(data, dict) else {}
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return {}

    def _save(self) -> None:
        """Save current favorites to JSON file with indent=4."""
        with open(self.filename, "w") as f:
            json.dump(self.favorites, f, indent=4)

    def add(self, name: str, location: str) -> bool:
        """Add a favorite location. Returns True if added, False if duplicate exists."""
        key = name.lower()
        if key in self.favorites:
            return False
        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name: str) -> bool:
        """Remove a favorite location by name. Returns True if removed, False if missing."""
        key = name.lower()
        if key in self.favorites:
            del self.favorites[key]
            self._save()
            return True
        return False

    def list_all(self) -> dict:
        """Return a dictionary of all favorites."""
        return dict(self.favorites)

    def get_location(self, name: str) -> str | None:
        """Get location string for favorite name, case-insensitively."""
        return self.favorites.get(name.lower())