import os
from rdflib import Graph, Namespace, RDF
try: from rdflib import OWL
except: OWL = Namespace('http://www.w3.org/2002/07/owl#')

from minerva.common.constants import ONTOLOGY_FILE

MINERVA = Namespace('http://www.semanticweb.org/ontologies/2012/11/minerva.owl#')

class OntologyManager(object):
    
    def __init__(self):
        self.filepath = os.path.dirname(os.path.abspath(__file__)) + os.sep + ONTOLOGY_FILE
        self.graph = Graph()
        self.graph.parse(self.filepath)
    
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
        self.graph.serialize(self.filepath)
            