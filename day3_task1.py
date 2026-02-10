# Problem Statement
# Create a program for a Smartphone System using Multiple Inheritance.
# Requirements
# Create a class Camera
# attribute: camera_quality
# method: display_camera_details()
# Create a class MusicPlayer
# attribute: sound_quality
# method: display_music_details()
# Create a child class SmartPhone that inherits from both Camera and MusicPlayer
# attribute: brand
# method: display_smartphone_details()
# Create one object of SmartPhone and display all details.


# Parent class 1
class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


# Parent class 2
class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


# Child class using Multiple Inheritance
class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        self.brand = brand
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)

    def display_smartphone_details(self):
        print("Smartphone Brand:", self.brand)


# Create object
phone = SmartPhone("Samsung", "64MP", "Dolby Atmos")

# Display all details
phone.display_smartphone_details()
phone.display_camera_details()
phone.display_music_details()