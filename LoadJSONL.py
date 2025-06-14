# Python code​​​​​​‌‌​‌‌​​​​​‌‌‌​​‌​​‌‌‌‌‌​‌ below
import json
from datetime import datetime
from typing import List, Dict

show_expected_result = False
show_hints = False

# Use print("messages...") to debug your solution.

filename = '/tmp/deps/top250.jsonl'

def get_data(filename: str) -> List[Dict]:
    """Parse movie json files into a list of dicts"""
    with open(filename, "r") as file:
        movies = []
        for line in file:
            movie = json.loads(line)
            try:
                date_release = datetime.strptime(movie["Released"], "%d %b %Y").date()
                movie["Released"] = date_release
                movies.append(movie)
            except ValueError:
                continue
        return movies # Replace this line with your solution
