from math import ceil


class WinDoor:
    def __init__(self, height, width, name: str):
        self.height = height
        self.width = width
        self.name = name
        self.squareWD = self.square()

    def square(self):
        self.squareWD = self.height * self.width
        return self.squareWD

    def __repr__(self):
        return f"{self.name}: {self.height}x{self.width}"


class Room:

    def __init__(self, height, width_1, width_2):
        self.square_wall = 2 * height * (width_1 + width_2)
        self.height = height
        self.width_1 = width_1
        self.width_2 = width_2
        self.square_room = self.square_room()
        self.wd = []

    def addWD(self, height, width, name: str):
        self.wd.append(WinDoor(height, width, name))

    def workSurface(self):
        total_square_wall = self.square_wall
        for i in self.wd:
            total_square_wall -= i.squareWD
        return total_square_wall

    def square_room(self):
        self.square_room = self.width_1 * self.width_2
        return self.square_room

    def roll_wallpaper(self, width, length):
        self.total_roll = ceil(self.workSurface() / (width * length))
        return self.total_roll


class Interface:
    def __init__(self):
        self.room = Room(
            float(input("Enter height your room: ")),
            float(input("Enter length first wall: ")),
            float(input("Enter length second wall: "))
        )
        self.addwindoor = self.wd()
        self.square_surface = self.room.workSurface()
        self.roll_wallpaper = self.roll_paper()

    def wd(self):
        window = int(input("Enter the number of windows (if not, enter a zero): "))
        door = int(input("Enter the number of doors (if not, enter a zero): "))
        if window > 0:
            for i in range(window):
                self.room.addWD(
                    float(input(f"Window {i + 1}.\tEnter the window height: ")),
                    float(input("\t\tEnter the window width: ")),
                    input("\t\tEnter the window name: ")
                )
        if door > 0:
            for i in range(door):
                self.room.addWD(
                    float(input(f"Door {i + 1}.\t\tEnter the door height: ")),
                    float(input("\t\tEnter the door width: ")),
                    input("\t\tEnter the door name: ")
                )

    def roll_paper(self):
        return self.room.roll_wallpaper(
            float(input("Enter the width of the wallpaper: ")),
            float(input("Enter the length of the wallpaper: "))
        )

    def __repr__(self):
        return str(
            f"***\nYour room square: {self.room.square_room} м²"
            f"\nYour work surface: {self.square_surface} м²"
            f"\nNumber of wallpaper rolls: {self.roll_wallpaper}\n***"
                   )


start_interface = Interface()
print(start_interface)
