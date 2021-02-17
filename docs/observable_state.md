---
parent: Edge Properties
title: csolink:observable_state
grand_parent: Slots
layout: default
---

# Slot: observable_state


in experiments (e.g. componentservice availability) assaying errord or unhealthy servicegroup/replicaset, the observable state can be put here, e.g. STATE ID. For healthy servicegroup/replicasets, use XXX.

URI: [csolink:observable_state](https://w3id.org/csolink/vocab/observable_state)

## Domain and Range

[Association](Association.md) ->  <sub>OPT</sub> [ErrorOrObservableFeature](ErrorOrObservableFeature.md)

## Parents

 *  is_a: [association slot](association_slot.md)

## Children


## Used by

 * [ComponentserviceAvailabilityMixin](ComponentserviceAvailabilityMixin.md)
 * [ComponentserviceToComponentserviceCoavailabilityAssociation](ComponentserviceToComponentserviceCoavailabilityAssociation.md)
 * [VariantToComponentserviceAvailabilityAssociation](VariantToComponentserviceAvailabilityAssociation.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | csrc:State |
|  | | ssn-system:Condition |
|  | | WIKIDATA:Q599031 |
| **Narrow Mappings:** | | csrc:Active_state |
|  | | csrc:Compromised_state |
|  | | csrc:Conflict |
|  | | csrc:Deactivated_state |
|  | | csrc:Defect |
|  | | csrc:Desired_State |
|  | | csrc:Destroyed_state |
|  | | csrc:Entropy |
|  | | csrc:fail_safe |
|  | | csrc:fail_secure |
|  | | csrc:fail_soft |
|  | | csrc:Fail_to_Known_State |
|  | | csrc:Internal_State |
|  | | csrc:Key_states |
|  | | csrc:Pre_activation_state |
|  | | csrc:secure_state |
|  | | csrc:Steady_State |
|  | | csrc:Suspended_state |
|  | | csrc:Working_State |
|  | | sumo:deviceState |
|  | | sumo:finishes |
|  | | sumo:stateOfProcess |
|  | | WIKIDATA:Q1121708 |
|  | | WIKIDATA:Q7632586 |
| **Related Mappings:** | | csrc:stage |

