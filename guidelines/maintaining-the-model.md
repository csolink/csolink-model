---
title: "Maintaining the Csolink Model"
parent: "Csolink Model Guidelines"
layout: default
nav_order: 5
---

# Maintaining the Csolink Model

The Csolink Model is under constant development with new classes and slots being added on a monthly basis. The main driver for the model is the NCATS Biomedical Data Translator.

This rapid development of the model may cause tools that directly depend on the model to break. To avoid such a scenario any tool that uses Csolink Model YAML (or it artifacts) must pin to a particular release. A full list of releases can be found on [GitHub](https://github.com/csolink/csolink-model/releases)


This section will address the strategies for maintaining the Csolink Model.


## Managing versions

We use the [Semantic Versioning guidelines](https://semver.org/) for managing our releases.

> Given a version number MAJOR.MINOR.PATCH, increment the:
> - MAJOR version when you make incompatible API changes,
> - MINOR version when you add functionality in a backwards compatible manner, and
> - PATCH version when you make backwards compatible bug fixes.


Small changes to the model can be provided periodically as a new patch release. 

Any structural changes to the model should be followed by a new minor release, as long as the changes are backwards compatible.

Any modification that leads to breaking changes must be followed by a new major release.


## Deprecating classes and slots

LinkML provides slots that can be used to signify a class (or slot) as being deprecated.

Example:
```yaml
  edge label:
    deprecated: >-
      This slot is deprecated in favor of 'predicate' slot.
    deprecated_element_has_exact_replacement: predicate
    is_a: association slot
    domain: association
    range: predicate type
    required: true
```

In the above example we use the `deprecated` and `deprecated_element_has_exact_replacement` to signify the association slot `edge label` as being deprecated.
- Using the `deprecated` slot one can provide a human readable description of why the slot was deprecated
- Using the `deprecated_element_has_exact_replacement` slot one can define what is the ideal replacement for this slot (if any)

It's recommended that deprecated classes and slots remain in the model until the next major release.


## Artifacts

LinkML consumes the Csolink Model YAML and generates several artifacts.

This step is automated as part of [GitHub Actions](https://github.com/csolink/csolink-model/actions). 

That means no pull request to the Csolink Model repo should include updates to the artifacts themselves. In 99% of the cases any changes in a PR ought to be confined to `csolink-model.yaml`.


## Documentation

LinkML consumes the Csolink Model YAML and also generates Markdown for all the classes and slots defined in the model.

This step is automated as part of [GitHub Actions](https://github.com/csolink/csolink-model/actions) where changes in Markdown content are pushed to the `gh-pages` branch. 

The [Csolink Model Documentation](https://noelmcloughlin.github.io/csolink-model/) site is driven from the `gh-pages` branch.

That means no pull request to the Csolink Model repo should include generated Markdown. It is advised to ensure that [GitHub Actions](https://github.com/csolink/csolink-model/actions) remain disabled in the fork from which pull requests are made back to the main Csolink repository.
