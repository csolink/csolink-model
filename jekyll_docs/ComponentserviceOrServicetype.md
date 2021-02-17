---
parent: Class Mixins
title: csolink:ComponentserviceOrServicetype
grand_parent: Classes
layout: default
---

# Class: ComponentserviceOrServicetype


a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another

URI: [csolink:ComponentserviceOrServicetype](https://w3id.org/csolink/vocab/ComponentserviceOrServicetype)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ServicetypeMixin],[OrchestrationToComponentserviceAssociation],[MacrooperationalMachineMixin],[DeploymentEntity],[ComponentserviceToObservableFeatureAssociation],[ComponentserviceToErrorAssociation],[ComponentserviceToEntityAssociationMixin],[ComponentserviceToComponentserviceAssociation],[ComponentserviceToAvailabilitySiteAssociation],[ComponentserviceRegulatoryRelationship],[AdministrativeOperationalToComponentserviceAssociation]++-%20object%201..1%3E[ComponentserviceOrServicetype%7Cname(i):symbol_type%20%3F],[ComponentserviceAsAModelOfErrorAssociation]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceHasVariantThatContributesToErrorAssociation]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceRegulatoryRelationship]++-%20object%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceRegulatoryRelationship]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceToAvailabilitySiteAssociation]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceToComponentserviceAssociation]++-%20object%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceToComponentserviceAssociation]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceToEntityAssociationMixin]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceToErrorAssociation]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[ComponentserviceToObservableFeatureAssociation]++-%20subject%201..1%3E[ComponentserviceOrServicetype],[OrchestrationToComponentserviceAssociation]++-%20object%201..1%3E[ComponentserviceOrServicetype],[Componentservice]uses%20-.-%3E[ComponentserviceOrServicetype],[ComponentserviceOrServicetype]%5E-[ServicetypeMixin],[ComponentserviceOrServicetype]%5E-[Componentservice],[MacrooperationalMachineMixin]%5E-[ComponentserviceOrServicetype],[ComponentserviceHasVariantThatContributesToErrorAssociation],[ComponentserviceAsAModelOfErrorAssociation],[Componentservice],[AdministrativeOperationalToComponentserviceAssociation])

---


## Parents

 *  is_a: [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md) - A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a component. They either carry out individual computational activities, or they encode tasks which do this.

## Children

 * [Componentservice](Componentservice.md) - A component service.
 * [ServicetypeMixin](ServicetypeMixin.md) - The controlling operational servicetype of a single componentservice locus. ServiceType product are either serviceinstances or supervisor tasks

## Mixin for

 * [Componentservice](Componentservice.md) (mixin)  - A component service.

## Referenced by class

 *  **[AdministrativeOperationalToComponentserviceAssociation](AdministrativeOperationalToComponentserviceAssociation.md)** *[administrative operational to componentservice association➞object](administrative_operational_to_componentservice_association_object.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)** *[coavailable with](coavailable_with.md)*  <sub>0..*</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceAsAModelOfErrorAssociation](ComponentserviceAsAModelOfErrorAssociation.md)** *[componentservice as a model of error association➞subject](componentservice_as_a_model_of_error_association_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceHasVariantThatContributesToErrorAssociation](ComponentserviceHasVariantThatContributesToErrorAssociation.md)** *[componentservice has variant that contributes to error association➞subject](componentservice_has_variant_that_contributes_to_error_association_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceRegulatoryRelationship](ComponentserviceRegulatoryRelationship.md)** *[componentservice regulatory relationship➞object](componentservice_regulatory_relationship_object.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceRegulatoryRelationship](ComponentserviceRegulatoryRelationship.md)** *[componentservice regulatory relationship➞subject](componentservice_regulatory_relationship_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md)** *[componentservice to availability site association➞subject](componentservice_to_availability_site_association_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceToComponentserviceAssociation](ComponentserviceToComponentserviceAssociation.md)** *[componentservice to componentservice association➞object](componentservice_to_componentservice_association_object.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceToComponentserviceAssociation](ComponentserviceToComponentserviceAssociation.md)** *[componentservice to componentservice association➞subject](componentservice_to_componentservice_association_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceToEntityAssociationMixin](ComponentserviceToEntityAssociationMixin.md)** *[componentservice to entity association mixin➞subject](componentservice_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceToErrorAssociation](ComponentserviceToErrorAssociation.md)** *[componentservice to error association➞subject](componentservice_to_error_association_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceToObservableFeatureAssociation](ComponentserviceToObservableFeatureAssociation.md)** *[componentservice to observable feature association➞subject](componentservice_to_observable_feature_association_subject.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)** *[in complex with](in_complex_with.md)*  <sub>0..*</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)** *[in pathway with](in_pathway_with.md)*  <sub>0..*</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)** *[in serviceunit population with](in_serviceunit_population_with.md)*  <sub>0..*</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[OrchestrationToComponentserviceAssociation](OrchestrationToComponentserviceAssociation.md)** *[orchestration to componentservice association➞object](orchestration_to_componentservice_association_object.md)*  <sub>REQ</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**
 *  **[DeploymentEntity](DeploymentEntity.md)** *[unavailable in](unavailable_in.md)*  <sub>0..*</sub>  **[ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)**

## Attributes


### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
