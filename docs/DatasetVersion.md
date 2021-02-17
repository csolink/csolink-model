---
parent: Entities
title: csolink:DatasetVersion
grand_parent: Classes
layout: default
---

# Class: DatasetVersion




URI: [csolink:DatasetVersion](https://w3id.org/csolink/vocab/DatasetVersion)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DistributionLevel],[DatasetDistribution]%3Chas%20distribution%200..1-%20[DatasetVersion%7Cingest_date:string%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Dataset]%3Chas%20dataset%200..1-%20[DatasetVersion],[DatasetVersion]%5E-[DistributionLevel],[DatasetVersion]%5E-[DatasetSummary],[Dataset]%5E-[DatasetVersion],[DatasetSummary],[DatasetDistribution],[Dataset],[Attribute],[Agent])

---


## Parents

 *  is_a: [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.

## Children

 * [DatasetSummary](DatasetSummary.md)
 * [DistributionLevel](DistributionLevel.md)

## Referenced by class


## Attributes


### Own

 * [has dataset](has_dataset.md)  <sub>OPT</sub>
    * range: [Dataset](Dataset.md)
 * [has distribution](has_distribution.md)  <sub>OPT</sub>
    * range: [DatasetDistribution](DatasetDistribution.md)
 * [ingest date](ingest_date.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

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

### Inherited from information content entity:

 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which an entity was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)

### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [has dataset](has_dataset.md)  <sub>OPT</sub>
    * range: [Dataset](Dataset.md)
 * [has distribution](has_distribution.md)  <sub>OPT</sub>
    * range: [DatasetDistribution](DatasetDistribution.md)
 * [ingest date](ingest_date.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
