---
parent: Associations
title: csolink:Association
grand_parent: Classes
layout: default
---

# Class: Association


A typed association between two entities, supported by evidence

URI: [csolink:Association](https://w3id.org/csolink/vocab/Association)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[VariantToObservableFeatureAssociation],[VariantToErrorAssociation],[VariantToComponentserviceAssociation],[SystemicEntityAsAModelOfErrorAssociation],[ServiceunittypeToVariantAssociation],[ServiceunittypeToServiceunittypePartAssociation],[ServiceunittypeToObservableFeatureAssociation],[ServiceunittypeToErrorAssociation],[ServiceunittypeToComponentserviceAssociation],[SequenceVariantModulatesRepairingAssociation],[SequenceFeatureRelationship],[SequenceAssociation],[ResourceSampleToErrorOrObservableFeatureAssociation],[ResourceSampleDerivationAssociation],[Publication],[PopulationToPopulationAssociation],[OrchestrationToPathwayAssociation],[OrchestrationToOrchestrationAssociation],[OrchestrationToErrorOrObservableFeatureAssociation],[OrchestrationToComponentserviceAssociation],[OntologyClass],[NamedThing],[FunctionalAssociation],[ExposureEventToOutcomeAssociation],[ExposureEventToObservableFeatureAssociation],[ErrorToObservableFeatureAssociation],[ErrorToExposureEventAssociation],[ErrorOrObservableFeatureToLocationAssociation],[ErrorOrObservableFeatureAssociationToLocationAssociation],[Entity],[DeploymentEntityToDeploymentEntityAssociation],[ContributorAssociation],[ComponentserviceToObservableFeatureAssociation],[ComponentserviceToErrorAssociation],[ComponentserviceToComponentserviceAssociation],[ComponentserviceToAvailabilitySiteAssociation],[ComponentserviceRegulatoryRelationship],[ComponentTypeToErrorOrObservableFeatureAssociation],[CaseToObservableFeatureAssociation],[BehaviorToBehavioralFeatureAssociation],[Attribute],[Association]%3Ccategory%201..%2A-%20[Association%7Cpredicate:predicate_type;relation:uriorcurie;negated:boolean%20%3F;type:string%20%3F;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Publication]%3Cpublications%200..%2A-%20[Association],[OntologyClass]%3Cqualifiers%200..%2A-%20[Association],[NamedThing]%3Cobject%201..1-%20[Association],[NamedThing]%3Csubject%201..1-%20[Association],[Association]%5E-[VariantToPopulationAssociation],[Association]%5E-[VariantToObservableFeatureAssociation],[Association]%5E-[VariantToErrorAssociation],[Association]%5E-[VariantToComponentserviceAssociation],[Association]%5E-[SystemicEntityAsAModelOfErrorAssociation],[Association]%5E-[ServiceunittypeToVariantAssociation],[Association]%5E-[ServiceunittypeToServiceunittypePartAssociation],[Association]%5E-[ServiceunittypeToObservableFeatureAssociation],[Association]%5E-[ServiceunittypeToErrorAssociation],[Association]%5E-[ServiceunittypeToComponentserviceAssociation],[Association]%5E-[SequenceVariantModulatesRepairingAssociation],[Association]%5E-[SequenceFeatureRelationship],[Association]%5E-[SequenceAssociation],[Association]%5E-[ResourceSampleToErrorOrObservableFeatureAssociation],[Association]%5E-[ResourceSampleDerivationAssociation],[Association]%5E-[PopulationToPopulationAssociation],[Association]%5E-[OrchestrationToPathwayAssociation],[Association]%5E-[OrchestrationToOrchestrationAssociation],[Association]%5E-[OrchestrationToErrorOrObservableFeatureAssociation],[Association]%5E-[OrchestrationToComponentserviceAssociation],[Association]%5E-[FunctionalAssociation],[Association]%5E-[ExposureEventToOutcomeAssociation],[Association]%5E-[ExposureEventToObservableFeatureAssociation],[Association]%5E-[ErrorToObservableFeatureAssociation],[Association]%5E-[ErrorToExposureEventAssociation],[Association]%5E-[ErrorOrObservableFeatureToLocationAssociation],[Association]%5E-[ErrorOrObservableFeatureAssociationToLocationAssociation],[Association]%5E-[DeploymentEntityToDeploymentEntityAssociation],[Association]%5E-[ContributorAssociation],[Association]%5E-[ComponentserviceToObservableFeatureAssociation],[Association]%5E-[ComponentserviceToErrorAssociation],[Association]%5E-[ComponentserviceToComponentserviceAssociation],[Association]%5E-[ComponentserviceToAvailabilitySiteAssociation],[Association]%5E-[ComponentserviceRegulatoryRelationship],[Association]%5E-[ComponentTypeToErrorOrObservableFeatureAssociation],[Association]%5E-[CaseToObservableFeatureAssociation],[Association]%5E-[BehaviorToBehavioralFeatureAssociation],[Association]%5E-[AdministrativeOperationalToComponentserviceAssociation],[Entity]%5E-[Association],[Agent],[AdministrativeOperationalToComponentserviceAssociation])

---


## Parents

 *  is_a: [Entity](Entity.md) - Root Csolink Model class for all things and informational relationships, real or imagined.

## Children

 * [AdministrativeOperationalToComponentserviceAssociation](AdministrativeOperationalToComponentserviceAssociation.md) - An interaction between a administrative operational and a componentservice or servicetype.
 * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) - An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
 * [CaseToObservableFeatureAssociation](CaseToObservableFeatureAssociation.md) - An association between a case (e.g. individual patient) and a observable feature in which the individual has or has had the observability.
 * [ComponentTypeToErrorOrObservableFeatureAssociation](ComponentTypeToErrorOrObservableFeatureAssociation.md) - An relationship between a component type and a error or a observability, where the component type is derived from an individual with that error or observability.
 * [ComponentserviceRegulatoryRelationship](ComponentserviceRegulatoryRelationship.md) - A regulatory relationship between two componentservices
 * [ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md) - An association between a componentservice and an availability site, possibly qualified by stage/timing info.
 * [ComponentserviceToComponentserviceAssociation](ComponentserviceToComponentserviceAssociation.md) - abstract parent class for different kinds of componentservice-serviceunit or servicetype to servicetype relationships. Includes homology and interaction.
 * [ComponentserviceToErrorAssociation](ComponentserviceToErrorAssociation.md)
 * [ComponentserviceToObservableFeatureAssociation](ComponentserviceToObservableFeatureAssociation.md)
 * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
 * [DeploymentEntityToDeploymentEntityAssociation](DeploymentEntityToDeploymentEntityAssociation.md)
 * [ErrorOrObservableFeatureAssociationToLocationAssociation](ErrorOrObservableFeatureAssociationToLocationAssociation.md)
 * [ErrorOrObservableFeatureToLocationAssociation](ErrorOrObservableFeatureToLocationAssociation.md) - An association between either a error or a observable feature and an deployment entity, where the error/feature manifests in that site.
 * [ErrorToExposureEventAssociation](ErrorToExposureEventAssociation.md) - An association between an exposure event and a error.
 * [ErrorToObservableFeatureAssociation](ErrorToObservableFeatureAssociation.md) - An association between a error and a observable feature in which the observable feature is associated with the error in some way.
 * [ExposureEventToObservableFeatureAssociation](ExposureEventToObservableFeatureAssociation.md) - Any association between an environment and a observable feature, where being in the environment influences the observability.
 * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) - An association between an exposure event and an outcome.
 * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes) and either a operational activity, a computational process or a component location in which a function is executed.
 * [OrchestrationToComponentserviceAssociation](OrchestrationToComponentserviceAssociation.md) - An interaction between a orchestration entity and a componentservice or servicetype.
 * [OrchestrationToErrorOrObservableFeatureAssociation](OrchestrationToErrorOrObservableFeatureAssociation.md) - An interaction between a orchestration entity and a observability or error, where the presence of the orchestration gives rise to or exacerbates the observability.
 * [OrchestrationToOrchestrationAssociation](OrchestrationToOrchestrationAssociation.md) - A relationship between two orchestration entities. This can encompass actual interactions as well as temporal causal edges, e.g. one orchestration converted to another.
 * [OrchestrationToPathwayAssociation](OrchestrationToPathwayAssociation.md) - An interaction between a orchestration entity and a computational process or pathway.
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
 * [ResourceSampleDerivationAssociation](ResourceSampleDerivationAssociation.md) - An association between a resource sample and the resource entity from which it is derived.
 * [ResourceSampleToErrorOrObservableFeatureAssociation](ResourceSampleToErrorOrObservableFeatureAssociation.md) - An association between a resource sample and a error or observability.
 * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a workload entity it is localized to.
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular daemon is part of a particular componentserviceinstance or componentservice
 * [SequenceVariantModulatesRepairingAssociation](SequenceVariantModulatesRepairingAssociation.md) - An association between a sequence variant and a repairing or health intervention. The repairing object itself encompasses both the error and the administrative operational used.
 * [ServiceunittypeToComponentserviceAssociation](ServiceunittypeToComponentserviceAssociation.md) - Any association between a serviceunittype and a componentservice. The serviceunittype have have multiple variants in that componentservice or a single one. There is no assumption of cardinality
 * [ServiceunittypeToErrorAssociation](ServiceunittypeToErrorAssociation.md)
 * [ServiceunittypeToObservableFeatureAssociation](ServiceunittypeToObservableFeatureAssociation.md) - Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the observability, either in isolation or through environment
 * [ServiceunittypeToServiceunittypePartAssociation](ServiceunittypeToServiceunittypePartAssociation.md) - Any association between one serviceunittype and a microservice entity that is a subset of it
 * [ServiceunittypeToVariantAssociation](ServiceunittypeToVariantAssociation.md) - Any association between a serviceunittype and a sequence variant.
 * [SystemicEntityAsAModelOfErrorAssociation](SystemicEntityAsAModelOfErrorAssociation.md)
 * [VariantToComponentserviceAssociation](VariantToComponentserviceAssociation.md) - An association between a variant and a componentservice, where the variant has a service association with the componentservice (i.e. is in linkage disequilibrium)
 * [VariantToErrorAssociation](VariantToErrorAssociation.md)
 * [VariantToObservableFeatureAssociation](VariantToObservableFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class

 *  **[Association](Association.md)** *[association➞category](association_category.md)*  <sub>1..*</sub>  **[Association](Association.md)**

## Attributes


### Own

 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of csolink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
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

 * [association➞category](association_category.md)  <sub>1..*</sub>
    * range: [Association](Association.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of csolink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (service, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | This is roughly the model used by csolink and ontobio at the moment |
| **Exact Mappings:** | | csrc:Association |
|  | | rdf:Statement |
|  | | owl:Axiom |
| **Narrow Mappings:** | | CSO:data_association |
|  | | MAID:117220453 |
|  | | MAID:79714647 |
|  | | WIKIDATA:Q382571 |
| **Broad Mappings:** | | WIKIDATA:Q186290 |

