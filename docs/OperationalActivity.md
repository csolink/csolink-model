---
parent: Entities
title: csolink:OperationalActivity
grand_parent: Classes
layout: default
---

# Class: OperationalActivity


An execution of a operational function carried out by a servicetype or macrooperational complex.

URI: [csolink:OperationalActivity](https://w3id.org/csolink/vocab/OperationalActivity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MacrooperationalMachineMixin]%3Cenabled%20by%200..%2A-++[OperationalActivity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ControlActor]%3Chas%20output%200..%2A-%20[OperationalActivity],[ControlActor]%3Chas%20input%200..%2A-%20[OperationalActivity],[MacrooperationalMachineMixinToOperationalActivityAssociation]-%20object%201..1%3E[OperationalActivity],[OperationalActivity]uses%20-.-%3E[Occurrent],[ComputationalProcessOrActivity]%5E-[OperationalActivity],[Occurrent],[NamedThing],[MacrooperationalMachineMixinToOperationalActivityAssociation],[MacrooperationalMachineMixin],[ControlActor],[ComputationalProcessOrActivity],[Attribute],[Agent])

---


## Parents

 *  is_a: [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.

## Referenced by class

 *  **[MacrooperationalMachineMixinToOperationalActivityAssociation](MacrooperationalMachineMixinToOperationalActivityAssociation.md)** *[macrooperational machine mixin to operational activity association➞object](macrooperational_machine_mixin_to_operational_activity_association_object.md)*  <sub>REQ</sub>  **[OperationalActivity](OperationalActivity.md)**

## Attributes


### Own

 * [operational activity➞enabled by](operational_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The servicetype, componentservice, or complex that catalyzes the reaction
    * range: [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)
 * [operational activity➞has input](operational_activity_has_input.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the input for the reaction
    * range: [ControlActor](ControlActor.md)
 * [operational activity➞has output](operational_activity_has_output.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the output for the reaction
    * range: [ControlActor](ControlActor.md)

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

### Domain for slot:

 * [operational activity➞enabled by](operational_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The servicetype, componentservice, or complex that catalyzes the reaction
    * range: [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)
 * [operational activity➞has input](operational_activity_has_input.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the input for the reaction
    * range: [ControlActor](ControlActor.md)
 * [operational activity➞has output](operational_activity_has_output.md)  <sub>0..*</sub>
    * Description: A orchestration entity that is the output for the reaction
    * range: [ControlActor](ControlActor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | operation function |
|  | | operation event |
|  | | reaction |
| **Broad Mappings:** | | csrc:activity |
| **Related Mappings:** | | geolink:hasOperator |
|  | | sumo:LogicalOperator |

