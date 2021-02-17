---
parent: Class Mixins
title: csolink:ComponentserviceGroupingMixin
grand_parent: Classes
layout: default
---

# Class: ComponentserviceGroupingMixin


any grouping of multiple componentservices or servicetypes

URI: [csolink:ComponentserviceGroupingMixin](https://w3id.org/csolink/vocab/ComponentserviceGroupingMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Componentservice]%3Chas%20componentservice%20or%20servicetype%200..%2A-++[ComponentserviceGroupingMixin],[ComponentserviceFamily]uses%20-.-%3E[ComponentserviceGroupingMixin],[ComponentserviceBackgroundExposure]uses%20-.-%3E[ComponentserviceGroupingMixin],[AdministrativeOperationalToComponentserviceInteractionExposure]uses%20-.-%3E[ComponentserviceGroupingMixin],[ComponentserviceFamily],[ComponentserviceBackgroundExposure],[Componentservice],[AdministrativeOperationalToComponentserviceInteractionExposure])

---


## Mixin for

 * [AdministrativeOperationalToComponentserviceInteractionExposure](AdministrativeOperationalToComponentserviceInteractionExposure.md) (mixin)  - administrative operational to componentservice interaction exposure is a administrative operational exposure is where the interactions of the administrative operational with specific componentservices are known to constitute an 'exposure' to the system, leading to or influencing an outcome.
 * [ComponentserviceBackgroundExposure](ComponentserviceBackgroundExposure.md) (mixin)  - A service background exposure is where an individual's specific service background of serviceunits, sequence variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or influencing an outcome.
 * [ComponentserviceFamily](ComponentserviceFamily.md) (mixin)  - any grouping of multiple componentservices or servicetypes related by common descent

## Referenced by class


## Attributes


### Own

 * [has componentservice or servicetype](has_componentservice_or_servicetype.md)  <sub>0..*</sub>
    * Description: connects an entity with one or more componentservice or servicetypes
    * range: [Componentservice](Componentservice.md)
