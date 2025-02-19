# ----------------------------------------------------------------------------
# Copyright (c) 2016-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import SemanticType

from ..plugin_setup import plugin
from . import (TSVTaxonomyDirectoryFormat, DNASequencesDirectoryFormat,
               PairedDNASequencesDirectoryFormat,
               AlignedDNASequencesDirectoryFormat,
               DifferentialDirectoryFormat, ProteinSequencesDirectoryFormat,
               AlignedProteinSequencesDirectoryFormat,
               RNASequencesDirectoryFormat, AlignedRNASequencesDirectoryFormat,
               PairedRNASequencesDirectoryFormat, BLAST6DirectoryFormat)


FeatureData = SemanticType('FeatureData', field_names='type')

Taxonomy = SemanticType('Taxonomy', variant_of=FeatureData.field['type'])

Sequence = SemanticType('Sequence', variant_of=FeatureData.field['type'])

RNASequence = SemanticType('RNASequence', variant_of=FeatureData.field['type'])

PairedEndSequence = SemanticType('PairedEndSequence',
                                 variant_of=FeatureData.field['type'])

PairedEndRNASequence = SemanticType('PairedEndRNASequence',
                                    variant_of=FeatureData.field['type'])

AlignedSequence = SemanticType('AlignedSequence',
                               variant_of=FeatureData.field['type'])

AlignedRNASequence = SemanticType('AlignedRNASequence',
                                  variant_of=FeatureData.field['type'])

Differential = SemanticType('Differential',
                            variant_of=FeatureData.field['type'])

ProteinSequence = SemanticType('ProteinSequence',
                               variant_of=FeatureData.field['type'])

AlignedProteinSequence = SemanticType('AlignedProteinSequence',
                                      variant_of=FeatureData.field['type'])

BLAST6 = SemanticType('BLAST6', variant_of=FeatureData.field['type'])

plugin.register_semantic_types(FeatureData, Taxonomy, Sequence,
                               PairedEndSequence, AlignedSequence,
                               Differential, ProteinSequence,
                               AlignedProteinSequence, RNASequence,
                               AlignedRNASequence, PairedEndRNASequence,
                               BLAST6)


plugin.register_artifact_class(
    FeatureData[Taxonomy],
    directory_format=TSVTaxonomyDirectoryFormat,
    description=("Hierarchical metadata or annotations associated with a set "
                 "of features. This can contain one or more hierarchical "
                 "levels, and annotations can be anything (e.g., taxonomy of "
                 "organisms, functional categorization of gene families, ...) "
                 "as long as it is strictly hierarchical."))
plugin.register_artifact_class(
    FeatureData[Sequence],
    directory_format=DNASequencesDirectoryFormat,
    description=("Unaligned DNA sequences associated with a set of feature "
                 "identifiers (e.g., ASV sequences or OTU representative "
                 "sequence). Exactly one sequence is associated with each "
                 "feature identfiier."))
plugin.register_artifact_class(
    FeatureData[RNASequence],
    directory_format=RNASequencesDirectoryFormat,
    description=("Unaligned RNA sequences associated with a set of feature "
                 "identifiers. Exactly one sequence is associated with each "
                 "feature identfiier."))
plugin.register_artifact_class(
    FeatureData[PairedEndSequence],
    directory_format=PairedDNASequencesDirectoryFormat)
plugin.register_artifact_class(
    FeatureData[PairedEndRNASequence],
    directory_format=PairedRNASequencesDirectoryFormat)
plugin.register_artifact_class(
    FeatureData[AlignedSequence],
    directory_format=AlignedDNASequencesDirectoryFormat,
    description=("Aligned DNA sequences associated with a set of feature "
                 "identifiers (e.g., aligned ASV sequences or OTU "
                 "representative sequence). Exactly one sequence is "
                 "associated with each feature identfiier."))
plugin.register_artifact_class(
    FeatureData[AlignedRNASequence],
    directory_format=AlignedRNASequencesDirectoryFormat,
    description=("Aligned RNA sequences associated with a set of feature "
                 "identifiers. Exactly one sequence is associated with each "
                 "feature identfiier."))
plugin.register_artifact_class(
    FeatureData[Differential], DifferentialDirectoryFormat)
plugin.register_artifact_class(
    FeatureData[ProteinSequence],
    directory_format=ProteinSequencesDirectoryFormat,
    description=("Unaligned protein sequences associated with a set of "
                 "feature identifiers. Exactly one sequence is associated "
                 "with each feature identfiier."))
plugin.register_artifact_class(
    FeatureData[AlignedProteinSequence],
    directory_format=AlignedProteinSequencesDirectoryFormat,
    description=("Aligned protein sequences associated with a set of "
                 "feature identifiers. Exactly one sequence is associated "
                 "with each feature identfiier."))
# FeatureData[BLAST6] seems to fix file type with semantic type.
plugin.register_artifact_class(
    FeatureData[BLAST6],
    directory_format=BLAST6DirectoryFormat,
    description=("BLAST results associated with a set of feature "
                 "identifiers."))
