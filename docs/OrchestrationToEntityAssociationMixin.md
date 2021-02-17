---
parent: Class Mixins
title: csolink:OrchestrationToEntityAssociationMixin
grand_parent: Classes
layout: default
---

# Class: OrchestrationToEntityAssociationMixin


An interaction between a orchestration entity and another entity

URI: [csolink:OrchestrationToEntityAssociationMixin](https://w3id.org/csolink/vocab/OrchestrationToEntityAssociationMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ControlActor]%3Csubject%201..1-%20[OrchestrationToEntityAssociationMixin],[OrchestrationToPathwayAssociation]uses%20-.-%3E[OrchestrationToEntityAssociationMixin],[OrchestrationToOrchestrationAssociation]uses%20-.-%3E[OrchestrationToEntityAssociationMixin],[OrchestrationToErrorOrObservableFeatureAssociation]uses%20-.-%3E[OrchestrationToEntityAssociationMixin],[OrchestrationToComponentserviceAssociation]uses%20-.-%3E[OrchestrationToEntityAssociationMixin],[OperationalEntityToEntityAssociationMixin]%5E-[OrchestrationToEntityAssociationMixin],[OrchestrationToPathwayAssociation],[OrchestrationToOrchestrationAssociation],[OrchestrationToErrorOrObservableFeatureAssociation],[OrchestrationToComponentserviceAssociation],[OperationalEntityToEntityAssociationMixin],[ControlActor])

---


## Parents

 *  is_a: [OperationalEntityToEntityAssociationMixin](OperationalEntityToEntityAssociationMixin.md) - An interaction between a operational entity and another entity

## Mixin for

 * [OrchestrationToComponentserviceAssociation](OrchestrationToComponentserviceAssociation.md) (mixin)  - An interaction between a orchestration entity and a componentservice or servicetype.
 * [OrchestrationToErrorOrObservableFeatureAssociation](OrchestrationToErrorOrObservableFeatureAssociation.md) (mixin)  - An interaction between a orchestration entity and a observability or error, where the presence of the orchestration gives rise to or exacerbates the observability.
 * [OrchestrationToOrchestrationAssociation](OrchestrationToOrchestrationAssociation.md) (mixin)  - A relationship between two orchestration entities. This can encompass actual interactions as well as temporal causal edges, e.g. one orchestration converted to another.
 * [OrchestrationToPathwayAssociation](OrchestrationToPathwayAssociation.md) (mixin)  - An interaction between a orchestration entity and a computational process or pathway.

## Referenced by class


## Attributes


### Own

 * [orchestration to entity association mixin➞subject](orchestration_to_entity_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: the control actor or entity that is an interactor
    * range: [ControlActor](ControlActor.md)

### Domain for slot:

 * [orchestration to entity association mixin➞subject](orchestration_to_entity_association_mixin_subject.md)  <sub>REQ</sub>
    * Description: the control actor or entity that is an interactor
    * range: [ControlActor](ControlActor.md)
