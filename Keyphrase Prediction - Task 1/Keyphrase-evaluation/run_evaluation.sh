#!/usr/bin/env bash

export PYTHONIOENCODING=utf-8

HOME_DIR=`realpath .`
export PYTHONPATH=${PYTHONPATH}:${HOME_DIR}

dataset=ikea
model=llama-instruct-finetuned-rslora
metrics=semantic_matching

OUTDIR=${HOME_DIR}/eval_results/${dataset}/${model}/
mkdir -p ${OUTDIR}

python ${HOME_DIR}/run_evaluation.py \
       --config-file ${HOME_DIR}/configs/sample_config_${dataset}.gin \
       --jsonl-file ${HOME_DIR}/model_outputs/${dataset}/${model}/${dataset}_hypotheses_linked.json \
       --metrics ${metrics} \
       --log-file-prefix ${OUTDIR}
