# Motor Racing Info

CLI program to track information about various motor racing series, such as the teams, drivers, engine manufacturers, and championship standings.

Current implementation includes the Formula One 2023 Championship.

## Glossary of Terms

*This glossary is listed in no particular order.*

**Formula One** / **Formula 1** / **F1**
An international motor racing series featuring open wheel racing. Currently, Formula One races are only street circuits or road courses. Famous Formula One drivers include Michael Schumacher, Lewis Hamilton, Max Verstappen, Fernando Alonso, and Sebastian Vettel.

**Formula Two** / **Formula 2** / **F2**
A junior series of Formula One. Similar to the relationship between Minor League Baseball and Major League Baseball.

**Formula E**
The electric vehicle open wheel racing series governed by the FIA.

**FIA** / **Fédération Internationale de l'Automobile**
The governing body of Formula One, and other related motor-racing series like Formula Two and Formula E.

**IndyCar**
A series of open wheel racing based in the United States. Most race are in the United States, although drivers come from a variety of countries. The points and team structures of IndyCar are very different from the system used by Formula One. IndyCar tracks can be ovals, street circuits, or road courses.

**Open Wheel Racing**
A type of vehicle in which the wheels are exposed. If you've seen Cars 2, think of the Italian race-car. Open wheel racing series include Formula One and IndyCar. This is in contrast to series like Nascar, in which the cars look very similar to regular street cars.

## Usage

### Install required packages

`pip3 install -r requirements.txt`

### Run unit tests

`pytest tests`

### Run the main program

`python3 main.py`

## Future Versions

* include Team Principals as an attribute of a Team
* add other FIA series like Formula 2 and Formula E
* differentiate between reserve/test drivers and full-time drivers
* add support for IndyCar type series
    * add support for calculating standings using IndyCar's points system