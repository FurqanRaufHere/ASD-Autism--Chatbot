# import streamlit as st
# from chatbot import generate_answer

# # Streamlit page config
# st.set_page_config(
#     page_title="ASD Chatbot",
#     page_icon="🧠",
#     layout="centered"
# )

# # App title
# st.markdown("<h1 style='text-align: center; color: #4B0082;'>ASD Chatbot 🤖</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center;'>An AI assistant for Autism Spectrum Disorder – powered by Gemini Flash & FAISS</p>", unsafe_allow_html=True)
# st.markdown("---")

# # Text input
# user_query = st.text_input("Ask something about Autism Spectrum Disorder:", placeholder="E.g., What are the symptoms of ASD?")

# # Ask button
# if user_query:
#     with st.spinner("Thinking... 🤔"):
#         response = generate_answer(user_query)
#     st.markdown("### 💬 Chatbot Response")
#     st.markdown(f"<div style='background-color: #f0f8ff; padding: 15px; border-radius: 10px;'>{response}</div>", unsafe_allow_html=True)




import streamlit as st
from chatbot import generate_answer

# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="ASD Chatbot",
    page_icon="🧠",
    layout="centered"
)


# ---------------- Sidebar ---------------- #
with st.sidebar:
    st.title("📖 Guide & FAQs")
    st.markdown("Welcome to the **ASD Chatbot Assistant** 👋")
    
    st.markdown("### 🧾 How to Use")
    st.markdown("""
    - Type any question related to Autism Spectrum Disorder (ASD).
    - The chatbot will provide an informative, evidence-based, and caring response.
    """)
    
    st.markdown("### ❓ Frequently Asked Questions")
    st.markdown("""
    - **Q:** What kind of questions can I ask?  
      **A:** Anything related to ASD – symptoms, diagnosis, therapies, causes, etc.

    - **Q:** Where is the information coming from?  
      **A:** From curated documents embedded using FAISS and generated with Gemini Flash 2.0.

    - **Q:** Can it give medical advice?  
      **A:** No. It provides educational information, not a substitute for professional medical advice.

    - **Q:** Is my data private?  
      **A:** Yes, we don’t store or track personal queries.
    """)

    st.markdown("---")
    st.markdown("💡 *Tip: Be specific in your questions to get better responses.*")


    # ---------------- Initialize Chat History ---------------- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ----------------- Page Title ----------------- #
st.markdown("<h1 style='text-align: center; color: #4B0082;'>ASD Chatbot 🤖</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>"
    "An AI assistant for Autism Spectrum Disorder – powered by Gemini Flash & FAISS"
    "</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# ----------------- User Query Section ----------------- #
st.markdown("## Ask a Question")
st.markdown("Enter your query related to Autism Spectrum Disorder below:")

# Input Field
user_query = st.text_input(
    label="",
    placeholder="E.g., What are early signs of autism in toddlers?",
    label_visibility="collapsed"
)

# ----------------- Chat Response ----------------- #
if user_query:
    with st.spinner("Thinking... 🤔"):
        response = generate_answer(user_query)

    st.markdown("### 💬 Chatbot Response")
    st.markdown(
        f"<div style='background-color: #f0f8ff; padding: 15px; border-radius: 10px;'>"
        f"{response}</div>",
        unsafe_allow_html=True
    )

# ---------------- Display Chat History ---------------- #
if st.session_state.chat_history:
    st.markdown("### 🗂️ Previous Chat History")
    for i, (query, reply) in enumerate(reversed(st.session_state.chat_history), 1):
        st.markdown(f"**You:** {query}")
        st.markdown(
            f"<div style='background-color: #f0f8ff; padding: 15px; border-radius: 10px;'>{reply}</div>",
            unsafe_allow_html=True
        )
        st.markdown("---")


# ----------------- Footer ----------------- #
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>"
    "Developed with ❤️ to support ASD awareness and education."
    "</p>",
    unsafe_allow_html=True
)
