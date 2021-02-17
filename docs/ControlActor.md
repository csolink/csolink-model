---
parent: Entities
title: csolink:ControlActor
grand_parent: Classes
layout: default
---

# Class: ControlActor


May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part

URI: [csolink:ControlActor](https://w3id.org/csolink/vocab/ControlActor)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon],[Power],[OrchestrationToOrchestrationDerivationAssociation],[OrchestrationToOrchestrationAssociation],[OrchestrationToEntityAssociationMixin],[OrchestrationExposure],[OperationalEntity],[OperationalActivity],[NotificationComponent],[NamedThing],[Controller],[Cluster]-%20has%20control%20actor%200..%2A%3E[ControlActor%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[OperationalActivity]-%20has%20input%200..%2A%3E[ControlActor],[OperationalActivity]-%20has%20output%200..%2A%3E[ControlActor],[OrchestrationToEntityAssociationMixin]-%20subject%201..1%3E[ControlActor],[OrchestrationToOrchestrationAssociation]-%20object%201..1%3E[ControlActor],[OrchestrationToOrchestrationDerivationAssociation]-%20object%201..1%3E[ControlActor],[OrchestrationToOrchestrationDerivationAssociation]-%20subject%201..1%3E[ControlActor],[ControlActor]%5E-[Power],[ControlActor]%5E-[OrchestrationExposure],[ControlActor]%5E-[NotificationComponent],[ControlActor]%5E-[Controller],[ControlActor]%5E-[ConsumedResource],[OperationalEntity]%5E-[ControlActor],[ConsumedResource],[Cluster],[Attribute],[Agent],[AdministrativeOperation])

---


## Parents

 *  is_a: [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

## Children

 * [ConsumedResource](ConsumedResource.md) - A control actor (often a cluster) consumed for information, engineering or technical use.
 * [Controller](Controller.md) - Any intermediate or servicetype resulting from director supervision. Includes primary and secondary controllers.
 * [NotificationComponent](NotificationComponent.md)
 * [OrchestrationExposure](OrchestrationExposure.md) - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
 * [Power](Power.md)

## Referenced by class

 *  **[AdministrativeOperation](AdministrativeOperation.md)** *[has active ingredient](has_active_ingredient.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[NamedThing](NamedThing.md)** *[has control actor](has_control_actor.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[ControlActor](ControlActor.md)** *[has controller](has_controller.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[AdministrativeOperation](AdministrativeOperation.md)** *[has excipient](has_excipient.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[ControlActor](ControlActor.md)** *[is controller of](is_controller_of.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[OperationalActivity](OperationalActivity.md)** *[operational activity➞has input](operational_activity_has_input.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[OperationalActivity](OperationalActivity.md)** *[operational activity➞has output](operational_activity_has_output.md)*  <sub>0..*</sub>  **[ControlActor](ControlActor.md)**
 *  **[OrchestrationToEntityAssociationMixin](OrchestrationToEntityAssociationMixin.md)** *[orchestration to entity association mixin➞subject](orchestration_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[ControlActor](ControlActor.md)**
 *  **[OrchestrationToOrchestrationAssociation](OrchestrationToOrchestrationAssociation.md)** *[orchestration to orchestration association➞object](orchestration_to_orchestration_association_object.md)*  <sub>REQ</sub>  **[ControlActor](ControlActor.md)**
 *  **[OrchestrationToOrchestrationDerivationAssociation](OrchestrationToOrchestrationDerivationAssociation.md)** *[orchestration to orchestration derivation association➞object](orchestration_to_orchestration_derivation_association_object.md)*  <sub>REQ</sub>  **[ControlActor](ControlActor.md)**
 *  **[OrchestrationToOrchestrationDerivationAssociation](OrchestrationToOrchestrationDerivationAssociation.md)** *[orchestration to orchestration derivation association➞subject](orchestration_to_orchestration_derivation_association_subject.md)*  <sub>REQ</sub>  **[ControlActor](ControlActor.md)**

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
| **In Subsets:** | | system_model_database |
| **Exact Mappings:** | | CTRL:ControlActor |
| **Narrow Mappings:** | | CSO:data_planes |
|  | | csrc:controlled |
|  | | csrc:controlled_access_area |
|  | | csrc:controlled_area |
|  | | csrc:controlled_interface |
|  | | csrc:controlled_space |
|  | | csrc:Control_Group |
|  | | csrc:Orchestrator |
|  | | csrc:Orchestration |
|  | | csrc:threat_actor |
|  | | csrc:Transmission_Power_Control |
|  | | CTRL:isSupervisedBy |
|  | | CTRL:supervises |
|  | | EFO:0009743 |
|  | | MAID:10597312 |
|  | | NCIT:C72011 |
|  | | NCIT:C134832 |
|  | | NCIT:C49887 |
|  | | SAN:consumes |
|  | | SAN:controlledBy |
|  | | SAN:isActedUponBy |
|  | | sosa:Actuator |
|  | | sosa:isObservedBy |
|  | | sosa:Actuator |
|  | | sosa:isActedOnBy |
|  | | sosa:isObservedBy |
|  | | sosa:observes |
|  | | sosa:Platform |
|  | | ssn:isProxyFor |
|  | | sumo:Controller |
|  | | sumo:controlled |
|  | | sumo:controlGroup |
|  | | sumo:ExternalAgency |
|  | | sumo:managedBy |
|  | | sumo:operator |
|  | | WIKIDATA:Q85850438 |
| **Related Mappings:** | | CSO:control_system |
|  | | MAID:48209547 |
|  | | schema:ControlAction |
|  | | WIKIDATA:Q1331104 |

