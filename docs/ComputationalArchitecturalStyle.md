---
parent: Other Classes
title: csolink:ComputationalArchitecturalStyle
grand_parent: Classes
layout: default
---

# Class: ComputationalArchitecturalStyle




URI: [csolink:ComputationalArchitecturalStyle](https://w3id.org/csolink/vocab/ComputationalArchitecturalStyle)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[OntologyClass],[ObservableArchitecturalStyle],[NamedThing],[MicroserviceArchitecturalStyle],[EntityToObservableFeatureAssociationMixin]++-%20architectural%20style%20qualifier%200..1%3E[ComputationalArchitecturalStyle%7Cname(i):label_type%20%3F;iri(i):iri_type%20%3F;source(i):label_type%20%3F],[ComputationalArchitecturalStyle]%5E-[ObservableArchitecturalStyle],[ComputationalArchitecturalStyle]%5E-[MicroserviceArchitecturalStyle],[Attribute]%5E-[ComputationalArchitecturalStyle],[EntityToObservableFeatureAssociationMixin],[Attribute],[Association])

---


## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, resource.

## Children

 * [MicroserviceArchitecturalStyle](MicroserviceArchitecturalStyle.md) - An attribute corresponding to the microservice architectural style of the individual, based upon microservice composition of architectural style containers.
 * [ObservableArchitecturalStyle](ObservableArchitecturalStyle.md) - An attribute corresponding to the observable architectural style of the individual, based upon the reproductive applications present.

## Referenced by class

 *  **[Association](Association.md)** *[architectural style qualifier](architectural_style_qualifier.md)*  <sub>OPT</sub>  **[ComputationalArchitecturalStyle](ComputationalArchitecturalStyle.md)**

## Attributes


### Inherited from attribute:

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Narrow Mappings:** | | CSO:multiagent_architecture |
|  | | csrc:centric_architecture |
|  | | csrc:Common_Object_Request_Broker_Architecture |
|  | | csrc:enterprise_architecture |
|  | | csrc:Enterprise_Information_Security_Architecture |
|  | | csrc:federal_enterprise_architecture |
|  | | csrc:IA_architecture |
|  | | csrc:information_security_architecture |
|  | | csrc:Information_Sharing_Architecture |
|  | | csrc:IT_Security_Architecture |
|  | | csrc:Net_centric_Architecture |
|  | | csrc:Next_Generation_Access_Control_Functional_Architecture |
|  | | csrc:Open_Grid_Services_Architecture |
|  | | csrc:Open_Network_Architecture |
|  | | csrc:privacy_architecture |
|  | | csrc:security_architecture |
|  | | csrc:Semantic_Web_Services_Architecture |
| **Broad Mappings:** | | csrc:architecture |
|  | | csrc:Architecture_Design_Principles |
|  | | sumo:architecture |

