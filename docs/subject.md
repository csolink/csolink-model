---
parent: Edge Properties
title: csolink:subject
grand_parent: Slots
layout: default
---

# Slot: subject


connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.

URI: [csolink:subject](https://w3id.org/csolink/vocab/subject)

## Domain and Range

[Association](Association.md) ->  <sub>REQ</sub> [NamedThing](NamedThing.md)

## Parents

 *  is_a: [association slot](association_slot.md)

## Children


## Used by

 * [Association](Association.md)
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md)
 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md)
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)
 * [DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md)
 * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md)
 * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md)
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md)
 * [DrugToGeneAssociation](DrugToGeneAssociation.md)
 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md)
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md)
 * [SequenceAssociation](SequenceAssociation.md)
 * [VariantToGeneAssociation](VariantToGeneAssociation.md)
 * [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Local names:** | | annotation subject (ga4gh) |
|  | | node with outgoing relationship (neo4j) |
| **Mappings:** | | rdf:subject |
| **Exact Mappings:** | | owl:annotatedSource |
|  | | OBAN:association_has_subject |

