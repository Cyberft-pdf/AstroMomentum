import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Konstanty
speed_of_light = 3e8  # Rychlost světla v metrech za sekundu
source_frequency = 5e14  # Frekvence záření zdroje v Hz
observer_speed = 2e7  # Rychlost pozorovatele v metrech za sekundu
distance = 1e9  # Vzdálenost mezi zdrojem a pozorovatelem v metrech

# Funkce pro výpočet Dopplerova jevu
def doppler_shift(frequency, speed, distance):
    return frequency * (speed_of_light + speed) / (speed_of_light + speed - (speed * distance / (speed_of_light + speed)))

# Inicializace grafu
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(4.9e14, 5.1e14)
line, = ax.plot([], [], lw=2)

# Funkce inicializace animace
def init():
    line.set_data([], [])
    return line,

# Funkce aktualizace animace
def update(frame):
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(4.9e14, 5.1e14)

    # Vypočítat Dopplerův jev pro každý snímek
    shifted_frequency = doppler_shift(source_frequency, observer_speed, distance * frame)

    # Zobrazit záznamy o frekvencích
    ax.text(0.5, 0.9, f'Zdrojová frekvence: {source_frequency / 1e14} THz', transform=ax.transAxes, fontsize=10, verticalalignment='top')
    ax.text(0.5, 0.85, f'Frekvence s Dopplerovým jevem: {shifted_frequency / 1e14:.2f} THz', transform=ax.transAxes, fontsize=10, verticalalignment='top')

    line.set_data([frame, frame], [source_frequency, shifted_frequency])
    return line,

# Vytvoření animace
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), init_func=init, blit=True)

plt.title('Dopplerův jev ve vesmíru')
plt.xlabel('Vzdálenost (milióny kilometrů)')
plt.ylabel('Frekvence (Hz)')
plt.show()
