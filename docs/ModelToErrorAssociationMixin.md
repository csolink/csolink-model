---
parent: Class Mixins
title: csolink:ModelToErrorAssociationMixin
grand_parent: Classes
layout: default
---

# Class: ModelToErrorAssociationMixin


This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the error in a way that is useful for studying the error outside a patient carrying the error

URI: [csolink:ModelToErrorAssociationMixin](https://w3id.org/csolink/vocab/ModelToErrorAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]%3Csubject%201..1-%20[ModelToErrorAssociationMixin%7Cpredicate:predicate_type],[VariantAsAModelOfErrorAssociation]uses%20-.-%3E[ModelToErrorAssociationMixin],[SystemicEntityAsAModelOfErrorAssociation]uses%20-.-%3E[ModelToErrorAssociationMixin],[ServiceunittypeAsAModelOfErrorAssociation]uses%20-.-%3E[ModelToErrorAssociationMixin],[ComponentserviceAsAModelOfErrorAssociation]uses%20-.-%3E[ModelToErrorAssociationMixin],[ComponentTypeAsAModelOfErrorAssociation]uses%20-.-%3E[ModelToErrorAssociationMixin],[VariantAsAModelOfErrorAssociation],[SystemicEntityAsAModelOfErrorAssociation],[ServiceunittypeAsAModelOfErrorAssociation],[ComponentserviceAsAModelOfErrorAssociation],[ComponentTypeAsAModelOfErrorAssociation])

---


## Mixin for

 * [ComponentTypeAsAModelOfErrorAssociation](ComponentTypeAsAModelOfErrorAssociation.md) (mixin) 
 * [ComponentserviceAsAModelOfErrorAssociation](ComponentserviceAsAModelOfErrorAssociation.md) (mixin) 
 * [ServiceunittypeAsAModelOfErrorAssociation](ServiceunittypeAsAModelOfErrorAssociation.md) (mixin) 
 * [SystemicEntityAsAModelOfErrorAssociation](SystemicEntityAsAModelOfErrorAssociation.md) (mixin) 
 * [VariantAsAModelOfErrorAssociation](VariantAsAModelOfErrorAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [model to error association mixin➞predicate](model_to_error_association_mixin_predicate.md)  <sub>REQ</sub>
    * Description: The relationship to the error
    * range: [PredicateType](types/PredicateType.md)
 * [model to error association mixin➞subject](model_to_error_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: The entity that serves as the model of the error. This may be a componentservice, system, a strain of system, a serviceunittype or variant that exhibits similar features, or a componentservice that when migrated exhibits features of the error
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [model to error association mixin➞predicate](model_to_error_association_mixin_predicate.md)  <sub>REQ</sub>
    * Description: The relationship to the error
    * range: [PredicateType](types/PredicateType.md)
 * [model to error association mixin➞subject](model_to_error_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: The entity that serves as the model of the error. This may be a componentservice, system, a strain of system, a serviceunittype or variant that exhibits similar features, or a componentservice that when migrated exhibits features of the error
    * range: [NamedThing](NamedThing.md)
