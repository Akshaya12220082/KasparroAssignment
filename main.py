"""Main entry point for the agentic FB analyst."""
import json
import os
from pathlib import Path
from config import DATA_PATH, OUTPUT_DIR
from agent import AgenticFBAnalyst


def save_outputs(insights: dict, creatives: dict, report: str):
    """Save generated outputs to files.
    
    Args:
        insights: Insights dictionary
        creatives: Creatives dictionary
        report: Markdown report string
    """
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(exist_ok=True)
    
    # Save insights.json
    insights_path = output_path / "insights.json"
    with open(insights_path, 'w', encoding='utf-8') as f:
        json.dump(insights, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved insights to {insights_path}")
    
    # Save creatives.json
    creatives_path = output_path / "creatives.json"
    with open(creatives_path, 'w', encoding='utf-8') as f:
        json.dump(creatives, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved creatives to {creatives_path}")
    
    # Save report.md
    report_path = output_path / "report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✓ Saved report to {report_path}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("Agentic Facebook Ads Analyst")
    print("=" * 60)
    
    # Check if data file exists
    if not os.path.exists(DATA_PATH):
        print(f"\n❌ Error: Data file not found at {DATA_PATH}")
        print("Please ensure the synthetic_fb_ads_undergarments.csv file is in the project root.")
        return
    
    # Initialize analyst
    analyst = AgenticFBAnalyst(DATA_PATH)
    
    # Run full analysis
    results = analyst.run_full_analysis()
    
    # Save outputs
    print(f"\n💾 Saving outputs to {OUTPUT_DIR}/...")
    save_outputs(results["insights"], results["creatives"], results["report"])
    
    print("\n" + "=" * 60)
    print("Analysis complete! Check the output/ directory for results.")
    print("=" * 60)


if __name__ == "__main__":
    main()

