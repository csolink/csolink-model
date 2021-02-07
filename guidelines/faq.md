---
title: "Frequently Asked Questions"
parent: "Csolink Model Guidelines"
layout: default
---

## FAQ

### How do I type nodes in a graph with concepts that are not in the Csolink Model?

Each node in a knowledge graph can be typed using the node property slot `category`.

In addition to category, one can type a node using the `rdf:type` and `rdfs:subClassOf` predicates.


### How do I type edges in a graph with concepts that are not in the Csolink Model?

Each edge in a knowledge graph can be typed using association slot `association type` (or `rdf:type`).


### How do I add properties that are not in the Csolink Model

Each node and/or edge can have properties that are outside of Csolink Model. 

Alternatively, for a more structured representation it is recommended to use the class `Attribute` to represent the property and link a node/edge using the `has attribute` slot.

### What is the serialized form of Csolink Model?

Refer to [Working with the Model[working-with-the-model.md] for an example on how a Csolink Model graph can be represented as labelled property graphs and RDF graphs.

### What is the difference between `predicate`, `relation`, `association_type`?

- `predicate` is an association slot and must have a value from the [`related to` hierarchy](https://csolink.github.io/csolink-model/docs/related_to)
- `relation` is an association slot and can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- `association_type` (or `rdf:type`) is an association slot and must have a value from the [`association` hierarchy](https://csolink.github.io/csolink-model/docs/Association)

