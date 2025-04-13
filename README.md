# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME*: AKULA PRANAY KUMAR

*INTERN ID*: CT04WJ109 

*DOMAIN*: PYTHON PROGRAMMING 
I 
*DURATION*: 4 WEEEKS 

*MENTOR*: NEELA SANTHOSH KUMAR


This Python-based project is a real-time data application that fetches current weather information for a specific city using the OpenWeatherMap API and visualizes the data using popular data analysis libraries such as Matplotlib, Seaborn, and Pandas. The goal of this application is to integrate live external data (from a public API), process it for insights, and create visual representations that help users understand the data more intuitively.

This program can be particularly useful in areas like education, environmental research, data journalism, app prototyping, and beginner-level data science projects. It demonstrates how to integrate APIs with Python, handle JSON data, and represent numeric information visually for better understanding. It is designed to be beginner-friendly yet practical enough to demonstrate real-world programming skills in data science, analytics, and full-stack development.


TOOLS & TECHNOLOGIES USED :-

Programming Language: Python 3.x

API Provider: OpenWeatherMap (https://openweathermap.org/api)

Data Fetching: requests – for making HTTP calls to the API

Data Processing: pandas – to structure and manipulate the fetched weather data


VISUALIZATION:

matplotlib – for basic graph rendering

seaborn – for more aesthetic and color-rich plotting

Environment Variables Management: python-dotenv – to securely load API keys from a hidden .env file

Platform: Developed and tested in Visual Studio Code on Windows 11 with Python 3.11 and Git integration


KEY FEATURES:

Connects to a live weather API to fetch data such as temperature, humidity, and pressure

Automatically structures and stores the data in a Pandas DataFrame

Plots a bar chart showing weather metrics using Seaborn for visual appeal

Uses a .env file to secure API credentials and keep your OpenWeatherMap key safe

Modular, well-commented code that makes it easy to read, understand, and extend


REAL-WORLD USE CASES:

Education & Learning:

Ideal for students learning Python, API usage, and data visualization. It provides practical exposure to combining external data with code to create meaningful outputs.

Weather Dashboards:

Can be the starting point for building full-fledged weather dashboards or widgets for websites or mobile apps.

Data Science Prototypes:

Suitable as a beginner-friendly template to demonstrate API handling and visual output generation in early-stage data science portfolios.


REPORTS & PRESENTATIONS:

This tool can be used to pull and visualize real-time weather data for presentations, research papers, or reports that require environmental data.

Smart Home Integration (future extension):

With a little modification, this system could integrate into smart home interfaces that adapt lighting, HVAC, or alert systems based on external weather data.


SECURITY BEST PRACTICES:

This project uses a .env file to store the API key securely. The real .env file is excluded from the GitHub repo using .gitignore, and a sample .env.example file is provided so others can set up the project without exposing sensitive credentials.


 SETUP INSTRUCTIONS:

Clone the repo:
git clone https://github.com/yourusername/weather-visualization.git
cd weather-visualization

Install the required packages:
pip install -r requirements.txt

Create a .env file and add your API key:
OPENWEATHER_API_KEY=your_api

Run the script:
python task1_weather_api.py

This chart updates based on the selected city in the code.

#OUTPUT

![Image](https://github.com/user-attachments/assets/0b5be62a-08a3-4ae7-b625-b1d583c77d24)


