---
parent: Other Classes
title: csolink:Componentservice
grand_parent: Classes
layout: default
---

# Class: Componentservice


A component service.

URI: [csolink:Componentservice](https://w3id.org/csolink/vocab/Componentservice)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToComponentserviceAssociation],[ServiceunittypeToComponentserviceAssociation],[SequenceVariant],[NamedThing],[ErrorOrObservableFeature],[ComponentserviceinstanceToComponentserviceRelationship],[ComponentserviceToServicetypeRelationship],[ComponentserviceOrServicetype],[ComponentserviceToServicetypeRelationship]++-%20subject%201..1%3E[Componentservice%7Csymbol:string%20%3F;synonym:label_type%20%2A;xref:iri_type%20%2A;name(i):symbol_type%20%3F],[ComponentserviceinstanceToComponentserviceRelationship]++-%20object%201..1%3E[Componentservice],[SequenceVariant]++-%20has%20componentservice(i)%200..%2A%3E[Componentservice],[ComponentserviceGroupingMixin]++-%20has%20componentservice%20or%20servicetype%200..%2A%3E[Componentservice],[SequenceVariant]++-%20has%20componentservice%200..%2A%3E[Componentservice],[ServiceunittypeToComponentserviceAssociation]++-%20object%201..1%3E[Componentservice],[VariantToComponentserviceAssociation]++-%20object%201..1%3E[Componentservice],[Componentservice]uses%20-.-%3E[ComponentserviceOrServicetype],[ComponentserviceOrServicetype]%5E-[Componentservice],[ComponentserviceGroupingMixin])

---


## Parents

 *  is_a: [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md) - a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another

## Uses Mixins

 *  mixin: [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md) - a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another

## Referenced by class

 *  **[ComponentserviceToServicetypeRelationship](ComponentserviceToServicetypeRelationship.md)** *[componentservice to servicetype relationship➞subject](componentservice_to_servicetype_relationship_subject.md)*  <sub>REQ</sub>  **[Componentservice](Componentservice.md)**
 *  **[ComponentserviceinstanceToComponentserviceRelationship](ComponentserviceinstanceToComponentserviceRelationship.md)** *[componentserviceinstance to componentservice relationship➞object](componentserviceinstance_to_componentservice_relationship_object.md)*  <sub>REQ</sub>  **[Componentservice](Componentservice.md)**
 *  **[ErrorOrObservableFeature](ErrorOrObservableFeature.md)** *[condition associated with componentservice](condition_associated_with_componentservice.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[NamedThing](NamedThing.md)** *[has componentservice](has_componentservice.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[NamedThing](NamedThing.md)** *[has componentservice or servicetype](has_componentservice_or_servicetype.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is missense variant of](is_missense_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is nearby variant of](is_nearby_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is non coding variant of](is_non_coding_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is nonsense variant of](is_nonsense_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is protocol variant of](is_protocol_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is splice site variant of](is_splice_site_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is synonymous variant of](is_synonymous_variant_of.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[sequence variant➞has componentservice](sequence_variant_has_componentservice.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[Componentservice](Componentservice.md)** *[service interacts with](service_interacts_with.md)*  <sub>0..*</sub>  **[Componentservice](Componentservice.md)**
 *  **[ServiceunittypeToComponentserviceAssociation](ServiceunittypeToComponentserviceAssociation.md)** *[serviceunittype to componentservice association➞object](serviceunittype_to_componentservice_association_object.md)*  <sub>REQ</sub>  **[Componentservice](Componentservice.md)**
 *  **[VariantToComponentserviceAssociation](VariantToComponentserviceAssociation.md)** *[variant to componentservice association➞object](variant_to_componentservice_association_object.md)*  <sub>REQ</sub>  **[Componentservice](Componentservice.md)**

## Attributes


### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | locus |
|  | | cs |
| **In Subsets:** | | system_model_database |
| **Broad Mappings:** | | csrc:Resource_Type |
|  | | OSO:hasComponentType |
|  | | schema:serviceType |

