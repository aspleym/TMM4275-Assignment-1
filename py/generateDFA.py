import requests


def generateSquareTable(pname):
    headers = {
        'Accept': 'application/sparql-results+json',
    }
    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT *\nWHERE\n{\n?table a kbe:Table.\n?table kbe:leg ?leg.\n?leg kbe:hasHeight ?legHeight.\n  ?leg kbe:hasWidth ?legWidth.\n  ?leg kbe:hasLength ?legLength.\n?table kbe:tableTop ?tableTop.\n  ?tableTop kbe:hasWidth ?ttWidth.\n  ?tableTop kbe:hasHeight ?ttHeight.\n  ?tableTop kbe:hasLength ?ttLength.\n  \n  FILTER(?table = kbe:'
    postfix = ').\n}'
    data = {
        'query': prefix + pname + postfix
    }
    response = requests.post('http://localhost:3030/kbe',
                             headers=headers, data=data)

    data = response.json()
    f = open("./squareTable.dfa", "r")
    txt = f.read()

    h_param = data['results']['bindings'][0]['ttHeight']['value']
    w_param = data['results']['bindings'][0]['ttWidth']['value']
    l_param = data['results']['bindings'][0]['ttLength']['value']
    lh_param = data['results']['bindings'][0]['legHeight']['value']

    # Replacement section for L_PARAM, W_PARAM, H_PARAM acording to cube side
    txt = txt.replace("<P_NAME>", pname)
    txt = txt.replace("<L_PARAM>", l_param)
    txt = txt.replace("<W_PARAM>", w_param)
    txt = txt.replace("<H_PARAM>", h_param)
    txt = txt.replace("<LH_PARAM>", lh_param)

    # Writing to the correct location
    f = open(f'./products/{pname}.dfa', "w")
    f.write(txt)
    f.close()


def generateStool(pname):
    # Definings a http request for getting a specific round table
    headers = {
        'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT *\nWHERE\n{\n?table a kbe:Table.\n?table kbe:leg ?leg.\n?leg kbe:hasHeight ?legHeight.\n  ?leg kbe:hasDiameter ?legDiameter.\n?table kbe:tableTop ?tableTop.\n  ?tableTop kbe:hasHeight ?ttHeight.\n  ?tableTop kbe:hasDiameter ?ttDiameter.\n  \n  FILTER(?table = kbe:'
    postfix = ').\n}'
    data = {
        'query': prefix + pname + postfix
    }
    response = requests.post('http://localhost:3030/kbe',
                             headers=headers, data=data)

    data = response.json()
    f = open("/products/templates/roundTable.dfa", "r")
    txt = f.read()

    h_param = data['results']['bindings'][0]['ttHeight']['value']
    d_param = data['results']['bindings'][0]['ttDiameter']['value']
    ld_param = data['results']['bindings'][0]['legDiameter']['value']
    lh_param = data['results']['bindings'][0]['legHeight']['value']

    # Replacement section for L_PARAM, W_PARAM, H_PARAM acording to cube side
    txt = txt.replace("<P_NAME>", pname)
    txt = txt.replace("<D_PARAM>", d_param)
    txt = txt.replace("<H_PARAM>", h_param)
    txt = txt.replace("<LH_PARAM>", lh_param)
    txt = txt.replace("<LD_PARAM>", ld_param)

    # Writing to the correct location
    f = open(f'./products/{pname}.dfa', "w")
    f.write(txt)
    f.close()
