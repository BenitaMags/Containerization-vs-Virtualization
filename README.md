# Containerization-vs-Virtualization

This interactive application was built with the assistance of Gemini AI.

It provides a clear visualization to explain and compare containerization and virtualization technologies. Designed to help you understand the architectural differences between how applications are packaged and run in these two popular environments.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Live Demo
Experience the app live:
https://containerization-vs-virtualization-a3wkedjwrlpsnomj3eaf8q.streamlit.app/

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Features
- Interactive Visualizations: Explore layered diagrams for both virtualization and containerization.
- Component Details: Click on specific architectural components (e.g., Physical Server, Hypervisor, Container Runtime) to view detailed explanations.
- Key Differences Summary: A concise comparison highlighting the main benefits and characteristics of each technology.
- Built with Streamlit: A user-friendly web application interface.
  
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Technologies Used
- Application Framework: Streamlit (For building and deploying the interactive web application in Python)
- Frontend (Visualization Logic): React.js (The core interactive diagram logic was originally prototyped in React)
- AI Assistance: Gemini AI (For code generation, architectural guidance, and explanations)
- Styling: Tailwind CSS (Conceptual, for the original React component)
- Icons: Lucide React (Conceptual, for the original React component)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## How to Run Locally (Streamlit Version)
To get this application running on your local machine, follow these simple steps:

Clone the Repository:
   ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
   ```
 (Replace YOUR_USERNAME and YOUR_REPOSITORY_NAME with your actual GitHub details.)

 Create a Virtual Environment (Recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
 Install Dependencies:

Code snippet

```bash
pip install -r requirements.txt
```

 Run the Streamlit Application:

```bash
streamlit run app.py
```
 Your web browser should automatically open a new tab displaying the application. If not, navigate to http://localhost:8501.
 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Deployment to Streamlit Cloud
This application is designed for easy deployment to Streamlit Cloud, a platform that allows you to host your Streamlit apps directly from your GitHub repository.

Push to GitHub: Ensure your app.py and requirements.txt files are pushed to a GitHub repository (as you planned).
Go to Streamlit Cloud: Visit share.streamlit.io.
Connect Repository: Sign in with your GitHub account, click "New app," select your repository, and specify app.py as the main file.
Deploy! Streamlit Cloud will handle the rest, building your app and providing you with a public URL.
Project Structure
.
├── app.py              # The main Streamlit application code
├── requirements.txt    # Python dependencies for Streamlit
└── README.md           # This file

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Contributing
Feel free to fork this repository, suggest improvements, or open issues. Contributions are welcome!
