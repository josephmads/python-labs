# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os

secret = os.environ["SECRET"]
env = os.environ["ENVIRONMENT"]

print(secret, env)