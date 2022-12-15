from world import World
from corrupted_save_file_error import CorruptedSaveFileError
from planet import Planet

class LoadSaveIO(object):

    def load_save(self, input):

        self.world = World()
        info_read = False
        next_line = ''

        try:
            # Read the file header and the save date
            line = input.readline()
            header_parts = line.split(" ")
            # Process the data we just read.
            if header_parts[0] != "INT":
                raise CorruptedSaveFileError("Unknown file type")

            if header_parts[2].strip().lower() != 'savefile':
                raise CorruptedSaveFileError("Unknown file type")
            info_read = True


            while True:
                line = input.readline()

                line = line.lower()
                line = line.strip()
                line = line.rstrip("\n")

                # looking into the #World chunk
                if line == "#world":
                    line = input.readline()
                    while line[:1] != "#" and line != "":
                        if line.startswith("Saved"):
                            line = line.split(":")
                            self.world.set_save(line[1])

                        elif line.startswith("Stars"):
                            line = line.split(":")
                            self.world.set_stars(line[1])

                        elif line.startswith("Planets"):
                            line = line.split(":")
                            self.world.set_pl_amount(line[1])

                        line = input.readline()
                        line = line.strip()


                elif line == "#bdy":
                    line = input.readline()
                    while line != "#BDYEND":
                        if line.startswith("PLN"):
                            p_number = line[3:]
                            line = input.readline()
                            planeg = Planet()
                            while line[:1] != "PLEND" and line != "":
                                if line.startswith("N"):
                                    line = line.strip()
                                    line = line.split(":")
                                    planeg.set_name(line[1])

                                elif line.startswith("R"):
                                    line = line.split(":")
                                    planeg.conv_set_radius(line[1])

                                elif line.startswith("M"):
                                    line = line.split(":")
                                    planeg.conv_set_mass(line[1])

                                elif line.startswith("G"):
                                    line = line.split(":")
                                    planeg.set_gravity(line[1])

                                elif line.startswith("L"):
                                    line = line.split(":")
                                    loc = line[1].split(",")
                                    planeg.conv_set_location(loc[0],loc[1], loc[2])

                                elif line.startswith("V"):
                                    line = line.split(":")
                                    vel = line[1].split(",")
                                    planeg.conv_set_velocity(vel[0], vel[1], vel[2])

                                elif line.startswith("C"):
                                    line = line.split(":")
                                    planeg.set_color(line[1])

                                line = input.readline()
                                line = line.strip()

                            self.world.add_planet(planeg)


                        line = input.readline()
                        line = line.strip()


                elif line == "#end000":

                    break


            # *************************************************************
            return self.world

        except OSError:

            raise CorruptedSaveFileError("Reading the save data failed.")

