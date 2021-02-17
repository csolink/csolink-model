---
parent: Associations
title: csolink:MacrooperationalMachineMixinToComputationalProcessAssociation
grand_parent: Classes
layout: default
---

# Class: MacrooperationalMachineMixinToComputationalProcessAssociation


A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a computational process or pathway (as represented in the GO computational process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it

URI: [csolink:MacrooperationalMachineMixinToComputationalProcessAssociation](https://w3id.org/csolink/vocab/MacrooperationalMachineMixinToComputationalProcessAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[ComputationalProcess]%3Cobject%201..1-%20[MacrooperationalMachineMixinToComputationalProcessAssociation%7Cpredicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[FunctionalAssociation]%5E-[MacrooperationalMachineMixinToComputationalProcessAssociation],[MacrooperationalMachineMixin],[FunctionalAssociation],[ComputationalProcess],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [FunctionalAssociation](FunctionalAssociation.md) - An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes) and either a operational activity, a computational process or a component location in which a function is executed.

## Referenced by class


## Attributes


### Own

 * [macrooperational machine mixin to computational process association➞object](macrooperational_machine_mixin_to_computational_process_association_object.md)  <sub>REQ</sub>
    * range: [ComputationalProcess](ComputationalProcess.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a componentservice-to-observability association, the componentservice is subject and observability is object.
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

### Inherited from functional association:

 * [functional association➞subject](functional_association_subject.md)  <sub>REQ</sub>
    * Description: componentservice, servicetype or macrooperational complex that has the function associated with the GO term
    * range: [MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)
 * [functional association➞object](functional_association_object.md)  <sub>REQ</sub>
    * Description: class describing the activity, process or localization of the servicetype
    * range: [ComponentserviceOntologyClass](ComponentserviceOntologyClass.md)

### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [macrooperational machine mixin to computational process association➞object](macrooperational_machine_mixin_to_computational_process_association_object.md)  <sub>REQ</sub>
    * range: [ComputationalProcess](ComputationalProcess.md)