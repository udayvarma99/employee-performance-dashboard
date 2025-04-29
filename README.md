# employee-performance-dashboard
This dashboard presents employee performance metrics in a clean, interactive bar chart. It fetches data dynamically from a Flask API and renders it beautifully using Chart.js, styled with TailwindCSS.

Tech Stack

Backend: Python Flask
Frontend: HTML, TailwindCSS, Chart.js
Data Source: JSON

Project Structure

employee-performance-dashboard/
├── app.py          # Flask backend server
├── templates/
│    └── index.html # Frontend dashboard
├── static/
│    └── chart.min.js (optional if hosted via CDN)
├── data.json       # Sample employee performance data
├── README.md       # Project documentation

Features

Visualizes employee performance scores
Responsive and clean UI with Tailwind CSS
Dynamic data loading through Flask API
Easy to extend with additional metrics

How to Run Locally

Clone the repository:
git clone https://github.com/your-username/employee-performance-dashboard.git
cd employee-performance-dashboard
Install dependencies:
pip install flask
Run the Flask app:
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000/

Future Improvements

Add more performance metrics (e.g., attendance, goal achievements)
User authentication
Export dashboard reports to PDF

License

This project is open-source and free to use under the MIT License.
