# trec_search

PRATIK'S RANKING:

Within a python IDE, after you have gone to the directory of where Pratik's ranking files are located, 
enter the following command: 

```
python gen_rankings.py train.benchmarkY1train.cbor.outlines train.benchmarkY1train.cbor.paragraphs output.prox.run PROX no_cache 100
```

the above command will create in the same directory, a run file called: "output.prox"
then within this same directory, enter the following command to produce MRR, Rprec and MAP: 

```
python eval_framework.py train.benchmarkY1train.cbor.hierarchical.qrels output.prox
```

-----------------------------------------------------------------------------------------------------
Then, copy the generated run file "output.prox" and "train.benchmarkY1train.cbor.hierarchical.qrels"
 to the directory where trec_eval content is located, this directory should have all the evaluation files 
m_num_ret.c, m_num_rel.c, m_map.c, etc.   In this directory, enter the following command: 

```
./trec_eval -m runid -m num_q -m num_ret -m num_rel -m map train.benchmarkY1train.cbor.hierarchical.qrels output.prox.run
```


DANU'S RANKING: 

The "Danu's Rank" folder contains three important pyhton files:

- danu_weight_score
- test_gen_rankings
- danu_tfidf_scoring
- eval_framework

The weight_score and tfidf_scoring files compute the weight and score of each passage. The gen_rankings
file uses these scores to rank passages based on their relevance to the query. The gen rankings file also creates 
a run/output file to compare with relevance judgement files using eval_framework.

Heres how the code should be run in the terminal:

1. Navigate to the folder containing the above files

2. Once all files are in the same folder, execute the following command to retrieve 100 passages from the corpus set:
***NOTE: this process may take some time depending on the number of passages retrieved***

```
python test_gen_rankings.py train.benchmarkY1train.cbor.outlines train.benchmarkY1train.cbor.paragraphs [output.______.run] RANK1 100 5
``` 
 
The command will attempt to retrieve 100 passages, and out of those 100 passsages, 5 will be used to compute the weight scores of the query  

3. After the run file is created, it must be inputted into the eval_framework file to get the precision metrics:

```
python eval_framework.py train.benchmarkY1train.cbor.hierarchical.qrels [output.______.run]
```


SANDEEP'S RANKING:

For Sandeep’s Ranking:

Make sure the following are in the folder:

train.benchmarkY1train.cbor.hierarchical.qrels
train.benchmarkY1train.cbor.outlines
train.benchmarkY1train.cbor.paragraphs

With these three files, this is out you produce a run file:

In your command line, enter in:

```
python3 gen_rankings.py train.benchmarkY1train.cbor.outlines train.benchmarkY1train.cbor.paragraphs [name of your run file] SANDEEP [# of passages]
```

Once created, you can produce the MAP using the eval_framework.py function

Enter in:

```
python3 eval_framework.py train.bechmarkY1train.cbor.hierachical.qrels [your run file name]
```

This command produces the MRR, Rprec, and MAP scores.
