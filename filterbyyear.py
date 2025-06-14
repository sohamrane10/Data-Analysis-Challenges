# Python code​​​​​​‌‌​‌‌​​​​​‌‌‌​‌​​​​​​​​‌‌ below
import json
from datetime import datetime
from typing import List, Dict

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

def filter_by_year(movies: List[Dict], year: int) -> List:
    """Return all movie titles for movies released in a certain year"""
    return [
            movie['Title']
            for movie in movies
            if movie['Released'].year == year
    ] # Replace this line with your solution
