# Rocket Trajectory & Fuel Analyzer

A modular Python project for educational analysis of rocket mission parameters, idealized trajectory simulation, fuel/delta-v calculations, SQLite CRUD operations, visualization, reporting, CSV import, and automated tests.

> **Educational simulator:** This project uses simplified physics. It is not a real launch-vehicle design or flight-planning tool.

## Features
- Mission CRUD operations
- SQLite persistence
- CSV sample-data import
- Ideal 2D trajectory simulation
- Maximum altitude, range, flight-time, and impact-speed calculations
- Tsiolkovsky rocket-equation delta-v and propellant calculations
- Matplotlib trajectory plots
- Text mission reports
- Automated pytest tests
- Command-line interface

## Structure
```text
rocket-trajectory-fuel-analyzer/
├── README.md
├── statement.md
├── requirements.txt
├── data/missions.csv
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── database.py
│   ├── fuel_calculator.py
│   ├── trajectory.py
│   ├── analyzer.py
│   ├── reporting.py
│   └── cli.py
├── main.py
└── tests/
    ├── __init__.py
    ├── test_fuel_calculator.py
    ├── test_trajectory.py
    ├── test_database.py
    └── test_analyzer.py
```

## Installation
Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

The CLI supports adding, listing, analyzing, updating, deleting, and importing missions.

## Import sample data
Choose **Import CSV** in the application and enter:
```text
data/missions.csv
```

## Testing
```bash
pytest -q
```

## Physics model

For launch speed `v`, angle `theta`, and gravity `g`:

- `x = v*cos(theta)*t`
- `y = v*sin(theta)*t - 0.5*g*t^2`
- `T = 2*v*sin(theta)/g`
- `H = v^2*sin(theta)^2/(2*g)`
- `R = v^2*sin(2*theta)/g`

Fuel analysis uses:

`delta-v = Isp*g0*ln(m0/mf)`

These calculations assume constant gravity, no atmospheric drag, a flat Earth, and an instantaneous launch velocity.

## Screenshots
After running the project, screenshots can be added under `screenshots/`:

```markdown
![CLI](screenshots/cli.png)
![Trajectory](screenshots/trajectory.png)
```

## Limitations
The model does not include drag, variable gravity, Earth's rotation, staging, engine thrust curves, structural constraints, guidance, or detailed atmospheric effects. Results are for coursework and software demonstrations only.
