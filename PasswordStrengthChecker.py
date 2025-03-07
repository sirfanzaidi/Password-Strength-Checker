import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker by Irfan Zaidi", page_icon="🌒", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: #CAF50; color: white; font-size: 18px;}
    .stButton button:hover { background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🔓 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  # Increase score by 1
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

# Input field (Placed outside the function)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔓")

# Button to Check Password Strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
