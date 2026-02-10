# Problem Statement
# Create a program for an Instagram Account System using Encapsulation.
# Requirements
# Create a class named InstagramAccount
# Public Variable
# account_name
# Protected Variable
# _private_reels (list of strings)
# Private Variable
# __archived_reels (list of strings)
# Methods to Implement
# 1. add_private_reel(reel_name)
# Adds a reel into _private_reels
# 2. display_private_reels(is_follower)
# If is_follower is True → display all private reels
# Else → print "Access Denied! Only followers can view private reels"
# 3. add_archived_reel(reel_name)
# Adds a reel into __archived_reels
# 4. display_archived_reels(password)
# If password is correct → display all archived reels
# Else → print "Access Denied! Only account holder can view archived reels"
#5. getter method for archived reels
#Create a getter method to return archived reels only if password is correct
#6. setter method to update password
#Create a setter method to update password
#Task
#Create one object of InstagramAccount
#Add at least 2 private reels
#Add at least 2 archived reels
#Display private reels as follower and non-follower
#Display archived reels using correct and wrong password
#Update password using setter and check again
#Push the code to github.


class InstagramAccount:
    # Public Variable
    account_name = ""

    def __init__(self, account_name, password):
        self.account_name = account_name
        
        # Protected Variable
        self._private_reels = []
        
        # Private Variable
        self.__archived_reels = []
        
        # Private password
        self.__password = password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")

    # 2. Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels.")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")

    # 4. Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels.")

    # 5. Getter for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Wrong password."

    # 6. Setter to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Wrong old password. Cannot update password.")


# ------------------ TASK EXECUTION ------------------

insta = InstagramAccount("my_insta_account", "1234")

# Add private reels
insta.add_private_reel("Vacation Reel")
insta.add_private_reel("Birthday Party Reel")

# Add archived reels
insta.add_archived_reel("Old Travel Reel")
insta.add_archived_reel("College Memories Reel")

print("\n---- Private Reels (Follower) ----")
insta.display_private_reels(True)

print("\n---- Private Reels (Non-Follower) ----")
insta.display_private_reels(False)

print("\n---- Archived Reels (Wrong Password) ----")
insta.display_archived_reels("0000")

print("\n---- Archived Reels (Correct Password) ----")
insta.display_archived_reels("1234")

print("\n---- Getter Method Test ----")
print(insta.get_archived_reels("1234"))

print("\n---- Update Password ----")
insta.set_password("1234", "9999")

print("\n---- Archived Reels After Password Change ----")
insta.display_archived_reels("9999")
