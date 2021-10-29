import rdflib
from rdflib.graph import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, XML
from rdflib.plugins.memory import IOMemory

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
    PREFIX org: <http://www.semanticweb.org/ontologies/CourseWork/Company#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    PREFIX dbpprop: <http://dbpedia.org/property/>
	
	CONSTRUCT {
		?company rdf:type org:Company .
		?company org:name ?name .
		?company org:ceo ?ceo .	
		?ceo rdf:type org:Ceos .
        ?company org:locationCity ?locationcity .	
		?locationcity rdf:type org:City .
		?company org:headquarter ?headquarter .	
		?headquarter rdf:type org:Country .
		?company org:industry ?industry .	
		?industry rdf:type org:Industry_Type .		
		?company org:subsidiary ?subsidiary .	
		?subsidiary rdf:type org:Subsidiary .
		?company org:product ?product .	
		?product rdf:type org:Main_Products .
		?company org:service ?service .	
		?service rdf:type org:Service .
		?company org:stockExchange ?stockexchange .	
		?stockexchange rdf:type org:StockExchange .
		?company org:parentOrganisation ?parent_organization .
		?parent_organization rdf:type org:Parent_Organization .
		?company org:assets ?assets .	
		?company org:equity ?equity .
		?company org:formationDate ?formation_date .
		?company org:formationYear ?formation_year .		
		?company org:netIncome ?profit .
		?company org:numberOfEmployees ?number_of_employees .
		?company org:operatingIncome ?operating_income .
		?company org:operatingIncome ?operating_income .
		?company org:ranking ?ranking .
		?company org:revenue ?revenue .
    }
     WHERE{
       ?company rdf:type dbpedia-owl:Company .
       ?company foaf:name ?name .	
	   
	   OPTIONAL {?company dbpedia-owl:ceo ?ceo}
	   OPTIONAL {?company dbpedia-owl:locationcity ?locationcity}
	   OPTIONAL {?company dbpedia-owl:headquarter ?headquarter}
	   OPTIONAL {?company dbpedia-owl:industry ?industry}
	   OPTIONAL {?company dbpedia-owl:subsidiary ?subsidiary}
	   OPTIONAL {?company dbpedia-owl:product ?product}
	   OPTIONAL {?company dbpedia-owl:service ?service}
	   OPTIONAL {?company dbpedia-owl:stockExchange ?stockExchange}
	   OPTIONAL {?company dbpedia-owl:parentOrganisation ?parentOrganisation}
	   OPTIONAL {?company dbpedia-owl:assets ?assets}
	   OPTIONAL {?company dbpedia-owl:equity ?equity}
	   OPTIONAL {?company dbpedia-owl:formationDate ?formationDate}
	   OPTIONAL {?company dbpedia-owl:formationYear ?formationYear}
	   OPTIONAL {?company dbpedia-owl:netIncome ?netIncome}
	   OPTIONAL {?company dbpedia-owl:operatingIncome ?operatingIncome}
	   OPTIONAL {?company dbpedia-owl:ranking ?ranking}
	   OPTIONAL {?company dbpedia-owl:revenue ?revenue}
	}
	LIMIT 10000
	"""

sparql.setQuery(construct_query)
sparql.setReturnFormat(XML)

memory_store = IOMemory()
graph_id = URIRef("http://www.semanticweb.org/store/company")
g = Graph(store = memory_store, identifier = graph_id)

print("  Relax! I am just working on...")

g = sparql.query().convert()

g.parse("company.owl")	

g.serialize("company_basic.owl", "xml")

print("  ...All done!")
print("")