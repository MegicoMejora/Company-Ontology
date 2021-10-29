import rdflib

# This basic query fetches all companies with a name and a figure for how much the
# company has made profit in the previous financial year.

query = """

PREFIX company: <http://www.semanticweb.org/ontologies/CourseWork/Company#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  

SELECT DISTINCT ?name ?profit
WHERE
{
	?film rdf:type company:Company .
  	?film company:profit ?profit .
	?film company:name ?name .
}"""

# Create an empty RDF graph and then parse the generated ontology into it.
g = rdflib.Graph()
g.parse("company_basic.owl", "xml")

print("graph has %s statements.\n" % len(g))

print ('{0:45s} {1:15s}'.format("Company Name","Profit"))
for x,y in g.query(query):
    print ('{0:45s} {1:15s}'.format(x,y))

print("")