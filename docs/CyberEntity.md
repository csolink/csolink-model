---
parent: Entities
title: csolink:CyberEntity
grand_parent: Classes
layout: default
---

# Class: CyberEntity


An entity that has digital reality (a.k.a. cyber essence).

URI: [csolink:CyberEntity](https://w3id.org/csolink/vocab/CyberEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ResourceSample],[NamedThing],[CyberEssence],[ComputationalProcessOrActivity]-%20enabled%20by%200..%2A%3E[CyberEntity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[CyberEntity]uses%20-.-%3E[CyberEssence],[CyberEntity]%5E-[ResourceSample],[NamedThing]%5E-[CyberEntity],[ComputationalProcessOrActivity],[Attribute],[Agent])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.

## Children

 * [ResourceSample](ResourceSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]

## Referenced by class

 *  **[ComputationalProcessOrActivity](ComputationalProcessOrActivity.md)** *[enabled by](enabled_by.md)*  <sub>0..*</sub>  **[CyberEntity](CyberEntity.md)**

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Narrow Mappings:** | | csrc:Authenticable_Entity |
|  | | csrc:cyber_resource |
|  | | csrc:non_person_entity |
|  | | MAID:179768478 |

