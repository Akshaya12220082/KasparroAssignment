#!/bin/bash
# Helper script to set up GitHub repository and create v1.0 release tag

echo "Setting up GitHub repository for Kasparro assignment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add all files
echo "Adding files to git..."
git add .

# Create initial commit
echo "Creating initial commit..."
git commit -m "Initial commit: Agentic FB Analyst system"

# Create v1.0 tag
echo "Creating v1.0 release tag..."
git tag -a v1.0 -m "Release v1.0: Agentic FB Analyst submission"

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a public repository on GitHub with name: kasparro-agentic-fb-analyst-<firstname-lastname>"
echo "2. Add the remote: git remote add origin <your-repo-url>"
echo "3. Push: git push -u origin main"
echo "4. Push tags: git push origin v1.0"
echo ""
echo "Then submit your repo link via the Google form."

