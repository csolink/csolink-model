# Auto generated from csolink-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-17 00:01
# Schema: Csolink-Model
#
# id: https://w3id.org/csolink/csolink-model
# description: Entity and association taxonomy and datamodel for computer services data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACMBOOKS = CurieNamespace('ACMBOOKS', 'https://dl.acm.org/action/doSearch?SeriesKey=acmbooks&AllField=')
ACMJOURNALS = CurieNamespace('ACMJOURNALS', 'https://dl.acm.org/action/doSearch?ConceptID=118230&AllField=')
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
CCDM = CurieNamespace('CCDM', 'http://cookingbigdata.com/linkeddata/ccdm#')
CCINSTANCES = CurieNamespace('CCINSTANCES', 'http://cookingbigdata.com/linkeddata/ccinstances#')
CCPRICING = CurieNamespace('CCPRICING', 'http://cookingbigdata.com/linkeddata/ccpricing#')
CCREGIONS = CurieNamespace('CCREGIONS', 'http://cookingbigdata.com/linkeddata/ccregions#')
CCSLA = CurieNamespace('CCSLA', 'http://cookingbigdata.com/linkeddata/ccsla#')
CNCF = CurieNamespace('CNCF', 'https://landscape.cncf.io/selected=')
CNTT = CurieNamespace('CNTT', 'https://cntt-n.github.io/CNTT/doc/common/glossary.html#1.1')
COAR_ACCESS = CurieNamespace('COAR_ACCESS', 'http://vocabularies.coar-repositories.org/documentation/access_rights/')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://vocabularies.coar-repositories.org/documentation/resource_types/')
COAR_VERSION = CurieNamespace('COAR_VERSION', 'http://vocabularies.coar-repositories.org/documentation/version_types/')
CORR = CurieNamespace('CORR', 'https://arxiv.org/corr')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
CVE = CurieNamespace('CVE', 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=')
DCMI = CurieNamespace('DCMI', 'http://purl.org/dc/elements/1.1/')
DID = CurieNamespace('DID', 'https://www.w3.org/TR/did-core/#')
DMCC = CurieNamespace('DMCC', 'http://cookingbigdata.com/linkeddata/dmcc-schema/documentation/#')
DNB = CurieNamespace('DNB', 'https://d-nb.info/gnd/')
DPN = CurieNamespace('DPN', 'http://purl.org/dpn#')
DPS = CurieNamespace('DPS', 'http://purl.org/dpn/services#')
DOCKERHUB = CurieNamespace('DockerHub', 'https://hub.docker.com/')
ECO = CurieNamespace('ECO', 'https://evidenceontology.org/term/')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/')
ETSINFV = CurieNamespace('ETSINFV', 'https://www.etsi.org/deliver/etsi_gr/NFV/001_099/003/01.05.01_60/gr_NFV003v010501p.pdf')
ETSINFV_MANO = CurieNamespace('ETSINFV-MANO', 'https://nfvwiki.etsi.org/index.php?title=API_specifications#API_conventions')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
GEANT = CurieNamespace('GEANT', 'https://wiki.geant.org/display/OAV/OAV+Terminology+and+Glossary')
GOIOTP = CurieNamespace('GOIotP', 'http://inter-iot.eu/GOIoTP#')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
IOTM3L = CurieNamespace('IOTM3L', 'http://smart-ics.ee.surrey.ac.uk/ontology/fiesta-iot/doc#')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
LOV = CurieNamespace('LOV', 'https://lov.linkeddata.es/dataset/lov/terms?q=')
MAID = CurieNamespace('MAID', 'https://academic.microsoft.com/#/detail/')
MOBI = CurieNamespace('MOBI', 'http://schema.mobivoc.org/#')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NOSQL = CurieNamespace('NOSQL', 'http://purl.org/db/nosql#')
OCO = CurieNamespace('OCO', 'https://www.openlinksw.com/describe/?url=http://www.openlinksw.com/ontology/components%23')
OCRM = CurieNamespace('OCRM', 'https://www.openlinksw.com/describe/?url=http://www.openlinksw.com/ontology/ecrm%23')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OMG_SPECS = CurieNamespace('OMG-SPECS', 'https://www.omg.org/spec/')
ONAP = CurieNamespace('ONAP', 'https://wiki.onap.org/display/DW/Glossary')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
OSO = CurieNamespace('OSO', 'https://www.openlinksw.com/describe/?url=http://www.openlinksw.com/ontology/software%23')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/pato#')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PEERINGDB = CurieNamespace('PeeringDb', 'https://www.peeringdb.com/ix/')
PEERINGDB_FAC = CurieNamespace('PeeringDb_fac', 'https://www.peeringdb.com/fac/')
PEERINGDB_PEERS = CurieNamespace('PeeringDb_peers', 'https://www.peeringdb.com/net/')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RNACENTRAL = CurieNamespace('RNACENTRAL', 'http://identifiers.org/rnacentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RTXKG1 = CurieNamespace('RTXKG1', 'http://kg1endpoint.rtx.ai/')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SAF = CurieNamespace('SAF', 'https://opensaf.sourceforge.io/SAI-Overview-B.05.03.AL.pdf')
SAFAISAMF = CurieNamespace('SAFAISAMF', 'https://opensaf.sourceforge.io/SAI-AIS-AMF-B.04.01.AL.pdf')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN')
SEMMEDDB = CurieNamespace('SEMMEDDB', 'https://skr3.nlm.nih.gov/SemMedDB')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_')
UBERON_CORE = CurieNamespace('UBERON_CORE', 'http://purl.obolibrary.org/obo/uberon/core#')
UMLSSC = CurieNamespace('UMLSSC', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/code#')
UMLSSG = CurieNamespace('UMLSSG', 'https://metamap.nlm.nih.gov/Docs/SemGroups_2018.txt/group#')
UMLSST = CurieNamespace('UMLSST', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/type#')
UO = CurieNamespace('UO', 'https://www.ebi.ac.uk/ols/ontologies/uo')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
XXXX = CurieNamespace('XXXX', 'http://example.org/UNKNOWN/XXXX/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CSOLINK = CurieNamespace('csolink', 'https://w3id.org/csolink/vocab/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
FOLDOC = CurieNamespace('foldoc', 'https://foldoc.org/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
ISBN = CurieNamespace('isbn', 'https://grp.isbn-international.org/content/using-register')
ISNI = CurieNamespace('isni', 'https://isni.org/isni/')
ISSN = CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/')
OPENVOCAB = CurieNamespace('openvocab', 'https://vocab.org/open/#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'https://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'https://www.w3.org/TR/vocab-ssn/#')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'http://sigma.ontologyportal.org:8080/sigma/TreeView.jsp?flang=SUO-KIF&kb=SUMO&simple=yes&term=')
SUMO_WN = CurieNamespace('sumo-wn', 'http://sigma.ontologyportal.org:8080/sigma/WordNet.jsp?POS=0&word=')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CSOLINK


# Types
class ControlPlaneValue(str):
    """ A control plane """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "control plane value"
    type_model_uri = CSOLINK.ControlPlaneValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the csolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the csolink class, for example csolink:Service. For an RDF representation, the value should be a URI such as https://w3id.org/csolink/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = CSOLINK.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = CSOLINK.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = CSOLINK.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the csolink related_to hierarchy. For example, csolink:related_to, csolink:causes, csolink:repairs. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = CSOLINK.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = CSOLINK.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = CSOLINK.SymbolType


class Frequency(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency"
    type_model_uri = CSOLINK.Frequency


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = CSOLINK.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = CSOLINK.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = CSOLINK.Unit


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = CSOLINK.TimeType


class ComputationalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "computational sequence"
    type_model_uri = CSOLINK.ComputationalSequence


# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class ComponentserviceOntologyClassId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class SystemTaxonId(OntologyClassId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DatasetDistributionId(InformationContentEntityId):
    pass


class DatasetVersionId(DatasetId):
    pass


class DistributionLevelId(DatasetVersionId):
    pass


class DatasetSummaryId(DatasetVersionId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BookId(PublicationId):
    pass


class BookChapterId(PublicationId):
    pass


class SerialId(PublicationId):
    pass


class ArticleId(PublicationId):
    pass


class CyberEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class ProcedureId(NamedThingId):
    pass


class PhenomenonId(NamedThingId):
    pass


class DeviceId(NamedThingId):
    pass


class ResourceSampleId(CyberEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class ComputationalEntityId(NamedThingId):
    pass


class OperationalEntityId(ComputationalEntityId):
    pass


class ComputationalProcessOrActivityId(ComputationalEntityId):
    pass


class OperationalActivityId(ComputationalProcessOrActivityId):
    pass


class ComputationalProcessId(ComputationalProcessOrActivityId):
    pass


class PathwayId(ComputationalProcessId):
    pass


class CyberProcessId(ComputationalProcessId):
    pass


class BehaviorId(ComputationalProcessId):
    pass


class DeathId(ComputationalProcessId):
    pass


class ControlActorId(OperationalEntityId):
    pass


class PowerId(ControlActorId):
    pass


class ConsumedResourceId(ControlActorId):
    pass


class AdministrativeOperationId(OperationalEntityId):
    pass


class NotificationComponentId(ControlActorId):
    pass


class EnvironmentalNotificationContaminantId(NotificationComponentId):
    pass


class AwarenessId(NotificationComponentId):
    pass


class DataId(NotificationComponentId):
    pass


class DatastreamId(DataId):
    pass


class BitstreamId(DataId):
    pass


class MessagePassingId(BitstreamId):
    pass


class NotificationId(OperationalEntityId):
    pass


class ControllerId(ControlActorId):
    pass


class SystemicEntityId(ComputationalEntityId):
    pass


class LifecycleStageId(SystemicEntityId):
    pass


class IndividualSystemId(SystemicEntityId):
    pass


class PopulationOfIndividualSystemsId(SystemicEntityId):
    pass


class StudyPopulationId(PopulationOfIndividualSystemsId):
    pass


class ErrorOrObservableFeatureId(ComputationalEntityId):
    pass


class ErrorId(ErrorOrObservableFeatureId):
    pass


class ObservableFeatureId(ErrorOrObservableFeatureId):
    pass


class BehavioralFeatureId(ObservableFeatureId):
    pass


class DeploymentEntityId(SystemicEntityId):
    pass


class ServiceunitId(DeploymentEntityId):
    pass


class ComponentId(DeploymentEntityId):
    pass


class ComponentTypeId(SystemicEntityId):
    pass


class GrossDeploymentStructureId(DeploymentEntityId):
    pass


class WorkloadEntityId(OperationalEntityId):
    pass


class WorkloadId(WorkloadEntityId):
    pass


class ComponentserviceinstanceId(WorkloadEntityId):
    pass


class DaemonId(WorkloadEntityId):
    pass


class CodingSequenceId(WorkloadEntityId):
    pass


class ServiceinstanceId(WorkloadEntityId):
    pass


class ServiceinstanceIsoformId(ServiceinstanceId):
    pass


class KernelServicetypeId(ComponentserviceinstanceId):
    pass


class KernelServicetypeIsoformId(KernelServicetypeId):
    pass


class NoncodingKernelServicetypeId(KernelServicetypeId):
    pass


class KernelMessageId(NoncodingKernelServicetypeId):
    pass


class KernelInterruptId(NoncodingKernelServicetypeId):
    pass


class ComponentserviceFamilyId(OperationalEntityId):
    pass


class ServiceunittypeId(WorkloadEntityId):
    pass


class VariantcomponentservicetypeId(WorkloadEntityId):
    pass


class SequenceVariantId(WorkloadEntityId):
    pass


class MonomericVariantId(SequenceVariantId):
    pass


class ReagentTargetedComponentserviceId(WorkloadEntityId):
    pass


class EmpiricalEntityId(NamedThingId):
    pass


class EmpiricalTrialId(EmpiricalEntityId):
    pass


class EmpiricalInterventionId(EmpiricalEntityId):
    pass


class EmpiricalFindingId(ObservableFeatureId):
    pass


class OfflineMaintenanceId(EmpiricalInterventionId):
    pass


class CaseId(IndividualSystemId):
    pass


class CohortId(StudyPopulationId):
    pass


class ServiceBackgroundExposureId(WorkloadEntityId):
    pass


class FaultyProcessId(ComputationalProcessId):
    pass


class ErrorOrObservableFeatureExposureId(ErrorOrObservableFeatureId):
    pass


class FaultyProcessExposureId(FaultyProcessId):
    pass


class FaultyDeploymentStructureId(DeploymentEntityId):
    pass


class FaultyDeploymentExposureId(FaultyDeploymentStructureId):
    pass


class OrchestrationExposureId(ControlActorId):
    pass


class ComplexOrchestrationExposureId(OrchestrationExposureId):
    pass


class AdministrativeOperationalExposureId(AdministrativeOperationId):
    pass


class AdministrativeOperationalToComponentserviceInteractionExposureId(AdministrativeOperationalExposureId):
    pass


class RepairingId(NamedThingId):
    pass


class BioticExposureId(SystemTaxonId):
    pass


class GeographicExposureId(GeographicLocationId):
    pass


class EnvironmentalExposureId(EnvironmentalProcessId):
    pass


class BehavioralExposureId(BehaviorId):
    pass


class SocioeconomicExposureId(BehaviorId):
    pass


class FaultyProcessOutcomeId(FaultyProcessId):
    pass


class FaultyDeploymentOutcomeId(FaultyDeploymentStructureId):
    pass


class ErrorOrObservableFeatureOutcomeId(ErrorOrObservableFeatureId):
    pass


class BehavioralOutcomeId(BehaviorId):
    pass


class OfflineMaintenanceOutcomeId(OfflineMaintenanceId):
    pass


class MortalityOutcomeId(DeathId):
    pass


class EpidemiologicalOutcomeId(ComputationalEntityId):
    pass


class SocioeconomicOutcomeId(BehaviorId):
    pass


class AssociationId(EntityId):
    pass


class ContributorAssociationId(AssociationId):
    pass


class ServiceunittypeToServiceunittypePartAssociationId(AssociationId):
    pass


class ServiceunittypeToComponentserviceAssociationId(AssociationId):
    pass


class ServiceunittypeToVariantAssociationId(AssociationId):
    pass


class ComponentserviceToComponentserviceAssociationId(AssociationId):
    pass


class ComponentserviceToComponentserviceHomologyAssociationId(ComponentserviceToComponentserviceAssociationId):
    pass


class ComponentserviceToComponentserviceCoavailabilityAssociationId(ComponentserviceToComponentserviceAssociationId):
    pass


class PairwiseComponentserviceToComponentserviceInteractionId(ComponentserviceToComponentserviceAssociationId):
    pass


class PairwiseOperationallyInteractionId(PairwiseComponentserviceToComponentserviceInteractionId):
    pass


class ComponentTypeToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class OrchestrationToOrchestrationAssociationId(AssociationId):
    pass


class OrchestrationToOrchestrationDerivationAssociationId(OrchestrationToOrchestrationAssociationId):
    pass


class OrchestrationToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class OrchestrationToPathwayAssociationId(AssociationId):
    pass


class OrchestrationToComponentserviceAssociationId(AssociationId):
    pass


class AdministrativeOperationalToComponentserviceAssociationId(AssociationId):
    pass


class ResourceSampleDerivationAssociationId(AssociationId):
    pass


class ResourceSampleToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class ErrorToExposureEventAssociationId(AssociationId):
    pass


class ExposureEventToOutcomeAssociationId(AssociationId):
    pass


class ErrorOrObservableFeatureAssociationToLocationAssociationId(AssociationId):
    pass


class ErrorOrObservableFeatureToLocationAssociationId(AssociationId):
    pass


class ServiceunittypeToObservableFeatureAssociationId(AssociationId):
    pass


class ExposureEventToObservableFeatureAssociationId(AssociationId):
    pass


class ErrorToObservableFeatureAssociationId(AssociationId):
    pass


class CaseToObservableFeatureAssociationId(AssociationId):
    pass


class BehaviorToBehavioralFeatureAssociationId(AssociationId):
    pass


class ComponentserviceToObservableFeatureAssociationId(AssociationId):
    pass


class ComponentserviceToErrorAssociationId(AssociationId):
    pass


class VariantToComponentserviceAssociationId(AssociationId):
    pass


class VariantToComponentserviceAvailabilityAssociationId(VariantToComponentserviceAssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToObservableFeatureAssociationId(AssociationId):
    pass


class VariantToErrorAssociationId(AssociationId):
    pass


class ServiceunittypeToErrorAssociationId(AssociationId):
    pass


class ComponentserviceAsAModelOfErrorAssociationId(ComponentserviceToErrorAssociationId):
    pass


class VariantAsAModelOfErrorAssociationId(VariantToErrorAssociationId):
    pass


class ServiceunittypeAsAModelOfErrorAssociationId(ServiceunittypeToErrorAssociationId):
    pass


class ComponentTypeAsAModelOfErrorAssociationId(ComponentTypeToErrorOrObservableFeatureAssociationId):
    pass


class SystemicEntityAsAModelOfErrorAssociationId(AssociationId):
    pass


class ComponentserviceHasVariantThatContributesToErrorAssociationId(ComponentserviceToErrorAssociationId):
    pass


class ComponentserviceToAvailabilitySiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesRepairingAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacrooperationalMachineMixinToOperationalActivityAssociationId(FunctionalAssociationId):
    pass


class MacrooperationalMachineMixinToComputationalProcessAssociationId(FunctionalAssociationId):
    pass


class MacrooperationalMachineMixinToComponentAssociationId(FunctionalAssociationId):
    pass


class ComponentserviceToGoTermAssociationId(FunctionalAssociationId):
    pass


class SequenceAssociationId(AssociationId):
    pass


class ServiceSequenceLocalizationId(SequenceAssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class ComponentserviceinstanceToComponentserviceRelationshipId(SequenceFeatureRelationshipId):
    pass


class ComponentserviceToServicetypeRelationshipId(SequenceFeatureRelationshipId):
    pass


class DaemonToComponentserviceinstanceRelationshipId(SequenceFeatureRelationshipId):
    pass


class ComponentserviceRegulatoryRelationshipId(AssociationId):
    pass


class DeploymentEntityToDeploymentEntityAssociationId(AssociationId):
    pass


class DeploymentEntityToDeploymentEntityPartOfAssociationId(DeploymentEntityToDeploymentEntityAssociationId):
    pass


class DeploymentEntityToDeploymentEntityOntogenicAssociationId(DeploymentEntityToDeploymentEntityAssociationId):
    pass


class Annotation(YAMLRoot):
    """
    Csolink Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Annotation
    class_class_curie: ClassVar[str] = "csolink:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.QuantityValue
    class_class_curie: ClassVar[str] = "csolink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = CSOLINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Attribute
    class_class_curie: ClassVar[str] = "csolink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Attribute

    has_attribute_type: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None
    source: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_attribute_type is None:
            raise ValueError("has_attribute_type must be supplied")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.has_quantitative_value is None:
            self.has_quantitative_value = []
        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value]
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**v) for v in self.has_quantitative_value]

        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.source is not None and not isinstance(self.source, LabelType):
            self.source = LabelType(self.source)

        super().__post_init__(**kwargs)


class AttributeType(YAMLRoot):
    """
    A property or characteristic type of an entity. For example, an apple may have properties types such as color
    type, shape type, age type, crispiness type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AttributeType
    class_class_curie: ClassVar[str] = "csolink:AttributeType"
    class_name: ClassVar[str] = "attribute type"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AttributeType


@dataclass
class ComputationalArchitecturalStyle(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComputationalArchitecturalStyle
    class_class_curie: ClassVar[str] = "csolink:ComputationalArchitecturalStyle"
    class_name: ClassVar[str] = "computational architectural style"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComputationalArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ObservableArchitecturalStyle(ComputationalArchitecturalStyle):
    """
    An attribute corresponding to the observable architectural style of the individual, based upon the reproductive
    applications present.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ObservableArchitecturalStyle
    class_class_curie: ClassVar[str] = "csolink:ObservableArchitecturalStyle"
    class_name: ClassVar[str] = "observable architectural style"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ObservableArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class MicroserviceArchitecturalStyle(ComputationalArchitecturalStyle):
    """
    An attribute corresponding to the microservice architectural style of the individual, based upon microservice
    composition of architectural style containers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MicroserviceArchitecturalStyle
    class_class_curie: ClassVar[str] = "csolink:MicroserviceArchitecturalStyle"
    class_name: ClassVar[str] = "microservice architectural style"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MicroserviceArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a observable feature or error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SeverityValue
    class_class_curie: ClassVar[str] = "csolink:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SeverityValue

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.FrequencyValue
    class_class_curie: ClassVar[str] = "csolink:FrequencyValue"
    class_name: ClassVar[str] = "frequency value"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FrequencyValue

    has_attribute_type: Union[str, OntologyClassId] = None

class RelationshipQuantifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.RelationshipQuantifier
    class_class_curie: ClassVar[str] = "csolink:RelationshipQuantifier"
    class_name: ClassVar[str] = "relationship quantifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.RelationshipQuantifier


class SensitivityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SensitivityQuantifier
    class_class_curie: ClassVar[str] = "csolink:SensitivityQuantifier"
    class_name: ClassVar[str] = "sensitivity quantifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SensitivityQuantifier


class SpecificityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SpecificityQuantifier
    class_class_curie: ClassVar[str] = "csolink:SpecificityQuantifier"
    class_name: ClassVar[str] = "specificity quantifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SpecificityQuantifier


class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a error, which is high when the presence of the feature
    implies the existence of the error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PathognomonicityQuantifier
    class_class_curie: ClassVar[str] = "csolink:PathognomonicityQuantifier"
    class_name: ClassVar[str] = "pathognomonicity quantifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PathognomonicityQuantifier


@dataclass
class FrequencyQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.FrequencyQuantifier
    class_class_curie: ClassVar[str] = "csolink:FrequencyQuantifier"
    class_name: ClassVar[str] = "frequency quantifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FrequencyQuantifier

    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Root Csolink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Entity
    class_class_curie: ClassVar[str] = "csolink:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Entity

    id: Union[str, EntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    iri: Optional[Union[str, IriType]] = None
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    source: Optional[Union[str, LabelType]] = None
    provided_by: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        elif not isinstance(self.category, list):
            self.category = [self.category]
        elif len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if self.source is not None and not isinstance(self.source, LabelType):
            self.source = LabelType(self.source)

        if self.provided_by is None:
            self.provided_by = []
        if not isinstance(self.provided_by, list):
            self.provided_by = [self.provided_by]
        self.provided_by = [v if isinstance(v, AgentId) else AgentId(v) for v in self.provided_by]

        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.NamedThing
    class_class_curie: ClassVar[str] = "csolink:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = CSOLINK.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.category is None:
            raise ValueError("category must be supplied")
        elif not isinstance(self.category, list):
            self.category = [self.category]
        elif len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.category]

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OntologyClass
    class_class_curie: ClassVar[str] = "csolink:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OntologyClass

    id: Union[str, OntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.RelationshipType
    class_class_curie: ClassVar[str] = "csolink:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = CSOLINK.RelationshipType

    id: Union[str, RelationshipTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceOntologyClass(OntologyClass):
    """
    an ontology class that describes a controlling aspect of a componentservice, servicetype or complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceOntologyClass
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceOntologyClass"
    class_name: ClassVar[str] = "componentservice ontology class"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceOntologyClass

    id: Union[str, ComponentserviceOntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceOntologyClassId):
            self.id = ComponentserviceOntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.TaxonomicRank
    class_class_curie: ClassVar[str] = "csolink:TaxonomicRank"
    class_name: ClassVar[str] = "taxonomic rank"
    class_model_uri: ClassVar[URIRef] = CSOLINK.TaxonomicRank

    id: Union[str, TaxonomicRankId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TaxonomicRankId):
            self.id = TaxonomicRankId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemTaxon(OntologyClass):
    """
    A classification of a set of systems. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.SystemTaxon
    class_class_curie: ClassVar[str] = "csolink:SystemTaxon"
    class_name: ClassVar[str] = "system taxon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SystemTaxon

    id: Union[str, SystemTaxonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None
    subclass_of: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SystemTaxonId):
            self.id = SystemTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AdministrativeEntity
    class_class_curie: ClassVar[str] = "csolink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    service, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Agent
    class_class_curie: ClassVar[str] = "csolink:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if self.affiliation is None:
            self.affiliation = []
        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation]
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.InformationContentEntity
    class_class_curie: ClassVar[str] = "csolink:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Dataset
    class_class_curie: ClassVar[str] = "csolink:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Dataset

    id: Union[str, DatasetId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DatasetDistribution
    class_class_curie: ClassVar[str] = "csolink:DatasetDistribution"
    class_name: ClassVar[str] = "dataset distribution"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DatasetDistribution

    id: Union[str, DatasetDistributionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    distribution_download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetDistributionId):
            self.id = DatasetDistributionId(self.id)

        if self.distribution_download_url is not None and not isinstance(self.distribution_download_url, str):
            self.distribution_download_url = str(self.distribution_download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetVersion(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DatasetVersion
    class_class_curie: ClassVar[str] = "csolink:DatasetVersion"
    class_name: ClassVar[str] = "dataset version"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DatasetVersion

    id: Union[str, DatasetVersionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_dataset: Optional[Union[str, DatasetId]] = None
    ingest_date: Optional[str] = None
    has_distribution: Optional[Union[str, DatasetDistributionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetVersionId):
            self.id = DatasetVersionId(self.id)

        if self.has_dataset is not None and not isinstance(self.has_dataset, DatasetId):
            self.has_dataset = DatasetId(self.has_dataset)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.has_distribution is not None and not isinstance(self.has_distribution, DatasetDistributionId):
            self.has_distribution = DatasetDistributionId(self.has_distribution)

        super().__post_init__(**kwargs)


@dataclass
class DistributionLevel(DatasetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DistributionLevel
    class_class_curie: ClassVar[str] = "csolink:DistributionLevel"
    class_name: ClassVar[str] = "distribution level"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DistributionLevel

    id: Union[str, DistributionLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.download_url is not None and not isinstance(self.download_url, str):
            self.download_url = str(self.download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetSummary(DatasetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DatasetSummary
    class_class_curie: ClassVar[str] = "csolink:DatasetSummary"
    class_name: ClassVar[str] = "dataset summary"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DatasetSummary

    id: Union[str, DatasetSummaryId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    source_web_page: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source_web_page is not None and not isinstance(self.source_web_page, str):
            self.source_web_page = str(self.source_web_page)

        super().__post_init__(**kwargs)


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ConfidenceLevel
    class_class_curie: ClassVar[str] = "csolink:ConfidenceLevel"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EvidenceType
    class_class_curie: ClassVar[str] = "csolink:EvidenceType"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed resources, either directly or in one of the Publication Csolink category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Publication
    class_class_curie: ClassVar[str] = "csolink:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    sumo_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.type is None:
            raise ValueError("type must be supplied")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.authors is None:
            self.authors = []
        if not isinstance(self.authors, list):
            self.authors = [self.authors]
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.pages is None:
            self.pages = []
        if not isinstance(self.pages, list):
            self.pages = [self.pages]
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.keywords is None:
            self.keywords = []
        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords]
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.sumo_terms is None:
            self.sumo_terms = []
        if not isinstance(self.sumo_terms, list):
            self.sumo_terms = [self.sumo_terms]
        self.sumo_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.sumo_terms]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Book(Publication):
    """
    This class may rarely be available except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Book
    class_class_curie: ClassVar[str] = "csolink:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if self.type is None:
            raise ValueError("type must be supplied")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class BookChapter(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.BookChapter
    class_class_curie: ClassVar[str] = "csolink:BookChapter"
    class_name: ClassVar[str] = "book chapter"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BookChapter

    id: Union[str, BookChapterId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    volume: Optional[str] = None
    chapter: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BookChapterId):
            self.id = BookChapterId(self.id)

        if self.published_in is None:
            raise ValueError("published_in must be supplied")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        super().__post_init__(**kwargs)


@dataclass
class Serial(Publication):
    """
    This class may rarely be available except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Serial
    class_class_curie: ClassVar[str] = "csolink:Serial"
    class_name: ClassVar[str] = "serial"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Serial

    id: Union[str, SerialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SerialId):
            self.id = SerialId(self.id)

        if self.type is None:
            raise ValueError("type must be supplied")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


@dataclass
class Article(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Article
    class_class_curie: ClassVar[str] = "csolink:Article"
    class_name: ClassVar[str] = "article"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Article

    id: Union[str, ArticleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ArticleId):
            self.id = ArticleId(self.id)

        if self.published_in is None:
            raise ValueError("published_in must be supplied")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


class CyberEssenceOrOccurrent(YAMLRoot):
    """
    Either a cyber or processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CyberEssenceOrOccurrent
    class_class_curie: ClassVar[str] = "csolink:CyberEssenceOrOccurrent"
    class_name: ClassVar[str] = "cyber essence or occurrent"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CyberEssenceOrOccurrent


class CyberEssence(CyberEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CyberEssence
    class_class_curie: ClassVar[str] = "csolink:CyberEssence"
    class_name: ClassVar[str] = "cyber essence"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CyberEssence


@dataclass
class CyberEntity(NamedThing):
    """
    An entity that has digital reality (a.k.a. cyber essence).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CyberEntity
    class_class_curie: ClassVar[str] = "csolink:CyberEntity"
    class_name: ClassVar[str] = "cyber entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CyberEntity

    id: Union[str, CyberEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CyberEntityId):
            self.id = CyberEntityId(self.id)

        super().__post_init__(**kwargs)


class Occurrent(CyberEssenceOrOccurrent):
    """
    A processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Occurrent
    class_class_curie: ClassVar[str] = "csolink:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Occurrent


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "csolink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ActivityAndBehavior


@dataclass
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Activity
    class_class_curie: ClassVar[str] = "csolink:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Activity

    id: Union[str, ActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Procedure(NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Procedure
    class_class_curie: ClassVar[str] = "csolink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Procedure

    id: Union[str, ProcedureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Phenomenon
    class_class_curie: ClassVar[str] = "csolink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Phenomenon

    id: Union[str, PhenomenonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Device
    class_class_curie: ClassVar[str] = "csolink:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Device

    id: Union[str, DeviceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)


class SubjectOfInvestigation(YAMLRoot):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SubjectOfInvestigation
    class_class_curie: ClassVar[str] = "csolink:SubjectOfInvestigation"
    class_name: ClassVar[str] = "subject of investigation"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SubjectOfInvestigation


@dataclass
class ResourceSample(CyberEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ResourceSample
    class_class_curie: ClassVar[str] = "csolink:ResourceSample"
    class_name: ClassVar[str] = "resource sample"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ResourceSample

    id: Union[str, ResourceSampleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceSampleId):
            self.id = ResourceSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PlanetaryEntity
    class_class_curie: ClassVar[str] = "csolink:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "csolink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "csolink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeographicLocation
    class_class_curie: ClassVar[str] = "csolink:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeographicLocationAtTime
    class_class_curie: ClassVar[str] = "csolink:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ComputationalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComputationalEntity
    class_class_curie: ClassVar[str] = "csolink:ComputationalEntity"
    class_name: ClassVar[str] = "computational entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComputationalEntity

    id: Union[str, ComputationalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems;
    componentservices, their servicetypes and other operation entities; computer parts; computational processes
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ThingWithTaxon
    class_class_curie: ClassVar[str] = "csolink:ThingWithTaxon"
    class_name: ClassVar[str] = "thing with taxon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntity(ComputationalEntity):
    """
    A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.OperationalEntity
    class_class_curie: ClassVar[str] = "csolink:OperationalEntity"
    class_name: ClassVar[str] = "operational entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OperationalEntity

    id: Union[str, OperationalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OperationalEntityId):
            self.id = OperationalEntityId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcessOrActivity(ComputationalEntity):
    """
    Either an individual operational activity, or a collection of causally connected operational activities
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComputationalProcessOrActivity
    class_class_curie: ClassVar[str] = "csolink:ComputationalProcessOrActivity"
    class_name: ClassVar[str] = "computational process or activity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComputationalProcessOrActivity

    id: Union[str, ComputationalProcessOrActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComputationalProcessOrActivityId):
            self.id = ComputationalProcessOrActivityId(self.id)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if self.has_output is None:
            self.has_output = []
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output]
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if self.enabled_by is None:
            self.enabled_by = []
        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by]
        self.enabled_by = [v if isinstance(v, CyberEntityId) else CyberEntityId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class OperationalActivity(ComputationalProcessOrActivity):
    """
    An execution of a operational function carried out by a servicetype or macrooperational complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.OperationalActivity
    class_class_curie: ClassVar[str] = "csolink:OperationalActivity"
    class_name: ClassVar[str] = "operational activity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OperationalActivity

    id: Union[str, OperationalActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "MacrooperationalMachineMixin"], List[Union[dict, "MacrooperationalMachineMixin"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OperationalActivityId):
            self.id = OperationalActivityId(self.id)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_input]

        if self.has_output is None:
            self.has_output = []
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output]
        self.has_output = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_output]

        if self.enabled_by is None:
            self.enabled_by = []
        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by]
        self.enabled_by = [v if isinstance(v, MacrooperationalMachineMixin) else MacrooperationalMachineMixin(**v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcess(ComputationalProcessOrActivity):
    """
    One or more causally connected executions of operational functions
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComputationalProcess
    class_class_curie: ClassVar[str] = "csolink:ComputationalProcess"
    class_name: ClassVar[str] = "computational process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComputationalProcess

    id: Union[str, ComputationalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComputationalProcessId):
            self.id = ComputationalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Pathway
    class_class_curie: ClassVar[str] = "csolink:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Pathway

    id: Union[str, PathwayId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CyberProcess(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.CyberProcess
    class_class_curie: ClassVar[str] = "csolink:CyberProcess"
    class_name: ClassVar[str] = "cyber process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CyberProcess

    id: Union[str, CyberProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CyberProcessId):
            self.id = CyberProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Behavior(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Behavior
    class_class_curie: ClassVar[str] = "csolink:Behavior"
    class_name: ClassVar[str] = "behavior"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Behavior

    id: Union[str, BehaviorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Death(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Death
    class_class_curie: ClassVar[str] = "csolink:Death"
    class_name: ClassVar[str] = "death"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Death

    id: Union[str, DeathId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeathId):
            self.id = DeathId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cluster(YAMLRoot):
    """
    The cyber combination of two or more operational entities in which the identities are retained and are mixed in
    the form of solutions,
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Cluster
    class_class_curie: ClassVar[str] = "csolink:Cluster"
    class_name: ClassVar[str] = "cluster"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Cluster

    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class ControlActor(OperationalEntity):
    """
    May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex
    resource with multiple orchestration entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ControlActor
    class_class_curie: ClassVar[str] = "csolink:ControlActor"
    class_name: ClassVar[str] = "control actor"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ControlActor

    id: Union[str, ControlActorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ControlActorId):
            self.id = ControlActorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Power(ControlActor):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Power
    class_class_curie: ClassVar[str] = "csolink:Power"
    class_name: ClassVar[str] = "power"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Power

    id: Union[str, PowerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PowerId):
            self.id = PowerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ConsumedResource(ControlActor):
    """
    A control actor (often a cluster) consumed for information, engineering or technical use.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ConsumedResource
    class_class_curie: ClassVar[str] = "csolink:ConsumedResource"
    class_name: ClassVar[str] = "consumed resource"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ConsumedResource

    id: Union[str, ConsumedResourceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ConsumedResourceId):
            self.id = ConsumedResourceId(self.id)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperation(OperationalEntity):
    """
    A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperation
    class_class_curie: ClassVar[str] = "csolink:AdministrativeOperation"
    class_name: ClassVar[str] = "administrative operation"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperation

    id: Union[str, AdministrativeOperationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationId):
            self.id = AdministrativeOperationId(self.id)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class NotificationComponent(ControlActor):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.NotificationComponent
    class_class_curie: ClassVar[str] = "csolink:NotificationComponent"
    class_name: ClassVar[str] = "notification component"
    class_model_uri: ClassVar[URIRef] = CSOLINK.NotificationComponent

    id: Union[str, NotificationComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NotificationComponentId):
            self.id = NotificationComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalNotificationContaminant(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalNotificationContaminant
    class_class_curie: ClassVar[str] = "csolink:EnvironmentalNotificationContaminant"
    class_name: ClassVar[str] = "environmental notification contaminant"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalNotificationContaminant

    id: Union[str, EnvironmentalNotificationContaminantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalNotificationContaminantId):
            self.id = EnvironmentalNotificationContaminantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Awareness(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Awareness
    class_class_curie: ClassVar[str] = "csolink:Awareness"
    class_name: ClassVar[str] = "awareness"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Awareness

    id: Union[str, AwarenessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AwarenessId):
            self.id = AwarenessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Data(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Data
    class_class_curie: ClassVar[str] = "csolink:Data"
    class_name: ClassVar[str] = "data"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Data

    id: Union[str, DataId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataId):
            self.id = DataId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Datastream(Data):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Datastream
    class_class_curie: ClassVar[str] = "csolink:Datastream"
    class_name: ClassVar[str] = "datastream"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Datastream

    id: Union[str, DatastreamId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatastreamId):
            self.id = DatastreamId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Bitstream(Data):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Bitstream
    class_class_curie: ClassVar[str] = "csolink:Bitstream"
    class_name: ClassVar[str] = "bitstream"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Bitstream

    id: Union[str, BitstreamId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BitstreamId):
            self.id = BitstreamId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MessagePassing(Bitstream):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MessagePassing
    class_class_curie: ClassVar[str] = "csolink:MessagePassing"
    class_name: ClassVar[str] = "message passing"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MessagePassing

    id: Union[str, MessagePassingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MessagePassingId):
            self.id = MessagePassingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Notification(OperationalEntity):
    """
    A event consumed by a healthy system as a source of information
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_data"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Notification
    class_class_curie: ClassVar[str] = "csolink:Notification"
    class_name: ClassVar[str] = "notification"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Notification

    id: Union[str, NotificationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_data: Optional[Union[Union[str, DataId], List[Union[str, DataId]]]] = empty_list()
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NotificationId):
            self.id = NotificationId(self.id)

        if self.has_data is None:
            self.has_data = []
        if not isinstance(self.has_data, list):
            self.has_data = [self.has_data]
        self.has_data = [v if isinstance(v, DataId) else DataId(v) for v in self.has_data]

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class Controller(ControlActor):
    """
    Any intermediate or servicetype resulting from director supervision. Includes primary and secondary controllers.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Controller
    class_class_curie: ClassVar[str] = "csolink:Controller"
    class_name: ClassVar[str] = "controller"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Controller

    id: Union[str, ControllerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    is_controller: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ControllerId):
            self.id = ControllerId(self.id)

        if self.is_controller is not None and not isinstance(self.is_controller, Bool):
            self.is_controller = Bool(self.is_controller)

        super().__post_init__(**kwargs)


@dataclass
class SystemAttribute(Attribute):
    """
    describes a characteristic of an systemic entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SystemAttribute
    class_class_curie: ClassVar[str] = "csolink:SystemAttribute"
    class_name: ClassVar[str] = "system attribute"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SystemAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ObservableQuality(SystemAttribute):
    """
    A property of a observable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ObservableQuality
    class_class_curie: ClassVar[str] = "csolink:ObservableQuality"
    class_name: ClassVar[str] = "observable quality"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ObservableQuality

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Inheritance(SystemAttribute):
    """
    The pattern or 'mode' in which a particular service trait or disorder is passed from one generation to the next,
    e.g. autosomal dominant, autosomal recessive, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Inheritance
    class_class_curie: ClassVar[str] = "csolink:Inheritance"
    class_name: ClassVar[str] = "inheritance"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Inheritance

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class SystemicEntity(ComputationalEntity):
    """
    A named entity that is either a part of a system, a whole system, population or clade of systems, excluding
    operational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SystemicEntity
    class_class_curie: ClassVar[str] = "csolink:SystemicEntity"
    class_name: ClassVar[str] = "systemic entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SystemicEntity

    id: Union[str, SystemicEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class LifecycleStage(SystemicEntity):
    """
    A stage of development or growth of a system.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.LifecycleStage
    class_class_curie: ClassVar[str] = "csolink:LifecycleStage"
    class_name: ClassVar[str] = "lifecycle stage"
    class_model_uri: ClassVar[URIRef] = CSOLINK.LifecycleStage

    id: Union[str, LifecycleStageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, LifecycleStageId):
            self.id = LifecycleStageId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class IndividualSystem(SystemicEntity):
    """
    An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID:
    ORCID:0000-0002-5355-2576
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.IndividualSystem
    class_class_curie: ClassVar[str] = "csolink:IndividualSystem"
    class_name: ClassVar[str] = "individual system"
    class_model_uri: ClassVar[URIRef] = CSOLINK.IndividualSystem

    id: Union[str, IndividualSystemId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, IndividualSystemId):
            self.id = IndividualSystemId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class PopulationOfIndividualSystems(SystemicEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.PopulationOfIndividualSystems
    class_class_curie: ClassVar[str] = "csolink:PopulationOfIndividualSystems"
    class_name: ClassVar[str] = "population of individual systems"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PopulationOfIndividualSystems

    id: Union[str, PopulationOfIndividualSystemsId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PopulationOfIndividualSystemsId):
            self.id = PopulationOfIndividualSystemsId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class StudyPopulation(PopulationOfIndividualSystems):
    """
    A group of individuals banded together or repaired as a group as participants in a research study.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.StudyPopulation
    class_class_curie: ClassVar[str] = "csolink:StudyPopulation"
    class_name: ClassVar[str] = "study population"
    class_model_uri: ClassVar[URIRef] = CSOLINK.StudyPopulation

    id: Union[str, StudyPopulationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, StudyPopulationId):
            self.id = StudyPopulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeature(ComputationalEntity):
    """
    Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as
    distinct, others conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeature
    class_class_curie: ClassVar[str] = "csolink:ErrorOrObservableFeature"
    class_name: ClassVar[str] = "error or observable feature"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeature

    id: Union[str, ErrorOrObservableFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureId):
            self.id = ErrorOrObservableFeatureId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Error(ErrorOrObservableFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Error
    class_class_curie: ClassVar[str] = "csolink:Error"
    class_name: ClassVar[str] = "error"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Error

    id: Union[str, ErrorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorId):
            self.id = ErrorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObservableFeature(ErrorOrObservableFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ObservableFeature
    class_class_curie: ClassVar[str] = "csolink:ObservableFeature"
    class_name: ClassVar[str] = "observable feature"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ObservableFeature

    id: Union[str, ObservableFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ObservableFeatureId):
            self.id = ObservableFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralFeature(ObservableFeature):
    """
    A observable feature which is behavioral in nature.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BehavioralFeature
    class_class_curie: ClassVar[str] = "csolink:BehavioralFeature"
    class_name: ClassVar[str] = "behavioral feature"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BehavioralFeature

    id: Union[str, BehavioralFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralFeatureId):
            self.id = BehavioralFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntity(SystemicEntity):
    """
    A process location, serviceunit type or gross deployment part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntity
    class_class_curie: ClassVar[str] = "csolink:DeploymentEntity"
    class_name: ClassVar[str] = "deployment entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntity

    id: Union[str, DeploymentEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityId):
            self.id = DeploymentEntityId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Serviceunit(DeploymentEntity):
    """
    The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a
    group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a
    cluster. It can be deployed, isolated, and repaired independently.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Serviceunit
    class_class_curie: ClassVar[str] = "csolink:Serviceunit"
    class_name: ClassVar[str] = "serviceunit"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Serviceunit

    id: Union[str, ServiceunitId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunitId):
            self.id = ServiceunitId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Component(DeploymentEntity):
    """
    The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and
    repaired independently. Each component belongs to one, and only one, serviceunit.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Component
    class_class_curie: ClassVar[str] = "csolink:Component"
    class_name: ClassVar[str] = "component"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Component

    id: Union[str, ComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentType(SystemicEntity):
    """
    A component type defines the set of components running the same software and sharing the same configuration. It's
    a single point of configuration control.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentType
    class_class_curie: ClassVar[str] = "csolink:ComponentType"
    class_name: ClassVar[str] = "component type"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentType

    id: Union[str, ComponentTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentTypeId):
            self.id = ComponentTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GrossDeploymentStructure(DeploymentEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GrossDeploymentStructure
    class_class_curie: ClassVar[str] = "csolink:GrossDeploymentStructure"
    class_name: ClassVar[str] = "gross deployment structure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GrossDeploymentStructure

    id: Union[str, GrossDeploymentStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GrossDeploymentStructureId):
            self.id = GrossDeploymentStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixin(YAMLRoot):
    """
    A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a
    component. They either carry out individual computational activities, or they encode tasks which do this.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixin
    class_class_curie: ClassVar[str] = "csolink:MacrooperationalMachineMixin"
    class_name: ClassVar[str] = "macrooperational machine mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixin

    name: Optional[Union[str, SymbolType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)

        super().__post_init__(**kwargs)


class ComponentserviceOrServicetype(MacrooperationalMachineMixin):
    """
    a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for
    another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceOrServicetype
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceOrServicetype"
    class_name: ClassVar[str] = "componentservice or servicetype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceOrServicetype


@dataclass
class Componentservice(ComponentserviceOrServicetype):
    """
    A component service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Componentservice
    class_class_curie: ClassVar[str] = "csolink:Componentservice"
    class_name: ClassVar[str] = "componentservice"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Componentservice

    symbol: Optional[str] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ServicetypeMixin(ComponentserviceOrServicetype):
    """
    The controlling operational servicetype of a single componentservice locus. ServiceType product are either
    serviceinstances or supervisor tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServicetypeMixin
    class_class_curie: ClassVar[str] = "csolink:ServicetypeMixin"
    class_name: ClassVar[str] = "servicetype mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServicetypeMixin

    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


class ServicetypeIsoformMixin(ServicetypeMixin):
    """
    This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the
    servicetype is intended to represent a specific isoform rather than a canonical or reference or generic
    servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all
    isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServicetypeIsoformMixin
    class_class_curie: ClassVar[str] = "csolink:ServicetypeIsoformMixin"
    class_name: ClassVar[str] = "servicetype isoform mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServicetypeIsoformMixin


class MacrooperationalComplexMixin(MacrooperationalMachineMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalComplexMixin
    class_class_curie: ClassVar[str] = "csolink:MacrooperationalComplexMixin"
    class_name: ClassVar[str] = "macrooperational complex mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalComplexMixin


@dataclass
class WorkloadEntity(OperationalEntity):
    """
    An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon,
    regulatory region) or is encoded in a workload (serviceinstance)
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.WorkloadEntity
    class_class_curie: ClassVar[str] = "csolink:WorkloadEntity"
    class_name: ClassVar[str] = "workload entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.WorkloadEntity

    id: Union[str, WorkloadEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, WorkloadEntityId):
            self.id = WorkloadEntityId(self.id)

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class Workload(WorkloadEntity):
    """
    A workload is the sum of componentservice resources within a serviceunit or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Workload
    class_class_curie: ClassVar[str] = "csolink:Workload"
    class_name: ClassVar[str] = "workload"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Workload

    id: Union[str, WorkloadId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, WorkloadId):
            self.id = WorkloadId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Componentserviceinstance(WorkloadEntity):
    """
    The unit of service workload the component is capable of providing or protecting.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Componentserviceinstance
    class_class_curie: ClassVar[str] = "csolink:Componentserviceinstance"
    class_name: ClassVar[str] = "componentserviceinstance"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Componentserviceinstance

    id: Union[str, ComponentserviceinstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceinstanceId):
            self.id = ComponentserviceinstanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Daemon(WorkloadEntity):
    """
    A region of the componentserviceinstance sequence within a componentservice.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Daemon
    class_class_curie: ClassVar[str] = "csolink:Daemon"
    class_name: ClassVar[str] = "daemon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Daemon

    id: Union[str, DaemonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DaemonId):
            self.id = DaemonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CodingSequence(WorkloadEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.CodingSequence
    class_class_curie: ClassVar[str] = "csolink:CodingSequence"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Serviceinstance(WorkloadEntity):
    """
    A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Serviceinstance
    class_class_curie: ClassVar[str] = "csolink:Serviceinstance"
    class_name: ClassVar[str] = "serviceinstance"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Serviceinstance

    id: Union[str, ServiceinstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceinstanceId):
            self.id = ServiceinstanceId(self.id)

        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ServiceinstanceIsoform(Serviceinstance):
    """
    Represents a serviceinstance that is a specific isoform of the canonical or reference serviceinstance.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceinstanceIsoform
    class_class_curie: ClassVar[str] = "csolink:ServiceinstanceIsoform"
    class_name: ClassVar[str] = "serviceinstance isoform"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceinstanceIsoform

    id: Union[str, ServiceinstanceIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceinstanceIsoformId):
            self.id = ServiceinstanceIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelServicetype(Componentserviceinstance):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.KernelServicetype
    class_class_curie: ClassVar[str] = "csolink:KernelServicetype"
    class_name: ClassVar[str] = "kernel servicetype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.KernelServicetype

    id: Union[str, KernelServicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelServicetypeId):
            self.id = KernelServicetypeId(self.id)

        if self.synonym is None:
            self.synonym = []
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym]
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if self.xref is None:
            self.xref = []
        if not isinstance(self.xref, list):
            self.xref = [self.xref]
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class KernelServicetypeIsoform(KernelServicetype):
    """
    Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.KernelServicetypeIsoform
    class_class_curie: ClassVar[str] = "csolink:KernelServicetypeIsoform"
    class_name: ClassVar[str] = "kernel servicetype isoform"
    class_model_uri: ClassVar[URIRef] = CSOLINK.KernelServicetypeIsoform

    id: Union[str, KernelServicetypeIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelServicetypeIsoformId):
            self.id = KernelServicetypeIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NoncodingKernelServicetype(KernelServicetype):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.NoncodingKernelServicetype
    class_class_curie: ClassVar[str] = "csolink:NoncodingKernelServicetype"
    class_name: ClassVar[str] = "noncoding kernel servicetype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.NoncodingKernelServicetype

    id: Union[str, NoncodingKernelServicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NoncodingKernelServicetypeId):
            self.id = NoncodingKernelServicetypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelMessage(NoncodingKernelServicetype):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.KernelMessage
    class_class_curie: ClassVar[str] = "csolink:KernelMessage"
    class_name: ClassVar[str] = "kernel message"
    class_model_uri: ClassVar[URIRef] = CSOLINK.KernelMessage

    id: Union[str, KernelMessageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelMessageId):
            self.id = KernelMessageId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelInterrupt(NoncodingKernelServicetype):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.KernelInterrupt
    class_class_curie: ClassVar[str] = "csolink:KernelInterrupt"
    class_name: ClassVar[str] = "kernel interrupt"
    class_model_uri: ClassVar[URIRef] = CSOLINK.KernelInterrupt

    id: Union[str, KernelInterruptId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, KernelInterruptId):
            self.id = KernelInterruptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceGroupingMixin(YAMLRoot):
    """
    any grouping of multiple componentservices or servicetypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceGroupingMixin
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceGroupingMixin"
    class_name: ClassVar[str] = "componentservice grouping mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceGroupingMixin

    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceFamily(OperationalEntity):
    """
    any grouping of multiple componentservices or servicetypes related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceFamily
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceFamily"
    class_name: ClassVar[str] = "componentservice family"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceFamily

    id: Union[str, ComponentserviceFamilyId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceFamilyId):
            self.id = ComponentserviceFamilyId(self.id)

        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class Homogeneity(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Homogeneity
    class_class_curie: ClassVar[str] = "csolink:Homogeneity"
    class_name: ClassVar[str] = "homogeneity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Homogeneity

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Serviceunittype(WorkloadEntity):
    """
    An information content entity that describes a workload by specifying the total variation in service sequence
    and/or componentservice availability, relative to some established background
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Serviceunittype
    class_class_curie: ClassVar[str] = "csolink:Serviceunittype"
    class_name: ClassVar[str] = "serviceunittype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Serviceunittype

    id: Union[str, ServiceunittypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_homogeneity: Optional[Union[dict, Homogeneity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeId):
            self.id = ServiceunittypeId(self.id)

        if self.has_homogeneity is not None and not isinstance(self.has_homogeneity, Homogeneity):
            self.has_homogeneity = Homogeneity(**self.has_homogeneity)

        super().__post_init__(**kwargs)


@dataclass
class Variantcomponentservicetype(WorkloadEntity):
    """
    A set of zero or more variantcomponentservices on a single instance of a Sequence
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Variantcomponentservicetype
    class_class_curie: ClassVar[str] = "csolink:Variantcomponentservicetype"
    class_name: ClassVar[str] = "variantcomponentservicetype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Variantcomponentservicetype

    id: Union[str, VariantcomponentservicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantcomponentservicetypeId):
            self.id = VariantcomponentservicetypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariant(WorkloadEntity):
    """
    A variantcomponentservice that varies in its sequence from what is considered the reference
    variantcomponentservice at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.SequenceVariant
    class_class_curie: ClassVar[str] = "csolink:SequenceVariant"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)

        if self.has_componentservice is None:
            self.has_componentservice = []
        if not isinstance(self.has_componentservice, list):
            self.has_componentservice = [self.has_componentservice]
        self.has_componentservice = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice]

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class MonomericVariant(SequenceVariant):
    """
    A single monomeric position in the service monomeric variants are single monomeric positions in service DNA at
    which different sequence alternatives exist
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MonomericVariant
    class_class_curie: ClassVar[str] = "csolink:MonomericVariant"
    class_name: ClassVar[str] = "monomeric variant"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MonomericVariant

    id: Union[str, MonomericVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MonomericVariantId):
            self.id = MonomericVariantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ReagentTargetedComponentservice(WorkloadEntity):
    """
    A componentservice altered in its availability level in the context of some experiment as a result of being
    targeted by componentservice-knockdown reagent(s).
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ReagentTargetedComponentservice
    class_class_curie: ClassVar[str] = "csolink:ReagentTargetedComponentservice"
    class_name: ClassVar[str] = "reagent targeted componentservice"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ReagentTargetedComponentservice

    id: Union[str, ReagentTargetedComponentserviceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ReagentTargetedComponentserviceId):
            self.id = ReagentTargetedComponentserviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalAttribute(Attribute):
    """
    Attributes relating to a empirical manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalAttribute
    class_class_curie: ClassVar[str] = "csolink:EmpiricalAttribute"
    class_name: ClassVar[str] = "empirical attribute"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalMeasurement(EmpiricalAttribute):
    """
    A empirical measurement is a special kind of attribute which results from a quality of serviceunit observation
    from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalMeasurement
    class_class_curie: ClassVar[str] = "csolink:EmpiricalMeasurement"
    class_name: ClassVar[str] = "empirical measurement"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalMeasurement

    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_attribute_type is None:
            raise ValueError("has_attribute_type must be supplied")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalModifier(EmpiricalAttribute):
    """
    Used to characterize and specify the observable abnormalities defined in the observable abnormality sub-ontology,
    with respect to severity, laterality, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalModifier
    class_class_curie: ClassVar[str] = "csolink:EmpiricalModifier"
    class_name: ClassVar[str] = "empirical modifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalModifier

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalCourse(EmpiricalAttribute):
    """
    The course a error typically takes from its onset, progression in time, and eventual resolution or death of the
    affected individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalCourse
    class_class_curie: ClassVar[str] = "csolink:EmpiricalCourse"
    class_name: ClassVar[str] = "empirical course"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalCourse

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Onset(EmpiricalCourse):
    """
    The age group in which (error) symptom manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Onset
    class_class_curie: ClassVar[str] = "csolink:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Onset

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalEntity(NamedThing):
    """
    Any entity or process that exists in the empirical domain and outside the computational realm. Errors are placed
    under computational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalEntity
    class_class_curie: ClassVar[str] = "csolink:EmpiricalEntity"
    class_name: ClassVar[str] = "empirical entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalEntity

    id: Union[str, EmpiricalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalEntityId):
            self.id = EmpiricalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalTrial(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalTrial
    class_class_curie: ClassVar[str] = "csolink:EmpiricalTrial"
    class_name: ClassVar[str] = "empirical trial"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalTrial

    id: Union[str, EmpiricalTrialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalTrialId):
            self.id = EmpiricalTrialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalIntervention(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalIntervention
    class_class_curie: ClassVar[str] = "csolink:EmpiricalIntervention"
    class_name: ClassVar[str] = "empirical intervention"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalIntervention

    id: Union[str, EmpiricalInterventionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalInterventionId):
            self.id = EmpiricalInterventionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalFinding(ObservableFeature):
    """
    this category is currently considered broad enough to tag empirical lab measurements and other computational
    attributes taken as 'empirical traits' with some statistical score, for example, a p value in service
    associations.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.EmpiricalFinding
    class_class_curie: ClassVar[str] = "csolink:EmpiricalFinding"
    class_name: ClassVar[str] = "empirical finding"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EmpiricalFinding

    id: Union[str, EmpiricalFindingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, EmpiricalAttribute], List[Union[dict, EmpiricalAttribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EmpiricalFindingId):
            self.id = EmpiricalFindingId(self.id)

        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=EmpiricalAttribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenance(EmpiricalIntervention):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OfflineMaintenance
    class_class_curie: ClassVar[str] = "csolink:OfflineMaintenance"
    class_name: ClassVar[str] = "offline maintenance"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OfflineMaintenance

    id: Union[str, OfflineMaintenanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OfflineMaintenanceId):
            self.id = OfflineMaintenanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SocioeconomicAttribute
    class_class_curie: ClassVar[str] = "csolink:SocioeconomicAttribute"
    class_name: ClassVar[str] = "socioeconomic attribute"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SocioeconomicAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Case(IndividualSystem):
    """
    An individual system that has a patient role in some empirical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Case
    class_class_curie: ClassVar[str] = "csolink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Case

    id: Union[str, CaseId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cohort(StudyPopulation):
    """
    A group of individuals banded together or repaired as a group who share common characteristics. A cohort 'study'
    is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through
    time.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Cohort
    class_class_curie: ClassVar[str] = "csolink:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Cohort

    id: Union[str, CohortId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(YAMLRoot):
    """
    A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more
    observability of that system, potentially mediated by serviceunits
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExposureEvent
    class_class_curie: ClassVar[str] = "csolink:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExposureEvent

    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ServiceBackgroundExposure(WorkloadEntity):
    """
    A service background exposure is where an individual's specific service background of serviceunits, sequence
    variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or
    influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceBackgroundExposure
    class_class_curie: ClassVar[str] = "csolink:ServiceBackgroundExposure"
    class_name: ClassVar[str] = "service background exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceBackgroundExposure

    id: Union[str, ServiceBackgroundExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceBackgroundExposureId):
            self.id = ServiceBackgroundExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


class FaultyEntityMixin(YAMLRoot):
    """
    A faulty (abnormal) structure or process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyEntityMixin
    class_class_curie: ClassVar[str] = "csolink:FaultyEntityMixin"
    class_name: ClassVar[str] = "faulty entity mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyEntityMixin


@dataclass
class FaultyProcess(ComputationalProcess):
    """
    A compulogic function or a process having an abnormal or deleterious effect at the subcomponent, component,
    multi-component, node, or system level.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyProcess
    class_class_curie: ClassVar[str] = "csolink:FaultyProcess"
    class_name: ClassVar[str] = "faulty process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyProcess

    id: Union[str, FaultyProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyProcessId):
            self.id = FaultyProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureExposure(ErrorOrObservableFeature):
    """
    A error or observable feature exposure is where a error state is manifested which represents an precondition,
    leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular
    error.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureExposure
    class_class_curie: ClassVar[str] = "csolink:ErrorOrObservableFeatureExposure"
    class_name: ClassVar[str] = "error or observable feature exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureExposure

    id: Union[str, ErrorOrObservableFeatureExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureExposureId):
            self.id = ErrorOrObservableFeatureExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyProcessExposure(FaultyProcess):
    """
    A faulty process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome,
    e.g. autoimmunity leading to disease.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyProcessExposure
    class_class_curie: ClassVar[str] = "csolink:FaultyProcessExposure"
    class_name: ClassVar[str] = "faulty process exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyProcessExposure

    id: Union[str, FaultyProcessExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyProcessExposureId):
            self.id = FaultyProcessExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentStructure(DeploymentEntity):
    """
    An deployment structure with the potential of have an abnormal or deleterious effect at the process, serviceunit,
    multiserviceunit, or systemal level.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyDeploymentStructure
    class_class_curie: ClassVar[str] = "csolink:FaultyDeploymentStructure"
    class_name: ClassVar[str] = "faulty deployment structure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyDeploymentStructure

    id: Union[str, FaultyDeploymentStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyDeploymentStructureId):
            self.id = FaultyDeploymentStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentExposure(FaultyDeploymentStructure):
    """
    An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or
    influencing an outcome,
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyDeploymentExposure
    class_class_curie: ClassVar[str] = "csolink:FaultyDeploymentExposure"
    class_name: ClassVar[str] = "faulty deployment exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyDeploymentExposure

    id: Union[str, FaultyDeploymentExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyDeploymentExposureId):
            self.id = FaultyDeploymentExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationExposure(ControlActor):
    """
    A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationExposure
    class_class_curie: ClassVar[str] = "csolink:OrchestrationExposure"
    class_name: ClassVar[str] = "orchestration exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationExposure

    id: Union[str, OrchestrationExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationExposureId):
            self.id = OrchestrationExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ComplexOrchestrationExposure(OrchestrationExposure):
    """
    A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a
    administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComplexOrchestrationExposure
    class_class_curie: ClassVar[str] = "csolink:ComplexOrchestrationExposure"
    class_name: ClassVar[str] = "complex orchestration exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComplexOrchestrationExposure

    id: Union[str, ComplexOrchestrationExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComplexOrchestrationExposureId):
            self.id = ComplexOrchestrationExposureId(self.id)

        if self.has_control_actor is None:
            self.has_control_actor = []
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor]
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalExposure(AdministrativeOperation):
    """
    A administrative operational exposure is an intake of a particular administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalExposure
    class_class_curie: ClassVar[str] = "csolink:AdministrativeOperationalExposure"
    class_name: ClassVar[str] = "administrative operational exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalExposure

    id: Union[str, AdministrativeOperationalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationalExposureId):
            self.id = AdministrativeOperationalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToComponentserviceInteractionExposure(AdministrativeOperationalExposure):
    """
    administrative operational to componentservice interaction exposure is a administrative operational exposure is
    where the interactions of the administrative operational with specific componentservices are known to constitute
    an 'exposure' to the system, leading to or influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalToComponentserviceInteractionExposure
    class_class_curie: ClassVar[str] = "csolink:AdministrativeOperationalToComponentserviceInteractionExposure"
    class_name: ClassVar[str] = "administrative operational to componentservice interaction exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalToComponentserviceInteractionExposure

    id: Union[str, AdministrativeOperationalToComponentserviceInteractionExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationalToComponentserviceInteractionExposureId):
            self.id = AdministrativeOperationalToComponentserviceInteractionExposureId(self.id)

        if self.has_componentservice_or_servicetype is None:
            self.has_componentservice_or_servicetype = []
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype]
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**v) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class Repairing(NamedThing):
    """
    A repairing is targeted at a error or observability and may involve multiple administrative operational
    'exposures', engineering devices and/or procedures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Repairing
    class_class_curie: ClassVar[str] = "csolink:Repairing"
    class_name: ClassVar[str] = "repairing"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Repairing

    id: Union[str, RepairingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_administrative_operation: Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]] = empty_list()
    has_device: Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RepairingId):
            self.id = RepairingId(self.id)

        if self.has_administrative_operation is None:
            self.has_administrative_operation = []
        if not isinstance(self.has_administrative_operation, list):
            self.has_administrative_operation = [self.has_administrative_operation]
        self.has_administrative_operation = [v if isinstance(v, AdministrativeOperationId) else AdministrativeOperationId(v) for v in self.has_administrative_operation]

        if self.has_device is None:
            self.has_device = []
        if not isinstance(self.has_device, list):
            self.has_device = [self.has_device]
        self.has_device = [v if isinstance(v, DeviceId) else DeviceId(v) for v in self.has_device]

        if self.has_procedure is None:
            self.has_procedure = []
        if not isinstance(self.has_procedure, list):
            self.has_procedure = [self.has_procedure]
        self.has_procedure = [v if isinstance(v, ProcedureId) else ProcedureId(v) for v in self.has_procedure]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BioticExposure(SystemTaxon):
    """
    A biotic exposure is an intake of (sometimes faulty) computational systems (including viruses)
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BioticExposure
    class_class_curie: ClassVar[str] = "csolink:BioticExposure"
    class_name: ClassVar[str] = "biotic exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BioticExposure

    id: Union[str, BioticExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BioticExposureId):
            self.id = BioticExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class GeographicExposure(GeographicLocation):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeographicExposure
    class_class_curie: ClassVar[str] = "csolink:GeographicExposure"
    class_name: ClassVar[str] = "geographic exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeographicExposure

    id: Union[str, GeographicExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicExposureId):
            self.id = GeographicExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalExposure(EnvironmentalProcess):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including atmospheric (heat,
    cold, general pollution) and water-born contaminants
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalExposure
    class_class_curie: ClassVar[str] = "csolink:EnvironmentalExposure"
    class_name: ClassVar[str] = "environmental exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralExposure(Behavior):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BehavioralExposure
    class_class_curie: ClassVar[str] = "csolink:BehavioralExposure"
    class_name: ClassVar[str] = "behavioral exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BehavioralExposure

    id: Union[str, BehavioralExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralExposureId):
            self.id = BehavioralExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicExposure(Behavior):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g.
    poverty).
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.SocioeconomicExposure
    class_class_curie: ClassVar[str] = "csolink:SocioeconomicExposure"
    class_name: ClassVar[str] = "socioeconomic exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SocioeconomicExposure

    id: Union[str, SocioeconomicExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Union[Union[dict, SocioeconomicAttribute], List[Union[dict, SocioeconomicAttribute]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SocioeconomicExposureId):
            self.id = SocioeconomicExposureId(self.id)

        if self.has_attribute is None:
            raise ValueError("has_attribute must be supplied")
        elif not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        elif len(self.has_attribute) == 0:
            raise ValueError(f"has_attribute must be a non-empty list")
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=SocioeconomicAttribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


class Outcome(YAMLRoot):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible computational or non-computational (e.g. empirical) outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Outcome
    class_class_curie: ClassVar[str] = "csolink:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Outcome


@dataclass
class FaultyProcessOutcome(FaultyProcess):
    """
    An outcome resulting from an exposure event which is the manifestation of a faulty process.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyProcessOutcome
    class_class_curie: ClassVar[str] = "csolink:FaultyProcessOutcome"
    class_name: ClassVar[str] = "faulty process outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyProcessOutcome

    id: Union[str, FaultyProcessOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyProcessOutcomeId):
            self.id = FaultyProcessOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentOutcome(FaultyDeploymentStructure):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal deployment structure.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.FaultyDeploymentOutcome
    class_class_curie: ClassVar[str] = "csolink:FaultyDeploymentOutcome"
    class_name: ClassVar[str] = "faulty deployment outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FaultyDeploymentOutcome

    id: Union[str, FaultyDeploymentOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FaultyDeploymentOutcomeId):
            self.id = FaultyDeploymentOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureOutcome(ErrorOrObservableFeature):
    """
    logical outcomes resulting from an exposure event which is the manifestation of a error or other characteristic
    observability.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureOutcome
    class_class_curie: ClassVar[str] = "csolink:ErrorOrObservableFeatureOutcome"
    class_name: ClassVar[str] = "error or observable feature outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureOutcome

    id: Union[str, ErrorOrObservableFeatureOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureOutcomeId):
            self.id = ErrorOrObservableFeatureOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralOutcome(Behavior):
    """
    An outcome resulting from an exposure event which is the manifestation of individual behavior.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BehavioralOutcome
    class_class_curie: ClassVar[str] = "csolink:BehavioralOutcome"
    class_name: ClassVar[str] = "behavioral outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BehavioralOutcome

    id: Union[str, BehavioralOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralOutcomeId):
            self.id = BehavioralOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenanceOutcome(OfflineMaintenance):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room
    visit) or chronic (inpatient) offline maintenance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OfflineMaintenanceOutcome
    class_class_curie: ClassVar[str] = "csolink:OfflineMaintenanceOutcome"
    class_name: ClassVar[str] = "offline maintenance outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OfflineMaintenanceOutcome

    id: Union[str, OfflineMaintenanceOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OfflineMaintenanceOutcomeId):
            self.id = OfflineMaintenanceOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MortalityOutcome(Death):
    """
    An outcome of death from resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MortalityOutcome
    class_class_curie: ClassVar[str] = "csolink:MortalityOutcome"
    class_name: ClassVar[str] = "mortality outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MortalityOutcome

    id: Union[str, MortalityOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MortalityOutcomeId):
            self.id = MortalityOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EpidemiologicalOutcome(ComputationalEntity):
    """
    An epidemiological outcome, such as societal error burden, resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EpidemiologicalOutcome
    class_class_curie: ClassVar[str] = "csolink:EpidemiologicalOutcome"
    class_name: ClassVar[str] = "epidemiological outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EpidemiologicalOutcome

    id: Union[str, EpidemiologicalOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, EpidemiologicalOutcomeId):
            self.id = EpidemiologicalOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicOutcome(Behavior):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure
    event
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.SocioeconomicOutcome
    class_class_curie: ClassVar[str] = "csolink:SocioeconomicOutcome"
    class_name: ClassVar[str] = "socioeconomic outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SocioeconomicOutcome

    id: Union[str, SocioeconomicOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SocioeconomicOutcomeId):
            self.id = SocioeconomicOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Association
    class_class_curie: ClassVar[str] = "csolink:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        if self.category is None:
            raise ValueError("category must be supplied")
        elif not isinstance(self.category, list):
            self.category = [self.category]
        elif len(self.category) == 0:
            raise ValueError(f"category must be a non-empty list")
        self.category = [v if isinstance(v, AssociationId) else AssociationId(v) for v in self.category]

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        if self.publications is None:
            self.publications = []
        if not isinstance(self.publications, list):
            self.publications = [self.publications]
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ContributorAssociation
    class_class_curie: ClassVar[str] = "csolink:ContributorAssociation"
    class_name: ClassVar[str] = "contributor association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ContributorAssociation

    id: Union[str, ContributorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, InformationContentEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, AgentId] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ContributorAssociationId):
            self.id = ContributorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, InformationContentEntityId):
            self.subject = InformationContentEntityId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AgentId):
            self.object = AgentId(self.object)

        if self.qualifiers is None:
            self.qualifiers = []
        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers]
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToServiceunittypePartAssociation(Association):
    """
    Any association between one serviceunittype and a microservice entity that is a subset of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToServiceunittypePartAssociation
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeToServiceunittypePartAssociation"
    class_name: ClassVar[str] = "serviceunittype to serviceunittype part association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToServiceunittypePartAssociation

    id: Union[str, ServiceunittypeToServiceunittypePartAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToServiceunittypePartAssociationId):
            self.id = ServiceunittypeToServiceunittypePartAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServiceunittypeId):
            self.object = ServiceunittypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToComponentserviceAssociation(Association):
    """
    Any association between a serviceunittype and a componentservice. The serviceunittype have have multiple variants
    in that componentservice or a single one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeToComponentserviceAssociation"
    class_name: ClassVar[str] = "serviceunittype to componentservice association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToComponentserviceAssociation

    id: Union[str, ServiceunittypeToComponentserviceAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[dict, Componentservice] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToComponentserviceAssociationId):
            self.id = ServiceunittypeToComponentserviceAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToVariantAssociation(Association):
    """
    Any association between a serviceunittype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToVariantAssociation
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeToVariantAssociation"
    class_name: ClassVar[str] = "serviceunittype to variant association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToVariantAssociation

    id: Union[str, ServiceunittypeToVariantAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToVariantAssociationId):
            self.id = ServiceunittypeToVariantAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceAssociation(Association):
    """
    abstract parent class for different kinds of componentservice-serviceunit or servicetype to servicetype
    relationships. Includes homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToComponentserviceAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToComponentserviceAssociation

    id: Union[str, ComponentserviceToComponentserviceAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceHomologyAssociation(ComponentserviceToComponentserviceAssociation):
    """
    A homology association between two componentservices. May be orthology (in which case the species of subject and
    object should differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToComponentserviceHomologyAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToComponentserviceHomologyAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice homology association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToComponentserviceHomologyAssociation

    id: Union[str, ComponentserviceToComponentserviceHomologyAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToComponentserviceHomologyAssociationId):
            self.id = ComponentserviceToComponentserviceHomologyAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceAvailabilityMixin(YAMLRoot):
    """
    Observed componentservice availability intensity, context (site, stage) and associated observable status within
    which the availability occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceAvailabilityMixin
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceAvailabilityMixin"
    class_name: ClassVar[str] = "componentservice availability mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceAvailabilityMixin

    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceCoavailabilityAssociation(ComponentserviceToComponentserviceAssociation):
    """
    Indicates that two componentservices are co-available, generally under the same conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToComponentserviceCoavailabilityAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToComponentserviceCoavailabilityAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice coavailability association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToComponentserviceCoavailabilityAssociation

    id: Union[str, ComponentserviceToComponentserviceCoavailabilityAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToComponentserviceCoavailabilityAssociationId):
            self.id = ComponentserviceToComponentserviceCoavailabilityAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseComponentserviceToComponentserviceInteraction(ComponentserviceToComponentserviceAssociation):
    """
    An interaction between two componentservices or two servicetypes. May be cyber (e.g. serviceinstance binding) or
    service (between componentservices). May be symmetric (e.g. serviceinstance interaction) or directed (e.g.
    phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PairwiseComponentserviceToComponentserviceInteraction
    class_class_curie: ClassVar[str] = "csolink:PairwiseComponentserviceToComponentserviceInteraction"
    class_name: ClassVar[str] = "pairwise componentservice to componentservice interaction"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PairwiseComponentserviceToComponentserviceInteraction

    id: Union[str, PairwiseComponentserviceToComponentserviceInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PairwiseComponentserviceToComponentserviceInteractionId):
            self.id = PairwiseComponentserviceToComponentserviceInteractionId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseOperationallyInteraction(PairwiseComponentserviceToComponentserviceInteraction):
    """
    An interaction at the operational level between two cyber entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PairwiseOperationallyInteraction
    class_class_curie: ClassVar[str] = "csolink:PairwiseOperationallyInteraction"
    class_name: ClassVar[str] = "pairwise operationally interaction"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PairwiseOperationallyInteraction

    id: Union[str, PairwiseOperationallyInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OperationalEntityId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, OperationalEntityId] = None
    interacting_tasks_category: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PairwiseOperationallyInteractionId):
            self.id = PairwiseOperationallyInteractionId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.relation is None:
            raise ValueError("relation must be supplied")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, OperationalEntityId):
            self.object = OperationalEntityId(self.object)

        if self.interacting_tasks_category is not None and not isinstance(self.interacting_tasks_category, OntologyClassId):
            self.interacting_tasks_category = OntologyClassId(self.interacting_tasks_category)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToEntityAssociationMixin(YAMLRoot):
    """
    An relationship between a component type and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentTypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ComponentTypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "component type to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentTypeToEntityAssociationMixin

    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToErrorOrObservableFeatureAssociation(Association):
    """
    An relationship between a component type and a error or a observability, where the component type is derived from
    an individual with that error or observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentTypeToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentTypeToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "component type to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentTypeToErrorOrObservableFeatureAssociation

    id: Union[str, ComponentTypeToErrorOrObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentTypeToErrorOrObservableFeatureAssociationId):
            self.id = ComponentTypeToErrorOrObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ErrorOrObservableFeatureId):
            self.subject = ErrorOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntityToEntityAssociationMixin(YAMLRoot):
    """
    An interaction between a operational entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OperationalEntityToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:OperationalEntityToEntityAssociationMixin"
    class_name: ClassVar[str] = "operational entity to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OperationalEntityToEntityAssociationMixin

    subject: Union[str, OperationalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToEntityAssociationMixin(OperationalEntityToEntityAssociationMixin):
    """
    An interaction between a administrative operational and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:AdministrativeOperationalToEntityAssociationMixin"
    class_name: ClassVar[str] = "administrative operational to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalToEntityAssociationMixin

    subject: Union[str, AdministrativeOperationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, AdministrativeOperationId):
            self.subject = AdministrativeOperationId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToEntityAssociationMixin(OperationalEntityToEntityAssociationMixin):
    """
    An interaction between a orchestration entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:OrchestrationToEntityAssociationMixin"
    class_name: ClassVar[str] = "orchestration to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToEntityAssociationMixin

    subject: Union[str, ControlActorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ControlActorId):
            self.subject = ControlActorId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class CaseToEntityAssociationMixin(YAMLRoot):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CaseToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:CaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "case to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CaseToEntityAssociationMixin

    subject: Union[str, CaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToOrchestrationAssociation(Association):
    """
    A relationship between two orchestration entities. This can encompass actual interactions as well as temporal
    causal edges, e.g. one orchestration converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToOrchestrationAssociation
    class_class_curie: ClassVar[str] = "csolink:OrchestrationToOrchestrationAssociation"
    class_name: ClassVar[str] = "orchestration to orchestration association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToOrchestrationAssociation

    id: Union[str, OrchestrationToOrchestrationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ControlActorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToOrchestrationAssociationId):
            self.id = OrchestrationToOrchestrationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ControlActorId):
            self.object = ControlActorId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToOrchestrationDerivationAssociation(OrchestrationToOrchestrationAssociation):
    """
    A causal relationship between two orchestration entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction:
    IF
    R has-input C1 AND
    R has-output C2 AND
    R enabled-by P AND
    R type Reaction
    THEN
    C1 derives-into C2 <<catalyst qualifier P>>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToOrchestrationDerivationAssociation
    class_class_curie: ClassVar[str] = "csolink:OrchestrationToOrchestrationDerivationAssociation"
    class_name: ClassVar[str] = "orchestration to orchestration derivation association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToOrchestrationDerivationAssociation

    id: Union[str, OrchestrationToOrchestrationDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ControlActorId] = None
    object: Union[str, ControlActorId] = None
    predicate: Union[str, PredicateType] = None
    catalyst_qualifier: Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToOrchestrationDerivationAssociationId):
            self.id = OrchestrationToOrchestrationDerivationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ControlActorId):
            self.subject = ControlActorId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ControlActorId):
            self.object = ControlActorId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.catalyst_qualifier is None:
            self.catalyst_qualifier = []
        if not isinstance(self.catalyst_qualifier, list):
            self.catalyst_qualifier = [self.catalyst_qualifier]
        self.catalyst_qualifier = [v if isinstance(v, MacrooperationalMachineMixin) else MacrooperationalMachineMixin(**v) for v in self.catalyst_qualifier]

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToErrorOrObservableFeatureAssociation(Association):
    """
    An interaction between a orchestration entity and a observability or error, where the presence of the
    orchestration gives rise to or exacerbates the observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:OrchestrationToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "orchestration to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToErrorOrObservableFeatureAssociation

    id: Union[str, OrchestrationToErrorOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToErrorOrObservableFeatureAssociationId):
            self.id = OrchestrationToErrorOrObservableFeatureAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ErrorOrObservableFeatureId):
            self.object = ErrorOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToPathwayAssociation(Association):
    """
    An interaction between a orchestration entity and a computational process or pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToPathwayAssociation
    class_class_curie: ClassVar[str] = "csolink:OrchestrationToPathwayAssociation"
    class_name: ClassVar[str] = "orchestration to pathway association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToPathwayAssociation

    id: Union[str, OrchestrationToPathwayAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToPathwayAssociationId):
            self.id = OrchestrationToPathwayAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToComponentserviceAssociation(Association):
    """
    An interaction between a orchestration entity and a componentservice or servicetype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "csolink:OrchestrationToComponentserviceAssociation"
    class_name: ClassVar[str] = "orchestration to componentservice association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrchestrationToComponentserviceAssociation

    id: Union[str, OrchestrationToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrchestrationToComponentserviceAssociationId):
            self.id = OrchestrationToComponentserviceAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToComponentserviceAssociation(Association):
    """
    An interaction between a administrative operational and a componentservice or servicetype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "csolink:AdministrativeOperationalToComponentserviceAssociation"
    class_name: ClassVar[str] = "administrative operational to componentservice association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AdministrativeOperationalToComponentserviceAssociation

    id: Union[str, AdministrativeOperationalToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AdministrativeOperationalToComponentserviceAssociationId):
            self.id = AdministrativeOperationalToComponentserviceAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleToEntityAssociationMixin(YAMLRoot):
    """
    An association between a resource sample and something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ResourceSampleToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ResourceSampleToEntityAssociationMixin"
    class_name: ClassVar[str] = "resource sample to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ResourceSampleToEntityAssociationMixin

    subject: Union[str, ResourceSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ResourceSampleId):
            self.subject = ResourceSampleId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleDerivationAssociation(Association):
    """
    An association between a resource sample and the resource entity from which it is derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ResourceSampleDerivationAssociation
    class_class_curie: ClassVar[str] = "csolink:ResourceSampleDerivationAssociation"
    class_name: ClassVar[str] = "resource sample derivation association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ResourceSampleDerivationAssociation

    id: Union[str, ResourceSampleDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ResourceSampleId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceSampleDerivationAssociationId):
            self.id = ResourceSampleDerivationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ResourceSampleId):
            self.subject = ResourceSampleId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleToErrorOrObservableFeatureAssociation(Association):
    """
    An association between a resource sample and a error or observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ResourceSampleToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ResourceSampleToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "resource sample to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ResourceSampleToErrorOrObservableFeatureAssociation

    id: Union[str, ResourceSampleToErrorOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ResourceSampleToErrorOrObservableFeatureAssociationId):
            self.id = ResourceSampleToErrorOrObservableFeatureAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ErrorToEntityAssociationMixin"
    class_name: ClassVar[str] = "error to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorToEntityAssociationMixin

    subject: Union[str, ErrorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ErrorId):
            self.subject = ErrorId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EntityToExposureEventAssociationMixin(YAMLRoot):
    """
    An association between some entity and an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToExposureEventAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToExposureEventAssociationMixin"
    class_name: ClassVar[str] = "entity to exposure event association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToExposureEventAssociationMixin

    object: Union[dict, ExposureEvent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ExposureEvent):
            self.object = ExposureEvent(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToExposureEventAssociation(Association):
    """
    An association between an exposure event and a error.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorToExposureEventAssociation
    class_class_curie: ClassVar[str] = "csolink:ErrorToExposureEventAssociation"
    class_name: ClassVar[str] = "error to exposure event association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorToExposureEventAssociation

    id: Union[str, ErrorToExposureEventAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorToExposureEventAssociationId):
            self.id = ErrorToExposureEventAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToEntityAssociationMixin(YAMLRoot):
    """
    An association between some exposure event and some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ExposureEventToEntityAssociationMixin"
    class_name: ClassVar[str] = "exposure event to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToEntityAssociationMixin

    subject: Union[dict, ExposureEvent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EntityToOutcomeAssociationMixin(YAMLRoot):
    """
    An association between some entity and an outcome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToOutcomeAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToOutcomeAssociationMixin"
    class_name: ClassVar[str] = "entity to outcome association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToOutcomeAssociationMixin

    object: Union[dict, Outcome] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Outcome):
            self.object = Outcome()

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToOutcomeAssociation(Association):
    """
    An association between an exposure event and an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToOutcomeAssociation
    class_class_curie: ClassVar[str] = "csolink:ExposureEventToOutcomeAssociation"
    class_name: ClassVar[str] = "exposure event to outcome association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToOutcomeAssociation

    id: Union[str, ExposureEventToOutcomeAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    has_population_context: Optional[Union[str, PopulationOfIndividualSystemsId]] = None
    has_temporal_context: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExposureEventToOutcomeAssociationId):
            self.id = ExposureEventToOutcomeAssociationId(self.id)

        if self.has_population_context is not None and not isinstance(self.has_population_context, PopulationOfIndividualSystemsId):
            self.has_population_context = PopulationOfIndividualSystemsId(self.has_population_context)

        if self.has_temporal_context is not None and not isinstance(self.has_temporal_context, TimeType):
            self.has_temporal_context = TimeType(self.has_temporal_context)

        super().__post_init__(**kwargs)


@dataclass
class FrequencyQualifierMixin(YAMLRoot):
    """
    Qualifier for frequency type associations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.FrequencyQualifierMixin
    class_class_curie: ClassVar[str] = "csolink:FrequencyQualifierMixin"
    class_name: ClassVar[str] = "frequency qualifier mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FrequencyQualifierMixin

    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFeatureOrErrorQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to error or observability associations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToFeatureOrErrorQualifiersMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToFeatureOrErrorQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or error qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToFeatureOrErrorQualifiersMixin

    severity_qualifier: Optional[Union[dict, SeverityValue]] = None
    onset_qualifier: Optional[Union[dict, Onset]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValue):
            self.severity_qualifier = SeverityValue(**self.severity_qualifier)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, Onset):
            self.onset_qualifier = Onset(**self.onset_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToObservableFeatureAssociationMixin(EntityToFeatureOrErrorQualifiersMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToObservableFeatureAssociationMixin

    object: Union[str, ObservableFeatureId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ObservableFeatureId):
            self.object = ObservableFeatureId(self.object)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        super().__post_init__(**kwargs)


@dataclass
class EntityToErrorAssociationMixin(EntityToFeatureOrErrorQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToErrorAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToErrorAssociationMixin"
    class_name: ClassVar[str] = "entity to error association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToErrorAssociationMixin

    object: Union[str, ErrorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ErrorId):
            self.object = ErrorId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ErrorOrObservableFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "error or observable feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureToEntityAssociationMixin

    subject: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ErrorOrObservableFeatureId):
            self.subject = ErrorOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureAssociationToLocationAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureAssociationToLocationAssociation
    class_class_curie: ClassVar[str] = "csolink:ErrorOrObservableFeatureAssociationToLocationAssociation"
    class_name: ClassVar[str] = "error or observable feature association to location association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureAssociationToLocationAssociation

    id: Union[str, ErrorOrObservableFeatureAssociationToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureAssociationToLocationAssociationId):
            self.id = ErrorOrObservableFeatureAssociationToLocationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureToLocationAssociation(Association):
    """
    An association between either a error or a observable feature and an deployment entity, where the error/feature
    manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureToLocationAssociation
    class_class_curie: ClassVar[str] = "csolink:ErrorOrObservableFeatureToLocationAssociation"
    class_name: ClassVar[str] = "error or observable feature to location association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorOrObservableFeatureToLocationAssociation

    id: Union[str, ErrorOrObservableFeatureToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorOrObservableFeatureToLocationAssociationId):
            self.id = ErrorOrObservableFeatureToLocationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntityToErrorOrObservableFeatureAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToErrorOrObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToErrorOrObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to error or observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToErrorOrObservableFeatureAssociationMixin

    object: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ErrorOrObservableFeatureId):
            self.object = ErrorOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "serviceunittype to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToEntityAssociationMixin

    subject: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToObservableFeatureAssociation(Association):
    """
    Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the
    observability, either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeToObservableFeatureAssociation"
    class_name: ClassVar[str] = "serviceunittype to observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToObservableFeatureAssociation

    id: Union[str, ServiceunittypeToObservableFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToObservableFeatureAssociationId):
            self.id = ServiceunittypeToObservableFeatureAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToObservableFeatureAssociation(Association):
    """
    Any association between an environment and a observable feature, where being in the environment influences the
    observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ExposureEventToObservableFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToObservableFeatureAssociation

    id: Union[str, ExposureEventToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ExposureEvent] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExposureEventToObservableFeatureAssociationId):
            self.id = ExposureEventToObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToObservableFeatureAssociation(Association):
    """
    An association between a error and a observable feature in which the observable feature is associated with the
    error in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ErrorToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ErrorToObservableFeatureAssociation"
    class_name: ClassVar[str] = "error to observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ErrorToObservableFeatureAssociation

    id: Union[str, ErrorToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ErrorToObservableFeatureAssociationId):
            self.id = ErrorToObservableFeatureAssociationId(self.id)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class CaseToObservableFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a observable feature in which the individual has or
    has had the observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CaseToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:CaseToObservableFeatureAssociation"
    class_name: ClassVar[str] = "case to observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CaseToObservableFeatureAssociation

    id: Union[str, CaseToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CaseToObservableFeatureAssociationId):
            self.id = CaseToObservableFeatureAssociationId(self.id)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class BehaviorToBehavioralFeatureAssociation(Association):
    """
    An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or
    has exhibited the behavior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.BehaviorToBehavioralFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:BehaviorToBehavioralFeatureAssociation"
    class_name: ClassVar[str] = "behavior to behavioral feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BehaviorToBehavioralFeatureAssociation

    id: Union[str, BehaviorToBehavioralFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, BehaviorId] = None
    object: Union[str, BehavioralFeatureId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehaviorToBehavioralFeatureAssociationId):
            self.id = BehaviorToBehavioralFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, BehaviorId):
            self.subject = BehaviorId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, BehavioralFeatureId):
            self.object = BehavioralFeatureId(self.object)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToEntityAssociationMixin"
    class_name: ClassVar[str] = "componentservice to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToEntityAssociationMixin

    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:VariantToEntityAssociationMixin"
    class_name: ClassVar[str] = "variant to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToEntityAssociationMixin

    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToObservableFeatureAssociation"
    class_name: ClassVar[str] = "componentservice to observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToObservableFeatureAssociation

    id: Union[str, ComponentserviceToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToObservableFeatureAssociationId):
            self.id = ComponentserviceToObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToErrorAssociation"
    class_name: ClassVar[str] = "componentservice to error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToErrorAssociation

    id: Union[str, ComponentserviceToErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToErrorAssociationId):
            self.id = ComponentserviceToErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantToComponentserviceAssociation(Association):
    """
    An association between a variant and a componentservice, where the variant has a service association with the
    componentservice (i.e. is in linkage disequilibrium)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToComponentserviceAssociation"
    class_name: ClassVar[str] = "variant to componentservice association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToComponentserviceAssociation

    id: Union[str, VariantToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, Componentservice] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToComponentserviceAssociationId):
            self.id = VariantToComponentserviceAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToComponentserviceAvailabilityAssociation(VariantToComponentserviceAssociation):
    """
    An association between a variant and availability of a componentservice (i.e. e-QTL)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToComponentserviceAvailabilityAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToComponentserviceAvailabilityAssociation"
    class_name: ClassVar[str] = "variant to componentservice availability association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToComponentserviceAvailabilityAssociation

    id: Union[str, VariantToComponentserviceAvailabilityAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, Componentservice] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToComponentserviceAvailabilityAssociationId):
            self.id = VariantToComponentserviceAvailabilityAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToPopulationAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToPopulationAssociation"
    class_name: ClassVar[str] = "variant to population association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToPopulationAssociation

    id: Union[str, VariantToPopulationAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PopulationToPopulationAssociation
    class_class_curie: ClassVar[str] = "csolink:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, PopulationOfIndividualSystemsId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, PopulationOfIndividualSystemsId):
            self.subject = PopulationOfIndividualSystemsId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToObservableFeatureAssociation"
    class_name: ClassVar[str] = "variant to observable feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToObservableFeatureAssociation

    id: Union[str, VariantToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToObservableFeatureAssociationId):
            self.id = VariantToObservableFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**self.architectural_style_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class VariantToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToErrorAssociation"
    class_name: ClassVar[str] = "variant to error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToErrorAssociation

    id: Union[str, VariantToErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToErrorAssociationId):
            self.id = VariantToErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeToErrorAssociation"
    class_name: ClassVar[str] = "serviceunittype to error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeToErrorAssociation

    id: Union[str, ServiceunittypeToErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeToErrorAssociationId):
            self.id = ServiceunittypeToErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ModelToErrorAssociationMixin(YAMLRoot):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in
    that it recapitulates some features of the error in a way that is useful for studying the error outside a patient
    carrying the error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ModelToErrorAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ModelToErrorAssociationMixin"
    class_name: ClassVar[str] = "model to error association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ModelToErrorAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceAsAModelOfErrorAssociation(ComponentserviceToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "componentservice as a model of error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceAsAModelOfErrorAssociation

    id: Union[str, ComponentserviceAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceAsAModelOfErrorAssociationId):
            self.id = ComponentserviceAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantAsAModelOfErrorAssociation(VariantToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "variant as a model of error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantAsAModelOfErrorAssociation

    id: Union[str, VariantAsAModelOfErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantAsAModelOfErrorAssociationId):
            self.id = VariantAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeAsAModelOfErrorAssociation(ServiceunittypeToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:ServiceunittypeAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "serviceunittype as a model of error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceunittypeAsAModelOfErrorAssociation

    id: Union[str, ServiceunittypeAsAModelOfErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceunittypeAsAModelOfErrorAssociationId):
            self.id = ServiceunittypeAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeAsAModelOfErrorAssociation(ComponentTypeToErrorOrObservableFeatureAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentTypeAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentTypeAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "component type as a model of error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentTypeAsAModelOfErrorAssociation

    id: Union[str, ComponentTypeAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentTypeAsAModelOfErrorAssociationId):
            self.id = ComponentTypeAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class SystemicEntityAsAModelOfErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SystemicEntityAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:SystemicEntityAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "systemic entity as a model of error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SystemicEntityAsAModelOfErrorAssociation

    id: Union[str, SystemicEntityAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SystemicEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SystemicEntityAsAModelOfErrorAssociationId):
            self.id = SystemicEntityAsAModelOfErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SystemicEntityId):
            self.subject = SystemicEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceHasVariantThatContributesToErrorAssociation(ComponentserviceToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceHasVariantThatContributesToErrorAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceHasVariantThatContributesToErrorAssociation"
    class_name: ClassVar[str] = "componentservice has variant that contributes to error association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceHasVariantThatContributesToErrorAssociation

    id: Union[str, ComponentserviceHasVariantThatContributesToErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceHasVariantThatContributesToErrorAssociationId):
            self.id = ComponentserviceHasVariantThatContributesToErrorAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToAvailabilitySiteAssociation(Association):
    """
    An association between a componentservice and an availability site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToAvailabilitySiteAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToAvailabilitySiteAssociation"
    class_name: ClassVar[str] = "componentservice to availability site association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToAvailabilitySiteAssociation

    id: Union[str, ComponentserviceToAvailabilitySiteAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToAvailabilitySiteAssociationId):
            self.id = ComponentserviceToAvailabilitySiteAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariantModulatesRepairingAssociation(Association):
    """
    An association between a sequence variant and a repairing or health intervention. The repairing object itself
    encompasses both the error and the administrative operational used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SequenceVariantModulatesRepairingAssociation
    class_class_curie: ClassVar[str] = "csolink:SequenceVariantModulatesRepairingAssociation"
    class_name: ClassVar[str] = "sequence variant modulates repairing association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SequenceVariantModulatesRepairingAssociation

    id: Union[str, SequenceVariantModulatesRepairingAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, RepairingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, RepairingId):
            self.object = RepairingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes)
    and either a operational activity, a computational process or a component location in which a function is
    executed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.FunctionalAssociation
    class_class_curie: ClassVar[str] = "csolink:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComponentserviceOntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MacrooperationalMachineMixin):
            self.subject = MacrooperationalMachineMixin(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOntologyClassId):
            self.object = ComponentserviceOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToEntityAssociationMixin(YAMLRoot):
    """
    an association which has a macrooperational machine mixin mixin as a subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:MacrooperationalMachineMixinToEntityAssociationMixin"
    class_name: ClassVar[str] = "macrooperational machine mixin to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToOperationalActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    operational activity (as represented in the GO operational function branch), where the entity carries out the
    activity, or contributes to its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToOperationalActivityAssociation
    class_class_curie: ClassVar[str] = "csolink:MacrooperationalMachineMixinToOperationalActivityAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to operational activity association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToOperationalActivityAssociation

    id: Union[str, MacrooperationalMachineMixinToOperationalActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, OperationalActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacrooperationalMachineMixinToOperationalActivityAssociationId):
            self.id = MacrooperationalMachineMixinToOperationalActivityAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, OperationalActivityId):
            self.object = OperationalActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToComputationalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    computational process or pathway (as represented in the GO computational process branch), where the entity carries
    out some part of the process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToComputationalProcessAssociation
    class_class_curie: ClassVar[str] = "csolink:MacrooperationalMachineMixinToComputationalProcessAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to computational process association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToComputationalProcessAssociation

    id: Union[str, MacrooperationalMachineMixinToComputationalProcessAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComputationalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacrooperationalMachineMixinToComputationalProcessAssociationId):
            self.id = MacrooperationalMachineMixinToComputationalProcessAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComputationalProcessId):
            self.object = ComputationalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    component (as represented in the GO component branch), where the entity carries out its function in the component
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToComponentAssociation
    class_class_curie: ClassVar[str] = "csolink:MacrooperationalMachineMixinToComponentAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to component association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacrooperationalMachineMixinToComponentAssociation

    id: Union[str, MacrooperationalMachineMixinToComponentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacrooperationalMachineMixinToComponentAssociationId):
            self.id = MacrooperationalMachineMixinToComponentAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToGoTermAssociation
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToGoTermAssociation"
    class_name: ClassVar[str] = "componentservice to go term association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToGoTermAssociation

    id: Union[str, ComponentserviceToGoTermAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OperationalEntityId] = None
    object: Union[str, ComponentserviceOntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToGoTermAssociationId):
            self.id = ComponentserviceToGoTermAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOntologyClassId):
            self.object = ComponentserviceOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a workload entity it is localized to.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SequenceAssociation
    class_class_curie: ClassVar[str] = "csolink:SequenceAssociation"
    class_name: ClassVar[str] = "sequence association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SequenceAssociation

    id: Union[str, SequenceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceAssociationId):
            self.id = SequenceAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ServiceSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a workload entity it is localized to. The reference entity may be a
    container, componentservice or information entity such as a namespace.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ServiceSequenceLocalization
    class_class_curie: ClassVar[str] = "csolink:ServiceSequenceLocalization"
    class_name: ClassVar[str] = "service sequence localization"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ServiceSequenceLocalization

    id: Union[str, ServiceSequenceLocalizationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, WorkloadEntityId] = None
    object: Union[str, WorkloadEntityId] = None
    predicate: Union[str, PredicateType] = None
    start_interbase_coordinate: Optional[int] = None
    end_interbase_coordinate: Optional[int] = None
    workload_build: Optional[str] = None
    strand: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ServiceSequenceLocalizationId):
            self.id = ServiceSequenceLocalizationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, WorkloadEntityId):
            self.subject = WorkloadEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, WorkloadEntityId):
            self.object = WorkloadEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.start_interbase_coordinate is not None and not isinstance(self.start_interbase_coordinate, int):
            self.start_interbase_coordinate = int(self.start_interbase_coordinate)

        if self.end_interbase_coordinate is not None and not isinstance(self.end_interbase_coordinate, int):
            self.end_interbase_coordinate = int(self.end_interbase_coordinate)

        if self.workload_build is not None and not isinstance(self.workload_build, str):
            self.workload_build = str(self.workload_build)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.phase is not None and not isinstance(self.phase, str):
            self.phase = str(self.phase)

        super().__post_init__(**kwargs)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular daemon is part of a particular componentserviceinstance or componentservice
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SequenceFeatureRelationship
    class_class_curie: ClassVar[str] = "csolink:SequenceFeatureRelationship"
    class_name: ClassVar[str] = "sequence feature relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SequenceFeatureRelationship

    id: Union[str, SequenceFeatureRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, WorkloadEntityId] = None
    object: Union[str, WorkloadEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, WorkloadEntityId):
            self.subject = WorkloadEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, WorkloadEntityId):
            self.object = WorkloadEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceinstanceToComponentserviceRelationship(SequenceFeatureRelationship):
    """
    A componentservice is a collection of componentserviceinstances
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceinstanceToComponentserviceRelationship
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceinstanceToComponentserviceRelationship"
    class_name: ClassVar[str] = "componentserviceinstance to componentservice relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceinstanceToComponentserviceRelationship

    id: Union[str, ComponentserviceinstanceToComponentserviceRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ComponentserviceinstanceId] = None
    object: Union[dict, Componentservice] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceinstanceToComponentserviceRelationshipId):
            self.id = ComponentserviceinstanceToComponentserviceRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceinstanceId):
            self.subject = ComponentserviceinstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToServicetypeRelationship(SequenceFeatureRelationship):
    """
    A componentservice is transcribed and potentially translated to a servicetype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToServicetypeRelationship
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceToServicetypeRelationship"
    class_name: ClassVar[str] = "componentservice to servicetype relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceToServicetypeRelationship

    id: Union[str, ComponentserviceToServicetypeRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, Componentservice] = None
    object: Union[dict, ServicetypeMixin] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceToServicetypeRelationshipId):
            self.id = ComponentserviceToServicetypeRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, Componentservice):
            self.subject = Componentservice(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ServicetypeMixin):
            self.object = ServicetypeMixin(**self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class DaemonToComponentserviceinstanceRelationship(SequenceFeatureRelationship):
    """
    A componentserviceinstance is formed from multiple daemons
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DaemonToComponentserviceinstanceRelationship
    class_class_curie: ClassVar[str] = "csolink:DaemonToComponentserviceinstanceRelationship"
    class_name: ClassVar[str] = "daemon to componentserviceinstance relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DaemonToComponentserviceinstanceRelationship

    id: Union[str, DaemonToComponentserviceinstanceRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DaemonId] = None
    object: Union[str, ComponentserviceinstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DaemonToComponentserviceinstanceRelationshipId):
            self.id = DaemonToComponentserviceinstanceRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DaemonId):
            self.subject = DaemonId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceinstanceId):
            self.object = ComponentserviceinstanceId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceRegulatoryRelationship(Association):
    """
    A regulatory relationship between two componentservices
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceRegulatoryRelationship
    class_class_curie: ClassVar[str] = "csolink:ComponentserviceRegulatoryRelationship"
    class_name: ClassVar[str] = "componentservice regulatory relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComponentserviceRegulatoryRelationship

    id: Union[str, ComponentserviceRegulatoryRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComponentserviceRegulatoryRelationshipId):
            self.id = ComponentserviceRegulatoryRelationshipId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntityToDeploymentEntityAssociation
    class_class_curie: ClassVar[str] = "csolink:DeploymentEntityToDeploymentEntityAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntityToDeploymentEntityAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityAssociationId):
            self.id = DeploymentEntityToDeploymentEntityAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityPartOfAssociation(DeploymentEntityToDeploymentEntityAssociation):
    """
    A relationship between two deployment entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between components and componentservices, between
    componentservice and servicegroup/replicasets, servicegroup/replicasets and whole systems
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntityToDeploymentEntityPartOfAssociation
    class_class_curie: ClassVar[str] = "csolink:DeploymentEntityToDeploymentEntityPartOfAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity part of association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntityToDeploymentEntityPartOfAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityPartOfAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityPartOfAssociationId):
            self.id = DeploymentEntityToDeploymentEntityPartOfAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityOntogenicAssociation(DeploymentEntityToDeploymentEntityAssociation):
    """
    A relationship between two deployment entities where the relationship is ontogenic, i.e. the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntityToDeploymentEntityOntogenicAssociation
    class_class_curie: ClassVar[str] = "csolink:DeploymentEntityToDeploymentEntityOntogenicAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DeploymentEntityToDeploymentEntityOntogenicAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityOntogenicAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityOntogenicAssociationId):
            self.id = DeploymentEntityToDeploymentEntityOntogenicAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_attribute = Slot(uri=CSOLINK.has_attribute, name="has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.has_attribute_type = Slot(uri=CSOLINK.has_attribute_type, name="has attribute type", curie=CSOLINK.curie('has_attribute_type'),
                   model_uri=CSOLINK.has_attribute_type, domain=AttributeType, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=CSOLINK.has_qualitative_value, name="has qualitative value", curie=CSOLINK.curie('has_qualitative_value'),
                   model_uri=CSOLINK.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=CSOLINK.has_quantitative_value, name="has quantitative value", curie=CSOLINK.curie('has_quantitative_value'),
                   model_uri=CSOLINK.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=CSOLINK.has_numeric_value, name="has numeric value", curie=CSOLINK.curie('has_numeric_value'),
                   model_uri=CSOLINK.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_unit = Slot(uri=CSOLINK.has_unit, name="has unit", curie=CSOLINK.curie('has_unit'),
                   model_uri=CSOLINK.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.node_property = Slot(uri=CSOLINK.node_property, name="node property", curie=CSOLINK.curie('node_property'),
                   model_uri=CSOLINK.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=CSOLINK.id, name="id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.id, domain=None, range=URIRef)

slots.iri = Slot(uri=CSOLINK.iri, name="iri", curie=CSOLINK.curie('iri'),
                   model_uri=CSOLINK.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=CSOLINK.type, domain=None, range=Optional[str])

slots.category = Slot(uri=CSOLINK.category, name="category", curie=CSOLINK.curie('category'),
                   model_uri=CSOLINK.category, domain=Entity, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CSOLINK.name, domain=None, range=Optional[Union[str, LabelType]])

slots.source = Slot(uri=CSOLINK.source, name="source", curie=CSOLINK.curie('source'),
                   model_uri=CSOLINK.source, domain=None, range=Optional[Union[str, LabelType]])

slots.filler = Slot(uri=CSOLINK.filler, name="filler", curie=CSOLINK.curie('filler'),
                   model_uri=CSOLINK.filler, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.symbol = Slot(uri=CSOLINK.symbol, name="symbol", curie=CSOLINK.curie('symbol'),
                   model_uri=CSOLINK.symbol, domain=NamedThing, range=Optional[str])

slots.synonym = Slot(uri=CSOLINK.synonym, name="synonym", curie=CSOLINK.curie('synonym'),
                   model_uri=CSOLINK.synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.has_topic = Slot(uri=CSOLINK.has_topic, name="has topic", curie=CSOLINK.curie('has_topic'),
                   model_uri=CSOLINK.has_topic, domain=NamedThing, range=Optional[Union[str, OntologyClassId]])

slots.xref = Slot(uri=CSOLINK.xref, name="xref", curie=CSOLINK.curie('xref'),
                   model_uri=CSOLINK.xref, domain=NamedThing, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.full_name = Slot(uri=CSOLINK.full_name, name="full name", curie=CSOLINK.curie('full_name'),
                   model_uri=CSOLINK.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=CSOLINK.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=SIO['000122'], name="systematic synonym", curie=SIO.curie('000122'),
                   model_uri=CSOLINK.systematic_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.affiliation = Slot(uri=CSOLINK.affiliation, name="affiliation", curie=CSOLINK.curie('affiliation'),
                   model_uri=CSOLINK.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=CSOLINK.address, name="address", curie=CSOLINK.curie('address'),
                   model_uri=CSOLINK.address, domain=NamedThing, range=Optional[str])

slots.latitude = Slot(uri=CSOLINK.latitude, name="latitude", curie=CSOLINK.curie('latitude'),
                   model_uri=CSOLINK.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=CSOLINK.longitude, name="longitude", curie=CSOLINK.curie('longitude'),
                   model_uri=CSOLINK.longitude, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=CSOLINK.timepoint, name="timepoint", curie=CSOLINK.curie('timepoint'),
                   model_uri=CSOLINK.timepoint, domain=NamedThing, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=CSOLINK.creation_date, name="creation date", curie=CSOLINK.curie('creation_date'),
                   model_uri=CSOLINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=CSOLINK.update_date, name="update date", curie=CSOLINK.curie('update_date'),
                   model_uri=CSOLINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.aggregate_statistic = Slot(uri=CSOLINK.aggregate_statistic, name="aggregate statistic", curie=CSOLINK.curie('aggregate_statistic'),
                   model_uri=CSOLINK.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=CSOLINK.has_count, name="has count", curie=CSOLINK.curie('has_count'),
                   model_uri=CSOLINK.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=CSOLINK.has_total, name="has total", curie=CSOLINK.curie('has_total'),
                   model_uri=CSOLINK.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=CSOLINK.has_quotient, name="has quotient", curie=CSOLINK.curie('has_quotient'),
                   model_uri=CSOLINK.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=CSOLINK.has_percentage, name="has percentage", curie=CSOLINK.curie('has_percentage'),
                   model_uri=CSOLINK.has_percentage, domain=NamedThing, range=Optional[float])

slots.has_dataset = Slot(uri=DCT.source, name="has dataset", curie=DCT.curie('source'),
                   model_uri=CSOLINK.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.source_web_page = Slot(uri=CSOLINK.source_web_page, name="source web page", curie=CSOLINK.curie('source_web_page'),
                   model_uri=CSOLINK.source_web_page, domain=None, range=Optional[str])

slots.source_logo = Slot(uri=SCHEMA.logo, name="source logo", curie=SCHEMA.curie('logo'),
                   model_uri=CSOLINK.source_logo, domain=None, range=Optional[str])

slots.retrieved_on = Slot(uri=CSOLINK.retrieved_on, name="retrieved on", curie=CSOLINK.curie('retrieved_on'),
                   model_uri=CSOLINK.retrieved_on, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=CSOLINK.version_of, name="version of", curie=CSOLINK.curie('version_of'),
                   model_uri=CSOLINK.version_of, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.version = Slot(uri=CSOLINK.version, name="version", curie=CSOLINK.curie('version'),
                   model_uri=CSOLINK.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=CSOLINK.license, name="license", curie=CSOLINK.curie('license'),
                   model_uri=CSOLINK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=CSOLINK.rights, name="rights", curie=CSOLINK.curie('rights'),
                   model_uri=CSOLINK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=CSOLINK.format, name="format", curie=CSOLINK.curie('format'),
                   model_uri=CSOLINK.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=CSOLINK.created_with, name="created_with", curie=CSOLINK.curie('created_with'),
                   model_uri=CSOLINK.created_with, domain=Dataset, range=Optional[str])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download url", curie=DCAT.curie('downloadURL'),
                   model_uri=CSOLINK.download_url, domain=None, range=Optional[str])

slots.dataset_download_url = Slot(uri=DCAT.downloadURL, name="dataset download url", curie=DCAT.curie('downloadURL'),
                   model_uri=CSOLINK.dataset_download_url, domain=Dataset, range=Optional[str])

slots.distribution_download_url = Slot(uri=CSOLINK.distribution_download_url, name="distribution download url", curie=CSOLINK.curie('distribution_download_url'),
                   model_uri=CSOLINK.distribution_download_url, domain=DatasetDistribution, range=Optional[str])

slots.ingest_date = Slot(uri=PAV.version, name="ingest date", curie=PAV.curie('version'),
                   model_uri=CSOLINK.ingest_date, domain=DatasetVersion, range=Optional[str])

slots.has_distribution = Slot(uri=DCT.distribution, name="has distribution", curie=DCT.curie('distribution'),
                   model_uri=CSOLINK.has_distribution, domain=DatasetVersion, range=Optional[Union[str, DatasetDistributionId]])

slots.published_in = Slot(uri=CSOLINK.published_in, name="published in", curie=CSOLINK.curie('published_in'),
                   model_uri=CSOLINK.published_in, domain=Publication, range=Optional[Union[str, URIorCURIE]])

slots.iso_abbreviation = Slot(uri=CSOLINK.iso_abbreviation, name="iso abbreviation", curie=CSOLINK.curie('iso_abbreviation'),
                   model_uri=CSOLINK.iso_abbreviation, domain=Publication, range=Optional[str])

slots.authors = Slot(uri=CSOLINK.authors, name="authors", curie=CSOLINK.curie('authors'),
                   model_uri=CSOLINK.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.volume = Slot(uri=CSOLINK.volume, name="volume", curie=CSOLINK.curie('volume'),
                   model_uri=CSOLINK.volume, domain=Publication, range=Optional[str])

slots.chapter = Slot(uri=CSOLINK.chapter, name="chapter", curie=CSOLINK.curie('chapter'),
                   model_uri=CSOLINK.chapter, domain=BookChapter, range=Optional[str])

slots.issue = Slot(uri=CSOLINK.issue, name="issue", curie=CSOLINK.curie('issue'),
                   model_uri=CSOLINK.issue, domain=Publication, range=Optional[str])

slots.pages = Slot(uri=CSOLINK.pages, name="pages", curie=CSOLINK.curie('pages'),
                   model_uri=CSOLINK.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=CSOLINK.summary, name="summary", curie=CSOLINK.curie('summary'),
                   model_uri=CSOLINK.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=CSOLINK.keywords, name="keywords", curie=CSOLINK.curie('keywords'),
                   model_uri=CSOLINK.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.sumo_terms = Slot(uri=CSOLINK.sumo_terms, name="sumo terms", curie=CSOLINK.curie('sumo_terms'),
                   model_uri=CSOLINK.sumo_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_computational_sequence = Slot(uri=CSOLINK.has_computational_sequence, name="has computational sequence", curie=CSOLINK.curie('has_computational_sequence'),
                   model_uri=CSOLINK.has_computational_sequence, domain=NamedThing, range=Optional[Union[str, ComputationalSequence]])

slots.has_componentservice_or_servicetype = Slot(uri=CSOLINK.has_componentservice_or_servicetype, name="has componentservice or servicetype", curie=CSOLINK.curie('has_componentservice_or_servicetype'),
                   model_uri=CSOLINK.has_componentservice_or_servicetype, domain=NamedThing, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.has_componentservice = Slot(uri=CSOLINK.has_componentservice, name="has componentservice", curie=CSOLINK.curie('has_componentservice'),
                   model_uri=CSOLINK.has_componentservice, domain=NamedThing, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.has_homogeneity = Slot(uri=CSOLINK.has_homogeneity, name="has homogeneity", curie=CSOLINK.curie('has_homogeneity'),
                   model_uri=CSOLINK.has_homogeneity, domain=WorkloadEntity, range=Optional[Union[dict, "Homogeneity"]])

slots.has_control_plane = Slot(uri=CSOLINK.has_control_plane, name="has control plane", curie=CSOLINK.curie('has_control_plane'),
                   model_uri=CSOLINK.has_control_plane, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.is_controller = Slot(uri=CSOLINK.is_controller, name="is controller", curie=CSOLINK.curie('is_controller'),
                   model_uri=CSOLINK.is_controller, domain=Controller, range=Optional[Union[bool, Bool]])

slots.has_control_actor = Slot(uri=CSOLINK.has_control_actor, name="has control actor", curie=CSOLINK.curie('has_control_actor'),
                   model_uri=CSOLINK.has_control_actor, domain=NamedThing, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.has_administrative_operation = Slot(uri=CSOLINK.has_administrative_operation, name="has administrative operation", curie=CSOLINK.curie('has_administrative_operation'),
                   model_uri=CSOLINK.has_administrative_operation, domain=NamedThing, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]])

slots.has_device = Slot(uri=CSOLINK.has_device, name="has device", curie=CSOLINK.curie('has_device'),
                   model_uri=CSOLINK.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]])

slots.has_procedure = Slot(uri=CSOLINK.has_procedure, name="has procedure", curie=CSOLINK.curie('has_procedure'),
                   model_uri=CSOLINK.has_procedure, domain=NamedThing, range=Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]])

slots.has_gateway = Slot(uri=CSOLINK.has_gateway, name="has gateway", curie=CSOLINK.curie('has_gateway'),
                   model_uri=CSOLINK.has_gateway, domain=None, range=Optional[Union[str, SystemicEntityId]])

slots.has_stressor = Slot(uri=CSOLINK.has_stressor, name="has stressor", curie=CSOLINK.curie('has_stressor'),
                   model_uri=CSOLINK.has_stressor, domain=None, range=Optional[str])

slots.has_route = Slot(uri=CSOLINK.has_route, name="has route", curie=CSOLINK.curie('has_route'),
                   model_uri=CSOLINK.has_route, domain=None, range=Optional[str])

slots.has_population_context = Slot(uri=CSOLINK.has_population_context, name="has population context", curie=CSOLINK.curie('has_population_context'),
                   model_uri=CSOLINK.has_population_context, domain=Association, range=Optional[Union[str, PopulationOfIndividualSystemsId]])

slots.has_temporal_context = Slot(uri=CSOLINK.has_temporal_context, name="has temporal context", curie=CSOLINK.curie('has_temporal_context'),
                   model_uri=CSOLINK.has_temporal_context, domain=Association, range=Optional[Union[str, TimeType]])

slots.related_to = Slot(uri=CSOLINK.related_to, name="related to", curie=CSOLINK.curie('related_to'),
                   model_uri=CSOLINK.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.superclass_of = Slot(uri=CSOLINK.superclass_of, name="superclass of", curie=CSOLINK.curie('superclass_of'),
                   model_uri=CSOLINK.superclass_of, domain=OntologyClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass of", curie=RDFS.curie('subClassOf'),
                   model_uri=CSOLINK.subclass_of, domain=OntologyClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.same_as = Slot(uri=CSOLINK.same_as, name="same as", curie=CSOLINK.curie('same_as'),
                   model_uri=CSOLINK.same_as, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.close_match = Slot(uri=CSOLINK.close_match, name="close match", curie=CSOLINK.curie('close_match'),
                   model_uri=CSOLINK.close_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.exact_match = Slot(uri=CSOLINK.exact_match, name="exact match", curie=CSOLINK.curie('exact_match'),
                   model_uri=CSOLINK.exact_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.broad_match = Slot(uri=CSOLINK.broad_match, name="broad match", curie=CSOLINK.curie('broad_match'),
                   model_uri=CSOLINK.broad_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.narrow_match = Slot(uri=CSOLINK.narrow_match, name="narrow match", curie=CSOLINK.curie('narrow_match'),
                   model_uri=CSOLINK.narrow_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=CSOLINK.contributor, name="contributor", curie=CSOLINK.curie('contributor'),
                   model_uri=CSOLINK.contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.provider = Slot(uri=CSOLINK.provider, name="provider", curie=CSOLINK.curie('provider'),
                   model_uri=CSOLINK.provider, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.publisher = Slot(uri=CSOLINK.publisher, name="publisher", curie=CSOLINK.curie('publisher'),
                   model_uri=CSOLINK.publisher, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.editor = Slot(uri=CSOLINK.editor, name="editor", curie=CSOLINK.curie('editor'),
                   model_uri=CSOLINK.editor, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.author = Slot(uri=CSOLINK.author, name="author", curie=CSOLINK.curie('author'),
                   model_uri=CSOLINK.author, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.interacts_with = Slot(uri=CSOLINK.interacts_with, name="interacts with", curie=CSOLINK.curie('interacts_with'),
                   model_uri=CSOLINK.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.cyber_interaction_with = Slot(uri=CSOLINK.cyber_interaction_with, name="cyber interaction with", curie=CSOLINK.curie('cyber_interaction_with'),
                   model_uri=CSOLINK.cyber_interaction_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.operationally_interacts_with = Slot(uri=CSOLINK.operationally_interacts_with, name="operationally interacts with", curie=CSOLINK.curie('operationally_interacts_with'),
                   model_uri=CSOLINK.operationally_interacts_with, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.service_interacts_with = Slot(uri=CSOLINK.service_interacts_with, name="service interacts with", curie=CSOLINK.curie('service_interacts_with'),
                   model_uri=CSOLINK.service_interacts_with, domain=Componentservice, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.affects = Slot(uri=CSOLINK.affects, name="affects", curie=CSOLINK.curie('affects'),
                   model_uri=CSOLINK.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=CSOLINK.affected_by, name="affected by", curie=CSOLINK.curie('affected_by'),
                   model_uri=CSOLINK.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.control_role_mixin = Slot(uri=CSOLINK.control_role_mixin, name="control role mixin", curie=CSOLINK.curie('control_role_mixin'),
                   model_uri=CSOLINK.control_role_mixin, domain=None, range=Optional[str])

slots.computational_role_mixin = Slot(uri=CSOLINK.computational_role_mixin, name="computational role mixin", curie=CSOLINK.curie('computational_role_mixin'),
                   model_uri=CSOLINK.computational_role_mixin, domain=None, range=Optional[str])

slots.affects_abundance_of = Slot(uri=CSOLINK.affects_abundance_of, name="affects abundance of", curie=CSOLINK.curie('affects_abundance_of'),
                   model_uri=CSOLINK.affects_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_abundance_of = Slot(uri=CSOLINK.increases_abundance_of, name="increases abundance of", curie=CSOLINK.curie('increases_abundance_of'),
                   model_uri=CSOLINK.increases_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_abundance_of = Slot(uri=CSOLINK.decreases_abundance_of, name="decreases abundance of", curie=CSOLINK.curie('decreases_abundance_of'),
                   model_uri=CSOLINK.decreases_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_activity_of = Slot(uri=CSOLINK.affects_activity_of, name="affects activity of", curie=CSOLINK.curie('affects_activity_of'),
                   model_uri=CSOLINK.affects_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_activity_of = Slot(uri=CSOLINK.increases_activity_of, name="increases activity of", curie=CSOLINK.curie('increases_activity_of'),
                   model_uri=CSOLINK.increases_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_activity_of = Slot(uri=CSOLINK.decreases_activity_of, name="decreases activity of", curie=CSOLINK.curie('decreases_activity_of'),
                   model_uri=CSOLINK.decreases_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_availability_of = Slot(uri=CSOLINK.affects_availability_of, name="affects availability of", curie=CSOLINK.curie('affects_availability_of'),
                   model_uri=CSOLINK.affects_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.increases_availability_of = Slot(uri=CSOLINK.increases_availability_of, name="increases availability of", curie=CSOLINK.curie('increases_availability_of'),
                   model_uri=CSOLINK.increases_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.decreases_availability_of = Slot(uri=CSOLINK.decreases_availability_of, name="decreases availability of", curie=CSOLINK.curie('decreases_availability_of'),
                   model_uri=CSOLINK.decreases_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.affects_assignment_of = Slot(uri=CSOLINK.affects_assignment_of, name="affects assignment of", curie=CSOLINK.curie('affects_assignment_of'),
                   model_uri=CSOLINK.affects_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_assignment_of = Slot(uri=CSOLINK.increases_assignment_of, name="increases assignment of", curie=CSOLINK.curie('increases_assignment_of'),
                   model_uri=CSOLINK.increases_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_assignment_of = Slot(uri=CSOLINK.decreases_assignment_of, name="decreases assignment of", curie=CSOLINK.curie('decreases_assignment_of'),
                   model_uri=CSOLINK.decreases_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_localization_of = Slot(uri=CSOLINK.affects_localization_of, name="affects localization of", curie=CSOLINK.curie('affects_localization_of'),
                   model_uri=CSOLINK.affects_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_localization_of = Slot(uri=CSOLINK.increases_localization_of, name="increases localization of", curie=CSOLINK.curie('increases_localization_of'),
                   model_uri=CSOLINK.increases_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_localization_of = Slot(uri=CSOLINK.decreases_localization_of, name="decreases localization of", curie=CSOLINK.curie('decreases_localization_of'),
                   model_uri=CSOLINK.decreases_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_supervision_of = Slot(uri=CSOLINK.affects_supervision_of, name="affects supervision of", curie=CSOLINK.curie('affects_supervision_of'),
                   model_uri=CSOLINK.affects_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_supervision_of = Slot(uri=CSOLINK.increases_supervision_of, name="increases supervision of", curie=CSOLINK.curie('increases_supervision_of'),
                   model_uri=CSOLINK.increases_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_supervision_of = Slot(uri=CSOLINK.decreases_supervision_of, name="decreases supervision of", curie=CSOLINK.curie('decreases_supervision_of'),
                   model_uri=CSOLINK.decreases_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_operational_modification_of = Slot(uri=CSOLINK.affects_operational_modification_of, name="affects operational modification of", curie=CSOLINK.curie('affects_operational_modification_of'),
                   model_uri=CSOLINK.affects_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_operational_modification_of = Slot(uri=CSOLINK.increases_operational_modification_of, name="increases operational modification of", curie=CSOLINK.curie('increases_operational_modification_of'),
                   model_uri=CSOLINK.increases_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_operational_modification_of = Slot(uri=CSOLINK.decreases_operational_modification_of, name="decreases operational modification of", curie=CSOLINK.curie('decreases_operational_modification_of'),
                   model_uri=CSOLINK.decreases_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_instantiation_of = Slot(uri=CSOLINK.affects_instantiation_of, name="affects instantiation of", curie=CSOLINK.curie('affects_instantiation_of'),
                   model_uri=CSOLINK.affects_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_instantiation_of = Slot(uri=CSOLINK.increases_instantiation_of, name="increases instantiation of", curie=CSOLINK.curie('increases_instantiation_of'),
                   model_uri=CSOLINK.increases_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_instantiation_of = Slot(uri=CSOLINK.decreases_instantiation_of, name="decreases instantiation of", curie=CSOLINK.curie('decreases_instantiation_of'),
                   model_uri=CSOLINK.decreases_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_degradation_of = Slot(uri=CSOLINK.affects_degradation_of, name="affects degradation of", curie=CSOLINK.curie('affects_degradation_of'),
                   model_uri=CSOLINK.affects_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_degradation_of = Slot(uri=CSOLINK.increases_degradation_of, name="increases degradation of", curie=CSOLINK.curie('increases_degradation_of'),
                   model_uri=CSOLINK.increases_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_degradation_of = Slot(uri=CSOLINK.decreases_degradation_of, name="decreases degradation of", curie=CSOLINK.curie('decreases_degradation_of'),
                   model_uri=CSOLINK.decreases_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_updates_rate_of = Slot(uri=CSOLINK.affects_updates_rate_of, name="affects updates rate of", curie=CSOLINK.curie('affects_updates_rate_of'),
                   model_uri=CSOLINK.affects_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.increases_updates_rate_of = Slot(uri=CSOLINK.increases_updates_rate_of, name="increases updates rate of", curie=CSOLINK.curie('increases_updates_rate_of'),
                   model_uri=CSOLINK.increases_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.decreases_updates_rate_of = Slot(uri=CSOLINK.decreases_updates_rate_of, name="decreases updates rate of", curie=CSOLINK.curie('decreases_updates_rate_of'),
                   model_uri=CSOLINK.decreases_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.affects_response_to = Slot(uri=CSOLINK.affects_response_to, name="affects response to", curie=CSOLINK.curie('affects_response_to'),
                   model_uri=CSOLINK.affects_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_response_to = Slot(uri=CSOLINK.increases_response_to, name="increases response to", curie=CSOLINK.curie('increases_response_to'),
                   model_uri=CSOLINK.increases_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_response_to = Slot(uri=CSOLINK.decreases_response_to, name="decreases response to", curie=CSOLINK.curie('decreases_response_to'),
                   model_uri=CSOLINK.decreases_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_splicing_of = Slot(uri=CSOLINK.affects_splicing_of, name="affects splicing of", curie=CSOLINK.curie('affects_splicing_of'),
                   model_uri=CSOLINK.affects_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.increases_splicing_of = Slot(uri=CSOLINK.increases_splicing_of, name="increases splicing of", curie=CSOLINK.curie('increases_splicing_of'),
                   model_uri=CSOLINK.increases_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.decreases_splicing_of = Slot(uri=CSOLINK.decreases_splicing_of, name="decreases splicing of", curie=CSOLINK.curie('decreases_splicing_of'),
                   model_uri=CSOLINK.decreases_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.affects_stability_of = Slot(uri=CSOLINK.affects_stability_of, name="affects stability of", curie=CSOLINK.curie('affects_stability_of'),
                   model_uri=CSOLINK.affects_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_stability_of = Slot(uri=CSOLINK.increases_stability_of, name="increases stability of", curie=CSOLINK.curie('increases_stability_of'),
                   model_uri=CSOLINK.increases_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_stability_of = Slot(uri=CSOLINK.decreases_stability_of, name="decreases stability of", curie=CSOLINK.curie('decreases_stability_of'),
                   model_uri=CSOLINK.decreases_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_transport_of = Slot(uri=CSOLINK.affects_transport_of, name="affects transport of", curie=CSOLINK.curie('affects_transport_of'),
                   model_uri=CSOLINK.affects_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_transport_of = Slot(uri=CSOLINK.increases_transport_of, name="increases transport of", curie=CSOLINK.curie('increases_transport_of'),
                   model_uri=CSOLINK.increases_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_transport_of = Slot(uri=CSOLINK.decreases_transport_of, name="decreases transport of", curie=CSOLINK.curie('decreases_transport_of'),
                   model_uri=CSOLINK.decreases_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_output_of = Slot(uri=CSOLINK.affects_output_of, name="affects output of", curie=CSOLINK.curie('affects_output_of'),
                   model_uri=CSOLINK.affects_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_output_of = Slot(uri=CSOLINK.increases_output_of, name="increases output of", curie=CSOLINK.curie('increases_output_of'),
                   model_uri=CSOLINK.increases_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_output_of = Slot(uri=CSOLINK.decreases_output_of, name="decreases output of", curie=CSOLINK.curie('decreases_output_of'),
                   model_uri=CSOLINK.decreases_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_uptake_of = Slot(uri=CSOLINK.affects_uptake_of, name="affects uptake of", curie=CSOLINK.curie('affects_uptake_of'),
                   model_uri=CSOLINK.affects_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_uptake_of = Slot(uri=CSOLINK.increases_uptake_of, name="increases uptake of", curie=CSOLINK.curie('increases_uptake_of'),
                   model_uri=CSOLINK.increases_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_uptake_of = Slot(uri=CSOLINK.decreases_uptake_of, name="decreases uptake of", curie=CSOLINK.curie('decreases_uptake_of'),
                   model_uri=CSOLINK.decreases_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.regulates = Slot(uri=CSOLINK.regulates, name="regulates", curie=CSOLINK.curie('regulates'),
                   model_uri=CSOLINK.regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.regulated_by = Slot(uri=CSOLINK.regulated_by, name="regulated by", curie=CSOLINK.curie('regulated_by'),
                   model_uri=CSOLINK.regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.positively_regulates = Slot(uri=CSOLINK.positively_regulates, name="positively regulates", curie=CSOLINK.curie('positively_regulates'),
                   model_uri=CSOLINK.positively_regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.positively_regulated_by = Slot(uri=CSOLINK.positively_regulated_by, name="positively regulated by", curie=CSOLINK.curie('positively_regulated_by'),
                   model_uri=CSOLINK.positively_regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.negatively_regulates = Slot(uri=CSOLINK.negatively_regulates, name="negatively regulates", curie=CSOLINK.curie('negatively_regulates'),
                   model_uri=CSOLINK.negatively_regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.negatively_regulated_by = Slot(uri=CSOLINK.negatively_regulated_by, name="negatively regulated by", curie=CSOLINK.curie('negatively_regulated_by'),
                   model_uri=CSOLINK.negatively_regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.regulates_process_to_process = Slot(uri=CSOLINK.regulates_process_to_process, name="regulates, process to process", curie=CSOLINK.curie('regulates_process_to_process'),
                   model_uri=CSOLINK.regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulated_by_process_to_process = Slot(uri=CSOLINK.regulated_by_process_to_process, name="regulated by, process to process", curie=CSOLINK.curie('regulated_by_process_to_process'),
                   model_uri=CSOLINK.regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulates_process_to_process = Slot(uri=CSOLINK.positively_regulates_process_to_process, name="positively regulates, process to process", curie=CSOLINK.curie('positively_regulates_process_to_process'),
                   model_uri=CSOLINK.positively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulated_by_process_to_process = Slot(uri=CSOLINK.positively_regulated_by_process_to_process, name="positively regulated by, process to process", curie=CSOLINK.curie('positively_regulated_by_process_to_process'),
                   model_uri=CSOLINK.positively_regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulates_process_to_process = Slot(uri=CSOLINK.negatively_regulates_process_to_process, name="negatively regulates, process to process", curie=CSOLINK.curie('negatively_regulates_process_to_process'),
                   model_uri=CSOLINK.negatively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulated_by_process_to_process = Slot(uri=CSOLINK.negatively_regulated_by_process_to_process, name="negatively regulated by, process to process", curie=CSOLINK.curie('negatively_regulated_by_process_to_process'),
                   model_uri=CSOLINK.negatively_regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulates_entity_to_entity = Slot(uri=CSOLINK.regulates_entity_to_entity, name="regulates, entity to entity", curie=CSOLINK.curie('regulates_entity_to_entity'),
                   model_uri=CSOLINK.regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.regulated_by_entity_to_entity = Slot(uri=CSOLINK.regulated_by_entity_to_entity, name="regulated by, entity to entity", curie=CSOLINK.curie('regulated_by_entity_to_entity'),
                   model_uri=CSOLINK.regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.positively_regulates_entity_to_entity = Slot(uri=CSOLINK.positively_regulates_entity_to_entity, name="positively regulates, entity to entity", curie=CSOLINK.curie('positively_regulates_entity_to_entity'),
                   model_uri=CSOLINK.positively_regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.positively_regulated_by_entity_to_entity = Slot(uri=CSOLINK.positively_regulated_by_entity_to_entity, name="positively regulated by, entity to entity", curie=CSOLINK.curie('positively_regulated_by_entity_to_entity'),
                   model_uri=CSOLINK.positively_regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.negatively_regulates_entity_to_entity = Slot(uri=CSOLINK.negatively_regulates_entity_to_entity, name="negatively regulates, entity to entity", curie=CSOLINK.curie('negatively_regulates_entity_to_entity'),
                   model_uri=CSOLINK.negatively_regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.negatively_regulated_by_entity_to_entity = Slot(uri=CSOLINK.negatively_regulated_by_entity_to_entity, name="negatively regulated by, entity to entity", curie=CSOLINK.curie('negatively_regulated_by_entity_to_entity'),
                   model_uri=CSOLINK.negatively_regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.disrupts = Slot(uri=CSOLINK.disrupts, name="disrupts", curie=CSOLINK.curie('disrupts'),
                   model_uri=CSOLINK.disrupts, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.disrupted_by = Slot(uri=CSOLINK.disrupted_by, name="disrupted by", curie=CSOLINK.curie('disrupted_by'),
                   model_uri=CSOLINK.disrupted_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_servicetype = Slot(uri=CSOLINK.has_servicetype, name="has servicetype", curie=CSOLINK.curie('has_servicetype'),
                   model_uri=CSOLINK.has_servicetype, domain=Componentservice, range=Optional[Union[Union[dict, "ServicetypeMixin"], List[Union[dict, "ServicetypeMixin"]]]])

slots.homologous_to = Slot(uri=CSOLINK.homologous_to, name="homologous to", curie=CSOLINK.curie('homologous_to'),
                   model_uri=CSOLINK.homologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.paralogous_to = Slot(uri=CSOLINK.paralogous_to, name="paralogous to", curie=CSOLINK.curie('paralogous_to'),
                   model_uri=CSOLINK.paralogous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.orthologous_to = Slot(uri=CSOLINK.orthologous_to, name="orthologous to", curie=CSOLINK.curie('orthologous_to'),
                   model_uri=CSOLINK.orthologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.xenologous_to = Slot(uri=CSOLINK.xenologous_to, name="xenologous to", curie=CSOLINK.curie('xenologous_to'),
                   model_uri=CSOLINK.xenologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coexists_with = Slot(uri=CSOLINK.coexists_with, name="coexists with", curie=CSOLINK.curie('coexists_with'),
                   model_uri=CSOLINK.coexists_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_pathway_with = Slot(uri=CSOLINK.in_pathway_with, name="in pathway with", curie=CSOLINK.curie('in_pathway_with'),
                   model_uri=CSOLINK.in_pathway_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.in_complex_with = Slot(uri=CSOLINK.in_complex_with, name="in complex with", curie=CSOLINK.curie('in_complex_with'),
                   model_uri=CSOLINK.in_complex_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.in_serviceunit_population_with = Slot(uri=CSOLINK.in_serviceunit_population_with, name="in serviceunit population with", curie=CSOLINK.curie('in_serviceunit_population_with'),
                   model_uri=CSOLINK.in_serviceunit_population_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.colocalizes_with = Slot(uri=CSOLINK.colocalizes_with, name="colocalizes with", curie=CSOLINK.curie('colocalizes_with'),
                   model_uri=CSOLINK.colocalizes_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.service_association = Slot(uri=CSOLINK.service_association, name="service association", curie=CSOLINK.curie('service_association'),
                   model_uri=CSOLINK.service_association, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.componentservice_associated_with_condition = Slot(uri=CSOLINK.componentservice_associated_with_condition, name="componentservice associated with condition", curie=CSOLINK.curie('componentservice_associated_with_condition'),
                   model_uri=CSOLINK.componentservice_associated_with_condition, domain=Componentservice, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.condition_associated_with_componentservice = Slot(uri=CSOLINK.condition_associated_with_componentservice, name="condition associated with componentservice", curie=CSOLINK.curie('condition_associated_with_componentservice'),
                   model_uri=CSOLINK.condition_associated_with_componentservice, domain=ErrorOrObservableFeature, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.affects_risk_for = Slot(uri=CSOLINK.affects_risk_for, name="affects risk for", curie=CSOLINK.curie('affects_risk_for'),
                   model_uri=CSOLINK.affects_risk_for, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.predisposes = Slot(uri=CSOLINK.predisposes, name="predisposes", curie=CSOLINK.curie('predisposes'),
                   model_uri=CSOLINK.predisposes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributes_to = Slot(uri=CSOLINK.contributes_to, name="contributes to", curie=CSOLINK.curie('contributes_to'),
                   model_uri=CSOLINK.contributes_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes = Slot(uri=CSOLINK.causes, name="causes", curie=CSOLINK.curie('causes'),
                   model_uri=CSOLINK.causes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.caused_by = Slot(uri=CSOLINK.caused_by, name="caused by", curie=CSOLINK.curie('caused_by'),
                   model_uri=CSOLINK.caused_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.ameliorates = Slot(uri=CSOLINK.ameliorates, name="ameliorates", curie=CSOLINK.curie('ameliorates'),
                   model_uri=CSOLINK.ameliorates, domain=ComputationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.exacerbates = Slot(uri=CSOLINK.exacerbates, name="exacerbates", curie=CSOLINK.curie('exacerbates'),
                   model_uri=CSOLINK.exacerbates, domain=ComputationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.repairs = Slot(uri=CSOLINK.repairs, name="repairs", curie=CSOLINK.curie('repairs'),
                   model_uri=CSOLINK.repairs, domain=Repairing, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.repaired_by = Slot(uri=CSOLINK.repaired_by, name="repaired by", curie=CSOLINK.curie('repaired_by'),
                   model_uri=CSOLINK.repaired_by, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, RepairingId], List[Union[str, RepairingId]]]])

slots.approved_to_repair = Slot(uri=CSOLINK.approved_to_repair, name="approved to repair", curie=CSOLINK.curie('approved_to_repair'),
                   model_uri=CSOLINK.approved_to_repair, domain=Repairing, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.approved_for_repairing_by = Slot(uri=CSOLINK.approved_for_repairing_by, name="approved for repairing by", curie=CSOLINK.curie('approved_for_repairing_by'),
                   model_uri=CSOLINK.approved_for_repairing_by, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, RepairingId], List[Union[str, RepairingId]]]])

slots.prevents = Slot(uri=CSOLINK.prevents, name="prevents", curie=CSOLINK.curie('prevents'),
                   model_uri=CSOLINK.prevents, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.prevented_by = Slot(uri=CSOLINK.prevented_by, name="prevented by", curie=CSOLINK.curie('prevented_by'),
                   model_uri=CSOLINK.prevented_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.correlated_with = Slot(uri=CSOLINK.correlated_with, name="correlated with", curie=CSOLINK.curie('correlated_with'),
                   model_uri=CSOLINK.correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.positively_correlated_with = Slot(uri=CSOLINK.positively_correlated_with, name="positively correlated with", curie=CSOLINK.curie('positively_correlated_with'),
                   model_uri=CSOLINK.positively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.negatively_correlated_with = Slot(uri=CSOLINK.negatively_correlated_with, name="negatively correlated with", curie=CSOLINK.curie('negatively_correlated_with'),
                   model_uri=CSOLINK.negatively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coavailable_with = Slot(uri=CSOLINK.coavailable_with, name="coavailable with", curie=CSOLINK.curie('coavailable_with'),
                   model_uri=CSOLINK.coavailable_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.has_marker = Slot(uri=CSOLINK.has_marker, name="has marker", curie=CSOLINK.curie('has_marker'),
                   model_uri=CSOLINK.has_marker, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.marker_for = Slot(uri=CSOLINK.marker_for, name="marker for", curie=CSOLINK.curie('marker_for'),
                   model_uri=CSOLINK.marker_for, domain=OperationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.available_in = Slot(uri=CSOLINK.available_in, name="available in", curie=CSOLINK.curie('available_in'),
                   model_uri=CSOLINK.available_in, domain=None, range=Optional[Union[Union[str, DeploymentEntityId], List[Union[str, DeploymentEntityId]]]])

slots.unavailable_in = Slot(uri=CSOLINK.unavailable_in, name="unavailable in", curie=CSOLINK.curie('unavailable_in'),
                   model_uri=CSOLINK.unavailable_in, domain=DeploymentEntity, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.has_observability = Slot(uri=CSOLINK.has_observability, name="has observability", curie=CSOLINK.curie('has_observability'),
                   model_uri=CSOLINK.has_observability, domain=ComputationalEntity, range=Optional[Union[Union[str, ObservableFeatureId], List[Union[str, ObservableFeatureId]]]])

slots.occurs_in = Slot(uri=CSOLINK.occurs_in, name="occurs in", curie=CSOLINK.curie('occurs_in'),
                   model_uri=CSOLINK.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=CSOLINK.located_in, name="located in", curie=CSOLINK.curie('located_in'),
                   model_uri=CSOLINK.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=CSOLINK.location_of, name="location of", curie=CSOLINK.curie('location_of'),
                   model_uri=CSOLINK.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=CSOLINK.similar_to, name="similar to", curie=CSOLINK.curie('similar_to'),
                   model_uri=CSOLINK.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.orchestrationly_similar_to = Slot(uri=CSOLINK.orchestrationly_similar_to, name="orchestrationly similar to", curie=CSOLINK.curie('orchestrationly_similar_to'),
                   model_uri=CSOLINK.orchestrationly_similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_sequence_location = Slot(uri=CSOLINK.has_sequence_location, name="has sequence location", curie=CSOLINK.curie('has_sequence_location'),
                   model_uri=CSOLINK.has_sequence_location, domain=WorkloadEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.model_of = Slot(uri=CSOLINK.model_of, name="model of", curie=CSOLINK.curie('model_of'),
                   model_uri=CSOLINK.model_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.overlaps = Slot(uri=CSOLINK.overlaps, name="overlaps", curie=CSOLINK.curie('overlaps'),
                   model_uri=CSOLINK.overlaps, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_part = Slot(uri=CSOLINK.has_part, name="has part", curie=CSOLINK.curie('has_part'),
                   model_uri=CSOLINK.has_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=CSOLINK.part_of, name="part of", curie=CSOLINK.curie('part_of'),
                   model_uri=CSOLINK.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_input = Slot(uri=CSOLINK.has_input, name="has input", curie=CSOLINK.curie('has_input'),
                   model_uri=CSOLINK.has_input, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=CSOLINK.has_output, name="has output", curie=CSOLINK.curie('has_output'),
                   model_uri=CSOLINK.has_output, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_participant = Slot(uri=CSOLINK.has_participant, name="has participant", curie=CSOLINK.curie('has_participant'),
                   model_uri=CSOLINK.has_participant, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.participates_in = Slot(uri=CSOLINK.participates_in, name="participates in", curie=CSOLINK.curie('participates_in'),
                   model_uri=CSOLINK.participates_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.actively_involved_in = Slot(uri=CSOLINK.actively_involved_in, name="actively involved in", curie=CSOLINK.curie('actively_involved_in'),
                   model_uri=CSOLINK.actively_involved_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.capable_of = Slot(uri=CSOLINK.capable_of, name="capable of", curie=CSOLINK.curie('capable_of'),
                   model_uri=CSOLINK.capable_of, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.enables = Slot(uri=CSOLINK.enables, name="enables", curie=CSOLINK.curie('enables'),
                   model_uri=CSOLINK.enables, domain=CyberEntity, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=CSOLINK.enabled_by, name="enabled by", curie=CSOLINK.curie('enabled_by'),
                   model_uri=CSOLINK.enabled_by, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]])

slots.derives_into = Slot(uri=CSOLINK.derives_into, name="derives into", curie=CSOLINK.curie('derives_into'),
                   model_uri=CSOLINK.derives_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.derives_from = Slot(uri=CSOLINK.derives_from, name="derives from", curie=CSOLINK.curie('derives_from'),
                   model_uri=CSOLINK.derives_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_controller_of = Slot(uri=CSOLINK.is_controller_of, name="is controller of", curie=CSOLINK.curie('is_controller_of'),
                   model_uri=CSOLINK.is_controller_of, domain=ControlActor, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.has_controller = Slot(uri=CSOLINK.has_controller, name="has controller", curie=CSOLINK.curie('has_controller'),
                   model_uri=CSOLINK.has_controller, domain=ControlActor, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.notification_component_of = Slot(uri=CSOLINK.notification_component_of, name="notification component of", curie=CSOLINK.curie('notification_component_of'),
                   model_uri=CSOLINK.notification_component_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_notification_component = Slot(uri=CSOLINK.has_notification_component, name="has notification component", curie=CSOLINK.curie('has_notification_component'),
                   model_uri=CSOLINK.has_notification_component, domain=Notification, range=Optional[Union[Union[str, NotificationComponentId], List[Union[str, NotificationComponentId]]]])

slots.data_of = Slot(uri=CSOLINK.data_of, name="data of", curie=CSOLINK.curie('data_of'),
                   model_uri=CSOLINK.data_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_data = Slot(uri=CSOLINK.has_data, name="has data", curie=CSOLINK.curie('has_data'),
                   model_uri=CSOLINK.has_data, domain=Notification, range=Optional[Union[Union[str, DataId], List[Union[str, DataId]]]])

slots.is_active_ingredient_of = Slot(uri=CSOLINK.is_active_ingredient_of, name="is active ingredient of", curie=CSOLINK.curie('is_active_ingredient_of'),
                   model_uri=CSOLINK.is_active_ingredient_of, domain=ControlActor, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [RO["0002249"]])

slots.has_active_ingredient = Slot(uri=CSOLINK.has_active_ingredient, name="has active ingredient", curie=CSOLINK.curie('has_active_ingredient'),
                   model_uri=CSOLINK.has_active_ingredient, domain=AdministrativeOperation, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]], mappings = [RO["0002248"]])

slots.is_excipient_of = Slot(uri=CSOLINK.is_excipient_of, name="is excipient of", curie=CSOLINK.curie('is_excipient_of'),
                   model_uri=CSOLINK.is_excipient_of, domain=ControlActor, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [WIKIDATA.Q902638])

slots.has_excipient = Slot(uri=CSOLINK.has_excipient, name="has excipient", curie=CSOLINK.curie('has_excipient'),
                   model_uri=CSOLINK.has_excipient, domain=AdministrativeOperation, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]], mappings = [WIKIDATA.Q902638])

slots.manifestation_of = Slot(uri=CSOLINK.manifestation_of, name="manifestation of", curie=CSOLINK.curie('manifestation_of'),
                   model_uri=CSOLINK.manifestation_of, domain=NamedThing, range=Optional[Union[Union[str, ErrorId], List[Union[str, ErrorId]]]])

slots.produces = Slot(uri=CSOLINK.produces, name="produces", curie=CSOLINK.curie('produces'),
                   model_uri=CSOLINK.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=CSOLINK.produced_by, name="produced by", curie=CSOLINK.curie('produced_by'),
                   model_uri=CSOLINK.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.temporally_related_to = Slot(uri=CSOLINK.temporally_related_to, name="temporally related to", curie=CSOLINK.curie('temporally_related_to'),
                   model_uri=CSOLINK.temporally_related_to, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.precedes = Slot(uri=CSOLINK.precedes, name="precedes", curie=CSOLINK.curie('precedes'),
                   model_uri=CSOLINK.precedes, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.preceded_by = Slot(uri=CSOLINK.preceded_by, name="preceded by", curie=CSOLINK.curie('preceded_by'),
                   model_uri=CSOLINK.preceded_by, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.directly_interacts_with = Slot(uri=CSOLINK.directly_interacts_with, name="directly interacts with", curie=CSOLINK.curie('directly_interacts_with'),
                   model_uri=CSOLINK.directly_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affects_availability_in = Slot(uri=CSOLINK.affects_availability_in, name="affects availability in", curie=CSOLINK.curie('affects_availability_in'),
                   model_uri=CSOLINK.affects_availability_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_variant_part = Slot(uri=CSOLINK.has_variant_part, name="has variant part", curie=CSOLINK.curie('has_variant_part'),
                   model_uri=CSOLINK.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=CSOLINK.related_condition, name="related condition", curie=CSOLINK.curie('related_condition'),
                   model_uri=CSOLINK.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_sequence_variant_of = Slot(uri=CSOLINK.is_sequence_variant_of, name="is sequence variant of", curie=CSOLINK.curie('is_sequence_variant_of'),
                   model_uri=CSOLINK.is_sequence_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.is_missense_variant_of = Slot(uri=CSOLINK.is_missense_variant_of, name="is missense variant of", curie=CSOLINK.curie('is_missense_variant_of'),
                   model_uri=CSOLINK.is_missense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_synonymous_variant_of = Slot(uri=CSOLINK.is_synonymous_variant_of, name="is synonymous variant of", curie=CSOLINK.curie('is_synonymous_variant_of'),
                   model_uri=CSOLINK.is_synonymous_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_nonsense_variant_of = Slot(uri=CSOLINK.is_nonsense_variant_of, name="is nonsense variant of", curie=CSOLINK.curie('is_nonsense_variant_of'),
                   model_uri=CSOLINK.is_nonsense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_protocol_variant_of = Slot(uri=CSOLINK.is_protocol_variant_of, name="is protocol variant of", curie=CSOLINK.curie('is_protocol_variant_of'),
                   model_uri=CSOLINK.is_protocol_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_splice_site_variant_of = Slot(uri=CSOLINK.is_splice_site_variant_of, name="is splice site variant of", curie=CSOLINK.curie('is_splice_site_variant_of'),
                   model_uri=CSOLINK.is_splice_site_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_nearby_variant_of = Slot(uri=CSOLINK.is_nearby_variant_of, name="is nearby variant of", curie=CSOLINK.curie('is_nearby_variant_of'),
                   model_uri=CSOLINK.is_nearby_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_non_coding_variant_of = Slot(uri=CSOLINK.is_non_coding_variant_of, name="is non coding variant of", curie=CSOLINK.curie('is_non_coding_variant_of'),
                   model_uri=CSOLINK.is_non_coding_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.error_has_basis_in = Slot(uri=CSOLINK.error_has_basis_in, name="error has basis in", curie=CSOLINK.curie('error_has_basis_in'),
                   model_uri=CSOLINK.error_has_basis_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes_adverse_event = Slot(uri=CSOLINK.causes_adverse_event, name="causes adverse event", curie=CSOLINK.curie('causes_adverse_event'),
                   model_uri=CSOLINK.causes_adverse_event, domain=AdministrativeOperation, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.contraindicated_for = Slot(uri=CSOLINK.contraindicated_for, name="contraindicated for", curie=CSOLINK.curie('contraindicated_for'),
                   model_uri=CSOLINK.contraindicated_for, domain=AdministrativeOperation, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.has_not_completed = Slot(uri=CSOLINK.has_not_completed, name="has not completed", curie=CSOLINK.curie('has_not_completed'),
                   model_uri=CSOLINK.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=CSOLINK.has_completed, name="has completed", curie=CSOLINK.curie('has_completed'),
                   model_uri=CSOLINK.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreases_operational_interaction = Slot(uri=CSOLINK.decreases_operational_interaction, name="decreases operational interaction", curie=CSOLINK.curie('decreases_operational_interaction'),
                   model_uri=CSOLINK.decreases_operational_interaction, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_operational_interaction = Slot(uri=CSOLINK.increases_operational_interaction, name="increases operational interaction", curie=CSOLINK.curie('increases_operational_interaction'),
                   model_uri=CSOLINK.increases_operational_interaction, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.in_linkage_disequilibrium_with = Slot(uri=CSOLINK.in_linkage_disequilibrium_with, name="in linkage disequilibrium with", curie=CSOLINK.curie('in_linkage_disequilibrium_with'),
                   model_uri=CSOLINK.in_linkage_disequilibrium_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_increased_amount = Slot(uri=CSOLINK.has_increased_amount, name="has increased amount", curie=CSOLINK.curie('has_increased_amount'),
                   model_uri=CSOLINK.has_increased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_decreased_amount = Slot(uri=CSOLINK.has_decreased_amount, name="has decreased amount", curie=CSOLINK.curie('has_decreased_amount'),
                   model_uri=CSOLINK.has_decreased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.lacks_part = Slot(uri=CSOLINK.lacks_part, name="lacks part", curie=CSOLINK.curie('lacks_part'),
                   model_uri=CSOLINK.lacks_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.develops_from = Slot(uri=CSOLINK.develops_from, name="develops from", curie=CSOLINK.curie('develops_from'),
                   model_uri=CSOLINK.develops_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=CSOLINK.in_taxon, name="in taxon", curie=CSOLINK.curie('in_taxon'),
                   model_uri=CSOLINK.in_taxon, domain=None, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.has_operational_consequence = Slot(uri=CSOLINK.has_operational_consequence, name="has operational consequence", curie=CSOLINK.curie('has_operational_consequence'),
                   model_uri=CSOLINK.has_operational_consequence, domain=NamedThing, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.association_slot = Slot(uri=CSOLINK.association_slot, name="association slot", curie=CSOLINK.curie('association_slot'),
                   model_uri=CSOLINK.association_slot, domain=Association, range=Optional[str])

slots.association_id = Slot(uri=CSOLINK.id, name="association_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.association_id, domain=Association, range=Union[str, AssociationId])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=CSOLINK.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=CSOLINK.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=CSOLINK.predicate, domain=Association, range=Union[str, PredicateType])

slots.edge_label = Slot(uri=RDF.predicate, name="edge label", curie=RDF.curie('predicate'),
                   model_uri=CSOLINK.edge_label, domain=Association, range=Union[str, PredicateType])

slots.relation = Slot(uri=CSOLINK.relation, name="relation", curie=CSOLINK.curie('relation'),
                   model_uri=CSOLINK.relation, domain=Association, range=Union[str, URIorCURIE])

slots.negated = Slot(uri=CSOLINK.negated, name="negated", curie=CSOLINK.curie('negated'),
                   model_uri=CSOLINK.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_confidence_level = Slot(uri=CSOLINK.has_confidence_level, name="has confidence level", curie=CSOLINK.curie('has_confidence_level'),
                   model_uri=CSOLINK.has_confidence_level, domain=Association, range=Optional[Union[str, ConfidenceLevelId]])

slots.has_evidence = Slot(uri=CSOLINK.has_evidence, name="has evidence", curie=CSOLINK.curie('has_evidence'),
                   model_uri=CSOLINK.has_evidence, domain=Association, range=Optional[Union[str, EvidenceTypeId]])

slots.provided_by = Slot(uri=CSOLINK.provided_by, name="provided by", curie=CSOLINK.curie('provided_by'),
                   model_uri=CSOLINK.provided_by, domain=Association, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.association_type = Slot(uri=CSOLINK.association_type, name="association type", curie=CSOLINK.curie('association_type'),
                   model_uri=CSOLINK.association_type, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.chi_squared_statistic = Slot(uri=CSOLINK.chi_squared_statistic, name="chi squared statistic", curie=CSOLINK.curie('chi_squared_statistic'),
                   model_uri=CSOLINK.chi_squared_statistic, domain=Association, range=Optional[float])

slots.p_value = Slot(uri=CSOLINK.p_value, name="p value", curie=CSOLINK.curie('p_value'),
                   model_uri=CSOLINK.p_value, domain=Association, range=Optional[float])

slots.interacting_tasks_category = Slot(uri=CSOLINK.interacting_tasks_category, name="interacting tasks category", curie=CSOLINK.curie('interacting_tasks_category'),
                   model_uri=CSOLINK.interacting_tasks_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.quantifier_qualifier = Slot(uri=CSOLINK.quantifier_qualifier, name="quantifier qualifier", curie=CSOLINK.curie('quantifier_qualifier'),
                   model_uri=CSOLINK.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.catalyst_qualifier = Slot(uri=CSOLINK.catalyst_qualifier, name="catalyst qualifier", curie=CSOLINK.curie('catalyst_qualifier'),
                   model_uri=CSOLINK.catalyst_qualifier, domain=Association, range=Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]])

slots.availability_site = Slot(uri=CSOLINK.availability_site, name="availability site", curie=CSOLINK.curie('availability_site'),
                   model_uri=CSOLINK.availability_site, domain=Association, range=Optional[Union[str, DeploymentEntityId]])

slots.stage_qualifier = Slot(uri=CSOLINK.stage_qualifier, name="stage qualifier", curie=CSOLINK.curie('stage_qualifier'),
                   model_uri=CSOLINK.stage_qualifier, domain=Association, range=Optional[Union[str, LifecycleStageId]])

slots.observable_state = Slot(uri=CSOLINK.observable_state, name="observable state", curie=CSOLINK.curie('observable_state'),
                   model_uri=CSOLINK.observable_state, domain=Association, range=Optional[Union[str, ErrorOrObservableFeatureId]])

slots.qualifiers = Slot(uri=CSOLINK.qualifiers, name="qualifiers", curie=CSOLINK.curie('qualifiers'),
                   model_uri=CSOLINK.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=CSOLINK.frequency_qualifier, name="frequency qualifier", curie=CSOLINK.curie('frequency_qualifier'),
                   model_uri=CSOLINK.frequency_qualifier, domain=Association, range=Optional[Union[dict, FrequencyValue]])

slots.severity_qualifier = Slot(uri=CSOLINK.severity_qualifier, name="severity qualifier", curie=CSOLINK.curie('severity_qualifier'),
                   model_uri=CSOLINK.severity_qualifier, domain=Association, range=Optional[Union[dict, SeverityValue]])

slots.architectural_style_qualifier = Slot(uri=CSOLINK.architectural_style_qualifier, name="architectural style qualifier", curie=CSOLINK.curie('architectural_style_qualifier'),
                   model_uri=CSOLINK.architectural_style_qualifier, domain=Association, range=Optional[Union[dict, ComputationalArchitecturalStyle]])

slots.onset_qualifier = Slot(uri=CSOLINK.onset_qualifier, name="onset qualifier", curie=CSOLINK.curie('onset_qualifier'),
                   model_uri=CSOLINK.onset_qualifier, domain=Association, range=Optional[Union[dict, Onset]])

slots.empirical_modifier_qualifier = Slot(uri=CSOLINK.empirical_modifier_qualifier, name="empirical modifier qualifier", curie=CSOLINK.curie('empirical_modifier_qualifier'),
                   model_uri=CSOLINK.empirical_modifier_qualifier, domain=Association, range=Optional[Union[dict, EmpiricalModifier]])

slots.sequence_variant_qualifier = Slot(uri=CSOLINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=CSOLINK.curie('sequence_variant_qualifier'),
                   model_uri=CSOLINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[str, SequenceVariantId]])

slots.publications = Slot(uri=CSOLINK.publications, name="publications", curie=CSOLINK.curie('publications'),
                   model_uri=CSOLINK.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.sequence_localization_attribute = Slot(uri=CSOLINK.sequence_localization_attribute, name="sequence localization attribute", curie=CSOLINK.curie('sequence_localization_attribute'),
                   model_uri=CSOLINK.sequence_localization_attribute, domain=ServiceSequenceLocalization, range=Optional[str])

slots.interbase_coordinate = Slot(uri=CSOLINK.interbase_coordinate, name="interbase coordinate", curie=CSOLINK.curie('interbase_coordinate'),
                   model_uri=CSOLINK.interbase_coordinate, domain=ServiceSequenceLocalization, range=Optional[int])

slots.start_interbase_coordinate = Slot(uri=CSOLINK.start_interbase_coordinate, name="start interbase coordinate", curie=CSOLINK.curie('start_interbase_coordinate'),
                   model_uri=CSOLINK.start_interbase_coordinate, domain=ServiceSequenceLocalization, range=Optional[int])

slots.end_interbase_coordinate = Slot(uri=CSOLINK.end_interbase_coordinate, name="end interbase coordinate", curie=CSOLINK.curie('end_interbase_coordinate'),
                   model_uri=CSOLINK.end_interbase_coordinate, domain=ServiceSequenceLocalization, range=Optional[int])

slots.workload_build = Slot(uri=CSOLINK.workload_build, name="workload build", curie=CSOLINK.curie('workload_build'),
                   model_uri=CSOLINK.workload_build, domain=ServiceSequenceLocalization, range=Optional[str])

slots.strand = Slot(uri=CSOLINK.strand, name="strand", curie=CSOLINK.curie('strand'),
                   model_uri=CSOLINK.strand, domain=ServiceSequenceLocalization, range=Optional[str])

slots.phase = Slot(uri=CSOLINK.phase, name="phase", curie=CSOLINK.curie('phase'),
                   model_uri=CSOLINK.phase, domain=CodingSequence, range=Optional[str])

slots.has_taxonomic_rank = Slot(uri=CSOLINK.has_taxonomic_rank, name="has taxonomic rank", curie=CSOLINK.curie('has_taxonomic_rank'),
                   model_uri=CSOLINK.has_taxonomic_rank, domain=None, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.attribute_name = Slot(uri=CSOLINK.name, name="attribute_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=CSOLINK.category, name="named thing_category", curie=CSOLINK.curie('category'),
                   model_uri=CSOLINK.named_thing_category, domain=NamedThing, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.system_taxon_has_taxonomic_rank = Slot(uri=CSOLINK.has_taxonomic_rank, name="system taxon_has taxonomic rank", curie=CSOLINK.curie('has_taxonomic_rank'),
                   model_uri=CSOLINK.system_taxon_has_taxonomic_rank, domain=SystemTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.system_taxon_subclass_of = Slot(uri=CSOLINK.subclass_of, name="system taxon_subclass of", curie=CSOLINK.curie('subclass_of'),
                   model_uri=CSOLINK.system_taxon_subclass_of, domain=SystemTaxon, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.agent_id = Slot(uri=CSOLINK.id, name="agent_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=CSOLINK.name, name="agent_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.publication_id = Slot(uri=CSOLINK.id, name="publication_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_name = Slot(uri=CSOLINK.name, name="publication_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.publication_type = Slot(uri=DCT.type, name="publication_type", curie=DCT.curie('type'),
                   model_uri=CSOLINK.publication_type, domain=Publication, range=str)

slots.publication_pages = Slot(uri=CSOLINK.pages, name="publication_pages", curie=CSOLINK.curie('pages'),
                   model_uri=CSOLINK.publication_pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.book_id = Slot(uri=CSOLINK.id, name="book_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.book_id, domain=Book, range=Union[str, BookId])

slots.book_type = Slot(uri=CSOLINK.type, name="book_type", curie=CSOLINK.curie('type'),
                   model_uri=CSOLINK.book_type, domain=Book, range=str)

slots.book_chapter_published_in = Slot(uri=CSOLINK.published_in, name="book chapter_published in", curie=CSOLINK.curie('published_in'),
                   model_uri=CSOLINK.book_chapter_published_in, domain=BookChapter, range=Union[str, URIorCURIE])

slots.serial_id = Slot(uri=CSOLINK.id, name="serial_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.serial_id, domain=Serial, range=Union[str, SerialId])

slots.serial_type = Slot(uri=CSOLINK.type, name="serial_type", curie=CSOLINK.curie('type'),
                   model_uri=CSOLINK.serial_type, domain=Serial, range=str)

slots.article_published_in = Slot(uri=CSOLINK.published_in, name="article_published in", curie=CSOLINK.curie('published_in'),
                   model_uri=CSOLINK.article_published_in, domain=Article, range=Union[str, URIorCURIE])

slots.article_iso_abbreviation = Slot(uri=CSOLINK.iso_abbreviation, name="article_iso abbreviation", curie=CSOLINK.curie('iso_abbreviation'),
                   model_uri=CSOLINK.article_iso_abbreviation, domain=Article, range=Optional[str])

slots.operational_activity_has_input = Slot(uri=CSOLINK.has_input, name="operational activity_has input", curie=CSOLINK.curie('has_input'),
                   model_uri=CSOLINK.operational_activity_has_input, domain=OperationalActivity, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.operational_activity_has_output = Slot(uri=CSOLINK.has_output, name="operational activity_has output", curie=CSOLINK.curie('has_output'),
                   model_uri=CSOLINK.operational_activity_has_output, domain=OperationalActivity, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.operational_activity_enabled_by = Slot(uri=CSOLINK.enabled_by, name="operational activity_enabled by", curie=CSOLINK.curie('enabled_by'),
                   model_uri=CSOLINK.operational_activity_enabled_by, domain=OperationalActivity, range=Optional[Union[Union[dict, "MacrooperationalMachineMixin"], List[Union[dict, "MacrooperationalMachineMixin"]]]])

slots.systemic_entity_has_attribute = Slot(uri=CSOLINK.has_attribute, name="systemic entity_has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.systemic_entity_has_attribute, domain=SystemicEntity, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.macrooperational_machine_mixin_name = Slot(uri=CSOLINK.name, name="macrooperational machine mixin_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.macrooperational_machine_mixin_name, domain=None, range=Optional[Union[str, SymbolType]])

slots.sequence_variant_has_componentservice = Slot(uri=CSOLINK.has_componentservice, name="sequence variant_has componentservice", curie=CSOLINK.curie('has_componentservice'),
                   model_uri=CSOLINK.sequence_variant_has_componentservice, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.sequence_variant_has_computational_sequence = Slot(uri=CSOLINK.has_computational_sequence, name="sequence variant_has computational sequence", curie=CSOLINK.curie('has_computational_sequence'),
                   model_uri=CSOLINK.sequence_variant_has_computational_sequence, domain=SequenceVariant, range=Optional[Union[str, ComputationalSequence]])

slots.sequence_variant_id = Slot(uri=CSOLINK.id, name="sequence variant_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.sequence_variant_id, domain=SequenceVariant, range=Union[str, SequenceVariantId])

slots.empirical_measurement_has_attribute_type = Slot(uri=CSOLINK.has_attribute_type, name="empirical measurement_has attribute type", curie=CSOLINK.curie('has_attribute_type'),
                   model_uri=CSOLINK.empirical_measurement_has_attribute_type, domain=EmpiricalMeasurement, range=Union[str, OntologyClassId])

slots.empirical_finding_has_attribute = Slot(uri=CSOLINK.has_attribute, name="empirical finding_has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.empirical_finding_has_attribute, domain=EmpiricalFinding, range=Optional[Union[Union[dict, EmpiricalAttribute], List[Union[dict, EmpiricalAttribute]]]])

slots.socioeconomic_exposure_has_attribute = Slot(uri=CSOLINK.has_attribute, name="socioeconomic exposure_has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.socioeconomic_exposure_has_attribute, domain=SocioeconomicExposure, range=Union[Union[dict, SocioeconomicAttribute], List[Union[dict, SocioeconomicAttribute]]])

slots.association_type = Slot(uri=CSOLINK.type, name="association_type", curie=CSOLINK.curie('type'),
                   model_uri=CSOLINK.association_type, domain=Association, range=Optional[str])

slots.association_category = Slot(uri=CSOLINK.category, name="association_category", curie=CSOLINK.curie('category'),
                   model_uri=CSOLINK.association_category, domain=Association, range=Union[Union[str, AssociationId], List[Union[str, AssociationId]]])

slots.contributor_association_subject = Slot(uri=CSOLINK.subject, name="contributor association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.contributor_association_subject, domain=ContributorAssociation, range=Union[str, InformationContentEntityId])

slots.contributor_association_predicate = Slot(uri=CSOLINK.predicate, name="contributor association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.contributor_association_predicate, domain=ContributorAssociation, range=Union[str, PredicateType])

slots.contributor_association_object = Slot(uri=CSOLINK.object, name="contributor association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.contributor_association_object, domain=ContributorAssociation, range=Union[str, AgentId])

slots.contributor_association_qualifiers = Slot(uri=CSOLINK.qualifiers, name="contributor association_qualifiers", curie=CSOLINK.curie('qualifiers'),
                   model_uri=CSOLINK.contributor_association_qualifiers, domain=ContributorAssociation, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.serviceunittype_to_serviceunittype_part_association_predicate = Slot(uri=CSOLINK.predicate, name="serviceunittype to serviceunittype part association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.serviceunittype_to_serviceunittype_part_association_predicate, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_serviceunittype_part_association_subject = Slot(uri=CSOLINK.subject, name="serviceunittype to serviceunittype part association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_to_serviceunittype_part_association_subject, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_serviceunittype_part_association_object = Slot(uri=CSOLINK.object, name="serviceunittype to serviceunittype part association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.serviceunittype_to_serviceunittype_part_association_object, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_componentservice_association_predicate = Slot(uri=CSOLINK.predicate, name="serviceunittype to componentservice association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.serviceunittype_to_componentservice_association_predicate, domain=ServiceunittypeToComponentserviceAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_componentservice_association_subject = Slot(uri=CSOLINK.subject, name="serviceunittype to componentservice association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_to_componentservice_association_subject, domain=ServiceunittypeToComponentserviceAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_componentservice_association_object = Slot(uri=CSOLINK.object, name="serviceunittype to componentservice association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.serviceunittype_to_componentservice_association_object, domain=ServiceunittypeToComponentserviceAssociation, range=Union[dict, Componentservice])

slots.serviceunittype_to_variant_association_predicate = Slot(uri=CSOLINK.predicate, name="serviceunittype to variant association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.serviceunittype_to_variant_association_predicate, domain=ServiceunittypeToVariantAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_variant_association_subject = Slot(uri=CSOLINK.subject, name="serviceunittype to variant association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_to_variant_association_subject, domain=ServiceunittypeToVariantAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_variant_association_object = Slot(uri=CSOLINK.object, name="serviceunittype to variant association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.serviceunittype_to_variant_association_object, domain=ServiceunittypeToVariantAssociation, range=Union[str, SequenceVariantId])

slots.componentservice_to_componentservice_association_subject = Slot(uri=CSOLINK.subject, name="componentservice to componentservice association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_componentservice_association_subject, domain=ComponentserviceToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_componentservice_association_object = Slot(uri=CSOLINK.object, name="componentservice to componentservice association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.componentservice_to_componentservice_association_object, domain=ComponentserviceToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_componentservice_homology_association_predicate = Slot(uri=CSOLINK.predicate, name="componentservice to componentservice homology association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.componentservice_to_componentservice_homology_association_predicate, domain=ComponentserviceToComponentserviceHomologyAssociation, range=Union[str, PredicateType])

slots.componentservice_availability_mixin_quantifier_qualifier = Slot(uri=CSOLINK.quantifier_qualifier, name="componentservice availability mixin_quantifier qualifier", curie=CSOLINK.curie('quantifier_qualifier'),
                   model_uri=CSOLINK.componentservice_availability_mixin_quantifier_qualifier, domain=ComponentserviceAvailabilityMixin, range=Optional[Union[str, OntologyClassId]])

slots.componentservice_to_componentservice_coavailability_association_predicate = Slot(uri=CSOLINK.predicate, name="componentservice to componentservice coavailability association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.componentservice_to_componentservice_coavailability_association_predicate, domain=ComponentserviceToComponentserviceCoavailabilityAssociation, range=Union[str, PredicateType])

slots.pairwise_componentservice_to_componentservice_interaction_predicate = Slot(uri=CSOLINK.predicate, name="pairwise componentservice to componentservice interaction_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.pairwise_componentservice_to_componentservice_interaction_predicate, domain=PairwiseComponentserviceToComponentserviceInteraction, range=Union[str, PredicateType])

slots.pairwise_componentservice_to_componentservice_interaction_relation = Slot(uri=CSOLINK.relation, name="pairwise componentservice to componentservice interaction_relation", curie=CSOLINK.curie('relation'),
                   model_uri=CSOLINK.pairwise_componentservice_to_componentservice_interaction_relation, domain=PairwiseComponentserviceToComponentserviceInteraction, range=Union[str, URIorCURIE])

slots.pairwise_operationally_interaction_subject = Slot(uri=CSOLINK.subject, name="pairwise operationally interaction_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.pairwise_operationally_interaction_subject, domain=PairwiseOperationallyInteraction, range=Union[str, OperationalEntityId])

slots.pairwise_operationally_interaction_id = Slot(uri=CSOLINK.id, name="pairwise operationally interaction_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.pairwise_operationally_interaction_id, domain=PairwiseOperationallyInteraction, range=Union[str, PairwiseOperationallyInteractionId])

slots.pairwise_operationally_interaction_predicate = Slot(uri=CSOLINK.predicate, name="pairwise operationally interaction_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.pairwise_operationally_interaction_predicate, domain=PairwiseOperationallyInteraction, range=Union[str, PredicateType])

slots.pairwise_operationally_interaction_relation = Slot(uri=CSOLINK.relation, name="pairwise operationally interaction_relation", curie=CSOLINK.curie('relation'),
                   model_uri=CSOLINK.pairwise_operationally_interaction_relation, domain=PairwiseOperationallyInteraction, range=Union[str, URIorCURIE])

slots.pairwise_operationally_interaction_object = Slot(uri=CSOLINK.object, name="pairwise operationally interaction_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.pairwise_operationally_interaction_object, domain=PairwiseOperationallyInteraction, range=Union[str, OperationalEntityId])

slots.component_type_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="component type to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.component_type_to_entity_association_mixin_subject, domain=None, range=Union[str, ComponentTypeId])

slots.component_type_to_error_or_observable_feature_association_subject = Slot(uri=CSOLINK.subject, name="component type to error or observable feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.component_type_to_error_or_observable_feature_association_subject, domain=ComponentTypeToErrorOrObservableFeatureAssociation, range=Union[str, ErrorOrObservableFeatureId])

slots.operational_entity_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="operational entity to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.operational_entity_to_entity_association_mixin_subject, domain=None, range=Union[str, OperationalEntityId])

slots.administrative_operational_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="administrative operational to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.administrative_operational_to_entity_association_mixin_subject, domain=None, range=Union[str, AdministrativeOperationId])

slots.orchestration_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="orchestration to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.orchestration_to_entity_association_mixin_subject, domain=None, range=Union[str, ControlActorId])

slots.case_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="case to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.case_to_entity_association_mixin_subject, domain=None, range=Union[str, CaseId])

slots.orchestration_to_orchestration_association_object = Slot(uri=CSOLINK.object, name="orchestration to orchestration association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.orchestration_to_orchestration_association_object, domain=OrchestrationToOrchestrationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_subject = Slot(uri=CSOLINK.subject, name="orchestration to orchestration derivation association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.orchestration_to_orchestration_derivation_association_subject, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_object = Slot(uri=CSOLINK.object, name="orchestration to orchestration derivation association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.orchestration_to_orchestration_derivation_association_object, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_predicate = Slot(uri=CSOLINK.predicate, name="orchestration to orchestration derivation association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.orchestration_to_orchestration_derivation_association_predicate, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, PredicateType])

slots.orchestration_to_orchestration_derivation_association_catalyst_qualifier = Slot(uri=CSOLINK.catalyst_qualifier, name="orchestration to orchestration derivation association_catalyst qualifier", curie=CSOLINK.curie('catalyst_qualifier'),
                   model_uri=CSOLINK.orchestration_to_orchestration_derivation_association_catalyst_qualifier, domain=OrchestrationToOrchestrationDerivationAssociation, range=Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]])

slots.orchestration_to_error_or_observable_feature_association_object = Slot(uri=CSOLINK.object, name="orchestration to error or observable feature association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.orchestration_to_error_or_observable_feature_association_object, domain=OrchestrationToErrorOrObservableFeatureAssociation, range=Union[str, ErrorOrObservableFeatureId])

slots.orchestration_to_pathway_association_object = Slot(uri=CSOLINK.object, name="orchestration to pathway association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.orchestration_to_pathway_association_object, domain=OrchestrationToPathwayAssociation, range=Union[str, PathwayId])

slots.orchestration_to_componentservice_association_object = Slot(uri=CSOLINK.object, name="orchestration to componentservice association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.orchestration_to_componentservice_association_object, domain=OrchestrationToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.administrative_operational_to_componentservice_association_object = Slot(uri=CSOLINK.object, name="administrative operational to componentservice association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.administrative_operational_to_componentservice_association_object, domain=AdministrativeOperationalToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.resource_sample_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="resource sample to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.resource_sample_to_entity_association_mixin_subject, domain=None, range=Union[str, ResourceSampleId])

slots.resource_sample_derivation_association_subject = Slot(uri=CSOLINK.subject, name="resource sample derivation association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.resource_sample_derivation_association_subject, domain=ResourceSampleDerivationAssociation, range=Union[str, ResourceSampleId])

slots.resource_sample_derivation_association_object = Slot(uri=CSOLINK.object, name="resource sample derivation association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.resource_sample_derivation_association_object, domain=ResourceSampleDerivationAssociation, range=Union[str, NamedThingId])

slots.resource_sample_derivation_association_predicate = Slot(uri=CSOLINK.predicate, name="resource sample derivation association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.resource_sample_derivation_association_predicate, domain=ResourceSampleDerivationAssociation, range=Union[str, PredicateType])

slots.error_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="error to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.error_to_entity_association_mixin_subject, domain=None, range=Union[str, ErrorId])

slots.entity_to_exposure_event_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to exposure event association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_exposure_event_association_mixin_object, domain=None, range=Union[dict, ExposureEvent])

slots.exposure_event_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="exposure event to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.exposure_event_to_entity_association_mixin_subject, domain=None, range=Union[dict, ExposureEvent])

slots.entity_to_outcome_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to outcome association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_outcome_association_mixin_object, domain=None, range=Union[dict, Outcome])

slots.entity_to_observable_feature_association_mixin_description = Slot(uri=CSOLINK.description, name="entity to observable feature association mixin_description", curie=CSOLINK.curie('description'),
                   model_uri=CSOLINK.entity_to_observable_feature_association_mixin_description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.entity_to_observable_feature_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to observable feature association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_observable_feature_association_mixin_object, domain=None, range=Union[str, ObservableFeatureId])

slots.entity_to_error_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to error association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_error_association_mixin_object, domain=None, range=Union[str, ErrorId])

slots.error_or_observable_feature_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="error or observable feature to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.error_or_observable_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, ErrorOrObservableFeatureId])

slots.error_or_observable_feature_association_to_location_association_object = Slot(uri=CSOLINK.object, name="error or observable feature association to location association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.error_or_observable_feature_association_to_location_association_object, domain=ErrorOrObservableFeatureAssociationToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.error_or_observable_feature_to_location_association_object = Slot(uri=CSOLINK.object, name="error or observable feature to location association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.error_or_observable_feature_to_location_association_object, domain=ErrorOrObservableFeatureToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.entity_to_error_or_observable_feature_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to error or observable feature association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_error_or_observable_feature_association_mixin_object, domain=None, range=Union[str, ErrorOrObservableFeatureId])

slots.serviceunittype_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="serviceunittype to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_to_entity_association_mixin_subject, domain=None, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_observable_feature_association_predicate = Slot(uri=CSOLINK.predicate, name="serviceunittype to observable feature association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.serviceunittype_to_observable_feature_association_predicate, domain=ServiceunittypeToObservableFeatureAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_observable_feature_association_subject = Slot(uri=CSOLINK.subject, name="serviceunittype to observable feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_to_observable_feature_association_subject, domain=ServiceunittypeToObservableFeatureAssociation, range=Union[str, ServiceunittypeId])

slots.exposure_event_to_observable_feature_association_subject = Slot(uri=CSOLINK.subject, name="exposure event to observable feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.exposure_event_to_observable_feature_association_subject, domain=ExposureEventToObservableFeatureAssociation, range=Union[dict, ExposureEvent])

slots.behavior_to_behavioral_feature_association_subject = Slot(uri=CSOLINK.subject, name="behavior to behavioral feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.behavior_to_behavioral_feature_association_subject, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehaviorId])

slots.behavior_to_behavioral_feature_association_object = Slot(uri=CSOLINK.object, name="behavior to behavioral feature association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.behavior_to_behavioral_feature_association_object, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehavioralFeatureId])

slots.componentservice_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="componentservice to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_entity_association_mixin_subject, domain=None, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="variant to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_entity_association_mixin_subject, domain=None, range=Union[str, SequenceVariantId])

slots.componentservice_to_observable_feature_association_subject = Slot(uri=CSOLINK.subject, name="componentservice to observable feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_observable_feature_association_subject, domain=ComponentserviceToObservableFeatureAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_error_association_subject = Slot(uri=CSOLINK.subject, name="componentservice to error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_error_association_subject, domain=ComponentserviceToErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_to_componentservice_association_object = Slot(uri=CSOLINK.object, name="variant to componentservice association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.variant_to_componentservice_association_object, domain=VariantToComponentserviceAssociation, range=Union[dict, Componentservice])

slots.variant_to_componentservice_association_predicate = Slot(uri=CSOLINK.predicate, name="variant to componentservice association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.variant_to_componentservice_association_predicate, domain=VariantToComponentserviceAssociation, range=Union[str, PredicateType])

slots.variant_to_componentservice_availability_association_predicate = Slot(uri=CSOLINK.predicate, name="variant to componentservice availability association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.variant_to_componentservice_availability_association_predicate, domain=VariantToComponentserviceAvailabilityAssociation, range=Union[str, PredicateType])

slots.variant_to_population_association_subject = Slot(uri=CSOLINK.subject, name="variant to population association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=CSOLINK.object, name="variant to population association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.variant_to_population_association_has_quotient = Slot(uri=CSOLINK.has_quotient, name="variant to population association_has quotient", curie=CSOLINK.curie('has_quotient'),
                   model_uri=CSOLINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=CSOLINK.has_count, name="variant to population association_has count", curie=CSOLINK.curie('has_count'),
                   model_uri=CSOLINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=CSOLINK.has_total, name="variant to population association_has total", curie=CSOLINK.curie('has_total'),
                   model_uri=CSOLINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=CSOLINK.subject, name="population to population association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_object = Slot(uri=CSOLINK.object, name="population to population association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_predicate = Slot(uri=CSOLINK.predicate, name="population to population association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.population_to_population_association_predicate, domain=PopulationToPopulationAssociation, range=Union[str, PredicateType])

slots.variant_to_observable_feature_association_subject = Slot(uri=CSOLINK.subject, name="variant to observable feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_observable_feature_association_subject, domain=VariantToObservableFeatureAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_error_association_subject = Slot(uri=CSOLINK.subject, name="variant to error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_error_association_subject, domain=VariantToErrorAssociation, range=Union[str, NamedThingId])

slots.variant_to_error_association_predicate = Slot(uri=CSOLINK.predicate, name="variant to error association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.variant_to_error_association_predicate, domain=VariantToErrorAssociation, range=Union[str, PredicateType])

slots.variant_to_error_association_object = Slot(uri=CSOLINK.object, name="variant to error association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.variant_to_error_association_object, domain=VariantToErrorAssociation, range=Union[str, NamedThingId])

slots.serviceunittype_to_error_association_subject = Slot(uri=CSOLINK.subject, name="serviceunittype to error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_to_error_association_subject, domain=ServiceunittypeToErrorAssociation, range=Union[str, NamedThingId])

slots.serviceunittype_to_error_association_predicate = Slot(uri=CSOLINK.predicate, name="serviceunittype to error association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.serviceunittype_to_error_association_predicate, domain=ServiceunittypeToErrorAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_error_association_object = Slot(uri=CSOLINK.object, name="serviceunittype to error association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.serviceunittype_to_error_association_object, domain=ServiceunittypeToErrorAssociation, range=Union[str, NamedThingId])

slots.model_to_error_association_mixin_subject = Slot(uri=CSOLINK.subject, name="model to error association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.model_to_error_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.model_to_error_association_mixin_predicate = Slot(uri=CSOLINK.predicate, name="model to error association mixin_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.model_to_error_association_mixin_predicate, domain=None, range=Union[str, PredicateType])

slots.componentservice_as_a_model_of_error_association_subject = Slot(uri=CSOLINK.subject, name="componentservice as a model of error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_as_a_model_of_error_association_subject, domain=ComponentserviceAsAModelOfErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_as_a_model_of_error_association_subject = Slot(uri=CSOLINK.subject, name="variant as a model of error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_as_a_model_of_error_association_subject, domain=VariantAsAModelOfErrorAssociation, range=Union[str, SequenceVariantId])

slots.serviceunittype_as_a_model_of_error_association_subject = Slot(uri=CSOLINK.subject, name="serviceunittype as a model of error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.serviceunittype_as_a_model_of_error_association_subject, domain=ServiceunittypeAsAModelOfErrorAssociation, range=Union[str, ServiceunittypeId])

slots.component_type_as_a_model_of_error_association_subject = Slot(uri=CSOLINK.subject, name="component type as a model of error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.component_type_as_a_model_of_error_association_subject, domain=ComponentTypeAsAModelOfErrorAssociation, range=Union[str, ComponentTypeId])

slots.systemic_entity_as_a_model_of_error_association_subject = Slot(uri=CSOLINK.subject, name="systemic entity as a model of error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.systemic_entity_as_a_model_of_error_association_subject, domain=SystemicEntityAsAModelOfErrorAssociation, range=Union[str, SystemicEntityId])

slots.componentservice_has_variant_that_contributes_to_error_association_subject = Slot(uri=CSOLINK.subject, name="componentservice has variant that contributes to error association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_has_variant_that_contributes_to_error_association_subject, domain=ComponentserviceHasVariantThatContributesToErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_availability_site_association_subject = Slot(uri=CSOLINK.subject, name="componentservice to availability site association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_availability_site_association_subject, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_availability_site_association_object = Slot(uri=CSOLINK.object, name="componentservice to availability site association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.componentservice_to_availability_site_association_object, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[str, DeploymentEntityId])

slots.componentservice_to_availability_site_association_predicate = Slot(uri=CSOLINK.predicate, name="componentservice to availability site association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.componentservice_to_availability_site_association_predicate, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[str, PredicateType])

slots.componentservice_to_availability_site_association_stage_qualifier = Slot(uri=CSOLINK.stage_qualifier, name="componentservice to availability site association_stage qualifier", curie=CSOLINK.curie('stage_qualifier'),
                   model_uri=CSOLINK.componentservice_to_availability_site_association_stage_qualifier, domain=ComponentserviceToAvailabilitySiteAssociation, range=Optional[Union[str, LifecycleStageId]])

slots.componentservice_to_availability_site_association_quantifier_qualifier = Slot(uri=CSOLINK.quantifier_qualifier, name="componentservice to availability site association_quantifier qualifier", curie=CSOLINK.curie('quantifier_qualifier'),
                   model_uri=CSOLINK.componentservice_to_availability_site_association_quantifier_qualifier, domain=ComponentserviceToAvailabilitySiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.sequence_variant_modulates_repairing_association_subject = Slot(uri=CSOLINK.subject, name="sequence variant modulates repairing association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.sequence_variant_modulates_repairing_association_subject, domain=SequenceVariantModulatesRepairingAssociation, range=Union[str, SequenceVariantId])

slots.sequence_variant_modulates_repairing_association_object = Slot(uri=CSOLINK.object, name="sequence variant modulates repairing association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.sequence_variant_modulates_repairing_association_object, domain=SequenceVariantModulatesRepairingAssociation, range=Union[str, RepairingId])

slots.functional_association_subject = Slot(uri=CSOLINK.subject, name="functional association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.functional_association_subject, domain=FunctionalAssociation, range=Union[dict, MacrooperationalMachineMixin])

slots.functional_association_object = Slot(uri=CSOLINK.object, name="functional association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.functional_association_object, domain=FunctionalAssociation, range=Union[str, ComponentserviceOntologyClassId])

slots.macrooperational_machine_mixin_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="macrooperational machine mixin to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.macrooperational_machine_mixin_to_entity_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.macrooperational_machine_mixin_to_operational_activity_association_object = Slot(uri=CSOLINK.object, name="macrooperational machine mixin to operational activity association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.macrooperational_machine_mixin_to_operational_activity_association_object, domain=MacrooperationalMachineMixinToOperationalActivityAssociation, range=Union[str, OperationalActivityId])

slots.macrooperational_machine_mixin_to_computational_process_association_object = Slot(uri=CSOLINK.object, name="macrooperational machine mixin to computational process association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.macrooperational_machine_mixin_to_computational_process_association_object, domain=MacrooperationalMachineMixinToComputationalProcessAssociation, range=Union[str, ComputationalProcessId])

slots.macrooperational_machine_mixin_to_component_association_object = Slot(uri=CSOLINK.object, name="macrooperational machine mixin to component association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.macrooperational_machine_mixin_to_component_association_object, domain=MacrooperationalMachineMixinToComponentAssociation, range=Union[str, ComponentId])

slots.componentservice_to_go_term_association_subject = Slot(uri=CSOLINK.subject, name="componentservice to go term association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_go_term_association_subject, domain=ComponentserviceToGoTermAssociation, range=Union[str, OperationalEntityId])

slots.componentservice_to_go_term_association_object = Slot(uri=CSOLINK.object, name="componentservice to go term association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.componentservice_to_go_term_association_object, domain=ComponentserviceToGoTermAssociation, range=Union[str, ComponentserviceOntologyClassId])

slots.service_sequence_localization_subject = Slot(uri=CSOLINK.subject, name="service sequence localization_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.service_sequence_localization_subject, domain=ServiceSequenceLocalization, range=Union[str, WorkloadEntityId])

slots.service_sequence_localization_object = Slot(uri=CSOLINK.object, name="service sequence localization_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.service_sequence_localization_object, domain=ServiceSequenceLocalization, range=Union[str, WorkloadEntityId])

slots.service_sequence_localization_predicate = Slot(uri=CSOLINK.predicate, name="service sequence localization_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.service_sequence_localization_predicate, domain=ServiceSequenceLocalization, range=Union[str, PredicateType])

slots.sequence_feature_relationship_subject = Slot(uri=CSOLINK.subject, name="sequence feature relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[str, WorkloadEntityId])

slots.sequence_feature_relationship_object = Slot(uri=CSOLINK.object, name="sequence feature relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[str, WorkloadEntityId])

slots.componentserviceinstance_to_componentservice_relationship_subject = Slot(uri=CSOLINK.subject, name="componentserviceinstance to componentservice relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentserviceinstance_to_componentservice_relationship_subject, domain=ComponentserviceinstanceToComponentserviceRelationship, range=Union[str, ComponentserviceinstanceId])

slots.componentserviceinstance_to_componentservice_relationship_object = Slot(uri=CSOLINK.object, name="componentserviceinstance to componentservice relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.componentserviceinstance_to_componentservice_relationship_object, domain=ComponentserviceinstanceToComponentserviceRelationship, range=Union[dict, Componentservice])

slots.componentservice_to_servicetype_relationship_subject = Slot(uri=CSOLINK.subject, name="componentservice to servicetype relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_to_servicetype_relationship_subject, domain=ComponentserviceToServicetypeRelationship, range=Union[dict, Componentservice])

slots.componentservice_to_servicetype_relationship_object = Slot(uri=CSOLINK.object, name="componentservice to servicetype relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.componentservice_to_servicetype_relationship_object, domain=ComponentserviceToServicetypeRelationship, range=Union[dict, ServicetypeMixin])

slots.componentservice_to_servicetype_relationship_predicate = Slot(uri=CSOLINK.predicate, name="componentservice to servicetype relationship_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.componentservice_to_servicetype_relationship_predicate, domain=ComponentserviceToServicetypeRelationship, range=Union[str, PredicateType])

slots.daemon_to_componentserviceinstance_relationship_subject = Slot(uri=CSOLINK.subject, name="daemon to componentserviceinstance relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.daemon_to_componentserviceinstance_relationship_subject, domain=DaemonToComponentserviceinstanceRelationship, range=Union[str, DaemonId])

slots.daemon_to_componentserviceinstance_relationship_object = Slot(uri=CSOLINK.object, name="daemon to componentserviceinstance relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.daemon_to_componentserviceinstance_relationship_object, domain=DaemonToComponentserviceinstanceRelationship, range=Union[str, ComponentserviceinstanceId])

slots.componentservice_regulatory_relationship_predicate = Slot(uri=CSOLINK.predicate, name="componentservice regulatory relationship_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.componentservice_regulatory_relationship_predicate, domain=ComponentserviceRegulatoryRelationship, range=Union[str, PredicateType])

slots.componentservice_regulatory_relationship_subject = Slot(uri=CSOLINK.subject, name="componentservice regulatory relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.componentservice_regulatory_relationship_subject, domain=ComponentserviceRegulatoryRelationship, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_regulatory_relationship_object = Slot(uri=CSOLINK.object, name="componentservice regulatory relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.componentservice_regulatory_relationship_object, domain=ComponentserviceRegulatoryRelationship, range=Union[dict, ComponentserviceOrServicetype])

slots.deployment_entity_to_deployment_entity_association_subject = Slot(uri=CSOLINK.subject, name="deployment entity to deployment entity association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_association_subject, domain=DeploymentEntityToDeploymentEntityAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_association_object = Slot(uri=CSOLINK.object, name="deployment entity to deployment entity association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_association_object, domain=DeploymentEntityToDeploymentEntityAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_subject = Slot(uri=CSOLINK.subject, name="deployment entity to deployment entity part of association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_part_of_association_subject, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_object = Slot(uri=CSOLINK.object, name="deployment entity to deployment entity part of association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_part_of_association_object, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_predicate = Slot(uri=CSOLINK.predicate, name="deployment entity to deployment entity part of association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_part_of_association_predicate, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, PredicateType])

slots.deployment_entity_to_deployment_entity_ontogenic_association_subject = Slot(uri=CSOLINK.subject, name="deployment entity to deployment entity ontogenic association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_ontogenic_association_subject, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_ontogenic_association_object = Slot(uri=CSOLINK.object, name="deployment entity to deployment entity ontogenic association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_ontogenic_association_object, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_ontogenic_association_predicate = Slot(uri=CSOLINK.predicate, name="deployment entity to deployment entity ontogenic association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.deployment_entity_to_deployment_entity_ontogenic_association_predicate, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, PredicateType])
