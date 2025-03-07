import re
import streamlit as st


#page Styling
st.set_page_config(page_title="Password Strength Checker by Irfan Zaidi", page_icon="🌒", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color #CAF50; color: white; font-size: 18px;}
    .stBUtton button:hover { background-color: # 45a049;}
</style>
     
""", unsafe_allow_html=True)

#page title and description
st.title("🔓 Password Strength Generator ")
st.write("Enter your password below to check its security level. 🔍")

# function to check password strenght

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌password should be **atleast 8 character long**")

    if re.search(r"[A-Z]", password) and re.research(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌password should include **both upper case (A-Z) and lowercase (a-z) letters **.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌password should include **at least one number (0-9) **.")

    # special charactor
    if re.search(r"[!@#$%&*]", password):
        score += 1
        feedback.append("❌Include **at least one character (!@#$%&*) **.")

    # display password strength results

    if score == 4:
        st.success("✔️ ""Strong Password"" - your password is secure.")
    elif score == 3 :
        st.info("⚠️ ** Moderate password** - Consider Improving security by adding more features")
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it.")

        #feedback
        if feedback:
            with st.expander("🔍 **Improve your Password**"):
                for item in feedback:
                    st.write(item)
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔓")

    #Button Working
    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password  first!")
