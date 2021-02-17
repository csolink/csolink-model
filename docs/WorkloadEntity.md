---
parent: Entities
title: csolink:WorkloadEntity
grand_parent: Classes
layout: default
---

# Class: WorkloadEntity


An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

URI: [csolink:WorkloadEntity](https://w3id.org/csolink/vocab/WorkloadEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ComponentserviceSequenceLocalization]-%20object%201..1%3E[WorkloadEntity%7Chas_computational_sequence:computational_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ComponentserviceSequenceLocalization]-%20subject%201..1%3E[WorkloadEntity],[SequenceFeatureRelationship]-%20object%201..1%3E[WorkloadEntity],[SequenceFeatureRelationship]-%20subject%201..1%3E[WorkloadEntity],[WorkloadEntity]%5E-[Workload],[WorkloadEntity]%5E-[Variantcomponentservicetype],[WorkloadEntity]%5E-[Serviceunittype],[WorkloadEntity]%5E-[Serviceinstance],[WorkloadEntity]%5E-[SequenceVariant],[WorkloadEntity]%5E-[ReagentTargetedComponentservice],[WorkloadEntity]%5E-[Daemon],[WorkloadEntity]%5E-[Componentserviceinstance],[WorkloadEntity]%5E-[ComponentserviceBackgroundExposure],[WorkloadEntity]%5E-[CodingSequence],[OperationalEntity]%5E-[WorkloadEntity],[Workload],[Variantcomponentservicetype],[SystemTaxon],[Serviceunittype],[Serviceinstance],[SequenceVariant],[SequenceFeatureRelationship],[ReagentTargetedComponentservice],[OperationalEntity],[NamedThing],[Daemon],[Componentserviceinstance],[ComponentserviceSequenceLocalization],[ComponentserviceBackgroundExposure],[CodingSequence],[Attribute],[Agent])

---


## Parents

 *  is_a: [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"

## Children

 * [CodingSequence](CodingSequence.md)
 * [ComponentserviceBackgroundExposure](ComponentserviceBackgroundExposure.md) - A service background exposure is where an individual's specific service background of serviceunits, sequence variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or influencing an outcome.
 * [Componentserviceinstance](Componentserviceinstance.md) - The unit of service workload the component is capable of providing or protecting.
 * [Daemon](Daemon.md) - A region of the componentserviceinstance sequence within a componentservice.
 * [ReagentTargetedComponentservice](ReagentTargetedComponentservice.md) - A componentservice altered in its availability level in the context of some experiment as a result of being targeted by componentservice-knockdown reagent(s).
 * [SequenceVariant](SequenceVariant.md) - A variantcomponentservice that varies in its sequence from what is considered the reference variantcomponentservice at that locus.
 * [Serviceinstance](Serviceinstance.md) - A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message
 * [Serviceunittype](Serviceunittype.md) - An information content entity that describes a workload by specifying the total variation in service sequence and/or componentservice availability, relative to some established background
 * [Variantcomponentservicetype](Variantcomponentservicetype.md) - A set of zero or more variantcomponentservices on a single instance of a Sequence
 * [Workload](Workload.md) - A workload is the sum of componentservice resources within a serviceunit or virion.

## Referenced by class

 *  **[OperationalEntity](OperationalEntity.md)** *[affects availability of](affects_availability_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[affects updates rate of](affects_updates_rate_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[ComponentserviceSequenceLocalization](ComponentserviceSequenceLocalization.md)** *[componentservice sequence localization➞object](componentservice_sequence_localization_object.md)*  <sub>REQ</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[ComponentserviceSequenceLocalization](ComponentserviceSequenceLocalization.md)** *[componentservice sequence localization➞subject](componentservice_sequence_localization_subject.md)*  <sub>REQ</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases availability of](decreases_availability_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[decreases updates rate of](decreases_updates_rate_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[WorkloadEntity](WorkloadEntity.md)** *[has sequence location](has_sequence_location.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases availability of](increases_availability_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[OperationalEntity](OperationalEntity.md)** *[increases updates rate of](increases_updates_rate_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[is sequence variant of](is_sequence_variant_of.md)*  <sub>0..*</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[SequenceFeatureRelationship](SequenceFeatureRelationship.md)** *[sequence feature relationship➞object](sequence_feature_relationship_object.md)*  <sub>REQ</sub>  **[WorkloadEntity](WorkloadEntity.md)**
 *  **[SequenceFeatureRelationship](SequenceFeatureRelationship.md)** *[sequence feature relationship➞subject](sequence_feature_relationship_subject.md)*  <sub>REQ</sub>  **[WorkloadEntity](WorkloadEntity.md)**

## Attributes


### Own

 * [has computational sequence](has_computational_sequence.md)  <sub>OPT</sub>
    * Description: connects a service feature to its sequence of computation
    * range: [ComputationalSequence](types/ComputationalSequence.md)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sequence feature |
| **In Subsets:** | | system_model_database |
| **Exact Mappings:** | | MAID:2993258540 |
| **Narrow Mappings:** | | MAID:115235246 |

