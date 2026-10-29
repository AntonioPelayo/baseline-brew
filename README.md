# Baseline Brew
Dashboard for monitoring my coffee purchase trends.

Built with Python, Plotly Dash, and Pandas, web service hosted on Render.com.

[https://baseline-brew.apelayo.com](https://baseline-brew.apelayo.com)

## Run (Local dev, no Docker)
1. Copy `.env.example` to `.env` and fill values.
2. Start the app:
   - Dev (auto reload): `bin/build_local.sh -d`
   - Prod test (Gunicorn): `bin/build_local.sh`
3. Access the app at `http://127.0.0.1:8050`

## Data sources
- `data/coffee_beans.csv` — coffee purchases
- `data/coffee_roasters.csv` — roaster locations

## Project structure
```
baseline-brew/
├── bin/                        # Build and run scripts
├── data/                       # CSV data files
└── src/
    ├── assets/                 # CSS and static assets
    │   └── images/             # Image assets
    ├── pages/                  # Web app pages
    │   ├── brew_tools.py       # Coffee brewing equipment
    │   ├── coffee_beans.py     # Purchase trends and metrics dashboard
    │   └── index.py            # Home page
    └── utils/
    │   ├── columns.py          # CSV column name constants
    │   ├── data_helpers.py     # CSV loading into DataFrames
    │   ├── google_maps_api.py  # Google Maps API integration
    │   └── plots.py            # Plotting functions
    │── app.py                  # Main application
    └── config.py               # Configuration settings
```
