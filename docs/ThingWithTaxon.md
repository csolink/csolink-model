---
parent: Class Mixins
title: csolink:ThingWithTaxon
grand_parent: Classes
layout: default
---

# Class: ThingWithTaxon


A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems; componentservices, their servicetypes and other operation entities; computer parts; computational processes

URI: [csolink:ThingWithTaxon](https://w3id.org/csolink/vocab/ThingWithTaxon)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SystemTaxon]%3Cin%20taxon%200..%2A-%20[ThingWithTaxon],[PopulationOfIndividualSystems]uses%20-.-%3E[ThingWithTaxon],[OperationalEntity]uses%20-.-%3E[ThingWithTaxon],[LifecycleStage]uses%20-.-%3E[ThingWithTaxon],[IndividualSystem]uses%20-.-%3E[ThingWithTaxon],[ErrorOrObservableFeature]uses%20-.-%3E[ThingWithTaxon],[DeploymentEntity]uses%20-.-%3E[ThingWithTaxon],[SystemTaxon],[PopulationOfIndividualSystems],[OperationalEntity],[LifecycleStage],[IndividualSystem],[ErrorOrObservableFeature],[DeploymentEntity])

---


## Mixin for

 * [DeploymentEntity](DeploymentEntity.md) (mixin)  - A process location, serviceunit type or gross deployment part
 * [ErrorOrObservableFeature](ErrorOrObservableFeature.md) (mixin)  - Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as distinct, others conflate.
 * [IndividualSystem](IndividualSystem.md) (mixin)  - An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576
 * [LifecycleStage](LifecycleStage.md) (mixin)  - A stage of development or growth of a system.
 * [OperationalEntity](OperationalEntity.md) (mixin)  - A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
 * [PopulationOfIndividualSystems](PopulationOfIndividualSystems.md) (mixin)  - A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.

## Referenced by class


## Attributes


### Own

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
    * range: [SystemTaxon](SystemTaxon.md)
    * in subsets: (translator_minimal)
