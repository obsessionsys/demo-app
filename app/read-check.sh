#!/bin/sh
# read-check.sh

set -e

host="$1"
shift
cmd="$@"

until ping -c 1 -w 50 prometheus-app ; do
  >&2 echo "Prometheus is unavailable - sleeping"
  sleep 1
done

>&2 echo "Prometheus is up - executing command"
exec $cmd