#!/bin/bash
cd ~/Desktop/KaizenFlowNew
source .venv/bin/activate
uvicorn app.main:app --reload
