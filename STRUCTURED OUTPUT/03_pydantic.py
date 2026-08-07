from pydantic import BaseModel
from typing import Optional

class student(BaseModel):
    name:str
    age:Optional[int]=None
    

new_student={'name':'Ram','age':22}

student=student(**new_student)

print(student)