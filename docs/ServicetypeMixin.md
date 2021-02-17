---
parent: Class Mixins
title: csolink:ServicetypeMixin
grand_parent: Classes
layout: default
---

# Class: ServicetypeMixin


The controlling operational servicetype of a single componentservice locus. ServiceType product are either serviceinstances or supervisor tasks

URI: [csolink:ServicetypeMixin](https://w3id.org/csolink/vocab/ServicetypeMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ComponentserviceToServicetypeRelationship]++-%20object%201..1%3E[ServicetypeMixin%7Csynonym:label_type%20%2A;xref:iri_type%20%2A;name(i):symbol_type%20%3F],[Serviceinstance]uses%20-.-%3E[ServicetypeMixin],[KernelServicetype]uses%20-.-%3E[ServicetypeMixin],[ServicetypeMixin]%5E-[ServicetypeIsoformMixin],[ComponentserviceOrServicetype]%5E-[ServicetypeMixin],[ServicetypeIsoformMixin],[Serviceinstance],[KernelServicetype],[ComponentserviceToServicetypeRelationship],[ComponentserviceOrServicetype],[Componentservice])

---


## Parents

 *  is_a: [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md) - a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another

## Children

 * [ServicetypeIsoformMixin](ServicetypeIsoformMixin.md) - This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the servicetype is intended to represent a specific isoform rather than a canonical or reference or generic servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

## Mixin for

 * [KernelServicetype](KernelServicetype.md) (mixin) 
 * [Serviceinstance](Serviceinstance.md) (mixin)  - A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message

## Referenced by class

 *  **[ComponentserviceToServicetypeRelationship](ComponentserviceToServicetypeRelationship.md)** *[componentservice to servicetype relationship➞object](componentservice_to_servicetype_relationship_object.md)*  <sub>REQ</sub>  **[ServicetypeMixin](ServicetypeMixin.md)**
 *  **[Componentservice](Componentservice.md)** *[has servicetype](has_servicetype.md)*  <sub>0..*</sub>  **[ServicetypeMixin](ServicetypeMixin.md)**

## Attributes


### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
