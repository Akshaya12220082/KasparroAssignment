"""Data loading and preprocessing module."""
import pandas as pd
import json
from typing import Dict, List, Any
from pathlib import Path


class DataLoader:
    """Load and preprocess Facebook ads data."""
    
    def __init__(self, data_path: str):
        """Initialize data loader.
        
        Args:
            data_path: Path to the CSV file containing FB ads data
        """
        self.data_path = data_path
        self.df = None
        
    def load_data(self) -> pd.DataFrame:
        """Load data from CSV file.
        
        Returns:
            DataFrame containing the ads data
        """
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"✓ Loaded {len(self.df)} rows from {self.data_path}")
            return self.df
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Get summary statistics of the dataset.
        
        Returns:
            Dictionary containing summary statistics
        """
        if self.df is None:
            self.load_data()
        
        summary = {
            "total_campaigns": len(self.df),
            "columns": list(self.df.columns),
            "numeric_summary": self.df.describe().to_dict() if len(self.df.select_dtypes(include=['number']).columns) > 0 else {},
            "missing_values": self.df.isnull().sum().to_dict(),
            "data_types": self.df.dtypes.astype(str).to_dict()
        }
        
        return summary
    
    def get_data_preview(self, n_rows: int = 5) -> List[Dict[str, Any]]:
        """Get a preview of the data.
        
        Args:
            n_rows: Number of rows to preview
            
        Returns:
            List of dictionaries representing rows
        """
        if self.df is None:
            self.load_data()
        
        return self.df.head(n_rows).to_dict('records')
    
    def get_data_for_analysis(self) -> str:
        """Get formatted data string for LLM analysis.
        
        Returns:
            Formatted string representation of the data
        """
        if self.df is None:
            self.load_data()
        
        # Convert DataFrame to a readable format
        summary = self.get_summary_stats()
        preview = self.get_data_preview(10)
        
        data_str = f"""
Dataset Summary:
- Total campaigns/ads: {summary['total_campaigns']}
- Columns: {', '.join(summary['columns'])}
- Missing values: {summary['missing_values']}

Sample Data (first 10 rows):
{json.dumps(preview, indent=2)}

Full Dataset Statistics:
{json.dumps(summary['numeric_summary'], indent=2)}
"""
        return data_str

