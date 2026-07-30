# TO CREATE DYNAMIC TEMPLATE

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

# chat_template=ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple terms what is {topic}')
# ])

# this does not work so we use different method as langchain is not a matured library

chat_template=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms what is {topic}')
])

prompt=chat_template.invoke({'domain':'Cricket','topic':'LBW'})

print(prompt)