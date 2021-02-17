---
parent: Entities
title: csolink:LifecycleStage
grand_parent: Classes
layout: default
---

# Class: LifecycleStage


A stage of development or growth of a system.

URI: [csolink:LifecycleStage](https://w3id.org/csolink/vocab/LifecycleStage)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[SystemicEntity],[SystemTaxon],[NamedThing],[ComponentserviceToAvailabilitySiteAssociation]-%20stage%20qualifier%200..1%3E[LifecycleStage%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ComponentserviceAvailabilityMixin]-%20stage%20qualifier%200..1%3E[LifecycleStage],[ComponentserviceToAvailabilitySiteAssociation]-%20stage%20qualifier(i)%200..1%3E[LifecycleStage],[LifecycleStage]uses%20-.-%3E[ThingWithTaxon],[SystemicEntity]%5E-[LifecycleStage],[ComponentserviceToAvailabilitySiteAssociation],[ComponentserviceAvailabilityMixin],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes

## Referenced by class

 *  **[ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md)** *[componentservice to availability site association➞stage qualifier](componentservice_to_availability_site_association_stage_qualifier.md)*  <sub>OPT</sub>  **[LifecycleStage](LifecycleStage.md)**
 *  **[Association](Association.md)** *[stage qualifier](stage_qualifier.md)*  <sub>OPT</sub>  **[LifecycleStage](LifecycleStage.md)**

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
| **In Subsets:** | | system_model_database |
| **Close Mappings:** | | MAID:2987510170 |
|  | | RO:0002546 |
|  | | sumo:lifeStageAchieved |
| **Narrow Mappings:** | | dwc:lifeStage |
|  | | RO:0002487 |
| **Broad Mappings:** | | csrc:System_Development_Lifecycle |
|  | | csrc:Security_Development_Lifecycle |
|  | | MAID:30452754 |
|  | | WIKIDATA:Q3298282 |
