# Agentic Facebook Ads Analyst

An intelligent, agentic system for analyzing Facebook ads performance data and generating actionable insights, creative recommendations, and comprehensive reports.

## 🎯 Overview

This project implements an agentic AI system that:
- Analyzes Facebook ads performance data
- Generates actionable insights (`insights.json`)
- Provides creative recommendations (`creatives.json`)
- Creates comprehensive analysis reports (`report.md`)
- Integrates with Langfuse for observability and tracing

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- (Optional) Langfuse account for tracing

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/kasparro-agentic-fb-analyst-<firstname-lastname>.git
cd kasparro-agentic-fb-analyst-<firstname-lastname>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# On Windows PowerShell
Copy-Item env_template.txt .env

# On Linux/Mac
cp env_template.txt .env
```

Edit `.env` and add your credentials:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o

# Optional - for Langfuse tracing
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com

# Data Configuration
DATA_PATH=synthetic_fb_ads_undergarments.csv
OUTPUT_DIR=output
```

### 4. Prepare Your Data

Place your `synthetic_fb_ads_undergarments.csv` file in the project root directory.

If you don't have the dataset, you can generate a sample one using:

```bash
python generate_sample_data.py
```

## 📊 Data Path

The system expects the data file at: `synthetic_fb_ads_undergarments.csv` (in the project root)

You can change this path by setting the `DATA_PATH` environment variable in your `.env` file.

## 🏃 Running the Analysis

Execute the main script:

```bash
python main.py
```

The system will:
1. Load and analyze the Facebook ads data
2. Generate insights
3. Create creative recommendations
4. Generate a comprehensive report
5. Save all outputs to the `output/` directory

## 📁 Output Files

After running the analysis, you'll find the following files in the `output/` directory:

- **insights.json**: Key insights, performance summary, and opportunities
- **creatives.json**: Creative recommendations, A/B test suggestions, and best practices
- **report.md**: Comprehensive markdown report with executive summary and detailed analysis

## 📝 Sample Output

### insights.json Structure

```json
{
  "key_insights": [
    {
      "insight": "Campaign X shows 3x higher CTR",
      "metric": "Click-Through Rate",
      "value": "4.5%",
      "impact": "high",
      "recommendation": "Scale similar creative approaches"
    }
  ],
  "performance_summary": {
    "top_performers": [...],
    "underperformers": [...],
    "trends": [...]
  },
  "opportunities": [...]
}
```

### creatives.json Structure

```json
{
  "creative_recommendations": [
    {
      "campaign_type": "Conversion",
      "ad_format": "Carousel",
      "headline": "...",
      "primary_text": "...",
      "call_to_action": "Shop Now",
      "visual_elements": [...],
      "targeting_suggestions": [...],
      "rationale": "..."
    }
  ],
  "a_b_test_suggestions": [...],
  "creative_best_practices": [...]
}
```

### report.md

A comprehensive markdown report including:
- Executive Summary
- Data Overview
- Key Insights
- Performance Analysis
- Creative Recommendations
- Action Items and Next Steps

## 🔍 Observability

The system integrates with Langfuse for tracing and observability. If you've configured Langfuse credentials, all LLM calls will be automatically traced and logged.

To view traces:
1. Log in to your Langfuse dashboard
2. Navigate to the Traces section
3. Filter by the trace name or session

## 🏗️ Project Structure

```
kasparro-agentic-fb-analyst-<firstname-lastname>/
├── main.py                 # Main entry point
├── agent.py                # Agentic system implementation
├── data_loader.py          # Data loading and preprocessing
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── synthetic_fb_ads_undergarments.csv  # Input data
├── generate_sample_data.py # Optional: Generate sample data
└── output/                # Generated outputs
    ├── insights.json
    ├── creatives.json
    └── report.md
```

## 🧪 Testing

### Validate Setup

First, validate that your project is set up correctly:

```bash
python validate_setup.py
```

### Generate Sample Data

If you don't have the dataset, generate sample data:

```bash
python generate_sample_data.py
```

### Run Analysis

Run the full analysis:

```bash
python main.py
```

## 📚 Dependencies

- `openai`: OpenAI API client
- `langchain`: LLM framework
- `langchain-openai`: OpenAI integration for LangChain
- `langfuse`: Observability and tracing
- `pandas`: Data manipulation
- `numpy`: Numerical operations
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation

## 🔧 Troubleshooting

### Issue: "Data file not found"
- Ensure `synthetic_fb_ads_undergarments.csv` is in the project root
- Check the `DATA_PATH` in your `.env` file

### Issue: "OpenAI API key not found"
- Verify your `.env` file contains `OPENAI_API_KEY`
- Ensure the `.env` file is in the project root

### Issue: Langfuse errors
- Langfuse is optional. If you don't want to use it, leave the Langfuse credentials empty in `.env`
- The system will work without Langfuse, just without tracing

## 📄 License

This project is created for the Kasparro Applied AI Engineer assignment.

## 👤 Author

<firstname-lastname>

---

**Note**: This is an assignment submission for Kasparro's Applied AI Engineer position.

