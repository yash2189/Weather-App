#!/bin/bash

if [ "$SKIP_KUBELINTER" = "1" ]; then
  echo "Skipping kube-linter due to SKIP_KUBELINTER=1"
  exit 0
fi

kube-linter lint ./k8s "$@"
