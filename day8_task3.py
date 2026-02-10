# Problem: Permission Checker
# You want a function dashboard() but only admin should access it.
# What to do
# Create a decorator called admin_only
# Decorator behavior
# if username == "admin" → allow function execution
# else → print "Access Denied"
# Apply decorator
# Use it on:
# dashboard()
# Test
# Call dashboard using:
# admin → works
# other user → blocked
# Main point
# Decorator means:
#  ✅ adding extra security/checks to a function
#  ✅ without changing the function code


def admin_only(func):
    def wrapper(user):
        if user=="admin":
            func(user)
        else:
            print("invalid user")
    return wrapper
            

@admin_only
def dashboard(user):    
    print("Welcome to the dashboard page")

@admin_only
def listing():
    print("Welcome to the listing page")

@admin_only
def profile():
    print("Welcome to the profile page")

@admin_only
def settings():
    print("Welcome to the settings page")

user="admin"
dashboard(user)

user="moulya"
dashboard(user)