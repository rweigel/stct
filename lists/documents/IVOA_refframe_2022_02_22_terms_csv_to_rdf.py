import csv
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF, DCTERMS, RDFS, OWL, XSD, FOAF
from pathlib import Path
import re

# an RE our term URIs must match (we're not very diligent yet)
FULL_TERM_PATTERN = "[\w\d#:/_.*%-]+"
# an RE our terms themselves must match
TERM_PATTERN = "[\w\d_-]+"

FILE = Path("ivoa-refframe-2022-02-22-terms.csv")

REFFRAME = Namespace("http://www.ivoa.net/rdf/refframe#")
IVOASEM = Namespace("http://www.ivoa.net/rdf/ivoasem#")

AUTHORS = [
    "Rots, A.",
    "Cresitello-Dittmar, M.",
    "Demleitner, M.",
]


def read_source(filename):
    """creates RDF Graph from our custom CSV format.
    """
    parent_stack = []
    last_term = None
    header = {}
    g = Graph()
    #g.base = "http://www.ivoa.net/rdf/refframe#"
    g.bind('ivoasem', IVOASEM)
    g.bind('', REFFRAME)

    # define the document as an Ontology
    g.add((URIRef(REFFRAME), RDF.type, OWL.Ontology))
    g.add((URIRef(REFFRAME), RDFS.label, Literal("Reference Frames", lang="en")))
    g.add((URIRef(REFFRAME), DCTERMS.created, Literal("2022-02-22", datatype=XSD.date)))
    for author in AUTHORS:
        tmp = BNode()
        g.add((tmp, FOAF.name, Literal(author)))
        g.add((URIRef(REFFRAME), DCTERMS.creator, tmp))
    g.add((URIRef(REFFRAME), DCTERMS.description, Literal(
    """A collection of reference frames in common use in astronomy,
    organised by top-level categories (equatorial, galactic, etc).  These
    concepts are used in VOTable's COOSYS, in SimpleDALRegExt's PosParam
    type, and of course in the Coords data model.  Where no more precise
    reference are given, http://www.iaufs.org/res.html is often of help.""",
           lang="en")))
    g.add((URIRef(REFFRAME), DCTERMS.license, URIRef("http://creativecommons.org/publicdomain/zero/1.0/")))
    g.add((URIRef(REFFRAME), DCTERMS.title, Literal("Reference Frames", lang="en")))
    g.add((URIRef(REFFRAME), IVOASEM.vocflavour, Literal("RDF Class")))

    g.add((REFFRAME.term("REFFRAME"), RDF.type, RDFS.Class))
    g.add((REFFRAME.term("REFFRAME"), RDFS.label, Literal("Reference Frame", lang="en")))
    g.add((REFFRAME.term("REFFRAME"), RDFS.comment, Literal("Generic Reference Frame class.", lang="en")))

    with open(filename, "r", encoding="utf-8") as f:
        for rec in csv.reader(f, delimiter=";"):
            if rec[0].startswith("#"):
                hdr_k, hdr_v = rec[0][1:].split("=")
                header[hdr_k] = hdr_v
            else:
                rec = [(s or None) for s in rec]

                hierarchy_level = int(rec[1])
                if hierarchy_level - 1 > len(parent_stack):
                    parent_stack.append(last_term)
                while hierarchy_level - 1 < len(parent_stack):
                    parent_stack.pop()
                last_term = rec[0]

                if parent_stack:
                    parent = parent_stack[-1]
                else:
                    parent = None

                more_relations = None if len(rec) < 5 else rec[4]

                g.add((REFFRAME.term(rec[0]), RDF.type, RDFS.Class))
                g.add((REFFRAME.term(rec[0]), RDFS.label, Literal(rec[2])))
                g.add((REFFRAME.term(rec[0]), RDFS.comment, Literal(rec[3])))
                if parent is not None:
                    g.add((REFFRAME.term(rec[0]), RDFS.subClassOf, REFFRAME.term(parent)))
                else:
                    g.add((REFFRAME.term(rec[0]), RDFS.subClassOf, REFFRAME.REFFRAME))
                if more_relations is not None:
                    for rel in more_relations.split():
                        mat = re.match(r"({})(?:\(({})\))?$".format(
                            FULL_TERM_PATTERN, FULL_TERM_PATTERN), rel)
                        prop, obj = mat.group(1), mat.group(2)
                        if prop == "ivoasem:deprecated":
                            g.add((REFFRAME.term(rec[0]), RDF.type, OWL.DeprecatedClass))
                            g.add((REFFRAME.term(rec[0]), IVOASEM.deprecated, Literal("true", datatype=XSD.boolean)))
                        if prop == "ivoasem:useInstead":
                            g.add((REFFRAME.term(rec[0]), RDFS.seeAlso, REFFRAME.term(obj)))
                            g.add((REFFRAME.term(rec[0]), IVOASEM.useInstead, REFFRAME.term(obj)))

    return g, header


if __name__ == "__main__":
    g, _ = read_source(FILE)
    g.serialize("ivoa_refframe.ttl")
