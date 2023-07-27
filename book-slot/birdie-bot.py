from booking import book
from login import login

# User flow
login()

# Book slots for Tuesdays
book('Tuesday', "0600")
book('Tuesday', "0700")

# Book slots for Thursdays
book('Thursday', "0600")
book('Thursday', "0700")