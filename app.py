import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

from langchain.schema.runnable import RunnableLambda

from dotenv import load_dotenv
import os

import template
import template.model_auditing_template
import template.qa_template

# Load environment variables
load_dotenv()
model_name = "gpt-4o-mini"
# Initialize model
model = ChatOpenAI(model_name=model_name, api_key=os.getenv("OPENAI_API_KEY"))

# Initialize memory for chat history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define prompt templates
prompt_qa = PromptTemplate(
    input_variables=["question"],
    template=template.qa_template.template
)

prompt_model_auditing = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=template.model_auditing_template.template
)

# Streamlit interface
st.title("🧠 Quill Genius Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

elif st.button("Remove chat history"):
    st.session_state.chat_history = []

# Select prompt type
prompt_type = st.radio("Choose prompt type:", ("Prompt 1 (No Memory)", "Prompt 2 (With Memory)"))

# User input
question = st.text_area("Ask a question:")

if st.button("Get Answer") and question:
    if prompt_type == "Prompt 1 (No Memory)":
        # Use Prompt 1 (no memory)

        chain = RunnableLambda(lambda inputs: model.invoke(prompt_qa.format(**inputs))) 
        response = chain.invoke({"question": question})

    else:
        # Use Prompt 2 (with memory)

        chat_history = "\n".join(st.session_state.chat_history)
        chain = RunnableLambda(lambda inputs: model.invoke(prompt_model_auditing.format(**inputs)))
        response = chain.invoke({"chat_history": chat_history, "question": question})

    # Display the answer
    st.write("**Answer:**", response)

    # Update chat history for Prompt 2
    st.session_state.chat_history.append(f"Q: {question}\nA: {response.content}")
