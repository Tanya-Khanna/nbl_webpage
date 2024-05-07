import streamlit as st
import streamlit.components.v1 as components


def display_additional_info():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    
    with col1:
        if st.button("Total Hours: 13.5"):
            st.write("This course includes 9 sessions, each lasting 1.5 hours.")

    with col2:
        if st.button("Library Guide"):
            st.write("Data Science - Graduate Specialists - Rutgers University Research Guides")
            st.markdown("[View Guide](https://libguides.rutgers.edu/datascience)", unsafe_allow_html=True)
    
    with col3:
        if st.button("Workshop Calendar"):
            st.write("New Brunswick Libraries Workshops - Upcoming Events")
            st.markdown("[View Calendar](https://libcal.rutgers.edu/calendar/nblworkshops?cid=4537&t=d&d=0000-00-00&cal=4537&inc=0)", unsafe_allow_html=True)
    
    with col4:
        if st.button("Contact Info"):
            st.write("Reach out via email: tanya.khanna@rutgers.edu")

    with col5:
        if st.button("GitHub Repository"):
            st.write("Workshop Materials for Data Science at Rutgers-New Brunswick Libraries")
            st.markdown("[Visit GitHub](https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL)", unsafe_allow_html=True)

def main_layout():
    st.markdown("<h1 style='text-align: center;'>Data Science Workshops: Spring 2024</h1>", unsafe_allow_html=True)
    left, center, right = st.columns([14, 16, 14])
    with center:
        st.image('logo.png', width=500) 

    display_additional_info()

main_layout()

st.markdown("---")

workshops = [
    {"title": "Workshop 1: Introduction to Python Programming", "description": "Beginner-friendly workshop introducing Python programming basics.", "full_description": "This workshop is designed for beginners with little to no experience in programming, aiming to provide a rapid yet comprehensive introduction to the world of Python, one of the most popular and versatile programming languages today. Learners will quickly grasp Python syntax, script execution, and fundamental constructs like variables, data types, and operators. They will also explore control structures like if-else statements, loops, and functions, gaining practical skills in data structures such as lists, tuples, sets, and dictionaries. Additionally, the workshop covers file handling and text processing.", "link": "https://drive.google.com/file/d/19prKM96ZKK0m0YiD2xAEUhjhsf2VGF72/preview", "gif": "Python-Symbol.png", "video_link": "https://rutgers.app.box.com/s/28oms37i6vyb77d042zssxwy9dehodvr",
        "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%201_Introduction%20to%20Python/1.%20Introduction%20to%20Python%20Programming.ipynb",
        "notebook_path": "Workshop 1_Introduction to Python/1. Introduction to Python Programming.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL" },
    {"title": "Workshop 2: Mastering Data Analysis: Pandas and NumPy Essentials", "description": "Hands-on experience with data analysis using Pandas and NumPy in Python.", "full_description": "This workshop is designed to equip learners with powerful tools for data analysis in Python. Participants will delve into the world of NumPy, exploring its efficient arrays and array operations, which form the backbone of numerical computing in Python. The workshop then shifts to Pandas, where learners will get hands-on experience with its fundamental data structures - Series and DataFrame. This comprehensive session is ideal for anyone looking to enhance their data analysis skills, offering the tools needed to unlock insights from data with efficiency and precision.", "link": "https://drive.google.com/file/d/1hGmqXrAVJzqMKG1vaRWq1mTZaFMzJBzc/preview", "gif": "workshop2_new_resized.png",  "video_link": "https://rutgers.app.box.com/s/86tttuh40jv5y91v2wc5x20nw8wd3cd8", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop_2_Numpy_Pandas/Mastering%20Data%20Analysis%20-%20Pandas%20and%20NumPy%20Essentials.ipynb",
        "notebook_path": "Workshop_2_Numpy_Pandas/Mastering Data Analysis - Pandas and NumPy Essentials.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL"  },
    {"title": "Workshop 3: Unveiling Data Stories: Python for Visualization", "description": "Learn to reveal hidden stories in data using visualization tools like Matplotlib and Seaborn.", "full_description": "This workshop is designed to guide participants through the process of revealing hidden stories in data using Python. It focuses on using Matplotlib and Seaborn, two prominent visualization tools, for effective exploratory data analysis (EDA). This workshop emphasizes the creation of engaging visual narratives, enabling participants to transform complex data insights into compelling and understandable visual formats.", "link": "https://drive.google.com/file/d/1YDNQlAV9XDnPW-wdJh2-ElFKjR-M8xRh/preview",  "gif": "workshop3_resized (1).png", "video_link": "https://rutgers.app.box.com/s/f7w64jvm9txqhj3wrg0byne73qsx9dnl", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop_3_Data%20Viz%20%26%20Exploration/Python%20for%20Visualization%20and%20Exploration.ipynb",
        "notebook_path": "Workshop_3_Data Viz & Exploration/Python for Visualization and Exploration.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL" },
    {"title": "Workshop 4: Mathematical Foundations for Data Science", "description": "Overview of essential mathematics for data science, including statistics, probability, and linear algebra.", "full_description": "This workshop offers a brief yet comprehensive overview of essential mathematics for data science. It covers foundational statistics and probability, crucial for model understanding, and basic hypothesis testing techniques. It also introduces linear algebra concepts like vectors and matrices, alongside fundamental calculus for derivatives and integrals.", "link": "https://drive.google.com/file/d/103VXTSYxd64egPD7isStTdO9XzWNb6Bq/preview",  "gif": "workshop4_resized.jpeg", "video_link": "https://rutgers.app.box.com/s/6vfncnhgng6mmb6e4mci1m76djzo8sy0"},
    {"title": "Workshop 5: Introduction to Machine Learning: Supervised Learning", "description": "Dive into supervised learning algorithms and understand how machines learn from data.", "full_description": "This workshop is tailored for beginners in machine learning. It focuses on supervised learning algorithms that are a cornerstone of machine learning, where the algorithm learns from labeled training data, helping to predict outcomes for unforeseen data. Classification and Regression will be introduced. Participants will learn about key algorithms like Linear Regression and Decision Trees, exploring how these methods enable machines to learn from and make predictions based on data.", "link": "https://drive.google.com/file/d/183pf5YYaUsLsE1Z3GsDht9yTHcT-Kq09/preview",  "gif": "workshop5.png", "video_link": "https://rutgers.app.box.com/s/vvjmyzdo6ndgqu5hkh8bol9s1gya6re9", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%205_Machine%20Learning-Supervised/ML%20-%20Supervised%20Learning.ipynb",
        "notebook_path": "Workshop 5_Machine Learning-Supervised/ML - Supervised Learning.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL" },
    {"title": "Workshop 6: Introduction to Machine Learning: Unsupervised Learning", "description": "Explore unsupervised learning concepts and techniques such as clustering and PCA.", "full_description": "This workshop is designed to introduce the concepts of unsupervised learning, a branch of machine learning where algorithms infer patterns from unlabelled data. The course covers clustering methods like K-means and DBSCAN, used to identify inherent groupings in data. It also explores dimensionality reduction techniques such as PCA, which simplify complex data sets while preserving their key features. Additionally, the session introduces association rules, a method for finding interesting relationships within data sets. This workshop is ideal for those interested in learning how to extract insights from data without predetermined labels or categories.", "link": "https://drive.google.com/file/d/1hz5kr7VpZH07aV1QpyLpRlYZEeVMb6dl/preview",  "gif": "workshop6_resized.png", "video_link": "https://rutgers.app.box.com/s/c3ah73jfqc72mrrl3nezl9wszxptu5fu", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%206_Machine%20Learning-Unsupervised/Machine%20Learning%20-%20Unsupervised%20Learning.ipynb",
        "notebook_path": "Workshop 6_Machine Learning-Unsupervised/Machine Learning - Unsupervised Learning.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL" },
    {"title": "Workshop 7: Introduction to Deep Learning", "description": "Fundamentals of deep learning, including neural networks and their architectures.", "full_description": "This workshop offers an introduction to the fundamentals of deep learning, a highly influential branch of artificial intelligence. This session focuses on the core concepts of neural networks, including feedforward neural networks, the simplest type of artificial neural network architecture. The course also covers convolutional neural networks (CNNs), essential for image and video recognition, and recurrent neural networks (RNNs), which are crucial for handling sequential data like text and speech.", "link": "https://drive.google.com/file/d/14p9947uh1Mpv-YaeRpgm1Xy30LZN9hoU/preview",  "gif": "workshop7.gif", "video_link": "https://rutgers.app.box.com/s/u45bm5qo692rxl5yf3znvkei8qxcihi7", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop_7_Deep_Learning/Recurrent_Neural_Networks.ipynb",
        "notebook_path": "Workshop_7_Deep_Learning/Recurrent_Neural_Networks.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL" },
    {"title": "Workshop 8: Deep Dive into Natural Language Processing", "description": "Techniques for processing and understanding human language using NLP.", "full_description": "Are you eager to learn how to communicate with computer systems using Natural Language Processing (NLP) techniques, or to make machines understand human sentiments? Do you aspire to build intelligent applications like Siri, Alexa, or chatbots, even if you're starting from scratch? This workshop introduces Natural Language Processing (NLP), teaching you to preprocess text, analyze sentiments, model topics, and use language generation models. It's perfect for anyone eager to build applications that interact naturally with human language.", "link": "https://drive.google.com/file/d/1y2fDEczq8MzqDFdhVpBpIWMYzJzQy3dy/preview",  "gif": "workshop8.gif", "video_link": "https://rutgers.app.box.com/s/zxnowedjxpv7hr66joiqvlrvlcrdobk0", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%208_Natural%20Language%20Processing/Deep-Dive-into-Natural-Language-Processing.ipynb",
        "notebook_path": "Workshop 8_Natural Language Processing/Deep-Dive-into-Natural-Language-Processing.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL" },
    {"title": "Workshop 9: Large Language Models and ChatGPT", "description": "Explore the workings and applications of large language models like ChatGPT.", "full_description": "This workshop offers a thorough exploration of cutting-edge language models, with a spotlight on ChatGPT. Attendees will delve into the design, training techniques, and practical uses of these models. Discussions on ethical usage and best practices will be a key part of the learning experience. By the workshop's end, participants will gain a deep understanding of large language models and how to effectively apply ChatGPT and similar technologies.", "link": "https://drive.google.com/file/d/1jCWIan-WntBD5rP6f1DwRGbrFpf8Sj-E/preview",  "gif": "workshop9.jpeg", "video_link": "https://rutgers.app.box.com/s/4xkb3wrodv4ay9mrqou56gfk3d2tlukw", "code_link": "https://github.com/Tanya-Khanna/DataScienceWorkshop_2024_NBL/blob/main/Workshop%209_Large%20Language%20Models/Workshop9-Practical%20Session.ipynb",
        "notebook_path": "Workshop 9_Large Language Models/Workshop9-Practical Session.ipynb",
        "github_repo": "Tanya-Khanna/DataScienceWorkshop_2024_NBL"},
]

def display_notebook_via_nbviewer(github_repo, notebook_path):
    if notebook_path:
        notebook_path = notebook_path.replace(" ", "%20")
        nbviewer_url = f"http://nbviewer.jupyter.org/github/{github_repo}/blob/main/{notebook_path}"
        st.markdown(f"[View Notebook]({nbviewer_url})", unsafe_allow_html=True)
    else:
        st.write("No notebook available for this workshop.")

def create_workshop_column(workshop):
    st.image(workshop['gif'], use_column_width=True)  
    st.subheader(workshop['title'])

    with st.expander("Read more"):
        st.write(workshop['full_description'])

    left, btn_col1, btn_col2, btn_col3, right = st.columns([1, 2, 2, 2, 1])

    st.markdown("""
    <style>
    .stButton>button {
        display: inline-block;
        padding: 0.5em 2em;
        margin: 0.1em;
        border-radius: 0.15em;
        box-sizing: border-box;
        text-decoration: none;
        font-family: 'Times New Roman',sans-serif;
        font-weight: 600;
        color: #FFFFFF;
        background-color: #AA4A44; 
        text-align: center;
        transition: all 0.2s;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0056b3;  /* Darker blue */
    }
    </style>
    """, unsafe_allow_html=True)
    
    if btn_col1.button("PPT", key='dive_in_' + workshop['title']):
        st.session_state['show_pdf_' + workshop["title"]] = True 

    if btn_col2.button("Video", key='video_' + workshop['title']):
        st.markdown(f'<a href="{workshop["video_link"]}" target="_blank">Watch the Workshop Recording!</a>', unsafe_allow_html=True)

    if btn_col3.button("Code", key='code_' + workshop['title']):
            if 'notebook_path' in workshop and 'github_repo' in workshop:
                display_notebook_via_nbviewer(workshop['github_repo'], workshop['notebook_path'])
            elif 'code_link' in workshop:
                st.markdown(f'<a href="{workshop["code_link"]}" target="_blank">Code</a>', unsafe_allow_html=True)
            else:
                st.write("No code available for this workshop.")

    if st.session_state.get('show_pdf_' + workshop['title'], False):
        pdf_url = workshop['link'].replace("/view?usp=sharing", "/preview")
        components.html(
            f"""
            <iframe src="{pdf_url}" width="100%" height="800" frameborder="0">
                This browser does not support PDFs. Please download the PDF to view it: <a href="{pdf_url}">Download PDF</a>
            </iframe>
            """,
            height=800
        )
        
        if st.button("Hide", key='hide_' + workshop['title']):
            st.session_state['show_pdf_' + workshop['title']] = False  


for i in range(0, len(workshops), 3):
    cols = st.columns(3)
    for col, workshop in zip(cols, workshops[i:i+3]):
        with col:
            create_workshop_column(workshop)
    
    st.markdown(" " * 10)  
