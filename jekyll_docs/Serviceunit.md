---
parent: Entities
title: csolink:Serviceunit
grand_parent: Classes
layout: default
---

# Class: Serviceunit


The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a cluster. It can be deployed, isolated, and repaired independently.

URI: [csolink:Serviceunit](https://w3id.org/csolink/vocab/Serviceunit)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[DeploymentEntity]%5E-[Serviceunit%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NamedThing],[DeploymentEntity],[Attribute],[Agent])

---


## Parents

 *  is_a: [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part

## Attributes


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

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Inherited from systemic entity:

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | csrc:Basic_Service_Set |
|  | | csrc:Interdependent_Basic_Service_Set |
|  | | sumo:serviceProvider |
|  | | sumo:Group |
| **Narrow Mappings:** | | csrc:Class_of_Service |
|  | | csrc:Service_Agent |
| **Broad Mappings:** | | CSO:component_repository |
|  | | CSO:component-based_framework |
|  | | csrc:Extended_Service_Set |
|  | | csrc:Service_Component_Reference_Model |
|  | | sumo:Group |
|  | | sumo:ReplicationsOnSameHostOK |
|  | | sumo:UnitFn |
|  | | sumo:UnitOfInformation |
