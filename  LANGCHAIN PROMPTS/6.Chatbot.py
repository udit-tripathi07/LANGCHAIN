from langchain_ollama import  ChatOllama
from langchain_core.messages import SystemMessage, AIMessage,HumanMessage
model=ChatOllama(model="llama3.1:latest")

chat_history=[
    SystemMessage(content='You are a helpful professor')
] 
while True:
    user_input=input("YOU: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input== 'exit':
        print(chat_history) # show chat_history after the end of session
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

# since here the system message and human messages are static so now we study how can we send the 
# list of msg in dynamic manner with the help of CAHT PROMPT TEMPLATE