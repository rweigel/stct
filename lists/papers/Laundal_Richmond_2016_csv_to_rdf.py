import csv
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, DCTERMS, RDFS, OWL, XSD, FOAF
from pathlib import Path
import re

# an RE our term URIs must match (we're not very diligent yet)
FULL_TERM_PATTERN = "[\w\d#:/_.*%-]+"
# an RE our terms themselves must match
TERM_PATTERN = "[\w\d_-]+"

FILE = Path("laundal-and-richmond-2016.csv")

REFFRAME = Namespace("http://www.ivoa.net/rdf/refframe#")
LR2016 = Namespace("http://www.voparis-ns.obspm.fr/rdf/ihdea/laundal-richmond-2016#")
IVOASEM = Namespace("http://www.ivoa.net/rdf/ivoasem#")
WDRS = Namespace("http://www.w3.org/2007/05/powder-s#")

AUTHORS = [
    "Laundal, K.M.",
    "Richmond, A.D.",
]


def read_source(filename):
    """creates RDF Graph from our custom CSV format.
    """
    g = Graph()
    g.bind('ivoasem', IVOASEM)
    g.bind('', LR2016)
    g.bind('wdrs', WDRS)

    # define the document as an Ontology
    g.add((URIRef(LR2016), RDF.type, OWL.Ontology))
    g.add((URIRef(LR2016), RDFS.label, Literal("Magnetic Coordinate Systems", lang="en")))
    g.add((URIRef(LR2016), DCTERMS.created, Literal("2016-07-19", datatype=XSD.date)))
    for author in AUTHORS:
        tmp = BNode()
        g.add((tmp, FOAF.name, Literal(author)))
        g.add((URIRef(LR2016), DCTERMS.creator, tmp))
    g.add((URIRef(LR2016), DCTERMS.description, Literal(
    """Geospace phenomena such as the aurora, plasma motion, ionospheric currents and associated magnetic 
    field disturbances are highly organized by Earth's main magnetic field. This is due to the fact that the 
    charged particles that comprise space plasma can move almost freely along magnetic field lines, but not 
    across them. For this reason it is sensible to present such phenomena relative to Earth's magnetic field. 
    A large variety of magnetic coordinate systems exist, designed for different purposes and regions, ranging 
    from the magnetopause to the ionosphere. In this paper we review the most common magnetic coordinate systems 
    and describe how they are defined, where they are used, and how to convert between them. The definitions are 
    presented based on the spherical harmonic expansion coefficients of the International Geomagnetic Reference 
    Field (IGRF) and, in some of the coordinate systems, the position of the Sun which we show how to calculate 
    from the time and date. The most detailed coordinate systems take the full IGRF into account and define 
    magnetic latitude and longitude such that they are constant along field lines. These coordinate systems, 
    which are useful at ionospheric altitudes, are non-orthogonal. We show how to handle vectors and vector 
    calculus in such coordinates, and discuss how systematic errors may appear if this is not done correctly.""",
           lang="en")))
    g.add((URIRef(LR2016), DCTERMS.license, URIRef("http://creativecommons.org/publicdomain/zero/1.0/")))
    g.add((URIRef(LR2016), DCTERMS.title, Literal("Magnetic Coordinate Systems", lang="en")))
    g.add((URIRef(LR2016), IVOASEM.vocflavour, Literal("RDF Class")))

    with open(filename, "r", encoding="utf-8") as f:
        for rec in csv.reader(f, delimiter=","):
            rec = [(s or None) for s in rec]
            g.add((LR2016.term(rec[0]), RDF.type, RDFS.Class))
            label = "(".join(rec[1].split('(')[:-1]).strip()
            comment = ")".join(rec[1].split(')')[:-1]).strip() + " of Laundal and Richmond 2016)"
            g.add((LR2016.term(rec[0]), RDFS.label, Literal(label)))
            g.add((LR2016.term(rec[0]), RDFS.comment, Literal(comment)))
            g.add((LR2016.term(rec[0]), WDRS.describedby, URIRef("https://doi.org/10.1007/s11214-016-0275-y")))

    return g


if __name__ == "__main__":
    g = read_source(FILE)
    g.serialize("lr2016_refframe.ttl")
