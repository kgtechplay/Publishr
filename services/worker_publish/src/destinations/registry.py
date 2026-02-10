DESTINATIONS = {}

def register(name: str, plugin):
    DESTINATIONS[name] = plugin

def get(name: str):
    return DESTINATIONS[name]
