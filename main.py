import xmlschema
from pprint import pprint
from xml.etree import ElementTree


def run():
	schema = xmlschema.XMLSchema('drugbank.xsd')
	xt = ElementTree.parse('full_database.xml')
	root = xt.getroot()
	pprint(xs.elements['drug'].decode(root[0]))
	#print(schema.types)
	#pprint(dict(schema.elements))
	#pprint(sorted(schema.maps.types.keys())[:])
	#pprint(sorted(schema.maps.elements.keys())[:10])
	#save = drugbank_schema.to_dict('full_database.xml')
	# drug_gene = {} # keys will be drug generic names, values will be gene symbols
	# tree = ET.parse('full_database.xml')
	# root = tree.getroot()
	# drugs = root.findall("drug")
	# for drug in drugs:
	# 	# get its common name
	# 	name = drug.find("name")
	# 	if name is None:
	# 		continue
	# 	generic_name = name.text.lower()
	# 	# figure out if approved
	# 	is_approved = False
	# 	groups = drug.find("groups")
	# 	if groups is not None:
	# 		for group in groups.findall("group"):
	# 			if group.text == "approved":
	# 				is_approved = True
	# 	if not is_approved:
	# 		continue
	# 	if debug:
	# 		sys.stderr.write(generic_name+"\t")
	# 	gene_symbol = None
	# 	targets_element = drug.find("targets")


	#     if targets_element is not None:
	# 		targets = targets_element.findall("target")
	# 		for target in targets:
	# 		    # not all targets have a position, but for those that do,
	# 		    # only take the top-ranked target association
	# 		    if target.attrib.has_key("position"):
	# 		        if target.attrib["position"] != '1':
	# 		            continue
	# 		    known_action = target.find("known-action")
	# 		    if known_action.text != "yes":
	# 		        continue
	# 		    polypeptide = target.find("polypeptide")
	# 		    if polypeptide is None:
	# 		        continue
	# 		    organism = polypeptide.find("organism")
	# 		    if organism.text != "Human":
	# 		        continue
	# 		    extids = polypeptide.find("external-identifiers")
	# 		    for extid in extids.findall("external-identifier"):
	# 		        if extid.find("resource").text == "HUGO Gene Nomenclature Committee (HGNC)":
	# 		            hgnc_id = extid.find("identifier").text
	# 		    if hgnc_id is not None:
	# 		        if hgnc.has_key(hgnc_id):
	# 		            gene_symbol = hgnc[hgnc_id]['Approved Symbol']
	# 		            break
	#         drug_gene[generic_name] = gene_symbol # add key-value pair to dictionary
	#         if debug:
	#             if gene_symbol is None:
	#                 print ""
	#             else:
	#                 print gene_symbol
	# return drug_gene

if __name__ == '__main__':
	run()
