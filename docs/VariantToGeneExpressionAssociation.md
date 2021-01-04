---
parent: Associations
title: csolink:VariantToGeneExpressionAssociation
grand_parent: Classes
layout: default
---

# Class: VariantToGeneExpressionAssociation


An association between a variant and expression of a gene (i.e. e-QTL)

URI: [csolink:VariantToGeneExpressionAssociation](https://w3id.org/csolink/vocab/VariantToGeneExpressionAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToGeneExpressionAssociation%7Cpredicate:predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F]uses%20-.-%3E[GeneExpressionMixin],[VariantToGeneAssociation]%5E-[VariantToGeneExpressionAssociation],[VariantToGeneAssociation],[Publication],[OntologyClass],[NamedThing],[LifeStage],[GeneExpressionMixin],[Gene],[DiseaseOrPhenotypicFeature],[Attribute],[Association],[AnatomicalEntity],[Agent])

---


## Parents

 *  is_a: [VariantToGeneAssociation](VariantToGeneAssociation.md) - An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium)

## Uses Mixins

 *  mixin: [GeneExpressionMixin](GeneExpressionMixin.md) - Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs.

## Referenced by class


## Attributes


### Own

 * [variant to gene expression association➞predicate](variant_to_gene_expression_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of csolink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)

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

### Inherited from gene expression mixin:

 * [gene expression mixin➞quantifier qualifier](gene_expression_mixin_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: Optional quantitative value indicating degree of expression.
    * range: [OntologyClass](OntologyClass.md)
 * [expression site](expression_site.md)  <sub>OPT</sub>
    * Description: location in which gene or protein expression takes place. May be cell, tissue, or organ.
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * Example: UBERON:0002037 cerebellum
 * [phenotypic state](phenotypic_state.md)  <sub>OPT</sub>
    * Description: in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

### Inherited from gene to expression site association:

 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * Description: stage at which the gene is expressed in the site
    * range: [LifeStage](LifeStage.md)
    * Example:    
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: can be used to indicate magnitude, or also ranking
    * range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>REQ</sub>
    * Description: gene in which variation is correlated with the phenotypic feature
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>REQ</sub>
    * Description: location in which the gene is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * Example:    
 * [gene to expression site association➞predicate](gene_to_expression_site_association_predicate.md)  <sub>REQ</sub>
    * Description: expression relationship
    * range: [PredicateType](types/PredicateType.md)

### Inherited from variant to gene association:

 * [variant to gene association➞object](variant_to_gene_association_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [variant to gene association➞predicate](variant_to_gene_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)

### Domain for slot:

 * [variant to gene expression association➞predicate](variant_to_gene_expression_association_predicate.md)  <sub>REQ</sub>
    * range: [PredicateType](types/PredicateType.md)
