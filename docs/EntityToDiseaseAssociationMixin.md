---
parent: Class Mixins
title: csolink:EntityToDiseaseAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToDiseaseAssociationMixin


mixin class for any association whose object (target node) is a disease

URI: [csolink:EntityToDiseaseAssociationMixin](https://w3id.org/csolink/vocab/EntityToDiseaseAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyValue],[EntityToFeatureOrDiseaseQualifiersMixin],[Disease]%3Cobject%201..1-%20[EntityToDiseaseAssociationMixin],[VariantToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[VariantAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[OrganismalEntityAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[GenotypeToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[GenotypeAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[GeneToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[GeneAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[CellLineAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociationMixin],[EntityToFeatureOrDiseaseQualifiersMixin]%5E-[EntityToDiseaseAssociationMixin],[VariantToDiseaseAssociation],[VariantAsAModelOfDiseaseAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation],[GenotypeToDiseaseAssociation],[GenotypeAsAModelOfDiseaseAssociation],[GeneToDiseaseAssociation],[GeneAsAModelOfDiseaseAssociation],[Disease],[CellLineAsAModelOfDiseaseAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) - Qualifiers for entity to disease or phenotype associations.

## Mixin for

 * [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) (mixin) 
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) (mixin) 
 * [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) (mixin) 
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [entity to disease association mixin➞object](entity_to_disease_association_mixin_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)
    * Example:    

### Inherited from entity to feature or disease qualifiers mixin:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)

### Domain for slot:

 * [entity to disease association mixin➞object](entity_to_disease_association_mixin_object.md)  <sub>REQ</sub>
    * Description: disease
    * range: [Disease](Disease.md)
    * Example:    
