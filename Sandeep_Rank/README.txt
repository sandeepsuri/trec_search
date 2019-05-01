{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 For Sandeep\'92s Ranking:\
\
Make sure the following are in the folder:\
\
train.benchmarkY1train.cbor.hierarchical.qrels\
train.benchmarkY1train.cbor.outlines\
train.benchmarkY1train.cbor.paragraphs\
\
With these three files, this is out you produce a run file:\
\
In your command line, enter in:\
\
>> python3 gen_rankings.py train.benchmarkY1train.cbor.outlines train.benchmarkY1train.cbor.paragraphs [name of your run file] SANDEEP [# of passages]\
\
Once created, you can produce the MAP using the eval_framework.py function\
\
Enter in:\
\
>> python3 eval_framework.py train.bechmarkY1train.cbor.hierachical.qrels [your run file name]\
\
This command produces the MRR, Rprec, and MAP scores.}