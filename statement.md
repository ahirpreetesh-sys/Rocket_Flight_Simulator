

# Problem Statement
- The goal of this project is to build a 2D numerical flight simulation script in Python to model a model rocket trajectory. Instead of relying on oversimplified physics, the script uses discrete numerical integration to calculate realistic rocket dynamics over time.The simulation accurately accounts for several competing physical forces and changing variables:
- Dynamic Mass Reduction: The rocket gets lighter over time as it burns through fuel.
- Thrust and Aerodynamics: Models variable thrust vectors alongside a constant aerodynamic drag.
- Environmental Forces: Continuous calculation of gravitational pull acting on the rocket.
- As the simulation runs, it generates a step-by-step, it store value like altitude, downrange displacement, speed, and time. The program runs continuously until it again come at y=0 time threshold or encounters a crash event..

# Scope
## In-Scope1D & 2D
- Launch Physics: Accurate handling of vertical or angled launches using basic trigonometry .
- Mass Variances: Live tracking of decaying total mass as a function of the fuel burn rate over the declared burn time.
- Environmental Forces: Dynamic calculation of aerodynamic drag forces based on surface cross-sectional area, drag coefficients, air density.
- Vectorized Decompositions: Resolution of net acceleration in horizontal and vertical planes.
## Out-of-Scope3D
- Trajectory & Wind Vectors: Side-winds, wind shears, and rotational movements are excluded.
- Dynamic Altitudinal Mechanics: Atmospheric density (rho) is treated as a fixed sea-level constant (1.2 kg/m³) rather than a gradient scale that drops off with altitude.
- Advanced Integration Methods: High-precision solvers (e.g., Runge-Kutta RK4) are outside the core implementation; calculations strictly use standard dt interval Euler integration steps.
# Target Users
- Physics & Aerospace Students: Individuals looking to understand how thrust, mass loss, gravity, and drag interact in flight mechanics.
- Hobbyist Rocketry Enthusiasts: Amateur rocketeers seeking a swift, code-accessible baseline tool to predict their model rocket’s performance criteria before flight tests.
- Coding Instructors & Beginners: Educators searching for real-world programmatic execution examples showcasing math applications, loops, and conditional structures

# High-Level Features
- Interactive Parameter Initialization: Allows users to input customized rocket structural constraints (dry mass, fuel mass, thrust capability, burn duration and launch angles).
- Dynamic Flight State Machine: Evaluates conditions sequentially for operational stages like powered flight (active thrust) and unpowered coasting (ballistic arc after fuel depletion).
- Auto-Adjusting Pitch Profiling: Reorientates thrust vectors and drag dynamics natively based on actual direction vectors (atan2 calculations of directional velocity).
- Smart Throttled Logging: Built-in modulo check logic ensures terminal streams print clean telemetry data rows at readable time intervals instead of overflowing the console.
- Automated Crash Stop Safeguard: Active terrain intersection logic checks if the altitude falls below zero after launch, providing a crash warning and preventing infinite negative-loop calculations
- Mission management
- Trajectory simulation
- Visualization
- Report generation
- Automated testing
## Architectural Trade-offs & Limitations
- Velocity Reference Error: The script derives the current loop's drag from the previous loop's acceleration array profile (VMg = math.sqrt(ax**2+ay**2) instead of referencing instantaneous scalar velocity arrays), For steep acceleration curves, this creates minor drift errors.

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
