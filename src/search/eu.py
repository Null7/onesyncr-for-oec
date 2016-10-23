import csv
import oec


# Global dictionary for all systems.
SYSTEMS = {}


def add_system(name, row):
    # Create new System object.
    system = oec.System(name)

    # declination
    system._declination = oec.deg_to_dms(row["dec"])
    
    # rightascension
    system._rightascension = oec.deg_to_hms(row["ra"])

    # distance & error -/+
    system._distance = [row["star_distance"],
                        row["star_distance_error_min"],
                        row["star_distance_error_max"]]
    
    # epoch????


    SYSTEMS[name] = system



def add_star(system, row):
    star_name = row["star_name"]

    star = oec.Star(star_name)
    # alternate names
    star_alt_names = row["star_alternate_names"].split(",")
    
    if "" in star_alt_names: star_alt_names.remove("")
    star._names.union(set(star_alt_names))

    # mass
    star._mass = [row["star_mass"],
                  row["star_mass_error_min"],
                  row["star_mass_error_max"]]

    # radius
    star._radius = [row["star_radius"],
                  row["star_radius_error_min"],
                  row["star_radius_error_max"]]

    # temperature
    star._temperature = [row["star_teff"],
                  row["star_teff_error_min"],
                  row["star_teff_error_max"]]

    # age
    star._age = [row["star_age"],
                  row["star_age_error_min"],
                  row["star_age_error_max"]]

    # metallicity
    star._metallicity = [row["star_metallicity"],
                  row["star_metallicity_error_min"],
                  row["star_metallicity_error_max"]]

    # spectraltype ???
    star._spectraltype = []

    # magB, magV, magR, magI, magJ, magH, magK
    # missing magB and magR
    star._magV = row["mag_v"]
    star._magI = row["mag_i"]
    star._magJ = row["mag_j"]
    star._magH = row["mag_h"]
    star._magK = row["mag_k"]

    # Add star into System.
    system._stars[star_name] = star


def add_planet(system, row):
    planet_name = row["# name"]

    planet = oec.Planet(planet_name)
    planet_alt_names = row["alternate_names"].split(",")

    if "" in planet_alt_names: planet_alt_names.remove("")
    planet._names.union(set(planet_alt_names))
    
    # mass
    planet._mass = [row["mass"],
                    row["mass_error_min"],
                    row["mass_error_max"]]

    # radius
    planet._radius = [row["radius"],
                      row["radius_error_min"],
                      row["radius_error_max"]]
    
    # temperature
    
    # age
    
    # spectraltype

    # semimajoraxis
    planet._semimajoraxix = [row["semi_major_axis"],
                             row["semi_major_axis_min"],
                             row["semi_major_axis_max"]]

    # seperation
    
    # eccentricity
    planet._eccentricity = [row["eccentricity"],
                            row["eccentricity_error_min"],
                            row["eccentricity_error_max"]]
    
    # periastron
    planet._periastron = [row["omega"],
                          row["omega_error_min"],
                          row["omega_error_max"]]
    
    # longitude
    
    # meananomaly
    
    # ascendingnode
    
    # inclination
    planet._inclination = [row["inclination"],
                           row["inclination_error_min"],
                           row["inclination_error_max"]]
    
    # impactperameter
    
    # period
    planet._period = [row["orbital_period"],
                      row["orbital_period_error_min"],
                      row["orbital_period_error_max"]]
    
    # periastrontime
    planet._periastrontime = [row["tperi"],
                              row["tperi_error_min"],
                              row["tperi_error_max"]]
    
    # maximumrvtime
    
    # discoverymethod
    
    # istransiting
    
    # description
    
    # discoveryyear
    planet._discoveryyear = row["discovered"]
    
    # lastupdate
    planet._lastupdate = row["updated"]
    
    # spinorbitalalignment

# Call dlcsv to download csvs

csvfile = open('tmp/eu.csv')
reader = csv.DictReader(csvfile)


for row in reader:
    system_name = row["star_name"]
    star_name = row["star_name"]
    planet_name = row["# name"]

    # Create new system if system does not exit.
    if system_name not in SYSTEMS:
        add_system(system_name, row)

    # Create new star if star does not exit.    
    if star_name not in SYSTEMS[system_name]._stars:
        add_star(SYSTEMS[system_name], row)
    
    
    # Create new planet.
    add_planet(SYSTEMS[system_name], row)

    a = (row.keys())
    if row["# name"] == "Kepler-152 b":
        break


for k, v in row.items():
    print(k, "+++++++++++++++++",  v)
    
