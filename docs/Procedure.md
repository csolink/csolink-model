---
parent: Entities
title: csolink:Procedure
grand_parent: Classes
layout: default
---

# Class: Procedure


A series of actions conducted in a certain order or manner

URI: [csolink:Procedure](https://w3id.org/csolink/vocab/Procedure)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Repairing]-%20has%20procedure%200..%2A%3E[Procedure%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Procedure]uses%20-.-%3E[ActivityAndBehavior],[NamedThing]%5E-[Procedure],[Repairing],[NamedThing],[Attribute],[Agent],[ActivityAndBehavior])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral healthy, organization or mechanical actor in the world

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[has procedure](has_procedure.md)*  <sub>0..*</sub>  **[Procedure](Procedure.md)**

## Attributes


### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a csolink model class URI.
This field is multi-valued. It should include values for ancestors of the csolink class; for example, a serviceinstance such as Shh would have category values `bl:Interface`, `bl:ComponentTypeProduct`, `bl:ComponentTypeEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific csolink class, or potentially to a class more specific than something in csolink.
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (service, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | NCIT:C79751 |
|  | | SIO:000999 |
|  | | schema:procedure |
|  | | sosa:Procedure |
|  | | sumo:Procedure |
|  | | WIKIDATA:Q41689629 |
|  | | WIKIDATA:Q28520605 |
| **Narrow Mappings:** | | csrc:assessment_procedure |
|  | | csrc:Key_derivation procedure |
|  | | csrc:overwrite_procedure |
|  | | csrc:recovery_procedures |
|  | | csrc:Standard_operating_procedures |
|  | | csrc:Tactic_Technique_Procedure |
|  | | csrc:Tactics_Techniques_and_Procedures |
|  | | CSO:decision_procedure |
|  | | CSO:computer_operating_procedures |
|  | | CSO:greedy_randomized_adaptive_search_procedure |
|  | | EFO:0002571 |
|  | | IAO:0000591 |
|  | | MAID:81303663 |
|  | | MMO:0000575 |
|  | | NCIT:C19233 |
|  | | NCIT:C25218 |
|  | | REPR:ComputationalStep |
|  | | REPR:Non-computationalStep |
|  | | SWO:0000148 |
|  | | SWO:0000252 |
|  | | sumo:EncodingProcedure |
|  | | WIKIDATA:Q190686 |

