# ⚽ Football Fixtures API (API-Football)
This is a Python-based CLI tool that fetches and displays **daily football fixtures** from the [API-Football](https://www.api-football.com/) service.  It groups the fixture by various league type and displays them in the terminal.

## 🚀 Features
- Fetches today's football fixtures using API-Football
- Displays fixtures grouped by league
- Uses a clean, Object-Oriented Programming (OOP) structure
- Fully configurable via `.env` file

## 🛠️ Requirements
- Python 3.8+
- [API-Football](https://v3.football.api-sports.io/) API key

## 📦 Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/football-fixtures-api.git
   cd football-fixtures-api
````
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file**:

   Create a `.env` file in the project root:

   ```
   API_KEY=your_api_football_key_here
   ```

---

## ▶️ Usage

Run the script using:

```bash
python main.py
```

This will display today's fixtures grouped by league:

```
📅 Fixtures for 2025-07-16:

🏆 Premier League
   - Arsenal vs Chelsea at 2025-07-16T17:30:00+00:00

🏆 Serie A
   - Napoli vs AC Milan at 2025-07-16T20:45:00+00:00
```

## 🧰 Project Structure

```
football-fixtures-fetcher/
│
├── main.py              # Main script
├── .env                 # API key (not committed to Git)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 📌 Future Improvements

* Add CLI date input (e.g. `--date 2025-07-20`)
* Support filtering by league or team
* Export results to JSON or CSV
* Add unit tests


## 🤝 Acknowledgments

* [API-Football](https://v3.football.api-sports.io/) — for providing reliable football data
