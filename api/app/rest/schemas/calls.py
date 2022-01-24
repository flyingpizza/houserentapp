from pydantic import BaseModel, validator, Field
from typing import Dict, FrozenSet, List

class Call(BaseModel):
    """    
    call model
    """
    id: int = Field(None, description="The id of the row in the data")
    age: int = Field(None, description="The age of the user.", gt=0, lt=120)
    
    class Config:
        orm_mode=True
        anystr_strip_whitespace = True
        use_enum_values = True
        
class HousePredictionResult(BaseModel):
    median_house_value: int
    currency: str = "USD"
    
class HousePredictionPayload(BaseModel):
    median_income_in_block: float
    median_house_age_in_block: int
    average_rooms: int
    average_bedrooms: int
    population_per_block: int
    average_house_occupancy: int
    block_latitude: float
    block_longitude: float
    
def payload_to_list(hpp: HousePredictionPayload) -> List:
    return [
        hpp.median_income_in_block,
        hpp.median_house_age_in_block,
        hpp.average_rooms,
        hpp.average_bedrooms,
        hpp.population_per_block,
        hpp.average_house_occupancy,
        hpp.block_latitude,
        hpp.block_longitude]

    