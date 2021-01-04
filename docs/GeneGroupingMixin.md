---
parent: Class Mixins
title: csolink:GeneGroupingMixin
grand_parent: Classes
layout: default
---

# Class: GeneGroupingMixin


any grouping of multiple genes or gene products

URI: [csolink:GeneGroupingMixin](https://w3id.org/csolink/vocab/GeneGroupingMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Gene]%3Chas%20gene%20or%20gene%20product%200..%2A-%20[GeneGroupingMixin],[GenomicBackgroundExposure]uses%20-.-%3E[GeneGroupingMixin],[GeneFamily]uses%20-.-%3E[GeneGroupingMixin],[DrugToGeneInteractionExposure]uses%20-.-%3E[GeneGroupingMixin],[GenomicBackgroundExposure],[GeneFamily],[Gene],[DrugToGeneInteractionExposure])

---


## Mixin for

 * [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) (mixin)  - drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
 * [GeneFamily](GeneFamily.md) (mixin)  - any grouping of multiple genes or gene products related by common descent
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.

## Referenced by class


## Attributes


### Own

 * [has gene or gene product](has_gene_or_gene_product.md)  <sub>0..*</sub>
    * Description: connects an entity with one or more gene products
    * range: [Gene](Gene.md)
