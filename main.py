import os
from datetime import date
from collections import defaultdict
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {"x-apisports-key": API_KEY}


class FootballAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS

    def get_fixtures_by_date(self, target_date: str):
        url = f"{self.base_url}/fixtures"
        params = {"date": target_date}

        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code != 200:
            raise ConnectionError(f"API error: {response.status_code} - {response.text}")

        fixtures = []
        for item in response.json().get("response", []):
            fixtures.append({
                "league": item["league"]["name"],
                "home": item["teams"]["home"]["name"],
                "away": item["teams"]["away"]["name"],
                "kickoff": item["fixture"]["date"]
            })

        return fixtures

    @staticmethod
    #group fixtures by league
    def group_fixtures_by_league(fixtures: list):
        grouped = defaultdict(list)
        for match in fixtures:
            grouped[match["league"]].append(match)
        return grouped
    #display fixtures grouped by league
    def display_fixtures(self, fixtures: list, date_label: str):
        print(f"\n📅 Fixtures for {date_label}:\n")

        if not fixtures:
            print("No fixtures found.")
            return

        grouped = self.group_fixtures_by_league(fixtures)

        for league, matches in grouped.items():
            print(f"🏆 {league}")
            for match in matches:
                print(f"   - {match['home']} vs {match['away']} at {match['kickoff']}")
            print()  # Spacing between leagues


def main():
    today = date.today().isoformat()
    api = FootballAPI()

    try:
        fixtures = api.get_fixtures_by_date(today)
        api.display_fixtures(fixtures, today)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
