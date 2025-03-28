import streamlit as st

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check for a digit
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check for a special character
    special_chars = "!@#$%^&*"
    has_special = any(char in special_chars for char in password)
    if has_special:
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Determine strength level
    if score == 4:
        strength = "Strong"
        color = "green"
    elif score == 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    return score, strength, color, feedback

# Streamlit UI
st.title("Password Strength Meter")
st.write("Enter your password below to check its strength!")

password = st.text_input("Password", type="password")

if password:
    score, strength, color, feedback = check_password_strength(password)
    
    # Display strength indicator
    st.markdown(f"### Password Strength: <span style='color: {color}'>{strength}</span>", unsafe_allow_html=True)
    
    # Display score
    st.progress(score/4)
    st.write(f"Score: {score}/4")
    
    # Display feedback
    if feedback:
        st.write("### Suggestions for improvement:")
        for item in feedback:
            st.write(item) 