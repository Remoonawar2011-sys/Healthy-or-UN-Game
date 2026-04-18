import streamlit as st

# عنوان اللعبة
st.title("🍎 Healthy vs Unhealthy Game")

# الأسئلة (صورة + الإجابة الصح)
questions = [
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0b/RedDot_Burger.jpg",
        "answer": "Unhealthy"
    },
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
        "answer": "Healthy"
    },
    {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/French_fries.jpg",
        "answer": "Unhealthy"
    }
]

# حفظ الحالة (مهم جدًا)
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0

# لو خلصت الأسئلة
if st.session_state.q_index >= len(questions):
    st.success(f"🎉 Game Over! Your score: {st.session_state.score}/{len(questions)}")

    if st.button("🔄 Play Again"):
        st.session_state.q_index = 0
        st.session_state.score = 0
    st.stop()

# السؤال الحالي
q = questions[st.session_state.q_index]

# عرض الصورة
st.image(q["image"], width=250)

# الاختيارات
choice = st.radio("Choose:", ["Healthy", "Unhealthy"], key=st.session_state.q_index)

# زر التأكيد
if st.button("Submit"):
    if choice == q["answer"]:
        st.success("✔ Correct!")
        st.session_state.score += 1
    else:
        st.error("❌ Wrong!")

    st.session_state.q_index += 1
    st.rerun()