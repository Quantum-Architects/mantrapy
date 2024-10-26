#!/bin/bash
source /opt/homebrew/opt/nvm/nvm.sh && nvm use && npm install && npm run build
mv ./docs/dist ./dist
