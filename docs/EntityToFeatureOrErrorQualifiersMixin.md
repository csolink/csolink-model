---
parent: Class Mixins
title: csolink:EntityToFeatureOrErrorQualifiersMixin
grand_parent: Classes
layout: default
---

# Class: EntityToFeatureOrErrorQualifiersMixin


Qualifiers for entity to error or observability associations.

URI: [csolink:EntityToFeatureOrErrorQualifiersMixin](https://w3id.org/csolink/vocab/EntityToFeatureOrErrorQualifiersMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[FrequencyValue],[FrequencyQualifierMixin],[EntityToObservableFeatureAssociationMixin],[Onset]%3Conset%20qualifier%200..1-++[EntityToFeatureOrErrorQualifiersMixin],[SeverityValue]%3Cseverity%20qualifier%200..1-++[EntityToFeatureOrErrorQualifiersMixin],[EntityToFeatureOrErrorQualifiersMixin]%5E-[EntityToObservableFeatureAssociationMixin],[EntityToFeatureOrErrorQualifiersMixin]%5E-[EntityToErrorAssociationMixin],[FrequencyQualifierMixin]%5E-[EntityToFeatureOrErrorQualifiersMixin],[EntityToErrorAssociationMixin])

---


## Parents

 *  is_a: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations

## Children

 * [EntityToErrorAssociationMixin](EntityToErrorAssociationMixin.md) - mixin class for any association whose object (target node) is a error
 * [EntityToObservableFeatureAssociationMixin](EntityToObservableFeatureAssociationMixin.md)

## Referenced by class


## Attributes


### Own

 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state when the observability appears is in the subject
    * range: [Onset](Onset.md)
 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state how severe the observability is in the subject
    * range: [SeverityValue](SeverityValue.md)

### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state how frequent the observability is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
