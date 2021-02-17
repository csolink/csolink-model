---
parent: Entities
title: csolink:Serviceunittype
grand_parent: Classes
layout: default
---

# Class: Serviceunittype


An information content entity that describes a workload by specifying the total variation in service sequence and/or componentservice availability, relative to some established background

URI: [csolink:Serviceunittype](https://w3id.org/csolink/vocab/Serviceunittype)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[SystemTaxon],[ServiceunittypeToVariantAssociation],[ServiceunittypeToServiceunittypePartAssociation],[ServiceunittypeToObservableFeatureAssociation],[ServiceunittypeToEntityAssociationMixin],[ServiceunittypeToComponentserviceAssociation],[ServiceunittypeAsAModelOfErrorAssociation],[Homogeneity]%3Chas%20homogeneity%200..1-++[Serviceunittype%7Chas_computational_sequence(i):computational_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ServiceunittypeAsAModelOfErrorAssociation]-%20subject%201..1%3E[Serviceunittype],[ServiceunittypeToComponentserviceAssociation]-%20subject%201..1%3E[Serviceunittype],[ServiceunittypeToEntityAssociationMixin]-%20subject%201..1%3E[Serviceunittype],[ServiceunittypeToObservableFeatureAssociation]-%20subject%201..1%3E[Serviceunittype],[ServiceunittypeToServiceunittypePartAssociation]-%20object%201..1%3E[Serviceunittype],[ServiceunittypeToServiceunittypePartAssociation]-%20subject%201..1%3E[Serviceunittype],[ServiceunittypeToVariantAssociation]-%20subject%201..1%3E[Serviceunittype],[WorkloadEntity]%5E-[Serviceunittype],[NamedThing],[Homogeneity],[Attribute],[Agent])

---


## Parents

 *  is_a: [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

## Referenced by class

 *  **[ServiceunittypeAsAModelOfErrorAssociation](ServiceunittypeAsAModelOfErrorAssociation.md)** *[serviceunittype as a model of error association➞subject](serviceunittype_as_a_model_of_error_association_subject.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**
 *  **[ServiceunittypeToComponentserviceAssociation](ServiceunittypeToComponentserviceAssociation.md)** *[serviceunittype to componentservice association➞subject](serviceunittype_to_componentservice_association_subject.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**
 *  **[ServiceunittypeToEntityAssociationMixin](ServiceunittypeToEntityAssociationMixin.md)** *[serviceunittype to entity association mixin➞subject](serviceunittype_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**
 *  **[ServiceunittypeToObservableFeatureAssociation](ServiceunittypeToObservableFeatureAssociation.md)** *[serviceunittype to observable feature association➞subject](serviceunittype_to_observable_feature_association_subject.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**
 *  **[ServiceunittypeToServiceunittypePartAssociation](ServiceunittypeToServiceunittypePartAssociation.md)** *[serviceunittype to serviceunittype part association➞object](serviceunittype_to_serviceunittype_part_association_object.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**
 *  **[ServiceunittypeToServiceunittypePartAssociation](ServiceunittypeToServiceunittypePartAssociation.md)** *[serviceunittype to serviceunittype part association➞subject](serviceunittype_to_serviceunittype_part_association_subject.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**
 *  **[ServiceunittypeToVariantAssociation](ServiceunittypeToVariantAssociation.md)** *[serviceunittype to variant association➞subject](serviceunittype_to_variant_association_subject.md)*  <sub>REQ</sub>  **[Serviceunittype](Serviceunittype.md)**

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
| **In Subsets:** | | system_model_database |
| **Broad Mappings:** | | sumo:controlGroup |

