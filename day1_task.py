# Class and object
# For the Given code add the comments, Creator_name, Location and their display methods . Note comments should be a list of strings.

class Instagram:
    def __init__(self, title, description, creator_name, location):
        # Initializing reel details
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []    # List of comments (strings)

    # Display title of the reel
    def display_title(self):  
        print("The title of the reel is:", self.title)

    # Display description of the reel
    def display_description(self):
        print("The description of the reel is:", self.description)

    # Display creator name
    def display_creator(self):
        print("The creator of the reel is:", self.creator_name)

    # Display location
    def display_location(self):
        print("The location of the reel is:", self.location)

    # Display likes count
    def display_likes(self):
        print("The likes of the reel is:", self.likes)

    # Add like
    def liked(self):
        self.likes += 1

    # Remove like
    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    # Add a comment
    def add_comment(self, comment):
        self.comments.append(comment)

    # Display all comments
    def display_comments(self):
        print("Comments on the reel:")
        for comment in self.comments:
            print("-", comment)

    #Delete last comment method
    def delete_comment(self):
        if self.comments:
            self.comments.pop()
        

# Creating objects
reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "Moulya",
    "Bangalore"
)

reel2 = Instagram(
    "finance minister conference",
    "finance minister conference with friends",
    "Amulya",
    "Delhi"
)

# Performing operations
reel1.disliked()   # likes = 0
reel1.liked()      # likes = 1
reel1.liked()      # likes = 2
reel2.liked()      # likes = 1
reel1.disliked()   # likes = 1

# Adding comments
reel1.add_comment("Nice dance!")
reel1.add_comment("Amazing energy 🔥")
reel2.add_comment("Very informative session")
reel1.delete_comment()

# Displaying details
reel1.display_likes()
reel2.display_likes()
reel1.display_comments()
reel2.display_comments()

# Display object IDs
print(id(reel1))
print(id(reel2))