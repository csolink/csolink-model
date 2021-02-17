---
parent: Associations
title: csolink:PairwiseOperationallyInteraction
grand_parent: Classes
layout: default
---

# Class: PairwiseOperationallyInteraction


An interaction at the operational level between two cyber entities

URI: [csolink:PairwiseOperationallyInteraction](https://w3id.org/csolink/vocab/PairwiseOperationallyInteraction)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OperationalEntity]%3Cobject%201..1-%20[PairwiseOperationallyInteraction%7Cid:string;predicate:predicate_type;relation:uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[OperationalEntity]%3Csubject%201..1-%20[PairwiseOperationallyInteraction],[OntologyClass]%3Cinteracting%20tasks%20category%200..1-%20[PairwiseOperationallyInteraction],[PairwiseComponentserviceToComponentserviceInteraction]%5E-[PairwiseOperationallyInteraction],[PairwiseComponentserviceToComponentserviceInteraction],[OperationalEntity],[OntologyClass],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [PairwiseComponentserviceToComponentserviceInteraction](PairwiseComponentserviceToComponentserviceInteraction.md) - An interaction between two componentservices or two servicetypes. May be cyber (e.g. serviceinstance binding) or service (between componentservices). May be symmetric (e.g. serviceinstance interaction) or directed (e.g. phosphorylation)

## Referenced by class


## Attributes


### Own

 * [interacting tasks category](interacting_tasks_category.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
 * [pairwise operationally interaction➞id](pairwise_operationally_interaction_id.md)  <sub>REQ</sub>
    * Description: identifier for the interaction. This may come from an interaction database.
    * range: [String](types/String.md)
 * [pairwise operationally interaction➞object](pairwise_operationally_interaction_object.md)  <sub>REQ</sub>
    * range: [OperationalEntity](OperationalEntity.md)
 * [pairwise operationally interaction➞predicate](pairwise_operationally_interaction_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [pairwise operationally interaction➞relation](pairwise_operationally_interaction_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [pairwise operationally interaction➞subject](pairwise_operationally_interaction_subject.md)  <sub>REQ</sub>
    * range: [OperationalEntity](OperationalEntity.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of csolink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a csolink model class URI.
This field is multi-valued. It should include values for ancestors of the csolink class; for example, a serviceinstance such as Shh would have category values `bl:Interface`, `bl:ComponentTypeProduct`, `bl:ComponentTypeEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific csolink class, or potentially to a class more specific than something in csolink.
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (service, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [pairwise operationally interaction➞id](pairwise_operationally_interaction_id.md)  <sub>REQ</sub>
    * Description: identifier for the interaction. This may come from an interaction database.
    * range: [String](types/String.md)
 * [pairwise operationally interaction➞object](pairwise_operationally_interaction_object.md)  <sub>REQ</sub>
    * range: [OperationalEntity](OperationalEntity.md)
 * [pairwise operationally interaction➞predicate](pairwise_operationally_interaction_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
 * [pairwise operationally interaction➞relation](pairwise_operationally_interaction_relation.md)  <sub>REQ</sub>
    * Description: interaction relationship type
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [pairwise operationally interaction➞subject](pairwise_operationally_interaction_subject.md)  <sub>REQ</sub>
    * range: [OperationalEntity](OperationalEntity.md)
