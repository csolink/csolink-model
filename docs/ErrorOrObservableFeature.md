---
parent: Entities
title: csolink:ErrorOrObservableFeature
grand_parent: Classes
layout: default
---

# Class: ErrorOrObservableFeature


Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as distinct, others conflate.

URI: [csolink:ErrorOrObservableFeature](https://w3id.org/csolink/vocab/ErrorOrObservableFeature)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[SystemTaxon],[Repairing],[OrchestrationToErrorOrObservableFeatureAssociation],[OperationalEntity],[ObservableFeature],[NamedThing],[ErrorOrObservableFeatureToEntityAssociationMixin],[ErrorOrObservableFeatureOutcome],[ErrorOrObservableFeatureExposure],[ComponentTypeToErrorOrObservableFeatureAssociation]-%20subject%201..1%3E[ErrorOrObservableFeature%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[EntityToErrorOrObservableFeatureAssociationMixin]-%20object%201..1%3E[ErrorOrObservableFeature],[ErrorOrObservableFeatureToEntityAssociationMixin]-%20subject%201..1%3E[ErrorOrObservableFeature],[ComponentserviceAvailabilityMixin]-%20observable%20state%200..1%3E[ErrorOrObservableFeature],[OrchestrationToErrorOrObservableFeatureAssociation]-%20object%201..1%3E[ErrorOrObservableFeature],[ErrorOrObservableFeature]uses%20-.-%3E[ThingWithTaxon],[ErrorOrObservableFeature]%5E-[ObservableFeature],[ErrorOrObservableFeature]%5E-[ErrorOrObservableFeatureOutcome],[ErrorOrObservableFeature]%5E-[ErrorOrObservableFeatureExposure],[ErrorOrObservableFeature]%5E-[Error],[ComputationalEntity]%5E-[ErrorOrObservableFeature],[Error],[EntityToErrorOrObservableFeatureAssociationMixin],[ComputationalEntity],[ComponentserviceAvailabilityMixin],[Componentservice],[ComponentTypeToErrorOrObservableFeatureAssociation],[Attribute],[Association],[Agent],[AdministrativeOperation])

---


## Parents

 *  is_a: [ComputationalEntity](ComputationalEntity.md)

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes

## Children

 * [Error](Error.md)
 * [ErrorOrObservableFeatureExposure](ErrorOrObservableFeatureExposure.md) - A error or observable feature exposure is where a error state is manifested which represents an precondition, leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular error.
 * [ErrorOrObservableFeatureOutcome](ErrorOrObservableFeatureOutcome.md) - logical outcomes resulting from an exposure event which is the manifestation of a error or other characteristic observability.
 * [ObservableFeature](ObservableFeature.md)

## Referenced by class

 *  **[ComputationalEntity](ComputationalEntity.md)** *[ameliorates](ameliorates.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[Repairing](Repairing.md)** *[approved to repair](approved_to_repair.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[AdministrativeOperation](AdministrativeOperation.md)** *[causes adverse event](causes_adverse_event.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[ComponentTypeToErrorOrObservableFeatureAssociation](ComponentTypeToErrorOrObservableFeatureAssociation.md)** *[component type to error or observable feature association➞subject](component_type_to_error_or_observable_feature_association_subject.md)*  <sub>REQ</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[Componentservice](Componentservice.md)** *[componentservice associated with condition](componentservice_associated_with_condition.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[AdministrativeOperation](AdministrativeOperation.md)** *[contraindicated for](contraindicated_for.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[EntityToErrorOrObservableFeatureAssociationMixin](EntityToErrorOrObservableFeatureAssociationMixin.md)** *[entity to error or observable feature association mixin➞object](entity_to_error_or_observable_feature_association_mixin_object.md)*  <sub>REQ</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[ErrorOrObservableFeatureToEntityAssociationMixin](ErrorOrObservableFeatureToEntityAssociationMixin.md)** *[error or observable feature to entity association mixin➞subject](error_or_observable_feature_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[ComputationalEntity](ComputationalEntity.md)** *[exacerbates](exacerbates.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[marker for](marker_for.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[Association](Association.md)** *[observable state](observable_state.md)*  <sub>OPT</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[OrchestrationToErrorOrObservableFeatureAssociation](OrchestrationToErrorOrObservableFeatureAssociation.md)** *[orchestration to error or observable feature association➞object](orchestration_to_error_or_observable_feature_association_object.md)*  <sub>REQ</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**
 *  **[Repairing](Repairing.md)** *[repairs](repairs.md)*  <sub>0..*</sub>  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)**

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
| **Aliases:** | | phenome |
| **Narrow Mappings:** | | NCIT:C3367 |
|  | | CSO:partial_observation |
|  | | csrc:Cyber_Observable_eXpression |

