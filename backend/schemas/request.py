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
