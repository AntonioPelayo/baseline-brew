# Coffee Canary
Dashboard for monitoring coffee purchase metrics and trends.

## Run (Local dev, no Docker)
1. Copy `.env.example` to `.env` and fill values.
2. Start the app:
   - Dev (auto reload): `bin/build_local.sh -d`
   - Prod test (Gunicorn): `bin/build_local.sh`
3. Access the app at `http://127.0.0.1:8050`

## Data sources
- coffee_canary.db (SQLite)
- CSV fallback

## Project structure
```
coffee-canary/
├── bin/                        # Build and run scripts
├── data/                       # CSV and .db data files
└── src/
    ├── assets/                 # CSS and static assets
    │   └── images/             # Image assets
    ├── db/                     # Database handlers
    ├── pages/                  # Web app pages
    │   ├── brew_tools.py       # Coffee brewing equipment
    │   ├── coffee_beans.py     # Purchase trends and metrics dashboard
    │   └── index.py            # Home page
    └── utils/
    │   ├── data_helpers.py     # Dataframe loading and processing
    │   ├── db.py               # Database connection and queries
    │   ├── google_maps_api.py  # Google Maps API integration
    │   └── plots.py            # Plotting functions
    │── app.py                  # Main application
    └── config.py               # Configuration settings
```
