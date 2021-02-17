---
parent: Entities
title: csolink:OntologyClass
grand_parent: Classes
layout: default
---

# Class: OntologyClass


a concept or class in an ontology, vocabulary or thesaurus

URI: [csolink:OntologyClass](https://w3id.org/csolink/vocab/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TaxonomicRank],[SystemTaxon],[RelationshipType],[ComponentserviceAvailabilityMixin]-%20quantifier%20qualifier%200..1%3E[OntologyClass%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ComponentserviceToAvailabilitySiteAssociation]-%20quantifier%20qualifier%200..1%3E[OntologyClass],[ContributorAssociation]-%20qualifiers%200..%2A%3E[OntologyClass],[EmpiricalMeasurement]-%20has%20attribute%20type%201..1%3E[OntologyClass],[Attribute]-%20has%20attribute%20type%201..1%3E[OntologyClass],[PairwiseOperationallyInteraction]-%20interacting%20tasks%20category%200..1%3E[OntologyClass],[Association]-%20qualifiers%200..%2A%3E[OntologyClass],[ComponentserviceAvailabilityMixin]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[ComponentserviceToAvailabilitySiteAssociation]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[OntologyClass]%5E-[TaxonomicRank],[OntologyClass]%5E-[SystemTaxon],[OntologyClass]%5E-[RelationshipType],[OntologyClass]%5E-[ComponentserviceOntologyClass],[NamedThing]%5E-[OntologyClass],[PairwiseOperationallyInteraction],[NamedThing],[EmpiricalMeasurement],[ContributorAssociation],[ComponentserviceToAvailabilitySiteAssociation],[ComponentserviceOntologyClass],[ComponentserviceAvailabilityMixin],[AttributeType],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ComponentserviceOntologyClass](ComponentserviceOntologyClass.md) - an ontology class that describes a controlling aspect of a componentservice, servicetype or complex
 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
 * [SystemTaxon](SystemTaxon.md) - A classification of a set of systems. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
 * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

## Referenced by class

 *  **[Association](Association.md)** *[association type](association_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ComponentserviceAvailabilityMixin](ComponentserviceAvailabilityMixin.md)** *[componentservice availability mixin➞quantifier qualifier](componentservice_availability_mixin_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md)** *[componentservice to availability site association➞quantifier qualifier](componentservice_to_availability_site_association_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[contributor association➞qualifiers](contributor_association_qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[EmpiricalMeasurement](EmpiricalMeasurement.md)** *[empirical measurement➞has attribute type](empirical_measurement_has_attribute_type.md)*  <sub>REQ</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[AttributeType](AttributeType.md)** *[has attribute type](has_attribute_type.md)*  <sub>REQ</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has operational consequence](has_operational_consequence.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has topic](has_topic.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[interacting tasks category](interacting_tasks_category.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[superclass of](superclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**

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
