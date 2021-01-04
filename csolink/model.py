# Auto generated from csolink-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2020-12-21 15:18
# Schema: Csolink-Model
#
# id: https://w3id.org//csolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
import parse
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from ml.utils.slot import Slot
from ml.utils.metamodelcore import empty_list, empty_dict, bnode
from ml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from ml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from ml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from ml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from ml.utils.curienamespace import CurieNamespace
from ml.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime
from includes.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie

metamodel_version = "1.6.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
APO = CurieNamespace('APO', 'http://purl.obolibrary.org/obo/APO_')
AEOLUS = CurieNamespace('Aeolus', 'http://translator.ncats.nih.gov/Aeolus_')
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
BIOSAMPLE = CurieNamespace('BIOSAMPLE', 'http://identifiers.org/biosample/')
BSPO = CurieNamespace('BSPO', 'http://purl.obolibrary.org/obo/BSPO_')
CAID = CurieNamespace('CAID', 'http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://identifiers.org/chembl.compound/')
CHEMBL_MECHANISM = CurieNamespace('CHEMBL_MECHANISM', 'https://www.ebi.ac.uk/chembl/mechanism/inspect/')
CHEMBL_TARGET = CurieNamespace('CHEMBL_TARGET', 'http://identifiers.org/chembl.target/')
CID = CurieNamespace('CID', 'http://pubchem.ncbi.nlm.nih.gov/compound/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CLINVAR = CurieNamespace('CLINVAR', 'http://identifiers.org/clinvar/')
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://purl.org/coar/resource_type/')
CPT = CurieNamespace('CPT', 'https://www.ama-assn.org/practice-management/cpt/')
CTD = CurieNamespace('CTD', 'http://translator.ncats.nih.gov/CTD_')
CLINVARVARIANT = CurieNamespace('ClinVarVariant', 'http://www.ncbi.nlm.nih.gov/clinvar/variation/')
DBSNP = CurieNamespace('DBSNP', 'http://identifiers.org/dbsnp/')
DGIDB = CurieNamespace('DGIdb', 'https://www.dgidb.org/interaction_types')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
DRUGBANK = CurieNamespace('DRUGBANK', 'http://identifiers.org/drugbank/')
DRUGCENTRAL = CurieNamespace('DrugCentral', 'http://translator.ncats.nih.gov/DrugCentral_')
EC = CurieNamespace('EC', 'http://www.enzyme-database.org/query.php?ec=')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
FAO = CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
FBCV = CurieNamespace('FBcv', 'http://purl.obolibrary.org/obo/FBcv_')
FLYBASE = CurieNamespace('FlyBase', 'http://flybase.org/reports/')
GAMMA = CurieNamespace('GAMMA', 'http://translator.renci.org/GAMMA_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GOP = CurieNamespace('GOP', 'http://purl.obolibrary.org/obo/go#')
GOREL = CurieNamespace('GOREL', 'http://purl.obolibrary.org/obo/GOREL_')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
GTEX = CurieNamespace('GTEx', 'https://www.gtexportal.org/home/gene/')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://www.ebi.ac.uk/ancestro/ancestro_')
HCPCS = CurieNamespace('HCPCS', 'http://purl.bioontology.org/ontology/HCPCS/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
HGNC_FAMILY = CurieNamespace('HGNC_FAMILY', 'http://identifiers.org/hgnc.family/')
HMDB = CurieNamespace('HMDB', 'http://identifiers.org/hmdb/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
ICD0 = CurieNamespace('ICD0', 'http://translator.ncats.nih.gov/ICD0_')
ICD10 = CurieNamespace('ICD10', 'http://translator.ncats.nih.gov/ICD10_')
ICD9 = CurieNamespace('ICD9', 'http://translator.ncats.nih.gov/ICD9_')
INCHI = CurieNamespace('INCHI', 'http://identifiers.org/inchi/')
INCHIKEY = CurieNamespace('INCHIKEY', 'http://identifiers.org/inchikey/')
INTACT = CurieNamespace('INTACT', 'http://identifiers.org/intact/')
IUPHAR_FAMILY = CurieNamespace('IUPHAR_FAMILY', 'http://identifiers.org/iuphar.family/')
KEGG = CurieNamespace('KEGG', 'http://identifiers.org/kegg/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MEDDRA = CurieNamespace('MEDDRA', 'http://identifiers.org/meddra/')
MESH = CurieNamespace('MESH', 'http://identifiers.org/mesh/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
MI = CurieNamespace('MI', 'http://purl.obolibrary.org/obo/MI_')
MIR = CurieNamespace('MIR', 'http://identifiers.org/mir/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MP = CurieNamespace('MP', 'http://purl.obolibrary.org/obo/MP_')
MSIGDB = CurieNamespace('MSigDB', 'https://www.gsea-msigdb.org/gsea/msigdb/')
METACYC = CurieNamespace('MetaCyc', 'http://translator.ncats.nih.gov/MetaCyc_')
NCBIGENE = CurieNamespace('NCBIGENE', 'http://identifiers.org/ncbigene/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NDDF = CurieNamespace('NDDF', 'http://purl.bioontology.org/ontology/NDDF/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
OBOREL = CurieNamespace('OBOREL', 'http://purl.obolibrary.org/obo/RO_')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OMIM = CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
ORPHA = CurieNamespace('ORPHA', 'http://www.orpha.net/ORDO/Orphanet_')
ORPHANET = CurieNamespace('ORPHANET', 'http://identifiers.org/orphanet/')
PANTHER_FAMILY = CurieNamespace('PANTHER_FAMILY', 'http://identifiers.org/panther.family/')
PATO_PROPERTY = CurieNamespace('PATO-PROPERTY', 'http://purl.obolibrary.org/obo/pato#')
PDQ = CurieNamespace('PDQ', 'https://www.cancer.gov/publications/pdq#')
PHARMGKB_DRUG = CurieNamespace('PHARMGKB_DRUG', 'http://identifiers.org/pharmgkb.drug/')
PHARMGKB_PATHWAYS = CurieNamespace('PHARMGKB_PATHWAYS', 'http://identifiers.org/pharmgkb.pathways/')
PHAROS = CurieNamespace('PHAROS', 'http://pharos.nih.gov')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
POMBASE = CurieNamespace('POMBASE', 'http://identifiers.org/pombase/')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://identifiers.org/pubchem.compound/')
PUBCHEM_SUBSTANCE = CurieNamespace('PUBCHEM_SUBSTANCE', 'http://identifiers.org/pubchem.substance/')
PATHWHIZ = CurieNamespace('PathWhiz', 'http://smpdb.ca/pathways/#')
REACT = CurieNamespace('REACT', 'http://www.reactome.org/PathwayBrowser/#/')
REPODB = CurieNamespace('REPODB', 'http://apps.chiragjpgroup.org/repoDB/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
RHEA = CurieNamespace('RHEA', 'http://identifiers.org/rhea/')
RNACENTRAL = CurieNamespace('RNACENTRAL', 'http://identifiers.org/rnacentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RTXKG1 = CurieNamespace('RTXKG1', 'http://kg1endpoint.rtx.ai/')
RXNORM = CurieNamespace('RXNORM', 'http://purl.bioontology.org/ontology/RXNORM/')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SEMMEDDB = CurieNamespace('SEMMEDDB', 'https://skr3.nlm.nih.gov/SemMedDB')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SMPDB = CurieNamespace('SMPDB', 'http://identifiers.org/smpdb/')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://identifiers.org/snomedct/')
SNPEFF = CurieNamespace('SNPEFF', 'http://translator.ncats.nih.gov/SNPEFF_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_')
UBERGRAPH = CurieNamespace('UBERGRAPH', 'http://translator.renci.org/ubergraph-axioms.ofn#')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UBERON_CORE = CurieNamespace('UBERON_CORE', 'http://purl.obolibrary.org/obo/uberon/core#')
UMLS = CurieNamespace('UMLS', 'http://identifiers.org/umls/')
UMLSSC = CurieNamespace('UMLSSC', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/code#')
UMLSSG = CurieNamespace('UMLSSG', 'https://metamap.nlm.nih.gov/Docs/SemGroups_2018.txt/group#')
UMLSST = CurieNamespace('UMLSST', 'https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt/type#')
UNII = CurieNamespace('UNII', 'http://identifiers.org/unii/')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://identifiers.org/uniprot/')
VANDF = CurieNamespace('VANDF', 'https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/VANDF/')
VMC = CurieNamespace('VMC', 'https://github.com/ga4gh/vr-spec/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
WBPHENOTYPE = CurieNamespace('WBPhenotype', 'http://purl.obolibrary.org/obo/WBPhenotype_')
WBVOCAB = CurieNamespace('WBVocab', 'http://bio2rdf.org/wormbase_vocabulary')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
WIKIPATHWAYS = CurieNamespace('WIKIPATHWAYS', 'http://identifiers.org/wikipathways/')
WORMBASE = CurieNamespace('WormBase', 'https://www.wormbase.org/get?name=')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ZP = CurieNamespace('ZP', 'http://purl.obolibrary.org/obo/ZP_')
ALLIANCEGENOME = CurieNamespace('alliancegenome', 'https://www.alliancegenome.org/')
CSOLINK = CurieNamespace('csolink', 'https://w3id.org/csolink/vocab/')
BIOLINKML = CurieNamespace('ml', 'https://w3id.org/biolink/biolinkml/')
CHEMBIO = CurieNamespace('chembio', 'http://translator.ncats.nih.gov/chembio_')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DICTYBASE = CurieNamespace('dictyBase', 'http://dictybase.org/gene/')
DOI = CurieNamespace('doi', 'https://doi.org/')
FABIO = CurieNamespace('fabio', 'http://purl.org/spar/fabio/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
FOODB_COMPOUND = CurieNamespace('foodb_compound', 'http://foodb.ca/compounds/')
GFF3 = CurieNamespace('gff3', 'https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md#')
GPI = CurieNamespace('gpi', 'https://github.com/geneontology/go-annotation/blob/master/specs/gpad-gpi-2-0.md#')
GTPO = CurieNamespace('gtpo', 'https://rdf.guidetopharmacology.org/ns/gtpo#')
HETIO = CurieNamespace('hetio', 'http://translator.ncats.nih.gov/hetio_')
INTERPRO = CurieNamespace('interpro', 'https://www.ebi.ac.uk/interpro/entry/')
ISBN = CurieNamespace('isbn', 'https://www.isbn-international.org/identifier/')
ISNI = CurieNamespace('isni', 'https://isni.org/isni/')
ISSN = CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/')
MEDGEN = CurieNamespace('medgen', 'https://www.ncbi.nlm.nih.gov/medgen/')
OBOFORMAT = CurieNamespace('oboformat', 'http://www.geneontology.org/formats/oboInOWL#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CSOLINK


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = CSOLINK.ChemicalFormulaValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the csolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the csolink class, for example csolink:Gene. For an RDF representation, the value should be a URI such as https://w3id.org/csolink/vocab/Gene """
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
    """ A CURIE from the csolink related_to hierarchy. For example, csolink:related_to, csolink:causes, csolink:treats. """
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


class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological sequence"
    type_model_uri = CSOLINK.BiologicalSequence


# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class GeneOntologyClassId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class OrganismTaxonId(OntologyClassId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class DataFileId(InformationContentEntityId):
    pass


class SourceFileId(DataFileId):
    pass


class DataSetId(InformationContentEntityId):
    pass


class DataSetVersionId(DataSetId):
    pass


class DistributionLevelId(DataSetVersionId):
    pass


class DataSetSummaryId(DataSetVersionId):
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


class PhysicalEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class ProcedureId(NamedThingId):
    pass


class PhenomenonId(NamedThingId):
    pass


class DeviceId(NamedThingId):
    pass


class MaterialSampleId(PhysicalEntityId):
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


class BiologicalEntityId(NamedThingId):
    pass


class MolecularEntityId(BiologicalEntityId):
    pass


class BiologicalProcessOrActivityId(BiologicalEntityId):
    pass


class MolecularActivityId(BiologicalProcessOrActivityId):
    pass


class BiologicalProcessId(BiologicalProcessOrActivityId):
    pass


class PathwayId(BiologicalProcessId):
    pass


class PhysiologicalProcessId(BiologicalProcessId):
    pass


class PathologicalProcessId(BiologicalProcessId):
    pass


class BehaviorId(BiologicalProcessId):
    pass


class DeathId(BiologicalProcessId):
    pass


class ChemicalSubstanceId(MolecularEntityId):
    pass


class CarbohydrateId(ChemicalSubstanceId):
    pass


class ProcessedMaterialId(ChemicalSubstanceId):
    pass


class DrugId(MolecularEntityId):
    pass


class FoodId(MolecularEntityId):
    pass


class MetaboliteId(ChemicalSubstanceId):
    pass


class OrganismalEntityId(BiologicalEntityId):
    pass


class LifeStageId(OrganismalEntityId):
    pass


class IndividualOrganismId(OrganismalEntityId):
    pass


class PopulationOfIndividualOrganismsId(OrganismalEntityId):
    pass


class StudyPopulationId(PopulationOfIndividualOrganismsId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class AnatomicalEntityId(OrganismalEntityId):
    pass


class CellularComponentId(AnatomicalEntityId):
    pass


class CellId(AnatomicalEntityId):
    pass


class CellLineId(OrganismalEntityId):
    pass


class GrossAnatomicalStructureId(AnatomicalEntityId):
    pass


class GenomicEntityId(MolecularEntityId):
    pass


class GenomeId(GenomicEntityId):
    pass


class ExonId(GenomicEntityId):
    pass


class CodingSequenceId(GenomicEntityId):
    pass


class MacromolecularMachineId(GenomicEntityId):
    pass


class GeneOrGeneProductId(MacromolecularMachineId):
    pass


class GeneId(GeneOrGeneProductId):
    pass


class GeneProductId(GeneOrGeneProductId):
    pass


class TranscriptId(GeneProductId):
    pass


class ProteinId(GeneProductId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class RNAProductId(GeneProductId):
    pass


class RNAProductIsoformId(RNAProductId):
    pass


class NoncodingRNAProductId(RNAProductId):
    pass


class MicroRNAId(NoncodingRNAProductId):
    pass


class SiRNAId(NoncodingRNAProductId):
    pass


class MacromolecularComplexId(MacromolecularMachineId):
    pass


class GeneFamilyId(MolecularEntityId):
    pass


class GenotypeId(GenomicEntityId):
    pass


class HaplotypeId(GenomicEntityId):
    pass


class SequenceVariantId(GenomicEntityId):
    pass


class SnvId(SequenceVariantId):
    pass


class ReagentTargetedGeneId(GenomicEntityId):
    pass


class ClinicalEntityId(NamedThingId):
    pass


class ClinicalTrialId(ClinicalEntityId):
    pass


class ClinicalInterventionId(ClinicalEntityId):
    pass


class ClinicalFindingId(PhenotypicFeatureId):
    pass


class HospitalizationId(ClinicalInterventionId):
    pass


class CaseId(IndividualOrganismId):
    pass


class CohortId(StudyPopulationId):
    pass


class GenomicBackgroundExposureId(GenomicEntityId):
    pass


class DiseaseOrPhenotypicFeatureExposureId(DiseaseOrPhenotypicFeatureId):
    pass


class ChemicalExposureId(ChemicalSubstanceId):
    pass


class ComplexChemicalExposureId(ChemicalExposureId):
    pass


class DrugExposureId(DrugId):
    pass


class DrugToGeneInteractionExposureId(DrugExposureId):
    pass


class TreatmentId(NamedThingId):
    pass


class BioticExposureId(OrganismTaxonId):
    pass


class GeographicExposureId(GeographicLocationId):
    pass


class EnvironmentalExposureId(EnvironmentalProcessId):
    pass


class BehavioralExposureId(BehaviorId):
    pass


class SocioeconomicExposureId(BehaviorId):
    pass


class DiseaseOrPhenotypicFeatureOutcomeId(DiseaseOrPhenotypicFeatureId):
    pass


class BehavioralOutcomeId(BehaviorId):
    pass


class HospitalizationOutcomeId(HospitalizationId):
    pass


class MortalityOutcomeId(DeathId):
    pass


class EpidemiologicalOutcomeId(BiologicalEntityId):
    pass


class SocioeconomicOutcomeId(BehaviorId):
    pass


class AssociationId(EntityId):
    pass


class ContributorAssociationId(AssociationId):
    pass


class GenotypeToGenotypePartAssociationId(AssociationId):
    pass


class GenotypeToGeneAssociationId(AssociationId):
    pass


class GenotypeToVariantAssociationId(AssociationId):
    pass


class GeneToGeneAssociationId(AssociationId):
    pass


class GeneToGeneHomologyAssociationId(GeneToGeneAssociationId):
    pass


class GeneToGeneCoexpressionAssociationId(GeneToGeneAssociationId):
    pass


class PairwiseGeneToGeneInteractionId(GeneToGeneAssociationId):
    pass


class PairwiseMolecularInteractionId(PairwiseGeneToGeneInteractionId):
    pass


class CellLineToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToChemicalAssociationId(AssociationId):
    pass


class ChemicalToChemicalDerivationAssociationId(ChemicalToChemicalAssociationId):
    pass


class ChemicalToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class ChemicalToPathwayAssociationId(AssociationId):
    pass


class ChemicalToGeneAssociationId(AssociationId):
    pass


class DrugToGeneAssociationId(AssociationId):
    pass


class MaterialSampleDerivationAssociationId(AssociationId):
    pass


class MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToExposureEventAssociationId(AssociationId):
    pass


class ExposureEventToOutcomeAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(AssociationId):
    pass


class DiseaseOrPhenotypicFeatureToLocationAssociationId(AssociationId):
    pass


class GenotypeToPhenotypicFeatureAssociationId(AssociationId):
    pass


class ExposureEventToPhenotypicFeatureAssociationId(AssociationId):
    pass


class DiseaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class CaseToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToPhenotypicFeatureAssociationId(AssociationId):
    pass


class GeneToDiseaseAssociationId(AssociationId):
    pass


class VariantToGeneAssociationId(AssociationId):
    pass


class VariantToGeneExpressionAssociationId(VariantToGeneAssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToPhenotypicFeatureAssociationId(AssociationId):
    pass


class VariantToDiseaseAssociationId(AssociationId):
    pass


class GenotypeToDiseaseAssociationId(AssociationId):
    pass


class GeneAsAModelOfDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class VariantAsAModelOfDiseaseAssociationId(VariantToDiseaseAssociationId):
    pass


class GenotypeAsAModelOfDiseaseAssociationId(GenotypeToDiseaseAssociationId):
    pass


class CellLineAsAModelOfDiseaseAssociationId(CellLineToDiseaseOrPhenotypicFeatureAssociationId):
    pass


class OrganismalEntityAsAModelOfDiseaseAssociationId(AssociationId):
    pass


class GeneHasVariantThatContributesToDiseaseAssociationId(GeneToDiseaseAssociationId):
    pass


class GeneToExpressionSiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesTreatmentAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacromolecularMachineToMolecularActivityAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToBiologicalProcessAssociationId(FunctionalAssociationId):
    pass


class MacromolecularMachineToCellularComponentAssociationId(FunctionalAssociationId):
    pass


class GeneToGoTermAssociationId(FunctionalAssociationId):
    pass


class SequenceAssociationId(AssociationId):
    pass


class GenomicSequenceLocalizationId(SequenceAssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class TranscriptToGeneRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneToGeneProductRelationshipId(SequenceFeatureRelationshipId):
    pass


class ExonToTranscriptRelationshipId(SequenceFeatureRelationshipId):
    pass


class GeneRegulatoryRelationshipId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityAssociationId(AssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityPartOfAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
    pass


class AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(AnatomicalEntityToAnatomicalEntityAssociationId):
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
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.QuantityValue
    class_class_curie: ClassVar[str] = "csolink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = CSOLINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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


@dataclass
class BiologicalSex(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.BiologicalSex
    class_class_curie: ClassVar[str] = "csolink:BiologicalSex"
    class_name: ClassVar[str] = "biological sex"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BiologicalSex

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PhenotypicSex
    class_class_curie: ClassVar[str] = "csolink:PhenotypicSex"
    class_name: ClassVar[str] = "phenotypic sex"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PhenotypicSex

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypicSex
    class_class_curie: ClassVar[str] = "csolink:GenotypicSex"
    class_name: ClassVar[str] = "genotypic sex"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypicSex

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
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
    A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the
    feature implies the existence of the disease
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneOntologyClass
    class_class_curie: ClassVar[str] = "csolink:GeneOntologyClass"
    class_name: ClassVar[str] = "gene ontology class"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneOntologyClass

    id: Union[str, GeneOntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneOntologyClassId):
            self.id = GeneOntologyClassId(self.id)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TaxonomicRankId):
            self.id = TaxonomicRankId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OrganismTaxon(OntologyClass):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrganismTaxon
    class_class_curie: ClassVar[str] = "csolink:OrganismTaxon"
    class_name: ClassVar[str] = "organism taxon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrganismTaxon

    id: Union[str, OrganismTaxonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None
    subclass_of: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.subclass_of]

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
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
class DataFile(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DataFile
    class_class_curie: ClassVar[str] = "csolink:DataFile"
    class_name: ClassVar[str] = "data file"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DataFile

    id: Union[str, DataFileId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataFileId):
            self.id = DataFileId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SourceFile(DataFile):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SourceFile
    class_class_curie: ClassVar[str] = "csolink:SourceFile"
    class_name: ClassVar[str] = "source file"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SourceFile

    id: Union[str, SourceFileId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    source_version: Optional[str] = None
    retrieved_on: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SourceFileId):
            self.id = SourceFileId(self.id)

        if self.source_version is not None and not isinstance(self.source_version, str):
            self.source_version = str(self.source_version)

        if self.retrieved_on is not None and not isinstance(self.retrieved_on, XSDDate):
            self.retrieved_on = XSDDate(self.retrieved_on)

        super().__post_init__(**kwargs)


@dataclass
class DataSet(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DataSet
    class_class_curie: ClassVar[str] = "csolink:DataSet"
    class_name: ClassVar[str] = "data set"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DataSet

    id: Union[str, DataSetId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataSetId):
            self.id = DataSetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DataSetVersion(DataSet):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DataSetVersion
    class_class_curie: ClassVar[str] = "csolink:DataSetVersion"
    class_name: ClassVar[str] = "data set version"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DataSetVersion

    id: Union[str, DataSetVersionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    source_data_file: Optional[Union[str, DataFileId]] = None
    version_of: Optional[Union[str, DataSetId]] = None
    distribution: Optional[Union[str, DistributionLevelId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataSetVersionId):
            self.id = DataSetVersionId(self.id)

        if self.source_data_file is not None and not isinstance(self.source_data_file, DataFileId):
            self.source_data_file = DataFileId(self.source_data_file)

        if self.version_of is not None and not isinstance(self.version_of, DataSetId):
            self.version_of = DataSetId(self.version_of)

        if self.distribution is not None and not isinstance(self.distribution, DistributionLevelId):
            self.distribution = DistributionLevelId(self.distribution)

        super().__post_init__(**kwargs)


@dataclass
class DistributionLevel(DataSetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DistributionLevel
    class_class_curie: ClassVar[str] = "csolink:DistributionLevel"
    class_name: ClassVar[str] = "distribution level"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DistributionLevel

    id: Union[str, DistributionLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    download_url: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.download_url is not None and not isinstance(self.download_url, str):
            self.download_url = str(self.download_url)

        super().__post_init__(**kwargs)


@dataclass
class DataSetSummary(DataSetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DataSetSummary
    class_class_curie: ClassVar[str] = "csolink:DataSetSummary"
    class_name: ClassVar[str] = "data set summary"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DataSetSummary

    id: Union[str, DataSetSummaryId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    source_web_page: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
    well as printed materials, either directly or in one of the Publication Csolink category subclasses.
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
    mesh_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

        if self.mesh_terms is None:
            self.mesh_terms = []
        if not isinstance(self.mesh_terms, list):
            self.mesh_terms = [self.mesh_terms]
        self.mesh_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.mesh_terms]

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
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Book
    class_class_curie: ClassVar[str] = "csolink:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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


class PhysicalEssenceOrOccurrent(YAMLRoot):
    """
    Either a physical or processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PhysicalEssenceOrOccurrent
    class_class_curie: ClassVar[str] = "csolink:PhysicalEssenceOrOccurrent"
    class_name: ClassVar[str] = "physical essence or occurrent"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PhysicalEssenceOrOccurrent


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PhysicalEssence
    class_class_curie: ClassVar[str] = "csolink:PhysicalEssence"
    class_name: ClassVar[str] = "physical essence"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PhysicalEssence


@dataclass
class PhysicalEntity(NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PhysicalEntity
    class_class_curie: ClassVar[str] = "csolink:PhysicalEntity"
    class_name: ClassVar[str] = "physical entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PhysicalEntity

    id: Union[str, PhysicalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PhysicalEntityId):
            self.id = PhysicalEntityId(self.id)

        super().__post_init__(**kwargs)


class Occurrent(PhysicalEssenceOrOccurrent):
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
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
class MaterialSample(PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MaterialSample
    class_class_curie: ClassVar[str] = "csolink:MaterialSample"
    class_name: ClassVar[str] = "material sample"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MaterialSample

    id: Union[str, MaterialSampleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.BiologicalEntity
    class_class_curie: ClassVar[str] = "csolink:BiologicalEntity"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms;
    genes, their products and other molecular entities; body parts; biological processes
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ThingWithTaxon
    class_class_curie: ClassVar[str] = "csolink:ThingWithTaxon"
    class_name: ClassVar[str] = "thing with taxon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class MolecularEntity(BiologicalEntity):
    """
    A gene, gene product, small molecule or macromolecule (including protein complex)"
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MolecularEntity
    class_class_curie: ClassVar[str] = "csolink:MolecularEntity"
    class_name: ClassVar[str] = "molecular entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MolecularEntity

    id: Union[str, MolecularEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularEntityId):
            self.id = MolecularEntityId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcessOrActivity(BiologicalEntity):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BiologicalProcessOrActivity
    class_class_curie: ClassVar[str] = "csolink:BiologicalProcessOrActivity"
    class_name: ClassVar[str] = "biological process or activity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BiologicalProcessOrActivity

    id: Union[str, BiologicalProcessOrActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, PhysicalEntityId], List[Union[str, PhysicalEntityId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BiologicalProcessOrActivityId):
            self.id = BiologicalProcessOrActivityId(self.id)

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
        self.enabled_by = [v if isinstance(v, PhysicalEntityId) else PhysicalEntityId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(BiologicalProcessOrActivity):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MolecularActivity
    class_class_curie: ClassVar[str] = "csolink:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, MacromolecularMachineId], List[Union[str, MacromolecularMachineId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        if self.has_input is None:
            self.has_input = []
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input]
        self.has_input = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_input]

        if self.has_output is None:
            self.has_output = []
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output]
        self.has_output = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_output]

        if self.enabled_by is None:
            self.enabled_by = []
        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by]
        self.enabled_by = [v if isinstance(v, MacromolecularMachineId) else MacromolecularMachineId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcess(BiologicalProcessOrActivity):
    """
    One or more causally connected executions of molecular functions
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BiologicalProcess
    class_class_curie: ClassVar[str] = "csolink:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Pathway
    class_class_curie: ClassVar[str] = "csolink:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Pathway

    id: Union[str, PathwayId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PhysiologicalProcess(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.PhysiologicalProcess
    class_class_curie: ClassVar[str] = "csolink:PhysiologicalProcess"
    class_name: ClassVar[str] = "physiological process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PhysiologicalProcess

    id: Union[str, PhysiologicalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PhysiologicalProcessId):
            self.id = PhysiologicalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PathologicalProcess(BiologicalProcess):
    """
    A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular,
    multicellular, or organismal level.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.PathologicalProcess
    class_class_curie: ClassVar[str] = "csolink:PathologicalProcess"
    class_name: ClassVar[str] = "pathological process"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PathologicalProcess

    id: Union[str, PathologicalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PathologicalProcessId):
            self.id = PathologicalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Behavior(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Behavior
    class_class_curie: ClassVar[str] = "csolink:Behavior"
    class_name: ClassVar[str] = "behavior"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Behavior

    id: Union[str, BehaviorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Death(BiologicalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Death
    class_class_curie: ClassVar[str] = "csolink:Death"
    class_name: ClassVar[str] = "death"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Death

    id: Union[str, DeathId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DeathId):
            self.id = DeathId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Mixture(YAMLRoot):
    """
    The physical combination of two or more molecular entities in which the identities are retained and are mixed in
    the form of solutions, suspensions and colloids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Mixture
    class_class_curie: ClassVar[str] = "csolink:Mixture"
    class_name: ClassVar[str] = "mixture"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Mixture

    has_constituent: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_constituent is None:
            self.has_constituent = []
        if not isinstance(self.has_constituent, list):
            self.has_constituent = [self.has_constituent]
        self.has_constituent = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_constituent]

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSubstance(MolecularEntity):
    """
    May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with
    multiple chemical entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalSubstance
    class_class_curie: ClassVar[str] = "csolink:ChemicalSubstance"
    class_name: ClassVar[str] = "chemical substance"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Carbohydrate(ChemicalSubstance):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Carbohydrate
    class_class_curie: ClassVar[str] = "csolink:Carbohydrate"
    class_name: ClassVar[str] = "carbohydrate"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Carbohydrate

    id: Union[str, CarbohydrateId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CarbohydrateId):
            self.id = CarbohydrateId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProcessedMaterial(ChemicalSubstance):
    """
    A chemical substance (often a mixture) processed for consumption for nutritional, medical or technical use.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ProcessedMaterial
    class_class_curie: ClassVar[str] = "csolink:ProcessedMaterial"
    class_name: ClassVar[str] = "processed material"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ProcessedMaterial

    id: Union[str, ProcessedMaterialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_constituent: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProcessedMaterialId):
            self.id = ProcessedMaterialId(self.id)

        if self.has_constituent is None:
            self.has_constituent = []
        if not isinstance(self.has_constituent, list):
            self.has_constituent = [self.has_constituent]
        self.has_constituent = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_constituent]

        super().__post_init__(**kwargs)


@dataclass
class Drug(MolecularEntity):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Drug
    class_class_curie: ClassVar[str] = "csolink:Drug"
    class_name: ClassVar[str] = "drug"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Drug

    id: Union[str, DrugId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_active_ingredient: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()
    has_excipient: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()
    has_constituent: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)

        if self.has_active_ingredient is None:
            self.has_active_ingredient = []
        if not isinstance(self.has_active_ingredient, list):
            self.has_active_ingredient = [self.has_active_ingredient]
        self.has_active_ingredient = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_active_ingredient]

        if self.has_excipient is None:
            self.has_excipient = []
        if not isinstance(self.has_excipient, list):
            self.has_excipient = [self.has_excipient]
        self.has_excipient = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_excipient]

        if self.has_constituent is None:
            self.has_constituent = []
        if not isinstance(self.has_constituent, list):
            self.has_constituent = [self.has_constituent]
        self.has_constituent = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_constituent]

        super().__post_init__(**kwargs)


@dataclass
class Food(MolecularEntity):
    """
    A substance consumed by a living organism as a source of nutrition
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Food
    class_class_curie: ClassVar[str] = "csolink:Food"
    class_name: ClassVar[str] = "food"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Food

    id: Union[str, FoodId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_nutrient: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()
    has_constituent: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FoodId):
            self.id = FoodId(self.id)

        if self.has_nutrient is None:
            self.has_nutrient = []
        if not isinstance(self.has_nutrient, list):
            self.has_nutrient = [self.has_nutrient]
        self.has_nutrient = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_nutrient]

        if self.has_constituent is None:
            self.has_constituent = []
        if not isinstance(self.has_constituent, list):
            self.has_constituent = [self.has_constituent]
        self.has_constituent = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_constituent]

        super().__post_init__(**kwargs)


@dataclass
class Metabolite(ChemicalSubstance):
    """
    Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Metabolite
    class_class_curie: ClassVar[str] = "csolink:Metabolite"
    class_name: ClassVar[str] = "metabolite"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Metabolite

    id: Union[str, MetaboliteId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MetaboliteId):
            self.id = MetaboliteId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OrganismAttribute(Attribute):
    """
    describes a characteristic of an organismal entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrganismAttribute
    class_class_curie: ClassVar[str] = "csolink:OrganismAttribute"
    class_name: ClassVar[str] = "organism attribute"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrganismAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Inheritance(OrganismAttribute):
    """
    The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next,
    e.g. autosomal dominant, autosomal recessive, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Inheritance
    class_class_curie: ClassVar[str] = "csolink:Inheritance"
    class_name: ClassVar[str] = "inheritance"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Inheritance

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    molecular entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrganismalEntity
    class_class_curie: ClassVar[str] = "csolink:OrganismalEntity"
    class_name: ClassVar[str] = "organismal entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrganismalEntity

    id: Union[str, OrganismalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class LifeStage(OrganismalEntity):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.LifeStage
    class_class_curie: ClassVar[str] = "csolink:LifeStage"
    class_name: ClassVar[str] = "life stage"
    class_model_uri: ClassVar[URIRef] = CSOLINK.LifeStage

    id: Union[str, LifeStageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, LifeStageId):
            self.id = LifeStageId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class IndividualOrganism(OrganismalEntity):
    """
    An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID:
    ORCID:0000-0002-5355-2576
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.IndividualOrganism
    class_class_curie: ClassVar[str] = "csolink:IndividualOrganism"
    class_name: ClassVar[str] = "individual organism"
    class_model_uri: ClassVar[URIRef] = CSOLINK.IndividualOrganism

    id: Union[str, IndividualOrganismId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, IndividualOrganismId):
            self.id = IndividualOrganismId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class PopulationOfIndividualOrganisms(OrganismalEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.PopulationOfIndividualOrganisms
    class_class_curie: ClassVar[str] = "csolink:PopulationOfIndividualOrganisms"
    class_name: ClassVar[str] = "population of individual organisms"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PopulationOfIndividualOrganisms

    id: Union[str, PopulationOfIndividualOrganismsId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PopulationOfIndividualOrganismsId):
            self.id = PopulationOfIndividualOrganismsId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class StudyPopulation(PopulationOfIndividualOrganisms):
    """
    A group of people banded together or treated as a group as participants in a research study.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.StudyPopulation
    class_class_curie: ClassVar[str] = "csolink:StudyPopulation"
    class_name: ClassVar[str] = "study population"
    class_model_uri: ClassVar[URIRef] = CSOLINK.StudyPopulation

    id: Union[str, StudyPopulationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, StudyPopulationId):
            self.id = StudyPopulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "csolink:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeature

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Disease
    class_class_curie: ClassVar[str] = "csolink:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Disease

    id: Union[str, DiseaseId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.PhenotypicFeature
    class_class_curie: ClassVar[str] = "csolink:PhenotypicFeature"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PhenotypicFeature

    id: Union[str, PhenotypicFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(OrganismalEntity):
    """
    A subcellular location, cell type or gross anatomical part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntity
    class_class_curie: ClassVar[str] = "csolink:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self.in_taxon is None:
            self.in_taxon = []
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon]
        self.in_taxon = [v if isinstance(v, OrganismTaxonId) else OrganismTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.CellularComponent
    class_class_curie: ClassVar[str] = "csolink:CellularComponent"
    class_name: ClassVar[str] = "cellular component"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CellularComponent

    id: Union[str, CellularComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cell(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Cell
    class_class_curie: ClassVar[str] = "csolink:Cell"
    class_name: ClassVar[str] = "cell"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Cell

    id: Union[str, CellId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CellId):
            self.id = CellId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CellLine(OrganismalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CellLine
    class_class_curie: ClassVar[str] = "csolink:CellLine"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CellLine

    id: Union[str, CellLineId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GrossAnatomicalStructure(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GrossAnatomicalStructure
    class_class_curie: ClassVar[str] = "csolink:GrossAnatomicalStructure"
    class_name: ClassVar[str] = "gross anatomical structure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GrossAnatomicalStructure

    id: Union[str, GrossAnatomicalStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GrossAnatomicalStructureId):
            self.id = GrossAnatomicalStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GenomicEntity(MolecularEntity):
    """
    an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is
    encoded in a genome (protein)
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenomicEntity
    class_class_curie: ClassVar[str] = "csolink:GenomicEntity"
    class_name: ClassVar[str] = "genomic entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenomicEntity

    id: Union[str, GenomicEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenomicEntityId):
            self.id = GenomicEntityId(self.id)

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)


@dataclass
class Genome(GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Genome
    class_class_curie: ClassVar[str] = "csolink:Genome"
    class_name: ClassVar[str] = "genome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Genome

    id: Union[str, GenomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenomeId):
            self.id = GenomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Exon(GenomicEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Exon
    class_class_curie: ClassVar[str] = "csolink:Exon"
    class_name: ClassVar[str] = "exon"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Exon

    id: Union[str, ExonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExonId):
            self.id = ExonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CodingSequence(GenomicEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.CodingSequence
    class_class_curie: ClassVar[str] = "csolink:CodingSequence"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachine(GenomicEntity):
    """
    A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They
    either carry out individual biological activities, or they encode molecules which do this.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachine
    class_class_curie: ClassVar[str] = "csolink:MacromolecularMachine"
    class_name: ClassVar[str] = "macromolecular machine"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachine

    id: Union[str, MacromolecularMachineId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    name: Optional[Union[str, SymbolType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacromolecularMachineId):
            self.id = MacromolecularMachineId(self.id)

        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class GeneOrGeneProduct(MacromolecularMachine):
    """
    a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneOrGeneProduct
    class_class_curie: ClassVar[str] = "csolink:GeneOrGeneProduct"
    class_name: ClassVar[str] = "gene or gene product"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneOrGeneProduct

    id: Union[str, GeneOrGeneProductId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneOrGeneProductId):
            self.id = GeneOrGeneProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Gene(GeneOrGeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Gene
    class_class_curie: ClassVar[str] = "csolink:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Gene

    id: Union[str, GeneId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    symbol: Optional[str] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

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
class GeneProduct(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneProduct
    class_class_curie: ClassVar[str] = "csolink:GeneProduct"
    class_name: ClassVar[str] = "gene product"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneProduct

    id: Union[str, GeneProductId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneProductId):
            self.id = GeneProductId(self.id)

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
class Transcript(GeneProduct):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Transcript
    class_class_curie: ClassVar[str] = "csolink:Transcript"
    class_name: ClassVar[str] = "transcript"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Transcript

    id: Union[str, TranscriptId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TranscriptId):
            self.id = TranscriptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Protein(GeneProduct):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Protein
    class_class_curie: ClassVar[str] = "csolink:Protein"
    class_name: ClassVar[str] = "protein"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Protein

    id: Union[str, ProteinId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        super().__post_init__(**kwargs)


class GeneProductIsoform(YAMLRoot):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneProductIsoform
    class_class_curie: ClassVar[str] = "csolink:GeneProductIsoform"
    class_name: ClassVar[str] = "gene product isoform"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneProductIsoform


@dataclass
class ProteinIsoform(Protein):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ProteinIsoform
    class_class_curie: ClassVar[str] = "csolink:ProteinIsoform"
    class_name: ClassVar[str] = "protein isoform"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ProteinIsoform

    id: Union[str, ProteinIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RNAProduct(GeneProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.RNAProduct
    class_class_curie: ClassVar[str] = "csolink:RNAProduct"
    class_name: ClassVar[str] = "RNA product"
    class_model_uri: ClassVar[URIRef] = CSOLINK.RNAProduct

    id: Union[str, RNAProductId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RNAProductId):
            self.id = RNAProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RNAProductIsoform(RNAProduct):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.RNAProductIsoform
    class_class_curie: ClassVar[str] = "csolink:RNAProductIsoform"
    class_name: ClassVar[str] = "RNA product isoform"
    class_model_uri: ClassVar[URIRef] = CSOLINK.RNAProductIsoform

    id: Union[str, RNAProductIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, RNAProductIsoformId):
            self.id = RNAProductIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NoncodingRNAProduct(RNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.NoncodingRNAProduct
    class_class_curie: ClassVar[str] = "csolink:NoncodingRNAProduct"
    class_name: ClassVar[str] = "noncoding RNA product"
    class_model_uri: ClassVar[URIRef] = CSOLINK.NoncodingRNAProduct

    id: Union[str, NoncodingRNAProductId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NoncodingRNAProductId):
            self.id = NoncodingRNAProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MicroRNA(NoncodingRNAProduct):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MicroRNA
    class_class_curie: ClassVar[str] = "csolink:MicroRNA"
    class_name: ClassVar[str] = "microRNA"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MicroRNA

    id: Union[str, MicroRNAId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MicroRNAId):
            self.id = MicroRNAId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SiRNA(NoncodingRNAProduct):
    """
    A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular
    duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both
    strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.SiRNA
    class_class_curie: ClassVar[str] = "csolink:SiRNA"
    class_name: ClassVar[str] = "siRNA"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SiRNA

    id: Union[str, SiRNAId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SiRNAId):
            self.id = SiRNAId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MacromolecularComplex(MacromolecularMachine):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacromolecularComplex
    class_class_curie: ClassVar[str] = "csolink:MacromolecularComplex"
    class_name: ClassVar[str] = "macromolecular complex"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacromolecularComplex

    id: Union[str, MacromolecularComplexId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacromolecularComplexId):
            self.id = MacromolecularComplexId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeneGroupingMixin(YAMLRoot):
    """
    any grouping of multiple genes or gene products
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneGroupingMixin
    class_class_curie: ClassVar[str] = "csolink:GeneGroupingMixin"
    class_name: ClassVar[str] = "gene grouping mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneGroupingMixin

    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_gene_or_gene_product is None:
            self.has_gene_or_gene_product = []
        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product]
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)


@dataclass
class GeneFamily(MolecularEntity):
    """
    any grouping of multiple genes or gene products related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneFamily
    class_class_curie: ClassVar[str] = "csolink:GeneFamily"
    class_name: ClassVar[str] = "gene family"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneFamily

    id: Union[str, GeneFamilyId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneFamilyId):
            self.id = GeneFamilyId(self.id)

        if self.has_gene_or_gene_product is None:
            self.has_gene_or_gene_product = []
        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product]
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)


@dataclass
class Zygosity(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Zygosity
    class_class_curie: ClassVar[str] = "csolink:Zygosity"
    class_name: ClassVar[str] = "zygosity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Zygosity

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Genotype(GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some established background
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Genotype
    class_class_curie: ClassVar[str] = "csolink:Genotype"
    class_name: ClassVar[str] = "genotype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Genotype

    id: Union[str, GenotypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_zygosity: Optional[Union[dict, Zygosity]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeId):
            self.id = GenotypeId(self.id)

        if self.has_zygosity is not None and not isinstance(self.has_zygosity, Zygosity):
            self.has_zygosity = Zygosity(**self.has_zygosity)

        super().__post_init__(**kwargs)


@dataclass
class Haplotype(GenomicEntity):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Haplotype
    class_class_curie: ClassVar[str] = "csolink:Haplotype"
    class_name: ClassVar[str] = "haplotype"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Haplotype

    id: Union[str, HaplotypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, HaplotypeId):
            self.id = HaplotypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariant(GenomicEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.SequenceVariant
    class_class_curie: ClassVar[str] = "csolink:SequenceVariant"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_gene: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)

        if self.has_gene is None:
            self.has_gene = []
        if not isinstance(self.has_gene, list):
            self.has_gene = [self.has_gene]
        self.has_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene]

        if self.has_biological_sequence is not None and not isinstance(self.has_biological_sequence, BiologicalSequence):
            self.has_biological_sequence = BiologicalSequence(self.has_biological_sequence)

        super().__post_init__(**kwargs)


@dataclass
class Snv(SequenceVariant):
    """
    SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Snv
    class_class_curie: ClassVar[str] = "csolink:Snv"
    class_name: ClassVar[str] = "snv"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Snv

    id: Union[str, SnvId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SnvId):
            self.id = SnvId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ReagentTargetedGene(GenomicEntity):
    """
    A gene altered in its expression level in the context of some experiment as a result of being targeted by
    gene-knockdown reagent(s) such as a morpholino or RNAi.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ReagentTargetedGene
    class_class_curie: ClassVar[str] = "csolink:ReagentTargetedGene"
    class_name: ClassVar[str] = "reagent targeted gene"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ReagentTargetedGene

    id: Union[str, ReagentTargetedGeneId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ReagentTargetedGeneId):
            self.id = ReagentTargetedGeneId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalAttribute(Attribute):
    """
    Attributes relating to a clinical manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalAttribute
    class_class_curie: ClassVar[str] = "csolink:ClinicalAttribute"
    class_name: ClassVar[str] = "clinical attribute"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ClinicalMeasurement(ClinicalAttribute):
    """
    A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject
    individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalMeasurement
    class_class_curie: ClassVar[str] = "csolink:ClinicalMeasurement"
    class_name: ClassVar[str] = "clinical measurement"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalMeasurement

    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_attribute_type is None:
            raise ValueError("has_attribute_type must be supplied")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalModifier(ClinicalAttribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology,
    with respect to severity, laterality, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalModifier
    class_class_curie: ClassVar[str] = "csolink:ClinicalModifier"
    class_name: ClassVar[str] = "clinical modifier"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalModifier

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ClinicalCourse(ClinicalAttribute):
    """
    The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the
    affected individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalCourse
    class_class_curie: ClassVar[str] = "csolink:ClinicalCourse"
    class_name: ClassVar[str] = "clinical course"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalCourse

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Onset(ClinicalCourse):
    """
    The age group in which (disease) symptom manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Onset
    class_class_curie: ClassVar[str] = "csolink:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Onset

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalEntity
    class_class_curie: ClassVar[str] = "csolink:ClinicalEntity"
    class_name: ClassVar[str] = "clinical entity"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalEntity

    id: Union[str, ClinicalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalTrial(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalTrial
    class_class_curie: ClassVar[str] = "csolink:ClinicalTrial"
    class_name: ClassVar[str] = "clinical trial"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalTrial

    id: Union[str, ClinicalTrialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalIntervention(ClinicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalIntervention
    class_class_curie: ClassVar[str] = "csolink:ClinicalIntervention"
    class_name: ClassVar[str] = "clinical intervention"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalIntervention

    id: Union[str, ClinicalInterventionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ClinicalInterventionId):
            self.id = ClinicalInterventionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalFinding(PhenotypicFeature):
    """
    this category is currently considered broad enough to tag clinical lab measurements and other biological
    attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ClinicalFinding
    class_class_curie: ClassVar[str] = "csolink:ClinicalFinding"
    class_name: ClassVar[str] = "clinical finding"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ClinicalFinding

    id: Union[str, ClinicalFindingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, ClinicalAttribute], List[Union[dict, ClinicalAttribute]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ClinicalFindingId):
            self.id = ClinicalFindingId(self.id)

        if self.has_attribute is None:
            self.has_attribute = []
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute]
        self._normalize_inlined_slot(slot_name="has_attribute", slot_type=ClinicalAttribute, key_name="has attribute type", inlined_as_list=True, keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Hospitalization(ClinicalIntervention):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Hospitalization
    class_class_curie: ClassVar[str] = "csolink:Hospitalization"
    class_name: ClassVar[str] = "hospitalization"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Hospitalization

    id: Union[str, HospitalizationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, HospitalizationId):
            self.id = HospitalizationId(self.id)

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
class Case(IndividualOrganism):
    """
    An individual (human) organism that has a patient role in some clinical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Case
    class_class_curie: ClassVar[str] = "csolink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Case

    id: Union[str, CaseId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cohort(StudyPopulation):
    """
    A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a
    particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.Cohort
    class_class_curie: ClassVar[str] = "csolink:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Cohort

    id: Union[str, CohortId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(YAMLRoot):
    """
    A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more
    phenotypic features of that organism, potentially mediated by genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExposureEvent
    class_class_curie: ClassVar[str] = "csolink:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExposureEvent

    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class GenomicBackgroundExposure(GenomicEntity):
    """
    A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or
    other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing
    an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenomicBackgroundExposure
    class_class_curie: ClassVar[str] = "csolink:GenomicBackgroundExposure"
    class_name: ClassVar[str] = "genomic background exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenomicBackgroundExposure

    id: Union[str, GenomicBackgroundExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenomicBackgroundExposureId):
            self.id = GenomicBackgroundExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if self.has_gene_or_gene_product is None:
            self.has_gene_or_gene_product = []
        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product]
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureExposure(DiseaseOrPhenotypicFeature):
    """
    A disease or phenotypic feature exposure is where a disease state is manifested which represents an precondition,
    leading to or influencing an outcome, e.g. hypertension leading to a related disease outcome such as
    cardiovascular disease.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureExposure
    class_class_curie: ClassVar[str] = "csolink:DiseaseOrPhenotypicFeatureExposure"
    class_name: ClassVar[str] = "disease or phenotypic feature exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureExposure

    id: Union[str, DiseaseOrPhenotypicFeatureExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureExposureId):
            self.id = DiseaseOrPhenotypicFeatureExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalExposure(ChemicalSubstance):
    """
    A chemical exposure is an intake of a particular chemical substance, other than a drug.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalExposure
    class_class_curie: ClassVar[str] = "csolink:ChemicalExposure"
    class_name: ClassVar[str] = "chemical exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalExposure

    id: Union[str, ChemicalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ComplexChemicalExposure(ChemicalExposure):
    """
    A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.ComplexChemicalExposure
    class_class_curie: ClassVar[str] = "csolink:ComplexChemicalExposure"
    class_name: ClassVar[str] = "complex chemical exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ComplexChemicalExposure

    id: Union[str, ComplexChemicalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_constituent: Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ComplexChemicalExposureId):
            self.id = ComplexChemicalExposureId(self.id)

        if self.has_constituent is None:
            self.has_constituent = []
        if not isinstance(self.has_constituent, list):
            self.has_constituent = [self.has_constituent]
        self.has_constituent = [v if isinstance(v, ChemicalSubstanceId) else ChemicalSubstanceId(v) for v in self.has_constituent]

        super().__post_init__(**kwargs)


@dataclass
class DrugExposure(Drug):
    """
    A drug exposure is an intake of a particular drug.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.DrugExposure
    class_class_curie: ClassVar[str] = "csolink:DrugExposure"
    class_name: ClassVar[str] = "drug exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DrugExposure

    id: Union[str, DrugExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DrugExposureId):
            self.id = DrugExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class DrugToGeneInteractionExposure(DrugExposure):
    """
    drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are
    known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.DrugToGeneInteractionExposure
    class_class_curie: ClassVar[str] = "csolink:DrugToGeneInteractionExposure"
    class_name: ClassVar[str] = "drug to gene interaction exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DrugToGeneInteractionExposure

    id: Union[str, DrugToGeneInteractionExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_gene_or_gene_product: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DrugToGeneInteractionExposureId):
            self.id = DrugToGeneInteractionExposureId(self.id)

        if self.has_gene_or_gene_product is None:
            self.has_gene_or_gene_product = []
        if not isinstance(self.has_gene_or_gene_product, list):
            self.has_gene_or_gene_product = [self.has_gene_or_gene_product]
        self.has_gene_or_gene_product = [v if isinstance(v, GeneId) else GeneId(v) for v in self.has_gene_or_gene_product]

        super().__post_init__(**kwargs)


@dataclass
class Treatment(NamedThing):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices
    and/or procedures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Treatment
    class_class_curie: ClassVar[str] = "csolink:Treatment"
    class_name: ClassVar[str] = "treatment"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Treatment

    id: Union[str, TreatmentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_drug: Optional[Union[Union[str, DrugId], List[Union[str, DrugId]]]] = empty_list()
    has_device: Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)

        if self.has_drug is None:
            self.has_drug = []
        if not isinstance(self.has_drug, list):
            self.has_drug = [self.has_drug]
        self.has_drug = [v if isinstance(v, DrugId) else DrugId(v) for v in self.has_drug]

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
class BioticExposure(OrganismTaxon):
    """
    A biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses)
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BioticExposure
    class_class_curie: ClassVar[str] = "csolink:BioticExposure"
    class_name: ClassVar[str] = "biotic exposure"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BioticExposure

    id: Union[str, BioticExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
    various categories of possible biological or non-biological (e.g. clinical) outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.Outcome
    class_class_curie: ClassVar[str] = "csolink:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.Outcome


@dataclass
class DiseaseOrPhenotypicFeatureOutcome(DiseaseOrPhenotypicFeature):
    """
    Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other
    characteristic phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureOutcome
    class_class_curie: ClassVar[str] = "csolink:DiseaseOrPhenotypicFeatureOutcome"
    class_name: ClassVar[str] = "disease or phenotypic feature outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureOutcome

    id: Union[str, DiseaseOrPhenotypicFeatureOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureOutcomeId):
            self.id = DiseaseOrPhenotypicFeatureOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralOutcome(Behavior):
    """
    An outcome resulting from an exposure event which is the manifestation of human behavior.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = CSOLINK.BehavioralOutcome
    class_class_curie: ClassVar[str] = "csolink:BehavioralOutcome"
    class_name: ClassVar[str] = "behavioral outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.BehavioralOutcome

    id: Union[str, BehavioralOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, BehavioralOutcomeId):
            self.id = BehavioralOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class HospitalizationOutcome(Hospitalization):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room
    visit) or chronic (inpatient) hospitalization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.HospitalizationOutcome
    class_class_curie: ClassVar[str] = "csolink:HospitalizationOutcome"
    class_name: ClassVar[str] = "hospitalization outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.HospitalizationOutcome

    id: Union[str, HospitalizationOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, HospitalizationOutcomeId):
            self.id = HospitalizationOutcomeId(self.id)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MortalityOutcomeId):
            self.id = MortalityOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EpidemiologicalOutcome(BiologicalEntity):
    """
    An epidemiological outcome, such as societal disease burden, resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EpidemiologicalOutcome
    class_class_curie: ClassVar[str] = "csolink:EpidemiologicalOutcome"
    class_name: ClassVar[str] = "epidemiological outcome"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EpidemiologicalOutcome

    id: Union[str, EpidemiologicalOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
    negated: Optional[Bool] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    type: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeToGenotypePartAssociation
    class_class_curie: ClassVar[str] = "csolink:GenotypeToGenotypePartAssociation"
    class_name: ClassVar[str] = "genotype to genotype part association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeToGenotypePartAssociation

    id: Union[str, GenotypeToGenotypePartAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, GenotypeId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeToGenotypePartAssociationId):
            self.id = GenotypeToGenotypePartAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GenotypeId):
            self.object = GenotypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeToGeneAssociation
    class_class_curie: ClassVar[str] = "csolink:GenotypeToGeneAssociation"
    class_name: ClassVar[str] = "genotype to gene association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeToGeneAssociation

    id: Union[str, GenotypeToGeneAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, GeneId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeToGeneAssociationId):
            self.id = GenotypeToGeneAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeToVariantAssociation
    class_class_curie: ClassVar[str] = "csolink:GenotypeToVariantAssociation"
    class_name: ClassVar[str] = "genotype to variant association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeToVariantAssociation

    id: Union[str, GenotypeToVariantAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    object: Union[str, SequenceVariantId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeToVariantAssociationId):
            self.id = GenotypeToVariantAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToGeneAssociation"
    class_name: ClassVar[str] = "gene to gene association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneAssociation

    id: Union[str, GeneToGeneAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneHomologyAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToGeneHomologyAssociation"
    class_name: ClassVar[str] = "gene to gene homology association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneHomologyAssociation

    id: Union[str, GeneToGeneHomologyAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToGeneHomologyAssociationId):
            self.id = GeneToGeneHomologyAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class GeneExpressionMixin(YAMLRoot):
    """
    Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the
    expression occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneExpressionMixin
    class_class_curie: ClassVar[str] = "csolink:GeneExpressionMixin"
    class_name: ClassVar[str] = "gene expression mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneExpressionMixin

    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    expression_site: Optional[Union[str, AnatomicalEntityId]] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    phenotypic_state: Optional[Union[str, DiseaseOrPhenotypicFeatureId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.expression_site is not None and not isinstance(self.expression_site, AnatomicalEntityId):
            self.expression_site = AnatomicalEntityId(self.expression_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.phenotypic_state is not None and not isinstance(self.phenotypic_state, DiseaseOrPhenotypicFeatureId):
            self.phenotypic_state = DiseaseOrPhenotypicFeatureId(self.phenotypic_state)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneCoexpressionAssociation(GeneToGeneAssociation):
    """
    Indicates that two genes are co-expressed, generally under the same conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneCoexpressionAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToGeneCoexpressionAssociation"
    class_name: ClassVar[str] = "gene to gene coexpression association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneCoexpressionAssociation

    id: Union[str, GeneToGeneCoexpressionAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    expression_site: Optional[Union[str, AnatomicalEntityId]] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    phenotypic_state: Optional[Union[str, DiseaseOrPhenotypicFeatureId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToGeneCoexpressionAssociationId):
            self.id = GeneToGeneCoexpressionAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.expression_site is not None and not isinstance(self.expression_site, AnatomicalEntityId):
            self.expression_site = AnatomicalEntityId(self.expression_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.phenotypic_state is not None and not isinstance(self.phenotypic_state, DiseaseOrPhenotypicFeatureId):
            self.phenotypic_state = DiseaseOrPhenotypicFeatureId(self.phenotypic_state)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PairwiseGeneToGeneInteraction
    class_class_curie: ClassVar[str] = "csolink:PairwiseGeneToGeneInteraction"
    class_name: ClassVar[str] = "pairwise gene to gene interaction"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PairwiseGeneToGeneInteraction

    id: Union[str, PairwiseGeneToGeneInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PairwiseGeneToGeneInteractionId):
            self.id = PairwiseGeneToGeneInteractionId(self.id)

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
class PairwiseMolecularInteraction(PairwiseGeneToGeneInteraction):
    """
    An interaction at the molecular level between two physical entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.PairwiseMolecularInteraction
    class_class_curie: ClassVar[str] = "csolink:PairwiseMolecularInteraction"
    class_name: ClassVar[str] = "pairwise molecular interaction"
    class_model_uri: ClassVar[URIRef] = CSOLINK.PairwiseMolecularInteraction

    id: Union[str, PairwiseMolecularInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, MolecularEntityId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, MolecularEntityId] = None
    interacting_molecules_category: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PairwiseMolecularInteractionId):
            self.id = PairwiseMolecularInteractionId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)

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
        if not isinstance(self.object, MolecularEntityId):
            self.object = MolecularEntityId(self.object)

        if self.interacting_molecules_category is not None and not isinstance(self.interacting_molecules_category, OntologyClassId):
            self.interacting_molecules_category = OntologyClassId(self.interacting_molecules_category)

        super().__post_init__(**kwargs)


@dataclass
class CellLineToEntityAssociationMixin(YAMLRoot):
    """
    An relationship between a cell line and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CellLineToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:CellLineToEntityAssociationMixin"
    class_name: ClassVar[str] = "cell line to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CellLineToEntityAssociationMixin

    subject: Union[str, CellLineId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class CellLineToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:CellLineToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "cell line to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CellLineToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, CellLineToDiseaseOrPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CellLineToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = CellLineToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class MolecularEntityToEntityAssociationMixin(YAMLRoot):
    """
    An interaction between a molecular entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MolecularEntityToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:MolecularEntityToEntityAssociationMixin"
    class_name: ClassVar[str] = "molecular entity to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MolecularEntityToEntityAssociationMixin

    subject: Union[str, MolecularEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class DrugToEntityAssociationMixin(MolecularEntityToEntityAssociationMixin):
    """
    An interaction between a drug and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DrugToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:DrugToEntityAssociationMixin"
    class_name: ClassVar[str] = "drug to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DrugToEntityAssociationMixin

    subject: Union[str, DrugId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalToEntityAssociationMixin(MolecularEntityToEntityAssociationMixin):
    """
    An interaction between a chemical entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ChemicalToEntityAssociationMixin"
    class_name: ClassVar[str] = "chemical to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalToEntityAssociationMixin

    subject: Union[str, ChemicalSubstanceId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalToChemicalAssociation(Association):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal
    edges, e.g. one chemical converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalToChemicalAssociation
    class_class_curie: ClassVar[str] = "csolink:ChemicalToChemicalAssociation"
    class_name: ClassVar[str] = "chemical to chemical association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalToChemicalAssociation

    id: Union[str, ChemicalToChemicalAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ChemicalSubstanceId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalToChemicalAssociationId):
            self.id = ChemicalToChemicalAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ChemicalSubstanceId):
            self.object = ChemicalSubstanceId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalToChemicalDerivationAssociation(ChemicalToChemicalAssociation):
    """
    A causal relationship between two chemical entities, where the subject represents the upstream entity and the
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

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalToChemicalDerivationAssociation
    class_class_curie: ClassVar[str] = "csolink:ChemicalToChemicalDerivationAssociation"
    class_name: ClassVar[str] = "chemical to chemical derivation association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalToChemicalDerivationAssociation

    id: Union[str, ChemicalToChemicalDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ChemicalSubstanceId] = None
    object: Union[str, ChemicalSubstanceId] = None
    predicate: Union[str, PredicateType] = None
    catalyst_qualifier: Optional[Union[Union[str, MacromolecularMachineId], List[Union[str, MacromolecularMachineId]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalToChemicalDerivationAssociationId):
            self.id = ChemicalToChemicalDerivationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ChemicalSubstanceId):
            self.subject = ChemicalSubstanceId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ChemicalSubstanceId):
            self.object = ChemicalSubstanceId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.catalyst_qualifier is None:
            self.catalyst_qualifier = []
        if not isinstance(self.catalyst_qualifier, list):
            self.catalyst_qualifier = [self.catalyst_qualifier]
        self.catalyst_qualifier = [v if isinstance(v, MacromolecularMachineId) else MacromolecularMachineId(v) for v in self.catalyst_qualifier]

        super().__post_init__(**kwargs)


@dataclass
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "chemical to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, ChemicalToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = ChemicalToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalToPathwayAssociation(Association):
    """
    An interaction between a chemical entity and a biological process or pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalToPathwayAssociation
    class_class_curie: ClassVar[str] = "csolink:ChemicalToPathwayAssociation"
    class_name: ClassVar[str] = "chemical to pathway association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalToPathwayAssociation

    id: Union[str, ChemicalToPathwayAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalToPathwayAssociationId):
            self.id = ChemicalToPathwayAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalToGeneAssociation(Association):
    """
    An interaction between a chemical entity and a gene or gene product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ChemicalToGeneAssociation
    class_class_curie: ClassVar[str] = "csolink:ChemicalToGeneAssociation"
    class_name: ClassVar[str] = "chemical to gene association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ChemicalToGeneAssociation

    id: Union[str, ChemicalToGeneAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChemicalToGeneAssociationId):
            self.id = ChemicalToGeneAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DrugToGeneAssociation(Association):
    """
    An interaction between a drug and a gene or gene product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DrugToGeneAssociation
    class_class_curie: ClassVar[str] = "csolink:DrugToGeneAssociation"
    class_name: ClassVar[str] = "drug to gene association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DrugToGeneAssociation

    id: Union[str, DrugToGeneAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DrugToGeneAssociationId):
            self.id = DrugToGeneAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleToEntityAssociationMixin(YAMLRoot):
    """
    An association between a material sample and something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MaterialSampleToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:MaterialSampleToEntityAssociationMixin"
    class_name: ClassVar[str] = "material sample to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MaterialSampleToEntityAssociationMixin

    subject: Union[str, MaterialSampleId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity from which it is derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MaterialSampleDerivationAssociation
    class_class_curie: ClassVar[str] = "csolink:MaterialSampleDerivationAssociation"
    class_name: ClassVar[str] = "material sample derivation association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MaterialSampleDerivationAssociation

    id: Union[str, MaterialSampleDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, MaterialSampleId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MaterialSampleDerivationAssociationId):
            self.id = MaterialSampleDerivationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MaterialSampleId):
            self.subject = MaterialSampleId(self.subject)

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
class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(Association):
    """
    An association between a material sample and a disease or phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "material sample to disease or phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MaterialSampleToDiseaseOrPhenotypicFeatureAssociation

    id: Union[str, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId):
            self.id = MaterialSampleToDiseaseOrPhenotypicFeatureAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:DiseaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "disease to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseToEntityAssociationMixin

    subject: Union[str, DiseaseId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ExposureEvent):
            self.object = ExposureEvent(**self.object)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseToExposureEventAssociation(Association):
    """
    An association between an exposure event and a disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseToExposureEventAssociation
    class_class_curie: ClassVar[str] = "csolink:DiseaseToExposureEventAssociation"
    class_name: ClassVar[str] = "disease to exposure event association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseToExposureEventAssociation

    id: Union[str, DiseaseToExposureEventAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseToExposureEventAssociationId):
            self.id = DiseaseToExposureEventAssociationId(self.id)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
    has_population_context: Optional[Union[str, PopulationOfIndividualOrganismsId]] = None
    has_temporal_context: Optional[Union[str, TimeType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExposureEventToOutcomeAssociationId):
            self.id = ExposureEventToOutcomeAssociationId(self.id)

        if self.has_population_context is not None and not isinstance(self.has_population_context, PopulationOfIndividualOrganismsId):
            self.has_population_context = PopulationOfIndividualOrganismsId(self.has_population_context)

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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**self.frequency_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToFeatureOrDiseaseQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to disease or phenotype associations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToFeatureOrDiseaseQualifiersMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToFeatureOrDiseaseQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or disease qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToFeatureOrDiseaseQualifiersMixin

    severity_qualifier: Optional[Union[dict, SeverityValue]] = None
    onset_qualifier: Optional[Union[dict, Onset]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValue):
            self.severity_qualifier = SeverityValue(**self.severity_qualifier)

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, Onset):
            self.onset_qualifier = Onset(**self.onset_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class EntityToPhenotypicFeatureAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToPhenotypicFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToPhenotypicFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to phenotypic feature association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToPhenotypicFeatureAssociationMixin

    object: Union[str, PhenotypicFeatureId] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PhenotypicFeatureId):
            self.object = PhenotypicFeatureId(self.object)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        super().__post_init__(**kwargs)


@dataclass
class EntityToDiseaseAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToDiseaseAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToDiseaseAssociationMixin"
    class_name: ClassVar[str] = "entity to disease association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToDiseaseAssociationMixin

    object: Union[str, DiseaseId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:DiseaseOrPhenotypicFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "disease or phenotypic feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureToEntityAssociationMixin

    subject: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, DiseaseOrPhenotypicFeatureId):
            self.subject = DiseaseOrPhenotypicFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureAssociationToLocationAssociation
    class_class_curie: ClassVar[str] = "csolink:DiseaseOrPhenotypicFeatureAssociationToLocationAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature association to location association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureAssociationToLocationAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureAssociationToLocationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeatureToLocationAssociation(Association):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureToLocationAssociation
    class_class_curie: ClassVar[str] = "csolink:DiseaseOrPhenotypicFeatureToLocationAssociation"
    class_name: ClassVar[str] = "disease or phenotypic feature to location association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseOrPhenotypicFeatureToLocationAssociation

    id: Union[str, DiseaseOrPhenotypicFeatureToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureToLocationAssociationId):
            self.id = DiseaseOrPhenotypicFeatureToLocationAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntityToDiseaseOrPhenotypicFeatureAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.EntityToDiseaseOrPhenotypicFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:EntityToDiseaseOrPhenotypicFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to disease or phenotypic feature association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.EntityToDiseaseOrPhenotypicFeatureAssociationMixin

    object: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, DiseaseOrPhenotypicFeatureId):
            self.object = DiseaseOrPhenotypicFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GenotypeToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:GenotypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "genotype to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeToEntityAssociationMixin

    subject: Union[str, GenotypeId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class GenotypeToPhenotypicFeatureAssociation(Association):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:GenotypeToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "genotype to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeToPhenotypicFeatureAssociation

    id: Union[str, GenotypeToPhenotypicFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GenotypeId] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeToPhenotypicFeatureAssociationId):
            self.id = GenotypeToPhenotypicFeatureAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToPhenotypicFeatureAssociation(Association):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:ExposureEventToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExposureEventToPhenotypicFeatureAssociation

    id: Union[str, ExposureEventToPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ExposureEvent] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExposureEventToPhenotypicFeatureAssociationId):
            self.id = ExposureEventToPhenotypicFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.DiseaseToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:DiseaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "disease to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.DiseaseToPhenotypicFeatureAssociation

    id: Union[str, DiseaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DiseaseToPhenotypicFeatureAssociationId):
            self.id = DiseaseToPhenotypicFeatureAssociationId(self.id)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class CaseToPhenotypicFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CaseToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:CaseToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "case to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CaseToPhenotypicFeatureAssociation

    id: Union[str, CaseToPhenotypicFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CaseToPhenotypicFeatureAssociationId):
            self.id = CaseToPhenotypicFeatureAssociationId(self.id)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class GeneToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:GeneToEntityAssociationMixin"
    class_name: ClassVar[str] = "gene to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToEntityAssociationMixin

    subject: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:VariantToEntityAssociationMixin"
    class_name: ClassVar[str] = "variant to entity association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToEntityAssociationMixin

    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class GeneToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "gene to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToPhenotypicFeatureAssociation

    id: Union[str, GeneToPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToPhenotypicFeatureAssociationId):
            self.id = GeneToPhenotypicFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class GeneToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToDiseaseAssociation"
    class_name: ClassVar[str] = "gene to disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToDiseaseAssociation

    id: Union[str, GeneToDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToDiseaseAssociationId):
            self.id = GeneToDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantToGeneAssociation(Association):
    """
    An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in
    linkage disequilibrium)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToGeneAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToGeneAssociation"
    class_name: ClassVar[str] = "variant to gene association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToGeneAssociation

    id: Union[str, VariantToGeneAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, GeneId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToGeneAssociationId):
            self.id = VariantToGeneAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToGeneExpressionAssociation(VariantToGeneAssociation):
    """
    An association between a variant and expression of a gene (i.e. e-QTL)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToGeneExpressionAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToGeneExpressionAssociation"
    class_name: ClassVar[str] = "variant to gene expression association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToGeneExpressionAssociation

    id: Union[str, VariantToGeneExpressionAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, GeneId] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    expression_site: Optional[Union[str, AnatomicalEntityId]] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    phenotypic_state: Optional[Union[str, DiseaseOrPhenotypicFeatureId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToGeneExpressionAssociationId):
            self.id = VariantToGeneExpressionAssociationId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.expression_site is not None and not isinstance(self.expression_site, AnatomicalEntityId):
            self.expression_site = AnatomicalEntityId(self.expression_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.phenotypic_state is not None and not isinstance(self.phenotypic_state, DiseaseOrPhenotypicFeatureId):
            self.phenotypic_state = DiseaseOrPhenotypicFeatureId(self.phenotypic_state)

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
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)

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
    subject: Union[str, PopulationOfIndividualOrganismsId] = None
    object: Union[str, PopulationOfIndividualOrganismsId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, PopulationOfIndividualOrganismsId):
            self.subject = PopulationOfIndividualOrganismsId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, PopulationOfIndividualOrganismsId):
            self.object = PopulationOfIndividualOrganismsId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToPhenotypicFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToPhenotypicFeatureAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToPhenotypicFeatureAssociation"
    class_name: ClassVar[str] = "variant to phenotypic feature association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToPhenotypicFeatureAssociation

    id: Union[str, VariantToPhenotypicFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    sex_qualifier: Optional[Union[dict, BiologicalSex]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToPhenotypicFeatureAssociationId):
            self.id = VariantToPhenotypicFeatureAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.sex_qualifier is not None and not isinstance(self.sex_qualifier, BiologicalSex):
            self.sex_qualifier = BiologicalSex(**self.sex_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class VariantToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantToDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantToDiseaseAssociation"
    class_name: ClassVar[str] = "variant to disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantToDiseaseAssociation

    id: Union[str, VariantToDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantToDiseaseAssociationId):
            self.id = VariantToDiseaseAssociationId(self.id)

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
class GenotypeToDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeToDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:GenotypeToDiseaseAssociation"
    class_name: ClassVar[str] = "genotype to disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeToDiseaseAssociation

    id: Union[str, GenotypeToDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeToDiseaseAssociationId):
            self.id = GenotypeToDiseaseAssociationId(self.id)

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
class ModelToDiseaseAssociationMixin(YAMLRoot):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in
    that it recapitulates some features of the disease in a way that is useful for studying the disease outside a
    patient carrying the disease
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ModelToDiseaseAssociationMixin
    class_class_curie: ClassVar[str] = "csolink:ModelToDiseaseAssociationMixin"
    class_name: ClassVar[str] = "model to disease association mixin"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ModelToDiseaseAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
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
class GeneAsAModelOfDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "gene as a model of disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneAsAModelOfDiseaseAssociation

    id: Union[str, GeneAsAModelOfDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneAsAModelOfDiseaseAssociationId):
            self.id = GeneAsAModelOfDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class VariantAsAModelOfDiseaseAssociation(VariantToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.VariantAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:VariantAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "variant as a model of disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.VariantAsAModelOfDiseaseAssociation

    id: Union[str, VariantAsAModelOfDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, VariantAsAModelOfDiseaseAssociationId):
            self.id = VariantAsAModelOfDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class GenotypeAsAModelOfDiseaseAssociation(GenotypeToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenotypeAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:GenotypeAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "genotype as a model of disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenotypeAsAModelOfDiseaseAssociation

    id: Union[str, GenotypeAsAModelOfDiseaseAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, GenotypeId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenotypeAsAModelOfDiseaseAssociationId):
            self.id = GenotypeAsAModelOfDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenotypeId):
            self.subject = GenotypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class CellLineAsAModelOfDiseaseAssociation(CellLineToDiseaseOrPhenotypicFeatureAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.CellLineAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:CellLineAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "cell line as a model of disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.CellLineAsAModelOfDiseaseAssociation

    id: Union[str, CellLineAsAModelOfDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, CellLineId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CellLineAsAModelOfDiseaseAssociationId):
            self.id = CellLineAsAModelOfDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, CellLineId):
            self.subject = CellLineId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrganismalEntityAsAModelOfDiseaseAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.OrganismalEntityAsAModelOfDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:OrganismalEntityAsAModelOfDiseaseAssociation"
    class_name: ClassVar[str] = "organismal entity as a model of disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.OrganismalEntityAsAModelOfDiseaseAssociation

    id: Union[str, OrganismalEntityAsAModelOfDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OrganismalEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, OrganismalEntityAsAModelOfDiseaseAssociationId):
            self.id = OrganismalEntityAsAModelOfDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, OrganismalEntityId):
            self.subject = OrganismalEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneHasVariantThatContributesToDiseaseAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneHasVariantThatContributesToDiseaseAssociation"
    class_name: ClassVar[str] = "gene has variant that contributes to disease association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneHasVariantThatContributesToDiseaseAssociation

    id: Union[str, GeneHasVariantThatContributesToDiseaseAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneHasVariantThatContributesToDiseaseAssociationId):
            self.id = GeneHasVariantThatContributesToDiseaseAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToExpressionSiteAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToExpressionSiteAssociation"
    class_name: ClassVar[str] = "gene to expression site association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToExpressionSiteAssociation

    id: Union[str, GeneToExpressionSiteAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, AnatomicalEntityId] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[str, LifeStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToExpressionSiteAssociationId):
            self.id = GeneToExpressionSiteAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifeStageId):
            self.stage_qualifier = LifeStageId(self.stage_qualifier)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.SequenceVariantModulatesTreatmentAssociation
    class_class_curie: ClassVar[str] = "csolink:SequenceVariantModulatesTreatmentAssociation"
    class_name: ClassVar[str] = "sequence variant modulates treatment association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.SequenceVariantModulatesTreatmentAssociation

    id: Union[str, SequenceVariantModulatesTreatmentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, TreatmentId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, TreatmentId):
            self.object = TreatmentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine (gene, gene product or complex of gene products) and either a
    molecular activity, a biological process or a cellular location in which a function is executed.
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
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, GeneOntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MacromolecularMachineId):
            self.subject = MacromolecularMachineId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachineToMolecularActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachineToMolecularActivityAssociation
    class_class_curie: ClassVar[str] = "csolink:MacromolecularMachineToMolecularActivityAssociation"
    class_name: ClassVar[str] = "macromolecular machine to molecular activity association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachineToMolecularActivityAssociation

    id: Union[str, MacromolecularMachineToMolecularActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, MolecularActivityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToMolecularActivityAssociationId):
            self.id = MacromolecularMachineToMolecularActivityAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachineToBiologicalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachineToBiologicalProcessAssociation
    class_class_curie: ClassVar[str] = "csolink:MacromolecularMachineToBiologicalProcessAssociation"
    class_name: ClassVar[str] = "macromolecular machine to biological process association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachineToBiologicalProcessAssociation

    id: Union[str, MacromolecularMachineToBiologicalProcessAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToBiologicalProcessAssociationId):
            self.id = MacromolecularMachineToBiologicalProcessAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacromolecularMachineToCellularComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachineToCellularComponentAssociation
    class_class_curie: ClassVar[str] = "csolink:MacromolecularMachineToCellularComponentAssociation"
    class_name: ClassVar[str] = "macromolecular machine to cellular component association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.MacromolecularMachineToCellularComponentAssociation

    id: Union[str, MacromolecularMachineToCellularComponentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, MacromolecularMachineId] = None
    object: Union[str, CellularComponentId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MacromolecularMachineToCellularComponentAssociationId):
            self.id = MacromolecularMachineToCellularComponentAssociationId(self.id)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToGoTermAssociation
    class_class_curie: ClassVar[str] = "csolink:GeneToGoTermAssociation"
    class_name: ClassVar[str] = "gene to go term association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToGoTermAssociation

    id: Union[str, GeneToGoTermAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, MolecularEntityId] = None
    object: Union[str, GeneOntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToGoTermAssociationId):
            self.id = GeneToGoTermAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, MolecularEntityId):
            self.subject = MolecularEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneOntologyClassId):
            self.object = GeneOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a genomic entity it is localized to.
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceAssociationId):
            self.id = SequenceAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GenomicSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a genomic entity it is localized to. The reference entity may be a
    chromosome, chromosome region or information entity such as a contig.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GenomicSequenceLocalization
    class_class_curie: ClassVar[str] = "csolink:GenomicSequenceLocalization"
    class_name: ClassVar[str] = "genomic sequence localization"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GenomicSequenceLocalization

    id: Union[str, GenomicSequenceLocalizationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GenomicEntityId] = None
    object: Union[str, GenomicEntityId] = None
    predicate: Union[str, PredicateType] = None
    start_interbase_coordinate: Optional[int] = None
    end_interbase_coordinate: Optional[int] = None
    genome_build: Optional[str] = None
    strand: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GenomicSequenceLocalizationId):
            self.id = GenomicSequenceLocalizationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.start_interbase_coordinate is not None and not isinstance(self.start_interbase_coordinate, int):
            self.start_interbase_coordinate = int(self.start_interbase_coordinate)

        if self.end_interbase_coordinate is not None and not isinstance(self.end_interbase_coordinate, int):
            self.end_interbase_coordinate = int(self.end_interbase_coordinate)

        if self.genome_build is not None and not isinstance(self.genome_build, str):
            self.genome_build = str(self.genome_build)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.phase is not None and not isinstance(self.phase, str):
            self.phase = str(self.phase)

        super().__post_init__(**kwargs)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
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
    subject: Union[str, GenomicEntityId] = None
    object: Union[str, GenomicEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GenomicEntityId):
            self.subject = GenomicEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GenomicEntityId):
            self.object = GenomicEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.TranscriptToGeneRelationship
    class_class_curie: ClassVar[str] = "csolink:TranscriptToGeneRelationship"
    class_name: ClassVar[str] = "transcript to gene relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.TranscriptToGeneRelationship

    id: Union[str, TranscriptToGeneRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, TranscriptId] = None
    object: Union[str, GeneId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, TranscriptToGeneRelationshipId):
            self.id = TranscriptToGeneRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, TranscriptId):
            self.subject = TranscriptId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneProductRelationship
    class_class_curie: ClassVar[str] = "csolink:GeneToGeneProductRelationship"
    class_name: ClassVar[str] = "gene to gene product relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneToGeneProductRelationship

    id: Union[str, GeneToGeneProductRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, GeneId] = None
    object: Union[str, GeneProductId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneToGeneProductRelationshipId):
            self.id = GeneToGeneProductRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneProductId):
            self.object = GeneProductId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.ExonToTranscriptRelationship
    class_class_curie: ClassVar[str] = "csolink:ExonToTranscriptRelationship"
    class_name: ClassVar[str] = "exon to transcript relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.ExonToTranscriptRelationship

    id: Union[str, ExonToTranscriptRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ExonId] = None
    object: Union[str, TranscriptId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExonToTranscriptRelationshipId):
            self.id = ExonToTranscriptRelationshipId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, ExonId):
            self.subject = ExonId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.GeneRegulatoryRelationship
    class_class_curie: ClassVar[str] = "csolink:GeneRegulatoryRelationship"
    class_name: ClassVar[str] = "gene regulatory relationship"
    class_model_uri: ClassVar[URIRef] = CSOLINK.GeneRegulatoryRelationship

    id: Union[str, GeneRegulatoryRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, GeneOrGeneProductId] = None
    object: Union[str, GeneOrGeneProductId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, GeneRegulatoryRelationshipId):
            self.id = GeneRegulatoryRelationshipId(self.id)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, GeneOrGeneProductId):
            self.subject = GeneOrGeneProductId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneOrGeneProductId):
            self.object = GeneOrGeneProductId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntityToAnatomicalEntityAssociation
    class_class_curie: ClassVar[str] = "csolink:AnatomicalEntityToAnatomicalEntityAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntityToAnatomicalEntityAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation
    class_class_curie: ClassVar[str] = "csolink:AnatomicalEntityToAnatomicalEntityPartOfAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity part of association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntityToAnatomicalEntityPartOfAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityPartOfAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityPartOfAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityPartOfAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(AnatomicalEntityToAnatomicalEntityAssociation):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation
    class_class_curie: ClassVar[str] = "csolink:AnatomicalEntityToAnatomicalEntityOntogenicAssociation"
    class_name: ClassVar[str] = "anatomical entity to anatomical entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = CSOLINK.AnatomicalEntityToAnatomicalEntityOntogenicAssociation

    id: Union[str, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, AnatomicalEntityId] = None
    object: Union[str, AnatomicalEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AnatomicalEntityToAnatomicalEntityOntogenicAssociationId):
            self.id = AnatomicalEntityToAnatomicalEntityOntogenicAssociationId(self.id)

        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, AnatomicalEntityId):
            self.subject = AnatomicalEntityId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.has_attribute = Slot(uri=CSOLINK.has_attribute, name="has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.has_attribute_type = Slot(uri=CSOLINK.has_attribute_type, name="has attribute type", curie=CSOLINK.curie('has_attribute_type'),
                   model_uri=CSOLINK.has_attribute_type, domain=Attribute, range=Union[str, OntologyClassId])

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

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=CSOLINK.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=GOP.systematic_synonym, name="systematic synonym", curie=GOP.curie('systematic_synonym'),
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

slots.source_data_file = Slot(uri=CSOLINK.source_data_file, name="source data file", curie=CSOLINK.curie('source_data_file'),
                   model_uri=CSOLINK.source_data_file, domain=DataSetVersion, range=Optional[Union[str, DataFileId]])

slots.source_web_page = Slot(uri=CSOLINK.source_web_page, name="source web page", curie=CSOLINK.curie('source_web_page'),
                   model_uri=CSOLINK.source_web_page, domain=None, range=Optional[str])

slots.retrieved_on = Slot(uri=CSOLINK.retrieved_on, name="retrieved on", curie=CSOLINK.curie('retrieved_on'),
                   model_uri=CSOLINK.retrieved_on, domain=SourceFile, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=CSOLINK.version_of, name="version of", curie=CSOLINK.curie('version_of'),
                   model_uri=CSOLINK.version_of, domain=DataSetVersion, range=Optional[Union[str, DataSetId]])

slots.source_version = Slot(uri=CSOLINK.source_version, name="source version", curie=CSOLINK.curie('source_version'),
                   model_uri=CSOLINK.source_version, domain=SourceFile, range=Optional[str])

slots.license = Slot(uri=CSOLINK.license, name="license", curie=CSOLINK.curie('license'),
                   model_uri=CSOLINK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=CSOLINK.rights, name="rights", curie=CSOLINK.curie('rights'),
                   model_uri=CSOLINK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=CSOLINK.format, name="format", curie=CSOLINK.curie('format'),
                   model_uri=CSOLINK.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=CSOLINK.created_with, name="created_with", curie=CSOLINK.curie('created_with'),
                   model_uri=CSOLINK.created_with, domain=SourceFile, range=Optional[str])

slots.download_url = Slot(uri=CSOLINK.download_url, name="download url", curie=CSOLINK.curie('download_url'),
                   model_uri=CSOLINK.download_url, domain=None, range=Optional[str])

slots.distribution = Slot(uri=CSOLINK.distribution, name="distribution", curie=CSOLINK.curie('distribution'),
                   model_uri=CSOLINK.distribution, domain=DataSetVersion, range=Optional[Union[str, DistributionLevelId]])

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

slots.mesh_terms = Slot(uri=CSOLINK.mesh_terms, name="mesh terms", curie=CSOLINK.curie('mesh_terms'),
                   model_uri=CSOLINK.mesh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_biological_sequence = Slot(uri=CSOLINK.has_biological_sequence, name="has biological sequence", curie=CSOLINK.curie('has_biological_sequence'),
                   model_uri=CSOLINK.has_biological_sequence, domain=NamedThing, range=Optional[Union[str, BiologicalSequence]])

slots.has_gene_or_gene_product = Slot(uri=CSOLINK.has_gene_or_gene_product, name="has gene or gene product", curie=CSOLINK.curie('has_gene_or_gene_product'),
                   model_uri=CSOLINK.has_gene_or_gene_product, domain=NamedThing, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.has_gene = Slot(uri=CSOLINK.has_gene, name="has gene", curie=CSOLINK.curie('has_gene'),
                   model_uri=CSOLINK.has_gene, domain=NamedThing, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.has_zygosity = Slot(uri=CSOLINK.has_zygosity, name="has zygosity", curie=CSOLINK.curie('has_zygosity'),
                   model_uri=CSOLINK.has_zygosity, domain=GenomicEntity, range=Optional[Union[dict, "Zygosity"]])

slots.has_chemical_formula = Slot(uri=CSOLINK.has_chemical_formula, name="has chemical formula", curie=CSOLINK.curie('has_chemical_formula'),
                   model_uri=CSOLINK.has_chemical_formula, domain=NamedThing, range=Optional[str])

slots.has_constituent = Slot(uri=CSOLINK.has_constituent, name="has constituent", curie=CSOLINK.curie('has_constituent'),
                   model_uri=CSOLINK.has_constituent, domain=NamedThing, range=Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]])

slots.has_drug = Slot(uri=CSOLINK.has_drug, name="has drug", curie=CSOLINK.curie('has_drug'),
                   model_uri=CSOLINK.has_drug, domain=NamedThing, range=Optional[Union[Union[str, DrugId], List[Union[str, DrugId]]]])

slots.has_device = Slot(uri=CSOLINK.has_device, name="has device", curie=CSOLINK.curie('has_device'),
                   model_uri=CSOLINK.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]])

slots.has_procedure = Slot(uri=CSOLINK.has_procedure, name="has procedure", curie=CSOLINK.curie('has_procedure'),
                   model_uri=CSOLINK.has_procedure, domain=NamedThing, range=Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]])

slots.has_active_ingredient = Slot(uri=CSOLINK.has_active_ingredient, name="has active ingredient", curie=CSOLINK.curie('has_active_ingredient'),
                   model_uri=CSOLINK.has_active_ingredient, domain=Drug, range=Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]])

slots.has_excipient = Slot(uri=CSOLINK.has_excipient, name="has excipient", curie=CSOLINK.curie('has_excipient'),
                   model_uri=CSOLINK.has_excipient, domain=Drug, range=Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]])

slots.has_nutrient = Slot(uri=CSOLINK.has_nutrient, name="has nutrient", curie=CSOLINK.curie('has_nutrient'),
                   model_uri=CSOLINK.has_nutrient, domain=Food, range=Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]])

slots.has_receptor = Slot(uri=CSOLINK.has_receptor, name="has receptor", curie=CSOLINK.curie('has_receptor'),
                   model_uri=CSOLINK.has_receptor, domain=None, range=Optional[Union[str, OrganismalEntityId]])

slots.has_stressor = Slot(uri=CSOLINK.has_stressor, name="has stressor", curie=CSOLINK.curie('has_stressor'),
                   model_uri=CSOLINK.has_stressor, domain=None, range=Optional[str])

slots.has_route = Slot(uri=CSOLINK.has_route, name="has route", curie=CSOLINK.curie('has_route'),
                   model_uri=CSOLINK.has_route, domain=None, range=Optional[str])

slots.has_population_context = Slot(uri=CSOLINK.has_population_context, name="has population context", curie=CSOLINK.curie('has_population_context'),
                   model_uri=CSOLINK.has_population_context, domain=Association, range=Optional[Union[str, PopulationOfIndividualOrganismsId]])

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

slots.physically_interacts_with = Slot(uri=CSOLINK.physically_interacts_with, name="physically interacts with", curie=CSOLINK.curie('physically_interacts_with'),
                   model_uri=CSOLINK.physically_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.molecularly_interacts_with = Slot(uri=CSOLINK.molecularly_interacts_with, name="molecularly interacts with", curie=CSOLINK.curie('molecularly_interacts_with'),
                   model_uri=CSOLINK.molecularly_interacts_with, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.genetically_interacts_with = Slot(uri=CSOLINK.genetically_interacts_with, name="genetically interacts with", curie=CSOLINK.curie('genetically_interacts_with'),
                   model_uri=CSOLINK.genetically_interacts_with, domain=Gene, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.affects = Slot(uri=CSOLINK.affects, name="affects", curie=CSOLINK.curie('affects'),
                   model_uri=CSOLINK.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=CSOLINK.affected_by, name="affected by", curie=CSOLINK.curie('affected_by'),
                   model_uri=CSOLINK.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affects_abundance_of = Slot(uri=CSOLINK.affects_abundance_of, name="affects abundance of", curie=CSOLINK.curie('affects_abundance_of'),
                   model_uri=CSOLINK.affects_abundance_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_abundance_of = Slot(uri=CSOLINK.increases_abundance_of, name="increases abundance of", curie=CSOLINK.curie('increases_abundance_of'),
                   model_uri=CSOLINK.increases_abundance_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_abundance_of = Slot(uri=CSOLINK.decreases_abundance_of, name="decreases abundance of", curie=CSOLINK.curie('decreases_abundance_of'),
                   model_uri=CSOLINK.decreases_abundance_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_activity_of = Slot(uri=CSOLINK.affects_activity_of, name="affects activity of", curie=CSOLINK.curie('affects_activity_of'),
                   model_uri=CSOLINK.affects_activity_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_activity_of = Slot(uri=CSOLINK.increases_activity_of, name="increases activity of", curie=CSOLINK.curie('increases_activity_of'),
                   model_uri=CSOLINK.increases_activity_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_activity_of = Slot(uri=CSOLINK.decreases_activity_of, name="decreases activity of", curie=CSOLINK.curie('decreases_activity_of'),
                   model_uri=CSOLINK.decreases_activity_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_expression_of = Slot(uri=CSOLINK.affects_expression_of, name="affects expression of", curie=CSOLINK.curie('affects_expression_of'),
                   model_uri=CSOLINK.affects_expression_of, domain=MolecularEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.increases_expression_of = Slot(uri=CSOLINK.increases_expression_of, name="increases expression of", curie=CSOLINK.curie('increases_expression_of'),
                   model_uri=CSOLINK.increases_expression_of, domain=MolecularEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.decreases_expression_of = Slot(uri=CSOLINK.decreases_expression_of, name="decreases expression of", curie=CSOLINK.curie('decreases_expression_of'),
                   model_uri=CSOLINK.decreases_expression_of, domain=MolecularEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.affects_folding_of = Slot(uri=CSOLINK.affects_folding_of, name="affects folding of", curie=CSOLINK.curie('affects_folding_of'),
                   model_uri=CSOLINK.affects_folding_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_folding_of = Slot(uri=CSOLINK.increases_folding_of, name="increases folding of", curie=CSOLINK.curie('increases_folding_of'),
                   model_uri=CSOLINK.increases_folding_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_folding_of = Slot(uri=CSOLINK.decreases_folding_of, name="decreases folding of", curie=CSOLINK.curie('decreases_folding_of'),
                   model_uri=CSOLINK.decreases_folding_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_localization_of = Slot(uri=CSOLINK.affects_localization_of, name="affects localization of", curie=CSOLINK.curie('affects_localization_of'),
                   model_uri=CSOLINK.affects_localization_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_localization_of = Slot(uri=CSOLINK.increases_localization_of, name="increases localization of", curie=CSOLINK.curie('increases_localization_of'),
                   model_uri=CSOLINK.increases_localization_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_localization_of = Slot(uri=CSOLINK.decreases_localization_of, name="decreases localization of", curie=CSOLINK.curie('decreases_localization_of'),
                   model_uri=CSOLINK.decreases_localization_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_metabolic_processing_of = Slot(uri=CSOLINK.affects_metabolic_processing_of, name="affects metabolic processing of", curie=CSOLINK.curie('affects_metabolic_processing_of'),
                   model_uri=CSOLINK.affects_metabolic_processing_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_metabolic_processing_of = Slot(uri=CSOLINK.increases_metabolic_processing_of, name="increases metabolic processing of", curie=CSOLINK.curie('increases_metabolic_processing_of'),
                   model_uri=CSOLINK.increases_metabolic_processing_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_metabolic_processing_of = Slot(uri=CSOLINK.decreases_metabolic_processing_of, name="decreases metabolic processing of", curie=CSOLINK.curie('decreases_metabolic_processing_of'),
                   model_uri=CSOLINK.decreases_metabolic_processing_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_molecular_modification_of = Slot(uri=CSOLINK.affects_molecular_modification_of, name="affects molecular modification of", curie=CSOLINK.curie('affects_molecular_modification_of'),
                   model_uri=CSOLINK.affects_molecular_modification_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_molecular_modification_of = Slot(uri=CSOLINK.increases_molecular_modification_of, name="increases molecular modification of", curie=CSOLINK.curie('increases_molecular_modification_of'),
                   model_uri=CSOLINK.increases_molecular_modification_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_molecular_modification_of = Slot(uri=CSOLINK.decreases_molecular_modification_of, name="decreases molecular modification of", curie=CSOLINK.curie('decreases_molecular_modification_of'),
                   model_uri=CSOLINK.decreases_molecular_modification_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_synthesis_of = Slot(uri=CSOLINK.affects_synthesis_of, name="affects synthesis of", curie=CSOLINK.curie('affects_synthesis_of'),
                   model_uri=CSOLINK.affects_synthesis_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_synthesis_of = Slot(uri=CSOLINK.increases_synthesis_of, name="increases synthesis of", curie=CSOLINK.curie('increases_synthesis_of'),
                   model_uri=CSOLINK.increases_synthesis_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_synthesis_of = Slot(uri=CSOLINK.decreases_synthesis_of, name="decreases synthesis of", curie=CSOLINK.curie('decreases_synthesis_of'),
                   model_uri=CSOLINK.decreases_synthesis_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_degradation_of = Slot(uri=CSOLINK.affects_degradation_of, name="affects degradation of", curie=CSOLINK.curie('affects_degradation_of'),
                   model_uri=CSOLINK.affects_degradation_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_degradation_of = Slot(uri=CSOLINK.increases_degradation_of, name="increases degradation of", curie=CSOLINK.curie('increases_degradation_of'),
                   model_uri=CSOLINK.increases_degradation_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_degradation_of = Slot(uri=CSOLINK.decreases_degradation_of, name="decreases degradation of", curie=CSOLINK.curie('decreases_degradation_of'),
                   model_uri=CSOLINK.decreases_degradation_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_mutation_rate_of = Slot(uri=CSOLINK.affects_mutation_rate_of, name="affects mutation rate of", curie=CSOLINK.curie('affects_mutation_rate_of'),
                   model_uri=CSOLINK.affects_mutation_rate_of, domain=MolecularEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.increases_mutation_rate_of = Slot(uri=CSOLINK.increases_mutation_rate_of, name="increases mutation rate of", curie=CSOLINK.curie('increases_mutation_rate_of'),
                   model_uri=CSOLINK.increases_mutation_rate_of, domain=MolecularEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.decreases_mutation_rate_of = Slot(uri=CSOLINK.decreases_mutation_rate_of, name="decreases mutation rate of", curie=CSOLINK.curie('decreases_mutation_rate_of'),
                   model_uri=CSOLINK.decreases_mutation_rate_of, domain=MolecularEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.affects_response_to = Slot(uri=CSOLINK.affects_response_to, name="affects response to", curie=CSOLINK.curie('affects_response_to'),
                   model_uri=CSOLINK.affects_response_to, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_response_to = Slot(uri=CSOLINK.increases_response_to, name="increases response to", curie=CSOLINK.curie('increases_response_to'),
                   model_uri=CSOLINK.increases_response_to, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_response_to = Slot(uri=CSOLINK.decreases_response_to, name="decreases response to", curie=CSOLINK.curie('decreases_response_to'),
                   model_uri=CSOLINK.decreases_response_to, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_splicing_of = Slot(uri=CSOLINK.affects_splicing_of, name="affects splicing of", curie=CSOLINK.curie('affects_splicing_of'),
                   model_uri=CSOLINK.affects_splicing_of, domain=MolecularEntity, range=Optional[Union[Union[str, TranscriptId], List[Union[str, TranscriptId]]]])

slots.increases_splicing_of = Slot(uri=CSOLINK.increases_splicing_of, name="increases splicing of", curie=CSOLINK.curie('increases_splicing_of'),
                   model_uri=CSOLINK.increases_splicing_of, domain=MolecularEntity, range=Optional[Union[Union[str, TranscriptId], List[Union[str, TranscriptId]]]])

slots.decreases_splicing_of = Slot(uri=CSOLINK.decreases_splicing_of, name="decreases splicing of", curie=CSOLINK.curie('decreases_splicing_of'),
                   model_uri=CSOLINK.decreases_splicing_of, domain=MolecularEntity, range=Optional[Union[Union[str, TranscriptId], List[Union[str, TranscriptId]]]])

slots.affects_stability_of = Slot(uri=CSOLINK.affects_stability_of, name="affects stability of", curie=CSOLINK.curie('affects_stability_of'),
                   model_uri=CSOLINK.affects_stability_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_stability_of = Slot(uri=CSOLINK.increases_stability_of, name="increases stability of", curie=CSOLINK.curie('increases_stability_of'),
                   model_uri=CSOLINK.increases_stability_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_stability_of = Slot(uri=CSOLINK.decreases_stability_of, name="decreases stability of", curie=CSOLINK.curie('decreases_stability_of'),
                   model_uri=CSOLINK.decreases_stability_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_transport_of = Slot(uri=CSOLINK.affects_transport_of, name="affects transport of", curie=CSOLINK.curie('affects_transport_of'),
                   model_uri=CSOLINK.affects_transport_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_transport_of = Slot(uri=CSOLINK.increases_transport_of, name="increases transport of", curie=CSOLINK.curie('increases_transport_of'),
                   model_uri=CSOLINK.increases_transport_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_transport_of = Slot(uri=CSOLINK.decreases_transport_of, name="decreases transport of", curie=CSOLINK.curie('decreases_transport_of'),
                   model_uri=CSOLINK.decreases_transport_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_secretion_of = Slot(uri=CSOLINK.affects_secretion_of, name="affects secretion of", curie=CSOLINK.curie('affects_secretion_of'),
                   model_uri=CSOLINK.affects_secretion_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_secretion_of = Slot(uri=CSOLINK.increases_secretion_of, name="increases secretion of", curie=CSOLINK.curie('increases_secretion_of'),
                   model_uri=CSOLINK.increases_secretion_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_secretion_of = Slot(uri=CSOLINK.decreases_secretion_of, name="decreases secretion of", curie=CSOLINK.curie('decreases_secretion_of'),
                   model_uri=CSOLINK.decreases_secretion_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.affects_uptake_of = Slot(uri=CSOLINK.affects_uptake_of, name="affects uptake of", curie=CSOLINK.curie('affects_uptake_of'),
                   model_uri=CSOLINK.affects_uptake_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_uptake_of = Slot(uri=CSOLINK.increases_uptake_of, name="increases uptake of", curie=CSOLINK.curie('increases_uptake_of'),
                   model_uri=CSOLINK.increases_uptake_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.decreases_uptake_of = Slot(uri=CSOLINK.decreases_uptake_of, name="decreases uptake of", curie=CSOLINK.curie('decreases_uptake_of'),
                   model_uri=CSOLINK.decreases_uptake_of, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.regulates = Slot(uri=CSOLINK.regulates, name="regulates", curie=CSOLINK.curie('regulates'),
                   model_uri=CSOLINK.regulates, domain=None, range=Optional[Union[dict, "PhysicalEssenceOrOccurrent"]])

slots.regulated_by = Slot(uri=CSOLINK.regulated_by, name="regulated by", curie=CSOLINK.curie('regulated_by'),
                   model_uri=CSOLINK.regulated_by, domain=None, range=Optional[Union[dict, "PhysicalEssenceOrOccurrent"]])

slots.positively_regulates = Slot(uri=CSOLINK.positively_regulates, name="positively regulates", curie=CSOLINK.curie('positively_regulates'),
                   model_uri=CSOLINK.positively_regulates, domain=None, range=Optional[Union[dict, "PhysicalEssenceOrOccurrent"]])

slots.positively_regulated_by = Slot(uri=CSOLINK.positively_regulated_by, name="positively regulated by", curie=CSOLINK.curie('positively_regulated_by'),
                   model_uri=CSOLINK.positively_regulated_by, domain=None, range=Optional[Union[dict, "PhysicalEssenceOrOccurrent"]])

slots.negatively_regulates = Slot(uri=CSOLINK.negatively_regulates, name="negatively regulates", curie=CSOLINK.curie('negatively_regulates'),
                   model_uri=CSOLINK.negatively_regulates, domain=None, range=Optional[Union[dict, "PhysicalEssenceOrOccurrent"]])

slots.negatively_regulated_by = Slot(uri=CSOLINK.negatively_regulated_by, name="negatively regulated by", curie=CSOLINK.curie('negatively_regulated_by'),
                   model_uri=CSOLINK.negatively_regulated_by, domain=None, range=Optional[Union[dict, "PhysicalEssenceOrOccurrent"]])

slots.regulates_process_to_process = Slot(uri=CSOLINK.regulates_process_to_process, name="regulates, process to process", curie=CSOLINK.curie('regulates_process_to_process'),
                   model_uri=CSOLINK.regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulated_by_process_to_process = Slot(uri=CSOLINK.regulated_by_process_to_process, name="regulated by, process to process", curie=CSOLINK.curie('regulated_by_process_to_process'),
                   model_uri=CSOLINK.regulated_by_process_to_process, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.positively_regulates_process_to_process = Slot(uri=CSOLINK.positively_regulates_process_to_process, name="positively regulates, process to process", curie=CSOLINK.curie('positively_regulates_process_to_process'),
                   model_uri=CSOLINK.positively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulated_by_process_to_process = Slot(uri=CSOLINK.positively_regulated_by_process_to_process, name="positively regulated by, process to process", curie=CSOLINK.curie('positively_regulated_by_process_to_process'),
                   model_uri=CSOLINK.positively_regulated_by_process_to_process, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.negatively_regulates_process_to_process = Slot(uri=CSOLINK.negatively_regulates_process_to_process, name="negatively regulates, process to process", curie=CSOLINK.curie('negatively_regulates_process_to_process'),
                   model_uri=CSOLINK.negatively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulated_by_process_to_process = Slot(uri=CSOLINK.negatively_regulated_by_process_to_process, name="negatively regulated by, process to process", curie=CSOLINK.curie('negatively_regulated_by_process_to_process'),
                   model_uri=CSOLINK.negatively_regulated_by_process_to_process, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.regulates_entity_to_entity = Slot(uri=CSOLINK.regulates_entity_to_entity, name="regulates, entity to entity", curie=CSOLINK.curie('regulates_entity_to_entity'),
                   model_uri=CSOLINK.regulates_entity_to_entity, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.regulated_by_entity_to_entity = Slot(uri=CSOLINK.regulated_by_entity_to_entity, name="regulated by, entity to entity", curie=CSOLINK.curie('regulated_by_entity_to_entity'),
                   model_uri=CSOLINK.regulated_by_entity_to_entity, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.positively_regulates_entity_to_entity = Slot(uri=CSOLINK.positively_regulates_entity_to_entity, name="positively regulates, entity to entity", curie=CSOLINK.curie('positively_regulates_entity_to_entity'),
                   model_uri=CSOLINK.positively_regulates_entity_to_entity, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.positively_regulated_by_entity_to_entity = Slot(uri=CSOLINK.positively_regulated_by_entity_to_entity, name="positively regulated by, entity to entity", curie=CSOLINK.curie('positively_regulated_by_entity_to_entity'),
                   model_uri=CSOLINK.positively_regulated_by_entity_to_entity, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.negatively_regulates_entity_to_entity = Slot(uri=CSOLINK.negatively_regulates_entity_to_entity, name="negatively regulates, entity to entity", curie=CSOLINK.curie('negatively_regulates_entity_to_entity'),
                   model_uri=CSOLINK.negatively_regulates_entity_to_entity, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.negatively_regulated_by_entity_to_entity = Slot(uri=CSOLINK.negatively_regulated_by_entity_to_entity, name="negatively regulated by, entity to entity", curie=CSOLINK.curie('negatively_regulated_by_entity_to_entity'),
                   model_uri=CSOLINK.negatively_regulated_by_entity_to_entity, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.disrupts = Slot(uri=CSOLINK.disrupts, name="disrupts", curie=CSOLINK.curie('disrupts'),
                   model_uri=CSOLINK.disrupts, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.disrupted_by = Slot(uri=CSOLINK.disrupted_by, name="disrupted by", curie=CSOLINK.curie('disrupted_by'),
                   model_uri=CSOLINK.disrupted_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_gene_product = Slot(uri=CSOLINK.has_gene_product, name="has gene product", curie=CSOLINK.curie('has_gene_product'),
                   model_uri=CSOLINK.has_gene_product, domain=Gene, range=Optional[Union[Union[str, GeneProductId], List[Union[str, GeneProductId]]]])

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
                   model_uri=CSOLINK.in_pathway_with, domain=GeneOrGeneProduct, range=Optional[Union[Union[str, GeneOrGeneProductId], List[Union[str, GeneOrGeneProductId]]]])

slots.in_complex_with = Slot(uri=CSOLINK.in_complex_with, name="in complex with", curie=CSOLINK.curie('in_complex_with'),
                   model_uri=CSOLINK.in_complex_with, domain=GeneOrGeneProduct, range=Optional[Union[Union[str, GeneOrGeneProductId], List[Union[str, GeneOrGeneProductId]]]])

slots.in_cell_population_with = Slot(uri=CSOLINK.in_cell_population_with, name="in cell population with", curie=CSOLINK.curie('in_cell_population_with'),
                   model_uri=CSOLINK.in_cell_population_with, domain=GeneOrGeneProduct, range=Optional[Union[Union[str, GeneOrGeneProductId], List[Union[str, GeneOrGeneProductId]]]])

slots.colocalizes_with = Slot(uri=CSOLINK.colocalizes_with, name="colocalizes with", curie=CSOLINK.curie('colocalizes_with'),
                   model_uri=CSOLINK.colocalizes_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.genetic_association = Slot(uri=CSOLINK.genetic_association, name="genetic association", curie=CSOLINK.curie('genetic_association'),
                   model_uri=CSOLINK.genetic_association, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.gene_associated_with_condition = Slot(uri=CSOLINK.gene_associated_with_condition, name="gene associated with condition", curie=CSOLINK.curie('gene_associated_with_condition'),
                   model_uri=CSOLINK.gene_associated_with_condition, domain=Gene, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.condition_associated_with_gene = Slot(uri=CSOLINK.condition_associated_with_gene, name="condition associated with gene", curie=CSOLINK.curie('condition_associated_with_gene'),
                   model_uri=CSOLINK.condition_associated_with_gene, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

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
                   model_uri=CSOLINK.ameliorates, domain=BiologicalEntity, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.exacerbates = Slot(uri=CSOLINK.exacerbates, name="exacerbates", curie=CSOLINK.curie('exacerbates'),
                   model_uri=CSOLINK.exacerbates, domain=BiologicalEntity, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.treats = Slot(uri=CSOLINK.treats, name="treats", curie=CSOLINK.curie('treats'),
                   model_uri=CSOLINK.treats, domain=Treatment, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.treated_by = Slot(uri=CSOLINK.treated_by, name="treated by", curie=CSOLINK.curie('treated_by'),
                   model_uri=CSOLINK.treated_by, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[str, TreatmentId], List[Union[str, TreatmentId]]]])

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

slots.coexpressed_with = Slot(uri=CSOLINK.coexpressed_with, name="coexpressed with", curie=CSOLINK.curie('coexpressed_with'),
                   model_uri=CSOLINK.coexpressed_with, domain=GeneOrGeneProduct, range=Optional[Union[Union[str, GeneOrGeneProductId], List[Union[str, GeneOrGeneProductId]]]])

slots.has_biomarker = Slot(uri=CSOLINK.has_biomarker, name="has biomarker", curie=CSOLINK.curie('has_biomarker'),
                   model_uri=CSOLINK.has_biomarker, domain=DiseaseOrPhenotypicFeature, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.biomarker_for = Slot(uri=CSOLINK.biomarker_for, name="biomarker for", curie=CSOLINK.curie('biomarker_for'),
                   model_uri=CSOLINK.biomarker_for, domain=MolecularEntity, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.expressed_in = Slot(uri=CSOLINK.expressed_in, name="expressed in", curie=CSOLINK.curie('expressed_in'),
                   model_uri=CSOLINK.expressed_in, domain=GeneOrGeneProduct, range=Optional[Union[Union[str, AnatomicalEntityId], List[Union[str, AnatomicalEntityId]]]])

slots.expresses = Slot(uri=CSOLINK.expresses, name="expresses", curie=CSOLINK.curie('expresses'),
                   model_uri=CSOLINK.expresses, domain=AnatomicalEntity, range=Optional[Union[Union[str, GeneOrGeneProductId], List[Union[str, GeneOrGeneProductId]]]])

slots.has_phenotype = Slot(uri=CSOLINK.has_phenotype, name="has phenotype", curie=CSOLINK.curie('has_phenotype'),
                   model_uri=CSOLINK.has_phenotype, domain=BiologicalEntity, range=Optional[Union[Union[str, PhenotypicFeatureId], List[Union[str, PhenotypicFeatureId]]]])

slots.occurs_in = Slot(uri=CSOLINK.occurs_in, name="occurs in", curie=CSOLINK.curie('occurs_in'),
                   model_uri=CSOLINK.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=CSOLINK.located_in, name="located in", curie=CSOLINK.curie('located_in'),
                   model_uri=CSOLINK.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=CSOLINK.location_of, name="location of", curie=CSOLINK.curie('location_of'),
                   model_uri=CSOLINK.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=CSOLINK.similar_to, name="similar to", curie=CSOLINK.curie('similar_to'),
                   model_uri=CSOLINK.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.chemically_similar_to = Slot(uri=CSOLINK.chemically_similar_to, name="chemically similar to", curie=CSOLINK.curie('chemically_similar_to'),
                   model_uri=CSOLINK.chemically_similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_sequence_location = Slot(uri=CSOLINK.has_sequence_location, name="has sequence location", curie=CSOLINK.curie('has_sequence_location'),
                   model_uri=CSOLINK.has_sequence_location, domain=GenomicEntity, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

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
                   model_uri=CSOLINK.enables, domain=PhysicalEntity, range=Optional[Union[Union[str, BiologicalProcessOrActivityId], List[Union[str, BiologicalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=CSOLINK.enabled_by, name="enabled by", curie=CSOLINK.curie('enabled_by'),
                   model_uri=CSOLINK.enabled_by, domain=BiologicalProcessOrActivity, range=Optional[Union[Union[str, PhysicalEntityId], List[Union[str, PhysicalEntityId]]]])

slots.derives_into = Slot(uri=CSOLINK.derives_into, name="derives into", curie=CSOLINK.curie('derives_into'),
                   model_uri=CSOLINK.derives_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.derives_from = Slot(uri=CSOLINK.derives_from, name="derives from", curie=CSOLINK.curie('derives_from'),
                   model_uri=CSOLINK.derives_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.manifestation_of = Slot(uri=CSOLINK.manifestation_of, name="manifestation of", curie=CSOLINK.curie('manifestation_of'),
                   model_uri=CSOLINK.manifestation_of, domain=NamedThing, range=Optional[Union[Union[str, DiseaseId], List[Union[str, DiseaseId]]]])

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

slots.affects_expression_in = Slot(uri=CSOLINK.affects_expression_in, name="affects expression in", curie=CSOLINK.curie('affects_expression_in'),
                   model_uri=CSOLINK.affects_expression_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_variant_part = Slot(uri=CSOLINK.has_variant_part, name="has variant part", curie=CSOLINK.curie('has_variant_part'),
                   model_uri=CSOLINK.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=CSOLINK.related_condition, name="related condition", curie=CSOLINK.curie('related_condition'),
                   model_uri=CSOLINK.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_sequence_variant_of = Slot(uri=CSOLINK.is_sequence_variant_of, name="is sequence variant of", curie=CSOLINK.curie('is_sequence_variant_of'),
                   model_uri=CSOLINK.is_sequence_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GenomicEntityId], List[Union[str, GenomicEntityId]]]])

slots.is_missense_variant_of = Slot(uri=CSOLINK.is_missense_variant_of, name="is missense variant of", curie=CSOLINK.curie('is_missense_variant_of'),
                   model_uri=CSOLINK.is_missense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.is_synonymous_variant_of = Slot(uri=CSOLINK.is_synonymous_variant_of, name="is synonymous variant of", curie=CSOLINK.curie('is_synonymous_variant_of'),
                   model_uri=CSOLINK.is_synonymous_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.is_nonsense_variant_of = Slot(uri=CSOLINK.is_nonsense_variant_of, name="is nonsense variant of", curie=CSOLINK.curie('is_nonsense_variant_of'),
                   model_uri=CSOLINK.is_nonsense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.is_frameshift_variant_of = Slot(uri=CSOLINK.is_frameshift_variant_of, name="is frameshift variant of", curie=CSOLINK.curie('is_frameshift_variant_of'),
                   model_uri=CSOLINK.is_frameshift_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.is_splice_site_variant_of = Slot(uri=CSOLINK.is_splice_site_variant_of, name="is splice site variant of", curie=CSOLINK.curie('is_splice_site_variant_of'),
                   model_uri=CSOLINK.is_splice_site_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.is_nearby_variant_of = Slot(uri=CSOLINK.is_nearby_variant_of, name="is nearby variant of", curie=CSOLINK.curie('is_nearby_variant_of'),
                   model_uri=CSOLINK.is_nearby_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.is_non_coding_variant_of = Slot(uri=CSOLINK.is_non_coding_variant_of, name="is non coding variant of", curie=CSOLINK.curie('is_non_coding_variant_of'),
                   model_uri=CSOLINK.is_non_coding_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.disease_has_basis_in = Slot(uri=CSOLINK.disease_has_basis_in, name="disease has basis in", curie=CSOLINK.curie('disease_has_basis_in'),
                   model_uri=CSOLINK.disease_has_basis_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes_adverse_event = Slot(uri=CSOLINK.causes_adverse_event, name="causes adverse event", curie=CSOLINK.curie('causes_adverse_event'),
                   model_uri=CSOLINK.causes_adverse_event, domain=Drug, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.contraindicated_for = Slot(uri=CSOLINK.contraindicated_for, name="contraindicated for", curie=CSOLINK.curie('contraindicated_for'),
                   model_uri=CSOLINK.contraindicated_for, domain=Drug, range=Optional[Union[Union[str, DiseaseOrPhenotypicFeatureId], List[Union[str, DiseaseOrPhenotypicFeatureId]]]])

slots.has_not_completed = Slot(uri=CSOLINK.has_not_completed, name="has not completed", curie=CSOLINK.curie('has_not_completed'),
                   model_uri=CSOLINK.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=CSOLINK.has_completed, name="has completed", curie=CSOLINK.curie('has_completed'),
                   model_uri=CSOLINK.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreases_molecular_interaction = Slot(uri=CSOLINK.decreases_molecular_interaction, name="decreases molecular interaction", curie=CSOLINK.curie('decreases_molecular_interaction'),
                   model_uri=CSOLINK.decreases_molecular_interaction, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

slots.increases_molecular_interaction = Slot(uri=CSOLINK.increases_molecular_interaction, name="increases molecular interaction", curie=CSOLINK.curie('increases_molecular_interaction'),
                   model_uri=CSOLINK.increases_molecular_interaction, domain=MolecularEntity, range=Optional[Union[Union[str, MolecularEntityId], List[Union[str, MolecularEntityId]]]])

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
                   model_uri=CSOLINK.in_taxon, domain=None, range=Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]])

slots.has_molecular_consequence = Slot(uri=CSOLINK.has_molecular_consequence, name="has molecular consequence", curie=CSOLINK.curie('has_molecular_consequence'),
                   model_uri=CSOLINK.has_molecular_consequence, domain=NamedThing, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

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
                   model_uri=CSOLINK.negated, domain=Association, range=Optional[Bool])

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

slots.interacting_molecules_category = Slot(uri=CSOLINK.interacting_molecules_category, name="interacting molecules category", curie=CSOLINK.curie('interacting_molecules_category'),
                   model_uri=CSOLINK.interacting_molecules_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.quantifier_qualifier = Slot(uri=CSOLINK.quantifier_qualifier, name="quantifier qualifier", curie=CSOLINK.curie('quantifier_qualifier'),
                   model_uri=CSOLINK.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.catalyst_qualifier = Slot(uri=CSOLINK.catalyst_qualifier, name="catalyst qualifier", curie=CSOLINK.curie('catalyst_qualifier'),
                   model_uri=CSOLINK.catalyst_qualifier, domain=Association, range=Optional[Union[Union[str, MacromolecularMachineId], List[Union[str, MacromolecularMachineId]]]])

slots.expression_site = Slot(uri=CSOLINK.expression_site, name="expression site", curie=CSOLINK.curie('expression_site'),
                   model_uri=CSOLINK.expression_site, domain=Association, range=Optional[Union[str, AnatomicalEntityId]])

slots.stage_qualifier = Slot(uri=CSOLINK.stage_qualifier, name="stage qualifier", curie=CSOLINK.curie('stage_qualifier'),
                   model_uri=CSOLINK.stage_qualifier, domain=Association, range=Optional[Union[str, LifeStageId]])

slots.phenotypic_state = Slot(uri=CSOLINK.phenotypic_state, name="phenotypic state", curie=CSOLINK.curie('phenotypic_state'),
                   model_uri=CSOLINK.phenotypic_state, domain=Association, range=Optional[Union[str, DiseaseOrPhenotypicFeatureId]])

slots.qualifiers = Slot(uri=CSOLINK.qualifiers, name="qualifiers", curie=CSOLINK.curie('qualifiers'),
                   model_uri=CSOLINK.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=CSOLINK.frequency_qualifier, name="frequency qualifier", curie=CSOLINK.curie('frequency_qualifier'),
                   model_uri=CSOLINK.frequency_qualifier, domain=Association, range=Optional[Union[dict, FrequencyValue]])

slots.severity_qualifier = Slot(uri=CSOLINK.severity_qualifier, name="severity qualifier", curie=CSOLINK.curie('severity_qualifier'),
                   model_uri=CSOLINK.severity_qualifier, domain=Association, range=Optional[Union[dict, SeverityValue]])

slots.sex_qualifier = Slot(uri=CSOLINK.sex_qualifier, name="sex qualifier", curie=CSOLINK.curie('sex_qualifier'),
                   model_uri=CSOLINK.sex_qualifier, domain=Association, range=Optional[Union[dict, BiologicalSex]])

slots.onset_qualifier = Slot(uri=CSOLINK.onset_qualifier, name="onset qualifier", curie=CSOLINK.curie('onset_qualifier'),
                   model_uri=CSOLINK.onset_qualifier, domain=Association, range=Optional[Union[dict, Onset]])

slots.clinical_modifier_qualifier = Slot(uri=CSOLINK.clinical_modifier_qualifier, name="clinical modifier qualifier", curie=CSOLINK.curie('clinical_modifier_qualifier'),
                   model_uri=CSOLINK.clinical_modifier_qualifier, domain=Association, range=Optional[Union[dict, ClinicalModifier]])

slots.sequence_variant_qualifier = Slot(uri=CSOLINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=CSOLINK.curie('sequence_variant_qualifier'),
                   model_uri=CSOLINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[str, SequenceVariantId]])

slots.publications = Slot(uri=CSOLINK.publications, name="publications", curie=CSOLINK.curie('publications'),
                   model_uri=CSOLINK.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.sequence_localization_attribute = Slot(uri=CSOLINK.sequence_localization_attribute, name="sequence localization attribute", curie=CSOLINK.curie('sequence_localization_attribute'),
                   model_uri=CSOLINK.sequence_localization_attribute, domain=GenomicSequenceLocalization, range=Optional[str])

slots.interbase_coordinate = Slot(uri=CSOLINK.interbase_coordinate, name="interbase coordinate", curie=CSOLINK.curie('interbase_coordinate'),
                   model_uri=CSOLINK.interbase_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.start_interbase_coordinate = Slot(uri=CSOLINK.start_interbase_coordinate, name="start interbase coordinate", curie=CSOLINK.curie('start_interbase_coordinate'),
                   model_uri=CSOLINK.start_interbase_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.end_interbase_coordinate = Slot(uri=CSOLINK.end_interbase_coordinate, name="end interbase coordinate", curie=CSOLINK.curie('end_interbase_coordinate'),
                   model_uri=CSOLINK.end_interbase_coordinate, domain=GenomicSequenceLocalization, range=Optional[int])

slots.genome_build = Slot(uri=CSOLINK.genome_build, name="genome build", curie=CSOLINK.curie('genome_build'),
                   model_uri=CSOLINK.genome_build, domain=GenomicSequenceLocalization, range=Optional[str])

slots.strand = Slot(uri=CSOLINK.strand, name="strand", curie=CSOLINK.curie('strand'),
                   model_uri=CSOLINK.strand, domain=GenomicSequenceLocalization, range=Optional[str])

slots.phase = Slot(uri=CSOLINK.phase, name="phase", curie=CSOLINK.curie('phase'),
                   model_uri=CSOLINK.phase, domain=CodingSequence, range=Optional[str])

slots.has_taxonomic_rank = Slot(uri=CSOLINK.has_taxonomic_rank, name="has taxonomic rank", curie=CSOLINK.curie('has_taxonomic_rank'),
                   model_uri=CSOLINK.has_taxonomic_rank, domain=None, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.attribute_name = Slot(uri=CSOLINK.name, name="attribute_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=CSOLINK.category, name="named thing_category", curie=CSOLINK.curie('category'),
                   model_uri=CSOLINK.named_thing_category, domain=NamedThing, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.organism_taxon_has_taxonomic_rank = Slot(uri=CSOLINK.has_taxonomic_rank, name="organism taxon_has taxonomic rank", curie=CSOLINK.curie('has_taxonomic_rank'),
                   model_uri=CSOLINK.organism_taxon_has_taxonomic_rank, domain=OrganismTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.organism_taxon_subclass_of = Slot(uri=CSOLINK.subclass_of, name="organism taxon_subclass of", curie=CSOLINK.curie('subclass_of'),
                   model_uri=CSOLINK.organism_taxon_subclass_of, domain=OrganismTaxon, range=Optional[Union[Union[str, OrganismTaxonId], List[Union[str, OrganismTaxonId]]]])

slots.agent_id = Slot(uri=CSOLINK.id, name="agent_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=CSOLINK.name, name="agent_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.publication_id = Slot(uri=CSOLINK.id, name="publication_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_name = Slot(uri=CSOLINK.name, name="publication_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.publication_type = Slot(uri=DCTERMS.type, name="publication_type", curie=DCTERMS.curie('type'),
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

slots.molecular_activity_has_input = Slot(uri=CSOLINK.has_input, name="molecular activity_has input", curie=CSOLINK.curie('has_input'),
                   model_uri=CSOLINK.molecular_activity_has_input, domain=MolecularActivity, range=Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]])

slots.molecular_activity_has_output = Slot(uri=CSOLINK.has_output, name="molecular activity_has output", curie=CSOLINK.curie('has_output'),
                   model_uri=CSOLINK.molecular_activity_has_output, domain=MolecularActivity, range=Optional[Union[Union[str, ChemicalSubstanceId], List[Union[str, ChemicalSubstanceId]]]])

slots.molecular_activity_enabled_by = Slot(uri=CSOLINK.enabled_by, name="molecular activity_enabled by", curie=CSOLINK.curie('enabled_by'),
                   model_uri=CSOLINK.molecular_activity_enabled_by, domain=MolecularActivity, range=Optional[Union[Union[str, MacromolecularMachineId], List[Union[str, MacromolecularMachineId]]]])

slots.organismal_entity_has_attribute = Slot(uri=CSOLINK.has_attribute, name="organismal entity_has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.organismal_entity_has_attribute, domain=OrganismalEntity, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.macromolecular_machine_name = Slot(uri=CSOLINK.name, name="macromolecular machine_name", curie=CSOLINK.curie('name'),
                   model_uri=CSOLINK.macromolecular_machine_name, domain=MacromolecularMachine, range=Optional[Union[str, SymbolType]])

slots.sequence_variant_has_gene = Slot(uri=CSOLINK.has_gene, name="sequence variant_has gene", curie=CSOLINK.curie('has_gene'),
                   model_uri=CSOLINK.sequence_variant_has_gene, domain=SequenceVariant, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.sequence_variant_has_biological_sequence = Slot(uri=CSOLINK.has_biological_sequence, name="sequence variant_has biological sequence", curie=CSOLINK.curie('has_biological_sequence'),
                   model_uri=CSOLINK.sequence_variant_has_biological_sequence, domain=SequenceVariant, range=Optional[Union[str, BiologicalSequence]])

slots.sequence_variant_id = Slot(uri=CSOLINK.id, name="sequence variant_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.sequence_variant_id, domain=SequenceVariant, range=Union[str, SequenceVariantId])

slots.clinical_measurement_has_attribute_type = Slot(uri=CSOLINK.has_attribute_type, name="clinical measurement_has attribute type", curie=CSOLINK.curie('has_attribute_type'),
                   model_uri=CSOLINK.clinical_measurement_has_attribute_type, domain=ClinicalMeasurement, range=Union[str, OntologyClassId])

slots.clinical_finding_has_attribute = Slot(uri=CSOLINK.has_attribute, name="clinical finding_has attribute", curie=CSOLINK.curie('has_attribute'),
                   model_uri=CSOLINK.clinical_finding_has_attribute, domain=ClinicalFinding, range=Optional[Union[Union[dict, ClinicalAttribute], List[Union[dict, ClinicalAttribute]]]])

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

slots.genotype_to_genotype_part_association_predicate = Slot(uri=CSOLINK.predicate, name="genotype to genotype part association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.genotype_to_genotype_part_association_predicate, domain=GenotypeToGenotypePartAssociation, range=Union[str, PredicateType])

slots.genotype_to_genotype_part_association_subject = Slot(uri=CSOLINK.subject, name="genotype to genotype part association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_to_genotype_part_association_subject, domain=GenotypeToGenotypePartAssociation, range=Union[str, GenotypeId])

slots.genotype_to_genotype_part_association_object = Slot(uri=CSOLINK.object, name="genotype to genotype part association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.genotype_to_genotype_part_association_object, domain=GenotypeToGenotypePartAssociation, range=Union[str, GenotypeId])

slots.genotype_to_gene_association_predicate = Slot(uri=CSOLINK.predicate, name="genotype to gene association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.genotype_to_gene_association_predicate, domain=GenotypeToGeneAssociation, range=Union[str, PredicateType])

slots.genotype_to_gene_association_subject = Slot(uri=CSOLINK.subject, name="genotype to gene association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_to_gene_association_subject, domain=GenotypeToGeneAssociation, range=Union[str, GenotypeId])

slots.genotype_to_gene_association_object = Slot(uri=CSOLINK.object, name="genotype to gene association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.genotype_to_gene_association_object, domain=GenotypeToGeneAssociation, range=Union[str, GeneId])

slots.genotype_to_variant_association_predicate = Slot(uri=CSOLINK.predicate, name="genotype to variant association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.genotype_to_variant_association_predicate, domain=GenotypeToVariantAssociation, range=Union[str, PredicateType])

slots.genotype_to_variant_association_subject = Slot(uri=CSOLINK.subject, name="genotype to variant association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_to_variant_association_subject, domain=GenotypeToVariantAssociation, range=Union[str, GenotypeId])

slots.genotype_to_variant_association_object = Slot(uri=CSOLINK.object, name="genotype to variant association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.genotype_to_variant_association_object, domain=GenotypeToVariantAssociation, range=Union[str, SequenceVariantId])

slots.gene_to_gene_association_subject = Slot(uri=CSOLINK.subject, name="gene to gene association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_gene_association_subject, domain=GeneToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_gene_association_object = Slot(uri=CSOLINK.object, name="gene to gene association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.gene_to_gene_association_object, domain=GeneToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_gene_homology_association_predicate = Slot(uri=CSOLINK.predicate, name="gene to gene homology association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.gene_to_gene_homology_association_predicate, domain=GeneToGeneHomologyAssociation, range=Union[str, PredicateType])

slots.gene_expression_mixin_quantifier_qualifier = Slot(uri=CSOLINK.quantifier_qualifier, name="gene expression mixin_quantifier qualifier", curie=CSOLINK.curie('quantifier_qualifier'),
                   model_uri=CSOLINK.gene_expression_mixin_quantifier_qualifier, domain=GeneExpressionMixin, range=Optional[Union[str, OntologyClassId]])

slots.gene_to_gene_coexpression_association_predicate = Slot(uri=CSOLINK.predicate, name="gene to gene coexpression association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.gene_to_gene_coexpression_association_predicate, domain=GeneToGeneCoexpressionAssociation, range=Union[str, PredicateType])

slots.pairwise_gene_to_gene_interaction_predicate = Slot(uri=CSOLINK.predicate, name="pairwise gene to gene interaction_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.pairwise_gene_to_gene_interaction_predicate, domain=PairwiseGeneToGeneInteraction, range=Union[str, PredicateType])

slots.pairwise_gene_to_gene_interaction_relation = Slot(uri=CSOLINK.relation, name="pairwise gene to gene interaction_relation", curie=CSOLINK.curie('relation'),
                   model_uri=CSOLINK.pairwise_gene_to_gene_interaction_relation, domain=PairwiseGeneToGeneInteraction, range=Union[str, URIorCURIE])

slots.pairwise_molecular_interaction_subject = Slot(uri=CSOLINK.subject, name="pairwise molecular interaction_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.pairwise_molecular_interaction_subject, domain=PairwiseMolecularInteraction, range=Union[str, MolecularEntityId])

slots.pairwise_molecular_interaction_id = Slot(uri=CSOLINK.id, name="pairwise molecular interaction_id", curie=CSOLINK.curie('id'),
                   model_uri=CSOLINK.pairwise_molecular_interaction_id, domain=PairwiseMolecularInteraction, range=Union[str, PairwiseMolecularInteractionId])

slots.pairwise_molecular_interaction_predicate = Slot(uri=CSOLINK.predicate, name="pairwise molecular interaction_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.pairwise_molecular_interaction_predicate, domain=PairwiseMolecularInteraction, range=Union[str, PredicateType])

slots.pairwise_molecular_interaction_relation = Slot(uri=CSOLINK.relation, name="pairwise molecular interaction_relation", curie=CSOLINK.curie('relation'),
                   model_uri=CSOLINK.pairwise_molecular_interaction_relation, domain=PairwiseMolecularInteraction, range=Union[str, URIorCURIE])

slots.pairwise_molecular_interaction_object = Slot(uri=CSOLINK.object, name="pairwise molecular interaction_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.pairwise_molecular_interaction_object, domain=PairwiseMolecularInteraction, range=Union[str, MolecularEntityId])

slots.cell_line_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="cell line to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.cell_line_to_entity_association_mixin_subject, domain=None, range=Union[str, CellLineId])

slots.cell_line_to_disease_or_phenotypic_feature_association_subject = Slot(uri=CSOLINK.subject, name="cell line to disease or phenotypic feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.cell_line_to_disease_or_phenotypic_feature_association_subject, domain=CellLineToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.molecular_entity_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="molecular entity to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.molecular_entity_to_entity_association_mixin_subject, domain=None, range=Union[str, MolecularEntityId])

slots.drug_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="drug to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.drug_to_entity_association_mixin_subject, domain=None, range=Union[str, DrugId])

slots.chemical_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="chemical to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.chemical_to_entity_association_mixin_subject, domain=None, range=Union[str, ChemicalSubstanceId])

slots.case_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="case to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.case_to_entity_association_mixin_subject, domain=None, range=Union[str, CaseId])

slots.chemical_to_chemical_association_object = Slot(uri=CSOLINK.object, name="chemical to chemical association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.chemical_to_chemical_association_object, domain=ChemicalToChemicalAssociation, range=Union[str, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_subject = Slot(uri=CSOLINK.subject, name="chemical to chemical derivation association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.chemical_to_chemical_derivation_association_subject, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_object = Slot(uri=CSOLINK.object, name="chemical to chemical derivation association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.chemical_to_chemical_derivation_association_object, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, ChemicalSubstanceId])

slots.chemical_to_chemical_derivation_association_predicate = Slot(uri=CSOLINK.predicate, name="chemical to chemical derivation association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.chemical_to_chemical_derivation_association_predicate, domain=ChemicalToChemicalDerivationAssociation, range=Union[str, PredicateType])

slots.chemical_to_chemical_derivation_association_catalyst_qualifier = Slot(uri=CSOLINK.catalyst_qualifier, name="chemical to chemical derivation association_catalyst qualifier", curie=CSOLINK.curie('catalyst_qualifier'),
                   model_uri=CSOLINK.chemical_to_chemical_derivation_association_catalyst_qualifier, domain=ChemicalToChemicalDerivationAssociation, range=Optional[Union[Union[str, MacromolecularMachineId], List[Union[str, MacromolecularMachineId]]]])

slots.chemical_to_disease_or_phenotypic_feature_association_object = Slot(uri=CSOLINK.object, name="chemical to disease or phenotypic feature association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.chemical_to_disease_or_phenotypic_feature_association_object, domain=ChemicalToDiseaseOrPhenotypicFeatureAssociation, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.chemical_to_pathway_association_object = Slot(uri=CSOLINK.object, name="chemical to pathway association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.chemical_to_pathway_association_object, domain=ChemicalToPathwayAssociation, range=Union[str, PathwayId])

slots.chemical_to_gene_association_object = Slot(uri=CSOLINK.object, name="chemical to gene association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.chemical_to_gene_association_object, domain=ChemicalToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.drug_to_gene_association_object = Slot(uri=CSOLINK.object, name="drug to gene association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.drug_to_gene_association_object, domain=DrugToGeneAssociation, range=Union[str, GeneOrGeneProductId])

slots.material_sample_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="material sample to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.material_sample_to_entity_association_mixin_subject, domain=None, range=Union[str, MaterialSampleId])

slots.material_sample_derivation_association_subject = Slot(uri=CSOLINK.subject, name="material sample derivation association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.material_sample_derivation_association_subject, domain=MaterialSampleDerivationAssociation, range=Union[str, MaterialSampleId])

slots.material_sample_derivation_association_object = Slot(uri=CSOLINK.object, name="material sample derivation association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.material_sample_derivation_association_object, domain=MaterialSampleDerivationAssociation, range=Union[str, NamedThingId])

slots.material_sample_derivation_association_predicate = Slot(uri=CSOLINK.predicate, name="material sample derivation association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.material_sample_derivation_association_predicate, domain=MaterialSampleDerivationAssociation, range=Union[str, PredicateType])

slots.disease_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="disease to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.disease_to_entity_association_mixin_subject, domain=None, range=Union[str, DiseaseId])

slots.entity_to_exposure_event_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to exposure event association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_exposure_event_association_mixin_object, domain=None, range=Union[dict, ExposureEvent])

slots.exposure_event_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="exposure event to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.exposure_event_to_entity_association_mixin_subject, domain=None, range=Union[dict, ExposureEvent])

slots.entity_to_outcome_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to outcome association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_outcome_association_mixin_object, domain=None, range=Union[dict, Outcome])

slots.entity_to_phenotypic_feature_association_mixin_description = Slot(uri=CSOLINK.description, name="entity to phenotypic feature association mixin_description", curie=CSOLINK.curie('description'),
                   model_uri=CSOLINK.entity_to_phenotypic_feature_association_mixin_description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.entity_to_phenotypic_feature_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to phenotypic feature association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_phenotypic_feature_association_mixin_object, domain=None, range=Union[str, PhenotypicFeatureId])

slots.entity_to_disease_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to disease association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_disease_association_mixin_object, domain=None, range=Union[str, DiseaseId])

slots.disease_or_phenotypic_feature_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="disease or phenotypic feature to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.disease_or_phenotypic_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.disease_or_phenotypic_feature_association_to_location_association_object = Slot(uri=CSOLINK.object, name="disease or phenotypic feature association to location association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.disease_or_phenotypic_feature_association_to_location_association_object, domain=DiseaseOrPhenotypicFeatureAssociationToLocationAssociation, range=Union[str, AnatomicalEntityId])

slots.disease_or_phenotypic_feature_to_location_association_object = Slot(uri=CSOLINK.object, name="disease or phenotypic feature to location association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.disease_or_phenotypic_feature_to_location_association_object, domain=DiseaseOrPhenotypicFeatureToLocationAssociation, range=Union[str, AnatomicalEntityId])

slots.entity_to_disease_or_phenotypic_feature_association_mixin_object = Slot(uri=CSOLINK.object, name="entity to disease or phenotypic feature association mixin_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.entity_to_disease_or_phenotypic_feature_association_mixin_object, domain=None, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.genotype_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="genotype to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_to_entity_association_mixin_subject, domain=None, range=Union[str, GenotypeId])

slots.genotype_to_phenotypic_feature_association_predicate = Slot(uri=CSOLINK.predicate, name="genotype to phenotypic feature association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.genotype_to_phenotypic_feature_association_predicate, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, PredicateType])

slots.genotype_to_phenotypic_feature_association_subject = Slot(uri=CSOLINK.subject, name="genotype to phenotypic feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_to_phenotypic_feature_association_subject, domain=GenotypeToPhenotypicFeatureAssociation, range=Union[str, GenotypeId])

slots.exposure_event_to_phenotypic_feature_association_subject = Slot(uri=CSOLINK.subject, name="exposure event to phenotypic feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.exposure_event_to_phenotypic_feature_association_subject, domain=ExposureEventToPhenotypicFeatureAssociation, range=Union[dict, ExposureEvent])

slots.gene_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="gene to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_entity_association_mixin_subject, domain=None, range=Union[str, GeneOrGeneProductId])

slots.variant_to_entity_association_mixin_subject = Slot(uri=CSOLINK.subject, name="variant to entity association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_entity_association_mixin_subject, domain=None, range=Union[str, SequenceVariantId])

slots.gene_to_phenotypic_feature_association_subject = Slot(uri=CSOLINK.subject, name="gene to phenotypic feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_phenotypic_feature_association_subject, domain=GeneToPhenotypicFeatureAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_disease_association_subject = Slot(uri=CSOLINK.subject, name="gene to disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_disease_association_subject, domain=GeneToDiseaseAssociation, range=Union[str, GeneOrGeneProductId])

slots.variant_to_gene_association_object = Slot(uri=CSOLINK.object, name="variant to gene association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.variant_to_gene_association_object, domain=VariantToGeneAssociation, range=Union[str, GeneId])

slots.variant_to_gene_association_predicate = Slot(uri=CSOLINK.predicate, name="variant to gene association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.variant_to_gene_association_predicate, domain=VariantToGeneAssociation, range=Union[str, PredicateType])

slots.variant_to_gene_expression_association_predicate = Slot(uri=CSOLINK.predicate, name="variant to gene expression association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.variant_to_gene_expression_association_predicate, domain=VariantToGeneExpressionAssociation, range=Union[str, PredicateType])

slots.variant_to_population_association_subject = Slot(uri=CSOLINK.subject, name="variant to population association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=CSOLINK.object, name="variant to population association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.variant_to_population_association_has_quotient = Slot(uri=CSOLINK.has_quotient, name="variant to population association_has quotient", curie=CSOLINK.curie('has_quotient'),
                   model_uri=CSOLINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=CSOLINK.has_count, name="variant to population association_has count", curie=CSOLINK.curie('has_count'),
                   model_uri=CSOLINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=CSOLINK.has_total, name="variant to population association_has total", curie=CSOLINK.curie('has_total'),
                   model_uri=CSOLINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=CSOLINK.subject, name="population to population association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_object = Slot(uri=CSOLINK.object, name="population to population association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualOrganismsId])

slots.population_to_population_association_predicate = Slot(uri=CSOLINK.predicate, name="population to population association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.population_to_population_association_predicate, domain=PopulationToPopulationAssociation, range=Union[str, PredicateType])

slots.variant_to_phenotypic_feature_association_subject = Slot(uri=CSOLINK.subject, name="variant to phenotypic feature association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_phenotypic_feature_association_subject, domain=VariantToPhenotypicFeatureAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_disease_association_subject = Slot(uri=CSOLINK.subject, name="variant to disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_to_disease_association_subject, domain=VariantToDiseaseAssociation, range=Union[str, NamedThingId])

slots.variant_to_disease_association_predicate = Slot(uri=CSOLINK.predicate, name="variant to disease association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.variant_to_disease_association_predicate, domain=VariantToDiseaseAssociation, range=Union[str, PredicateType])

slots.variant_to_disease_association_object = Slot(uri=CSOLINK.object, name="variant to disease association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.variant_to_disease_association_object, domain=VariantToDiseaseAssociation, range=Union[str, NamedThingId])

slots.genotype_to_disease_association_subject = Slot(uri=CSOLINK.subject, name="genotype to disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_to_disease_association_subject, domain=GenotypeToDiseaseAssociation, range=Union[str, NamedThingId])

slots.genotype_to_disease_association_predicate = Slot(uri=CSOLINK.predicate, name="genotype to disease association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.genotype_to_disease_association_predicate, domain=GenotypeToDiseaseAssociation, range=Union[str, PredicateType])

slots.genotype_to_disease_association_object = Slot(uri=CSOLINK.object, name="genotype to disease association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.genotype_to_disease_association_object, domain=GenotypeToDiseaseAssociation, range=Union[str, NamedThingId])

slots.model_to_disease_association_mixin_subject = Slot(uri=CSOLINK.subject, name="model to disease association mixin_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.model_to_disease_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.model_to_disease_association_mixin_predicate = Slot(uri=CSOLINK.predicate, name="model to disease association mixin_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.model_to_disease_association_mixin_predicate, domain=None, range=Union[str, PredicateType])

slots.gene_as_a_model_of_disease_association_subject = Slot(uri=CSOLINK.subject, name="gene as a model of disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_as_a_model_of_disease_association_subject, domain=GeneAsAModelOfDiseaseAssociation, range=Union[str, GeneOrGeneProductId])

slots.variant_as_a_model_of_disease_association_subject = Slot(uri=CSOLINK.subject, name="variant as a model of disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.variant_as_a_model_of_disease_association_subject, domain=VariantAsAModelOfDiseaseAssociation, range=Union[str, SequenceVariantId])

slots.genotype_as_a_model_of_disease_association_subject = Slot(uri=CSOLINK.subject, name="genotype as a model of disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genotype_as_a_model_of_disease_association_subject, domain=GenotypeAsAModelOfDiseaseAssociation, range=Union[str, GenotypeId])

slots.cell_line_as_a_model_of_disease_association_subject = Slot(uri=CSOLINK.subject, name="cell line as a model of disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.cell_line_as_a_model_of_disease_association_subject, domain=CellLineAsAModelOfDiseaseAssociation, range=Union[str, CellLineId])

slots.organismal_entity_as_a_model_of_disease_association_subject = Slot(uri=CSOLINK.subject, name="organismal entity as a model of disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.organismal_entity_as_a_model_of_disease_association_subject, domain=OrganismalEntityAsAModelOfDiseaseAssociation, range=Union[str, OrganismalEntityId])

slots.gene_has_variant_that_contributes_to_disease_association_subject = Slot(uri=CSOLINK.subject, name="gene has variant that contributes to disease association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_has_variant_that_contributes_to_disease_association_subject, domain=GeneHasVariantThatContributesToDiseaseAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_expression_site_association_subject = Slot(uri=CSOLINK.subject, name="gene to expression site association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_expression_site_association_subject, domain=GeneToExpressionSiteAssociation, range=Union[str, GeneOrGeneProductId])

slots.gene_to_expression_site_association_object = Slot(uri=CSOLINK.object, name="gene to expression site association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.gene_to_expression_site_association_object, domain=GeneToExpressionSiteAssociation, range=Union[str, AnatomicalEntityId])

slots.gene_to_expression_site_association_predicate = Slot(uri=CSOLINK.predicate, name="gene to expression site association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.gene_to_expression_site_association_predicate, domain=GeneToExpressionSiteAssociation, range=Union[str, PredicateType])

slots.gene_to_expression_site_association_stage_qualifier = Slot(uri=CSOLINK.stage_qualifier, name="gene to expression site association_stage qualifier", curie=CSOLINK.curie('stage_qualifier'),
                   model_uri=CSOLINK.gene_to_expression_site_association_stage_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[str, LifeStageId]])

slots.gene_to_expression_site_association_quantifier_qualifier = Slot(uri=CSOLINK.quantifier_qualifier, name="gene to expression site association_quantifier qualifier", curie=CSOLINK.curie('quantifier_qualifier'),
                   model_uri=CSOLINK.gene_to_expression_site_association_quantifier_qualifier, domain=GeneToExpressionSiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.sequence_variant_modulates_treatment_association_subject = Slot(uri=CSOLINK.subject, name="sequence variant modulates treatment association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.sequence_variant_modulates_treatment_association_subject, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[str, SequenceVariantId])

slots.sequence_variant_modulates_treatment_association_object = Slot(uri=CSOLINK.object, name="sequence variant modulates treatment association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.sequence_variant_modulates_treatment_association_object, domain=SequenceVariantModulatesTreatmentAssociation, range=Union[str, TreatmentId])

slots.functional_association_subject = Slot(uri=CSOLINK.subject, name="functional association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.functional_association_subject, domain=FunctionalAssociation, range=Union[str, MacromolecularMachineId])

slots.functional_association_object = Slot(uri=CSOLINK.object, name="functional association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.functional_association_object, domain=FunctionalAssociation, range=Union[str, GeneOntologyClassId])

slots.macromolecular_machine_to_molecular_activity_association_object = Slot(uri=CSOLINK.object, name="macromolecular machine to molecular activity association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.macromolecular_machine_to_molecular_activity_association_object, domain=MacromolecularMachineToMolecularActivityAssociation, range=Union[str, MolecularActivityId])

slots.macromolecular_machine_to_biological_process_association_object = Slot(uri=CSOLINK.object, name="macromolecular machine to biological process association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.macromolecular_machine_to_biological_process_association_object, domain=MacromolecularMachineToBiologicalProcessAssociation, range=Union[str, BiologicalProcessId])

slots.macromolecular_machine_to_cellular_component_association_object = Slot(uri=CSOLINK.object, name="macromolecular machine to cellular component association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.macromolecular_machine_to_cellular_component_association_object, domain=MacromolecularMachineToCellularComponentAssociation, range=Union[str, CellularComponentId])

slots.gene_to_go_term_association_subject = Slot(uri=CSOLINK.subject, name="gene to go term association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_go_term_association_subject, domain=GeneToGoTermAssociation, range=Union[str, MolecularEntityId])

slots.gene_to_go_term_association_object = Slot(uri=CSOLINK.object, name="gene to go term association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.gene_to_go_term_association_object, domain=GeneToGoTermAssociation, range=Union[str, GeneOntologyClassId])

slots.genomic_sequence_localization_subject = Slot(uri=CSOLINK.subject, name="genomic sequence localization_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.genomic_sequence_localization_subject, domain=GenomicSequenceLocalization, range=Union[str, GenomicEntityId])

slots.genomic_sequence_localization_object = Slot(uri=CSOLINK.object, name="genomic sequence localization_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.genomic_sequence_localization_object, domain=GenomicSequenceLocalization, range=Union[str, GenomicEntityId])

slots.genomic_sequence_localization_predicate = Slot(uri=CSOLINK.predicate, name="genomic sequence localization_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.genomic_sequence_localization_predicate, domain=GenomicSequenceLocalization, range=Union[str, PredicateType])

slots.sequence_feature_relationship_subject = Slot(uri=CSOLINK.subject, name="sequence feature relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[str, GenomicEntityId])

slots.sequence_feature_relationship_object = Slot(uri=CSOLINK.object, name="sequence feature relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[str, GenomicEntityId])

slots.transcript_to_gene_relationship_subject = Slot(uri=CSOLINK.subject, name="transcript to gene relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.transcript_to_gene_relationship_subject, domain=TranscriptToGeneRelationship, range=Union[str, TranscriptId])

slots.transcript_to_gene_relationship_object = Slot(uri=CSOLINK.object, name="transcript to gene relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.transcript_to_gene_relationship_object, domain=TranscriptToGeneRelationship, range=Union[str, GeneId])

slots.gene_to_gene_product_relationship_subject = Slot(uri=CSOLINK.subject, name="gene to gene product relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_to_gene_product_relationship_subject, domain=GeneToGeneProductRelationship, range=Union[str, GeneId])

slots.gene_to_gene_product_relationship_object = Slot(uri=CSOLINK.object, name="gene to gene product relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.gene_to_gene_product_relationship_object, domain=GeneToGeneProductRelationship, range=Union[str, GeneProductId])

slots.gene_to_gene_product_relationship_predicate = Slot(uri=CSOLINK.predicate, name="gene to gene product relationship_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.gene_to_gene_product_relationship_predicate, domain=GeneToGeneProductRelationship, range=Union[str, PredicateType])

slots.exon_to_transcript_relationship_subject = Slot(uri=CSOLINK.subject, name="exon to transcript relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.exon_to_transcript_relationship_subject, domain=ExonToTranscriptRelationship, range=Union[str, ExonId])

slots.exon_to_transcript_relationship_object = Slot(uri=CSOLINK.object, name="exon to transcript relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.exon_to_transcript_relationship_object, domain=ExonToTranscriptRelationship, range=Union[str, TranscriptId])

slots.gene_regulatory_relationship_predicate = Slot(uri=CSOLINK.predicate, name="gene regulatory relationship_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.gene_regulatory_relationship_predicate, domain=GeneRegulatoryRelationship, range=Union[str, PredicateType])

slots.gene_regulatory_relationship_subject = Slot(uri=CSOLINK.subject, name="gene regulatory relationship_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.gene_regulatory_relationship_subject, domain=GeneRegulatoryRelationship, range=Union[str, GeneOrGeneProductId])

slots.gene_regulatory_relationship_object = Slot(uri=CSOLINK.object, name="gene regulatory relationship_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.gene_regulatory_relationship_object, domain=GeneRegulatoryRelationship, range=Union[str, GeneOrGeneProductId])

slots.anatomical_entity_to_anatomical_entity_association_subject = Slot(uri=CSOLINK.subject, name="anatomical entity to anatomical entity association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_association_subject, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_association_object = Slot(uri=CSOLINK.object, name="anatomical entity to anatomical entity association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_association_object, domain=AnatomicalEntityToAnatomicalEntityAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_subject = Slot(uri=CSOLINK.subject, name="anatomical entity to anatomical entity part of association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_part_of_association_subject, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_object = Slot(uri=CSOLINK.object, name="anatomical entity to anatomical entity part of association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_part_of_association_object, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_part_of_association_predicate = Slot(uri=CSOLINK.predicate, name="anatomical entity to anatomical entity part of association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_part_of_association_predicate, domain=AnatomicalEntityToAnatomicalEntityPartOfAssociation, range=Union[str, PredicateType])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_subject = Slot(uri=CSOLINK.subject, name="anatomical entity to anatomical entity ontogenic association_subject", curie=CSOLINK.curie('subject'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_subject, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_object = Slot(uri=CSOLINK.object, name="anatomical entity to anatomical entity ontogenic association_object", curie=CSOLINK.curie('object'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_object, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, AnatomicalEntityId])

slots.anatomical_entity_to_anatomical_entity_ontogenic_association_predicate = Slot(uri=CSOLINK.predicate, name="anatomical entity to anatomical entity ontogenic association_predicate", curie=CSOLINK.curie('predicate'),
                   model_uri=CSOLINK.anatomical_entity_to_anatomical_entity_ontogenic_association_predicate, domain=AnatomicalEntityToAnatomicalEntityOntogenicAssociation, range=Union[str, PredicateType])
