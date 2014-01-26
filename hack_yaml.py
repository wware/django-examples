# http://pyyaml.org/wiki/PyYAMLDocumentation
# http://yaml.org/spec/current.html
# http://www.yaml.org/refcard.html

import yaml
import pprint

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

assert pprint.pformat(yaml.load(document)) == "{'a': 1, 'b': {'c': 3, 'd': 4}}"

##########################################################

struc = {
    'left': {
        'name': 'big sword',
        'weight': 3.14159
    }
}
struc['right'] = struc['left']
expected = """\
- left: &id001 {name: big sword, weight: 3.14159}
  right: *id001
"""
assert yaml.dump([struc]) == expected

##########################################################

document = """
# comment can go here
  &A
  - 1
  - 2
  # comment can also go here
  - 3
  - 4
  - *A
"""

x = yaml.load(document)
assert x[4] == x

##########################################################

document = """\
--- !!set
    ? here is one thing
    ? here is another thing
    ? yet another
...
"""

x = yaml.load(document)
pprint.pprint(x)

##########################################################

document = """\
&x
--- !!set
    ? here is one thing
    ? here is another thing
    ? yet another
...

asserted: true
name: http://foobar
rdf-model: *x

"""

"""
rdf-model: !!set
    ?   s: &bing w3.org,YYYY-MM:bnode _:cwtAGnDy1
        p: w3.org,YYYY-MM:uri http://xmlns.com/foaf/0.1/nick
        o: donna

    ?   s: *bing
        p: w3.org,YYYY-MM:uri http://xmlns.com/foaf/0.1/mbox
        o: donna@...

    ?   s: *bing
        p: w3.org,YYYY-MM:uri http://www.w3.org/1999/02/22-rdf-syntax-ns#type
        o: w3.org,YYYY-MM:uri http://xmlns.com/foaf/0.1/Person

    ?   s: *bing
        p: w3.org,YYYY-MM:uri http://xmlns.com/foaf/0.1/name
        o: str "Donna Fales"
"""
x = yaml.load(document)
pprint.pprint(x)
