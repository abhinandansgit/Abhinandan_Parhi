import streamlit as st
from streamlit.components.v1 import html

# Custom CSS to style the page with improved color scheme and layout
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        body {
            background-color: #1a1a2e;
            color: #e0e0e0;
            font-family: 'Poppins', sans-serif;
        }
        .header {
            background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
            padding: 30px;
            color: white;
            text-align: center;
            border-radius: 0 0 20px 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 2.5em;
            margin: 0;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            display: inline-block;
        }
        .section-title {
            font-size: 2.5em;
            margin-top: 40px;
            margin-bottom: 20px;
            color: #e94560;
            text-align: center;
        }
        .content-box {
            background-color: #16213e;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .content-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 8px rgba(233, 69, 96, 0.2);
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #e94560;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .btn:hover {
            background-color: #c81d4e;
            transform: translateY(-3px);
            box-shadow: 0 4px 6px rgba(233, 69, 96, 0.2);
        }
        .skills-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 40px;
        }
        .skill-card {
            background: linear-gradient(135deg, #0f3460 0%, #16213e 100%);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: all 0.3s ease;
        }
        .skill-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 8px rgba(233, 69, 96, 0.2);
        }
        .footer {
            background-color: #0f3460;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            border-radius: 20px 20px 0 0;
        }
        .animate-charcter {
            background-image: linear-gradient(
                -225deg,
                #e94560 0%,
                #44107a 29%,
                #ff1361 67%,
                #fff800 100%
            );
            background-size: auto auto;
            background-clip: border-box;
            background-size: 200% auto;
            color: #fff;
            background-clip: text;
            text-fill-color: transparent;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textclip 2s linear infinite;
            display: inline-block;
        }
        @keyframes textclip {
            to {
                background-position: 200% center;
            }
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
    </style>
""", unsafe_allow_html=True)

# Header with animated name
st.markdown("""
    <div class='header'>
        <h1>
            <span class='animate-charcter'>Abhinandan Parhi</span>
        </h1>
    </div>
""", unsafe_allow_html=True)

# Rest of the code remains the same...

# About Section
st.markdown("<h2 class='section-title'>About</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content-box'>
        <p>
            I am an innovative Python Developer with expertise in AI/ML, blending technical prowess with creative problem-solving to deliver impactful solutions. My journey has been shaped by hands-on experience in diverse industries, where I honed my skills and contributed to transformative projects.
        </p>
    </div>
""", unsafe_allow_html=True)

# Skills Section with animated progress bars
st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)
skills = [
    ("Python", 90),
    ("AI/ML", 85),
    ("Internet of Things (IoT)", 80),
    ("Drone Technology", 75),
    ("Web Development", 70),
    ("Team Management", 85)
]

st.markdown("<div class='skills-container'>", unsafe_allow_html=True)
for skill, proficiency in skills:
    st.markdown(f"""
        <div class='skill-card'>
            <h3>{skill}</h3>
            <div class='progress-bar' style='background-color: #e0e0e0; border-radius: 5px; height: 10px;'>
                <div style='width: {proficiency}%; background-color: #e94560; height: 100%; border-radius: 5px; transition: width 1s ease-in-out;'></div>
            </div>
            <p>{proficiency}%</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Experience Section
st.markdown("<h2 class='section-title'>Experience</h2>", unsafe_allow_html=True)
experiences = [
    ("Innovation Lead", "Entrepreneurship Cell Nalanda", "2023", "Leading innovative projects and mentoring aspiring entrepreneurs. Focus on driving growth through tech-enabled solutions."),
    ("Incubation Trainee", "AIC-Nalanda Institute of Technology Foundation", "2022", "Gained hands-on experience in startup incubation, focusing on technological advancements and market strategies."),
    ("Python Developer", "Freelance", "", "Developed scalable software solutions for various clients in AI and data-driven projects."),
    ("Photogrammetrist", "Jaywing Technologies Pvt Ltd", "2023", "Applied geomatics and photogrammetry techniques to optimize data analysis for aerial surveys and mapping projects.")
]

for title, company, year, description in experiences:
    st.markdown(f"""
        <div class='content-box'>
            <h3>{title} {f"({year})" if year else ""}</h3>
            <h4>{company}</h4>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

# Achievements Section
st.markdown("<h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)
achievements = [
    ("October 2023 | IIT Kharagpur", "Recognized for outstanding performance in a prestigious competition."),
    ("November 2023 | BPUT Tech Carnival", "Achieved excellence by winning the Innovate-X competition, sponsored by IBM."),
    ("INNOVATE-X (by IBM) Winner", "Demonstrated innovative thinking and technical skills to secure first place."),
    ("Drone Competition Winner", "Excelled in drone technology, leading to victory in a highly competitive event."),
    ("August 2023 | IIT Ropar", "Won the Startup Sprint, showcasing entrepreneurial skills and startup strategies.")
]

for achievement, description in achievements:
    st.markdown(f"""
        <div class='content-box'>
            <h3>{achievement}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

# Contact Section
st.markdown("<h2 class='section-title'>Contact Me</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content-box'>
        <p>Feel free to reach out for collaborations or just a friendly hello.</p>
        <p>Email: abhinandanparhi48@google.com</p>
        <a href='https://www.linkedin.com/in/abhinandan-parhi-ap/' class='btn'>LinkedIn</a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'><p>&copy; 2024 Abhinandan Parhi Portfolio. All rights reserved.</p></div>", unsafe_allow_html=True)

# JavaScript remains the same
