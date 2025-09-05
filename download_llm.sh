#!/bin/bash

#hf download openai/gpt-oss-20b --include original/* --local-dir gpt-oss-20b/


#huggingface-cli download openai/gpt-oss-20b --include "original/*" --local-dir gpt-oss-20b/
#pip install gpt-oss
#python -m gpt_oss.chat model/

#hf download gpt2 config.json --local-dir gpt2


#pip install huggingface-hub[hf_transfer]
#pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
export HF_HUB_ENABLE_EMERGENCY_RETRY=True
export HF_ENABLE_EMERGENCY_RETRY_WAIT_TIME=1
export force_download=True
export HF_HUB_DOWNLOAD_THREADS=32
export HF_HUB_DOWNLOAD_CHUNK_SIZE=209715200
#209715200
#104857600
#hf download openai/gpt-oss-20b --local-dir gpt-oss-20b



hf download openai-community/gpt2 --local-dir gpt2/
#meta-llama/Llama-3.2-1B --local-dir llama/
#microsoft/phi-3 --local-dir phi3
#google/gemma-3-270m --local-dir gemma3/
#mistralai/Mistral-7B-v0.1 --local-dir mistral7B/





