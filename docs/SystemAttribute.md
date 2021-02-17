---
parent: Other Classes
title: csolink:SystemAttribute
grand_parent: Classes
layout: default
---

# Class: SystemAttribute


describes a characteristic of an systemic entity.

URI: [csolink:SystemAttribute](https://w3id.org/csolink/vocab/SystemAttribute)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemAttribute%7Cname(i):label_type%20%3F;iri(i):iri_type%20%3F;source(i):label_type%20%3F]%5E-[ObservableQuality],[SystemAttribute]%5E-[Inheritance],[Attribute]%5E-[SystemAttribute],[QuantityValue],[OntologyClass],[ObservableQuality],[NamedThing],[Inheritance],[Attribute])

---


## Parents

 *  is_a: [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, resource.

## Children

 * [Inheritance](Inheritance.md) - The pattern or 'mode' in which a particular service trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc.
 * [ObservableQuality](ObservableQuality.md) - A property of a observable

## Referenced by class


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
| **Exact Mappings:** | | MAID:3019042566 |
|  | | ssn-system:SystemProperty |
| **Narrow Mappings:** | | csrc:Resource_Starvation |
|  | | geolink:isSchedulerOf |
|  | | MAID:2982962739 |
|  | | MAID:139330139 |
|  | | MAID:3283095 |
|  | | MAID:54956558 |
|  | | MAID:57022672 |
|  | | ssn-system:Accuracy |
|  | | ssn-system:ActuationRange |
|  | | ssn-system:BatteryLifetime |
|  | | ssn-system:Condition |
|  | | ssn-system:DetectionLimit |
|  | | ssn-system:Drift |
|  | | ssn-system:Frequency |
|  | | ssn-system:Latency |
|  | | ssn-system:MaintenanceSchedule |
|  | | ssn-system:MeasurementRange |
|  | | ssn-system:OperatingProperty |
|  | | ssn-system:OperatingPowerRange |
|  | | ssn-system:OperatingRange |
|  | | ssn-system:Precision |
|  | | ssn-system:Resolution |
|  | | ssn-system:ResponseTime |
|  | | ssn-system:Selectivity |
|  | | ssn-system:Sensitivity |
|  | | ssn-system:SurvivalRange |
|  | | ssn-system:SurvivalProperty |
|  | | ssn-system:SystemCapability |
|  | | ssn-system:SystemProperty |
|  | | ssn-system:SystemLifetime |
|  | | ssn-system:qualityOfObservation |
|  | | WIKIDATA:Q1554231 |

