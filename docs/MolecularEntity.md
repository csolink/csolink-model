---
parent: Entities
title: csolink:MolecularEntity
grand_parent: Classes
layout: default
---

# Class: MolecularEntity


A gene, gene product, small molecule or macromolecule (including protein complex)"

URI: [csolink:MolecularEntity](https://w3id.org/csolink/vocab/MolecularEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[PhysicalEssence],[PairwiseMolecularInteraction],[OrganismTaxon],[NamedThing],[MolecularEntityToEntityAssociationMixin],[GeneToGoTermAssociation]-%20subject%201..1%3E[MolecularEntity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[MolecularEntityToEntityAssociationMixin]-%20subject%201..1%3E[MolecularEntity],[PairwiseMolecularInteraction]-%20object%201..1%3E[MolecularEntity],[PairwiseMolecularInteraction]-%20subject%201..1%3E[MolecularEntity],[MolecularEntity]uses%20-.-%3E[ThingWithTaxon],[MolecularEntity]uses%20-.-%3E[PhysicalEssence],[MolecularEntity]%5E-[GenomicEntity],[MolecularEntity]%5E-[GeneFamily],[MolecularEntity]%5E-[Food],[MolecularEntity]%5E-[Drug],[MolecularEntity]%5E-[ChemicalSubstance],[BiologicalEntity]%5E-[MolecularEntity],[GenomicEntity],[GeneToGoTermAssociation],[GeneFamily],[Food],[Drug],[DiseaseOrPhenotypicFeature],[ChemicalSubstance],[BiologicalEntity],[Attribute],[Agent])

---


## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
 *  mixin: [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.

## Children

 * [ChemicalSubstance](ChemicalSubstance.md) - May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part
 * [Drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
 * [Food](Food.md) - A substance consumed by a living organism as a source of nutrition
 * [GeneFamily](GeneFamily.md) - any grouping of multiple genes or gene products related by common descent
 * [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[MolecularEntity](MolecularEntity.md)** *[affects abundance of](affects_abundance_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects activity of](affects_activity_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects degradation of](affects_degradation_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects folding of](affects_folding_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects localization of](affects_localization_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects metabolic processing of](affects_metabolic_processing_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects molecular modification of](affects_molecular_modification_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects response to](affects_response_to.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects secretion of](affects_secretion_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects stability of](affects_stability_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects synthesis of](affects_synthesis_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects transport of](affects_transport_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[affects uptake of](affects_uptake_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases abundance of](decreases_abundance_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases activity of](decreases_activity_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases degradation of](decreases_degradation_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases folding of](decreases_folding_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases localization of](decreases_localization_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases metabolic processing of](decreases_metabolic_processing_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases molecular interaction](decreases_molecular_interaction.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases molecular modification of](decreases_molecular_modification_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases response to](decreases_response_to.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases secretion of](decreases_secretion_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases stability of](decreases_stability_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases synthesis of](decreases_synthesis_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases transport of](decreases_transport_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases uptake of](decreases_uptake_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[GeneToGoTermAssociation](GeneToGoTermAssociation.md)** *[gene to go term association➞subject](gene_to_go_term_association_subject.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[has biomarker](has_biomarker.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases abundance of](increases_abundance_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases activity of](increases_activity_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases degradation of](increases_degradation_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases folding of](increases_folding_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases localization of](increases_localization_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases metabolic processing of](increases_metabolic_processing_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases molecular interaction](increases_molecular_interaction.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases molecular modification of](increases_molecular_modification_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases response to](increases_response_to.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases secretion of](increases_secretion_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases stability of](increases_stability_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases synthesis of](increases_synthesis_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases transport of](increases_transport_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases uptake of](increases_uptake_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntityToEntityAssociationMixin](MolecularEntityToEntityAssociationMixin.md)** *[molecular entity to entity association mixin➞subject](molecular_entity_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[molecularly interacts with](molecularly_interacts_with.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)** *[pairwise molecular interaction➞object](pairwise_molecular_interaction_object.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)** *[pairwise molecular interaction➞subject](pairwise_molecular_interaction_subject.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[positively regulates, entity to entity](positively_regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[regulates, entity to entity](regulates_entity_to_entity.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**

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
This field is multi-valued. It should include values for ancestors of the csolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific csolink class, or potentially to a class more specific than something in csolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in csolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for an attribute or entity.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | bioentity |
| **Narrow Mappings:** | | SIO:010341 |
|  | | WIKIDATA:Q43460564 |
|  | | UMLSSG:CHEM |
|  | | UMLSSC:T085 |
|  | | UMLSST:mosq |
|  | | UMLSSC:T123 |
|  | | UMLSST:bacs |
|  | | UMLSSC:T125 |
|  | | UMLSST:horm |
|  | | UMLSSC:T126 |
|  | | UMLSST:enzy |
|  | | UMLSSC:T129 |
|  | | UMLSST:imft |
|  | | UMLSSC:T192 |
|  | | UMLSST:rcpt |

