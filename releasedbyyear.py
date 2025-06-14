# Python code​​​​​​‌‌​‌‌​​​​​‌‌‌​‌​​​​​‌​​‌‌ below
import json
from datetime import datetime
from typing import List, Dict
from collections import Counter

filename = '/tmp/deps/top250.jsonl'

show_expected_result = False
show_hints = False

# Use print("messages...") to debug your solution.

def get_data(filename: str) -> List[Dict]:
    """Parse movie json files into a list of dicts"""
    with open(filename, "r") as file:
        movies = []
        for line in file:
            movie = json.loads(line)
            try:
                date_released = datetime.strptime(movie["Released"], "%d %b %Y").date()
                movie["Released"] = date_released
                movies.append(movie)
            except ValueError:
                continue
        return movies

movies = get_data(filename)

def released_by_year(movies: List[Dict]) -> Dict:
    """Return the count of movies released each year as a dictionary.
    If no movies were released in a particular year, then that year should not be a part of the dictionary."""    
    #return {1983: 0, 1999:0, 2003:0, 2023: 0} # Replace this line with your solution
    return dict(
            Counter(
                movie['Released'].year
                for movie in movies
            )
    )
