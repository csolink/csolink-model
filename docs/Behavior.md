---
parent: Entities
title: csolink:Behavior
grand_parent: Classes
layout: default
---

# Class: Behavior




URI: [csolink:Behavior](https://w3id.org/csolink/vocab/Behavior)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SocioeconomicOutcome],[SocioeconomicExposure],[NamedThing],[CyberEntity],[ComputationalProcess],[BehavioralOutcome],[BehavioralExposure],[BehaviorToBehavioralFeatureAssociation],[BehaviorToBehavioralFeatureAssociation]-%20subject%201..1%3E[Behavior%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Behavior]%5E-[SocioeconomicOutcome],[Behavior]%5E-[SocioeconomicExposure],[Behavior]%5E-[BehavioralOutcome],[Behavior]%5E-[BehavioralExposure],[ComputationalProcess]%5E-[Behavior],[Attribute],[Agent])

---


## Parents

 *  is_a: [ComputationalProcess](ComputationalProcess.md) - One or more causally connected executions of operational functions

## Children

 * [BehavioralExposure](BehavioralExposure.md) - A behavioral exposure is a factor relating to behavior impacting an individual.
 * [BehavioralOutcome](BehavioralOutcome.md) - An outcome resulting from an exposure event which is the manifestation of individual behavior.
 * [SocioeconomicExposure](SocioeconomicExposure.md) - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
 * [SocioeconomicOutcome](SocioeconomicOutcome.md) - An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event

## Referenced by class

 *  **[BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md)** *[behavior to behavioral feature association➞subject](behavior_to_behavioral_feature_association_subject.md)*  <sub>REQ</sub>  **[Behavior](Behavior.md)**

## Attributes


### Inherited from computational process or activity:

 * [enabled by](enabled_by.md)  <sub>0..*</sub>
    * Description: holds between a process and a cyber entity, where the cyber entity executes the process
    * range: [CyberEntity](CyberEntity.md)
    * in subsets: (translator_minimal)

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
| **Exact Mappings:** | | CSO:component_behavior |
|  | | dwc:behavior |
|  | | SIO:001195 |
|  | | sumo:systemBehavior |
|  | | WIKIDATA:Q9332 |
| **Narrow Mappings:** | | CSO:anomalous_behavior |
|  | | CSO:normal_behavior |
|  | | CSO:malicious_behavior |
|  | | CSO:robot_behavior |
|  | | CSO:chaotic_behavior |
|  | | csrc:Behavioral_Outcome |
|  | | SAN:ActuatorInput |
|  | | SAN:ActuatorOutput |
| **Broad Mappings:** | | MAID:5570062 |

