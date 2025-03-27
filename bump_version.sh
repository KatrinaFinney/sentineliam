#!/bin/bash

set -e

VERSION_FILE="pyproject.toml"
VERSION_LINE=$(grep -E '^version = "' $VERSION_FILE)
CURRENT_VERSION=$(echo $VERSION_LINE | sed -E 's/version = "([0-9]+)\.([0-9]+)\.([0-9]+)"/\1.\2.\3/')

IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"

case "$1" in
  patch)
    PATCH=$((PATCH + 1))
    ;;
  minor)
    MINOR=$((MINOR + 1))
    PATCH=0
    ;;
  major)
    MAJOR=$((MAJOR + 1))
    MINOR=0
    PATCH=0
    ;;
  *)
    echo "Usage: $0 [patch|minor|major]"
    exit 1
    ;;
esac

NEW_VERSION="$MAJOR.$MINOR.$PATCH"

echo "🔁 Bumping version: $CURRENT_VERSION → $NEW_VERSION"

# Replace version line
sed -i '' -E "s/^version = \".*\"/version = \"$NEW_VERSION\"/" $VERSION_FILE

# Commit and tag
git add $VERSION_FILE
git commit -m "🔖 Bump version: $CURRENT_VERSION → $NEW_VERSION"
git tag "v$NEW_VERSION"

echo "✅ Done. Committed and tagged v$NEW_VERSION"
