---
parent: Other Classes
title: csolink:Attribute
grand_parent: Classes
layout: default
---

# Class: Attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, resource.

URI: [csolink:Attribute](https://w3id.org/csolink/vocab/Attribute)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemicEntity],[SystemAttribute],[SocioeconomicAttribute],[SeverityValue],[QuantityValue],[OntologyClass],[NamedThing],[Homogeneity],[FrequencyValue],[EmpiricalAttribute],[ComputationalArchitecturalStyle],[NamedThing]%3Chas%20qualitative%20value%200..1-%20[Attribute%7Cname:label_type%20%3F;iri:iri_type%20%3F;source:label_type%20%3F],[QuantityValue]%3Chas%20quantitative%20value%200..%2A-++[Attribute],[OntologyClass]%3Chas%20attribute%20type%201..1-%20[Attribute],[Entity]++-%20has%20attribute%200..%2A%3E[Attribute],[SystemicEntity]++-%20has%20attribute%200..%2A%3E[Attribute],[Attribute]%5E-[SystemAttribute],[Attribute]%5E-[SocioeconomicAttribute],[Attribute]%5E-[SeverityValue],[Attribute]%5E-[Homogeneity],[Attribute]%5E-[FrequencyValue],[Attribute]%5E-[EmpiricalAttribute],[Attribute]%5E-[ComputationalArchitecturalStyle],[Annotation]%5E-[Attribute],[Entity],[Annotation])

---


## Identifier prefixes

 * EDAM-DATA
 * EDAM-FORMAT
 * EDAM-OPERATION
 * EDAM-TOPIC

## Parents

 *  is_a: [Annotation](Annotation.md) - Csolink Model root class for entity annotations.

## Children

 * [ComputationalArchitecturalStyle](ComputationalArchitecturalStyle.md)
 * [EmpiricalAttribute](EmpiricalAttribute.md) - Attributes relating to a empirical manifestation
 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [Homogeneity](Homogeneity.md)
 * [SeverityValue](SeverityValue.md) - describes the severity of a observable feature or error
 * [SocioeconomicAttribute](SocioeconomicAttribute.md) - Attributes relating to a socioeconomic manifestation
 * [SystemAttribute](SystemAttribute.md) - describes a characteristic of an systemic entity.

## Referenced by class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**
 *  **[SystemicEntity](SystemicEntity.md)** *[systemic entity➞has attribute](systemic_entity_has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
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

### Domain for slot:

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | samples |
| **Exact Mappings:** | | csrc:attribute |
|  | | SIO:000614 |
|  | | sumo:Attribute |
|  | | sumo:attribute |
|  | | WIKIDATA:Q758243 |
| **Close Mappings:** | | SAN:property |
|  | | schema:property |
|  | | ssn:Property |
| **Narrow Mappings:** | | CSO:quantitative_attributes |
|  | | csrc:Application_virtualization |
|  | | csrc:Capability |
|  | | csrc:Capability_Anomalous_Event_Detection_Management |
|  | | csrc:Capability_Anomalous_Event_Response_and_Recovery_Management |
|  | | csrc:Capability_Behavior_Management |
|  | | csrc:Capability_Boundary_Management |
|  | | csrc:Capability_Configuration_Settings_Management |
|  | | csrc:Capability_Credentials_and_Authentication_Management |
|  | | csrc:Capability_Event_Preparation_Management |
|  | | csrc:Capability_Hardware_Asset_Management |
|  | | csrc:Capability_ISCM |
|  | | csrc:Capability_Manage_and_Assess_Risk |
|  | | csrc:Capability_Perform_Resilient_Systems_Engineering |
|  | | csrc:Capability_Privilege_and_Account_Management |
|  | | csrc:Capability_Software_Asset_Management |
|  | | csrc:Capability_Trust_Management |
|  | | csrc:Capability_Vulnerability_Management |
|  | | CSO:release_date |
|  | | csrc:security_attribute |
|  | | dwc:identificationQualifier |
|  | | dwc:typeStatus |
|  | | dwc:usewithiri |
|  | | gr:UnitPriceSpecification |
|  | | PATO:0000001 |
|  | | SAN:impactedProperty |
|  | | sumo:TimeMeasure |
|  | | schema:releaseDate |
|  | | schema:Softwareapplication |
|  | | sosa:actsOnProperty |
|  | | sosa:ActuatableProperty |
|  | | sosa:DateTime |
|  | | sosa:FeatureOfInterest |
|  | | sosa:implementedBy |
|  | | sosa:ObservableProperty |
|  | | sosa:observedProperty |
|  | | ssn:Stimulus |
|  | | ssn:detects |
|  | | ssn:MeasurementProperty |
|  | | ssn:OperatingProperty |
|  | | ssn:SurvivalProperty |
|  | | sumo:criticalityLevel |
|  | | sumo:duration |
|  | | sumo:deviceAccount |
|  | | sumo:deviceOS |
|  | | sumo:DeviceClosed |
|  | | sumo:deviceState |
|  | | sumo:DeviceDamaged |
|  | | sumo:DeviceOff |
|  | | sumo:DeviceOn |
|  | | sumo:DeviceOff |
|  | | sumo:DeviceOpen |
|  | | sumo:DeviceStateAttribute |
|  | | sumo:FormOfAdaptationAttribute |
|  | | sumo:greaterThan |
|  | | sumo:greaterThanOrEqualTo |
|  | | sumo:lessThan |
|  | | sumo:lessThanOrEqualTo |
|  | | sumo:load |
|  | | sumo:most |
|  | | sumo:magneticVariation |
|  | | sumo:onboard |
|  | | sumo:providesDestination |
|  | | sumo:publishes |
|  | | sumo:validityPeriod |
|  | | sumo:VirtualAddress |

