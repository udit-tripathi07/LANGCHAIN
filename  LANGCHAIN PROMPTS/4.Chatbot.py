from langchain_ollama import  ChatOllama

model=ChatOllama(model="llama3.1:latest")

chat_history=[] # to save history so that we can do Q/A
while True:
    user_input=input("YOU: ")
    chat_history.append(user_input)
    if user_input== 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)

# since the chat_history become large after some msg so the AI finds it difficult
# to understand which is user msg and which is AI's so we use the concept of 
# SystemMessage,AImessage and HumanMessage which is in file 6.Chatbot.py