import csv
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, DCTERMS, RDFS, OWL, XSD, FOAF
from pathlib import Path
import re

# an RE our term URIs must match (we're not very diligent yet)
FULL_TERM_PATTERN = "[\w\d#:/_.*%-]+"
# an RE our terms themselves must match
TERM_PATTERN = "[\w\d_-]+"

FILE = Path("spase.csv")

REFFRAME = Namespace("http://www.ivoa.net/rdf/refframe#")
SPASECOORDS = Namespace("http://www.voparis-ns.obspm.fr/rdf/ihdea/spase-coordinate-system-names#")
IVOASEM = Namespace("http://www.ivoa.net/rdf/ivoasem#")
WDRS = Namespace("http://www.w3.org/2007/05/powder-s#")

AUTHORS = [
    "SPASE Group",
]


def read_source(filename):
    """creates RDF Graph from our custom CSV format.
    """
    g = Graph()
    g.bind('ivoasem', IVOASEM)
    g.bind('', SPASECOORDS)
    g.bind('wdrs', WDRS)

    # define the document as an Ontology
    g.add((URIRef(SPASECOORDS), RDF.type, OWL.Ontology))
    g.add((URIRef(SPASECOORDS), RDFS.label, Literal("SPASE Coordinate System Names", lang="en")))
    g.add((URIRef(SPASECOORDS), DCTERMS.created, Literal("2021-06-10", datatype=XSD.date)))
    for author in AUTHORS:
        tmp = BNode()
        g.add((tmp, FOAF.name, Literal(author)))
        g.add((URIRef(SPASECOORDS), DCTERMS.creator, tmp))
    g.add((URIRef(SPASECOORDS), DCTERMS.description, Literal(
    """Identifiers of the origin and orientation of a set of typical orthogonal axes. List defined
    by the SPASE group, as presetned in version 2.4.0.""",
           lang="en")))
    g.add((URIRef(SPASECOORDS), DCTERMS.license, URIRef("http://creativecommons.org/publicdomain/zero/1.0/")))
    g.add((URIRef(SPASECOORDS), DCTERMS.title, Literal("SPASE Coordinate System Names", lang="en")))
    g.add((URIRef(SPASECOORDS), IVOASEM.vocflavour, Literal("RDF Class")))

    with open(filename, "r", encoding="utf-8") as f:
        data = csv.DictReader(f, delimiter=",")
        print(data)
        for line in data:
            print(line)
            key, label, comment, same_as, see_also = line.values()
            if same_as == "":
                same_as = None
            if see_also == "":
                see_also = None
            if key.startswith("#"):
                g.add((URIRef(SPASECOORDS), RDFS.seeAlso, URIRef(key[1:].strip())))
                continue
            g.add((SPASECOORDS[key], RDF.type, RDFS.Class))
            g.add((SPASECOORDS[key], RDFS.label, Literal(label)))
            g.add((SPASECOORDS[key], RDFS.comment, Literal(comment)))
            g.add((SPASECOORDS[key], WDRS.describedby, URIRef("https://spase-group.org/data/model/spase-2.4.0/spase-2_4_0_xsd.html")))
            if same_as is not None:
                g.add((SPASECOORDS[key], OWL.sameAs, SPASECOORDS[same_as]))
            if see_also is not None:
                for item in see_also.split(","):
                    if item.startswith("doi:"):
                        uri = URIRef(item.replace("doi:", "https://doi.org/"))
                    elif item.startswith("bibcode:"):
                        uri = URIRef(item.replace("bibcode:", "https://ui.adsabs.harvard.edu/abs/"))
                    elif item.startswith("http"):
                        uri = URIRef(item)
                    else:
                        raise ValueError("unknown URI type")
                    g.add((SPASECOORDS[key], RDFS.seeAlso, uri))
    return g


if __name__ == "__main__":
    g = read_source(FILE)
    g.serialize("spase_refframe.ttl")
