---
parent: Entities
title: csolink:SystemicEntity
grand_parent: Classes
layout: default
---

# Class: SystemicEntity


A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities

URI: [csolink:SystemicEntity](https://w3id.org/csolink/vocab/SystemicEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemicEntityAsAModelOfErrorAssociation],[Attribute]%3Chas%20attribute%200..%2A-++[SystemicEntity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[SystemicEntityAsAModelOfErrorAssociation]-%20subject%201..1%3E[SystemicEntity],[SystemicEntity]%5E-[PopulationOfIndividualSystems],[SystemicEntity]%5E-[LifecycleStage],[SystemicEntity]%5E-[IndividualSystem],[SystemicEntity]%5E-[DeploymentEntity],[SystemicEntity]%5E-[ComponentType],[ComputationalEntity]%5E-[SystemicEntity],[PopulationOfIndividualSystems],[NamedThing],[LifecycleStage],[IndividualSystem],[ExposureEvent],[DeploymentEntity],[ComputationalEntity],[ComponentType],[Attribute],[Agent])

---


## Parents

 *  is_a: [ComputationalEntity](ComputationalEntity.md)

## Children

 * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
 * [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part
 * [IndividualSystem](IndividualSystem.md) - An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
 * [LifecycleStage](LifecycleStage.md) - A stage of development or growth of a system.
 * [PopulationOfIndividualSystems](PopulationOfIndividualSystems.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.

## Referenced by class

 *  **[ExposureEvent](ExposureEvent.md)** *[has gateway](has_gateway.md)*  <sub>OPT</sub>  **[SystemicEntity](SystemicEntity.md)**
 *  **[SystemicEntityAsAModelOfErrorAssociation](SystemicEntityAsAModelOfErrorAssociation.md)** *[systemic entity as a model of error association➞subject](systemic_entity_as_a_model_of_error_association_subject.md)*  <sub>REQ</sub>  **[SystemicEntity](SystemicEntity.md)**

## Attributes


### Own

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

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

 * [systemic entity➞has attribute](systemic_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may often be an system attribute
    * range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Narrow Mappings:** | | CSO:operating_system |
|  | | csrc:Operations_System |
|  | | sosa:Platform |
|  | | ssn:deployedSystem |
|  | | ssn:Deployment |
|  | | ssn:inDeployment |
|  | | sumo:OperatingSystem |
|  | | sumo:MonitoringProgram |
|  | | sumo:RegulatoryProcess |
| **Broad Mappings:** | | ssn:System |
| **Related Mappings:** | | WIKIDATA:Q17089065 |

