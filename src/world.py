from math import sqrt

from planet import Planet


class World(object):
    '''
    The class describes a world that the heavenly bodies inhabit.
    '''
    def __init__(self):
        #self.__name = name
        self._stars = None
        self._save = None
        self._pl_amount = None
        self._planets = []


    def update_all(self):
        '''
        Method to update all of the data for each planet stored in the world.
        Iterates the list of planet objects, and for each planet calculates the forces on it.
        Then updates the new velocity for the planet.Finally updates the location of that planet after 1 day.
        --> repeat for next planet in the world.
        '''
        for planet in self._planets:
            self.calc_force(planet)
            self.update_vel(planet)
            self.update_loca(planet)

    def update_loca(self, p):
        '''
        updates the location of each planet after elapsed time
        Distance and speed in [m] and [m/s]
        t = 1d = 60*60*24s
        '''
        t = float(60*60*24)
        x = p.x_loca + (p.x_vel * t)
        y = p.y_loca + (p.y_vel * t)
        z = p.z_loca + (p.z_vel * t)
        p.set_location(x, y, z)

    def update_vel(self, p):
        '''
        updates the velocity of each planet after elapsed time
        Keeps the distances in km and time in days,
        since the data of location and velocity is already stored as [km] and [km/d]
        F = ma --> a = F/m
        V = V0 + at --> V = V0 + F/m * t
        t = 1d = 60*60*24s
        '''
        t = float(60*60*24)
        vx = (p.x_vel) + ((p.fx / p.mass) * t)
        vy = (p.y_vel) + ((p.fy / p.mass) * t)
        vz = (p.z_vel) + ((p.fz / p.mass) * t)
        p.set_velocity(vx, vy, vz)


    def calc_force(self, p):
        '''
        Algorithm to calculate all forces applied on a specific planet p.
        Based on all of the other planets in the world.
        Distance and speed in [m] and [m/s]
        G is the gravitational constant from Newtons law of gravity.
        Sets the forces in each dimension for each planet (negative since opposite of planet).
        dx(y,z) is the distance between the two objects in the x-dimension.
        d is the total distance between the two dimensions calculated as the abs() of a vector.
        '''
        G = float(6.675 * 10.0**-11.0)
        fx = 0
        fy = 0
        fz = 0

        for planet in self._planets:
            if not planet == p:
                dx = (p.x_loca - planet.x_loca)
                dy = (p.y_loca - planet.y_loca)
                dz = (p.z_loca - planet.z_loca)
                d = sqrt(dx**2.0 + dy**2.0 + dz**2.0)

                fx += dx * (G * planet.mass * p.mass) / (d ** 3.0)
                fy += dy * (G * planet.mass * p.mass) / (d ** 3.0)
                fz += dz * (G * planet.mass * p.mass) / (d ** 3.0)
        p.set_force(-fx, -fy, -fz)



    def add_planet(self, planet):
        self._planets.append(planet)
    def get_planets(self):
        return self._planets

    def set_pl_amount(self, amount):
        self._pl_amount = amount
    def add_pl_amount(self):
        self._pl_amount += 1
    def get_pl_amount(self):
        return self._pl_amount

    def set_stars(self, star_amt):
        self._stars = star_amt
    def get_stars(self):
        return self._stars

    def set_save(self, date):
        self._save = date
    def get_save(self):
        return self._save
