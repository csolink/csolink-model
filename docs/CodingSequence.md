---
parent: Entities
title: csolink:CodingSequence
grand_parent: Classes
layout: default
---

# Class: CodingSequence




URI: [csolink:CodingSequence](https://w3id.org/csolink/vocab/CodingSequence)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[SystemTaxon],[NamedThing],[WorkloadEntity]%5E-[CodingSequence%7Chas_computational_sequence(i):computational_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Attribute],[Agent])

---


## Parents

 *  is_a: [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

## Referenced by class


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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (translator_minimal)

### Inherited from workload entity:

 * [has computational sequence](has_computational_sequence.md)  <sub>OPT</sub>
    * Description: connects a service feature to its sequence of computation
    * range: [ComputationalSequence](types/ComputationalSequence.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | MAID:11413529 |
|  | | schema:algorithm |
|  | | sumo:coding |
| **Close Mappings:** | | MAID:179518139 |
|  | | MAID:199360897 |
| **Narrow Mappings:** | | csrc:Packet_Binary_Convolutional_Coding |
|  | | CSO:image_coding |
|  | | CSO:signal_encoding |
|  | | CSO:iterative_decoding |
|  | | CSO:network_coding |
|  | | CSO:video_coding |
|  | | CSO:precoding |
|  | | CSO:channel_coding |
|  | | CSO:scalable_video_coding |
|  | | CSO:space_time_block_coding |
|  | | CSO:space-time_coding |
|  | | CSO:distributed_video_coding |
|  | | CSO:audio_coding |
|  | | CSO:wyner-ziv_coding |
|  | | CSO:adaptive_modulation_and_coding |
|  | | CSO:linear_pre-coding |
|  | | CSO:transcoding |
|  | | CSO:multiview_video_coding |
|  | | CSO:distributed_source_coding |
|  | | CSO:joint_source-channel_coding |
|  | | CSO:huffman_coding |
|  | | CSO:viterbi_decoding |
|  | | CSO:source_coding |
|  | | CSO:multiple_description_coding |
|  | | CSO:scalable_coding |
|  | | CSO:turbo_coding |
|  | | CSO:lossy_coding |
|  | | CSO:lossless_image_coding |
|  | | CSO:lossless_coding |
|  | | CSO:lossy_source_coding |
|  | | CSO:transform_coding |
|  | | CSO:advanced_video_coding |
|  | | CSO:high-efficiency_video_coding |
|  | | CSO:entropy_coding |
|  | | CSO:belief_propagation_decoding |
|  | | CSO:binary_coding |
|  | | CSO:random_linear_network_coding |
|  | | CSO:linear_network_coding |
|  | | CSO:arithmetic_coding |
|  | | CSO:source_channel_coding |
|  | | CSO:channel_coding_scheme |
|  | | CSO:orthogonal_space_time_block_coding |
|  | | CSO:physical-layer_network_coding |
|  | | CSO:convolutional_coding |
|  | | CSO:linear_predictive_coding |
|  | | CSO:source_and_channel_coding |
|  | | CSO:random_network_coding |
|  | | CSO:h.264_video_coding |
|  | | CSO:super-position_coding |
|  | | CSO:video_transcoding |
|  | | CSO:slepian-wolf_coding |
|  | | CSO:soft_decision_decoding |
|  | | CSO:coding_scheme |
|  | | CSO:decoding_complexity |
|  | | CSO:distributed_space-time_coding |
|  | | CSO:3d_video_coding |
|  | | CSO:analog_network_coding |
|  | | CSO:ldpc_coding |
|  | | CSO:distributed_coding |
|  | | CSO:erasure_coding |
|  | | CSO:channel_decoding |
|  | | CSO:concatenated_coding |
|  | | CSO:wireless_network_coding |
|  | | CSO:dirty_paper_coding |
| **Broad Mappings:** | | MAID:177212765 |

