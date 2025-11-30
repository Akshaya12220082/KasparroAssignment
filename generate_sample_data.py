"""Generate sample synthetic Facebook ads data for testing."""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_sample_data(n_campaigns: int = 50, output_path: str = "synthetic_fb_ads_undergarments.csv"):
    """Generate synthetic Facebook ads data.
    
    Args:
        n_campaigns: Number of campaigns to generate
        output_path: Path to save the CSV file
    """
    np.random.seed(42)
    random.seed(42)
    
    # Campaign types
    campaign_types = ["Awareness", "Conversion", "Engagement", "Retargeting", "Lookalike"]
    
    # Ad formats
    ad_formats = ["Single Image", "Carousel", "Video", "Collection", "Stories"]
    
    # CTAs
    ctas = ["Shop Now", "Learn More", "Sign Up", "Download", "Get Started"]
    
    # Age groups
    age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
    
    # Genders
    genders = ["All", "Male", "Female"]
    
    # Product categories
    categories = ["Bras", "Panties", "Shapewear", "Lingerie Sets", "Sleepwear"]
    
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(n_campaigns):
        campaign_id = f"CAMP_{i+1:04d}"
        campaign_type = random.choice(campaign_types)
        ad_format = random.choice(ad_formats)
        category = random.choice(categories)
        age_group = random.choice(age_groups)
        gender = random.choice(genders)
        
        # Generate realistic performance metrics
        impressions = np.random.randint(10000, 500000)
        reach = int(impressions * np.random.uniform(0.6, 0.9))
        clicks = int(impressions * np.random.uniform(0.01, 0.05))
        conversions = int(clicks * np.random.uniform(0.02, 0.15))
        spend = np.random.uniform(50, 5000)
        
        # Calculate derived metrics
        ctr = (clicks / impressions * 100) if impressions > 0 else 0
        cpc = (spend / clicks) if clicks > 0 else 0
        cpm = (spend / impressions * 1000) if impressions > 0 else 0
        conversion_rate = (conversions / clicks * 100) if clicks > 0 else 0
        cpa = (spend / conversions) if conversions > 0 else 0
        roas = np.random.uniform(1.5, 8.0)  # Return on ad spend
        
        # Date range
        days_ago = np.random.randint(0, 90)
        start = start_date + timedelta(days=days_ago)
        end = start + timedelta(days=np.random.randint(7, 30))
        
        data.append({
            "campaign_id": campaign_id,
            "campaign_name": f"{category} {campaign_type} Campaign",
            "campaign_type": campaign_type,
            "ad_format": ad_format,
            "product_category": category,
            "target_age_group": age_group,
            "target_gender": gender,
            "start_date": start.strftime("%Y-%m-%d"),
            "end_date": end.strftime("%Y-%m-%d"),
            "impressions": impressions,
            "reach": reach,
            "clicks": clicks,
            "conversions": conversions,
            "spend_usd": round(spend, 2),
            "ctr_percent": round(ctr, 2),
            "cpc_usd": round(cpc, 2),
            "cpm_usd": round(cpm, 2),
            "conversion_rate_percent": round(conversion_rate, 2),
            "cpa_usd": round(cpa, 2),
            "roas": round(roas, 2),
            "engagement_rate": round(np.random.uniform(1.0, 5.0), 2),
            "video_views": clicks if ad_format == "Video" else 0,
            "video_completion_rate": round(np.random.uniform(20, 80), 2) if ad_format == "Video" else 0
        })
    
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"✓ Generated {n_campaigns} synthetic campaigns and saved to {output_path}")
    print(f"  Columns: {', '.join(df.columns)}")
    return df


if __name__ == "__main__":
    generate_sample_data(n_campaigns=50)

