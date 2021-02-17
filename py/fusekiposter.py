import requests


def postDiningChair(pname, width, length, height):
    leg_width = width * 0.1
    leg_length = length * 0.1
    leg_height = height * 0.4

    seat_width = width
    seat_length = length
    seat_height = height * 0.1

    back_width = width * 0.1
    back_length = length
    back_height = height * 0.5

    headers = {
        'Accept': 'text/plain,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n  PREFIX owl: <http://www.w3.org/2002/07/owl#>\n  INSERT\n  {\n'
    info = f'kbe:{pname}  a        owl:NamedIndividual, kbe:DiningChair; \n        kbe:leg       kbe:{pname}_leg; \n    \tkbe:back\tkbe:{pname}_back; \n        kbe:seat  kbe:{pname}_seat .\n\nkbe:{pname}_leg  a           owl:NamedIndividual, kbe:Block; \n        kbe:hasHeight  "{leg_height}"^^xsd:float; \n        kbe:hasLength  "{leg_length}"^^xsd:float; \n        kbe:hasWidth   "{leg_width}"^^xsd:float .\n\nkbe:{pname}_back  a      owl:NamedIndividual, kbe:Block; \n        kbe:hasHeight  "{back_height}"^^xsd:float; \n        kbe:hasLength  "{back_length}"^^xsd:float; \n        kbe:hasWidth   "{back_width}"^^xsd:float .\n\nkbe:{pname}_seat  a      owl:NamedIndividual, kbe:Block; \n        kbe:hasHeight  "{seat_height}"^^xsd:float; \n        kbe:hasLength  "{seat_length}"^^xsd:float; \n        kbe:hasWidth   "{seat_width}"^^xsd:float .\n'
    postfix = '\n}\nwhere {}'
    data = {
        'update': prefix + info + postfix

    }
    try:
        response = requests.post('http://localhost:3030/kbe',
                                 headers=headers, data=data)

        print(response)
    except:
        return(400)
    return(response.status_code)


def postStoolChair(pname, diameter, height):
    seat_height = height * 0.1
    seat_diameter = diameter

    leg_height = height * 0.8
    leg_diameter = diameter * 0.15

    leg_bottom_height = height * 0.1
    leg_bottom_diameter = diameter * 0.35

    headers = {
        'Accept': 'text/plain,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nINSERT\n{\n'
    info = f'kbe:{pname}  a        owl:NamedIndividual , kbe:StoolChair ;\n        kbe:leg       kbe:{pname}_leg;\n    \tkbe:bottomleg\tkbe:{pname}_bottomleg;\n        kbe:seat  kbe:{pname}_seat .\n\nkbe:{pname}_leg  a           owl:NamedIndividual , kbe:Cylinder ;\n        kbe:hasHeight  "{leg_height}"^^xsd:float ;\n        kbe:hasDiameter  "{leg_diameter}"^^xsd:float .\n  \nkbe:{pname}_bottomleg  a           owl:NamedIndividual , kbe:Cylinder ;\n        kbe:hasHeight  "{leg_bottom_height}"^^xsd:float ;\n        kbe:hasDiameter  "{leg_bottom_diameter}"^^xsd:float .\n\nkbe:{pname}_seat  a      owl:NamedIndividual , kbe:Cylinder ;\n        kbe:hasHeight  "{seat_height}"^^xsd:float ;\n        kbe:hasDiameter  "{seat_diameter}"^^xsd:float .'
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


def postModernChair(pname, width, length, height):
    leg_width = width * 0.2
    leg_length = length
    leg_height = height

    seat_width = width * 0.6
    seat_length = length
    seat_height = height * 0.5

    back_width = width * 0.6
    back_length = length * 0.2
    back_height = height * 0.5

    headers = {
        'Accept': 'text/plain,*/*;q=0.9',
    }

    prefix = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>\n  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n  PREFIX owl: <http://www.w3.org/2002/07/owl#>\n  INSERT\n  {\n'
    info = f'kbe:{pname}  a        owl:NamedIndividual, kbe:ModernChair; \n        kbe:leg       kbe:{pname}_leg; \n    \tkbe:back\tkbe:{pname}_back; \n        kbe:seat  kbe:{pname}_seat .\n\nkbe:{pname}_leg  a           owl:NamedIndividual, kbe:Block; \n        kbe:hasHeight  "{leg_height}"^^xsd:float; \n        kbe:hasLength  "{leg_length}"^^xsd:float; \n        kbe:hasWidth   "{leg_width}"^^xsd:float .\n\nkbe:{pname}_back  a      owl:NamedIndividual, kbe:Block; \n        kbe:hasHeight  "{back_height}"^^xsd:float; \n        kbe:hasLength  "{back_length}"^^xsd:float; \n        kbe:hasWidth   "{back_width}"^^xsd:float .\n\nkbe:{pname}_seat  a      owl:NamedIndividual, kbe:Block; \n        kbe:hasHeight  "{seat_height}"^^xsd:float; \n        kbe:hasLength  "{seat_length}"^^xsd:float; \n        kbe:hasWidth   "{seat_width}"^^xsd:float .\n'
    postfix = '\n}\nwhere {}'
    data = {
        'update': prefix + info + postfix

    }
    try:
        response = requests.post('http://localhost:3030/kbe',
                                 headers=headers, data=data)

        print(response)
    except:
        return(400)
    return(response.status_code)
