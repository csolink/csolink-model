---
parent: Class Mixins
title: csolink:EntityToErrorAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToErrorAssociationMixin


mixin class for any association whose object (target node) is a error

URI: [csolink:EntityToErrorAssociationMixin](https://w3id.org/csolink/vocab/EntityToErrorAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyValue],[Error],[EntityToFeatureOrErrorQualifiersMixin],[Error]%3Cobject%201..1-%20[EntityToErrorAssociationMixin],[VariantToErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[VariantAsAModelOfErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[SystemicEntityAsAModelOfErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[ServiceunittypeToErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[ServiceunittypeAsAModelOfErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[ComponentserviceToErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[ComponentserviceAsAModelOfErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[ComponentTypeAsAModelOfErrorAssociation]uses%20-.-%3E[EntityToErrorAssociationMixin],[EntityToFeatureOrErrorQualifiersMixin]%5E-[EntityToErrorAssociationMixin],[VariantToErrorAssociation],[VariantAsAModelOfErrorAssociation],[SystemicEntityAsAModelOfErrorAssociation],[ServiceunittypeToErrorAssociation],[ServiceunittypeAsAModelOfErrorAssociation],[ComponentserviceToErrorAssociation],[ComponentserviceAsAModelOfErrorAssociation],[ComponentTypeAsAModelOfErrorAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrErrorQualifiersMixin](EntityToFeatureOrErrorQualifiersMixin.md) - Qualifiers for entity to error or observability associations.

## Mixin for

 * [ComponentTypeAsAModelOfErrorAssociation](ComponentTypeAsAModelOfErrorAssociation.md) (mixin) 
 * [ComponentserviceAsAModelOfErrorAssociation](ComponentserviceAsAModelOfErrorAssociation.md) (mixin) 
 * [ComponentserviceToErrorAssociation](ComponentserviceToErrorAssociation.md) (mixin) 
 * [ServiceunittypeAsAModelOfErrorAssociation](ServiceunittypeAsAModelOfErrorAssociation.md) (mixin) 
 * [ServiceunittypeToErrorAssociation](ServiceunittypeToErrorAssociation.md) (mixin) 
 * [SystemicEntityAsAModelOfErrorAssociation](SystemicEntityAsAModelOfErrorAssociation.md) (mixin) 
 * [VariantAsAModelOfErrorAssociation](VariantAsAModelOfErrorAssociation.md) (mixin) 
 * [VariantToErrorAssociation](VariantToErrorAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [entity to error association mixin➞object](entity_to_error_association_mixin_object.md)  <sub>REQ</sub>
    * Description: error
    * range: [Error](Error.md)

### Inherited from entity to feature or error qualifiers mixin:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state how severe the observability is in the subject
    * range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state when the observability appears is in the subject
    * range: [Onset](Onset.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state how frequent the observability is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)

### Domain for slot:

 * [entity to error association mixin➞object](entity_to_error_association_mixin_object.md)  <sub>REQ</sub>
    * Description: error
    * range: [Error](Error.md)
