---
parent: Entities
title: csolink:ObservableFeature
grand_parent: Classes
layout: default
---

# Class: ObservableFeature




URI: [csolink:ObservableFeature](https://w3id.org/csolink/vocab/ObservableFeature)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[EntityToObservableFeatureAssociationMixin]-%20object%201..1%3E[ObservableFeature%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ObservableFeature]%5E-[EmpiricalFinding],[ObservableFeature]%5E-[BehavioralFeature],[ErrorOrObservableFeature]%5E-[ObservableFeature],[NamedThing],[ErrorOrObservableFeature],[EntityToObservableFeatureAssociationMixin],[EmpiricalFinding],[ComputationalEntity],[BehavioralFeature],[Attribute],[Agent])

---


## Parents

 *  is_a: [ErrorOrObservableFeature](ErrorOrObservableFeature.md) - Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as distinct, others conflate.

## Children

 * [BehavioralFeature](BehavioralFeature.md) - A observable feature which is behavioral in nature.
 * [EmpiricalFinding](EmpiricalFinding.md) - this category is currently considered broad enough to tag empirical lab measurements and other computational attributes taken as 'empirical traits' with some statistical score, for example, a p value in componentservice associations.

## Referenced by class

 *  **[EntityToObservableFeatureAssociationMixin](EntityToObservableFeatureAssociationMixin.md)** *[entity to observable feature association mixin➞object](entity_to_observable_feature_association_mixin_object.md)*  <sub>REQ</sub>  **[ObservableFeature](ObservableFeature.md)**
 *  **[ComputationalEntity](ComputationalEntity.md)** *[has observability](has_observability.md)*  <sub>0..*</sub>  **[ObservableFeature](ObservableFeature.md)**

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sign |
|  | | symptom |
|  | | observability |
|  | | trait |
|  | | condition |
| **In Subsets:** | | system_model_database |
| **Exact Mappings:** | | csrc:Features |
|  | | sumo:result |
|  | | sumo:status |
|  | | WIKIDATA:Q4485156 |
| **Narrow Mappings:** | | MAID:32848918 |
|  | | MAID:40608802 |
|  | | NCIT:C73619 |
|  | | sumo:BeginFn |
|  | | sumo:BeginningOperations |
|  | | sumo:hostStatus |
|  | | sumo:On |
|  | | sumo:StateChange |
|  | | sumo:stateOfProcess |
|  | | WIKIDATA:Q567555 |
|  | | WIKIDATA:Q24238419 |
|  | | WIKIDATA:Q1375683 |
|  | | WIKIDATA:Q813912 |
|  | | WIKIDATA:Q169872 |
|  | | WIKIDATA:Q1207505 |
| **Broad Mappings:** | | CSO:observability |
|  | | MAID:59345033 |
|  | | MAID:32848918 |
|  | | sumo:ObservationAndMonitoring |
| **Related Mappings:** | | csrc:Feature_set |
|  | | NCIT:C3367 |

