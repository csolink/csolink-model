---
parent: Entities
title: csolink:Device
grand_parent: Classes
layout: default
---

# Class: Device


A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment

URI: [csolink:Device](https://w3id.org/csolink/vocab/Device)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[Repairing]-%20has%20device%200..%2A%3E[Device%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NamedThing]%5E-[Device],[Repairing],[Attribute],[Agent])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[has device](has_device.md)*  <sub>0..*</sub>  **[Device](Device.md)**

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
| **Exact Mappings:** | | csrc:Device |
|  | | NCIT:C62103 |
|  | | SAN:device |
|  | | schema:device |
|  | | SIO:000956 |
|  | | ssn:device |
|  | | sumo:Device |
|  | | WIKIDATA:Q1183543 |
| **Narrow Mappings:** | | CSO:access_routers |
|  | | csrc:boundary_protection_device |
|  | | csrc:Bring_Your_Own_Device |
|  | | csrc:common_fill_device |
|  | | csrc:Computing_Device |
|  | | csrc:Consumer_Device |
|  | | csrc:Cryptographic_device |
|  | | csrc:Data_Transfer_Device |
|  | | csrc:embedded_computer |
|  | | csrc:Personal_Computer |
|  | | csrc:Router |
|  | | CSO:mobile_device |
|  | | CSO:optoelectronic_device |
|  | | CSO:display_device |
|  | | CSO:mim_device |
|  | | CSO:microstrip_device |
|  | | CSO:acoustic_surface_wave_device |
|  | | CSO:acoustic_device |
|  | | CSO:logic_device |
|  | | CSO:haptic_device |
|  | | CSO:digital_device |
|  | | CSO:electromechanical_device |
|  | | CSO:hand_held_device |
|  | | CSO:timing_device |
|  | | CSO:magnetostrictive_device |
|  | | CSO:electrooptical_device |
|  | | CSO:wearable_device |
|  | | CSO:acquisition_device |
|  | | CSO:memsdevice |
|  | | CSO:assistive_device |
|  | | CSO:clamping_device |
|  | | CSO:fpga_device |
|  | | CSO:reconfigurable_device |
|  | | CSO:programmable_logic_device |
|  | | CSO:bluetooth_device |
|  | | CSO:mis_device |
|  | | CSO:electromagnetic_device |
|  | | CSO:energy_harvesting_device |
|  | | CSO:radio_frequency_identification_device |
|  | | CSO:device_architecture |
|  | | CSO:storage_device |
|  | | CSO:mram_device |
|  | | CSO:facts_device |
|  | | CSO:compute_unified_device_architecture |
|  | | CSO:device_driver |
|  | | CSO:embedded_device |
|  | | CSO:portable_device |
|  | | CSO:force_feedback_device |
|  | | CSO:electric_sensing_device |
|  | | CSO:mobile_handheld_device |
|  | | CSO:digital_micro-mirror_device |
|  | | CSO:cryptographic_device |
|  | | CSO:sensor_device |
|  | | NCIT:C16830 |
|  | | NCIT:C49831 |
|  | | NCIT:C49927 |
|  | | NCIT:C49918 |
|  | | sosa:Actuator |
|  | | sosa:Sensor |
|  | | sumo:CommunicationDevice |
|  | | sumo:DataStorageDevice |
|  | | sumo:FlashDrive |
|  | | sumo:HardwareSystem |
|  | | WIKIDATA:Q178648 |
|  | | WIKIDATA:Q2858615 |
|  | | WIKIDATA_PROPERTY:P6948 |
|  | | WIKIDATA_PROPERTY:P7501 |

