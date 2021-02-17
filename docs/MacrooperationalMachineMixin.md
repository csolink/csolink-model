---
parent: Class Mixins
title: csolink:MacrooperationalMachineMixin
grand_parent: Classes
layout: default
---

# Class: MacrooperationalMachineMixin


A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a component. They either carry out individual computational activities, or they encode tasks which do this.

URI: [csolink:MacrooperationalMachineMixin](https://w3id.org/csolink/vocab/MacrooperationalMachineMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrchestrationToOrchestrationDerivationAssociation],[OperationalActivity],[OrchestrationToOrchestrationDerivationAssociation]++-%20catalyst%20qualifier(i)%200..%2A%3E[MacrooperationalMachineMixin%7Cname:symbol_type%20%3F],[FunctionalAssociation]++-%20subject%201..1%3E[MacrooperationalMachineMixin],[OperationalActivity]++-%20enabled%20by%200..%2A%3E[MacrooperationalMachineMixin],[OrchestrationToOrchestrationDerivationAssociation]++-%20catalyst%20qualifier%200..%2A%3E[MacrooperationalMachineMixin],[MacrooperationalMachineMixin]%5E-[MacrooperationalComplexMixin],[MacrooperationalMachineMixin]%5E-[ComponentserviceOrServicetype],[MacrooperationalComplexMixin],[FunctionalAssociation],[ComponentserviceOrServicetype],[Association])

---


## Children

 * [ComponentserviceOrServicetype](ComponentserviceOrServicetype.md) - a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for another
 * [MacrooperationalComplexMixin](MacrooperationalComplexMixin.md)

## Referenced by class

 *  **[Association](Association.md)** *[catalyst qualifier](catalyst_qualifier.md)*  <sub>0..*</sub>  **[MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)**
 *  **[FunctionalAssociation](FunctionalAssociation.md)** *[functional association➞subject](functional_association_subject.md)*  <sub>REQ</sub>  **[MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)**
 *  **[OperationalActivity](OperationalActivity.md)** *[operational activity➞enabled by](operational_activity_enabled_by.md)*  <sub>0..*</sub>  **[MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)**
 *  **[OrchestrationToOrchestrationDerivationAssociation](OrchestrationToOrchestrationDerivationAssociation.md)** *[orchestration to orchestration derivation association➞catalyst qualifier](orchestration_to_orchestration_derivation_association_catalyst_qualifier.md)*  <sub>0..*</sub>  **[MacrooperationalMachineMixin](MacrooperationalMachineMixin.md)**

## Attributes


### Own

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [macrooperational machine mixin➞name](macrooperational_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: componentservices are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
