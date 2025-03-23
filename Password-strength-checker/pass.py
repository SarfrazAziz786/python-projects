import streamlit as st
import re #regular expression library (captital letter , small letter, digit, special character)

st.set_page_config(page_title="Password Checker", page_icon="🔒")

st.title("🔒Password Checker")

st.markdown("""
            ## Welcome to the Password strength Checker App!
             Use this simple tool to check password strength
            we will give you helpful tips to make your  **password stronger**.""")


password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters")

    if re.search(r"\d", password):  # \d is a special character for any digit (0-9) 
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit")

    if re.search(r"[!@#$%*]", password):  #  OR \W is a special character for any non-word character
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character (!@#$%*)")

    if score == 4:
        feedback.append("✅Your password is strong")
    elif score == 3:
        feedback.append("🟡Your password is medium") 
    else:
        feedback.append("🔴Your password is weak. Please make it stronger")

    if feedback:
        st.markdown("### Improvement Suggestions:")
    for tip in feedback:
        st.write(tip)

else:
    st.info("Please enter your password")