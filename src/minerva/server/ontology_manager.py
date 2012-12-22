from rdflib.graph import Graph
from rdflib.namespace import Namespace, RDF, OWL
from rdflib import OWL

from minerva.common.constants import ONTOLOGY_FILE

MINERVA = Namespace('http://www.semanticweb.org/ontologies/2012/11/minerva.owl#')

class OntologyManager(object):
    
    def __init__(self):
        self.graph = Graph()
        self.graph.parse(ONTOLOGY_FILE)
    
    def decorate_owl(self, value):
        return OWL[value] 
    
    def decorate_minerva(self, value):
        return MINERVA[value]
        
    def add(self, s, p, o):
        self.graph.add((s, p, o))
        
    def add_individual(self, class__, individual):
        self.add(self.decorate_minerva(individual),
                 RDF.type,
                 self.decorate_minerva(class__))
        self.add(self.decorate_minerva(individual),
                 RDF.type,
                 self.decorate_owl('NamedIndividual'))

    def print__(self):
        for s,p,o in self.graph:
            print 'Triple: s: %s, p: %s, o: %s' % (s, p, o)
            
    def save(self):
        self.graph.serialize(ONTOLOGY_FILE)
            