#!/bin/bash

# DEPLOY_USER and DEPLOY_PASS are defined as private Environment Variables
# in the Travis web UI: https://travis-ci.org/18F/django-uswds-forms/settings

set -e

API="https://api.fr.cloud.gov"
ORG="sandbox-gsa"

SPACE="atul.varma"
APP_NAME="django-uswds-forms"
MANIFEST="manifest.yml"

echo "Deploying to $SPACE space."

cd example

cf login -a $API -u $DEPLOY_USER -p $DEPLOY_PASS -o $ORG -s $SPACE

cf push $APP_NAME
