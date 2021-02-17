---
title: Browse Csolink Model
has_children: true
nav_order: 2
layout: default
has_toc: false
---

Entity and association taxonomy and datamodel for computer services data


## Classes


### Entities


### Associations


### Class Mixins

 * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
 * [AdministrativeOperationalToEntityAssociationMixin](AdministrativeOperationalToEntityAssociationMixin.md) - An interaction between a administrative operational and another entity
 * [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) - An abstract association for use where the case is the subject
 * [Cluster](Cluster.md) - The cyber combination of two or more operational entities in which the identities are retained and are mixed in the form of solutions,
 * [ComponentTypeToEntityAssociationMixin](ComponentTypeToEntityAssociationMixin.md) - An relationship between a component type and another entity
 * [ComponentserviceGroupingMixin](ComponentserviceGroupingMixin.md) - any grouping of multiple componentservices or servicetypes
 * [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md) - a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another
    * [Componentservice](Componentservice.md) - A component service.
    * [ServicetypeMixin](ServicetypeMixin.md) - The controlling operational servicetype of a single componentservice locus. ServiceType product are either serviceinstances or supervisor tasks
       * [ServicetypeIsoformMixin](ServicetypeIsoformMixin.md) - This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the servicetype is intended to represent a specific isoform rather than a canonical or reference or generic servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
 * [ComponentserviceToEntityAssociationMixin](ComponentserviceToEntityAssociationMixin.md)
 * [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
 * [CyberEssenceOrOccurrent](CyberEssenceOrOccurrent.md) - Either a cyber or processual entity.
    * [CyberEssence](CyberEssence.md) - Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
    * [Occurrent](Occurrent.md) - A processual entity.
       * [ActivityAndBehavior](ActivityAndBehavior.md) - Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
 * [DatasetSummary](DatasetSummary.md)
 * [DistributionLevel](DistributionLevel.md)
 * [EntityToErrorAssociationMixin](EntityToErrorAssociationMixin.md) - mixin class for any association whose object (target node) is a error
 * [EntityToErrorOrObservableFeatureAssociationMixin](EntityToErrorOrObservableFeatureAssociationMixin.md)
 * [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) - An association between some entity and an exposure event.
 * [EntityToFeatureOrErrorQualifiersMixin](EntityToFeatureOrErrorQualifiersMixin.md) - Qualifiers for entity to error or observability associations.
    * [EntityToErrorAssociationMixin](EntityToErrorAssociationMixin.md) - mixin class for any association whose object (target node) is a error
    * [EntityToObservableFeatureAssociationMixin](EntityToObservableFeatureAssociationMixin.md)
 * [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) - An association between some entity and an outcome
 * [ErrorOrObservableFeatureToEntityAssociationMixin](ErrorOrObservableFeatureToEntityAssociationMixin.md)
 * [ErrorToEntityAssociationMixin](ErrorToEntityAssociationMixin.md)
 * [ExposureEvent](ExposureEvent.md) - A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more observability of that system, potentially mediated by serviceunits
 * [ExposureEventToEntityAssociationMixin](ExposureEventToEntityAssociationMixin.md) - An association between some exposure event and some entity.
 * [FaultyEntityMixin](FaultyEntityMixin.md) - A faulty (abnormal) structure or process.
 * [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations
    * [EntityToFeatureOrErrorQualifiersMixin](EntityToFeatureOrErrorQualifiersMixin.md) - Qualifiers for entity to error or observability associations.
       * [EntityToErrorAssociationMixin](EntityToErrorAssociationMixin.md) - mixin class for any association whose object (target node) is a error
       * [EntityToObservableFeatureAssociationMixin](EntityToObservableFeatureAssociationMixin.md)
 * [FrequencyQuantifier](FrequencyQuantifier.md)
 * [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md) - A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a component. They either carry out individual computational activities, or they encode tasks which do this.
    * [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md) - a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another
       * [Componentservice](Componentservice.md) - A component service.
       * [ServicetypeMixin](ServicetypeMixin.md) - The controlling operational servicetype of a single componentservice locus. ServiceType product are either serviceinstances or supervisor tasks
          * [ServicetypeIsoformMixin](ServicetypeIsoformMixin.md) - This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the servicetype is intended to represent a specific isoform rather than a canonical or reference or generic servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    * [MacrooperationalComplexMixin](MacrooperationalComplexMixin.md)
 * [MacrooperationalMachineMixinToEntityAssociationMixin](MacrooperationalMachineMixinToEntityAssociationMixin.md) - an association which has a macrooperational machine mixin mixin as a subject
 * [ModelToErrorAssociationMixin](ModelToErrorAssociationMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the error in a way that is useful for studying the error outside a patient carrying the error
 * [OperationalEntityToEntityAssociationMixin](OperationalEntityToEntityAssociationMixin.md) - An interaction between a operational entity and another entity
    * [AdministrativeOperationalToEntityAssociationMixin](AdministrativeOperationalToEntityAssociationMixin.md) - An interaction between a administrative operational and another entity
    * [OrchestrationToEntityAssociationMixin](OrchestrationToEntityAssociationMixin.md) - An interaction between a orchestration entity and another entity
 * [Outcome](Outcome.md) - An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible computational or non-computational (e.g. empirical) outcomes.
 * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a error, which is high when the presence of the feature implies the existence of the error
 * [RelationshipQuantifier](RelationshipQuantifier.md)
    * [FrequencyQuantifier](FrequencyQuantifier.md)
    * [SensitivityQuantifier](SensitivityQuantifier.md)
    * [SpecificityQuantifier](SpecificityQuantifier.md)
       * [PathognomonicityQuantifier](PathognomonicityQuantifier.md) - A relationship quantifier between a variant or symptom and a error, which is high when the presence of the feature implies the existence of the error
 * [ResourceSampleToEntityAssociationMixin](ResourceSampleToEntityAssociationMixin.md) - An association between a resource sample and something.
 * [ServiceunittypeToEntityAssociationMixin](ServiceunittypeToEntityAssociationMixin.md)
 * [SubjectOfInvestigation](SubjectOfInvestigation.md) - An entity that has the role of being studied in an investigation, study, or experiment
 * [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes
 * [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)

### Other Classes

 * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
 * [AdministrativeEntity](AdministrativeEntity.md)
    * [Agent](Agent.md) - service, group, organization or project that provides a piece of information (i.e. a knowledge association)
 * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
    * [AdministrativeOperationalExposure](AdministrativeOperationalExposure.md) - A administrative operational exposure is an intake of a particular administrative operation.
       * [AdministrativeOperationalToComponentserviceInteractionExposure](AdministrativeOperationalToComponentserviceInteractionExposure.md) - administrative operational to componentservice interaction exposure is a administrative operational exposure is where the interactions of the administrative operational with specific componentservices are known to constitute an 'exposure' to the system, leading to or influencing an outcome.
 * [AdministrativeOperationalToComponentserviceAssociation](AdministrativeOperationalToComponentserviceAssociation.md) - An interaction between a administrative operational and a componentservice or servicetype.
 * [Annotation](Annotation.md) - Csolink Model root class for entity annotations.
    * [Attribute](Attribute.md) - A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, resource.
       * [ComputationalArchitecturalStyle](ComputationalArchitecturalStyle.md)
          * [MicroserviceArchitecturalStyle](MicroserviceArchitecturalStyle.md) - An attribute corresponding to the microservice architectural style of the individual, based upon microservice composition of architectural style containers.
          * [ObservableArchitecturalStyle](ObservableArchitecturalStyle.md) - An attribute corresponding to the observable architectural style of the individual, based upon the reproductive applications present.
       * [EmpiricalAttribute](EmpiricalAttribute.md) - Attributes relating to a empirical manifestation
          * [EmpiricalCourse](EmpiricalCourse.md) - The course a error typically takes from its onset, progression in time, and eventual resolution or death of the affected individual
             * [Onset](Onset.md) - The age group in which (error) symptom manifestations appear
          * [EmpiricalMeasurement](EmpiricalMeasurement.md) - A empirical measurement is a special kind of attribute which results from a quality of serviceunit observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
          * [EmpiricalModifier](EmpiricalModifier.md) - Used to characterize and specify the observable abnormalities defined in the observable abnormality sub-ontology, with respect to severity, laterality, and other aspects
       * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
       * [Homogeneity](Homogeneity.md)
       * [SeverityValue](SeverityValue.md) - describes the severity of a observable feature or error
       * [SocioeconomicAttribute](SocioeconomicAttribute.md) - Attributes relating to a socioeconomic manifestation
       * [SystemAttribute](SystemAttribute.md) - describes a characteristic of an systemic entity.
          * [Inheritance](Inheritance.md) - The pattern or 'mode' in which a particular service trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc.
          * [ObservableQuality](ObservableQuality.md) - A property of a observable
    * [QuantityValue](QuantityValue.md) - A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric value
 * [Article](Article.md)
 * [Association](Association.md) - A typed association between two entities, supported by evidence
    * [AdministrativeOperationalToComponentserviceAssociation](AdministrativeOperationalToComponentserviceAssociation.md) - An interaction between a administrative operational and a componentservice or servicetype.
    * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) - An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
    * [CaseToObservableFeatureAssociation](CaseToObservableFeatureAssociation.md) - An association between a case (e.g. individual patient) and a observable feature in which the individual has or has had the observability.
    * [ComponentTypeToErrorOrObservableFeatureAssociation](ComponentTypeToErrorOrObservableFeatureAssociation.md) - An relationship between a component type and a error or a observability, where the component type is derived from an individual with that error or observability.
       * [ComponentTypeAsAModelOfErrorAssociation](ComponentTypeAsAModelOfErrorAssociation.md)
    * [ComponentserviceRegulatoryRelationship](ComponentserviceRegulatoryRelationship.md) - A regulatory relationship between two componentservices
    * [ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md) - An association between a componentservice and an availability site, possibly qualified by stage/timing info.
    * [ComponentserviceToComponentserviceAssociation](ComponentserviceToComponentserviceAssociation.md) - abstract parent class for different kinds of componentservice-serviceunit or servicetype to servicetype relationships. Includes homology and interaction.
       * [ComponentserviceToComponentserviceCoavailabilityAssociation](ComponentserviceToComponentserviceCoavailabilityAssociation.md) - Indicates that two componentservices are co-available, generally under the same conditions.
       * [ComponentserviceToComponentserviceHomologyAssociation](ComponentserviceToComponentserviceHomologyAssociation.md) - A homology association between two componentservices. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
       * [PairwiseComponentserviceToComponentserviceInteraction](PairwiseComponentserviceToComponentserviceInteraction.md) - An interaction between two componentservices or two servicetypes. May be cyber (e.g. serviceinstance binding) or service (between componentservices). May be symmetric (e.g. serviceinstance interaction) or directed (e.g. phosphorylation)
          * [PairwiseOperationallyInteraction](PairwiseOperationallyInteraction.md) - An interaction at the operational level between two cyber entities
    * [ComponentserviceToErrorAssociation](ComponentserviceToErrorAssociation.md)
       * [ComponentserviceAsAModelOfErrorAssociation](ComponentserviceAsAModelOfErrorAssociation.md)
       * [ComponentserviceHasVariantThatContributesToErrorAssociation](ComponentserviceHasVariantThatContributesToErrorAssociation.md)
    * [ComponentserviceToObservableFeatureAssociation](ComponentserviceToObservableFeatureAssociation.md)
    * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
    * [DeploymentEntityToDeploymentEntityAssociation](DeploymentEntityToDeploymentEntityAssociation.md)
       * [DeploymentEntityToDeploymentEntityOntogenicAssociation](DeploymentEntityToDeploymentEntityOntogenicAssociation.md) - A relationship between two deployment entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship.
       * [DeploymentEntityToDeploymentEntityPartOfAssociation](DeploymentEntityToDeploymentEntityPartOfAssociation.md) - A relationship between two deployment entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between components and componentservices, between componentservice and servicegroup/replicasets, servicegroup/replicasets and whole systems
    * [ErrorOrObservableFeatureAssociationToLocationAssociation](ErrorOrObservableFeatureAssociationToLocationAssociation.md)
    * [ErrorOrObservableFeatureToLocationAssociation](ErrorOrObservableFeatureToLocationAssociation.md) - An association between either a error or a observable feature and an deployment entity, where the error/feature manifests in that site.
    * [ErrorToExposureEventAssociation](ErrorToExposureEventAssociation.md) - An association between an exposure event and a error.
    * [ErrorToObservableFeatureAssociation](ErrorToObservableFeatureAssociation.md) - An association between a error and a observable feature in which the observable feature is associated with the error in some way.
    * [ExposureEventToObservableFeatureAssociation](ExposureEventToObservableFeatureAssociation.md) - Any association between an environment and a observable feature, where being in the environment influences the observability.
    * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) - An association between an exposure event and an outcome.
    * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes) and either a operational activity, a computational process or a component location in which a function is executed.
       * [ComponentserviceToGoTermAssociation](ComponentserviceToGoTermAssociation.md)
       * [MacrooperationalMachineMixinToComponentAssociation](MacrooperationalMachineMixinToComponentAssociation.md) - A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a component (as represented in the GO component branch), where the entity carries out its function in the component
       * [MacrooperationalMachineMixinToComputationalProcessAssociation](MacrooperationalMachineMixinToComputationalProcessAssociation.md) - A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a computational process or pathway (as represented in the GO computational process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
       * [MacrooperationalMachineMixinToOperationalActivityAssociation](MacrooperationalMachineMixinToOperationalActivityAssociation.md) - A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a operational activity (as represented in the GO operational function branch), where the entity carries out the activity, or contributes to its execution
    * [OrchestrationToComponentserviceAssociation](OrchestrationToComponentserviceAssociation.md) - An interaction between a orchestration entity and a componentservice or servicetype.
    * [OrchestrationToErrorOrObservableFeatureAssociation](OrchestrationToErrorOrObservableFeatureAssociation.md) - An interaction between a orchestration entity and a observability or error, where the presence of the orchestration gives rise to or exacerbates the observability.
    * [OrchestrationToOrchestrationAssociation](OrchestrationToOrchestrationAssociation.md) - A relationship between two orchestration entities. This can encompass actual interactions as well as temporal causal edges, e.g. one orchestration converted to another.
       * [OrchestrationToOrchestrationDerivationAssociation](OrchestrationToOrchestrationDerivationAssociation.md) - A causal relationship between two orchestration entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
    * [OrchestrationToPathwayAssociation](OrchestrationToPathwayAssociation.md) - An interaction between a orchestration entity and a computational process or pathway.
    * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
    * [ResourceSampleDerivationAssociation](ResourceSampleDerivationAssociation.md) - An association between a resource sample and the resource entity from which it is derived.
    * [ResourceSampleToErrorOrObservableFeatureAssociation](ResourceSampleToErrorOrObservableFeatureAssociation.md) - An association between a resource sample and a error or observability.
    * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a workload entity it is localized to.
       * [ComponentserviceSequenceLocalization](ComponentserviceSequenceLocalization.md) - A relationship between a sequence feature and a workload entity it is localized to. The reference entity may be a container, componentservice or information entity such as a namespace.
    * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular daemon is part of a particular componentserviceinstance or componentservice
       * [ComponentserviceToServicetypeRelationship](ComponentserviceToServicetypeRelationship.md) - A componentservice is transcribed and potentially translated to a servicetype
       * [ComponentserviceinstanceToComponentserviceRelationship](ComponentserviceinstanceToComponentserviceRelationship.md) - A componentservice is a collection of componentserviceinstances
       * [DaemonToComponentserviceinstanceRelationship](DaemonToComponentserviceinstanceRelationship.md) - A componentserviceinstance is formed from multiple daemons
    * [SequenceVariantModulatesRepairingAssociation](SequenceVariantModulatesRepairingAssociation.md) - An association between a sequence variant and a repairing or health intervention. The repairing object itself encompasses both the error and the administrative operational used.
    * [ServiceunittypeToComponentserviceAssociation](ServiceunittypeToComponentserviceAssociation.md) - Any association between a serviceunittype and a componentservice. The serviceunittype have have multiple variants in that componentservice or a single one. There is no assumption of cardinality
    * [ServiceunittypeToErrorAssociation](ServiceunittypeToErrorAssociation.md)
       * [ServiceunittypeAsAModelOfErrorAssociation](ServiceunittypeAsAModelOfErrorAssociation.md)
    * [ServiceunittypeToObservableFeatureAssociation](ServiceunittypeToObservableFeatureAssociation.md) - Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the observability, either in isolation or through environment
    * [ServiceunittypeToServiceunittypePartAssociation](ServiceunittypeToServiceunittypePartAssociation.md) - Any association between one serviceunittype and a microservice entity that is a subset of it
    * [ServiceunittypeToVariantAssociation](ServiceunittypeToVariantAssociation.md) - Any association between a serviceunittype and a sequence variant.
    * [SystemicEntityAsAModelOfErrorAssociation](SystemicEntityAsAModelOfErrorAssociation.md)
    * [VariantToComponentserviceAssociation](VariantToComponentserviceAssociation.md) - An association between a variant and a componentservice, where the variant has a componentservice association with the componentservice (i.e. is in linkage disequilibrium)
       * [VariantToComponentserviceAvailabilityAssociation](VariantToComponentserviceAvailabilityAssociation.md) - An association between a variant and availability of a componentservice (i.e. e-QTL)
    * [VariantToErrorAssociation](VariantToErrorAssociation.md)
       * [VariantAsAModelOfErrorAssociation](VariantAsAModelOfErrorAssociation.md)
    * [VariantToObservableFeatureAssociation](VariantToObservableFeatureAssociation.md)
    * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
 * [AttributeType](AttributeType.md) - A property or characteristic type of an entity. For example, an apple may have properties types such as color type, shape type, age type, crispiness type.
 * [Awareness](Awareness.md)
 * [Behavior](Behavior.md)
    * [BehavioralExposure](BehavioralExposure.md) - A behavioral exposure is a factor relating to behavior impacting an individual.
    * [BehavioralOutcome](BehavioralOutcome.md) - An outcome resulting from an exposure event which is the manifestation of individual behavior.
    * [SocioeconomicExposure](SocioeconomicExposure.md) - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
    * [SocioeconomicOutcome](SocioeconomicOutcome.md) - An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event
 * [BehavioralFeature](BehavioralFeature.md) - A observable feature which is behavioral in nature.
 * [BioticExposure](BioticExposure.md) - A biotic exposure is an intake of (sometimes faulty) computational systems (including viruses)
 * [Bitstream](Bitstream.md)
    * [MessagePassing](MessagePassing.md)
 * [Book](Book.md) - This class may rarely be available except if use cases of a given knowledge graph support its utility.
 * [BookChapter](BookChapter.md)
 * [Case](Case.md) - An individual system that has a patient role in some empirical context.
 * [CodingSequence](CodingSequence.md)
 * [Cohort](Cohort.md) - A group of individuals banded together or repaired as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
 * [ComplexOrchestrationExposure](ComplexOrchestrationExposure.md) - A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a administrative operation.
 * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
 * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
 * [ComponentserviceAvailabilityMixin](ComponentserviceAvailabilityMixin.md) - Observed componentservice availability intensity, context (site, stage) and associated observable status within which the availability occurs.
 * [ComponentserviceBackgroundExposure](ComponentserviceBackgroundExposure.md) - A service background exposure is where an individual's specific service background of serviceunits, sequence variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or influencing an outcome.
 * [ComponentserviceFamily](ComponentserviceFamily.md) - any grouping of multiple componentservices or servicetypes related by common descent
 * [ComponentserviceOntologyClass](ComponentserviceOntologyClass.md) - an ontology class that describes a controlling aspect of a componentservice, servicetype or complex
 * [Componentserviceinstance](Componentserviceinstance.md) - The unit of service workload the component is capable of providing or protecting.
    * [KernelServicetype](KernelServicetype.md)
       * [KernelServicetypeIsoform](KernelServicetypeIsoform.md) - Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
       * [NoncodingKernelServicetype](NoncodingKernelServicetype.md)
          * [KernelInterrupt](KernelInterrupt.md) - TBD
          * [KernelMessage](KernelMessage.md)
 * [ComputationalEntity](ComputationalEntity.md)
    * [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities
       * [ComputationalProcess](ComputationalProcess.md) - One or more causally connected executions of operational functions
          * [Behavior](Behavior.md)
             * [BehavioralExposure](BehavioralExposure.md) - A behavioral exposure is a factor relating to behavior impacting an individual.
             * [BehavioralOutcome](BehavioralOutcome.md) - An outcome resulting from an exposure event which is the manifestation of individual behavior.
             * [SocioeconomicExposure](SocioeconomicExposure.md) - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
             * [SocioeconomicOutcome](SocioeconomicOutcome.md) - An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event
          * [CyberProcess](CyberProcess.md)
          * [Death](Death.md)
             * [MortalityOutcome](MortalityOutcome.md) - An outcome of death from resulting from an exposure event.
          * [FaultyProcess](FaultyProcess.md) - A compulogic function or a process having an abnormal or deleterious effect at the subcomponent, component, multi-component, node, or system level.
             * [FaultyProcessExposure](FaultyProcessExposure.md) - A faulty process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
             * [FaultyProcessOutcome](FaultyProcessOutcome.md) - An outcome resulting from an exposure event which is the manifestation of a faulty process.
          * [Pathway](Pathway.md)
       * [OperationalActivity](OperationalActivity.md) - An execution of a operational function carried out by a servicetype or macrooperational complex.
    * [EpidemiologicalOutcome](EpidemiologicalOutcome.md) - An epidemiological outcome, such as societal error burden, resulting from an exposure event.
    * [ErrorOrObservableFeature](ErrorOrObservableFeature.md) - Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as distinct, others conflate.
       * [Error](Error.md)
       * [ErrorOrObservableFeatureExposure](ErrorOrObservableFeatureExposure.md) - A error or observable feature exposure is where a error state is manifested which represents an precondition, leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular error.
       * [ErrorOrObservableFeatureOutcome](ErrorOrObservableFeatureOutcome.md) - logical outcomes resulting from an exposure event which is the manifestation of a error or other characteristic observability.
       * [ObservableFeature](ObservableFeature.md)
          * [BehavioralFeature](BehavioralFeature.md) - A observable feature which is behavioral in nature.
          * [EmpiricalFinding](EmpiricalFinding.md) - this category is currently considered broad enough to tag empirical lab measurements and other computational attributes taken as 'empirical traits' with some statistical score, for example, a p value in componentservice associations.
    * [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
       * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
          * [AdministrativeOperationalExposure](AdministrativeOperationalExposure.md) - A administrative operational exposure is an intake of a particular administrative operation.
             * [AdministrativeOperationalToComponentserviceInteractionExposure](AdministrativeOperationalToComponentserviceInteractionExposure.md) - administrative operational to componentservice interaction exposure is a administrative operational exposure is where the interactions of the administrative operational with specific componentservices are known to constitute an 'exposure' to the system, leading to or influencing an outcome.
       * [ComponentserviceFamily](ComponentserviceFamily.md) - any grouping of multiple componentservices or servicetypes related by common descent
       * [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part
          * [ConsumedResource](ConsumedResource.md) - A control actor (often a cluster) consumed for information, engineering or technical use.
          * [Controller](Controller.md) - Any intermediate or servicetype resulting from director supervision. Includes primary and secondary controllers.
          * [NotificationComponent](NotificationComponent.md)
             * [Awareness](Awareness.md)
             * [Data](Data.md)
                * [Bitstream](Bitstream.md)
                   * [MessagePassing](MessagePassing.md)
                * [Datastream](Datastream.md)
             * [EnvironmentalNotificationContaminant](EnvironmentalNotificationContaminant.md)
          * [OrchestrationExposure](OrchestrationExposure.md) - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
             * [ComplexOrchestrationExposure](ComplexOrchestrationExposure.md) - A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a administrative operation.
          * [Power](Power.md)
       * [Notification](Notification.md) - A event consumed by a healthy system as a source of information
       * [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)
          * [CodingSequence](CodingSequence.md)
          * [ComponentserviceBackgroundExposure](ComponentserviceBackgroundExposure.md) - A service background exposure is where an individual's specific service background of serviceunits, sequence variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or influencing an outcome.
          * [Componentserviceinstance](Componentserviceinstance.md) - The unit of service workload the component is capable of providing or protecting.
             * [KernelServicetype](KernelServicetype.md)
                * [KernelServicetypeIsoform](KernelServicetypeIsoform.md) - Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
                * [NoncodingKernelServicetype](NoncodingKernelServicetype.md)
                   * [KernelInterrupt](KernelInterrupt.md) - TBD
                   * [KernelMessage](KernelMessage.md)
          * [Daemon](Daemon.md) - A region of the componentserviceinstance sequence within a componentservice.
          * [ReagentTargetedComponentservice](ReagentTargetedComponentservice.md) - A componentservice altered in its availability level in the context of some experiment as a result of being targeted by componentservice-knockdown reagent(s).
          * [SequenceVariant](SequenceVariant.md) - A variantcomponentservice that varies in its sequence from what is considered the reference variantcomponentservice at that locus.
             * [MonomericVariant](MonomericVariant.md) - A single monomeric position in the service monomeric variants are single monomeric positions in service DNA at which different sequence alternatives exist
          * [Serviceinstance](Serviceinstance.md) - A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message
             * [ServiceinstanceIsoform](ServiceinstanceIsoform.md) - Represents a serviceinstance that is a specific isoform of the canonical or reference serviceinstance.
          * [Serviceunittype](Serviceunittype.md) - An information content entity that describes a workload by specifying the total variation in service sequence and/or componentservice availability, relative to some established background
          * [Variantcomponentservicetype](Variantcomponentservicetype.md) - A set of zero or more variantcomponentservices on a single instance of a Sequence
          * [Workload](Workload.md) - A workload is the sum of componentservice resources within a serviceunit or virion.
    * [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities
       * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
       * [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part
          * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
          * [FaultyDeploymentStructure](FaultyDeploymentStructure.md) - An deployment structure with the potential of have an abnormal or deleterious effect at the process, serviceunit, multiserviceunit, or systemal level.
             * [FaultyDeploymentExposure](FaultyDeploymentExposure.md) - An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome,
             * [FaultyDeploymentOutcome](FaultyDeploymentOutcome.md) - An outcome resulting from an exposure event which is the manifestation of an abnormal deployment structure.
          * [GrossDeploymentStructure](GrossDeploymentStructure.md)
          * [Serviceunit](Serviceunit.md) - The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a cluster. It can be deployed, isolated, and repaired independently.
       * [IndividualSystem](IndividualSystem.md) - An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
          * [Case](Case.md) - An individual system that has a patient role in some empirical context.
       * [LifecycleStage](LifecycleStage.md) - A stage of development or growth of a system.
       * [PopulationOfIndividualSystems](PopulationOfIndividualSystems.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.
          * [StudyPopulation](StudyPopulation.md) - A group of individuals banded together or repaired as a group as participants in a research study.
             * [Cohort](Cohort.md) - A group of individuals banded together or repaired as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
 * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
 * [CyberEntity](CyberEntity.md) - An entity that has digital reality (a.k.a. cyber essence).
    * [ResourceSample](ResourceSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
 * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
    * [DatasetVersion](DatasetVersion.md)
       * [DatasetSummary](DatasetSummary.md)
       * [DistributionLevel](DistributionLevel.md)
 * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
 * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
 * [EmpiricalEntity](EmpiricalEntity.md) - Any entity or process that exists in the empirical domain and outside the computational realm. Errors are placed under computational entities
    * [EmpiricalIntervention](EmpiricalIntervention.md)
       * [OfflineMaintenance](OfflineMaintenance.md)
          * [OfflineMaintenanceOutcome](OfflineMaintenanceOutcome.md) - An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) offline maintenance.
    * [EmpiricalTrial](EmpiricalTrial.md)
 * [Entity](Entity.md) - Root Csolink Model class for all things and informational relationships, real or imagined.
    * [Association](Association.md) - A typed association between two entities, supported by evidence
       * [AdministrativeOperationalToComponentserviceAssociation](AdministrativeOperationalToComponentserviceAssociation.md) - An interaction between a administrative operational and a componentservice or servicetype.
       * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) - An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior.
       * [CaseToObservableFeatureAssociation](CaseToObservableFeatureAssociation.md) - An association between a case (e.g. individual patient) and a observable feature in which the individual has or has had the observability.
       * [ComponentTypeToErrorOrObservableFeatureAssociation](ComponentTypeToErrorOrObservableFeatureAssociation.md) - An relationship between a component type and a error or a observability, where the component type is derived from an individual with that error or observability.
          * [ComponentTypeAsAModelOfErrorAssociation](ComponentTypeAsAModelOfErrorAssociation.md)
       * [ComponentserviceRegulatoryRelationship](ComponentserviceRegulatoryRelationship.md) - A regulatory relationship between two componentservices
       * [ComponentserviceToAvailabilitySiteAssociation](ComponentserviceToAvailabilitySiteAssociation.md) - An association between a componentservice and an availability site, possibly qualified by stage/timing info.
       * [ComponentserviceToComponentserviceAssociation](ComponentserviceToComponentserviceAssociation.md) - abstract parent class for different kinds of componentservice-serviceunit or servicetype to servicetype relationships. Includes homology and interaction.
          * [ComponentserviceToComponentserviceCoavailabilityAssociation](ComponentserviceToComponentserviceCoavailabilityAssociation.md) - Indicates that two componentservices are co-available, generally under the same conditions.
          * [ComponentserviceToComponentserviceHomologyAssociation](ComponentserviceToComponentserviceHomologyAssociation.md) - A homology association between two componentservices. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
          * [PairwiseComponentserviceToComponentserviceInteraction](PairwiseComponentserviceToComponentserviceInteraction.md) - An interaction between two componentservices or two servicetypes. May be cyber (e.g. serviceinstance binding) or service (between componentservices). May be symmetric (e.g. serviceinstance interaction) or directed (e.g. phosphorylation)
             * [PairwiseOperationallyInteraction](PairwiseOperationallyInteraction.md) - An interaction at the operational level between two cyber entities
       * [ComponentserviceToErrorAssociation](ComponentserviceToErrorAssociation.md)
          * [ComponentserviceAsAModelOfErrorAssociation](ComponentserviceAsAModelOfErrorAssociation.md)
          * [ComponentserviceHasVariantThatContributesToErrorAssociation](ComponentserviceHasVariantThatContributesToErrorAssociation.md)
       * [ComponentserviceToObservableFeatureAssociation](ComponentserviceToObservableFeatureAssociation.md)
       * [ContributorAssociation](ContributorAssociation.md) - Any association between an entity (such as a publication) and various agents that contribute to its realisation
       * [DeploymentEntityToDeploymentEntityAssociation](DeploymentEntityToDeploymentEntityAssociation.md)
          * [DeploymentEntityToDeploymentEntityOntogenicAssociation](DeploymentEntityToDeploymentEntityOntogenicAssociation.md) - A relationship between two deployment entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship.
          * [DeploymentEntityToDeploymentEntityPartOfAssociation](DeploymentEntityToDeploymentEntityPartOfAssociation.md) - A relationship between two deployment entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between components and componentservices, between componentservice and servicegroup/replicasets, servicegroup/replicasets and whole systems
       * [ErrorOrObservableFeatureAssociationToLocationAssociation](ErrorOrObservableFeatureAssociationToLocationAssociation.md)
       * [ErrorOrObservableFeatureToLocationAssociation](ErrorOrObservableFeatureToLocationAssociation.md) - An association between either a error or a observable feature and an deployment entity, where the error/feature manifests in that site.
       * [ErrorToExposureEventAssociation](ErrorToExposureEventAssociation.md) - An association between an exposure event and a error.
       * [ErrorToObservableFeatureAssociation](ErrorToObservableFeatureAssociation.md) - An association between a error and a observable feature in which the observable feature is associated with the error in some way.
       * [ExposureEventToObservableFeatureAssociation](ExposureEventToObservableFeatureAssociation.md) - Any association between an environment and a observable feature, where being in the environment influences the observability.
       * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) - An association between an exposure event and an outcome.
       * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes) and either a operational activity, a computational process or a component location in which a function is executed.
          * [ComponentserviceToGoTermAssociation](ComponentserviceToGoTermAssociation.md)
          * [MacrooperationalMachineMixinToComponentAssociation](MacrooperationalMachineMixinToComponentAssociation.md) - A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a component (as represented in the GO component branch), where the entity carries out its function in the component
          * [MacrooperationalMachineMixinToComputationalProcessAssociation](MacrooperationalMachineMixinToComputationalProcessAssociation.md) - A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a computational process or pathway (as represented in the GO computational process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
          * [MacrooperationalMachineMixinToOperationalActivityAssociation](MacrooperationalMachineMixinToOperationalActivityAssociation.md) - A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a operational activity (as represented in the GO operational function branch), where the entity carries out the activity, or contributes to its execution
       * [OrchestrationToComponentserviceAssociation](OrchestrationToComponentserviceAssociation.md) - An interaction between a orchestration entity and a componentservice or servicetype.
       * [OrchestrationToErrorOrObservableFeatureAssociation](OrchestrationToErrorOrObservableFeatureAssociation.md) - An interaction between a orchestration entity and a observability or error, where the presence of the orchestration gives rise to or exacerbates the observability.
       * [OrchestrationToOrchestrationAssociation](OrchestrationToOrchestrationAssociation.md) - A relationship between two orchestration entities. This can encompass actual interactions as well as temporal causal edges, e.g. one orchestration converted to another.
          * [OrchestrationToOrchestrationDerivationAssociation](OrchestrationToOrchestrationDerivationAssociation.md) - A causal relationship between two orchestration entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
       * [OrchestrationToPathwayAssociation](OrchestrationToPathwayAssociation.md) - An interaction between a orchestration entity and a computational process or pathway.
       * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
       * [ResourceSampleDerivationAssociation](ResourceSampleDerivationAssociation.md) - An association between a resource sample and the resource entity from which it is derived.
       * [ResourceSampleToErrorOrObservableFeatureAssociation](ResourceSampleToErrorOrObservableFeatureAssociation.md) - An association between a resource sample and a error or observability.
       * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a workload entity it is localized to.
          * [ComponentserviceSequenceLocalization](ComponentserviceSequenceLocalization.md) - A relationship between a sequence feature and a workload entity it is localized to. The reference entity may be a container, componentservice or information entity such as a namespace.
       * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular daemon is part of a particular componentserviceinstance or componentservice
          * [ComponentserviceToServicetypeRelationship](ComponentserviceToServicetypeRelationship.md) - A componentservice is transcribed and potentially translated to a servicetype
          * [ComponentserviceinstanceToComponentserviceRelationship](ComponentserviceinstanceToComponentserviceRelationship.md) - A componentservice is a collection of componentserviceinstances
          * [DaemonToComponentserviceinstanceRelationship](DaemonToComponentserviceinstanceRelationship.md) - A componentserviceinstance is formed from multiple daemons
       * [SequenceVariantModulatesRepairingAssociation](SequenceVariantModulatesRepairingAssociation.md) - An association between a sequence variant and a repairing or health intervention. The repairing object itself encompasses both the error and the administrative operational used.
       * [ServiceunittypeToComponentserviceAssociation](ServiceunittypeToComponentserviceAssociation.md) - Any association between a serviceunittype and a componentservice. The serviceunittype have have multiple variants in that componentservice or a single one. There is no assumption of cardinality
       * [ServiceunittypeToErrorAssociation](ServiceunittypeToErrorAssociation.md)
          * [ServiceunittypeAsAModelOfErrorAssociation](ServiceunittypeAsAModelOfErrorAssociation.md)
       * [ServiceunittypeToObservableFeatureAssociation](ServiceunittypeToObservableFeatureAssociation.md) - Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the observability, either in isolation or through environment
       * [ServiceunittypeToServiceunittypePartAssociation](ServiceunittypeToServiceunittypePartAssociation.md) - Any association between one serviceunittype and a microservice entity that is a subset of it
       * [ServiceunittypeToVariantAssociation](ServiceunittypeToVariantAssociation.md) - Any association between a serviceunittype and a sequence variant.
       * [SystemicEntityAsAModelOfErrorAssociation](SystemicEntityAsAModelOfErrorAssociation.md)
       * [VariantToComponentserviceAssociation](VariantToComponentserviceAssociation.md) - An association between a variant and a componentservice, where the variant has a componentservice association with the componentservice (i.e. is in linkage disequilibrium)
          * [VariantToComponentserviceAvailabilityAssociation](VariantToComponentserviceAvailabilityAssociation.md) - An association between a variant and availability of a componentservice (i.e. e-QTL)
       * [VariantToErrorAssociation](VariantToErrorAssociation.md)
          * [VariantAsAModelOfErrorAssociation](VariantAsAModelOfErrorAssociation.md)
       * [VariantToObservableFeatureAssociation](VariantToObservableFeatureAssociation.md)
       * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
    * [NamedThing](NamedThing.md) - a databased entity or concept/class
       * [Activity](Activity.md) - An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
       * [AdministrativeEntity](AdministrativeEntity.md)
          * [Agent](Agent.md) - service, group, organization or project that provides a piece of information (i.e. a knowledge association)
       * [ComputationalEntity](ComputationalEntity.md)
          * [ComputationalProcessOrActivity](ComputationalProcessOrActivity.md) - Either an individual operational activity, or a collection of causally connected operational activities
             * [ComputationalProcess](ComputationalProcess.md) - One or more causally connected executions of operational functions
                * [Behavior](Behavior.md)
                   * [BehavioralExposure](BehavioralExposure.md) - A behavioral exposure is a factor relating to behavior impacting an individual.
                   * [BehavioralOutcome](BehavioralOutcome.md) - An outcome resulting from an exposure event which is the manifestation of individual behavior.
                   * [SocioeconomicExposure](SocioeconomicExposure.md) - A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty).
                   * [SocioeconomicOutcome](SocioeconomicOutcome.md) - An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event
                * [CyberProcess](CyberProcess.md)
                * [Death](Death.md)
                   * [MortalityOutcome](MortalityOutcome.md) - An outcome of death from resulting from an exposure event.
                * [FaultyProcess](FaultyProcess.md) - A compulogic function or a process having an abnormal or deleterious effect at the subcomponent, component, multi-component, node, or system level.
                   * [FaultyProcessExposure](FaultyProcessExposure.md) - A faulty process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
                   * [FaultyProcessOutcome](FaultyProcessOutcome.md) - An outcome resulting from an exposure event which is the manifestation of a faulty process.
                * [Pathway](Pathway.md)
             * [OperationalActivity](OperationalActivity.md) - An execution of a operational function carried out by a servicetype or macrooperational complex.
          * [EpidemiologicalOutcome](EpidemiologicalOutcome.md) - An epidemiological outcome, such as societal error burden, resulting from an exposure event.
          * [ErrorOrObservableFeature](ErrorOrObservableFeature.md) - Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as distinct, others conflate.
             * [Error](Error.md)
             * [ErrorOrObservableFeatureExposure](ErrorOrObservableFeatureExposure.md) - A error or observable feature exposure is where a error state is manifested which represents an precondition, leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular error.
             * [ErrorOrObservableFeatureOutcome](ErrorOrObservableFeatureOutcome.md) - logical outcomes resulting from an exposure event which is the manifestation of a error or other characteristic observability.
             * [ObservableFeature](ObservableFeature.md)
                * [BehavioralFeature](BehavioralFeature.md) - A observable feature which is behavioral in nature.
                * [EmpiricalFinding](EmpiricalFinding.md) - this category is currently considered broad enough to tag empirical lab measurements and other computational attributes taken as 'empirical traits' with some statistical score, for example, a p value in componentservice associations.
          * [OperationalEntity](OperationalEntity.md) - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
             * [AdministrativeOperation](AdministrativeOperation.md) - A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
                * [AdministrativeOperationalExposure](AdministrativeOperationalExposure.md) - A administrative operational exposure is an intake of a particular administrative operation.
                   * [AdministrativeOperationalToComponentserviceInteractionExposure](AdministrativeOperationalToComponentserviceInteractionExposure.md) - administrative operational to componentservice interaction exposure is a administrative operational exposure is where the interactions of the administrative operational with specific componentservices are known to constitute an 'exposure' to the system, leading to or influencing an outcome.
             * [ComponentserviceFamily](ComponentserviceFamily.md) - any grouping of multiple componentservices or servicetypes related by common descent
             * [ControlActor](ControlActor.md) - May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex resource with multiple orchestration entities as part
                * [ConsumedResource](ConsumedResource.md) - A control actor (often a cluster) consumed for information, engineering or technical use.
                * [Controller](Controller.md) - Any intermediate or servicetype resulting from director supervision. Includes primary and secondary controllers.
                * [NotificationComponent](NotificationComponent.md)
                   * [Awareness](Awareness.md)
                   * [Data](Data.md)
                      * [Bitstream](Bitstream.md)
                         * [MessagePassing](MessagePassing.md)
                      * [Datastream](Datastream.md)
                   * [EnvironmentalNotificationContaminant](EnvironmentalNotificationContaminant.md)
                * [OrchestrationExposure](OrchestrationExposure.md) - A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
                   * [ComplexOrchestrationExposure](ComplexOrchestrationExposure.md) - A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a administrative operation.
                * [Power](Power.md)
             * [Notification](Notification.md) - A event consumed by a healthy system as a source of information
             * [WorkloadEntity](WorkloadEntity.md) - An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon, regulatory region) or is encoded in a workload (serviceinstance)
                * [CodingSequence](CodingSequence.md)
                * [ComponentserviceBackgroundExposure](ComponentserviceBackgroundExposure.md) - A service background exposure is where an individual's specific service background of serviceunits, sequence variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or influencing an outcome.
                * [Componentserviceinstance](Componentserviceinstance.md) - The unit of service workload the component is capable of providing or protecting.
                   * [KernelServicetype](KernelServicetype.md)
                      * [KernelServicetypeIsoform](KernelServicetypeIsoform.md) - Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
                      * [NoncodingKernelServicetype](NoncodingKernelServicetype.md)
                         * [KernelInterrupt](KernelInterrupt.md) - TBD
                         * [KernelMessage](KernelMessage.md)
                * [Daemon](Daemon.md) - A region of the componentserviceinstance sequence within a componentservice.
                * [ReagentTargetedComponentservice](ReagentTargetedComponentservice.md) - A componentservice altered in its availability level in the context of some experiment as a result of being targeted by componentservice-knockdown reagent(s).
                * [SequenceVariant](SequenceVariant.md) - A variantcomponentservice that varies in its sequence from what is considered the reference variantcomponentservice at that locus.
                   * [MonomericVariant](MonomericVariant.md) - A single monomeric position in the service monomeric variants are single monomeric positions in service DNA at which different sequence alternatives exist
                * [Serviceinstance](Serviceinstance.md) - A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message
                   * [ServiceinstanceIsoform](ServiceinstanceIsoform.md) - Represents a serviceinstance that is a specific isoform of the canonical or reference serviceinstance.
                * [Serviceunittype](Serviceunittype.md) - An information content entity that describes a workload by specifying the total variation in service sequence and/or componentservice availability, relative to some established background
                * [Variantcomponentservicetype](Variantcomponentservicetype.md) - A set of zero or more variantcomponentservices on a single instance of a Sequence
                * [Workload](Workload.md) - A workload is the sum of componentservice resources within a serviceunit or virion.
          * [SystemicEntity](SystemicEntity.md) - A named entity that is either a part of a system, a whole system, population or clade of systems, excluding operational entities
             * [ComponentType](ComponentType.md) - A component type defines the set of components running the same software and sharing the same configuration. It's a single point of configuration control.
             * [DeploymentEntity](DeploymentEntity.md) - A process location, serviceunit type or gross deployment part
                * [Component](Component.md) - The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and repaired independently. Each component belongs to one, and only one, serviceunit.
                * [FaultyDeploymentStructure](FaultyDeploymentStructure.md) - An deployment structure with the potential of have an abnormal or deleterious effect at the process, serviceunit, multiserviceunit, or systemal level.
                   * [FaultyDeploymentExposure](FaultyDeploymentExposure.md) - An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome,
                   * [FaultyDeploymentOutcome](FaultyDeploymentOutcome.md) - An outcome resulting from an exposure event which is the manifestation of an abnormal deployment structure.
                * [GrossDeploymentStructure](GrossDeploymentStructure.md)
                * [Serviceunit](Serviceunit.md) - The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a cluster. It can be deployed, isolated, and repaired independently.
             * [IndividualSystem](IndividualSystem.md) - An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
                * [Case](Case.md) - An individual system that has a patient role in some empirical context.
             * [LifecycleStage](LifecycleStage.md) - A stage of development or growth of a system.
             * [PopulationOfIndividualSystems](PopulationOfIndividualSystems.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.
                * [StudyPopulation](StudyPopulation.md) - A group of individuals banded together or repaired as a group as participants in a research study.
                   * [Cohort](Cohort.md) - A group of individuals banded together or repaired as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
       * [CyberEntity](CyberEntity.md) - An entity that has digital reality (a.k.a. cyber essence).
          * [ResourceSample](ResourceSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
       * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
       * [EmpiricalEntity](EmpiricalEntity.md) - Any entity or process that exists in the empirical domain and outside the computational realm. Errors are placed under computational entities
          * [EmpiricalIntervention](EmpiricalIntervention.md)
             * [OfflineMaintenance](OfflineMaintenance.md)
                * [OfflineMaintenanceOutcome](OfflineMaintenanceOutcome.md) - An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) offline maintenance.
          * [EmpiricalTrial](EmpiricalTrial.md)
       * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.
          * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
          * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
             * [DatasetVersion](DatasetVersion.md)
                * [DatasetSummary](DatasetSummary.md)
                * [DistributionLevel](DistributionLevel.md)
          * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
          * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
          * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed resources, either directly or in one of the Publication Csolink category subclasses.
             * [Article](Article.md)
             * [Book](Book.md) - This class may rarely be available except if use cases of a given knowledge graph support its utility.
             * [BookChapter](BookChapter.md)
             * [Serial](Serial.md) - This class may rarely be available except if use cases of a given knowledge graph support its utility.
       * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
          * [ComponentserviceOntologyClass](ComponentserviceOntologyClass.md) - an ontology class that describes a controlling aspect of a componentservice, servicetype or complex
          * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
          * [SystemTaxon](SystemTaxon.md) - A classification of a set of systems. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
             * [BioticExposure](BioticExposure.md) - A biotic exposure is an intake of (sometimes faulty) computational systems (including viruses)
          * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
       * [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
       * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet
          * [EnvironmentalFeature](EnvironmentalFeature.md)
          * [EnvironmentalProcess](EnvironmentalProcess.md)
             * [EnvironmentalExposure](EnvironmentalExposure.md) - A environmental exposure is a factor relating to abiotic processes in the environment including atmospheric (heat, cold, general pollution) and water-born contaminants
          * [GeographicLocation](GeographicLocation.md) - a location that can be described in lat/long coordinates
             * [GeographicExposure](GeographicExposure.md) - A geographic exposure is a factor relating to geographic proximity to some impactful entity.
             * [GeographicLocationAtTime](GeographicLocationAtTime.md) - a location that can be described in lat/long coordinates, for a particular time
       * [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner
       * [Repairing](Repairing.md) - A repairing is targeted at a error or observability and may involve multiple administrative operational 'exposures', engineering devices and/or procedures

## Slots


### Predicates

 * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
    * [capable of](capable_of.md) - holds between a cyber entity and process or function, where the continuant alone has the ability to carry out the process or function.
 * [affected by](affected_by.md) - describes an entity of which the state or quality is affected by another existing entity.
    * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
    * [regulated by, entity to entity](regulated_by_entity_to_entity.md)
       * [negatively regulated by, entity to entity](negatively_regulated_by_entity_to_entity.md)
       * [positively regulated by, entity to entity](positively_regulated_by_entity_to_entity.md)
    * [regulated by, process to process](regulated_by_process_to_process.md)
       * [negatively regulated by, process to process](negatively_regulated_by_process_to_process.md)
       * [positively regulated by, process to process](positively_regulated_by_process_to_process.md)
 * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents', where the outcome is something that may or may not come to be.
    * [affects abundance of](affects_abundance_of.md) - holds between two operational entities where the action or effect of one changes the amount of the other within a system of interest
       * [decreases abundance of](decreases_abundance_of.md) - holds between two operational entities where the action or effect of one decreases the amount of the other within a system of interest
       * [increases abundance of](increases_abundance_of.md) - holds between two operational entities where the action or effect of one increases the amount of the other within a system of interest
    * [affects activity of](affects_activity_of.md) - holds between two operational entities where the action or effect of one changes the activity of the other within a system of interest
       * [decreases activity of](decreases_activity_of.md) - holds between two operational entities where the action or effect of one decreases the activity of the other within a system of interest
       * [increases activity of](increases_activity_of.md) - holds between two operational entities where the action or effect of one increases the activity of the other within a system of interest
    * [affects assignment of](affects_assignment_of.md) - holds between two operational entities where the action or effect of one changes the rate or quality of assignment of the other
       * [decreases assignment of](decreases_assignment_of.md) - holds between two operational entities where the action or effect of one decreases the rate or quality of assignment of the other
       * [increases assignment of](increases_assignment_of.md) - holds between two operational entities where the action or effect of one increases the rate or quality of assignment of the other
    * [affects availability in](affects_availability_in.md) - Holds between a variant and an deployment entity where the availability of the variant is located in.
    * [affects availability of](affects_availability_of.md) - holds between two operational entities where the action or effect of one changes the level of availability of the other within a system of interest
       * [decreases availability of](decreases_availability_of.md) - holds between two operational entities where the action or effect of one decreases the level of availability of the other within a system of interest
       * [increases availability of](increases_availability_of.md) - holds between two operational entities where the action or effect of one increases the level of availability of the other within a system of interest
    * [affects degradation of](affects_degradation_of.md) - holds between two operational entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where orchestration degradation is defined act or process of simplifying or breaking down a task into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995)
       * [decreases degradation of](decreases_degradation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
       * [increases degradation of](increases_degradation_of.md) - holds between two operational entities where the action or effect of one increases the rate of degradation of the other within a system of interest
    * [affects instantiation of](affects_instantiation_of.md) - holds between two operational entities where the action or effect of one impacts the rate of orchestration instantiation of the other
       * [decreases instantiation of](decreases_instantiation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of orchestration instantiation of the other
       * [increases instantiation of](increases_instantiation_of.md) - holds between two operational entities where the action or effect of one increases the rate of orchestration instantiation of the other
    * [affects localization of](affects_localization_of.md) - holds between two operational entities where the action or effect of one changes the localization of the other within a system of interest
       * [decreases localization of](decreases_localization_of.md) - holds between two operational entities where the action or effect of one decreases the proper localization of the other within a system of interest
       * [increases localization of](increases_localization_of.md) - holds between two operational entities where the action or effect of one increases the proper localization of the other within a system of interest
    * [affects operational modification of](affects_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads changes in the operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as changing component configuration.
       * [decreases operational modification of](decreases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to decreased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as  ..
       * [increases operational modification of](increases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to increased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as the addition of a component type.
    * [affects output of](affects_output_of.md) - holds between two operational entities where the action or effect of one impacts the rate of output of the other out of a serviceunit, computehost, or application
       * [decreases output of](decreases_output_of.md) - holds between two operational entities where the action or effect of one decreases the rate of output of the other out of a serviceunit, computehost, or application
       * [increases output of](increases_output_of.md) - holds between two operational entities where the action or effect of one increases the rate of output of the other out of a serviceunit, computehost, or application
    * [affects response to](affects_response_to.md) - holds between two operational entities where the action or effect of one impacts the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
       * [decreases response to](decreases_response_to.md) - holds between two operational entities where the action or effect of one decreases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
       * [increases response to](increases_response_to.md) - holds between two operational entities where the action or effect of one increases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
    * [affects splicing of](affects_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity impacts the splicing of the kernel message
       * [decreases splicing of](decreases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity decreases the proper splicing of the kernel message
       * [increases splicing of](increases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity increases the proper splicing of the kernel message
    * [affects stability of](affects_stability_of.md) - holds between two operational entities where the action or effect of one impacts the stability of the other within a system of interest
       * [decreases stability of](decreases_stability_of.md) - holds between two operational entities where the action or effect of one decreases the stability of the other within a system of interest
       * [increases stability of](increases_stability_of.md) - holds between two operational entities where the action or effect of one increases the stability of the other within a system of interest
    * [affects supervision of](affects_supervision_of.md) - holds between two operational entities where the action or effect of one impacts the supervision of the other within a system of interest
       * [decreases supervision of](decreases_supervision_of.md) - holds between two operational entities where the action or effect of one decreases the rate of supervision of the other within a system of interest
       * [increases supervision of](increases_supervision_of.md) - holds between two operational entities where the action or effect of one increases the rate of supervision of the other within a system of interest
    * [affects transport of](affects_transport_of.md) - holds between two operational entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
       * [decreases transport of](decreases_transport_of.md) - holds between two operational entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
       * [increases transport of](increases_transport_of.md) - holds between two operational entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
    * [affects updates rate of](affects_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity impacts the rate of update of the workload entity within a system of interest
       * [decreases updates rate of](decreases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity decreases the rate of update of the workload entity within a system of interest
       * [increases updates rate of](increases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity increases the rate of update of the workload entity within a system of interest
    * [affects uptake of](affects_uptake_of.md) - holds between two operational entities where the action or effect of one impacts the rate of uptake of the other into of a serviceunit, computehost, or application
       * [decreases uptake of](decreases_uptake_of.md) - holds between two operational entities where the action or effect of one decreases the rate of uptake of the other into of a serviceunit, computehost, or application
       * [increases uptake of](increases_uptake_of.md) - holds between two operational entities where the action or effect of one increases the rate of uptake of the other into of a serviceunit, computehost, or application
    * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a serviceunittype, service variation, orchestration, or environmental exposure) and a condition (a observability or error), where the presence of the entity reduces or eliminates some or all aspects of the condition.
       * [repairs](repairs.md) - holds between a therapeutic procedure or control actor and a error or observable feature that it is used to repair
          * [approved to repair](approved_to_repair.md) - TBD
    * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
    * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a orchestration, environmental exposure, or some form of service variation) and a condition (a observability or error), where the presence of the entity worsens some or all aspects of the condition.
    * [regulates, entity to entity](regulates_entity_to_entity.md)
       * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
       * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
    * [regulates, process to process](regulates_process_to_process.md)
       * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
       * [positively regulates, process to process](positively_regulates_process_to_process.md)
 * [affects abundance of](affects_abundance_of.md) - holds between two operational entities where the action or effect of one changes the amount of the other within a system of interest
    * [decreases abundance of](decreases_abundance_of.md) - holds between two operational entities where the action or effect of one decreases the amount of the other within a system of interest
    * [increases abundance of](increases_abundance_of.md) - holds between two operational entities where the action or effect of one increases the amount of the other within a system of interest
 * [affects activity of](affects_activity_of.md) - holds between two operational entities where the action or effect of one changes the activity of the other within a system of interest
    * [decreases activity of](decreases_activity_of.md) - holds between two operational entities where the action or effect of one decreases the activity of the other within a system of interest
    * [increases activity of](increases_activity_of.md) - holds between two operational entities where the action or effect of one increases the activity of the other within a system of interest
 * [affects assignment of](affects_assignment_of.md) - holds between two operational entities where the action or effect of one changes the rate or quality of assignment of the other
    * [decreases assignment of](decreases_assignment_of.md) - holds between two operational entities where the action or effect of one decreases the rate or quality of assignment of the other
    * [increases assignment of](increases_assignment_of.md) - holds between two operational entities where the action or effect of one increases the rate or quality of assignment of the other
 * [affects availability in](affects_availability_in.md) - Holds between a variant and an deployment entity where the availability of the variant is located in.
 * [affects availability of](affects_availability_of.md) - holds between two operational entities where the action or effect of one changes the level of availability of the other within a system of interest
    * [decreases availability of](decreases_availability_of.md) - holds between two operational entities where the action or effect of one decreases the level of availability of the other within a system of interest
    * [increases availability of](increases_availability_of.md) - holds between two operational entities where the action or effect of one increases the level of availability of the other within a system of interest
 * [affects degradation of](affects_degradation_of.md) - holds between two operational entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where orchestration degradation is defined act or process of simplifying or breaking down a task into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995)
    * [decreases degradation of](decreases_degradation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
    * [increases degradation of](increases_degradation_of.md) - holds between two operational entities where the action or effect of one increases the rate of degradation of the other within a system of interest
 * [affects instantiation of](affects_instantiation_of.md) - holds between two operational entities where the action or effect of one impacts the rate of orchestration instantiation of the other
    * [decreases instantiation of](decreases_instantiation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of orchestration instantiation of the other
    * [increases instantiation of](increases_instantiation_of.md) - holds between two operational entities where the action or effect of one increases the rate of orchestration instantiation of the other
 * [affects localization of](affects_localization_of.md) - holds between two operational entities where the action or effect of one changes the localization of the other within a system of interest
    * [decreases localization of](decreases_localization_of.md) - holds between two operational entities where the action or effect of one decreases the proper localization of the other within a system of interest
    * [increases localization of](increases_localization_of.md) - holds between two operational entities where the action or effect of one increases the proper localization of the other within a system of interest
 * [affects operational modification of](affects_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads changes in the operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as changing component configuration.
    * [decreases operational modification of](decreases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to decreased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as  ..
    * [increases operational modification of](increases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to increased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as the addition of a component type.
 * [affects output of](affects_output_of.md) - holds between two operational entities where the action or effect of one impacts the rate of output of the other out of a serviceunit, computehost, or application
    * [decreases output of](decreases_output_of.md) - holds between two operational entities where the action or effect of one decreases the rate of output of the other out of a serviceunit, computehost, or application
    * [increases output of](increases_output_of.md) - holds between two operational entities where the action or effect of one increases the rate of output of the other out of a serviceunit, computehost, or application
 * [affects response to](affects_response_to.md) - holds between two operational entities where the action or effect of one impacts the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
    * [decreases response to](decreases_response_to.md) - holds between two operational entities where the action or effect of one decreases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
    * [increases response to](increases_response_to.md) - holds between two operational entities where the action or effect of one increases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
 * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
    * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
    * [prevents](prevents.md) - holds between an entity whose system or use reduces the likelihood of a potential outcome. Typically used to associate a control actor, exposure, activity, or engineering intervention that can prevent the onset a error or observable feature.
 * [affects splicing of](affects_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity impacts the splicing of the kernel message
    * [decreases splicing of](decreases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity decreases the proper splicing of the kernel message
    * [increases splicing of](increases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity increases the proper splicing of the kernel message
 * [affects stability of](affects_stability_of.md) - holds between two operational entities where the action or effect of one impacts the stability of the other within a system of interest
    * [decreases stability of](decreases_stability_of.md) - holds between two operational entities where the action or effect of one decreases the stability of the other within a system of interest
    * [increases stability of](increases_stability_of.md) - holds between two operational entities where the action or effect of one increases the stability of the other within a system of interest
 * [affects supervision of](affects_supervision_of.md) - holds between two operational entities where the action or effect of one impacts the supervision of the other within a system of interest
    * [decreases supervision of](decreases_supervision_of.md) - holds between two operational entities where the action or effect of one decreases the rate of supervision of the other within a system of interest
    * [increases supervision of](increases_supervision_of.md) - holds between two operational entities where the action or effect of one increases the rate of supervision of the other within a system of interest
 * [affects transport of](affects_transport_of.md) - holds between two operational entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
    * [decreases transport of](decreases_transport_of.md) - holds between two operational entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
    * [increases transport of](increases_transport_of.md) - holds between two operational entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
 * [affects updates rate of](affects_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity impacts the rate of update of the workload entity within a system of interest
    * [decreases updates rate of](decreases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity decreases the rate of update of the workload entity within a system of interest
    * [increases updates rate of](increases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity increases the rate of update of the workload entity within a system of interest
 * [affects uptake of](affects_uptake_of.md) - holds between two operational entities where the action or effect of one impacts the rate of uptake of the other into of a serviceunit, computehost, or application
    * [decreases uptake of](decreases_uptake_of.md) - holds between two operational entities where the action or effect of one decreases the rate of uptake of the other into of a serviceunit, computehost, or application
    * [increases uptake of](increases_uptake_of.md) - holds between two operational entities where the action or effect of one increases the rate of uptake of the other into of a serviceunit, computehost, or application
 * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a serviceunittype, service variation, orchestration, or environmental exposure) and a condition (a observability or error), where the presence of the entity reduces or eliminates some or all aspects of the condition.
    * [repairs](repairs.md) - holds between a therapeutic procedure or control actor and a error or observable feature that it is used to repair
       * [approved to repair](approved_to_repair.md) - TBD
 * [approved for repairing by](approved_for_repairing_by.md) - TBD
 * [approved to repair](approved_to_repair.md) - TBD
 * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
 * [available in](available_in.md) - holds between a componentservice or servicetype and an deployment entity in which it is available
 * [broad match](broad_match.md) - a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
 * [capable of](capable_of.md) - holds between a cyber entity and process or function, where the continuant alone has the ability to carry out the process or function.
 * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other
 * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
    * [causes adverse event](causes_adverse_event.md) - holds between a administrative operationa and a error or observability that can be caused by the administrative operation
 * [causes adverse event](causes_adverse_event.md) - holds between a administrative operationa and a error or observability that can be caused by the administrative operation
 * [close match](close_match.md) - a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. administrative operation as a type of control entity versus administrative operation as a type of role borne by a control entity).
    * [exact match](exact_match.md) - holds between two entities that are identical to each other, with a high degree of confidence
       * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [coavailable with](coavailable_with.md) - holds between any two componentservices or servicetypes, in which both are generally available within a single defined experimental context.
 * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
    * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
    * [in complex with](in_complex_with.md) - holds between two componentservices or servicetypes that are part of (or code for servicetypes that are part of) in the same macrooperational complex mixin
    * [in pathway with](in_pathway_with.md) - holds between two componentservice or servicetypes that are part of in the same computational pathway
    * [in serviceunit population with](in_serviceunit_population_with.md) - holds between two componentservice or servicetypes that are available in the same serviceunit type or population
 * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
 * [componentservice associated with condition](componentservice_associated_with_condition.md) - holds between a componentservice and a error or observable feature that the componentservice or its variantcomponentservice may influence, contribute to, or correlate with
 * [componentservice association](componentservice_association.md) - Co-occurrence of a certain variantcomponentservice marker and the observability of interest in the same individuals at above-chance level
    * [componentservice associated with condition](componentservice_associated_with_condition.md) - holds between a componentservice and a error or observable feature that the componentservice or its variantcomponentservice may influence, contribute to, or correlate with
    * [condition associated with componentservice](condition_associated_with_componentservice.md) - holds between a componentservice and a error or observable feature that may be influenced, contribute to, or be correlated with the componentservice or its incorrect correct/servicetypes
 * [componentservice interacts with](componentservice_interacts_with.md) - holds between two componentservices whose observable effects are dependent on each other in some way - such that their combined observable effects are the result of some interaction between the activity of their servicetypes. Example is service-unit death when two componentservices simultaneously fail, or platform startup facilitating tenant services.
 * [condition associated with componentservice](condition_associated_with_componentservice.md) - holds between a componentservice and a error or observable feature that may be influenced, contribute to, or be correlated with the componentservice or its incorrect correct/servicetypes
 * [contraindicated for](contraindicated_for.md) - Holds between a administrative operational and a error or observability, such that a service with that error should not be repaired with the administrative operation.
 * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
    * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
       * [causes adverse event](causes_adverse_event.md) - holds between a administrative operationa and a error or observability that can be caused by the administrative operation
 * [contributor](contributor.md)
    * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
    * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
    * [provider](provider.md) - service, person, group, organization or project that provides a piece of information (e.g. a knowledge association).
    * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, componentcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
 * [correlated with](correlated_with.md) - holds between any two named thing entities. For example, correlated_with holds between a error or observable feature and a measurable operation entity that is used as an indicator of the presence or state of the error or feature.
    * [coavailable with](coavailable_with.md) - holds between any two componentservices or servicetypes, in which both are generally available within a single defined experimental context.
    * [has marker](has_marker.md) - holds between a error or observable feature and a measurable operational entity that is used as an indicator of the presence or state of the error or feature.
    * [marker for](marker_for.md) - holds between a measurable operational entity and a error or observable feature, where the entity is used as an indicator of the presence or state of the error or feature.
    * [negatively correlated with](negatively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a negative manner.
    * [positively correlated with](positively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a positive manner.
 * [cyber interaction with](cyber_interaction_with.md) - holds between two entities that make cyber contact as part of some interaction
    * [operationally interacts with](operationally_interacts_with.md)
       * [decreases operational interaction](decreases_operational_interaction.md) - indicates that the source decreases the operationally interaction between the target and some other operational entity
       * [increases operational interaction](increases_operational_interaction.md) - indicates that the source increases the operationally interaction between the target and some other operational entity
 * [data of](data_of.md)
 * [decreases abundance of](decreases_abundance_of.md) - holds between two operational entities where the action or effect of one decreases the amount of the other within a system of interest
 * [decreases activity of](decreases_activity_of.md) - holds between two operational entities where the action or effect of one decreases the activity of the other within a system of interest
 * [decreases assignment of](decreases_assignment_of.md) - holds between two operational entities where the action or effect of one decreases the rate or quality of assignment of the other
 * [decreases availability of](decreases_availability_of.md) - holds between two operational entities where the action or effect of one decreases the level of availability of the other within a system of interest
 * [decreases degradation of](decreases_degradation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
 * [decreases instantiation of](decreases_instantiation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of orchestration instantiation of the other
 * [decreases localization of](decreases_localization_of.md) - holds between two operational entities where the action or effect of one decreases the proper localization of the other within a system of interest
 * [decreases operational interaction](decreases_operational_interaction.md) - indicates that the source decreases the operationally interaction between the target and some other operational entity
 * [decreases operational modification of](decreases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to decreased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as  ..
 * [decreases output of](decreases_output_of.md) - holds between two operational entities where the action or effect of one decreases the rate of output of the other out of a serviceunit, computehost, or application
 * [decreases response to](decreases_response_to.md) - holds between two operational entities where the action or effect of one decreases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
 * [decreases splicing of](decreases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity decreases the proper splicing of the kernel message
 * [decreases stability of](decreases_stability_of.md) - holds between two operational entities where the action or effect of one decreases the stability of the other within a system of interest
 * [decreases supervision of](decreases_supervision_of.md) - holds between two operational entities where the action or effect of one decreases the rate of supervision of the other within a system of interest
 * [decreases transport of](decreases_transport_of.md) - holds between two operational entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
 * [decreases updates rate of](decreases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity decreases the rate of update of the workload entity within a system of interest
 * [decreases uptake of](decreases_uptake_of.md) - holds between two operational entities where the action or effect of one decreases the rate of uptake of the other into of a serviceunit, computehost, or application
 * [derives from](derives_from.md) - holds between two distinct resource entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [is controller of](is_controller_of.md) - holds between two control actors in which the first one is derived from the second one as a product of supervision
 * [derives into](derives_into.md) - holds between two distinct resource entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * [has controller](has_controller.md) - holds between two control actors in which the second one is derived from the first one as a product of supervision
 * [develops from](develops_from.md)
 * [directly interacts with](directly_interacts_with.md) - Holds between operational entities that cyberly and directly interact with each other
 * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
 * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
 * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
 * [enabled by](enabled_by.md) - holds between a process and a cyber entity, where the cyber entity executes the process
 * [enables](enables.md) - holds between a cyber entity and a process, where the cyber entity executes the process
 * [error has basis in](error_has_basis_in.md) - A relation that holds between a error and an entity where the state of the entity has contribution to the error.
 * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a orchestration, environmental exposure, or some form of service variation) and a condition (a observability or error), where the presence of the entity worsens some or all aspects of the condition.
 * [exact match](exact_match.md) - holds between two entities that are identical to each other, with a high degree of confidence
    * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [has active ingredient](has_active_ingredient.md) - holds between a administrative operation and a control actor in which the latter is a part of the former, and is a computationally active component
 * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
 * [has controller](has_controller.md) - holds between two control actors in which the second one is derived from the first one as a product of supervision
 * [has data](has_data.md) - one or more datas which are growth factors for a system
 * [has decreased amount](has_decreased_amount.md)
 * [has excipient](has_excipient.md) - holds between a administrative operation and a control actors in which the latter is a part of the former, and is a computationally inactive component
 * [has increased amount](has_increased_amount.md)
 * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
 * [has marker](has_marker.md) - holds between a error or observable feature and a measurable operational entity that is used as an indicator of the presence or state of the error or feature.
 * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
 * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
    * [has data](has_data.md) - one or more datas which are growth factors for a system
 * [has observability](has_observability.md) - holds between a computational entity and a observability, where a observability is construed broadly as any kind of quality of an subsystem, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
 * [has operational consequence](has_operational_consequence.md) - connects a sequence variant to a class describing the operation consequence. E.g.  SO:0001583
 * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [has part](has_part.md) - holds between wholes and their parts (resource entities or processes)
    * [has active ingredient](has_active_ingredient.md) - holds between a administrative operation and a control actor in which the latter is a part of the former, and is a computationally active component
    * [has excipient](has_excipient.md) - holds between a administrative operation and a control actors in which the latter is a part of the former, and is a computationally inactive component
    * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
       * [has data](has_data.md) - one or more datas which are growth factors for a system
    * [has variant part](has_variant_part.md) - holds between a workload entity and a microservice entity that is a subset of it
 * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
    * [enabled by](enabled_by.md) - holds between a process and a cyber entity, where the cyber entity executes the process
    * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
    * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
 * [has sequence location](has_sequence_location.md) - holds between two service entities when the subject can be localized in sequence coordinates on the object. For example, between an daemon and a container/namespace.
 * [has servicetype](has_servicetype.md) - holds between a componentservice and a transcribed and/or translated servicetype generated from it
 * [has variant part](has_variant_part.md) - holds between a workload entity and a microservice entity that is a subset of it
 * [homologous to](homologous_to.md) - holds between two computational entities that have common evolutionary service
    * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically componentservices) that diverged after a speciation event.
    * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically componentservices) that diverged after a duplication event.
    * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
 * [in complex with](in_complex_with.md) - holds between two componentservices or servicetypes that are part of (or code for servicetypes that are part of) in the same macrooperational complex mixin
 * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
 * [in pathway with](in_pathway_with.md) - holds between two componentservice or servicetypes that are part of in the same computational pathway
 * [in serviceunit population with](in_serviceunit_population_with.md) - holds between two componentservice or servicetypes that are available in the same serviceunit type or population
 * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
 * [increases abundance of](increases_abundance_of.md) - holds between two operational entities where the action or effect of one increases the amount of the other within a system of interest
 * [increases activity of](increases_activity_of.md) - holds between two operational entities where the action or effect of one increases the activity of the other within a system of interest
 * [increases assignment of](increases_assignment_of.md) - holds between two operational entities where the action or effect of one increases the rate or quality of assignment of the other
 * [increases availability of](increases_availability_of.md) - holds between two operational entities where the action or effect of one increases the level of availability of the other within a system of interest
 * [increases degradation of](increases_degradation_of.md) - holds between two operational entities where the action or effect of one increases the rate of degradation of the other within a system of interest
 * [increases instantiation of](increases_instantiation_of.md) - holds between two operational entities where the action or effect of one increases the rate of orchestration instantiation of the other
 * [increases localization of](increases_localization_of.md) - holds between two operational entities where the action or effect of one increases the proper localization of the other within a system of interest
 * [increases operational interaction](increases_operational_interaction.md) - indicates that the source increases the operationally interaction between the target and some other operational entity
 * [increases operational modification of](increases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to increased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as the addition of a component type.
 * [increases output of](increases_output_of.md) - holds between two operational entities where the action or effect of one increases the rate of output of the other out of a serviceunit, computehost, or application
 * [increases response to](increases_response_to.md) - holds between two operational entities where the action or effect of one increases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
 * [increases splicing of](increases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity increases the proper splicing of the kernel message
 * [increases stability of](increases_stability_of.md) - holds between two operational entities where the action or effect of one increases the stability of the other within a system of interest
 * [increases supervision of](increases_supervision_of.md) - holds between two operational entities where the action or effect of one increases the rate of supervision of the other within a system of interest
 * [increases transport of](increases_transport_of.md) - holds between two operational entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
 * [increases updates rate of](increases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity increases the rate of update of the workload entity within a system of interest
 * [increases uptake of](increases_uptake_of.md) - holds between two operational entities where the action or effect of one increases the rate of uptake of the other into of a serviceunit, computehost, or application
 * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
    * [componentservice interacts with](componentservice_interacts_with.md) - holds between two componentservices whose observable effects are dependent on each other in some way - such that their combined observable effects are the result of some interaction between the activity of their servicetypes. Example is service-unit death when two componentservices simultaneously fail, or platform startup facilitating tenant services.
    * [cyber interaction with](cyber_interaction_with.md) - holds between two entities that make cyber contact as part of some interaction
       * [operationally interacts with](operationally_interacts_with.md)
          * [decreases operational interaction](decreases_operational_interaction.md) - indicates that the source decreases the operationally interaction between the target and some other operational entity
          * [increases operational interaction](increases_operational_interaction.md) - indicates that the source increases the operationally interaction between the target and some other operational entity
    * [directly interacts with](directly_interacts_with.md) - Holds between operational entities that cyberly and directly interact with each other
 * [is active ingredient of](is_active_ingredient_of.md) - holds between a control actor and a administrative operation, in which the former is a part of the latter, and is a computationally active component
 * [is controller of](is_controller_of.md) - holds between two control actors in which the first one is derived from the second one as a product of supervision
 * [is excipient of](is_excipient_of.md) - holds between a control actor and a administrative operation in which the former is a part of the latter, and is a computationally inactive component
 * [is missense variant of](is_missense_variant_of.md) - holds between a componentservice  and a sequence variant, such the sequence variant results in a different instruction sequence but the serviceinstance is preserved.
 * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a componentservice sequence that the variant is close to.
 * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a componentservice, where the variant does not affect the coding sequence
 * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant results in a premature sequence stop.
 * [is protocol variant of](is_protocol_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant causes a disruption of the translational reading frames and/or packets.
 * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a workload entity
    * [is missense variant of](is_missense_variant_of.md) - holds between a componentservice  and a sequence variant, such the sequence variant results in a different instruction sequence but the serviceinstance is preserved.
    * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a componentservice sequence that the variant is close to.
    * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a componentservice, where the variant does not affect the coding sequence
    * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant results in a premature sequence stop.
    * [is protocol variant of](is_protocol_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant causes a disruption of the translational reading frames and/or packets.
    * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant is in the canonical splice site of one of the componentservice's daemons.
    * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant is in the coding sequence of the componentservice, but results in the same instruction sequence
 * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant is in the canonical splice site of one of the componentservice's daemons.
 * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant is in the coding sequence of the componentservice, but results in the same instruction sequence
 * [lacks part](lacks_part.md)
 * [located in](located_in.md) - holds between a resource entity and a resource entity or site within which it is located (but of which it is not considered a part)
 * [location of](location_of.md) - holds between resource entity or site and a resource entity that is located within it (but not considered a part of it)
 * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly available, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some error or syndrome
 * [marker for](marker_for.md) - holds between a measurable operational entity and a error or observable feature, where the entity is used as an indicator of the presence or state of the error or feature.
 * [model of](model_of.md) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [narrow match](narrow_match.md) - a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
 * [negatively correlated with](negatively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a negative manner.
 * [negatively regulated by, entity to entity](negatively_regulated_by_entity_to_entity.md)
 * [negatively regulated by, process to process](negatively_regulated_by_process_to_process.md)
 * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
 * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
 * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
    * [data of](data_of.md)
 * [occurs in](occurs_in.md) - holds between a process and a resource entity or site within which the process occurs
 * [operationally interacts with](operationally_interacts_with.md)
    * [decreases operational interaction](decreases_operational_interaction.md) - indicates that the source decreases the operationally interaction between the target and some other operational entity
    * [increases operational interaction](increases_operational_interaction.md) - indicates that the source increases the operationally interaction between the target and some other operational entity
 * [orchestrationly similar to](orchestrationly_similar_to.md) - holds between one control actors and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically componentservices) that diverged after a speciation event.
 * [overlaps](overlaps.md) - holds between entities that overlap in their extents (resources or processes)
    * [has part](has_part.md) - holds between wholes and their parts (resource entities or processes)
       * [has active ingredient](has_active_ingredient.md) - holds between a administrative operation and a control actor in which the latter is a part of the former, and is a computationally active component
       * [has excipient](has_excipient.md) - holds between a administrative operation and a control actors in which the latter is a part of the former, and is a computationally inactive component
       * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
          * [has data](has_data.md) - one or more datas which are growth factors for a system
       * [has variant part](has_variant_part.md) - holds between a workload entity and a microservice entity that is a subset of it
    * [part of](part_of.md) - holds between parts and wholes (resource entities or processes)
       * [is active ingredient of](is_active_ingredient_of.md) - holds between a control actor and a administrative operation, in which the former is a part of the latter, and is a computationally active component
       * [is excipient of](is_excipient_of.md) - holds between a control actor and a administrative operation in which the former is a part of the latter, and is a computationally inactive component
       * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
          * [data of](data_of.md)
 * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically componentservices) that diverged after a duplication event.
 * [part of](part_of.md) - holds between parts and wholes (resource entities or processes)
    * [is active ingredient of](is_active_ingredient_of.md) - holds between a control actor and a administrative operation, in which the former is a part of the latter, and is a computationally active component
    * [is excipient of](is_excipient_of.md) - holds between a control actor and a administrative operation in which the former is a part of the latter, and is a computationally inactive component
    * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
       * [data of](data_of.md)
 * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
    * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
       * [capable of](capable_of.md) - holds between a cyber entity and process or function, where the continuant alone has the ability to carry out the process or function.
    * [enables](enables.md) - holds between a cyber entity and a process, where the cyber entity executes the process
 * [positively correlated with](positively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a positive manner.
 * [positively regulated by, entity to entity](positively_regulated_by_entity_to_entity.md)
 * [positively regulated by, process to process](positively_regulated_by_process_to_process.md)
 * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
 * [positively regulates, process to process](positively_regulates_process_to_process.md)
 * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
 * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
 * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
 * [prevented by](prevented_by.md) - holds between a potential outcome of which the likelihood was reduced by the system or use of an entity.
 * [prevents](prevents.md) - holds between an entity whose system or use reduces the likelihood of a potential outcome. Typically used to associate a control actor, exposure, activity, or engineering intervention that can prevent the onset a error or observable feature.
 * [produced by](produced_by.md)
 * [produces](produces.md) - holds between a resource entity and a servicetype that is generated through the intentional actions or functioning of the resource entity
 * [provider](provider.md) - service, person, group, organization or project that provides a piece of information (e.g. a knowledge association).
 * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, componentcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
 * [regulated by, entity to entity](regulated_by_entity_to_entity.md)
    * [negatively regulated by, entity to entity](negatively_regulated_by_entity_to_entity.md)
    * [positively regulated by, entity to entity](positively_regulated_by_entity_to_entity.md)
 * [regulated by, process to process](regulated_by_process_to_process.md)
    * [negatively regulated by, process to process](negatively_regulated_by_process_to_process.md)
    * [positively regulated by, process to process](positively_regulated_by_process_to_process.md)
 * [regulates, entity to entity](regulates_entity_to_entity.md)
    * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
    * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
 * [regulates, process to process](regulates_process_to_process.md)
    * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
    * [positively regulates, process to process](positively_regulates_process_to_process.md)
 * [related condition](related_condition.md)
 * [related to](related_to.md) - A relationship that is asserted between two named things
    * [affected by](affected_by.md) - describes an entity of which the state or quality is affected by another existing entity.
       * [disrupted by](disrupted_by.md) - describes a relationship where the structure, function, or occurrence of one entity is degraded or interfered with by another.
       * [regulated by, entity to entity](regulated_by_entity_to_entity.md)
          * [negatively regulated by, entity to entity](negatively_regulated_by_entity_to_entity.md)
          * [positively regulated by, entity to entity](positively_regulated_by_entity_to_entity.md)
       * [regulated by, process to process](regulated_by_process_to_process.md)
          * [negatively regulated by, process to process](negatively_regulated_by_process_to_process.md)
          * [positively regulated by, process to process](positively_regulated_by_process_to_process.md)
    * [affects](affects.md) - describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents', where the outcome is something that may or may not come to be.
       * [affects abundance of](affects_abundance_of.md) - holds between two operational entities where the action or effect of one changes the amount of the other within a system of interest
          * [decreases abundance of](decreases_abundance_of.md) - holds between two operational entities where the action or effect of one decreases the amount of the other within a system of interest
          * [increases abundance of](increases_abundance_of.md) - holds between two operational entities where the action or effect of one increases the amount of the other within a system of interest
       * [affects activity of](affects_activity_of.md) - holds between two operational entities where the action or effect of one changes the activity of the other within a system of interest
          * [decreases activity of](decreases_activity_of.md) - holds between two operational entities where the action or effect of one decreases the activity of the other within a system of interest
          * [increases activity of](increases_activity_of.md) - holds between two operational entities where the action or effect of one increases the activity of the other within a system of interest
       * [affects assignment of](affects_assignment_of.md) - holds between two operational entities where the action or effect of one changes the rate or quality of assignment of the other
          * [decreases assignment of](decreases_assignment_of.md) - holds between two operational entities where the action or effect of one decreases the rate or quality of assignment of the other
          * [increases assignment of](increases_assignment_of.md) - holds between two operational entities where the action or effect of one increases the rate or quality of assignment of the other
       * [affects availability in](affects_availability_in.md) - Holds between a variant and an deployment entity where the availability of the variant is located in.
       * [affects availability of](affects_availability_of.md) - holds between two operational entities where the action or effect of one changes the level of availability of the other within a system of interest
          * [decreases availability of](decreases_availability_of.md) - holds between two operational entities where the action or effect of one decreases the level of availability of the other within a system of interest
          * [increases availability of](increases_availability_of.md) - holds between two operational entities where the action or effect of one increases the level of availability of the other within a system of interest
       * [affects degradation of](affects_degradation_of.md) - holds between two operational entities where the action or effect of one impacts the rate of degradation of the other within a system of interest, where orchestration degradation is defined act or process of simplifying or breaking down a task into smaller parts, either naturally or artificially (Oxford English Dictionary, UK, 1995)
          * [decreases degradation of](decreases_degradation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
          * [increases degradation of](increases_degradation_of.md) - holds between two operational entities where the action or effect of one increases the rate of degradation of the other within a system of interest
       * [affects instantiation of](affects_instantiation_of.md) - holds between two operational entities where the action or effect of one impacts the rate of orchestration instantiation of the other
          * [decreases instantiation of](decreases_instantiation_of.md) - holds between two operational entities where the action or effect of one decreases the rate of orchestration instantiation of the other
          * [increases instantiation of](increases_instantiation_of.md) - holds between two operational entities where the action or effect of one increases the rate of orchestration instantiation of the other
       * [affects localization of](affects_localization_of.md) - holds between two operational entities where the action or effect of one changes the localization of the other within a system of interest
          * [decreases localization of](decreases_localization_of.md) - holds between two operational entities where the action or effect of one decreases the proper localization of the other within a system of interest
          * [increases localization of](increases_localization_of.md) - holds between two operational entities where the action or effect of one increases the proper localization of the other within a system of interest
       * [affects operational modification of](affects_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads changes in the operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as changing component configuration.
          * [decreases operational modification of](decreases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to decreased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as  ..
          * [increases operational modification of](increases_operational_modification_of.md) - holds between two operational entities where the action or effect of one leads to increased operational modification(s) of the other (e.g. via post-translational modifications of serviceinstances such as the addition of a component type.
       * [affects output of](affects_output_of.md) - holds between two operational entities where the action or effect of one impacts the rate of output of the other out of a serviceunit, computehost, or application
          * [decreases output of](decreases_output_of.md) - holds between two operational entities where the action or effect of one decreases the rate of output of the other out of a serviceunit, computehost, or application
          * [increases output of](increases_output_of.md) - holds between two operational entities where the action or effect of one increases the rate of output of the other out of a serviceunit, computehost, or application
       * [affects response to](affects_response_to.md) - holds between two operational entities where the action or effect of one impacts the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
          * [decreases response to](decreases_response_to.md) - holds between two operational entities where the action or effect of one decreases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
          * [increases response to](increases_response_to.md) - holds between two operational entities where the action or effect of one increases the susceptibility of a computational entity or system (e.g. a system, serviceunit, component, macrooperational machine mixin, computational or faulty process) to the other
       * [affects splicing of](affects_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity impacts the splicing of the kernel message
          * [decreases splicing of](decreases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity decreases the proper splicing of the kernel message
          * [increases splicing of](increases_splicing_of.md) - holds between a operational entity and an kernel message where the action or effect of the operational entity increases the proper splicing of the kernel message
       * [affects stability of](affects_stability_of.md) - holds between two operational entities where the action or effect of one impacts the stability of the other within a system of interest
          * [decreases stability of](decreases_stability_of.md) - holds between two operational entities where the action or effect of one decreases the stability of the other within a system of interest
          * [increases stability of](increases_stability_of.md) - holds between two operational entities where the action or effect of one increases the stability of the other within a system of interest
       * [affects supervision of](affects_supervision_of.md) - holds between two operational entities where the action or effect of one impacts the supervision of the other within a system of interest
          * [decreases supervision of](decreases_supervision_of.md) - holds between two operational entities where the action or effect of one decreases the rate of supervision of the other within a system of interest
          * [increases supervision of](increases_supervision_of.md) - holds between two operational entities where the action or effect of one increases the rate of supervision of the other within a system of interest
       * [affects transport of](affects_transport_of.md) - holds between two operational entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
          * [decreases transport of](decreases_transport_of.md) - holds between two operational entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
          * [increases transport of](increases_transport_of.md) - holds between two operational entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
       * [affects updates rate of](affects_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity impacts the rate of update of the workload entity within a system of interest
          * [decreases updates rate of](decreases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity decreases the rate of update of the workload entity within a system of interest
          * [increases updates rate of](increases_updates_rate_of.md) - holds between a operational entity and a workload entity where the action or effect of the operational entity increases the rate of update of the workload entity within a system of interest
       * [affects uptake of](affects_uptake_of.md) - holds between two operational entities where the action or effect of one impacts the rate of uptake of the other into of a serviceunit, computehost, or application
          * [decreases uptake of](decreases_uptake_of.md) - holds between two operational entities where the action or effect of one decreases the rate of uptake of the other into of a serviceunit, computehost, or application
          * [increases uptake of](increases_uptake_of.md) - holds between two operational entities where the action or effect of one increases the rate of uptake of the other into of a serviceunit, computehost, or application
       * [ameliorates](ameliorates.md) - A relationship between an entity (e.g. a serviceunittype, service variation, orchestration, or environmental exposure) and a condition (a observability or error), where the presence of the entity reduces or eliminates some or all aspects of the condition.
          * [repairs](repairs.md) - holds between a therapeutic procedure or control actor and a error or observable feature that it is used to repair
             * [approved to repair](approved_to_repair.md) - TBD
       * [disrupts](disrupts.md) - describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
       * [exacerbates](exacerbates.md) - A relationship between an entity (e.g. a orchestration, environmental exposure, or some form of service variation) and a condition (a observability or error), where the presence of the entity worsens some or all aspects of the condition.
       * [regulates, entity to entity](regulates_entity_to_entity.md)
          * [negatively regulates, entity to entity](negatively_regulates_entity_to_entity.md)
          * [positively regulates, entity to entity](positively_regulates_entity_to_entity.md)
       * [regulates, process to process](regulates_process_to_process.md)
          * [negatively regulates, process to process](negatively_regulates_process_to_process.md)
          * [positively regulates, process to process](positively_regulates_process_to_process.md)
    * [affects risk for](affects_risk_for.md) - holds between two entities where exposure to one entity alters the chance of developing the other
       * [predisposes](predisposes.md) - holds between two entities where exposure to one entity increases the chance of developing the other
       * [prevents](prevents.md) - holds between an entity whose system or use reduces the likelihood of a potential outcome. Typically used to associate a control actor, exposure, activity, or engineering intervention that can prevent the onset a error or observable feature.
    * [available in](available_in.md) - holds between a componentservice or servicetype and an deployment entity in which it is available
    * [broad match](broad_match.md) - a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree.
    * [caused by](caused_by.md) - holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other
    * [close match](close_match.md) - a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. administrative operation as a type of control entity versus administrative operation as a type of role borne by a control entity).
       * [exact match](exact_match.md) - holds between two entities that are identical to each other, with a high degree of confidence
          * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
    * [coexists with](coexists_with.md) - holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
       * [colocalizes with](colocalizes_with.md) - holds between two entities that are observed to be located in the same place.
       * [in complex with](in_complex_with.md) - holds between two componentservices or servicetypes that are part of (or code for servicetypes that are part of) in the same macrooperational complex mixin
       * [in pathway with](in_pathway_with.md) - holds between two componentservice or servicetypes that are part of in the same computational pathway
       * [in serviceunit population with](in_serviceunit_population_with.md) - holds between two componentservice or servicetypes that are available in the same serviceunit type or population
    * [componentservice association](componentservice_association.md) - Co-occurrence of a certain variantcomponentservice marker and the observability of interest in the same individuals at above-chance level
       * [componentservice associated with condition](componentservice_associated_with_condition.md) - holds between a componentservice and a error or observable feature that the componentservice or its variantcomponentservice may influence, contribute to, or correlate with
       * [condition associated with componentservice](condition_associated_with_componentservice.md) - holds between a componentservice and a error or observable feature that may be influenced, contribute to, or be correlated with the componentservice or its incorrect correct/servicetypes
    * [contraindicated for](contraindicated_for.md) - Holds between a administrative operational and a error or observability, such that a service with that error should not be repaired with the administrative operation.
    * [contributes to](contributes_to.md) - holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
       * [causes](causes.md) - holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other
          * [causes adverse event](causes_adverse_event.md) - holds between a administrative operationa and a error or observability that can be caused by the administrative operation
    * [contributor](contributor.md)
       * [author](author.md) - an instance of one (co-)creator primarily responsible for a written work
       * [editor](editor.md) - editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node).
       * [provider](provider.md) - service, person, group, organization or project that provides a piece of information (e.g. a knowledge association).
       * [publisher](publisher.md) - organization or person responsible for publishing books, periodicals, componentcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node).
    * [correlated with](correlated_with.md) - holds between any two named thing entities. For example, correlated_with holds between a error or observable feature and a measurable operation entity that is used as an indicator of the presence or state of the error or feature.
       * [coavailable with](coavailable_with.md) - holds between any two componentservices or servicetypes, in which both are generally available within a single defined experimental context.
       * [has marker](has_marker.md) - holds between a error or observable feature and a measurable operational entity that is used as an indicator of the presence or state of the error or feature.
       * [marker for](marker_for.md) - holds between a measurable operational entity and a error or observable feature, where the entity is used as an indicator of the presence or state of the error or feature.
       * [negatively correlated with](negatively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a negative manner.
       * [positively correlated with](positively_correlated_with.md) - holds between any two named thing entities "correlated with" one another in a positive manner.
    * [derives from](derives_from.md) - holds between two distinct resource entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
       * [is controller of](is_controller_of.md) - holds between two control actors in which the first one is derived from the second one as a product of supervision
    * [derives into](derives_into.md) - holds between two distinct resource entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
       * [has controller](has_controller.md) - holds between two control actors in which the second one is derived from the first one as a product of supervision
    * [develops from](develops_from.md)
    * [error has basis in](error_has_basis_in.md) - A relation that holds between a error and an entity where the state of the entity has contribution to the error.
    * [has completed](has_completed.md) - holds between an entity and a process that the entity is capable of and has completed
    * [has decreased amount](has_decreased_amount.md)
    * [has increased amount](has_increased_amount.md)
    * [has not completed](has_not_completed.md) - holds between an entity and a process that the entity is capable of, but has not completed
    * [has observability](has_observability.md) - holds between a computational entity and a observability, where a observability is construed broadly as any kind of quality of an subsystem, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * [has operational consequence](has_operational_consequence.md) - connects a sequence variant to a class describing the operation consequence. E.g.  SO:0001583
    * [has participant](has_participant.md) - holds between a process and a continuant, where the continuant is somehow involved in the process
       * [enabled by](enabled_by.md) - holds between a process and a cyber entity, where the cyber entity executes the process
       * [has input](has_input.md) - holds between a process and a continuant, where the continuant is an input into the process
       * [has output](has_output.md) - holds between a process and a continuant, where the continuant is an output of the process
    * [has sequence location](has_sequence_location.md) - holds between two service entities when the subject can be localized in sequence coordinates on the object. For example, between an daemon and a container/namespace.
    * [has servicetype](has_servicetype.md) - holds between a componentservice and a transcribed and/or translated servicetype generated from it
    * [in linkage disequilibrium with](in_linkage_disequilibrium_with.md) - holds between two sequence variants, the presence of which are correlated in a population
    * [in taxon](in_taxon.md) - connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * [interacts with](interacts_with.md) - holds between any two entities that directly or indirectly interact with each other
       * [componentservice interacts with](componentservice_interacts_with.md) - holds between two componentservices whose observable effects are dependent on each other in some way - such that their combined observable effects are the result of some interaction between the activity of their servicetypes. Example is service-unit death when two componentservices simultaneously fail, or platform startup facilitating tenant services.
       * [cyber interaction with](cyber_interaction_with.md) - holds between two entities that make cyber contact as part of some interaction
          * [operationally interacts with](operationally_interacts_with.md)
             * [decreases operational interaction](decreases_operational_interaction.md) - indicates that the source decreases the operationally interaction between the target and some other operational entity
             * [increases operational interaction](increases_operational_interaction.md) - indicates that the source increases the operationally interaction between the target and some other operational entity
       * [directly interacts with](directly_interacts_with.md) - Holds between operational entities that cyberly and directly interact with each other
    * [is sequence variant of](is_sequence_variant_of.md) - holds between a sequence variant and a workload entity
       * [is missense variant of](is_missense_variant_of.md) - holds between a componentservice  and a sequence variant, such the sequence variant results in a different instruction sequence but the serviceinstance is preserved.
       * [is nearby variant of](is_nearby_variant_of.md) - holds between a sequence variant and a componentservice sequence that the variant is close to.
       * [is non coding variant of](is_non_coding_variant_of.md) - holds between a sequence variant and a componentservice, where the variant does not affect the coding sequence
       * [is nonsense variant of](is_nonsense_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant results in a premature sequence stop.
       * [is protocol variant of](is_protocol_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant causes a disruption of the translational reading frames and/or packets.
       * [is splice site variant of](is_splice_site_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant is in the canonical splice site of one of the componentservice's daemons.
       * [is synonymous variant of](is_synonymous_variant_of.md) - holds between a sequence variant and a componentservice, such the sequence variant is in the coding sequence of the componentservice, but results in the same instruction sequence
    * [lacks part](lacks_part.md)
    * [located in](located_in.md) - holds between a resource entity and a resource entity or site within which it is located (but of which it is not considered a part)
    * [location of](location_of.md) - holds between resource entity or site and a resource entity that is located within it (but not considered a part of it)
    * [manifestation of](manifestation_of.md) - that part of a phenomenon which is directly observable or visibly available, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some error or syndrome
    * [narrow match](narrow_match.md) - a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree.
    * [occurs in](occurs_in.md) - holds between a process and a resource entity or site within which the process occurs
    * [overlaps](overlaps.md) - holds between entities that overlap in their extents (resources or processes)
       * [has part](has_part.md) - holds between wholes and their parts (resource entities or processes)
          * [has active ingredient](has_active_ingredient.md) - holds between a administrative operation and a control actor in which the latter is a part of the former, and is a computationally active component
          * [has excipient](has_excipient.md) - holds between a administrative operation and a control actors in which the latter is a part of the former, and is a computationally inactive component
          * [has notification component](has_notification_component.md) - holds between notification and one or more control actors composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)
             * [has data](has_data.md) - one or more datas which are growth factors for a system
          * [has variant part](has_variant_part.md) - holds between a workload entity and a microservice entity that is a subset of it
       * [part of](part_of.md) - holds between parts and wholes (resource entities or processes)
          * [is active ingredient of](is_active_ingredient_of.md) - holds between a control actor and a administrative operation, in which the former is a part of the latter, and is a computationally active component
          * [is excipient of](is_excipient_of.md) - holds between a control actor and a administrative operation in which the former is a part of the latter, and is a computationally inactive component
          * [notification component of](notification_component_of.md) - holds between a one or more control actors present in notification, irrespective of nutritional value (i.e. could also be a contaminant or additive)
             * [data of](data_of.md)
    * [participates in](participates_in.md) - holds between a continuant and a process, where the continuant is somehow involved in the process
       * [actively involved in](actively_involved_in.md) - holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
          * [capable of](capable_of.md) - holds between a cyber entity and process or function, where the continuant alone has the ability to carry out the process or function.
       * [enables](enables.md) - holds between a cyber entity and a process, where the cyber entity executes the process
    * [prevented by](prevented_by.md) - holds between a potential outcome of which the likelihood was reduced by the system or use of an entity.
    * [produced by](produced_by.md)
    * [produces](produces.md) - holds between a resource entity and a servicetype that is generated through the intentional actions or functioning of the resource entity
    * [related condition](related_condition.md)
    * [repaired by](repaired_by.md) - holds between a error or observable feature and a therapeutic process or control actor that is used to repair the condition
       * [approved for repairing by](approved_for_repairing_by.md) - TBD
    * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
       * [homologous to](homologous_to.md) - holds between two computational entities that have common evolutionary service
          * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically componentservices) that diverged after a speciation event.
          * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically componentservices) that diverged after a duplication event.
          * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
       * [model of](model_of.md) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
       * [orchestrationly similar to](orchestrationly_similar_to.md) - holds between one control actors and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
    * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
    * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
    * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
       * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
       * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
    * [unavailable in](unavailable_in.md) - holds between an deployment entity and componentservice or servicetype that is available there
 * [repaired by](repaired_by.md) - holds between a error or observable feature and a therapeutic process or control actor that is used to repair the condition
    * [approved for repairing by](approved_for_repairing_by.md) - TBD
 * [repairs](repairs.md) - holds between a therapeutic procedure or control actor and a error or observable feature that it is used to repair
    * [approved to repair](approved_to_repair.md) - TBD
 * [same as](same_as.md) - holds between two entities that are considered equivalent to each other
 * [similar to](similar_to.md) - holds between an entity and some other entity with similar features.
    * [homologous to](homologous_to.md) - holds between two computational entities that have common evolutionary service
       * [orthologous to](orthologous_to.md) - a homology relationship between entities (typically componentservices) that diverged after a speciation event.
       * [paralogous to](paralogous_to.md) - a homology relationship that holds between entities (typically componentservices) that diverged after a duplication event.
       * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
    * [model of](model_of.md) - holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
    * [orchestrationly similar to](orchestrationly_similar_to.md) - holds between one control actors and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
 * [subclass of](subclass_of.md) - holds between two classes where the domain class is a specialization of the range class
 * [superclass of](superclass_of.md) - holds between two classes where the domain class is a super class of the range class
 * [temporally related to](temporally_related_to.md) - holds between two entities with a temporal relationship
    * [preceded by](preceded_by.md) - holds between two processes, where the other is completed before the one begins
    * [precedes](precedes.md) - holds between two processes, where one completes before the other begins
 * [unavailable in](unavailable_in.md) - holds between an deployment entity and componentservice or servicetype that is available there
 * [xenologous to](xenologous_to.md) - a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.

### Node Properties

 * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
 * [affiliation](affiliation.md) - a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
 * [aggregate statistic](aggregate_statistic.md)
    * [has count](has_count.md) - number of things with a particular property
    * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
    * [has quotient](has_quotient.md)
    * [has total](has_total.md) - total number of things in a particular reference set
 * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in csolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
 * [chapter](chapter.md) - chapter of a book
 * [created_with](created_with.md)
 * [creation date](creation_date.md) - date on which an entity was created. This can be applied to nodes or edges
 * [dataset download url](dataset_download_url.md)
 * [distribution download url](distribution_download_url.md)
 * [download url](download_url.md)
 * [filler](filler.md) - The value in a property-value tuple
 * [format](format.md)
 * [full name](full_name.md) - a long-form human readable name for a thing
 * [has administrative operation](has_administrative_operation.md) - connects an entity to one or more administrative operations
 * [has componentservice](has_componentservice.md) - connects an entity associated with one or more componentservice
 * [has componentservice or servicetype](has_componentservice_or_servicetype.md) - connects an entity with one or more componentservice or servicetypes
    * [has componentservice](has_componentservice.md) - connects an entity associated with one or more componentservice
 * [has computational sequence](has_computational_sequence.md) - connects a service feature to its sequence of computation
 * [has control actor](has_control_actor.md) - one or more control actors within a cluster
 * [has control plane](has_control_plane.md) - one or more control actors within a cluster
 * [has count](has_count.md) - number of things with a particular property
 * [has dataset](has_dataset.md)
 * [has device](has_device.md) - connects an entity to one or more (engineering) devices
 * [has distribution](has_distribution.md)
 * [has gateway](has_gateway.md) - the system or subsystem being exposed
 * [has homogeneity](has_homogeneity.md)
 * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
 * [has procedure](has_procedure.md) - connects an entity to one or more (engineering) procedures
 * [has quotient](has_quotient.md)
 * [has route](has_route.md) - the process that results in the stressor coming into direct contact with the gateway
 * [has stressor](has_stressor.md) - the process or entity that the gateway is being exposed to
 * [has topic](has_topic.md) - Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred.
 * [has total](has_total.md) - total number of things in a particular reference set
 * [ingest date](ingest_date.md)
 * [is controller](is_controller.md) - indicates whether a control actor is a controller
 * [iso abbreviation](iso_abbreviation.md) - Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/systems/online-systems/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.
 * [issue](issue.md) - issue of a newspaper, a scientific journal or magazine for reference purpose
 * [keywords](keywords.md) - keywords tagging a publication
 * [latitude](latitude.md) - latitude
 * [license](license.md)
 * [longitude](longitude.md) - longitude
 * [node property](node_property.md) - A grouping for any property that holds between a node and a value
    * [address](address.md) - the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
    * [affiliation](affiliation.md) - a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * [aggregate statistic](aggregate_statistic.md)
       * [has count](has_count.md) - number of things with a particular property
       * [has percentage](has_percentage.md) - equivalent to has quotient multiplied by 100
       * [has quotient](has_quotient.md)
       * [has total](has_total.md) - total number of things in a particular reference set
    * [authors](authors.md) - connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in csolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * [chapter](chapter.md) - chapter of a book
    * [created_with](created_with.md)
    * [creation date](creation_date.md) - date on which an entity was created. This can be applied to nodes or edges
    * [dataset download url](dataset_download_url.md)
    * [distribution download url](distribution_download_url.md)
    * [download url](download_url.md)
    * [filler](filler.md) - The value in a property-value tuple
    * [format](format.md)
    * [full name](full_name.md) - a long-form human readable name for a thing
    * [has administrative operation](has_administrative_operation.md) - connects an entity to one or more administrative operations
    * [has componentservice or servicetype](has_componentservice_or_servicetype.md) - connects an entity with one or more componentservice or servicetypes
       * [has componentservice](has_componentservice.md) - connects an entity associated with one or more componentservice
    * [has computational sequence](has_computational_sequence.md) - connects a service feature to its sequence of computation
    * [has control actor](has_control_actor.md) - one or more control actors within a cluster
    * [has control plane](has_control_plane.md) - one or more control actors within a cluster
    * [has dataset](has_dataset.md)
    * [has device](has_device.md) - connects an entity to one or more (engineering) devices
    * [has distribution](has_distribution.md)
    * [has gateway](has_gateway.md) - the system or subsystem being exposed
    * [has homogeneity](has_homogeneity.md)
    * [has procedure](has_procedure.md) - connects an entity to one or more (engineering) procedures
    * [has route](has_route.md) - the process that results in the stressor coming into direct contact with the gateway
    * [has stressor](has_stressor.md) - the process or entity that the gateway is being exposed to
    * [has topic](has_topic.md) - Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred.
    * [ingest date](ingest_date.md)
    * [is controller](is_controller.md) - indicates whether a control actor is a controller
    * [iso abbreviation](iso_abbreviation.md) - Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/systems/online-systems/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself.
    * [issue](issue.md) - issue of a newspaper, a scientific journal or magazine for reference purpose
    * [keywords](keywords.md) - keywords tagging a publication
    * [latitude](latitude.md) - latitude
    * [license](license.md)
    * [longitude](longitude.md) - longitude
    * [pages](pages.md) - page number of source referenced for statement or publication
    * [published in](published_in.md) - CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal.
    * [retrieved on](retrieved_on.md)
    * [rights](rights.md)
    * [source logo](source_logo.md)
    * [source web page](source_web_page.md)
    * [summary](summary.md) - executive  summary of a publication
    * [sumo terms](sumo_terms.md) - sumo terms tagging a publication
    * [symbol](symbol.md) - Symbol for a particular thing
    * [synonym](synonym.md) - Alternate human-readable names for a thing
    * [systematic synonym](systematic_synonym.md) - a word with the same or very similar meanings
    * [timepoint](timepoint.md) - a point in time
    * [update date](update_date.md) - date on which an entity was migrated. This can be applied to nodes or edges
    * [version](version.md)
    * [version of](version_of.md)
    * [volume](volume.md) - volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication
    * [xref](xref.md) - Alternate CURIEs for a thing
 * [pages](pages.md) - page number of source referenced for statement or publication
 * [published in](published_in.md) - CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal.
 * [retrieved on](retrieved_on.md)
 * [rights](rights.md)
 * [source logo](source_logo.md)
 * [source web page](source_web_page.md)
 * [summary](summary.md) - executive  summary of a publication
 * [sumo terms](sumo_terms.md) - sumo terms tagging a publication
 * [symbol](symbol.md) - Symbol for a particular thing
 * [synonym](synonym.md) - Alternate human-readable names for a thing
 * [systematic synonym](systematic_synonym.md) - a word with the same or very similar meanings
 * [timepoint](timepoint.md) - a point in time
 * [update date](update_date.md) - date on which an entity was migrated. This can be applied to nodes or edges
 * [version](version.md)
 * [version of](version_of.md)
 * [volume](volume.md) - volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication
 * [xref](xref.md) - Alternate CURIEs for a thing

### Edge Properties

 * [architectural style qualifier](architectural_style_qualifier.md) - a qualifier used in a observable association to state whether the association is specific to a particular architectural style.
 * [association slot](association_slot.md) - any slot that relates an association to another entity
    * [architectural style qualifier](architectural_style_qualifier.md) - a qualifier used in a observable association to state whether the association is specific to a particular architectural style.
    * [association type](association_type.md) - connects an association to the category of association (e.g. componentservice to observability)
    * [availability site](availability_site.md) - location in which componentservice or serviceinstance availability takes place. May be serviceunit, servicegroup/replicaset, or application.
    * [catalyst qualifier](catalyst_qualifier.md) - a qualifier that connects an association between two causally connected entities (for example, two orchestration entities, or a orchestration entity in that changes location) and the servicetype, componentservice, or complex that enables or catalyzes the change.
    * [chi squared statistic](chi_squared_statistic.md) - represents the chi-squared statistic computed from observations
    * [edge label](edge_label.md)
    * [empirical modifier qualifier](empirical_modifier_qualifier.md) - Used to characterize and specify the observable abnormalities defined in the Observable abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a observable association to state how frequent the observability is observed in the subject
    * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
    * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
    * [has population context](has_population_context.md) - a computational population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.
    * [has temporal context](has_temporal_context.md) - a constraint of time placed upon the truth value of an association.
    * [interacting tasks category](interacting_tasks_category.md)
    * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
    * [object](object.md) - connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * [observable state](observable_state.md) - in experiments (e.g. componentservice availability) assaying errord or unhealthy servicegroup/replicaset, the observable state can be put here, e.g. STATE ID. For healthy servicegroup/replicasets, use XXX.
    * [onset qualifier](onset_qualifier.md) - a qualifier used in a observable association to state when the observability appears is in the subject
    * [p value](p_value.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
    * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * [provided by](provided_by.md) - connects an association to the agent (service, organization or group) that provided it
    * [publications](publications.md) - connects an association to publications supporting the association
    * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
    * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
    * [relation](relation.md) - The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * [sequence localization attribute](sequence_localization_attribute.md) - An attribute that can be applied to a workload sequence localization edge. These edges connect a workload entity such as an daemon to an entity such as a container. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line.
       * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. This is applied to a sequence localization edge.
          * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject workload entity ends on the container or other entity to which it is located on.
          * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject workload entity starts on the container or other entity to which it is located on.
       * [phase](phase.md) - TBD
       * [strand](strand.md) - TBD
       * [workload build](workload_build.md) - The version of the workload on which a feature is located.
    * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association with the variant
    * [severity qualifier](severity_qualifier.md) - a qualifier used in a observable association to state how severe the observability is in the subject
    * [stage qualifier](stage_qualifier.md) - stage during which componentservice or serviceinstance availability of takes place.
    * [subject](subject.md) - connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
 * [association type](association_type.md) - connects an association to the category of association (e.g. componentservice to observability)
 * [availability site](availability_site.md) - location in which componentservice or serviceinstance availability takes place. May be serviceunit, servicegroup/replicaset, or application.
 * [catalyst qualifier](catalyst_qualifier.md) - a qualifier that connects an association between two causally connected entities (for example, two orchestration entities, or a orchestration entity in that changes location) and the servicetype, componentservice, or complex that enables or catalyzes the change.
 * [chi squared statistic](chi_squared_statistic.md) - represents the chi-squared statistic computed from observations
 * [edge label](edge_label.md)
 * [empirical modifier qualifier](empirical_modifier_qualifier.md) - Used to characterize and specify the observable abnormalities defined in the Observable abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
 * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject workload entity ends on the container or other entity to which it is located on.
 * [frequency qualifier](frequency_qualifier.md) - a qualifier used in a observable association to state how frequent the observability is observed in the subject
 * [has confidence level](has_confidence_level.md) - connects an association to a qualitative term denoting the level of confidence
 * [has evidence](has_evidence.md) - connects an association to an instance of supporting evidence
 * [has population context](has_population_context.md) - a computational population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.
 * [has temporal context](has_temporal_context.md) - a constraint of time placed upon the truth value of an association.
 * [interacting tasks category](interacting_tasks_category.md)
 * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. This is applied to a sequence localization edge.
    * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject workload entity ends on the container or other entity to which it is located on.
    * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject workload entity starts on the container or other entity to which it is located on.
 * [negated](negated.md) - if set to true, then the association is negated i.e. is not true
 * [object](object.md) - connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
 * [observable state](observable_state.md) - in experiments (e.g. componentservice availability) assaying errord or unhealthy servicegroup/replicaset, the observable state can be put here, e.g. STATE ID. For healthy servicegroup/replicasets, use XXX.
 * [onset qualifier](onset_qualifier.md) - a qualifier used in a observable association to state when the observability appears is in the subject
 * [p value](p_value.md) - A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
 * [phase](phase.md) - TBD
 * [predicate](predicate.md) - A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
 * [provided by](provided_by.md) - connects an association to the agent (service, organization or group) that provided it
 * [publications](publications.md) - connects an association to publications supporting the association
 * [qualifiers](qualifiers.md) - connects an association to qualifiers that modify or qualify the meaning of that association
 * [quantifier qualifier](quantifier_qualifier.md) - A measurable quantity for the object of the association
 * [relation](relation.md) - The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
 * [sequence localization attribute](sequence_localization_attribute.md) - An attribute that can be applied to a workload sequence localization edge. These edges connect a workload entity such as an daemon to an entity such as a container. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line.
    * [interbase coordinate](interbase_coordinate.md) - A position in interbase coordinates. This is applied to a sequence localization edge.
       * [end interbase coordinate](end_interbase_coordinate.md) - The position at which the subject workload entity ends on the container or other entity to which it is located on.
       * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject workload entity starts on the container or other entity to which it is located on.
    * [phase](phase.md) - TBD
    * [strand](strand.md) - TBD
    * [workload build](workload_build.md) - The version of the workload on which a feature is located.
 * [sequence variant qualifier](sequence_variant_qualifier.md) - a qualifier used in an association with the variant
 * [severity qualifier](severity_qualifier.md) - a qualifier used in a observable association to state how severe the observability is in the subject
 * [stage qualifier](stage_qualifier.md) - stage during which componentservice or serviceinstance availability of takes place.
 * [start interbase coordinate](start_interbase_coordinate.md) - The position at which the subject workload entity starts on the container or other entity to which it is located on.
 * [strand](strand.md) - TBD
 * [subject](subject.md) - connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
 * [workload build](workload_build.md) - The version of the workload on which a feature is located.

### Slot Mixins

 * [computational role mixin](computational_role_mixin.md) - A role played by the operational entity or part thereof within a computational context.
 * [control role mixin](control_role_mixin.md) - A role played by the operational entity or part thereof within a control context.
 * [negatively regulated by](negatively_regulated_by.md)
 * [negatively regulates](negatively_regulates.md)
 * [positively regulated by](positively_regulated_by.md)
 * [positively regulates](positively_regulates.md)
 * [regulated by](regulated_by.md)
 * [regulates](regulates.md)

### Other Slots

 * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.
 * [description](description.md) - a human-readable description of an entity
 * [has attribute](has_attribute.md) - connects any entity to an attribute
 * [has attribute type](has_attribute_type.md) - connects an attribute to a class that describes it
 * [has numeric value](has_numeric_value.md) - connects a quantity value to a number
 * [has qualitative value](has_qualitative_value.md) - connects an attribute to a value
 * [has quantitative value](has_quantitative_value.md) - connects an attribute to a value
 * [has taxonomic rank](has_taxonomic_rank.md)
 * [has unit](has_unit.md) - connects a quantity value to a unit
 * [id](id.md) - A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
 * [iri](iri.md) - An IRI for an entity. This is determined by the id using expansion rules.
 * [name](name.md) - A human-readable name for an attribute or entity.
 * [source](source.md) - a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
 * [type](type.md)
    * [category](category.md) - Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the csolink entity type class.

## Types


### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [CategoryType](types/CategoryType.md)  ([Uriorcurie](types/Uriorcurie.md))  - A primitive type in which the value denotes a class within the csolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the csolink class, for example csolink:Service. For an RDF representation, the value should be a URI such as https://w3id.org/csolink/vocab/Service
 * [ComputationalSequence](types/ComputationalSequence.md)  ([String](types/String.md)) 
 * [ControlPlaneValue](types/ControlPlaneValue.md)  (**str**)  - A control plane
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Frequency](types/Frequency.md)  ([String](types/String.md)) 
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [IriType](types/IriType.md)  ([Uriorcurie](types/Uriorcurie.md))  - An IRI
 * [LabelType](types/LabelType.md)  ([String](types/String.md))  - A string that provides a human-readable name for an entity
 * [NarrativeText](types/NarrativeText.md)  ([String](types/String.md))  - A string that provides a human-readable description of something
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [PercentageFrequencyValue](types/PercentageFrequencyValue.md)  ([Double](types/Double.md)) 
 * [PredicateType](types/PredicateType.md)  ([Uriorcurie](types/Uriorcurie.md))  - A CURIE from the csolink related_to hierarchy. For example, csolink:related_to, csolink:causes, csolink:repairs.
 * [Quotient](types/Quotient.md)  ([Double](types/Double.md)) 
 * [String](types/String.md)  (**str**)  - A character string
 * [SymbolType](types/SymbolType.md)  ([String](types/String.md)) 
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [TimeType](types/TimeType.md)  ([Time](types/Time.md)) 
 * [Unit](types/Unit.md)  ([String](types/String.md)) 
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
