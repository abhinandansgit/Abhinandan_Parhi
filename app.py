import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Abhinandan Parhi | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# GLOBAL STYLES
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

.stApp {
    background-color: #1a1a2e;
    color: #e0e0e0;
    font-family: 'Poppins', sans-serif;
    max-width: 1200px;
    margin: auto;
}

/* =========================
   RAINBOW BORDER
   ========================= */
@keyframes rainbow-border {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.rainbow-border {
    position: relative;
    border-radius: 14px;
    overflow: hidden;
}

.rainbow-border::before {
    content: "";
    position: absolute;
    inset: -6px;
    background: linear-gradient(
        90deg,
        #ff0000, #ff7f00, #ffff00,
        #00ff00, #0000ff, #8b00ff, #ff0000
    );
    background-size: 200% 200%;
    animation: rainbow-border 4s linear infinite;
    z-index: -1;
}

/* =========================
   HEADER
   ========================= */
.header {
    background: linear-gradient(135deg, #16213e, #0f3460);
    padding: 45px 20px;
    text-align: center;
    border-radius: 0 0 28px 28px;
    margin-bottom: 50px;
    position: relative;
}

.animate-charcter {
    background-image: linear-gradient(
        -225deg,
        #e94560 0%,
        #44107a 29%,
        #ff1361 67%,
        #fff800 100%
    );
    background-size: 200% auto;
    color: transparent;
    background-clip: text;
    -webkit-background-clip: text;
    animation: textclip 2s linear infinite;
    font-size: 3rem;
    font-weight: 600;
}

@keyframes textclip {
    to { background-position: 200% center; }
}

/* =========================
   FLOATING LOGO
   ========================= */
.floating-logo {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 90px;
    height: 90px;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(233, 69, 96, 0.6);
    transition: transform 0.3s ease;
}

.floating-logo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* =========================
   SECTIONS
   ========================= */
.section-title {
    font-size: 2.4rem;
    color: #e94560;
    text-align: center;
    margin: 60px 0 30px;
}

.content-box {
    background-color: #16213e;
    padding: 25px;
    margin-bottom: 25px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.content-box:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 20px rgba(233, 69, 96, 0.25);
}

/* =========================
   SKILLS
   ========================= */
.skills-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 22px;
}

.skill-card {
    background: linear-gradient(135deg, #0f3460, #16213e);
    padding: 22px;
    text-align: center;
}

/* =========================
   BUTTON
   ========================= */
.btn {
    display: inline-block;
    padding: 12px 26px;
    background-color: #e94560;
    color: white;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 14px rgba(233, 69, 96, 0.35);
}

/* =========================
   FOOTER
   ========================= */
.footer {
    background-color: #0f3460;
    text-align: center;
    padding: 22px;
    margin-top: 60px;
    border-radius: 28px 28px 0 0;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header rainbow-border">
    <h1 class="animate-charcter">Abhinandan Parhi</h1>
    <div class="floating-logo rainbow-border">
        <img src="https://iili.io/dtPhOYX.md.png">
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# FLOATING LOGO JS (SAFE)
# =========================
html("""
<script>
const logo = document.querySelector('.floating-logo');
if (logo) {
    logo.addEventListener('mouseover', () => {
        logo.style.transform = 'scale(1.1) rotate(8deg)';
    });
    logo.addEventListener('mouseout', () => {
        logo.style.transform = 'scale(1)';
    });
}
</script>
""", height=0)

# =========================
# ABOUT
# =========================
st.markdown("<h2 class='section-title'>About</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="content-box rainbow-border">
<p>
I am an innovative Python Developer with expertise in AI/ML, blending technical depth with creative problem-solving.
My work spans AI systems, IoT, drones, and scalable web platforms, with a strong focus on real-world impact.
</p>
</div>
""", unsafe_allow_html=True)

# =========================
# SKILLS
# =========================
st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)

skills = [
    ("Python", 90),
    ("AI / ML", 85),
    ("IoT", 80),
    ("Drone Technology", 75),
    ("Web Development", 70),
    ("Team Management", 85),
]

st.markdown("<div class='skills-container'>", unsafe_allow_html=True)
for skill, value in skills:
    st.markdown(f"""
    <div class="skill-card rainbow-border">
        <h3>{skill}</h3>
        <div style="background:#333;height:10px;border-radius:6px;">
            <div style="width:{value}%;height:100%;
            background:#e94560;border-radius:6px;"></div>
        </div>
        <p>{value}%</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# EXPERIENCE
# =========================
st.markdown("<h2 class='section-title'>Experience</h2>", unsafe_allow_html=True)

experiences = [
    ("Innovation Lead", "Entrepreneurship Cell Nalanda", "2023",
     "Leading innovation-driven projects and mentoring student founders."),
    ("Incubation Trainee", "AIC-Nalanda Institute of Technology Foundation", "2022",
     "Worked on startup incubation, product validation, and tech strategy."),
    ("Python Developer", "Freelance", "",
     "Built AI-powered and data-driven software solutions."),
    ("Photogrammetrist", "Jaywing Technologies Pvt Ltd", "2023",
     "Applied geomatics and aerial data analytics for mapping projects."),
]

for role, org, year, desc in experiences:
    st.markdown(f"""
    <div class="content-box rainbow-border">
        <h3>{role} {f"({year})" if year else ""}</h3>
        <h4>{org}</h4>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# ACHIEVEMENTS
# =========================
st.markdown("<h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)

achievements = [
    ("IIT Kharagpur – Oct 2023", "Awarded for technical excellence."),
    ("BPUT Tech Carnival – Nov 2023", "Innovate-X Winner (IBM)."),
    ("INNOVATE-X (IBM)", "National-level innovation winner."),
    ("Drone Competition Winner", "Recognized for drone system design."),
    ("IIT Ropar – Aug 2023", "Startup Sprint Winner."),
]

for title, desc in achievements:
    st.markdown(f"""
    <div class="content-box rainbow-border">
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CONTACT
# =========================
st.markdown("<h2 class='section-title'>Contact</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="content-box rainbow-border">
<p>Email: abhinandanparhi48@gmail.com</p>
<p>Phone: +91 63722 02830</p>
<a href="https://www.linkedin.com/in/abhinandan-parhi-ap/" class="btn">LinkedIn</a>
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer rainbow-border">
<p>© 2024 Abhinandan Parhi. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
