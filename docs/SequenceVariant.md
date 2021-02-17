---
parent: Entities
title: csolink:SequenceVariant
grand_parent: Classes
layout: default
---

# Class: SequenceVariant


A variantcomponentservice that varies in its sequence from what is considered the reference variantcomponentservice at that locus.

URI: [csolink:SequenceVariant](https://w3id.org/csolink/vocab/SequenceVariant)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkloadEntity],[VariantToPopulationAssociation],[VariantToObservableFeatureAssociation],[VariantToEntityAssociationMixin],[VariantAsAModelOfErrorAssociation],[SystemTaxon],[ServiceunittypeToVariantAssociation],[SequenceVariantModulatesRepairingAssociation],[Componentservice]%3Chas%20componentservice%200..%2A-++[SequenceVariant%7Chas_computational_sequence:computational_sequence%20%3F;id:string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[SequenceVariantModulatesRepairingAssociation]-%20subject%201..1%3E[SequenceVariant],[ComponentserviceHasVariantThatContributesToErrorAssociation]-%20sequence%20variant%20qualifier%200..1%3E[SequenceVariant],[ServiceunittypeToVariantAssociation]-%20object%201..1%3E[SequenceVariant],[VariantAsAModelOfErrorAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToEntityAssociationMixin]-%20subject%201..1%3E[SequenceVariant],[VariantToObservableFeatureAssociation]-%20subject%201..1%3E[SequenceVariant],[VariantToPopulationAssociation]-%20subject%201..1%3E[SequenceVariant],[SequenceVariant]%5E-[MonomericVariant],[WorkloadEntity]%5E-[SequenceVariant],[NamedThing],[MonomericVariant],[ComponentserviceHasVariantThatContributesToErrorAssociation],[Componentservice],[Attribute],[Association],[Agent])

---


## Identifier prefixes

 * WIKIDATA

## Parents

 *  is_a: [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)

## Children

 * [MonomericVariant](MonomericVariant.md) - A single monomeric position in the service monomeric variants are single monomeric positions in service DNA at which different sequence alternatives exist

## Referenced by class

 *  **[SequenceVariantModulatesRepairingAssociation](SequenceVariantModulatesRepairingAssociation.md)** *[sequence variant modulates repairing association➞subject](sequence_variant_modulates_repairing_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Association](Association.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)*  <sub>OPT</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[ServiceunittypeToVariantAssociation](ServiceunittypeToVariantAssociation.md)** *[serviceunittype to variant association➞object](serviceunittype_to_variant_association_object.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantAsAModelOfErrorAssociation](VariantAsAModelOfErrorAssociation.md)** *[variant as a model of error association➞subject](variant_as_a_model_of_error_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)** *[variant to entity association mixin➞subject](variant_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToObservableFeatureAssociation](VariantToObservableFeatureAssociation.md)** *[variant to observable feature association➞subject](variant_to_observable_feature_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association➞subject](variant_to_population_association_subject.md)*  <sub>REQ</sub>  **[SequenceVariant](SequenceVariant.md)**

## Attributes


### Own

 * [sequence variant➞has componentservice](sequence_variant_has_componentservice.md)  <sub>0..*</sub>
    * Description: Each variantcomponentservice can be associated with any number of serviceunits
    * range: [Componentservice](Componentservice.md)
 * [sequence variant➞has computational sequence](sequence_variant_has_computational_sequence.md)  <sub>OPT</sub>
    * Description: The state of the sequence w.r.t a reference sequence
    * range: [ComputationalSequence](types/ComputationalSequence.md)
 * [sequence variant➞id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
    * Example:    
    * Example:    

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

### Domain for slot:

 * [sequence variant➞has componentservice](sequence_variant_has_componentservice.md)  <sub>0..*</sub>
    * Description: Each variantcomponentservice can be associated with any number of serviceunits
    * range: [Componentservice](Componentservice.md)
 * [sequence variant➞has computational sequence](sequence_variant_has_computational_sequence.md)  <sub>OPT</sub>
    * Description: The state of the sequence w.r.t a reference sequence
    * range: [ComputationalSequence](types/ComputationalSequence.md)
 * [sequence variant➞id](sequence_variant_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
    * Example:    
    * Example:    

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | variantcomponentservice |
|  | | malware |
| **Local names:** | | variantcomponentservice (agr) |
| **Alt Descriptions:** | | An entity that describes a single affected, endogenous variantcomponentservice. These can be of any type that matches that definition (AGR) |
|  | | A contiguous change at a Location (VMC) |
| **Comments:** | | This class is for modeling the specific state at a locus. |
| **In Subsets:** | | system_model_database |
| **Exact Mappings:** | | WIKIDATA:Q15304597 |
|  | | SO:0001059 |
| **Broad Mappings:** | | SO:0001060 |

