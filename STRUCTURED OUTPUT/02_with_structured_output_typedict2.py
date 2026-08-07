from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated

model=ChatOllama(model="llama3.1:latest")

class Review(TypedDict):

    summary:Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Return sentiment of the reviw positive,negative or neutral"]
    pros:Annotated[list[str],"Write down all the pros inside a list"]
    cons:Annotated[list[str],"Write down all the cons inside a list"]

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""I have been using this laptop for about three weeks, and my experience has been a mix of pleasant surprises and frustrating issues. On the positive side, the build quality feels premium, the keyboard is comfortable for long typing sessions, and the display is bright with excellent color accuracy, making it perfect for both work and watching movies. The performance is also impressive—I can run multiple applications simultaneously without noticing any lag, and the battery easily lasts an entire workday. However, the laptop isn't without its flaws. The cooling system becomes quite noisy under heavy workloads, and the device gets noticeably warm during gaming or video editing. I was also disappointed by the average webcam quality, which makes video calls look grainy in low light. While the speakers are clear, they lack the bass and volume I expected at this price. Overall, I genuinely enjoy using this laptop because its strengths outweigh its weaknesses, but I do wish the manufacturer had paid more attention to the thermal management and multimedia experience. I would still recommend it to students and professionals who prioritize performance and battery life over gaming or high-quality audio.""")

print(result)