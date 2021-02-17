---
parent: Class Mixins
title: csolink:EntityToObservableFeatureAssociationMixin
grand_parent: Classes
layout: default
---

# Class: EntityToObservableFeatureAssociationMixin




URI: [csolink:EntityToObservableFeatureAssociationMixin](https://w3id.org/csolink/vocab/EntityToObservableFeatureAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SeverityValue],[Onset],[ObservableFeature],[FrequencyValue],[ObservableFeature]%3Cobject%201..1-%20[EntityToObservableFeatureAssociationMixin%7Cdescription:narrative_text%20%3F],[ComputationalArchitecturalStyle]%3Carchitectural%20style%20qualifier%200..1-++[EntityToObservableFeatureAssociationMixin],[VariantToObservableFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[ServiceunittypeToObservableFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[ExposureEventToObservableFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[ErrorToObservableFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[ComponentserviceToObservableFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[CaseToObservableFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[BehaviorToBehavioralFeatureAssociation]uses%20-.-%3E[EntityToObservableFeatureAssociationMixin],[EntityToFeatureOrErrorQualifiersMixin]%5E-[EntityToObservableFeatureAssociationMixin],[VariantToObservableFeatureAssociation],[ServiceunittypeToObservableFeatureAssociation],[ExposureEventToObservableFeatureAssociation],[ErrorToObservableFeatureAssociation],[EntityToFeatureOrErrorQualifiersMixin],[ComputationalArchitecturalStyle],[ComponentserviceToObservableFeatureAssociation],[CaseToObservableFeatureAssociation],[BehaviorToBehavioralFeatureAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrErrorQualifiersMixin](EntityToFeatureOrErrorQualifiersMixin.md) - Qualifiers for entity to error or observability associations.

## Mixin for

 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) (mixin)  - An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
 * [CaseToObservableFeatureAssociation](CaseToObservableFeatureAssociation.md) (mixin)  - An association between a case (e.g. individual patient) and a observable feature in which the individual has or has had the observability.
 * [ComponentserviceToObservableFeatureAssociation](ComponentserviceToObservableFeatureAssociation.md) (mixin) 
 * [ErrorToObservableFeatureAssociation](ErrorToObservableFeatureAssociation.md) (mixin)  - An association between a error and a observable feature in which the observable feature is associated with the error in some way.
 * [ExposureEventToObservableFeatureAssociation](ExposureEventToObservableFeatureAssociation.md) (mixin)  - Any association between an environment and a observable feature, where being in the environment influences the observability.
 * [ServiceunittypeToObservableFeatureAssociation](ServiceunittypeToObservableFeatureAssociation.md) (mixin)  - Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the observability, either in isolation or through environment
 * [VariantToObservableFeatureAssociation](VariantToObservableFeatureAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [architectural style qualifier](architectural_style_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a observable association to state whether the association is specific to a particular architectural style.
    * range: [ComputationalArchitecturalStyle](ComputationalArchitecturalStyle.md)
 * [entity to observable feature association mixin➞description](entity_to_observable_feature_association_mixin_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this observability, not otherwise covered by the observability ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [entity to observable feature association mixin➞object](entity_to_observable_feature_association_mixin_object.md)  <sub>REQ</sub>
    * Description: observable class
    * range: [ObservableFeature](ObservableFeature.md)

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

 * [entity to observable feature association mixin➞description](entity_to_observable_feature_association_mixin_description.md)  <sub>OPT</sub>
    * Description: A description of specific aspects of this observability, not otherwise covered by the observability ontology class
    * range: [NarrativeText](types/NarrativeText.md)
 * [entity to observable feature association mixin➞object](entity_to_observable_feature_association_mixin_object.md)  <sub>REQ</sub>
    * Description: observable class
    * range: [ObservableFeature](ObservableFeature.md)
