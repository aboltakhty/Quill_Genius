# 🧠 Quill Genius Chat - Documentation

This documentation explains the purpose of the Quill Genius Chat application, how to set it up, and how to configure the necessary environment variables and prompt templates.

## 🚀 Purpose
The **Quill Genius Chat** is a Streamlit-based application that interacts with OpenAI's GPT models using LangChain. It provides two modes of interaction:

1. **Prompt 1 (No Memory)**: Responds to user queries without considering past interactions.
2. **Prompt 2 (With Memory)**: Maintains a conversation by remembering chat history.

This setup is ideal for applications requiring both standalone Q&A functionality and context-aware conversations.

---

## 🛠️ Installation Guide

Follow these steps to install and run the application:

### 1️⃣ **Clone the Repository**
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2️⃣ **Install Required Packages**
```bash
pip install streamlit langchain_openai python-dotenv
```

### 3️⃣ **Setup Environment Variables**
Create a `.env` file in the root directory with the following content:

```bash
OPENAI_API_KEY=your_api_key_here
```

> **Note:** Replace `your_api_key_here` with your actual OpenAI API key.

### 4️⃣ **Folder Structure**
Ensure you have a `template` folder with the following structure:

```
template/
    ├── model_auditing_template.py
    └── qa_template.py
```

### 5️⃣ **Prompt Templates**

#### **model_auditing_template.py**
```python
template = """
Chat History:
{chat_history}
User Question:
{question}

Response:
"""
```

#### **qa_template.py**
```python
template = """
Question:
{question}

Answer:
"""
```

---

## 🏃‍♂️ Run the Application
To start the Streamlit app, run the following command:

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. **Environment Setup:** Loads the OpenAI API key from `.env`.
2. **Model Initialization:** Uses `ChatOpenAI` with the specified model.
3. **Memory Management:** `ConversationBufferMemory` tracks chat history.
4. **Dynamic Prompt Selection:**
    - **Prompt 1:** Uses `qa_template` without memory.
    - **Prompt 2:** Uses `model_auditing_template` with memory.
5. **Interactive UI:** Streamlit interface for user interactions.

---

## ⚠️ Troubleshooting

- **Missing API Key:** Ensure `.env` is correctly set.
- **Prompt Issues:** Verify templates in the `template` folder.
- **Package Errors:** Run `pip install -r requirements.txt` if needed.

Happy chatting! 😊

