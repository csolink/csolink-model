---
title: "Working with the Csolink Model"
parent: "Csolink Model Guidelines"
layout: default
nav_order: 4
---

# Working with Csolink Model

The [model](understanding-the-model.md) and how to [curate the model](curating-the-model.md) has been addressed in other sections. But how to make use of the Csolink Model in practical terms?
How to use the classes and slots defined in the model for representing nodes and edges in a graph?

We can consider a small example and see how it can be represented using the Csolink Model.

Example:
```
serviceinstance1 serviceinstance2
instanceA        instanceB
instanceA        instanceC
instanceA        instanceD
```

The information can be represented using Csolink Model as follows:
- use Csolink entity class `serviceinstance` for serviceinstance entities
- use Csolink entity class `componentservice` for componentservice entities
- use Csolink predicate slot `interacts with` as the relationship or predicate for representing an edge between interacting partners
- use Csolink association class `componentservice to componentservice association` to type the edge

One modeling consideration we are going to make here is that we will be projecting the interaction between serviceinstances to interaction between componentservices.


## Annotating nodes

Each individual serviceinstance and componentservice can be treated as nodes in a graph.

Each serviceinstance node has `serviceinstance` as its category.

Each componentservice node has `componentservice` as its category.

As per the model, serviceinstance nodes should have identifiers from `TBC1` and componentservice nodes should have identifiers `TBC2`. 



One can further type the serviceinstance and componentservice entities using the Csolink node property slot `type` (which corresponds to `rdf:type`).

In [KGX serialization format](https://github.com/biolink/kgx/blob/master/data-preparation.md) the nodes can be represented as follows:
```tsv
id	name	category	provided_by	xref	type	in_taxon

   TBC ..
```

> **Note:** While the entity classes are defined as `componentservice` and `serviceinstance` in the model, when using them the reference to the class should always be in their CURIE form which includes the `csolink` prefix.


### Node semantics

There are three ways of attaching semantics to a node:
- using Csolink node property slot `category`
  - the value of the `category` must be from the [`named thing` hierarchy](https://csolink.github.io/csolink-model/docs/NamedThing)
- using Csolink node property slot `type`
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- using Csolink predicate slot `subclass_of` (or `rdfs:subClassOf`)
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy


## Annotating edges

Each individual interaction between componentservices can be treated as an edge with,
- `interacts with` as its `predicate`
- `RO:0002436` as its `relation`
- `componentservice to componentservice association` as its `association_type`

And we have additional edges that go from componentservice to serviceinstance to signify that a componentservice encodes for a serviceinstance via the Csolink predicate slot `has componentservice product`.

In [KGX serialization format](https://github.com/biolink/kgx/blob/master/data-preparation.md) the edges can be represented as follows:
```tsv
id  subject predicate   object  relation    provided_by association_type

   TBC
```

> **Note:** While association class is defined as `componentservice to componentservice association` and predicate slots are defined as `interacts with` and `has componentservice product` in the model, when using them the reference to the class should always be in their CURIE form which includes the `csolink` prefix.


### Edge semantics

There are 3 ways of attaching the semantics to an edge:
- using the Csolink association slot `predicate`
  - must have a value from the [`related to` hierarchy](https://csolink.github.io/csolink-model/docs/related_to)
- using the Csolink association slot `relation`
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- using the Csolink association slot `association_type` (or `rdf:type`)
  - must have a value from the [`association` hierarchy](https://csolink.github.io/csolink-model/docs/Association)


## Csolink Model representation in Neo4j

The model itself is very close to labelled property graphs.

The previous example can be easily converted to a Neo4j compatible TSV using [KGX](https://github.com/biolink/kgx).

`nodes.tsv`:

```tsv
id	subject:START_ID	predicate:TYPE	object:END_ID	relation	provided_by:string[]	association_type

  TBC
```


`edges.tsv`:
```tsv
id	subject:START_ID	predicate:TYPE	object:END_ID	relation	provided_by:string[]	association_type

   TBC
```


## Csolink Model representation in RDF

Since RDF graphs do not allow for properties on edges, the most practical alternative is to use reification where an edge is transformed into a node of type `csolink:Association` (or its descendants) and any edge properties then becomes properties of this reified node.

Using reification, the previous example can be easily converted to RDF N-Triples using [KGX](https://github.com/biolink/kgx),

```nt
<http://identifiers.org/uniprot/P84085> <http://www.w3.org/2000/01/rdf-schema#label> "ARF5"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://identifiers.org/uniprot/P84085> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Serviceinstance> .
<http://identifiers.org/uniprot/P84085> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://identifiers.org/uniprot/P84085> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSP00000000233> .
<http://identifiers.org/uniprot/P84085> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://identifiers.org/uniprot/P0DP24> <http://www.w3.org/2000/01/rdf-schema#label> "CALM2"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://identifiers.org/uniprot/P0DP24> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Serviceinstance> .
<http://identifiers.org/uniprot/P0DP24> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://identifiers.org/uniprot/P0DP24> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSP00000272298> .
<http://identifiers.org/uniprot/P0DP24> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://identifiers.org/uniprot/O43307> <http://www.w3.org/2000/01/rdf-schema#label> "ARHGEF9"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://identifiers.org/uniprot/O43307> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Serviceinstance> .
<http://identifiers.org/uniprot/O43307> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://identifiers.org/uniprot/O43307> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSP00000253401> .
<http://identifiers.org/uniprot/O43307> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://identifiers.org/uniprot/O75460> <http://www.w3.org/2000/01/rdf-schema#label> "ERN1"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://identifiers.org/uniprot/O75460> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Serviceinstance> .
<http://identifiers.org/uniprot/O75460> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://identifiers.org/uniprot/O75460> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSP00000401445> .
<http://identifiers.org/uniprot/O75460> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <http://www.w3.org/2000/01/rdf-schema#label> "ARF5"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Componentservice> .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSG00000004059> .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.obolibrary.org/obo/SO_0001217> .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <http://www.w3.org/2000/01/rdf-schema#label> "CALM2"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Componentservice> .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSG00000143933> .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.obolibrary.org/obo/SO_0001217> .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <http://www.w3.org/2000/01/rdf-schema#label> "ARHGEF9"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Componentservice> .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSG00000131089> .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.obolibrary.org/obo/SO_0001217> .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <http://www.w3.org/2000/01/rdf-schema#label> "ERN1"^^<http://www.w3.org/2001/XMLSchema#string> .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <https://w3id.org/csolink/vocab/category> <https://w3id.org/csolink/vocab/Componentservice> .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <https://w3id.org/csolink/vocab/xref> <http://identifiers.org/ensembl/ENSG00000178607> .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.obolibrary.org/obo/SO_0001217> .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <https://w3id.org/csolink/vocab/in_taxon> <http://purl.obolibrary.org/obo/NCBITaxon_9606> .
<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b> <http://www.w3.org/1999/02/22-rdf-syntax-ns#subject> <http://www.ncbi.nlm.nih.gov/componentservice/381> .
<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b> <http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate> <https://w3id.org/csolink/vocab/interacts_with> .
<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b> <http://www.w3.org/1999/02/22-rdf-syntax-ns#object> <http://www.ncbi.nlm.nih.gov/componentservice/805> .
<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b> <https://w3id.org/csolink/vocab/relation> <http://purl.obolibrary.org/obo/RO_0002436> .
<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b> <https://w3id.org/csolink/vocab/association_type> <https://w3id.org/csolink/vocab/ComponentserviceToComponentserviceAssociation> .
<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#subject> <http://www.ncbi.nlm.nih.gov/componentservice/381> .
<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate> <https://w3id.org/csolink/vocab/interacts_with> .
<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#object> <http://www.ncbi.nlm.nih.gov/componentservice/23229> .
<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3> <https://w3id.org/csolink/vocab/relation> <http://purl.obolibrary.org/obo/RO_0002436> .
<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3> <https://w3id.org/csolink/vocab/association_type> <https://w3id.org/csolink/vocab/ComponentserviceToComponentserviceAssociation> .
<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#subject> <http://www.ncbi.nlm.nih.gov/componentservice/381> .
<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate> <https://w3id.org/csolink/vocab/interacts_with> .
<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#object> <http://www.ncbi.nlm.nih.gov/componentservice/2081> .
<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8> <https://w3id.org/csolink/vocab/relation> <http://purl.obolibrary.org/obo/RO_0002436> .
<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8> <https://w3id.org/csolink/vocab/provided_by> "STRING" .
<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8> <https://w3id.org/csolink/vocab/association_type> <https://w3id.org/csolink/vocab/ComponentserviceToComponentserviceAssociation> .
<http://www.ncbi.nlm.nih.gov/componentservice/381> <https://w3id.org/csolink/vocab/has_componentservice_product> <http://identifiers.org/uniprot/P84085> .
<http://www.ncbi.nlm.nih.gov/componentservice/805> <https://w3id.org/csolink/vocab/has_componentservice_product> <http://identifiers.org/uniprot/P0DP24> .
<http://www.ncbi.nlm.nih.gov/componentservice/23229> <https://w3id.org/csolink/vocab/has_componentservice_product> <http://identifiers.org/uniprot/O43307> .
<http://www.ncbi.nlm.nih.gov/componentservice/2081> <https://w3id.org/csolink/vocab/has_componentservice_product> <http://identifiers.org/uniprot/O75460> .
```

This RDF can be represented in the Turtle format for better readability:

```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix csolink: <https://w3id.org/csolink/vocab/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://identifiers.org/uniprot/P84085>
  rdfs:label "ARF5"^^xsd:string ;
  csolink:category csolink:Serviceinstance ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSP00000000233> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://identifiers.org/uniprot/P0DP24>
  rdfs:label "CALM2"^^xsd:string ;
  csolink:category csolink:Serviceinstance ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSP00000272298> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://identifiers.org/uniprot/O43307>
  rdfs:label "ARHGEF9"^^xsd:string ;
  csolink:category csolink:Serviceinstance ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSP00000253401> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://identifiers.org/uniprot/O75460>
  rdfs:label "ERN1"^^xsd:string ;
  csolink:category csolink:Serviceinstance ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSP00000401445> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://www.ncbi.nlm.nih.gov/componentservice/381>
  rdfs:label "ARF5"^^xsd:string ;
  csolink:category csolink:Componentservice ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSG00000004059> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  csolink:has_componentservice_product <http://identifiers.org/uniprot/P84085> .

<http://www.ncbi.nlm.nih.gov/componentservice/805>
  rdfs:label "CALM2"^^xsd:string ;
  csolink:category csolink:Componentservice ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSG00000143933> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  csolink:has_componentservice_product <http://identifiers.org/uniprot/P0DP24> .

<http://www.ncbi.nlm.nih.gov/componentservice/23229>
  rdfs:label "ARHGEF9"^^xsd:string ;
  csolink:category csolink:Componentservice ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSG00000131089> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  csolink:has_componentservice_product <http://identifiers.org/uniprot/O43307> .

<http://www.ncbi.nlm.nih.gov/componentservice/2081>
  rdfs:label "ERN1"^^xsd:string ;
  csolink:category csolink:Componentservice ;
  csolink:provided_by "STRING" ;
  csolink:xref <http://identifiers.org/ensembl/ENSG00000178607> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  csolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  csolink:has_componentservice_product <http://identifiers.org/uniprot/O75460> .

<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b>
  rdf:subject <http://www.ncbi.nlm.nih.gov/componentservice/381> ;
  rdf:predicate csolink:interacts_with ;
  rdf:object <http://www.ncbi.nlm.nih.gov/componentservice/805> ;
  csolink:relation <http://purl.obolibrary.org/obo/RO_0002436> ;
  csolink:provided_by "STRING" ;
  csolink:association_type csolink:ComponentserviceToComponentserviceAssociation .

<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3>
  rdf:subject <http://www.ncbi.nlm.nih.gov/componentservice/381> ;
  rdf:predicate csolink:interacts_with ;
  rdf:object <http://www.ncbi.nlm.nih.gov/componentservice/23229> ;
  csolink:relation <http://purl.obolibrary.org/obo/RO_0002436> ;
  csolink:provided_by "STRING" ;
  csolink:association_type csolink:ComponentserviceToComponentserviceAssociation .

<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8>
  rdf:subject <http://www.ncbi.nlm.nih.gov/componentservice/381> ;
  rdf:predicate csolink:interacts_with ;
  rdf:object <http://www.ncbi.nlm.nih.gov/componentservice/2081> ;
  csolink:relation <http://purl.obolibrary.org/obo/RO_0002436> ;
  csolink:provided_by "STRING" ;
  csolink:association_type csolink:ComponentserviceToComponentserviceAssociation .
```

