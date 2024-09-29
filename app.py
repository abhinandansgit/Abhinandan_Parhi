import streamlit as st
from streamlit.components.v1 import html

# Custom CSS to style the page
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            color: #333;
            font-family: 'Roboto', sans-serif;
        }
        .header {
            background-color: #3498db;
            padding: 20px;
            color: white;
            text-align: center;
        }
        .section-title {
            font-size: 2.5em;
            margin-top: 40px;
            margin-bottom: 20px;
            color: #3498db;
        }
        .content {
            max-width: 1000px;
            margin: 0 auto;
            padding: 10px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #2980b9;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .skill-card {
            background-color: #808000;
            padding: 15px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 200px;
            text-align: center;
        }
        .footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'><h1>Abhinandan Parhi </h1></div>", unsafe_allow_html=True)

# About Section
st.markdown("<h2 class='section-title'>About</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
        <p>
            I am an innovative Python Developer with expertise in AI/ML, blending technical prowess with creative problem-solving to deliver impactful solutions. My journey has been shaped by hands-on experience in diverse industries, where I honed my skills and contributed to transformative projects.
        </p>
    </div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='skills-container'>
        <div class='skill-card'>
            <h3>Python</h3>
        </div>
        <div class='skill-card'>
            <h3>AI/ML</h3>
        </div>
        <div class='skill-card'>
            <h3>Internet of Things (IoT)</h3>
        </div>
        <div class='skill-card'>
            <h3>Drone Technology</h3>
        </div>
        <div class='skill-card'>
            <h3>Web Development</h3>
        </div>
        <div class='skill-card'>
            <h3>Team Management</h3>
        </div>
    </div>
""", unsafe_allow_html=True)

# Experience Section
st.markdown("<h2 class='section-title'>Experience</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    <p><strong>Innovation Lead, Entrepreneurship Cell Nalanda (2023)</strong></p>
    <p>Leading innovative projects and mentoring aspiring entrepreneurs. Focus on driving growth through tech-enabled solutions.</p>
        
     <p><strong>Incubation Trainee, AIC-Nalanda Institute of Technology Foundation (2022)</strong></p>
     <p>Gained hands-on experience in startup incubation, focusing on technological advancements and market strategies.</p>

     <p><strong>Python Developer (Freelance)</strong></p>
     <p>Developed scalable software solutions for various clients in AI and data-driven projects.</p>

     <p><strong>Photogrammetrist, Jaywing Technologies Pvt Ltd (2023)</strong></p>
     <p>Applied geomatics and photogrammetry techniques to optimize data analysis for aerial surveys and mapping projects.</p>
    </div>
""", unsafe_allow_html=True)

# Achievements Section
st.markdown("<h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
        <ul>
            <li><strong>October 2023 | IIT Kharagpur:</strong> Recognized for outstanding performance in a prestigious competition.</li>
            <li><strong>November 2023 | BPUT Tech Carnival:</strong> Achieved excellence by winning the Innovate-X competition, sponsored by IBM.</li>
            <li><strong>INNOVATE-X (by IBM) Winner:</strong> Demonstrated innovative thinking and technical skills to secure first place.</li>
            <li><strong>Drone Competition Winner:</strong> Excelled in drone technology, leading to victory in a highly competitive event.</li>
            <li><strong>August 2023 | IIT Ropar:</strong> Won the Startup Sprint, showcasing entrepreneurial skills and startup strategies.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("<h2 class='section-title'>Contact Me</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
        <p>Feel free to reach out for collaborations or just a friendly hello.</p>
        <p>Email: abhinandanparhi48@google.com</p>
        <p><a href='https://www.linkedin.com/in/abhinandan-parhi-ap/' class='btn'>LinkedIn</a></p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'><p>&copy; 2024 Abhinandan Parhi Portfolio. All rights reserved.</p></div>", unsafe_allow_html=True)
