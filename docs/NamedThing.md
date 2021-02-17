---
parent: Entities
title: csolink:NamedThing
grand_parent: Classes
layout: default
---

# Class: NamedThing


a databased entity or concept/class

URI: [csolink:NamedThing](https://w3id.org/csolink/vocab/NamedThing)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToErrorAssociation],[ServiceunittypeToErrorAssociation],[ResourceSampleDerivationAssociation],[Repairing],[Procedure],[PlanetaryEntity],[Phenomenon],[OntologyClass],[Occurrent],[NamedThing]%3Ccategory%201..%2A-%20[NamedThing%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ComputationalProcessOrActivity]-%20has%20input%200..%2A%3E[NamedThing],[ComputationalProcessOrActivity]-%20has%20output%200..%2A%3E[NamedThing],[Attribute]-%20has%20qualitative%20value%200..1%3E[NamedThing],[MacrooperationalMachineMixinToEntityAssociationMixin]-%20subject%201..1%3E[NamedThing],[ModelToErrorAssociationMixin]-%20subject%201..1%3E[NamedThing],[Association]-%20object%201..1%3E[NamedThing],[ResourceSampleDerivationAssociation]-%20object%201..1%3E[NamedThing],[ServiceunittypeToErrorAssociation]-%20object%201..1%3E[NamedThing],[ServiceunittypeToErrorAssociation]-%20subject%201..1%3E[NamedThing],[Association]-%20subject%201..1%3E[NamedThing],[VariantToErrorAssociation]-%20object%201..1%3E[NamedThing],[VariantToErrorAssociation]-%20subject%201..1%3E[NamedThing],[NamedThing]%5E-[Repairing],[NamedThing]%5E-[Procedure],[NamedThing]%5E-[PlanetaryEntity],[NamedThing]%5E-[Phenomenon],[NamedThing]%5E-[OntologyClass],[NamedThing]%5E-[InformationContentEntity],[NamedThing]%5E-[EmpiricalEntity],[NamedThing]%5E-[Device],[NamedThing]%5E-[CyberEntity],[NamedThing]%5E-[ComputationalEntity],[NamedThing]%5E-[AdministrativeEntity],[NamedThing]%5E-[Activity],[Entity]%5E-[NamedThing],[ModelToErrorAssociationMixin],[MacrooperationalMachineMixinToEntityAssociationMixin],[InformationContentEntity],[Entity],[EmpiricalEntity],[Device],[CyberEntity],[ComputationalProcessOrActivity],[ComputationalEntity],[Attribute],[Association],[Agent],[AdministrativeEntity],[Activity])

---


## Parents

 *  is_a: [Entity](Entity.md) - Root Csolink Model class for all things and informational relationships, real or imagined.

## Children

 * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
 * [AdministrativeEntity](AdministrativeEntity.md)
 * [ComputationalEntity](ComputationalEntity.md)
 * [CyberEntity](CyberEntity.md) - An entity that has digital reality (a.k.a. cyber essence).
 * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
 * [EmpiricalEntity](EmpiricalEntity.md) - Any entity or process that exists in the empirical domain and outside the computational realm. Errors are placed under computational entities
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.
 * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
 * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
 * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner
 * [Repairing](Repairing.md) - A repairing is targeted at a error or observability and may involve multiple administrative operational 'exposures', engineering devices and/or procedures

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[affected by](affected_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[affects](affects.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[affects availability in](affects_availability_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[affects risk for](affects_risk_for.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[broad match](broad_match.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[caused by](caused_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[causes](causes.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[close match](close_match.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[coexists with](coexists_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[colocalizes with](colocalizes_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[componentservice association](componentservice_association.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[contributes to](contributes_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[correlated with](correlated_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[cyber interaction with](cyber_interaction_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[derives from](derives_from.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[derives into](derives_into.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[develops from](develops_from.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[directly interacts with](directly_interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[disrupted by](disrupted_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[disrupts](disrupts.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[error has basis in](error_has_basis_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[exact match](exact_match.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[filler](filler.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has completed](has_completed.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has decreased amount](has_decreased_amount.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has increased amount](has_increased_amount.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has input](has_input.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has not completed](has_not_completed.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has output](has_output.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has part](has_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has participant](has_participant.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Attribute](Attribute.md)** *[has qualitative value](has_qualitative_value.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has variant part](has_variant_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[homologous to](homologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[in linkage disequilibrium with](in_linkage_disequilibrium_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[interacts with](interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[lacks part](lacks_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[located in](located_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[location of](location_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[MacrooperationalMachineMixinToEntityAssociationMixin](MacrooperationalMachineMixinToEntityAssociationMixin.md)** *[macrooperational machine mixin to entity association mixin➞subject](macrooperational_machine_mixin_to_entity_association_mixin_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[model of](model_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[ModelToErrorAssociationMixin](ModelToErrorAssociationMixin.md)** *[model to error association mixin➞subject](model_to_error_association_mixin_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[named thing➞category](named_thing_category.md)*  <sub>1..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[narrow match](narrow_match.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[negatively correlated with](negatively_correlated_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[object](object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[occurs in](occurs_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[orchestrationly similar to](orchestrationly_similar_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[orthologous to](orthologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[overlaps](overlaps.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[paralogous to](paralogous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[part of](part_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[positively correlated with](positively_correlated_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[predisposes](predisposes.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[prevented by](prevented_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[prevents](prevents.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produced by](produced_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produces](produces.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[related condition](related_condition.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[related to](related_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[ResourceSampleDerivationAssociation](ResourceSampleDerivationAssociation.md)** *[resource sample derivation association➞object](resource_sample_derivation_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[same as](same_as.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[ServiceunittypeToErrorAssociation](ServiceunittypeToErrorAssociation.md)** *[serviceunittype to error association➞object](serviceunittype_to_error_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[ServiceunittypeToErrorAssociation](ServiceunittypeToErrorAssociation.md)** *[serviceunittype to error association➞subject](serviceunittype_to_error_association_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[similar to](similar_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[subject](subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[VariantToErrorAssociation](VariantToErrorAssociation.md)** *[variant to error association➞object](variant_to_error_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[VariantToErrorAssociation](VariantToErrorAssociation.md)** *[variant to error association➞subject](variant_to_error_association_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[xenologous to](xenologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

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

### Domain for slot:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | BFO:0000001 |
|  | | WIKIDATA:Q35120 |

