# PhraseTableCombination
This repository describes two of our works in Phrase Table Combination Based on Symmetrization of Word Alignment for Low-Resource Languages:
1. We construct an algorithm to compare phrase translation parameter scores from two phrase tables. 
Phrase translation parameters score were computed from the co-occurrence of aligned phrases in the training corpora, then stored in the phrase table along with the phrase pair. The scores consist of inverse phrase translation probability (p(t|s)), inverse lexical weighting (lex(t|s)), direct phrase translation probability (p(s|t)), and direct lexical weight (lex(s|t)). Our algorithm is to found which component of phrase translation parameters affects the improvement of the BLEU scores. First, we collect 2,000 phrase pairs and their phrase translation parameters scores from phrase table of highest BLEU score as phrase table 1 (PT1). Subsequently, we collect 12,000 phrase pairs and their phrase translation parameters scores from phrase table of second highest BLEU score as phrase table 2 (PT2). Last, we examined which component of phrase translation parameter of PT1 that obtain higher score than phrase translation parameter of PT2 in same phrase pair.

<br>
<img height="500" src="https://github.com/s4d3/PhraseTableCombination/blob/master/TheComparisonAlgorithm.png" />
<br>
