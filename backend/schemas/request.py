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

from pydantic import BaseModel, Field

class HouseFeatures(BaseModel):
    sq_meters: float = Field(..., gt=0, description="Surface area in square meters (must be positive)")
    geography: str = Field(..., min_length=1, description="Geographical area/city/neighborhood")
    floorNumber: int = Field(...,  description="Floor Number")
    rooms: int = Field(..., ge=0, description="Number of rooms (non-negative)")
    no_of_bathrooms: int = Field(..., ge=0, description="Number of bathrooms (non-negative)")
    kitchens: int = Field(..., ge=0, description="Number of kitchens (non-negative)")
    livingRooms: int = Field(..., ge=0, description="Number of living rooms (non-negative)")

    class Config:
        json_schema_extra = {
            "example": {
                "sq_meters": 100.0,
                "geography": "Gkrava (Athens - Center)",
                "floorNumber": 4,
                "rooms": 3,
                "no_of_bathrooms": 2,
                "kitchens": 1,
                "livingRooms": 1
            }
        }
