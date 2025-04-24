import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Areeba", page_icon="🧿", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .stTextInput {
            border: 2px solid #4CAF50;
            padding: 10px;
            border-radius: 5px;
        }
        .password-strength {
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        remarks = "✅ Strong Password!"
        color = "green"
    elif score == 3:
        remarks = "⚠️ Moderate Password - Consider adding more security features."
        color = "orange"
    else:
        remarks = "❌ Weak Password - Improve it using the suggestions above."
        color = "red"
    
    return score, remarks, color, feedback

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    score, remarks, color, feedback = check_password_strength(password)
    
    st.markdown(f'<p class="password-strength" style="color: {color};">{remarks}</p>', unsafe_allow_html=True)
    
    for tip in feedback:
        st.markdown(f'<p style="color: red;">{tip}</p>', unsafe_allow_html=True)
    
    st.progress(score / 4)
