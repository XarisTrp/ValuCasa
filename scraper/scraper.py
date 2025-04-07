# MIT License
#
# Copyright (c) 2025 Spyros Mitsis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from curl_cffi import requests
import os
from pydantic import BaseModel
from rich import print
import time
from typing import List, Dict, Any

class House(BaseModel):
    house_id: int
    sq_meters: int
    price: int
    geography: str
    floorNumber: int
    rooms: int
    no_of_bathrooms: int
    kitchens: int
    livingRooms: int

def new_session():
    session = requests.Session(impersonate="chrome")
    return session

def fetch_properties(session, start_offset=0, end_offset=10200, step=300) -> List[House]:
    """
    Fetches property data from the API and returns a list of House objects.
    
    Args:
        session: The requests session to use.
        start_offset: The starting offset.
        end_offset: The ending offset.
        step: The step size for the offset.
        
    Returns:
        A list of House objects.
    """
    all_houses = []
    
    for offset in range(start_offset, end_offset, step):
        url = f"https://www.spitogatos.gr/n_api/v1/properties/search-results-map?listingType=sale&category=residential&areaIDs[]=100&sortBy=rankingscore&sortOrder=desc&offset={offset}"
        print(f"Fetching data from offset {offset}...")
        
        try:
            response = session.get(url)
            if response.status_code != 200:
                print(f"Error fetching data from {url}: {response.status_code}")
                continue
                
            data = response.json()
            
            for block_key, block_data in data.get('data', {}).items():
                if isinstance(block_data, dict) and 'properties' in block_data:
                    properties = block_data['properties']
                    
                    for prop in properties:
                        try:
                            house = House(
                                house_id=prop['id'],
                                sq_meters=prop['sq_meters'],
                                price=prop['price'],
                                geography=prop['geography'],
                                floorNumber=prop['floorNumber'],
                                rooms=prop['rooms'],
                                no_of_bathrooms=prop['no_of_bathrooms'],
                                kitchens=prop['kitchens'],
                                livingRooms=prop['livingRooms']
                            )
                            all_houses.append(house)
                        except Exception as e:
                            print(f"Error processing property: {e}")
            
            time.sleep(1)
            
        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
    
    return all_houses

def save_houses_to_file(houses: List[House], filename: str = "houses_data.txt"):
    """Save the list of houses to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        for house in houses:
            f.write(f"{house.model_dump_json()}\n")
    print(f"Saved {len(houses)} houses to {filename}")

def main():
    session = new_session()
    houses = fetch_properties(session)
    print(f"Found {len(houses)} houses")
    
    for i, house in enumerate(houses[:5]):
        print(f"House {i+1}:")
        print(house)
        print()
    
    save_houses_to_file(houses)

if __name__ == "__main__":
    main()
