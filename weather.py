from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import httpx
import uvicorn
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join("static", "index.html")
    if not os.path.isfile(index_path):
        return HTMLResponse("<h1>index.html not found</h1>", status_code=404)
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/weather")
async def get_weather(city: str = Query(..., description="City name")):
    geocode_url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "SkySenseAI/1.0 (contact@example.com)"}

    async with httpx.AsyncClient() as client:
        geocode_resp = await client.get(geocode_url, params=params, headers=headers)
        if geocode_resp.status_code != 200 or not geocode_resp.json():
            raise HTTPException(status_code=404, detail="City not found")

        geo_data = geocode_resp.json()[0]
        lat = geo_data["lat"]
        lon = geo_data["lon"]

        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
        }
        weather_resp = await client.get(weather_url, params=weather_params)
        if weather_resp.status_code != 200:
            raise HTTPException(status_code=500, detail="Weather API error")

        weather_data = weather_resp.json().get("current_weather", {})
        if not weather_data:
            raise HTTPException(status_code=404, detail="Weather data not found")

    return JSONResponse({
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "temperature": weather_data.get("temperature"),
        "windspeed": weather_data.get("windspeed"),
        "weathercode": weather_data.get("weathercode"),
        "time": weather_data.get("time"),
    })

if __name__ == "__main__":
    # Changed port to 8002 to avoid conflicts
    uvicorn.run(app, host="0.0.0.0", port=4001)
