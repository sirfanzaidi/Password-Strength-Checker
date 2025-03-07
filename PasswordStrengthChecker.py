import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker by Irfan Zaidi", page_icon="🌒", layout="centered")

# Custom CSS for Center Alignment
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput > div > div > input {width: 60% !important; margin: auto; text-align: center;}
        .stButton {display: flex; justify-content: center;}
        .stButton button {width: 50%; background-color: #CAF50; color: white; font-size: 18px;}
        .stButton button:hover {background-color: #45a049;}
    </style>
""", unsafe_allow_html=True)

# Page Title and Description
st.markdown("<h1 style='text-align: center;'>🔓 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your password below to check its security level. 🔍</p>", unsafe_allow_html=True)

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%&*)**.")

    # Display password strength results
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)  # Center Results
    if score == 4:
        st.success("✔️ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")
        
        # Feedback
        if feedback:
            with st.expander("🔍 **Improve Your Password**"):
                for item in feedback:
                    st.write(item)
    st.markdown("</div>", unsafe_allow_html=True)  # Close Centering Div

# Input field (Centered)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔓")

# Button (Centered)
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
