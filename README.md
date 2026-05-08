# SkySenseAI

SkySenseAI is a modern full-stack weather application developed using FastAPI, HTML, CSS, and JavaScript. The project focuses on delivering real-time weather information through a clean and responsive user interface while maintaining high backend performance with asynchronous API handling.

The application uses OpenStreetMap's Nominatim API for city geocoding and the Open-Meteo API for fetching live weather data. Users can search for any city and instantly receive weather details such as temperature, wind speed, weather conditions, sunrise and sunset timings, and local time.

The frontend was designed with a glassmorphism-inspired interface and dynamic background transitions that change according to weather conditions. The goal of the project was to create a visually appealing yet lightweight weather application without relying on heavy frontend frameworks.

---

# Features

* Real-time weather search by city
* FastAPI-powered backend API
* Asynchronous API requests using HTTPX
* Dynamic weather icons and themes
* Responsive and modern UI
* Sunrise and sunset integration
* Weather condition mapping
* Lightweight frontend using vanilla JavaScript

---

# Tech Stack

## Backend

* Python
* FastAPI
* HTTPX
* Uvicorn

## Frontend

* HTML5
* CSS3
* JavaScript
* Font Awesome

## External APIs

* Open-Meteo API
* OpenStreetMap Nominatim API
* Sunrise-Sunset API

---

# Project Structure

```bash id="9hziv7"
SkySenseAI/
│
├── main.py
├── static/
│   └── index.html
├── requirements.txt
└── README.md
```

---

# Installation

To run this project locally, first clone the repository and move into the project directory.

```bash id="rdb01k"
git clone https://github.com/yourusername/sky-sense-ai.git
cd sky-sense-ai
```

Create and activate a virtual environment.

### Windows

```bash id="wlj5m6"
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash id="o8v4vz"
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies.

```bash id="v92jeq"
pip install fastapi uvicorn httpx
```

You can also use a requirements file.

```txt id="d5g8qv"
fastapi
uvicorn
httpx
```

```bash id="p64yls"
pip install -r requirements.txt
```

---

# Running the Application

After installing the dependencies, start the FastAPI server using:

```bash id="z0o8j8"
python main.py
```

Alternatively, the application can be started directly with uvicorn.

```bash id="hz57by"
uvicorn main:app --reload --host 0.0.0.0 --port 4001
```

Once the server starts successfully, open the following URL in your browser:

```txt id="j0w1vv"
http://127.0.0.1:4001
```

---

# API Endpoint

The backend exposes a weather endpoint that accepts a city name as a query parameter.

```http id="ggkg3x"
GET /weather?city=London
```

Example JSON response:

```json id="1dujlwm"
{
  "city": "London",
  "latitude": "51.5074",
  "longitude": "-0.1278",
  "temperature": 21.5,
  "windspeed": 10.2,
  "weathercode": 2,
  "time": "2026-05-09T12:00"
}
```

---

# Frontend Design

The frontend interface was built entirely with vanilla HTML, CSS, and JavaScript. Dynamic weather conditions are represented using Font Awesome icons and animated background gradients. The UI automatically adapts based on the current weather condition returned by the API.

The application also includes loading states, error handling, responsive layouts for smaller devices, and smooth visual transitions to improve user experience.

---

# Future Improvements

Several additional features can be implemented in future versions of the project:

* 7-day weather forecasting
* GPS-based automatic location detection
* Humidity and pressure support
* Dark mode toggle
* Docker containerization
* Database integration for search history
* Weather analytics dashboard

---

# License

This project is licensed under the MIT License.

---

# Author

Developed by Aryan
