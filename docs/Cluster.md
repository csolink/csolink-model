---
parent: Class Mixins
title: csolink:Cluster
grand_parent: Classes
layout: default
---

# Class: Cluster


The cyber combination of two or more operational entities in which the identities are retained and are mixed in the form of solutions,

URI: [csolink:Cluster](https://w3id.org/csolink/vocab/Cluster)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ControlActor],[ControlActor]%3Chas%20control%20actor%200..%2A-%20[Cluster],[Notification]uses%20-.-%3E[Cluster],[ConsumedResource]uses%20-.-%3E[Cluster],[ComplexOrchestrationExposure]uses%20-.-%3E[Cluster],[AdministrativeOperation]uses%20-.-%3E[Cluster],[Notification],[ConsumedResource],[ComplexOrchestrationExposure],[AdministrativeOperation])

---


## Mixin for

 * [AdministrativeOperation](AdministrativeOperation.md) (mixin)  - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
 * [ComplexOrchestrationExposure](ComplexOrchestrationExposure.md) (mixin)  - A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a administrative operation.
 * [ConsumedResource](ConsumedResource.md) (mixin)  - A control actor (often a cluster) consumed for information, engineering or technical use.
 * [Notification](Notification.md) (mixin)  - A event consumed by a healthy system as a source of information

## Referenced by class


## Attributes


### Own

 * [has control actor](has_control_actor.md)  <sub>0..*</sub>
    * Description: one or more control actors within a cluster
    * range: [ControlActor](ControlActor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | CSO:cluster_system |
|  | | csrc:Cluster |
|  | | NCIT:C43418 |
|  | | WIKIDATA:Q21157127 |
| **Narrow Mappings:** | | CSO:cluster_nodes |
|  | | CSO:computing_cluster |
|  | | CSO:heterogeneous_cluster |
|  | | CSO:hpc_cluster |
|  | | CSO:large_cluster |
|  | | WIKIDATA:Q206637 |
|  | | sosa:hosts |
| **Broad Mappings:** | | CSO:cluster_computing |

