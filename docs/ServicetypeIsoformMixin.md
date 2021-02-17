---
parent: Class Mixins
title: csolink:ServicetypeIsoformMixin
grand_parent: Classes
layout: default
---

# Class: ServicetypeIsoformMixin


This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the servicetype is intended to represent a specific isoform rather than a canonical or reference or generic servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.

URI: [csolink:ServicetypeIsoformMixin](https://w3id.org/csolink/vocab/ServicetypeIsoformMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ServicetypeMixin],[ServiceinstanceIsoform]uses%20-.-%3E[ServicetypeIsoformMixin%7Csynonym(i):label_type%20%2A;xref(i):iri_type%20%2A;name(i):symbol_type%20%3F],[KernelServicetypeIsoform]uses%20-.-%3E[ServicetypeIsoformMixin],[ServicetypeMixin]%5E-[ServicetypeIsoformMixin],[ServiceinstanceIsoform],[KernelServicetypeIsoform])

---


## Parents

 *  is_a: [ServicetypeMixin](ServicetypeMixin.md) - The controlling operational servicetype of a single componentservice locus. ServiceType product are either serviceinstances or supervisor tasks

## Mixin for

 * [KernelServicetypeIsoform](KernelServicetypeIsoform.md) (mixin)  - Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
 * [ServiceinstanceIsoform](ServiceinstanceIsoform.md) (mixin)  - Represents a serviceinstance that is a specific isoform of the canonical or reference serviceinstance.

## Referenced by class


## Attributes


### Inherited from macrooperational machine mixin:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
