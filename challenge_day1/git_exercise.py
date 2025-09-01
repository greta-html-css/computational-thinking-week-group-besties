from ipek2 import name_ipek
from osjah2 import my_name
from anita import fie
from jacefile import name_jace
from greta import name 
from BassantFile import name_bassant


def group_info():
    names = [name_ipek(), my_name(), fie(), name_jace(), name(), name_bassant()]
    print("This team is Besties! We are:")
    print(", ".join(names))

group_info()

    