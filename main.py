import os
import asyncio
from collections import defaultdict
from datetime import date
from dotenv import load_dotenv
import httpx

BASE_URL = "https://v3.football.api-sports.io"
FIXTURES_ENDPOINT = "/fixtures"

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-apisports-key": API_KEY}


async def fetch_fixtures_by_date(target_date: str) -> list:
    url = f"{BASE_URL}{FIXTURES_ENDPOINT}?date={target_date}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise ConnectionError(f"API error: {response.status_code} - {response.text}")

    response_data = response.json().get("response", [])

    fixtures = []
    for fixture in response_data:
        fixtures.append({
            "league": fixture["league"]["name"],
            "home_team": fixture["teams"]["home"]["name"],
            "away_team": fixture["teams"]["away"]["name"],
            "kickoff": fixture["fixture"]["date"]
        })

    return fixtures

#group fixture by league
def group_fixtures_by_league(fixtures: list) -> dict:
    grouped = defaultdict(list)
    for match in fixtures:
        grouped[match["league"]].append(match)
    return grouped


def display_fixtures(fixtures: list, target_date: str) -> None:
    print(f"\n📅 Fixtures for {target_date}:\n")

    if not fixtures:
        print("No fixtures found.")
        return

    grouped_fixtures = group_fixtures_by_league(fixtures)

    for league, matches in grouped_fixtures.items():
        print(f"🏆 {league}")
        for match in matches:
            print(f"   - {match['home_team']} vs {match['away_team']} at {match['kickoff']}")
        print()  #add an empty line between the leagues for better readability


async def main():
    today = date.today().isoformat()
    try:
        fixtures = await fetch_fixtures_by_date(today)
        display_fixtures(fixtures, today)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
