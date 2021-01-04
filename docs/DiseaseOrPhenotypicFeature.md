---
parent: Entities
title: csolink:DiseaseOrPhenotypicFeature
grand_parent: Classes
layout: default
---

# Class: DiseaseOrPhenotypicFeature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [csolink:DiseaseOrPhenotypicFeature](https://w3id.org/csolink/vocab/DiseaseOrPhenotypicFeature)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Treatment],[ThingWithTaxon],[PhenotypicFeature],[OrganismTaxon],[NamedThing],[MolecularEntity],[Gene],[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[Drug],[DiseaseOrPhenotypicFeatureToEntityAssociationMixin],[DiseaseOrPhenotypicFeatureOutcome],[DiseaseOrPhenotypicFeatureExposure],[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject%201..1%3E[DiseaseOrPhenotypicFeature%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1%3E[DiseaseOrPhenotypicFeature],[DiseaseOrPhenotypicFeatureToEntityAssociationMixin]-%20subject%201..1%3E[DiseaseOrPhenotypicFeature],[EntityToDiseaseOrPhenotypicFeatureAssociationMixin]-%20object%201..1%3E[DiseaseOrPhenotypicFeature],[GeneExpressionMixin]-%20phenotypic%20state%200..1%3E[DiseaseOrPhenotypicFeature],[DiseaseOrPhenotypicFeature]uses%20-.-%3E[ThingWithTaxon],[DiseaseOrPhenotypicFeature]%5E-[PhenotypicFeature],[DiseaseOrPhenotypicFeature]%5E-[DiseaseOrPhenotypicFeatureOutcome],[DiseaseOrPhenotypicFeature]%5E-[DiseaseOrPhenotypicFeatureExposure],[DiseaseOrPhenotypicFeature]%5E-[Disease],[BiologicalEntity]%5E-[DiseaseOrPhenotypicFeature],[GeneExpressionMixin],[Disease],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[CellLineToDiseaseOrPhenotypicFeatureAssociation],[BiologicalEntity],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

## Children

 * [Disease](Disease.md)
 * [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) - A disease or phenotypic feature exposure is where a disease state is manifested which represents an precondition, leading to or influencing an outcome, e.g. hypertension leading to a related disease outcome such as cardiovascular disease.
 * [DiseaseOrPhenotypicFeatureOutcome](DiseaseOrPhenotypicFeatureOutcome.md) - Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other characteristic phenotype.
 * [PhenotypicFeature](PhenotypicFeature.md)

## Referenced by class

 *  **[BiologicalEntity](BiologicalEntity.md)** *[ameliorates](ameliorates.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[biomarker for](biomarker_for.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Drug](Drug.md)** *[causes adverse event](causes_adverse_event.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)** *[cell line to disease or phenotypic feature association➞subject](cell_line_to_disease_or_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)** *[chemical to disease or phenotypic feature association➞object](chemical_to_disease_or_phenotypic_feature_association_object.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Drug](Drug.md)** *[contraindicated for](contraindicated_for.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)** *[disease or phenotypic feature to entity association mixin➞subject](disease_or_phenotypic_feature_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)** *[entity to disease or phenotypic feature association mixin➞object](entity_to_disease_or_phenotypic_feature_association_mixin_object.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[BiologicalEntity](BiologicalEntity.md)** *[exacerbates](exacerbates.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Gene](Gene.md)** *[gene associated with condition](gene_associated_with_condition.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Association](Association.md)** *[phenotypic state](phenotypic_state.md)*  <sub>OPT</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Treatment](Treatment.md)** *[treats](treats.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**

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
| **Aliases:** | | phenome |
| **Narrow Mappings:** | | UMLSSC:T033 |
|  | | UMLSST:fndg |

