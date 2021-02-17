---
parent: Other Slots
title: csolink:category
grand_parent: Slots
layout: default
---

# Slot: category

translator_minimal
{: .translator_minimal-subset-label }


Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a csolink model class URI.
This field is multi-valued. It should include values for ancestors of the csolink class; for example, a serviceinstance such as Shh would have category values `bl:Interface`, `bl:ComponentTypeProduct`, `bl:ComponentTypeEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific csolink class, or potentially to a class more specific than something in csolink.

URI: [csolink:category](https://w3id.org/csolink/vocab/category)

## Domain and Range

[Entity](Entity.md) ->  <sub>1..*</sub> [CategoryType](types/CategoryType.md)

## Parents

 *  is_a: [type](type.md)

## Children


## Used by

 * [Entity](Entity.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Exact Mappings:** | | gr:category |
|  | | OCRM:category |
|  | | OSO:Category |
|  | | schema:category |
| **Narrow Mappings:** | | CSO:access_category |
|  | | OCRM:CaseCategory |
|  | | OSO:ComponentCategory |
|  | | schema:CategoryCode |

