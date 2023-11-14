#ORGANIZATION - dont know what is the purpose of this file (MO) - (PP): important for defining initialization for packages/subpackages in python (think of every folder as a package/subpackage, when you import it __init__.py is run)
from importlib.metadata import version
from dotenv import load_dotenv

#-----------------------
# [1] read version from installed package and provide in __version__ variable
#-----------------------
__version__ = version("spellbook-py")

print("\nWELCOME TO SPELLBOOK-PY")
print("---------------------------------------")
#-----------------------
# [2] read environment variables.
#-----------------------
# Set up environment variables based on the .env file https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
load_dotenv()