#  DYNAMIC PROMPT

from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
model=ChatOllama(model="llama3.1:latest")

st.header('Research Tool')

# insted of taking prompt from user we take some preferences  from them
paper_input = st.selectbox( "Select Research Paper Name",
                            ["Attention Is All You Need", 
                             "BERT: Pre-training of Deep Bidirectional Transformers",
                            "GPT-3: Language Models are Few-Shot Learners", 
                            "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style",
                            ["Beginner-Friendly", "Technical",
                              "Code-Oriented", "Mathematical"] ) 


length_input = st.selectbox( "Select Explanation Length", 
                            ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)",
                              "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:

# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematical Details:
#    - Include relevant mathematical equations if present.
#    - Explain the mathematics using simple code snippets whenever possible.

# 2. Analogies:
#    - Use relatable analogies.

# If certain information is unavailable, respond with:
# "Insufficient information available."

# Ensure the summary is clear and accurate.
# """,
#     input_variables=[
#         "paper_input",
#         "style_input",
#         "length_input"
#     ]
# )

template=load_prompt('template.json')

if st.button('Summarize'):
     prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input

})
     
     result=model.invoke(prompt)
     st.write(result.content)
    