from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present.
   - Explain the mathematics using simple code snippets whenever possible.

2. Analogies:
   - Use relatable analogies.

If certain information is unavailable, respond with:
"Insufficient information available."

Ensure the summary is clear and accurate.
""",
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ]
)

template.save('template.json')