from pydantic import BaseModel, Field
from typing import Optional
class Item(BaseModel):
    name:str
    price:float
    description:str = None # Optionnal
    
class User(BaseModel):
    name:str
    age:int
    email:Optional[str] = None
    
class UserWithValidation(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    
class Adress(BaseModel):
    street:str
    city:str
    country:str
    
class UserWithAdress(BaseModel):
    name:str
    adress: Adress
    
class UserList(BaseModel):
    users : list[User]
    total : int
    
