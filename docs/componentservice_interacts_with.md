---
parent: Predicates
title: csolink:componentservice_interacts_with
grand_parent: Slots
layout: default
---

# Relation: componentservice_interacts_with

translator_minimal
{: .translator_minimal-subset-label }


holds between two componentservices whose observable effects are dependent on each other in some way - such that their combined observable effects are the result of some interaction between the activity of their servicetypes. Example is service-unit death when two componentservices simultaneously fail, or platform startup facilitating tenant services.

URI: [csolink:componentservice_interacts_with](https://w3id.org/csolink/vocab/componentservice_interacts_with)

## Domain and Range

[Componentservice](Componentservice.md) ->  <sub>0..*</sub> [Componentservice](Componentservice.md)

## Parents

 *  is_a: [interacts with](interacts_with.md)

## Children


## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Related Mappings:** | | CSO:functional_dependency |
|  | | sumo:Dependent-TaskRelation |

