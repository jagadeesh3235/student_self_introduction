import streamlit as st

# Page configuration
st.set_page_config(page_title="Student Intro App", layout="centered")

# Title
st.title("🎓 Student Introduction Web App")
st.write("Generate a detailed, natural self-introduction paragraph 👇")

# Input: Student Name
name = st.text_input("👤 Student Name")

# Input: College Dropdown (NEW)
college = st.selectbox(
    "🏫 Select Your College",
    [
        "NSRIT (Nadimpalli Satyanarayana Raju Institute of Technology)",
        "IIT Bombay",
        "IIT Delhi",
        "IIT Madras",
        "NIT Trichy",
        "NIT Warangal",
        "VIT Vellore",
        "SRM University",
        "BITS Pilani",
        "Amrita University"
    ]
)

# Input: Department Dropdown
department = st.selectbox(
    "🏬 Select Your Department",
    [
        "Computer Science & Engineering (CSE)",
        "Artificial Intelligence & Data Science (AI & DS)",
        "Artificial Intelligence & Machine Learning (AI & ML)",
        "Information Technology (IT)",
        "Electronics & Communication Engineering (ECE)",
        "Electrical & Electronics Engineering (EEE)",
        "Electrical Engineering (EE)",
        "Mechanical Engineering (ME)",
        "Civil Engineering (CE)",
        "Chemical Engineering",
        "Biotechnology",
        "Aerospace Engineering",
        "Automobile Engineering",
        "Metallurgical Engineering",
        "Mining Engineering",
        "Petroleum Engineering",
        "Robotics Engineering",
        "Industrial Engineering"
    ]
)

# Input: Year Dropdown
year = st.selectbox(
    "📘 Year of Study",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# Input: Section Dropdown
section = st.selectbox(
    "🅰️ Section",
    ["A", "B", "C"]
)

# Input: Programming / Tech Area
language = st.selectbox(
    "💻 Preferred Programming / Tech Area",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "Data Science",
        "Machine Learning"
    ]
)

# Input: Sports Dropdown
sport = st.selectbox(
    "🏏 Favorite Sport / Game",
    [
        "Cricket",
        "Football",
        "Volleyball",
        "Badminton",
        "Basketball",
        "Kabaddi",
        "Chess",
        "Athletics"
    ]
)

# Programming-based sentences
language_lines = {
    "Python": "I have a strong interest in Python, especially for automation, data handling, and problem-solving.",
    "Java": "I enjoy working with Java because of its object-oriented structure and real-world applications.",
    "C": "I like learning C as it helps me understand programming fundamentals and memory concepts.",
    "C++": "I enjoy C++ because it improves my problem-solving and algorithmic thinking.",
    "JavaScript": "I am passionate about JavaScript and enjoy building interactive web applications.",
    "Data Science": "I am interested in Data Science and enjoy analyzing data to extract meaningful insights.",
    "Machine Learning": "I am passionate about Machine Learning and enjoy building intelligent systems."
}

# Sports-based sentences
sports_lines = {
    "Cricket": "Apart from academics, I enjoy playing cricket, which has helped me develop teamwork and leadership skills.",
    "Football": "I love playing football as it keeps me active and teaches me discipline and teamwork.",
    "Volleyball": "I enjoy volleyball because it improves my coordination and team spirit.",
    "Badminton": "I like playing badminton as it enhances my focus, agility, and fitness.",
    "Basketball": "I enjoy basketball because it teaches quick decision-making and collaboration.",
    "Kabaddi": "I enjoy kabaddi as it builds physical strength, confidence, and strategic thinking.",
    "Chess": "I like playing chess as it sharpens my logical thinking and problem-solving skills.",
    "Athletics": "I am interested in athletics as it helps me stay disciplined, fit, and mentally strong."
}

# Button
if st.button("✨ Generate Extended Introduction"):
    if name.strip() != "":
        st.markdown("---")
        st.success(
            f"Hello everyone, my name is **{name}**. "
            f"I am currently a **{year}** student studying **{department}** at "
            f"**{college}**, Section **{section}**. "
            f"{language_lines[language]} "
            f"{sports_lines[sport]} "
            "I am continuously working on improving my technical and personal skills. "
            "My goal is to grow as a confident professional and contribute to meaningful projects in the future. "
            "I am excited to learn, explore new opportunities, and continue my journey with **Vibe Coding**."
        )
    else:
        st.error("❌ Please enter your name before submitting.")
 