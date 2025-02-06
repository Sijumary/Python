from typing import Tuple
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation
from matplotlib.lines import Line2D
from tqdm import trange

G = 6.673e-11          # Gravitational constant
AU = 1.496e11          # Astronomical unit in KM
Year = 365*24*60*60.0  # Seconds in one year
MM = 6e24              # Normalising mass
ME = 6e24/MM           # Normalized mass of earth
MS = 2e30/MM           # Normalized mass of Sun
MJ = 500*1.9e27/MM     # Normalized mass of Jupiter 
GG = (MM*G*Year**2)/(AU**3) # Gravitational constant for simulation

# function to calculate gravitational force
def gravitational_force(m1:float, m2: float, r: np.ndarray) -> np.ndarray:

    F_mag = GG*m1*m2/(np.linalg.norm(r) + 1e-20)
    theta = np.arctan2(np.abs(r[1]), np.abs(r[0]) + 1e-20)
    F = F_mag * np.array([np.cos(theta), np.sin(theta)])
    F *= -np.sign(r)
    return F

    #RK4 solver (Runge-Kutta 4th order solver to solve the differential equations of mothon)
    # RK4 Solver
def RK4Solver(t: float, r: np.ndarray, v: np.ndarray, h: float, planet: str, r_other: np.ndarray, v_other: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    
    def dr_dt(v: np.ndarray) -> np.ndarray:
        return v

    def dv_dt(r: np.ndarray, planet: str) -> np.ndarray:
        if planet == 'earth':
            return (gravitational_force(ME, MS, r) + gravitational_force(ME, MJ, r - r_other)) / ME
        elif planet == 'jupiter':
            return (gravitational_force(MJ, MS, r) - gravitational_force(MJ, ME, r - r_other)) / MJ

    k11 = dr_dt(v)
    k21 = dv_dt(r, planet)

    k12 = dr_dt(v + 0.5 * h * k21)
    k22 = dv_dt(r + 0.5 * h * k11, planet)

    k13 = dr_dt(v + 0.5 * h * k22)
    k23 = dv_dt(r + 0.5 * h * k12, planet)

    k14 = dr_dt(v + h * k23)
    k24 = dv_dt(r + h * k13, planet)

    y0 = r + h * (k11 + 2 * k12 + 2 * k13 + k14) / 6
    y1 = v + h * (k21 + 2 * k22 + 2 * k23 + k24) / 6

    return y0, y1

# Setup animation
def setup_animation() -> Tuple[py.Figure, py.Axes, Line2D, Line2D, py.Text]:

    # Creating a Plot Figure and Axes
    fig, ax = py.subplots()

    # Setting Axes Limits and Ticks
    ax.axis('square')
    ax.set_xlim((-7.2, 7.2))
    ax.set_ylim((-7.2, 7.2))
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

    # Plotting the Sun
    ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813",
            markeredgecolor="#FD7813")

    # Initializing Lines for Earth and Jupiter
    line_earth, = ax.plot([], [], 'o-', color='#d2eeff',
                          markevery=10000, markerfacecolor='#0077BE', lw=2)
    line_jupiter, = ax.plot([], [], 'o-', color='#e3dccb', markersize=8,
                            markerfacecolor='#f66338', lw=2, markevery=10000)
    # Adding a Text Object
    ttl = ax.text(0.24, 1.05, '', transform=ax.transAxes, va='center')

    # Returning Components
    return fig, ax, line_earth, line_jupiter, ttl

# Animation function
def animate(i: int) -> Tuple[Line2D, Line2D, py.Text]:

    earth_trail, jupiter_trail = 40, 200
    tm_yr = 'Elapsed time = ' + str(round(t[i], 1)) + ' years'
    ttl.set_text(tm_yr)
    line_earth.set_data(r[i:max(1, i - earth_trail):-1, 0],
                        r[i:max(1, i - earth_trail):-1, 1])
    line_jupiter.set_data(r_jupiter[i:max(
        1, i - jupiter_trail):-1, 0], r_jupiter[i:max(1, i - jupiter_trail):-1, 1])
    return line_earth, line_jupiter, ttl

# Initialization
ti, tf = 0, 120  # Initial and final time in years
N = 100 * tf     # 100 points per year
t = np.linspace(ti, tf, N)  # Time array
h = t[1] - t[0]  # Time step

# Position and Velocity Initialization
r = np.zeros([N, 2])         # Position of Earth
v = np.zeros([N, 2])         # Velocity of Earth
r_jupiter = np.zeros([N, 2])  # Position of Jupiter
v_jupiter = np.zeros([N, 2])  # Velocity of Jupiter

# Initial Conditions
r[0] = [1496e8 / AU, 0]
r_jupiter[0] = [5.2, 0]
v[0] = [0, np.sqrt(MS * GG / r[0, 0])]
v_jupiter[0] = [0, 13.06e3 * Year / AU]

# Running the simulation
for i in trange(N - 1, desc="Generating Animation"):
    r[i + 1], v[i + 1] = RK4Solver(t[i], r[i],
                                   v[i], h, 'earth', r_jupiter[i], v_jupiter[i])
    r_jupiter[i + 1], v_jupiter[i +
                                1] = RK4Solver(t[i], r_jupiter[i], v_jupiter[i], h, 'jupiter', r[i], v[i])

# Setting Up the Animation
fig, ax, line_earth, line_jupiter, ttl = setup_animation()
# Adding Scale and Labels
ax.plot([-6,-5],[6.5,6.5],'r-')
ax.text(-4.5,6.3,r'1 AU = $1.496 \times 10^8$ km')

ax.plot(-6,-6.2,'o', color = '#d2eeff', markerfacecolor = '#0077BE')
ax.text(-5.5,-6.4,'Earth')

ax.plot(-3.3,-6.2,'o', color = '#e3dccb',markersize = 8, markerfacecolor = '#f66338')
ax.text(-2.9,-6.4,'Super Jupiter (500x mass)')

ax.plot(5,-6.2,'o', markersize = 9, markerfacecolor = "#FDB813",markeredgecolor ="#FD7813")
ax.text(5.5,-6.4,'Sun')

# Creating the Animation
anim = animation.FuncAnimation(
    fig, animate, frames=4000, interval=1, blit=False)

# Displaying the Animation
plt.show()
