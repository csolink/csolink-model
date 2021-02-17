---
parent: Class Mixins
title: csolink:ExposureEvent
grand_parent: Classes
layout: default
---

# Class: ExposureEvent


A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more observability of that system, potentially mediated by serviceunits

URI: [csolink:ExposureEvent](https://w3id.org/csolink/vocab/ExposureEvent)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ExposureEventToObservableFeatureAssociation],[ExposureEventToEntityAssociationMixin],[EntityToExposureEventAssociationMixin]++-%20object%201..1%3E[ExposureEvent%7Ctimepoint:time_type%20%3F],[ExposureEventToEntityAssociationMixin]++-%20subject%201..1%3E[ExposureEvent],[ExposureEventToObservableFeatureAssociation]++-%20subject%201..1%3E[ExposureEvent],[SocioeconomicExposure]uses%20-.-%3E[ExposureEvent],[ServiceBackgroundExposure]uses%20-.-%3E[ExposureEvent],[Repairing]uses%20-.-%3E[ExposureEvent],[OrchestrationExposure]uses%20-.-%3E[ExposureEvent],[GeographicExposure]uses%20-.-%3E[ExposureEvent],[FaultyProcessExposure]uses%20-.-%3E[ExposureEvent],[FaultyDeploymentExposure]uses%20-.-%3E[ExposureEvent],[ErrorOrObservableFeatureExposure]uses%20-.-%3E[ExposureEvent],[EnvironmentalExposure]uses%20-.-%3E[ExposureEvent],[BioticExposure]uses%20-.-%3E[ExposureEvent],[BehavioralExposure]uses%20-.-%3E[ExposureEvent],[AdministrativeOperationalExposure]uses%20-.-%3E[ExposureEvent],[SocioeconomicExposure],[ServiceBackgroundExposure],[Repairing],[OrchestrationExposure],[GeographicExposure],[FaultyProcessExposure],[FaultyDeploymentExposure],[ErrorOrObservableFeatureExposure],[EnvironmentalExposure],[EntityToExposureEventAssociationMixin],[BioticExposure],[BehavioralExposure],[AdministrativeOperationalExposure])

---


## Mixin for

 * [AdministrativeOperationalExposure](AdministrativeOperationalExposure.md) (mixin)  - A administrative operational exposure is an intake of a particular administrative operation.
 * [BehavioralExposure](BehavioralExposure.md) (mixin)  - A behavioral exposure is a factor relating to behavior impacting an individual.
 * [BioticExposure](BioticExposure.md) (mixin)  - A biotic exposure is an intake of (sometimes faulty) computational systems (including viruses)
 * [EnvironmentalExposure](EnvironmentalExposure.md) (mixin)  - A environmental exposure is a factor relating to abiotic processes in the environment including atmospheric (heat, cold, general pollution) and water-born contaminants
 * [ErrorOrObservableFeatureExposure](ErrorOrObservableFeatureExposure.md) (mixin)  - A error or observable feature exposure is where a error state is manifested which represents an precondition, leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular error.
 * [FaultyDeploymentExposure](FaultyDeploymentExposure.md) (mixin)  - An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome,
 * [FaultyProcessExposure](FaultyProcessExposure.md) (mixin)  - A faulty process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
 * [GeographicExposure](GeographicExposure.md) (mixin)  - A geographic exposure is a factor relating to geographic proximity to some impactful entity.
 * [OrchestrationExposure](OrchestrationExposure.md) (mixin)  - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
 * [Repairing](Repairing.md) (mixin)  - A repairing is targeted at a error or observability and may involve multiple administrative operational 'exposures', engineering devices and/or procedures
 * [ServiceBackgroundExposure](ServiceBackgroundExposure.md) (mixin)  - A service background exposure is where an individual's specific service background of serviceunits, sequence variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or influencing an outcome.
 * [SocioeconomicExposure](SocioeconomicExposure.md) (mixin)  - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).

## Referenced by class

 *  **[EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md)** *[entity to exposure event association mixin➞object](entity_to_exposure_event_association_mixin_object.md)*  <sub>REQ</sub>  **[ExposureEvent](ExposureEvent.md)**
 *  **[ExposureEventToEntityAssociationMixin](ExposureEventToEntityAssociationMixin.md)** *[exposure event to entity association mixin➞subject](exposure_event_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[ExposureEvent](ExposureEvent.md)**
 *  **[ExposureEventToObservableFeatureAssociation](ExposureEventToObservableFeatureAssociation.md)** *[exposure event to observable feature association➞subject](exposure_event_to_observable_feature_association_subject.md)*  <sub>REQ</sub>  **[ExposureEvent](ExposureEvent.md)**

## Attributes


### Own

 * [timepoint](timepoint.md)  <sub>OPT</sub>
    * Description: a point in time
    * range: [TimeType](types/TimeType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | exposure |
|  | | experimental condition |
| **In Subsets:** | | system_model_database |
| **Exact Mappings:** | | REPR:ExperimentalCondition |
| **Narrow Mappings:** | | csrc:Threat_Event |
|  | | RO:0002244 |
|  | | sumo:exclusiveEvent |
| **Broad Mappings:** | | schema:event |

