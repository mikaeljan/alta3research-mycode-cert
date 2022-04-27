#!/usr/bin/env python3
"""Star Wars API HTTP response parsing"""

# pprint helps make things like dictionaries more human-readable
from pprint import pprint
import requests

URL = "http://api.open-notify.org/"


def main():
    """getting at the JSON attached to this response"""

    # Open Notify - Astros response is stored in "response" object
    response = requests.get(f'{URL}'+'astros.json')
    jsonResponse = response.json()
    people = jsonResponse.get("people")
    message = jsonResponse.get("message")
    pprint(jsonResponse)

    # Prints the number of people in space and the outcome of the mission
    print(
        f"\nThere were {len(people)} members and the mission was a {message}!\n")
    for person in people:
        print(person.get("name"))


if __name__ == "__main__":
    main()
