#!/bin/bash
set -e

STACK_NAME=chess-analysis
TEMPLATE=cloudformation.yaml

case "$1" in
  up)
    aws cloudformation deploy \
      --stack-name "$STACK_NAME" \
      --template-file "$TEMPLATE" \
      --capabilities CAPABILITY_IAM \
      --parameter-overrides \
        KeyName=n8n \
        HttpPort="$2" \
        InstanceType="$3" \
        GameType="$4" \
        GameUser="$5" \
        SizeLimit="$6" \
        Start="$7" \
        End="$8" \
        GameUserLower=$(echo $5 | tr '[:upper:]' '[:lower:]')
    ;;
  down)
    aws cloudformation delete-stack \
      --stack-name "$STACK_NAME"
    ;;
  *)
    echo "Uso:"
    echo "  $0 up <httpPort> <instanceType> <gameType> <user> <sizeLimit> <start> <end>"
    echo "  $0 down"
    exit 1
    ;;
esac
