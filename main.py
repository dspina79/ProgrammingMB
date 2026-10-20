"""Entry point for the Programming Merit Badge app."""

from menagerie import *
from zoo import Zoo

zoo = Zoo()
archie = Lion('Archie')
beth = Lion('Beth')
claude = Elephant('Claude')

zoo.add(archie)
zoo.add(beth)
zoo.add(claude)

zoo.print_roster()