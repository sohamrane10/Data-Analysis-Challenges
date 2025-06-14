# Python code​​​​​​‌‌​‌‌​​​​​‌‌‌​‌​​​‌​​‌‌​‌ below
from typing import List, Dict
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

def parse_runtime(movie_runtime: str) -> int:
    runtime, _ = movie_runtime.split(" ")
    return int(runtime)

def sort_by_runtime(movies: List[Dict], *, shortest=0, longest=10_000) -> List:
    """Return movies sorted by their runtimes as a list of (runtime, title) tuples."""
    
    return sorted(
        (parse_runtime(movie['Runtime']), movie['Title'])
        for movie in movies
        if shortest <= parse_runtime(movie['Runtime']) <= longest
    )
    
