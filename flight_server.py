# flight_server.py
from mcp.server.fastmcp import FastMCP
from datetime import datetime
from typing import List, Dict

mcp = FastMCP("Flight Search")

@mcp.tool()
def search_flights(source: str, destination: str, date: str) -> List[Dict]:
    """
    Search for flights by IATA codes and date (YYYY-MM-DD).
    Returns a list of dicts (flight, source, destination, date, depart, arrive, price).
    """
    # basic date validation
    try:
        _ = datetime.fromisoformat(date).date()
    except Exception:
        return [{"error": "date must be YYYY-MM-DD"}]

    # ---- MOCK DATA (replace this with a real flight-API call later) ----
    sample_flights = [
        {"flight": "AI101", "source": "DEL", "destination": "JFK", "date": "2025-09-25", "depart": "08:00", "arrive": "14:00", "price": 750},
        {"flight": "AI102", "source": "DEL", "destination": "JFK", "date": "2025-09-25", "depart": "22:00", "arrive": "04:00", "price": 720},
        {"flight": "AC043", "source": "YYZ", "destination": "DEL", "date": "2025-09-26", "depart": "07:00", "arrive": "19:00", "price": 900},
    ]
    results = [
        f for f in sample_flights
        if f["source"].upper() == source.upper() and f["destination"].upper() == destination.upper() and f["date"] == date
    ]

    if not results:
        return [{"message": f"No flights found from {source} to {destination} on {date}"}]
    return results

if __name__ == "__main__":
    # direct execution for quick local testing:
    mcp.run()
