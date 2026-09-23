# Project Statement

## Problem Statement
Rocket analysis combines physics, numerical computation, data management, visualization, and reporting. This project provides one Python application that accepts mission parameters, stores them, calculates idealized trajectory characteristics, estimates propulsion requirements, and presents the results in useful reports and graphs.

## Scope
The project includes:
- Mission data entry
- Create/read/update/delete operations
- SQLite storage
- CSV import
- Ideal 2D trajectory simulation
- Flight-time, altitude, range, and impact-speed calculations
- Tsiolkovsky delta-v and propellant calculations
- Visualization
- Text reporting
- Automated tests

It does not model real launch operations, detailed propulsion systems, atmospheric drag, staging, guidance, structural constraints, or safety-critical aerospace behavior.

## Target Users
- Python students
- Introductory physics students
- Simulation/numerical-computing students
- Instructors demonstrating CRUD and database concepts
- Beginners learning SQLite, NumPy, and Matplotlib

## High-Level Features
1. Mission management
2. Trajectory simulation
3. Fuel/delta-v analysis
4. SQLite database
5. CSV data import
6. Visualization
7. Report generation
8. Automated testing

## Non-Functional Requirements
### Performance
Normal CRUD and simulation operations should complete quickly on a standard student computer.

### Reliability
Invalid inputs should be rejected with clear messages and SQL queries should be parameterized.

### Maintainability
Calculations, database access, models, reporting, and CLI behavior are separated into modules.

### Usability
The CLI provides understandable menus and prompts.

### Portability
The application should run on Windows, Linux, and macOS with Python 3.10+.

### Testability
Core calculations and database operations are covered by pytest tests.
