

class Planet():

    def __init__(self):
        self.name = None
        self.radius = None
        self.mass = None
        self.gravity = None
        self.color = None

        self.x_loca = None
        self.y_loca = None
        self.z_loca = None

        self.x_vel = None
        self.y_vel = None
        self.z_vel = None

        self.fx = None
        self.fy = None
        self.fz = None


    def set_force(self, x, y, z):
        self.fx = x
        self.fy = y
        self.fz = z

    #methods for name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    #methods for radius
    def conv_set_radius(self, radius):
        self.radius = float(radius) * 1000

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    #methods for mass
    def conv_set_mass(self, mass):
        mass_factor = 10.0**24
        self.mass = float(mass) * mass_factor

    def set_mass(self, mass):
        self.mass = mass

    def get_mass(self):
        return self.mass


    #methods for gravitational constants for planets
    def set_gravity(self, gravity):
        self.gravity = float(gravity)

    def get_gravity(self):
        return self.gravity

    #meethods for color
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    #methods for locations
    def conv_set_location(self,x, y, z):
        self.x_loca = float(x) * 1000
        self.y_loca = float(y) * 1000
        self.z_loca = float(z) * 1000

    def set_location(self, x, y, z):
        self.x_loca = x
        self.y_loca = y
        self.z_loca = z


    #methods for velocity
    def conv_set_velocity(self, x, y, z):
        self.x_vel = float(x) * 0.01157
        self.y_vel = float(y) * 0.01157
        self.z_vel = float(z) * 0.01157

    def set_velocity(self, x, y, z):
        self.x_vel = x
        self.y_vel = y
        self.z_vel = z


