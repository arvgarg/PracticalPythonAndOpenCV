import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--name", required=True, help="name of the user")
ap.add_argument("-f", "--features-db", required=True, help="Path to the features database")
args = vars(ap.parse_args())

print("Hi {}".format(args["name"]))
print("Path to Features: {}".format(args["features_db"]))

"""
Notice above that I’ve defined the argument as --features-db (with a dash), 
but I reference it by args["features_db"] (with an underscore). This is because the argparse  
Python library replaces dashes with underscores during the parsing.
"""

print()
print(args)

"""
args becomes a dictionary with full argument names as keys and their values are what
the user provided
"""