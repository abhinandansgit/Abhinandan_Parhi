import streamlit as st
from streamlit.components.v1 import html


st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        body {
            background-color: #1a1a2e;
            color: #e0e0e0;
            font-family: 'Poppins', sans-serif;
        }
        @keyframes rainbow-border {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .rainbow-border {
            position: relative;
            z-index: 0;
            border-radius: 10px;
            overflow: hidden;
        }
        .rainbow-border::before {
            content: '';
            position: absolute;
            z-index: -2;
            left: -8mm;
            top: -8mm;
            width: calc(100% + 16mm);
            height: calc(100% + 16mm);
            background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #8b00ff, #ff0000);
            background-size: 200% 200%;
            animation: rainbow-border 4s linear infinite;
        }
        .rainbow-border::after {
            content: '';
            position: absolute;
            z-index: -1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: inherit;
            border-radius: 10px;
        }
        .header {
            background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
            padding: 30px;
            color: white;
            text-align: center;
            border-radius: 0 0 20px 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
            position: relative;
        }
        .header h1 {
            font-size: 2.5em;
            margin: 0;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            display: inline-block;
        }
        .floating-logo {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(233, 69, 96, 0.5);
            transition: all 0.3s ease;
        }
        .floating-logo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
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

st.markdown("""
    <div class='header rainbow-border'>
        <h1>
            <span class='animate-charcter'>Abhinandan Parhi</span>
        </h1>
        <div class='floating-logo rainbow-border'>
            <img src="https://iili.io/dtPhOYX.md.png" alt="Logo">
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const logo = document.querySelector('.floating-logo');
            let lastScrollTop = 0;

            window.addEventListener('scroll', function() {
                let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                if (scrollTop > lastScrollTop) {
                    // Scrolling down
                    logo.style.transform = 'translateY(10px) rotate(5deg)';
                } else {
                    // Scrolling up
                    logo.style.transform = 'translateY(-10px) rotate(-5deg)';
                }
                lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
            });

            logo.addEventListener('mouseover', function() {
                this.style.transform = 'scale(1.1) rotate(10deg)';
            });

            logo.addEventListener('mouseout', function() {
                this.style.transform = 'scale(1) rotate(0deg)';
            });

            logo.addEventListener('click', function() {
                this.style.animation = 'spin 0.5s linear';
                setTimeout(() => {
                    this.style.animation = '';
                }, 500);
            });
        });
    </script>
""", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>About</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content-box rainbow-border'>
        <p>
            I am an innovative Python Developer with expertise in AI/ML, blending technical prowess with creative problem-solving to deliver impactful solutions. My journey has been shaped by hands-on experience in diverse industries, where I honed my skills and contributed to transformative projects.
        </p>
    </div>
""", unsafe_allow_html=True)

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
        <div class='skill-card rainbow-border'>
            <h3>{skill}</h3>
            <div class='progress-bar' style='background-color: #e0e0e0; border-radius: 5px; height: 10px;'>
                <div style='width: {proficiency}%; background-color: #e94560; height: 100%; border-radius: 5px; transition: width 1s ease-in-out;'></div>
            </div>
            <p>{proficiency}%</p>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Experience</h2>", unsafe_allow_html=True)
experiences = [
    ("Innovation Lead", "Entrepreneurship Cell Nalanda", "2023", "Leading innovative projects and mentoring aspiring entrepreneurs. Focus on driving growth through tech-enabled solutions."),
    ("Incubation Trainee", "AIC-Nalanda Institute of Technology Foundation", "2022", "Gained hands-on experience in startup incubation, focusing on technological advancements and market strategies."),
    ("Python Developer", "Freelance", "", "Developed scalable software solutions for various clients in AI and data-driven projects."),
    ("Photogrammetrist", "Jaywing Technologies Pvt Ltd", "2023", "Applied geomatics and photogrammetry techniques to optimize data analysis for aerial surveys and mapping projects.")
]

for title, company, year, description in experiences:
    st.markdown(f"""
        <div class='content-box rainbow-border'>
            <h3>{title} {f"({year})" if year else ""}</h3>
            <h4>{company}</h4>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

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
        <div class='content-box rainbow-border'>
            <h3>{achievement}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>Contact Me</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content-box rainbow-border'>
        <p>Feel free to reach out for collaborations or just a friendly hello.</p>
        <p>Email: abhinandanparhi48@google.com</p>
        <a href='https://www.linkedin.com/in/abhinandan-parhi-ap/' class='btn rainbow-border'>LinkedIn</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer rainbow-border'><p>&copy; 2024 Abhinandan Parhi Portfolio. All rights reserved.</p></div>", unsafe_allow_html=True)
