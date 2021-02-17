---
parent: Entities
title: csolink:OperationalEntity
grand_parent: Classes
layout: default
---

# Class: OperationalEntity


A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

URI: [csolink:OperationalEntity](https://w3id.org/csolink/vocab/OperationalEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[ThingWithTaxon],[SystemTaxon],[PairwiseOperationallyInteraction],[OperationalEntityToEntityAssociationMixin],[ComponentserviceToGoTermAssociation]-%20subject%201..1%3E[OperationalEntity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[OperationalEntityToEntityAssociationMixin]-%20subject%201..1%3E[OperationalEntity],[PairwiseOperationallyInteraction]-%20object%201..1%3E[OperationalEntity],[PairwiseOperationallyInteraction]-%20subject%201..1%3E[OperationalEntity],[OperationalEntity]uses%20-.-%3E[ThingWithTaxon],[OperationalEntity]uses%20-.-%3E[CyberEssence],[OperationalEntity]%5E-[WorkloadEntity],[OperationalEntity]%5E-[Notification],[OperationalEntity]%5E-[ControlActor],[OperationalEntity]%5E-[ComponentserviceFamily],[OperationalEntity]%5E-[AdministrativeOperation],[ComputationalEntity]%5E-[OperationalEntity],[Notification],[NamedThing],[ErrorOrObservableFeature],[CyberEssence],[ControlActor],[ComputationalEntity],[ComponentserviceToGoTermAssociation],[ComponentserviceFamily],[Attribute],[Agent],[AdministrativeOperation])

---


## Parents

 *  is_a: [ComputationalEntity](ComputationalEntity.md)

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes
 *  mixin: [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.

## Children

 * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
 * [ComponentserviceFamily](ComponentserviceFamily.md) - any grouping of multiple componentservices or servicetypes related by common descent
 * [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part
 * [Notification](Notification.md) - A event consumed by a healthy system as a source of information
 * [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

## Referenced by class

 *  **[OperationalEntity](OperationalEntity.md)** *[affects abundance of](affects_abundance_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects activity of](affects_activity_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects assignment of](affects_assignment_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects degradation of](affects_degradation_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects instantiation of](affects_instantiation_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects localization of](affects_localization_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects operational modification of](affects_operational_modification_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects output of](affects_output_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects response to](affects_response_to.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects stability of](affects_stability_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects supervision of](affects_supervision_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects transport of](affects_transport_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects uptake of](affects_uptake_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[ComponentserviceToGoTermAssociation](ComponentserviceToGoTermAssociation.md)** *[componentservice to go term association➞subject](componentservice_to_go_term_association_subject.md)*  <sub>REQ</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases abundance of](decreases_abundance_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases activity of](decreases_activity_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases assignment of](decreases_assignment_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases degradation of](decreases_degradation_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases instantiation of](decreases_instantiation_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases localization of](decreases_localization_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases operational interaction](decreases_operational_interaction.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases operational modification of](decreases_operational_modification_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases output of](decreases_output_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases response to](decreases_response_to.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases stability of](decreases_stability_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases supervision of](decreases_supervision_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases transport of](decreases_transport_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases uptake of](decreases_uptake_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)** *[has marker](has_marker.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases abundance of](increases_abundance_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases activity of](increases_activity_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases assignment of](increases_assignment_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases degradation of](increases_degradation_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases instantiation of](increases_instantiation_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases localization of](increases_localization_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases operational interaction](increases_operational_interaction.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases operational modification of](increases_operational_modification_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases output of](increases_output_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases response to](increases_response_to.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases stability of](increases_stability_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases supervision of](increases_supervision_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases transport of](increases_transport_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases uptake of](increases_uptake_of.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[negatively regulated by, entity to entity](negatively_regulated_by_entity_to_entity.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntityToEntityAssociationMixin](OperationalEntityToEntityAssociationMixin.md)** *[operational entity to entity association mixin➞subject](operational_entity_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[operationally interacts with](operationally_interacts_with.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[PairwiseOperationallyInteraction](PairwiseOperationallyInteraction.md)** *[pairwise operationally interaction➞object](pairwise_operationally_interaction_object.md)*  <sub>REQ</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[PairwiseOperationallyInteraction](PairwiseOperationallyInteraction.md)** *[pairwise operationally interaction➞subject](pairwise_operationally_interaction_subject.md)*  <sub>REQ</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[positively regulated by, entity to entity](positively_regulated_by_entity_to_entity.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[positively regulates, entity to entity](positively_regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[regulated by, entity to entity](regulated_by_entity_to_entity.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[regulates, entity to entity](regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[OperationalEntity](OperationalEntity.md)**

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
| **Aliases:** | | csoentity |
| **Narrow Mappings:** | | csrc:operational_technology |
|  | | NCIT:C47908 |
|  | | schema:operatingSystem |
|  | | ssn:Deployment |
|  | | sumo:Computer |
|  | | sumo:ComputerProgram |
|  | | sumo:ComputerProcess |
|  | | sumo:ComputerResource |
|  | | sumo:computerRunning |
|  | | sumo:OperationalAmplifier |
|  | | sumo:Server |
| **Broad Mappings:** | | sumo:ComputerComponent |
| **Related Mappings:** | | CSO:operational_profile |
|  | | geolink:hasOperationArea |
|  | | geolink:hasOperator |
|  | | geolink:isOperatorOf |

