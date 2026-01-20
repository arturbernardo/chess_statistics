#!/bin/bash

case "$1" in
  up)
    aws cloudformation create-stack \
      --stack-name chess-analysis \
      --template-body file://cloudformation.yaml \
      --parameters ParameterKey=KeyName,ParameterValue=n8n
    ;;
  down)
    aws cloudformation delete-stack \
      --stack-name chess-analysis
    ;;
esac