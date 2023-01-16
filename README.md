#Ant

The Ant dataset consists of entailment pairs suitable for evaluating Entailment Graphs constructed for the open domain. It is based on antonymous predicate pairs.

We provide a pre-defined dev/test split for Ant. In our work we have applied an unsupervised method to learning Entailment Graphs, which we have evaluated using the test set (data/ant_test.txt). A small development set (data/ant_dev.txt) is provided for those who wish to apply supervised methods to learning Entailment Graphs.

###Dataset Format

The files ant_test.txt and ant_dev.txt are tab separated, with each line containing an entailment relation between two predicates P and Q. Column 1 contains predicate P, column 2 contains predicate Q, and column 3 contains the entailment type label.
There are four possible values for entailment type:

* antonym: P is an antonym of Q; P does not entail Q
* directional_entailment: P entails Q (but Q does not entail P)
* directional_non-entailment: the set of directional entailments with the direction reversed; P does not entail Q
* paraphrase: P is a paraphrase of Q; P entails Q

###Convert to Levy/Holt format

To convert Ant to the Levy/Holt dataset, commonly used to evaluate Entailment Graphs, run the following:

```
python3 convert_dataset_to_Levy_format.py -i data/ant_test.txt -o <output_file_path>
```

###Licence
Code is licensed under the MIT License, data under the Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0).

###Contact

* Please direct any queries regarding Ant to Liane Guillou:
liane [dot] guillou [at] ed.ac.uk