import json

def parse_resume_to_json(resume_text):
    # Example resume sections
    sections = {
        "Personal Information": {},
        "Education": [],
        "Skills": [],
        "Experience": [],
        "Projects": []
    }

    # Example parsing logic (This will vary based on resume format)
    lines = resume_text.split('\n')
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if 'Personal Information' in line:
            current_section = 'Personal Information'
            continue
        elif 'Education' in line:
            current_section = 'Education'
            continue
        elif 'Skills' in line:
            current_section = 'Skills'
            continue
        elif 'Experience' in line:
            current_section = 'Experience'
            continue
        elif 'Projects' in line:
            current_section = 'Projects'
            continue
        
        if current_section == 'Personal Information':
            key, value = line.split(':', 1)
            sections[current_section][key.strip()] = value.strip()
        elif current_section in ['Education', 'Skills', 'Experience', 'Projects']:
            sections[current_section].append(line)

    return json.dumps(sections, indent=4)

# Example resume text input
resume_text = """
Personal Information:
Name: Amrutha Aananthi
Email: amrutha@gmail.com
Phone: 123-456-7890

Education:
B.Tech in Computer Science - XYZ University, 2024

Skills:
C, C++, Python, Front-end Web Development, UI/UX, Data Analytics

Experience:
Intern at ABC Corp - Worked on AI projects, 2023

Projects:
Project 1: Developed a machine learning model to predict stock prices.
Project 2: Designed a responsive website using HTML, CSS, and JavaScript.
"""

# Parse the resume text and print the JSON
parsed_resume_json = parse_resume_to_json(resume_text)
print(parsed_resume_json)
