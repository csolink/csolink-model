---
parent: Entities
title: csolink:DeploymentEntity
grand_parent: Classes
layout: default
---

# Class: DeploymentEntity


A process location, serviceunit type or gross deployment part

URI: [csolink:DeploymentEntity](https://w3id.org/csolink/vocab/DeploymentEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[SystemicEntity],[SystemTaxon],[Serviceunit],[NamedThing],[GrossDeploymentStructure],[FaultyDeploymentStructure],[ErrorOrObservableFeatureToLocationAssociation],[ErrorOrObservableFeatureAssociationToLocationAssociation],[DeploymentEntityToDeploymentEntityPartOfAssociation],[DeploymentEntityToDeploymentEntityOntogenicAssociation],[DeploymentEntityToDeploymentEntityAssociation],[ComponentserviceAvailabilityMixin]-%20availability%20site%200..1%3E[DeploymentEntity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ComponentserviceToAvailabilitySiteAssociation]-%20object%201..1%3E[DeploymentEntity],[DeploymentEntityToDeploymentEntityAssociation]-%20object%201..1%3E[DeploymentEntity],[DeploymentEntityToDeploymentEntityAssociation]-%20subject%201..1%3E[DeploymentEntity],[DeploymentEntityToDeploymentEntityOntogenicAssociation]-%20object%201..1%3E[DeploymentEntity],[DeploymentEntityToDeploymentEntityOntogenicAssociation]-%20subject%201..1%3E[DeploymentEntity],[DeploymentEntityToDeploymentEntityPartOfAssociation]-%20object%201..1%3E[DeploymentEntity],[DeploymentEntityToDeploymentEntityPartOfAssociation]-%20subject%201..1%3E[DeploymentEntity],[ErrorOrObservableFeatureAssociationToLocationAssociation]-%20object%201..1%3E[DeploymentEntity],[ErrorOrObservableFeatureToLocationAssociation]-%20object%201..1%3E[DeploymentEntity],[DeploymentEntity]uses%20-.-%3E[ThingWithTaxon],[DeploymentEntity]uses%20-.-%3E[CyberEssence],[DeploymentEntity]%5E-[Serviceunit],[DeploymentEntity]%5E-[GrossDeploymentStructure],[DeploymentEntity]%5E-[FaultyDeploymentStructure],[DeploymentEntity]%5E-[Component],[SystemicEntity]%5E-[DeploymentEntity],[CyberEssence],[ComponentserviceToAvailabilitySiteAssociation],[ComponentserviceOrServicetype],[ComponentserviceAvailabilityMixin],[Component],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes
 *  mixin: [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.

## Children

 * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
 * [FaultyDeploymentStructure](FaultyDeploymentStructure.md) - An deployment structure with the potential of have an abnormal or deleterious effect at the process, serviceunit, multiserviceunit, or systemal level.
 * [GrossDeploymentStructure](GrossDeploymentStructure.md)
 * [Serviceunit](Serviceunit.md) - The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a cluster. It can be deployed, isolated, and repaired independently.

## Referenced by class

 *  **[Association](Association.md)** *[availability site](availability_site.md)*  <sub>OPT</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)** *[available in](available_in.md)*  <sub>0..*</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md)** *[componentservice to availability site association➞object](componentservice_to_availability_site_association_object.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[DeploymentEntityToDeploymentEntityAssociation](DeploymentEntityToDeploymentEntityAssociation.md)** *[deployment entity to deployment entity association➞object](deployment_entity_to_deployment_entity_association_object.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[DeploymentEntityToDeploymentEntityAssociation](DeploymentEntityToDeploymentEntityAssociation.md)** *[deployment entity to deployment entity association➞subject](deployment_entity_to_deployment_entity_association_subject.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[DeploymentEntityToDeploymentEntityOntogenicAssociation](DeploymentEntityToDeploymentEntityOntogenicAssociation.md)** *[deployment entity to deployment entity ontogenic association➞object](deployment_entity_to_deployment_entity_ontogenic_association_object.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[DeploymentEntityToDeploymentEntityOntogenicAssociation](DeploymentEntityToDeploymentEntityOntogenicAssociation.md)** *[deployment entity to deployment entity ontogenic association➞subject](deployment_entity_to_deployment_entity_ontogenic_association_subject.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[DeploymentEntityToDeploymentEntityPartOfAssociation](DeploymentEntityToDeploymentEntityPartOfAssociation.md)** *[deployment entity to deployment entity part of association➞object](deployment_entity_to_deployment_entity_part_of_association_object.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[DeploymentEntityToDeploymentEntityPartOfAssociation](DeploymentEntityToDeploymentEntityPartOfAssociation.md)** *[deployment entity to deployment entity part of association➞subject](deployment_entity_to_deployment_entity_part_of_association_subject.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[ErrorOrObservableFeatureAssociationToLocationAssociation](ErrorOrObservableFeatureAssociationToLocationAssociation.md)** *[error or observable feature association to location association➞object](error_or_observable_feature_association_to_location_association_object.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**
 *  **[ErrorOrObservableFeatureToLocationAssociation](ErrorOrObservableFeatureToLocationAssociation.md)** *[error or observable feature to location association➞object](error_or_observable_feature_to_location_association_object.md)*  <sub>REQ</sub>  **[DeploymentEntity](DeploymentEntity.md)**

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
| **Close Mappings:** | | WIKIDATA:Q4936952 |
| **Narrow Mappings:** | | csrc:Platform |
|  | | MAID:9390403 |
|  | | MAID:105339364 |
|  | | csrc:Public_cloud |
|  | | csrc:cloud_computing |
|  | | csrc:Private_cloud |
|  | | csrc:Hybrid_cloud |
|  | | csrc:Java_Platform_Enterprise_Edition |
|  | | csrc:Platform_as_a_Service |
| **Broad Mappings:** | | MAID:96711827 |
|  | | WIKIDATA:Q3055454 |

