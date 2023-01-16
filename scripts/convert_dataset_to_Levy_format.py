########################################################################################################################
# Script to convert the antonym pair entailment dataset into the format used by the Levy/Holt dataset.
# Creates one output file per data subset:
#   Base (antonym (False), directional_entailment (True))
#   Directional (directional_entailment, directional_non-entailment (False))
#   Full (antonym, directional_entailment, directional_non-entailment, paraphrase (True))
#
# Command:
# python convert_dataset_to_Levy_format.py -i <input_file> -o <output_file_path>
#
#
# Liane Guillou and Sander Bijl de Vroe
# The University of Edinburgh
########################################################################################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import argparse


def read_original_file(file_name):
    """
    Read in the original tab-separated file with format:
        premise  hypothesis  label
    and return a dictionary of entailment pairs for each label
    :param file_name: file to read
    :return: dictionary of entailment pairs
    """
    result = {}
    with open(file_name, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            line = line.lower()
            line_parts = line.split("\t")
            premise = line_parts[0]
            hypothesis = line_parts[1]
            label = line_parts[2]
            if label not in result:
                result[label] = []
            result[label].append([hypothesis, premise])
    return result


def convert_format(args):
    """
    Read in the original format file, split the annotations into three output files:
    1. Base subset (antonym (False) and directional_entailment (True))
    2. Directional subset (directional_entailment and directional_non-entailment (False))
    3. All subsets (antonym, directional_entailment, directional_non-entailment, paraphrase (True))
    :param args: command line arguments
    :return: N/A
    """
    subset_group_map = {"ant_base": ["antonym", "directional_entailment"],
                        "ant_directional": ["directional_entailment", "directional_non-entailment"],
                        "ant_full": ["antonym", "directional_entailment", "directional_non-entailment", "paraphrase"]}
    label_map = {"antonym": "False",
                 "directional_entailment": "True",
                 "directional_non-entailment": "False",
                 "paraphrase": "True"}

    # Read original format file
    subsets = read_original_file(args.inputFile)

    # Write output files
    for subset_group in subset_group_map:
        file_name_s = os.path.join(args.outputFilePath, subset_group + "_s.txt")
        file_name_s2 = os.path.join(args.outputFilePath, subset_group + "_s2.txt")
        file_name = os.path.join(args.outputFilePath, subset_group + ".txt")
        with open(file_name_s, "w") as o_s, open(file_name_s2, "w") as o_s2, open(file_name, "w") as o:
            for subset_label in subset_group_map[subset_group]:
                for entailment_pair in subsets[subset_label]:
                    label = label_map[subset_label]
                    output_line = "\t".join([entailment_pair[0], entailment_pair[1], label])
                    output_line_s = "\t".join([entailment_pair[0].replace(", ", " "),
                                               entailment_pair[1].replace(", ", " "), label])
                    output_line_s2 = "\t".join([entailment_pair[0].replace(", ", ","),
                                                entailment_pair[1].replace(", ", ","), label])
                    o.write(output_line + "\n")
                    o_s.write(output_line_s + "\n")
                    o_s2.write(output_line_s2 + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputFile", help="Input file containing the antonym pair dataset")
    parser.add_argument("-o", "--outputFilePath", help="Output file path")

    args = parser.parse_args()

    convert_format(args)


if __name__ == "__main__":
    main()