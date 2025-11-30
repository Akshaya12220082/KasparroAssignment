# PowerShell helper script to set up GitHub repository and create v1.0 release tag

Write-Host "Setting up GitHub repository for Kasparro assignment..." -ForegroundColor Cyan

# Check if git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
}

# Add all files
Write-Host "Adding files to git..." -ForegroundColor Yellow
git add .

# Create initial commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Agentic FB Analyst system"

# Create v1.0 tag
Write-Host "Creating v1.0 release tag..." -ForegroundColor Yellow
git tag -a v1.0 -m "Release v1.0: Agentic FB Analyst submission"

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Create a public repository on GitHub with name: kasparro-agentic-fb-analyst-<firstname-lastname>"
Write-Host "2. Add the remote: git remote add origin <your-repo-url>"
Write-Host "3. Push: git push -u origin main"
Write-Host "4. Push tags: git push origin v1.0"
Write-Host ""
Write-Host "Then submit your repo link via the Google form." -ForegroundColor Yellow

