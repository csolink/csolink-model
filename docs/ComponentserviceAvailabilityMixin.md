---
parent: Other Classes
title: csolink:ComponentserviceAvailabilityMixin
grand_parent: Classes
layout: default
---

# Class: ComponentserviceAvailabilityMixin


Observed componentservice availability intensity, context (site, stage) and associated observable status within which the availability occurs.

URI: [csolink:ComponentserviceAvailabilityMixin](https://w3id.org/csolink/vocab/ComponentserviceAvailabilityMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[LifecycleStage],[ErrorOrObservableFeature],[DeploymentEntity],[ErrorOrObservableFeature]%3Cobservable%20state%200..1-%20[ComponentserviceAvailabilityMixin],[LifecycleStage]%3Cstage%20qualifier%200..1-%20[ComponentserviceAvailabilityMixin],[DeploymentEntity]%3Cavailability%20site%200..1-%20[ComponentserviceAvailabilityMixin],[OntologyClass]%3Cquantifier%20qualifier%200..1-%20[ComponentserviceAvailabilityMixin],[VariantToComponentserviceAvailabilityAssociation]uses%20-.-%3E[ComponentserviceAvailabilityMixin],[ComponentserviceToComponentserviceCoavailabilityAssociation]uses%20-.-%3E[ComponentserviceAvailabilityMixin],[VariantToComponentserviceAvailabilityAssociation],[ComponentserviceToComponentserviceCoavailabilityAssociation])

---


## Mixin for

 * [ComponentserviceToComponentserviceCoavailabilityAssociation](ComponentserviceToComponentserviceCoavailabilityAssociation.md) (mixin)  - Indicates that two componentservices are co-available, generally under the same conditions.
 * [VariantToComponentserviceAvailabilityAssociation](VariantToComponentserviceAvailabilityAssociation.md) (mixin)  - An association between a variant and availability of a componentservice (i.e. e-QTL)

## Referenced by class


## Attributes


### Own

 * [availability site](availability_site.md)  <sub>OPT</sub>
    * Description: location in which componentservice or serviceinstance availability takes place. May be serviceunit, servicegroup/replicaset, or application.
    * range: [DeploymentEntity](DeploymentEntity.md)
    * Example: ssn:Deployment Deployment
 * [componentservice availability mixin➞quantifier qualifier](componentservice_availability_mixin_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: Optional quantitative value indicating degree of availability.
    * range: [OntologyClass](OntologyClass.md)
 * [observable state](observable_state.md)  <sub>OPT</sub>
    * Description: in experiments (e.g. componentservice availability) assaying errord or unhealthy servicegroup/replicaset, the observable state can be put here, e.g. STATE ID. For healthy servicegroup/replicasets, use XXX.
    * range: [ErrorOrObservableFeature](ErrorOrObservableFeature.md)

### Inherited from componentservice to availability site association:

 * [componentservice to availability site association➞stage qualifier](componentservice_to_availability_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * Description: stage at which the componentservice is available in the site
    * range: [LifecycleStage](LifecycleStage.md)
 * [componentservice to availability site association➞quantifier qualifier](componentservice_to_availability_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: can be used to indicate magnitude, or also ranking
    * range: [OntologyClass](OntologyClass.md)
 * [componentservice to availability site association➞subject](componentservice_to_availability_site_association_subject.md)  <sub>REQ</sub>
    * Description: componentservice in which variation is correlated with the observable feature
    * range: [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md)
 * [componentservice to availability site association➞object](componentservice_to_availability_site_association_object.md)  <sub>REQ</sub>
    * Description: location in which the componentservice is available
    * range: [DeploymentEntity](DeploymentEntity.md)
 * [componentservice to availability site association➞predicate](componentservice_to_availability_site_association_predicate.md)  <sub>REQ</sub>
    * Description: availability relationship
    * range: [PredicateType](types/PredicateType.md)

### Domain for slot:

 * [componentservice availability mixin➞quantifier qualifier](componentservice_availability_mixin_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: Optional quantitative value indicating degree of availability.
    * range: [OntologyClass](OntologyClass.md)
