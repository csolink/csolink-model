---
parent: Class Mixins
title: csolink:ModelToDiseaseAssociationMixin
grand_parent: Classes
layout: default
---

# Class: ModelToDiseaseAssociationMixin


This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease

URI: [csolink:ModelToDiseaseAssociationMixin](https://w3id.org/csolink/vocab/ModelToDiseaseAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]%3Csubject%201..1-%20[ModelToDiseaseAssociationMixin%7Cpredicate:predicate_type],[VariantAsAModelOfDiseaseAssociation]uses%20-.-%3E[ModelToDiseaseAssociationMixin],[OrganismalEntityAsAModelOfDiseaseAssociation]uses%20-.-%3E[ModelToDiseaseAssociationMixin],[GenotypeAsAModelOfDiseaseAssociation]uses%20-.-%3E[ModelToDiseaseAssociationMixin],[GeneAsAModelOfDiseaseAssociation]uses%20-.-%3E[ModelToDiseaseAssociationMixin],[CellLineAsAModelOfDiseaseAssociation]uses%20-.-%3E[ModelToDiseaseAssociationMixin],[VariantAsAModelOfDiseaseAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[CellLineAsAModelOfDiseaseAssociation])

---


## Mixin for

 * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) (mixin) 
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) (mixin) 
 * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [model to disease association mixin➞predicate](model_to_disease_association_mixin_predicate.md)  <sub>REQ</sub>
    * Description: The relationship to the disease
    * range: [PredicateType](types/PredicateType.md)
 * [model to disease association mixin➞subject](model_to_disease_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [model to disease association mixin➞predicate](model_to_disease_association_mixin_predicate.md)  <sub>REQ</sub>
    * Description: The relationship to the disease
    * range: [PredicateType](types/PredicateType.md)
 * [model to disease association mixin➞subject](model_to_disease_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease
    * range: [NamedThing](NamedThing.md)
