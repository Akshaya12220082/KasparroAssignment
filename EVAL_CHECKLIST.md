# Evaluation Checklist

Use this checklist to self-review your work before submission.

## ✅ Project Structure

- [ ] Repository follows naming format: `kasparro-agentic-fb-analyst-<firstname-lastname>`
- [ ] All required files are present:
  - [ ] `README.md` with setup instructions
  - [ ] `requirements.txt` with all dependencies
  - [ ] `.gitignore` properly configured
  - [ ] Main Python files (`main.py`, `agent.py`, `data_loader.py`, `config.py`)
  - [ ] Environment template file (`env_template.txt` or `.env.example`)

## ✅ Functionality

- [ ] System successfully loads and processes `synthetic_fb_ads_undergarments.csv`
- [ ] Generates `insights.json` with proper structure:
  - [ ] Key insights with metrics, values, impact, and recommendations
  - [ ] Performance summary (top performers, underperformers, trends)
  - [ ] Opportunities with action items
- [ ] Generates `creatives.json` with proper structure:
  - [ ] Creative recommendations with campaign type, format, copy, CTA
  - [ ] A/B test suggestions
  - [ ] Creative best practices
- [ ] Generates `report.md` with:
  - [ ] Executive summary
  - [ ] Data overview
  - [ ] Key insights
  - [ ] Performance analysis
  - [ ] Creative recommendations
  - [ ] Action items

## ✅ Code Quality

- [ ] Code is well-structured and modular
- [ ] Proper error handling for missing files, API errors, etc.
- [ ] Code follows Python best practices (PEP 8)
- [ ] No linting errors
- [ ] Proper docstrings and comments
- [ ] Type hints where appropriate

## ✅ Agentic System

- [ ] Uses LLM (OpenAI) for analysis
- [ ] Implements proper prompt engineering
- [ ] Handles JSON parsing robustly (handles markdown-wrapped JSON)
- [ ] System is truly "agentic" - makes decisions and generates insights autonomously
- [ ] Multiple agentic steps (insights → creatives → report) with context passing

## ✅ Observability

- [ ] Langfuse integration implemented (optional but recommended)
- [ ] Traces are properly logged if Langfuse is configured
- [ ] System works gracefully without Langfuse (doesn't break if not configured)

## ✅ Documentation

- [ ] README includes:
  - [ ] Clear setup instructions
  - [ ] Data path specified
  - [ ] Sample output examples
  - [ ] Troubleshooting section
  - [ ] Project structure
- [ ] Code is self-documenting with clear variable names and docstrings

## ✅ Output Files

- [ ] `output/insights.json` exists and is valid JSON
- [ ] `output/creatives.json` exists and is valid JSON
- [ ] `output/report.md` exists and is well-formatted markdown
- [ ] All outputs are in the `output/` directory

## ✅ Testing

- [ ] System runs without errors with sample data
- [ ] Handles edge cases (empty data, missing columns, etc.)
- [ ] Works with the provided `synthetic_fb_ads_undergarments.csv`

## ✅ Git & GitHub

- [ ] Repository is public
- [ ] All files are committed
- [ ] `.env` file is NOT committed (in `.gitignore`)
- [ ] Sensitive data is not committed
- [ ] v1.0 release tag is created
- [ ] Repository has a clear commit history

## ✅ Submission

- [ ] Google form filled out with GitHub repo link
- [ ] Repository link is correct and accessible
- [ ] All deliverables are present in the repo

## Notes

- Make sure your OpenAI API key is set in `.env` (not committed to git)
- Test the full pipeline before submission
- Review the generated outputs for quality and relevance
- Ensure the system works end-to-end without manual intervention

