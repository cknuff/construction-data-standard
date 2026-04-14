#!/bin/bash
# Deploy UCDM to construction-data-standard.vercel.app
# Always use this script instead of `vercel --prod` directly.

set -e

echo "Deploying to Vercel..."
OUTPUT=$(npx vercel --prod --yes --scope procore-v0 2>&1)
echo "$OUTPUT"

# Extract the deployment URL
DEPLOY_URL=$(echo "$OUTPUT" | grep -o 'https://construction-data-standard-[^ ]*\.vercel\.app' | head -1)

if [ -z "$DEPLOY_URL" ]; then
  echo "ERROR: Could not extract deployment URL"
  exit 1
fi

echo ""
echo "Aliasing to construction-data-standard.vercel.app..."
npx vercel alias set "$DEPLOY_URL" construction-data-standard.vercel.app --scope procore-v0

echo ""
echo "Done! Live at https://construction-data-standard.vercel.app"
