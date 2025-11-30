"""Main agentic system for Facebook ads analysis."""
import json
from typing import Dict, Any, List
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from config import (
    OPENAI_API_KEY, 
    OPENAI_MODEL,
    LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY,
    LANGFUSE_HOST
)
from data_loader import DataLoader

# Optional Langfuse import
try:
    from langfuse.decorators import observe
    LANGFUSE_AVAILABLE = True
except ImportError:
    LANGFUSE_AVAILABLE = False
    # Create a no-op decorator if Langfuse is not available
    def observe(*args, **kwargs):
        def decorator(func):
            return func
        return decorator


class AgenticFBAnalyst:
    """Agentic system for analyzing Facebook ads and generating insights."""
    
    def __init__(self, data_path: str):
        """Initialize the agentic analyst.
        
        Args:
            data_path: Path to the CSV file containing FB ads data
        """
        self.data_loader = DataLoader(data_path)
        self.llm = ChatOpenAI(
            model=OPENAI_MODEL,
            temperature=0.7,
            api_key=OPENAI_API_KEY
        )
        
        # Initialize Langfuse if credentials are provided
        if LANGFUSE_AVAILABLE and LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY:
            try:
                from langfuse import Langfuse
                self.langfuse = Langfuse(
                    public_key=LANGFUSE_PUBLIC_KEY,
                    secret_key=LANGFUSE_SECRET_KEY,
                    host=LANGFUSE_HOST
                )
                print("✓ Langfuse tracing enabled")
            except Exception as e:
                print(f"⚠ Langfuse initialization failed: {e}")
                self.langfuse = None
        else:
            self.langfuse = None
            if not LANGFUSE_AVAILABLE:
                print("ℹ Langfuse not installed - tracing disabled (install with: pip install langfuse)")
            else:
                print("ℹ Langfuse credentials not provided - tracing disabled")
    
    @observe()
    def analyze_insights(self, data_summary: str) -> Dict[str, Any]:
        """Generate insights from the Facebook ads data.
        
        Args:
            data_summary: Formatted string containing data summary
            
        Returns:
            Dictionary containing insights
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert Facebook ads analyst. Your task is to analyze Facebook ads performance data and generate actionable insights.

Analyze the provided data and generate insights in the following JSON format:
{{
    "key_insights": [
        {{
            "insight": "Description of the insight",
            "metric": "Relevant metric name",
            "value": "Metric value",
            "impact": "high|medium|low",
            "recommendation": "Actionable recommendation"
        }}
    ],
    "performance_summary": {{
        "top_performers": ["List of top performing campaigns/ads"],
        "underperformers": ["List of underperforming campaigns/ads"],
        "trends": ["Key trends observed"]
    }},
    "opportunities": [
        {{
            "opportunity": "Description of opportunity",
            "potential_impact": "Expected impact",
            "action_items": ["List of action items"]
        }}
    ]
}}"""),
            ("human", f"""Please analyze the following Facebook ads data and generate comprehensive insights:

{data_summary}

Provide your analysis in valid JSON format only, no additional text.""")
        ])
        
        messages = prompt.format_messages()
        response = self.llm.invoke(messages)
        
        # Parse JSON response
        try:
            insights = json.loads(response.content)
        except json.JSONDecodeError:
            # Try to extract JSON from response if wrapped in markdown
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            insights = json.loads(content.strip())
        
        return insights
    
    @observe()
    def generate_creatives(self, data_summary: str, insights: Dict[str, Any]) -> Dict[str, Any]:
        """Generate creative recommendations based on insights.
        
        Args:
            data_summary: Formatted string containing data summary
            insights: Generated insights dictionary
            
        Returns:
            Dictionary containing creative recommendations
        """
        insights_str = json.dumps(insights, indent=2)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a creative strategist specializing in Facebook ads. Based on performance data and insights, generate creative recommendations.

Generate creative recommendations in the following JSON format:
{{
    "creative_recommendations": [
        {{
            "campaign_type": "Type of campaign (e.g., Awareness, Conversion, Engagement)",
            "ad_format": "Recommended ad format (e.g., Carousel, Single Image, Video)",
            "headline": "Suggested headline",
            "primary_text": "Suggested primary text/copy",
            "call_to_action": "Recommended CTA",
            "visual_elements": ["List of visual elements to include"],
            "targeting_suggestions": ["Targeting recommendations"],
            "rationale": "Why this creative approach is recommended"
        }}
    ],
    "a_b_test_suggestions": [
        {{
            "test_name": "Name of the A/B test",
            "hypothesis": "What you're testing",
            "variants": [
                {{
                    "variant_name": "Variant A",
                    "description": "Description of variant"
                }}
            ],
            "success_metrics": ["Metrics to measure success"]
        }}
    ],
    "creative_best_practices": [
        "List of best practices based on the data analysis"
    ]
}}"""),
            ("human", f"""Based on the following Facebook ads data and insights, generate creative recommendations:

Data Summary:
{data_summary}

Generated Insights:
{insights_str}

Provide your creative recommendations in valid JSON format only, no additional text.""")
        ])
        
        messages = prompt.format_messages()
        response = self.llm.invoke(messages)
        
        # Parse JSON response
        try:
            creatives = json.loads(response.content)
        except json.JSONDecodeError:
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            creatives = json.loads(content.strip())
        
        return creatives
    
    @observe()
    def generate_report(self, data_summary: str, insights: Dict[str, Any], creatives: Dict[str, Any]) -> str:
        """Generate a comprehensive markdown report.
        
        Args:
            data_summary: Formatted string containing data summary
            insights: Generated insights dictionary
            creatives: Generated creatives dictionary
            
        Returns:
            Markdown formatted report
        """
        insights_str = json.dumps(insights, indent=2)
        creatives_str = json.dumps(creatives, indent=2)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a senior Facebook ads analyst preparing an executive report. Create a comprehensive, well-structured markdown report that summarizes the analysis, insights, and recommendations.

The report should include:
1. Executive Summary
2. Data Overview
3. Key Insights
4. Performance Analysis
5. Creative Recommendations
6. Action Items and Next Steps

Format the report in clean, professional markdown with proper headings, bullet points, and sections."""),
            ("human", f"""Create a comprehensive markdown report based on:

Data Summary:
{data_summary}

Insights:
{insights_str}

Creative Recommendations:
{creatives_str}

Generate a professional markdown report.""")
        ])
        
        messages = prompt.format_messages()
        response = self.llm.invoke(messages)
        
        return response.content
    
    def run_full_analysis(self) -> Dict[str, Any]:
        """Run the complete analysis pipeline.
        
        Returns:
            Dictionary containing all generated outputs
        """
        print("🚀 Starting agentic FB ads analysis...")
        
        # Load and prepare data
        print("\n📊 Loading data...")
        self.data_loader.load_data()
        data_summary = self.data_loader.get_data_for_analysis()
        
        # Generate insights
        print("\n💡 Generating insights...")
        insights = self.analyze_insights(data_summary)
        
        # Generate creatives
        print("\n🎨 Generating creative recommendations...")
        creatives = self.generate_creatives(data_summary, insights)
        
        # Generate report
        print("\n📝 Generating comprehensive report...")
        report = self.generate_report(data_summary, insights, creatives)
        
        print("\n✅ Analysis complete!")
        
        return {
            "insights": insights,
            "creatives": creatives,
            "report": report
        }

