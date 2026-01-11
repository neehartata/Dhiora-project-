from pydantic import BaseModel

class Details(BaseModel):
    legacy_id:int
    name: str
    age : int 
    aadhar : int
    card_type : str
    status : str

