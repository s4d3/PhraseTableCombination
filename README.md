# PhraseTableCombination
This repository describes one of our works in Phrase Table Combination Based on Symmetrization of Word Alignment for Low-Resource Languages. We construct an algorithm to compare phrase translation parameter scores from two phrase tables. Phrase translation parameters score were computed from the co-occurrence of aligned phrases in the training corpora, then stored in the phrase table along with the phrase pair. The scores consist of inverse phrase translation probability (p(t|s)), inverse lexical weighting (lex(t|s)), direct phrase translation probability (p(s|t)), and direct lexical weight (lex(s|t)). 

Our algorithms are to found which component of phrase translation parameters affects the improvement of the BLEU scores. 
