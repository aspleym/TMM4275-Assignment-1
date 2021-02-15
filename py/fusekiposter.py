import requests


def postSquareTable(pname, theight, ttlength, ttwidth):
    headers = {
        'Accept': 'text/plain,*/*;q=0.9',
    }

    legName = f'leg_{pname}'
    topName = f'top_{pname}'

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nINSERT\n{\n'
    info = f'kbe:{pname}  a        owl:NamedIndividual , kbe:Table ;\n        kbe:leg       kbe:{legName} ;\n        kbe:tableTop  kbe:{topName} .\n\nkbe:{legName}  a           owl:NamedIndividual , kbe:Block ;\n        kbe:hasHeight  "{theight}"^^xsd:float ;\n        kbe:hasLength  "50.0"^^xsd:float ;\n        kbe:hasWidth   "50.0"^^xsd:float .\n\nkbe:{topName}  a      owl:NamedIndividual , kbe:Block ;\n        kbe:hasHeight  "25.0"^^xsd:float ;\n        kbe:hasLength  "{ttlength}"^^xsd:float ;\n        kbe:hasWidth   "{ttwidth}"^^xsd:float .'
    postfix = '\n}\nwhere {}'

    data = {
        'update': prefix + info + postfix
    }

    try:
        response = requests.post('http://localhost:3030/kbe',
                             headers=headers, data=data)
    except:
        return(400)
    return(response.status_code)


def postRoundTable(pname, theight, ttdiam):

    headers = {
        'Accept': 'text/plain,*/*;q=0.9',
    }

    legName = f'leg_{pname}'
    leg_diam = ("%.1f" % round((float(ttdiam) * 0.1), 1))
    topName = f'top_{pname}'

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nINSERT\n{\n'
    info = f'kbe:{pname}  a        owl:NamedIndividual , kbe:Table ;\n        kbe:leg       kbe:{legName} ;\n        kbe:tableTop  kbe:{topName} .\n\nkbe:{legName}  a           owl:NamedIndividual , kbe:Cylinder ;\n        kbe:hasHeight  "{theight}"^^xsd:float ;\n        kbe:hasDiameter  "{leg_diam}"^^xsd:float .\n\nkbe:{topName}  a      owl:NamedIndividual , kbe:Cylinder ;\n        kbe:hasHeight  "25.0"^^xsd:float ;\n        kbe:hasDiameter  "{ttdiam}"^^xsd:float .'
    postfix = '\n}\nwhere {}'

    data = {
        'update': prefix + info + postfix
    }
    try:
        response = requests.post('http://localhost:3030/kbe',
                             headers=headers, data=data)
    except:
        return(400)
    return(response.status_code)
