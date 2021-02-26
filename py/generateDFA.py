import os
import requests
import json


def generateDiningChair(pname, dfa):

    # Defining a http request for getting a specific dining chair

    headers = {
        'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }
    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT *\nWHERE\n{\n?dChair a kbe:DiningChair.\n?dChair kbe:leg ?leg.\n?leg kbe:hasHeight ?leg_height.\n  ?leg kbe:hasWidth ?leg_width.\n  ?leg kbe:hasLength ?leg_length.\n?dChair kbe:seat ?seat.\n  ?seat kbe:hasWidth ?seat_width.\n  ?seat kbe:hasHeight ?seat_height.\n  ?seat kbe:hasLength ?seat_length.\n?dChair kbe:back ?back.\n  ?back kbe:hasWidth ?back_width.\n  ?back kbe:hasHeight ?back_height.\n  ?back kbe:hasLength ?back_length.\n\n  \n  FILTER(?dChair = kbe:'
    postfix = ').\n}'
    data = {
        'query': prefix + pname + postfix
    }
    response = requests.post('http://localhost:3030/kbe',
                             headers=headers, data=data)

    data = response.json()

    script_dir = os.path.dirname(__file__)
    rel_path_template = "products/templates/diningChair.dfa"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 3], rel_path_template)

    f = open(abs_file_path_template, "r")
    txt = f.read()

    leg_side = data['results']['bindings'][0]['leg_width']['value']
    leg_height = data['results']['bindings'][0]['leg_height']['value']

    seat_width = data['results']['bindings'][0]['seat_width']['value']
    seat_length = data['results']['bindings'][0]['seat_length']['value']
    seat_height = data['results']['bindings'][0]['seat_height']['value']

    back_width = data['results']['bindings'][0]['back_width']['value']
    back_length = data['results']['bindings'][0]['back_length']['value']
    back_height = data['results']['bindings'][0]['back_height']['value']

    # Replacement section for parameters in the template file
    txt = txt.replace("<P_NAME>", pname)

    txt = txt.replace("<LEG_SIDE>", leg_side)
    txt = txt.replace("<LEG_HEIGHT>", leg_height)

    txt = txt.replace("<SEAT_HEIGHT>", seat_height)
    txt = txt.replace("<SEAT_WIDTH>", seat_width)
    txt = txt.replace("<SEAT_LENGTH>", seat_length)

    txt = txt.replace("<BACK_HEIGHT>", back_height)
    txt = txt.replace("<BACK_WIDTH>", back_width)
    txt = txt.replace("<BACK_LENGTH>", back_length)

    # Writing to the correct location

    if (dfa):
        rel_path_product = f'products/{pname}.dfa'
        abs_file_path_product = os.path.join(
            script_dir[:len(script_dir) - 3], rel_path_product)

        f = open(abs_file_path_product, "w")
        f.write(txt)
        f.close()

    data['results']['bindings'][0]['pname'] = pname
    return json.dumps(data['results']['bindings'][0])


def generateStoolChair(pname, dfa):
    # Defining a http request for getting a specific stool chair

    headers = {
        'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n  PREFIX owl: <http://www.w3.org/2002/07/owl#>\n  SELECT *\n  WHERE\n  {\n  ?sChair a kbe:StoolChair.\n  ?sChair kbe:leg ?leg.\n  \t?leg kbe:hasHeight ?leg_height.\n    ?leg kbe:hasDiameter ?leg_diameter.\n  ?sChair kbe:seat ?seat.\n    ?seat kbe:hasHeight ?seat_height.\n    ?seat kbe:hasDiameter ?seat_diameter.\n  ?sChair kbe:bottomleg ?leg_bottom.\n    ?leg_bottom kbe:hasHeight ?leg_bottom_height.\n    ?leg_bottom kbe:hasDiameter ?leg_bottom_diameter.\n\n    \n    FILTER(?sChair = kbe:'
    postfix = ').\n}'
    data = {
        'query': prefix + pname + postfix
    }

    response = requests.post('http://127.0.0.1:3030/kbe',
                             headers=headers, data=data)

    data = response.json()

    script_dir = os.path.dirname(__file__)
    rel_path_template = "products/templates/stoolChair.dfa"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 3], rel_path_template)

    f = open(abs_file_path_template, "r")
    txt = f.read()

    leg_height = data['results']['bindings'][0]['leg_height']['value']
    leg_diameter = data['results']['bindings'][0]['leg_diameter']['value']

    seat_height = data['results']['bindings'][0]['seat_height']['value']
    seat_diameter = data['results']['bindings'][0]['seat_diameter']['value']

    leg_bottom_height = data['results']['bindings'][0]['leg_bottom_height']['value']
    leg_bottom_diameter = data['results']['bindings'][0]['leg_bottom_diameter']['value']

    # Replacement section for L_PARAM, W_PARAM, H_PARAM acording to cube side
    txt = txt.replace("<P_NAME>", pname)
    txt = txt.replace("<LEG_HEIGHT>", leg_height)
    txt = txt.replace("<LEG_DIAMETER>", leg_diameter)
    txt = txt.replace("<LEG_BOTTOM_HEIGHT>", leg_bottom_height)
    txt = txt.replace("<LEG_BOTTOM_DIAMETER>", leg_bottom_diameter)
    txt = txt.replace("<SEAT_HEIGHT>", seat_height)
    txt = txt.replace("<SEAT_DIAMETER>", seat_diameter)

    # Writing to the correct location
    if (dfa):
        rel_path_product = f'products/{pname}.dfa'
        abs_file_path_product = os.path.join(
            script_dir[:len(script_dir) - 3], rel_path_product)

        f = open(abs_file_path_product, "w")
        f.write(txt)
        f.close()

    data['results']['bindings'][0]['pname'] = pname
    return json.dumps(data['results']['bindings'][0])


def generateModernChair(pname, dfa):

    # Defining a http request for getting a specific dining chair

    headers = {
        'Accept': 'application/sparql-results+json,*/*;q=0.9',
    }
    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT *\nWHERE\n{\n?mChair a kbe:ModernChair.\n?mChair kbe:leg ?leg.\n?leg kbe:hasHeight ?leg_height.\n  ?leg kbe:hasWidth ?leg_width.\n  ?leg kbe:hasLength ?leg_length.\n?mChair kbe:seat ?seat.\n  ?seat kbe:hasWidth ?seat_width.\n  ?seat kbe:hasHeight ?seat_height.\n  ?seat kbe:hasLength ?seat_length.\n?mChair kbe:back ?back.\n  ?back kbe:hasWidth ?back_width.\n  ?back kbe:hasHeight ?back_height.\n  ?back kbe:hasLength ?back_length.\n\n  \n  FILTER(?mChair = kbe:'
    postfix = ').\n}'
    data = {
        'query': prefix + pname + postfix
    }
    response = requests.post('http://localhost:3030/kbe',
                             headers=headers, data=data)

    data = response.json()

    script_dir = os.path.dirname(__file__)
    rel_path_template = "products/templates/modernChair.dfa"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 3], rel_path_template)

    f = open(abs_file_path_template, "r")
    txt = f.read()

    leg_width = data['results']['bindings'][0]['leg_width']['value']
    leg_length = data['results']['bindings'][0]['leg_length']['value']
    leg_height = data['results']['bindings'][0]['leg_height']['value']

    seat_width = data['results']['bindings'][0]['seat_width']['value']
    seat_length = data['results']['bindings'][0]['seat_length']['value']
    seat_height = data['results']['bindings'][0]['seat_height']['value']

    back_width = data['results']['bindings'][0]['back_width']['value']
    back_length = data['results']['bindings'][0]['back_length']['value']
    back_height = data['results']['bindings'][0]['back_height']['value']

    # Replacement section for parameters in the template file
    txt = txt.replace("<P_NAME>", pname)

    txt = txt.replace("<LEG_WIDTH>", leg_width)
    txt = txt.replace("<LEG_LENGTH>", leg_length)
    txt = txt.replace("<LEG_HEIGHT>", leg_height)

    txt = txt.replace("<SEAT_HEIGHT>", seat_height)
    txt = txt.replace("<SEAT_WIDTH>", seat_width)
    txt = txt.replace("<SEAT_LENGTH>", seat_length)

    txt = txt.replace("<BACK_HEIGHT>", back_height)
    txt = txt.replace("<BACK_WIDTH>", back_width)
    txt = txt.replace("<BACK_LENGTH>", back_length)

    # Writing to the correct location
    if (dfa):
        rel_path_product = f'products/{pname}.dfa'
        abs_file_path_product = os.path.join(
            script_dir[:len(script_dir) - 3], rel_path_product)

        f = open(abs_file_path_product, "w")
        f.write(txt)
        f.close()

    data['results']['bindings'][0]['pname'] = pname
    return json.dumps(data['results']['bindings'][0])
