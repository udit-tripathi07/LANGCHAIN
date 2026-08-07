from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated

model=ChatOllama(model="llama3.1:latest")

class Review(TypedDict):

    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return sentiment of the reviw positive,negative or neutral"]

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""I was really excited to buy this smartphone because the design is sleek, the display is vibrant, and the camera takes stunning photos. For the first few days, everything worked perfectly, and I genuinely thought it was the best phone I had ever owned. Unfortunately, after only a week, the battery started draining unusually fast, the phone began overheating during simple tasks, and several apps crashed repeatedly. Although I still appreciate the premium build quality and excellent camera, the poor battery life and unstable performance have made the overall experience frustrating. I hope a future software update fixes these issues because I truly want to enjoy using this device.""")

print(result)