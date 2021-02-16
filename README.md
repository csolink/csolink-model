[![Python 3.7](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.com/csolink/csolink-model.svg?branch=master)](https://travis-ci.com/csolink/csolink-model)
![Regenerate Csolink Model Artifacts](https://github.com/csolink/csolink-model/workflows/Regenerate%20Csolink%20Model%20Artifacts/badge.svg)
![Deploy Documentation](https://github.com/csolink/csolink-model/workflows/Deploy%20Documentation/badge.svg)

<img src="images/csolink-logo.png" width="20%">

# Csolink Model (Experimental translation of biolink-model)

Quickstart docs:

- Browse the model: [https://csolink.github.io/csolink-model](https://csolink.github.io/csolink-model)
  - [named thing](https://csolink.github.io/csolink-model/docs/NamedThing.html)
  - [association](https://csolink.github.io/csolink-model/docs/Association.html)
  - [predicate](https://csolink.github.io/csolink-model/docs/predicates.html)

See also [Csolink Model Guidelines](./guidelines/index.md) for understanding, curating, and working with the model.


## Introduction

The purpose of the Csolink Model is to provide a high-level datamodel of
computing system entities (computer, errors, observability, networks, instances, directors, etc),
their properties, relationships, and enumerate ways in which they can be associated.

The representation is independent of storage technology or metamodel (Solr documents, neo4j/property graphs,
RDF/OWL, JSON, CSVs, etc). Different mappings to each of these are provided.

The specification of the Csolink Model is a [single YAML file](csolink-model.yaml) built using [biolinkml](https://github.com/biolink/biolinkml).
The basic elements of the YAML are:

 - Class Definitions: definitions of upper level *classes* representing both 'named thing' and 'association'
 - Slot Definitions: definitions of *slots* (aka properties) that can be used to relate members of these classes to other classes or data types. Slots collectively refer to predicates, node properties, and edge properties

The model itself is being used in the following projects:


## Organization

The main source of truth is [csolink-model.yaml](csolink-model.yaml). This is a YAML file that is intended to
be relatively simple to view and edit in its native form.

The yaml definition is currently used to derive:

  - [JSON Schema](json-schema)
  - [Python dataclasses](csolink/model.py)
  - [Java code gen](java)
  - [ProtoBuf definitions](csolink-model.proto)
  - [GraphQL](csolink-model.graphql)
  - [RDF](csolink-model.ttl)
  - [OWL](csolink-model.owl.ttl)
  - [RDF Shape Expressions](csolink-model.shex)
  - [JSON-LD context](context.jsonld)
  - [Graphviz](graphviz)
  - [GOlr YAML schemas](golr-views)
    - these can be compiled down to Solr XML schemas
    - these are also intermediate targets used within the BBOP/AmiGO framework
  - [Markdown documentation](docs)


## Make and build instructions

Prerequisites: Python 3.7+ and pipenv

To install pipenv,

```sh
sudo pip3 install pipenv
```

To set your python version:

```sh
vi Pipfile    # i.e. requires=3.8
pipenv --python /usr/bin/python3
```

To install the project,
```sh
make install
```

If you make changes to [csolink-model.yaml](csolink-model.yaml) then be sure to run the Makefile to generate
up-to-date artifacts and documentation.

```sh
make
```


**Note:** the Makefile requires the following dependencies to be installed:

### jsonschema

[jsonschema](https://json-schema.org/)

Generally install using 

```sh
pip3 install jsonschema
```

### jsonschema2pojo

[jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo)

If you are on a Mac, it can be installed using `brew`:
```sh
brew install jsonschema2pojo
```
For other OS environments, download the latest release then extract it into your execution path.

### GraphViz

See [GraphViz site](https://graphviz.org/) for installation in your operating system.



## How do I use Csolink Model YAML programatically?

For operations such as CURIE lookup, finding class by synonyms, get parents, get ancestors, etc. please make use of [csolink-model-toolkit](https://github.com/csolink/csolink-model-toolkit/). It provides a convenience methods for traversing Csolink Model.

## External Weblinks

### Useful links

Apart from Csolink prefixes, other useful links are:

* [AMiner Dataset](https://www.aminer.cn/data/) categorizer
* [AI Lit. Panorama](http://aipano.cse.ust.hk/p9sw2ndt) viewer
* [Gensim](https://radimrehurek.com/gensim/models/ldaseqmodel.html) modeling
* [Wikiverse](http://wikiverse.io) visualizer.
* [Industry 4.0 Standards](https://i40-tools.github.io/StandardOntologyVisualization) visualizer.
* [VocReg](https://www.vocoreg.com/documentation/NOSQL/master) NoSQL
* [LOV](https://lov.linkeddata.es/dataset/lov) Linked Open Vocabs
* [OpenLink](https://www.openlinksw.com/describe/?url=http%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23Ontology&graph=urn%3Aontology%3Asemantic%3Amapping&graph=urn%3Aontology%3Acartridges%3Amapping&graph=urn%3Aopl%3Ashop%3Aoffering%3Asponging%3Acache%3Aofficial&graph=urn%3Aopenlink%3Aschema%3Ageneral%3Amappings&graph=urn%3Aopenlink%3Aschema%3Aoplweb%3Amappings&graph=urn%3Acartridges%3Amapping&graph=urn%3Adata%3Aopenlink%3Aproducts&graph=urn%3Adata%3Aopenlink%3Aglossary&graph=urn%3Adata%3Aopenlink%3Awebsites) OLS ontologies
* [Knowledge-Base Projects, Groups, and Related Materia](https://www.cs.utexas.edu/users/mfkb/related.html)
* [WordNet](http://wordnetweb.princeton.edu/perl/webwn)
 
### Other useful fragments?

* [Prakort](https://github.com/Prakort/Research-Enrich-Computer-Science-Ontology)
* [csoclassifier](https://github.com/angelosalatino/cso-classifier)
* [WikiOnto](https://github.com/MarcelH91/WikiOnto)
* [CSIHO](https://github.com/moreiragb/csiho), Computer Security Incident Handling Ontology (owl)
* [BibliOnto](https://github.com/nizarfahmi/BibliOnto)
* [hcio](https://github.com/sidornellas/hcio) Human-Comp interaction
