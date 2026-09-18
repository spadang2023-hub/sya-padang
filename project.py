import streamlit as st
import html

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Student Hub",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DARK THEME + ANIMATIONS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(99,102,241,.18), transparent 30%),
            radial-gradient(circle at 90% 20%, rgba(168,85,247,.15), transparent 30%),
            radial-gradient(circle at 50% 100%, rgba(236,72,153,.10), transparent 35%),
            linear-gradient(135deg, #030712, #0b1020, #111827);
        color: #f8fafc;
    }

    .main {
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    section[data-testid="stSidebar"] {
        background: #050816;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
    }

    p, label {
        color: #dbeafe !important;
    }

    .hero {
        padding: 38px 25px;
        border-radius: 28px;
        text-align: center;
        margin-bottom: 30px;
        background: linear-gradient(-45deg, #312e81, #581c87, #831843, #1e1b4b);
        background-size: 400% 400%;
        animation: gradientMove 8s ease infinite, heroFloat 4s ease-in-out infinite;
        color: white;
        box-shadow: 0 20px 50px rgba(99,102,241,.35);
    }

    .hero h1 {
        margin: 0;
        color: white !important;
        font-size: 3rem;
        font-weight: 800;
        animation: titlePop 1s ease;
    }

    .hero p {
        color: white !important;
        font-size: 1.1rem;
        opacity: .9;
        animation: fadeIn 1.5s ease;
    }

    div.stButton > button {
        border-radius: 14px;
        font-weight: 700;
        min-height: 2.8rem;
        background: linear-gradient(135deg, #1e293b, #312e81);
        color: white;
        border: 1px solid rgba(129,140,248,.30);
        transition: transform .2s ease, box-shadow .2s ease, background .2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        background: linear-gradient(135deg, #312e81, #7e22ce);
        color: white;
        box-shadow: 0 10px 30px rgba(99,102,241,.40);
    }

    div.stButton > button:active {
        transform: scale(.95);
    }

    div[data-baseweb="input"] {
        background: #111827 !important;
        border-radius: 12px;
        border: 1px solid rgba(148,163,184,.20);
        transition: transform .2s ease, box-shadow .2s ease;
    }

    div[data-baseweb="input"]:focus-within {
        transform: translateY(-2px);
        box-shadow: 0 0 0 2px rgba(99,102,241,.35), 0 8px 20px rgba(99,102,241,.15);
    }

    input, textarea {
        color: white !important;
        background: transparent !important;
    }

    div[data-baseweb="select"] {
        background: #111827 !important;
        border-radius: 12px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15,23,42,.80);
        border-radius: 20px !important;
        border: 1px solid rgba(148,163,184,.15);
        transition: transform .25s ease, box-shadow .25s ease;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,.40);
    }

    .calculator-display {
        background: linear-gradient(135deg, #020617, #111827, #1e1b4b);
        background-size: 200% 200%;
        animation: displayGradient 5s ease infinite;
        color: #ffffff;
        padding: 22px;
        border-radius: 20px;
        text-align: right;
        font-size: 42px;
        font-family: "Courier New", monospace;
        margin: 15px 0 20px 0;
        min-height: 55px;
        overflow: hidden;
        border: 1px solid rgba(129,140,248,.25);
        box-shadow: 0 12px 35px rgba(0,0,0,.45);
    }

    .subject-card, .quiz-card {
        padding: 20px;
        margin: 12px 0;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(15,23,42,.95), rgba(30,27,75,.85));
        border: 1px solid rgba(129,140,248,.18);
        box-shadow: 0 8px 25px rgba(0,0,0,.25);
        animation: fadeUp .7s ease;
    }

    .result-card {
        padding: 25px;
        border-radius: 22px;
        text-align: center;
        background: linear-gradient(135deg, rgba(49,46,129,.70), rgba(88,28,135,.70));
        border: 1px solid rgba(167,139,250,.30);
        box-shadow: 0 12px 40px rgba(76,29,149,.30);
        animation: titlePop .8s ease;
    }

    .quiz-question-card {
        padding: 25px;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(30,41,59,.95), rgba(49,46,129,.85));
        border: 1px solid rgba(129,140,248,.3);
        box-shadow: 0 15px 40px rgba(0,0,0,.35);
        animation: slideIn .6s ease;
    }

    .quiz-choice {
        padding: 14px 18px;
        margin: 8px 0;
        border-radius: 14px;
        background: rgba(15,23,42,.85);
        border: 1px solid rgba(129,140,248,.18);
        animation: fadeUp .5s ease;
    }

    .quiz-progress {
        height: 10px;
        border-radius: 20px;
        background: #1e293b;
        overflow: hidden;
        margin: 10px 0 20px 0;
    }

    .quiz-progress-inner {
        height: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
        animation: progressGlow 2s ease infinite;
    }

    hr {
        border-color: rgba(148,163,184,.15);
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes displayGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes heroFloat {
        0% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0); }
    }

    @keyframes titlePop {
        0% { opacity: 0; transform: scale(.7); }
        70% { transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes progressGlow {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.3); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <h1>🎓 Student Hub</h1>
        <p>✨ My Profile • 🧮 Calculator • 📚 Grade Calculator • 🧠 Master Quiz Maker</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# PROFILE
# ============================================================

st.header("👤 My Profile")
st.caption("✨ Tell us a little about yourself!")

with st.container(border=True):
    name = st.text_input(
        "What is your name?",
        key="profile_name",
        placeholder="Enter your name..."
    )

    age = st.number_input(
        "How old are you?",
        min_value=1,
        max_value=100,
        value=18,
        step=1,
        key="profile_age"
    )

    school = st.text_input(
        "What school do you go to?",
        key="profile_school",
        placeholder="Enter your school..."
    )

    subject = st.text_input(
        "What is your favorite subject?",
        key="profile_subject",
        placeholder="Example: Mathematics"
    )

    hobby = st.text_input(
        "What is your favorite hobby?",
        key="profile_hobby",
        placeholder="Example: Drawing"
    )

    if st.button(
        "✨ Create My Profile",
        key="profile_button",
        use_container_width=True
    ):
        if (
            name.strip()
            and school.strip()
            and subject.strip()
            and hobby.strip()
        ):
            st.success("🎉 Profile created successfully!")

            safe_name = html.escape(name)
            safe_school = html.escape(school)
            safe_subject = html.escape(subject)
            safe_hobby = html.escape(hobby)

            st.markdown(
                f"""
                <div class="subject-card">
                    <h2>👋 Hello, {safe_name}!</h2>
                    <p>🎂 I am <b>{age} years old</b>.</p>
                    <p>🏫 I go to <b>{safe_school}</b>.</p>
                    <p>📚 My favorite subject is <b>{safe_subject}</b>.</p>
                    <p>🎨 I enjoy <b>{safe_hobby}</b>.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.balloons()
        else:
            st.warning("⚠️ Please fill in all the fields first!")

# ============================================================
# CALCULATOR
# ============================================================

st.divider()
st.header("🧮 Calculator")
st.caption("Try it! Example: 5 × 4 = 20")

if "calculator" not in st.session_state:
    st.session_state.calculator = ""

if "stored_number" not in st.session_state:
    st.session_state.stored_number = None

if "current_operator" not in st.session_state:
    st.session_state.current_operator = None

if "start_new_number" not in st.session_state:
    st.session_state.start_new_number = False

if "calculator_finished" not in st.session_state:
    st.session_state.calculator_finished = False


def number_click(number):
    if (
        st.session_state.calculator == "Error"
        or st.session_state.calculator_finished
    ):
        st.session_state.calculator = ""
        st.session_state.stored_number = None
        st.session_state.current_operator = None
        st.session_state.start_new_number = False
        st.session_state.calculator_finished = False

    if st.session_state.start_new_number:
        st.session_state.calculator = ""
        st.session_state.start_new_number = False

    if (
        st.session_state.calculator == "0"
        and str(number) != "0"
    ):
        st.session_state.calculator = str(number)
    else:
        st.session_state.calculator += str(number)


def decimal_click():
    if (
        st.session_state.calculator == "Error"
        or st.session_state.calculator_finished
    ):
        st.session_state.calculator = ""
        st.session_state.stored_number = None
        st.session_state.current_operator = None
        st.session_state.start_new_number = False
        st.session_state.calculator_finished = False

    if st.session_state.start_new_number:
        st.session_state.calculator = "0"
        st.session_state.start_new_number = False

    if "." not in st.session_state.calculator:
        if st.session_state.calculator == "":
            st.session_state.calculator = "0"
        st.session_state.calculator += "."


def calculate_values(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError
        return first_number / second_number
    raise ValueError


def equals_click():
    if (
        st.session_state.stored_number is None
        or st.session_state.current_operator is None
        or st.session_state.calculator in ("", "Error")
        or st.session_state.start_new_number
    ):
        return

    try:
        first_number = float(st.session_state.stored_number)
        second_number = float(st.session_state.calculator)
        operator = st.session_state.current_operator

        answer = calculate_values(
            first_number,
            second_number,
            operator
        )

        if answer == int(answer):
            st.session_state.calculator = str(int(answer))
        else:
            st.session_state.calculator = str(round(answer, 10))

        st.session_state.stored_number = None
        st.session_state.current_operator = None
        st.session_state.start_new_number = False
        st.session_state.calculator_finished = True

    except (ValueError, TypeError, ZeroDivisionError):
        st.session_state.calculator = "Error"
        st.session_state.stored_number = None
        st.session_state.current_operator = None
        st.session_state.start_new_number = False
        st.session_state.calculator_finished = True


def operator_click(operator):
    if st.session_state.calculator in ("", "Error"):
        return

    try:
        # Allows chained calculations such as 5 × 4 + 2
        if (
            st.session_state.stored_number is not None
            and st.session_state.current_operator is not None
            and not st.session_state.start_new_number
        ):
            equals_click()

        st.session_state.stored_number = float(
            st.session_state.calculator
        )

        if operator == "×":
            operator = "*"
        elif operator == "÷":
            operator = "/"

        st.session_state.current_operator = operator
        st.session_state.start_new_number = True
        st.session_state.calculator_finished = False

    except (ValueError, TypeError):
        st.session_state.calculator = "Error"


def clear_click():
    st.session_state.calculator = ""
    st.session_state.stored_number = None
    st.session_state.current_operator = None
    st.session_state.start_new_number = False
    st.session_state.calculator_finished = False


def backspace_click():
    if st.session_state.calculator not in ("", "Error"):
        st.session_state.calculator = st.session_state.calculator[:-1]

    if st.session_state.calculator == "-":
        st.session_state.calculator = ""


display = st.session_state.calculator
if display == "":
    display = "0"

st.markdown(
    f"""
    <div class="calculator-display">{html.escape(display)}</div>
    """,
    unsafe_allow_html=True
)

# Calculator buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", key="num7", on_click=number_click, args=("7",), use_container_width=True)
with col2:
    st.button("8", key="num8", on_click=number_click, args=("8",), use_container_width=True)
with col3:
    st.button("9", key="num9", on_click=number_click, args=("9",), use_container_width=True)
with col4:
    st.button("÷", key="divide", on_click=operator_click, args=("÷",), use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("4", key="num4", on_click=number_click, args=("4",), use_container_width=True)
with col2:
    st.button("5", key="num5", on_click=number_click, args=("5",), use_container_width=True)
with col3:
    st.button("6", key="num6", on_click=number_click, args=("6",), use_container_width=True)
with col4:
    st.button("×", key="multiply", on_click=operator_click, args=("×",), use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("1", key="num1", on_click=number_click, args=("1",), use_container_width=True)
with col2:
    st.button("2", key="num2", on_click=number_click, args=("2",), use_container_width=True)
with col3:
    st.button("3", key="num3", on_click=number_click, args=("3",), use_container_width=True)
with col4:
    st.button("-", key="minus", on_click=operator_click, args=("-",), use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("0", key="num0", on_click=number_click, args=("0",), use_container_width=True)
with col2:
    st.button(".", key="decimal", on_click=decimal_click, use_container_width=True)
with col3:
    st.button("=", key="equals", on_click=equals_click, use_container_width=True)
with col4:
    st.button("+", key="plus", on_click=operator_click, args=("+",), use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.button("⌫ BACKSPACE", key="backspace", on_click=backspace_click, use_container_width=True)

with col2:
    st.button("🗑️ CLEAR", key="clear", on_click=clear_click, use_container_width=True)

# ============================================================
# GRADE CALCULATOR
# ============================================================

st.divider()
st.header("🎓 Grade Calculator")
st.caption("📚 Enter your subjects and marks from 0 to 100.")

number_of_subjects = st.number_input(
    "📚 How many subjects do you have?",
    min_value=1,
    max_value=20,
    value=3,
    step=1,
    key="number_of_subjects"
)

st.subheader("📝 Enter Your Subjects")

subjects = []

for i in range(int(number_of_subjects)):
    st.markdown(
        f"""
        <div class="subject-card">
            <h3>📖 Subject {i + 1}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        subject_name = st.text_input(
            f"Subject {i + 1} Name",
            key=f"subject_name_{i}",
            placeholder="Example: Mathematics"
        )

    with col2:
        mark = st.number_input(
            f"Subject {i + 1} Mark",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=1.0,
            key=f"subject_mark_{i}"
        )

    subjects.append({
        "name": subject_name.strip(),
        "mark": float(mark)
    })


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    return "F"


def get_gpa(mark):
    if mark >= 90:
        return 4.0
    elif mark >= 70:
        return 3.0
    elif mark >= 60:
        return 2.0
    return 0.0


if st.button(
    "🎯 Calculate My Grade",
    key="calculate_grade",
    use_container_width=True
):
    all_subjects_named = all(
        subject["name"].strip() != ""
        for subject in subjects
    )

    if not all_subjects_named:
        st.warning("⚠️ Please enter a name for every subject.")
    else:
        total_marks = sum(
            subject["mark"] for subject in subjects
        )

        maximum_marks = len(subjects) * 100
        percentage = (total_marks / maximum_marks) * 100

        total_gpa = sum(
            get_gpa(subject["mark"]) for subject in subjects
        )

        overall_gpa = total_gpa / len(subjects)
        overall_grade = get_grade(percentage)

        if percentage >= 90:
            performance = "🌟 Excellent Performance!"
        elif percentage >= 70:
            performance = "🎉 Great Performance!"
        elif percentage >= 60:
            performance = "👍 Good Performance!"
        else:
            performance = "💪 Keep Practicing!"

        st.divider()
        st.subheader("📊 Your Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📊 Total Marks",
                f"{total_marks:.0f} / {maximum_marks}"
            )

        with col2:
            st.metric(
                "📈 Percentage",
                f"{percentage:.2f}%"
            )

        with col3:
            st.metric(
                "🎓 Overall GPA",
                f"{overall_gpa:.2f}"
            )

        st.markdown(
            f"""
            <div class="result-card">
                <h2>🏆 Overall Result</h2>
                <h1>{overall_grade}</h1>
                <h3>{performance}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 📚 Individual Subject Results")

        for index, current_subject in enumerate(subjects):
            subject_name = html.escape(current_subject["name"])
            mark = current_subject["mark"]
            grade = get_grade(mark)
            gpa = get_gpa(mark)

            st.markdown(
                f"""
                <div class="subject-card"
                     style="animation-delay:{index * 0.12}s;">
                    <h3>📖 {subject_name}</h3>
                    <p>📝 Mark: <b>{mark:.0f} / 100</b></p>
                    <p>🎓 Grade: <b>{grade}</b></p>
                    <p>⭐ GPA: <b>{gpa:.1f}</b></p>
                </div>
                """,
                unsafe_allow_html=True
            )

        if percentage >= 90:
            st.balloons()
            st.success("🌟 Amazing! You achieved an excellent score!")
        elif percentage >= 70:
            st.success("🎉 Great job! Keep up the good work!")
        elif percentage >= 60:
            st.info("👍 Good work! Keep improving!")
        else:
            st.warning("💪 Don't give up! Keep practicing!")

st.divider()
st.subheader("📋 Grading Scale")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("**A**\n\n90–100\n\nGPA 4.0")

with col2:
    st.info("**B**\n\n70–89\n\nGPA 3.0")

with col3:
    st.info("**C**\n\n60–69\n\nGPA 2.0")

with col4:
    st.info("**F**\n\nBelow 60\n\nGPA 0.0")

# ============================================================
# MASTER QUIZ MAKER
# ============================================================

st.divider()
st.header("🧠 Master Quiz Maker")
st.caption("🎮 Create your own quiz with questions, choices, and correct answers!")

quiz_title = st.text_input(
    "🏆 Quiz Title",
    placeholder="Example: Science Quiz",
    key="quiz_title"
)

num_questions = st.number_input(
    "🔢 How many questions do you want to make?",
    min_value=1,
    max_value=50,
    value=5,
    step=1,
    key="num_questions"
)

st.info(
    f"💡 You entered {int(num_questions)} questions, "
    f"so Question 1 through Question {int(num_questions)} will appear."
)

# ============================================================
# CREATE QUESTIONS
# ============================================================

st.markdown("### ✏️ Create Your Questions")

for i in range(int(num_questions)):
    st.markdown(f"## ❓ Question {i + 1}")

    if i == 0:
        st.caption(
            "💡 Example: What is 2 + 2? "
            "A. 3   B. 4   C. 5   D. 6"
        )

    question = st.text_input(
        f"Enter Question {i + 1}",
        placeholder="Example: What is 2 + 2?",
        key=f"question_{i}"
    )

    st.markdown("### 📝 Answer Choices")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input(
            "🅰️ A",
            placeholder="Example: 3",
            key=f"option_a_{i}"
        )

        st.text_input(
            "🅱️ B",
            placeholder="Example: 4",
            key=f"option_b_{i}"
        )

    with col2:
        st.text_input(
            "©️ C",
            placeholder="Example: 5",
            key=f"option_c_{i}"
        )

        st.text_input(
            "🅳 D",
            placeholder="Example: 6",
            key=f"option_d_{i}"
        )

    st.markdown("### ✅ Select the Correct Answer")

    st.radio(
        f"Which answer is correct for Question {i + 1}?",
        ["A", "B", "C", "D"],
        horizontal=True,
        key=f"correct_answer_{i}"
    )

    st.divider()

# ============================================================
# START QUIZ
# ============================================================

if st.button(
    "🚀 Start Quiz",
    key="start_quiz",
    use_container_width=True
):
    all_questions_filled = True

    for i in range(int(num_questions)):
        question_value = st.session_state.get(
            f"question_{i}", ""
        ).strip()

        option_a_value = st.session_state.get(
            f"option_a_{i}", ""
        ).strip()

        option_b_value = st.session_state.get(
            f"option_b_{i}", ""
        ).strip()

        option_c_value = st.session_state.get(
            f"option_c_{i}", ""
        ).strip()

        option_d_value = st.session_state.get(
            f"option_d_{i}", ""
        ).strip()

        if not all([
            question_value,
            option_a_value,
            option_b_value,
            option_c_value,
            option_d_value
        ]):
            all_questions_filled = False
            break

    if not quiz_title.strip():
        st.error("⚠️ Please enter a quiz title.")
    elif not all_questions_filled:
        st.error(
            "⚠️ Please fill in every question and all A, B, C, and D choices."
        )
    else:
        st.session_state.quiz_started = True
        st.session_state.quiz_finished = False
        st.session_state.current_question = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_answers = {}

        st.success("🎉 Your quiz is ready!")
        st.rerun()

# ============================================================
# TAKE QUIZ
# ============================================================

if st.session_state.get("quiz_started", False):

    st.divider()

    if st.session_state.get("quiz_finished", False):
        # ----------------------------------------------------
        # FINAL RESULTS
        # ----------------------------------------------------

        score = st.session_state.get("quiz_score", 0)
        total = int(num_questions)
        percentage = (score / total) * 100

        st.markdown(
            f"""
            <div class="result-card">
                <h1>🏆 Quiz Complete!</h1>
                <h2>{html.escape(quiz_title)}</h2>
                <h1>⭐ {score} / {total}</h1>
                <h2>{percentage:.0f}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        if percentage >= 90:
            st.balloons()
            st.success("🌟 Outstanding! You are a quiz master!")
        elif percentage >= 70:
            st.success("🎉 Great job! You did really well!")
        elif percentage >= 60:
            st.info("👍 Good work! Keep practicing!")
        else:
            st.warning("💪 Keep practicing and try again!")

        if st.button(
            "🔄 Create Another Quiz",
            key="new_quiz",
            use_container_width=True
        ):
            st.session_state.quiz_started = False
            st.session_state.quiz_finished = False
            st.session_state.current_question = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answers = {}
            st.rerun()

    else:
        current = st.session_state.get("current_question", 0)
        total = int(num_questions)

        # Progress
        progress = ((current + 1) / total) * 100

        st.markdown(
            f"""
            <div class="quiz-progress">
                <div class="quiz-progress-inner"
                     style="width:{progress}%;">
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            f"**Question {current + 1} of {total}**"
        )

        question_text = st.session_state.get(
            f"question_{current}", ""
        )

        option_a = st.session_state.get(
            f"option_a_{current}", ""
        )

        option_b = st.session_state.get(
            f"option_b_{current}", ""
        )

        option_c = st.session_state.get(
            f"option_c_{current}", ""
        )

        option_d = st.session_state.get(
            f"option_d_{current}", ""
        )

        st.markdown(
            f"""
            <div class="quiz-question-card">
                <h2>❓ {html.escape(question_text)}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### 📝 Choose your answer")

        # The user sees A/B/C/D and clicks a button.
        answer_columns = st.columns(2)

        answer_options = {
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d
        }

        selected_answer = st.session_state.quiz_answers.get(
            current
        )

        for index, letter in enumerate(["A", "B", "C", "D"]):
            with answer_columns[index % 2]:
                button_text = (
                    f"🅰️  {answer_options[letter]}"
                    if letter == "A"
                    else
                    f"🅱️  {answer_options[letter]}"
                    if letter == "B"
                    else
                    f"©️  {answer_options[letter]}"
                    if letter == "C"
                    else
                    f"🅳  {answer_options[letter]}"
                )

                if st.button(
                    button_text,
                    key=f"quiz_choice_{current}_{letter}",
                    use_container_width=True
                ):
                    st.session_state.quiz_answers[current] = letter
                    st.rerun()

        selected_answer = st.session_state.quiz_answers.get(current)

        if selected_answer:
            st.success(
                f"✨ You selected **{selected_answer}**"
            )

            if current < total - 1:
                if st.button(
                    "➡️ Next Question",
                    key=f"next_question_{current}",
                    use_container_width=True
                ):
                    st.session_state.current_question += 1
                    st.rerun()

            else:
                if st.button(
                    "🏁 Finish Quiz",
                    key="finish_quiz",
                    use_container_width=True
                ):
                    score = 0

                    for question_number in range(total):
                        user_answer = st.session_state.quiz_answers.get(
                            question_number
                        )

                        correct_answer = st.session_state.get(
                            f"correct_answer_{question_number}",
                            ""
                        )

                        if user_answer == correct_answer:
                            score += 1

                    st.session_state.quiz_score = score
                    st.session_state.quiz_finished = True
                    st.rerun()
        else:
            st.info("👆 Click one of the four answers to continue.")

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        padding:25px;
        opacity:.75;
        animation:fadeIn 2s ease;
    ">
        <h3>🎓 Student Hub</h3>
        <p>✨ Profile • 🧮 Calculator • 📚 Grades • 🧠 Quizzes</p>
        <p>Made with Python & Streamlit 💜</p>
    </div>
    """,
    unsafe_allow_html=True
)
