---
parent: Class Mixins
title: csolink:FrequencyQuantifier
grand_parent: Classes
layout: default
---

# Class: FrequencyQuantifier




URI: [csolink:FrequencyQuantifier](https://w3id.org/csolink/vocab/FrequencyQuantifier)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipQuantifier],[VariantToPopulationAssociation]uses%20-.-%3E[FrequencyQuantifier%7Chas_count:integer%20%3F;has_total:integer%20%3F;has_quotient:double%20%3F;has_percentage:double%20%3F],[RelationshipQuantifier]%5E-[FrequencyQuantifier],[VariantToPopulationAssociation])

---


## Parents

 *  is_a: [RelationshipQuantifier](RelationshipQuantifier.md)

## Mixin for

 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [has count](has_count.md)  <sub>OPT</sub>
    * Description: number of things with a particular property
    * range: [Integer](types/Integer.md)
 * [has percentage](has_percentage.md)  <sub>OPT</sub>
    * Description: equivalent to has quotient multiplied by 100
    * range: [Double](types/Double.md)
 * [has quotient](has_quotient.md)  <sub>OPT</sub>
    * range: [Double](types/Double.md)
 * [has total](has_total.md)  <sub>OPT</sub>
    * Description: total number of things in a particular reference set
    * range: [Integer](types/Integer.md)
