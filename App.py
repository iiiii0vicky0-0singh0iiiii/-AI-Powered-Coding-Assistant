import streamlit as st
from streamlit_ace import st_ace
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

#  Setup Page Config
st.set_page_config(page_title="AI Code Assistant", layout="wide")

st.title("🚀 AI-Powered Code Assistant")
st.markdown("### Your personal Google-style coding companion")

#  Sidebar for API Key (Secure handling)
# Try to get key from environment, otherwise ask user
api_key = os.getenv("OPENAI_API_KEY")

with st.sidebar:
    st.header("⚙️ Settings")
    if not api_key:
        api_key = st.text_input("Enter OpenAI API Key", type="password")
    
    model_choice = st.selectbox("Select Model", ["gpt-4-turbo", "gpt-3.5-turbo", "gpt-4o"])
    language = st.selectbox("Programming Language", ["python", "javascript", "html", "css", "sql", "java"])
    st.info("💡 Tip: Use 'Ctrl+Enter' in the editor to apply changes.")

# Initialize OpenAI Client
client = None
if api_key:
    client = OpenAI(api_key=api_key)
else:
    st.warning("⚠️ Please provide an OpenAI API Key in the sidebar to proceed.")
    st.stop()

# Helper Function to Call AI 
def get_ai_response(system_prompt, user_prompt):
    try:
        response = client.chat.completions.create(
            model=model_choice,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Main App Layout 
tab1, tab2, tab3 = st.tabs(["✨ Auto-Complete / Generate", "🧐 Explain Code", "🐛 Debug & Fix"])

# TAB 1: CODE GENERATION (The "Google Code Assistance" feature)
with tab1:
    st.subheader("Describe what you want to build")
    user_instruction = st.text_area("Ex: 'Write a Python script to scrape a website using BeautifulSoup'", height=100)
    
    if st.button("Generate Code"):
        if user_instruction:
            with st.spinner("🤖 Writing code for you..."):
                prompt = f"Write clean, commented {language} code for the following task. Do not include markdown backticks (```). Just the raw code:\n\n{user_instruction}"
                generated_code = get_ai_response("You are an expert coding assistant.", prompt)
                
                if generated_code:
                    st.session_state['generated_code'] = generated_code
                    st.success("Code Generated!")
        else:
            st.warning("Please describe what code you want.")

    # Display the editor with the generated code (or empty)
    initial_code = st.session_state.get('generated_code', "# Your generated code will appear here")
    
    code_editor_gen = st_ace(
        value=initial_code,
        language=language,
        theme="monokai",
        height=400,
        key="editor_gen"
    )

# TAB 2: EXPLAIN CODE
with tab2:
    st.subheader("Paste code to understand it")
    
    code_to_explain = st_ace(
        placeholder="Paste complex code here...",
        language=language,
        theme="monokai",
        height=300,
        key="editor_explain"
    )
    
    if st.button("Explain This Code"):
        if code_to_explain:
            with st.spinner("Analyzing..."):
                explanation = get_ai_response(
                    "You are a helpful teacher. Explain the code step-by-step in simple terms.", 
                    f"Explain this {language} code:\n\n{code_to_explain}"
                )
                st.markdown("### 💡 Explanation")
                st.write(explanation)
        else:
            st.warning("Please enter some code first.")

# TAB -> DEBUG & FIX
with tab3:
    st.subheader("Find bugs and get fixes")
    
    buggy_code = st_ace(
        placeholder="Paste buggy code here...",
        language=language,
        theme="monokai",
        height=300,
        key="editor_debug"
    )
    
    error_message = st.text_input("Optional: Paste the error message (e.g., 'IndexError: list index out of range')")

    if st.button("Debug Code"):
        if buggy_code:
            with st.spinner("Hunting for bugs..."):
                prompt = f"Fix the following {language} code. \nError Context: {error_message}\n\nCode:\n{buggy_code}\n\nProvide the fixed code and explain what was wrong."
                fix = get_ai_response("You are a senior software engineer focused on debugging.", prompt)
                st.markdown("### 🛠️ Fix & Analysis")
                st.write(fix)
        else:
            st.warning("Please provide code to debug.")
