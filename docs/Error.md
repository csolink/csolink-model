---
parent: Entities
title: csolink:Error
grand_parent: Classes
layout: default
---

# Class: Error




URI: [csolink:Error](https://w3id.org/csolink/vocab/Error)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[NamedThing],[ErrorToEntityAssociationMixin],[ErrorOrObservableFeature],[EntityToErrorAssociationMixin]-%20object%201..1%3E[Error%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ErrorToEntityAssociationMixin]-%20subject%201..1%3E[Error],[ErrorOrObservableFeature]%5E-[Error],[EntityToErrorAssociationMixin],[Attribute],[Agent])

---


## Parents

 *  is_a: [ErrorOrObservableFeature](ErrorOrObservableFeature.md) - Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as distinct, others conflate.

## Referenced by class

 *  **[EntityToErrorAssociationMixin](EntityToErrorAssociationMixin.md)** *[entity to error association mixin➞object](entity_to_error_association_mixin_object.md)*  <sub>REQ</sub>  **[Error](Error.md)**
 *  **[ErrorToEntityAssociationMixin](ErrorToEntityAssociationMixin.md)** *[error to entity association mixin➞subject](error_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[Error](Error.md)**
 *  **[NamedThing](NamedThing.md)** *[manifestation of](manifestation_of.md)*  <sub>0..*</sub>  **[Error](Error.md)**

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
| **Aliases:** | | condition |
|  | | disorder |
|  | | engineering condition |
| **In Subsets:** | | system_model_database |
| **Exact Mappings:** | | NCIT:C43369 |
|  | | schema:error |
|  | | WIKIDATA:Q29485 |
| **Narrow Mappings:** | | CSO:bit_error_rate |
|  | | CSO:localization_error |
|  | | CSO:coding_error |
|  | | CSO:mean_square_error |
|  | | CSO:tracking_error |
|  | | CSO:soft_error |
|  | | CSO:root_mean_square_error |
|  | | CSO:symbol_error_rate |
|  | | CSO:word_error_rate |
|  | | CSO:minimum_mean-square_error |
|  | | CSO:linear_minimum_mean-squared_error |
|  | | CSO:error-prone_channel |
|  | | CSO:linear_minimum_mean_square_error |
|  | | CSO:forecasting_error |
|  | | CSO:equal_error_rate |
|  | | CSO:error_vector_magnitude |
|  | | CSO:soft_error_rate |
|  | | CSO:error_covariance_matrix |
|  | | CSO:multipath_error |
|  | | CSO:timing_error |
|  | | CSO:target_registration_error |
|  | | CSO:radiotherapy_setup_error |
|  | | CSO:bit_error_rate_(ber) |
|  | | CSO:filtering_error |
|  | | CSO:mean_absolute_error |
|  | | CSO:synchronization_error |
|  | | CSO:unequal_error_protection |
|  | | CSO:error_estimate |
|  | | CSO:bit_error |
|  | | CSO:ranging_error |
|  | | CSO:type_error |
|  | | CSO:minimum_classification_error |
|  | | CSO:channel_estimation_error |
|  | | csrc:Bit_Error |
|  | | csrc:Type_I_error |
|  | | NCIT:C53323 |
|  | | NCIT:C92042 |
|  | | NCIT:C19600 |
|  | | sumo:processAborted |
|  | | STATO:0000242 |
|  | | WIKIDATA:Q3847033 |
| **Related Mappings:** | | CSO:error_concealment |
|  | | CSO:error_floor |
|  | | CSO:error_resilience |
|  | | CSO:error_correcting_output_code |
|  | | CSO:bit_error_probability |
|  | | ssn-system:inCondition |

