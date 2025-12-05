"""
Utility functions for the Streamlit Dashboard
Handles data loading, caching, and chart generation
"""

import os
import sys
import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from orchestrator import FraudDetectionOrchestrator

@st.cache_resource
def get_orchestrator():
    """Initialize and cache the orchestrator"""
    return FraudDetectionOrchestrator()

@st.cache_data
def load_data():
    """Load claims and fraud data from database"""
    conn = sqlite3.connect('data/processed/fraud_detection.db')
    query = """
        SELECT 
            c.*,
            f.fraud_detected,
            f.fraud_score,
            f.rules_triggered,
            f.explanation
        FROM claims c
        LEFT JOIN fraud_flags f ON c.claim_id = f.claim_id
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Remove duplicate claim_ids (keep first occurrence)
    df = df.drop_duplicates(subset=['claim_id'], keep='first')
    
    # Convert dates
    df['claim_date'] = pd.to_datetime(df['claim_date'])
    
    return df

def create_fraud_metrics(df):
    """Calculate high-level metrics"""
    total_claims = len(df)
    total_amount = df['claim_amount'].sum()
    
    fraud_df = df[df['fraud_detected'] == 1]
    fraud_claims = len(fraud_df)
    fraud_amount = fraud_df['claim_amount'].sum()
    
    fraud_rate = (fraud_claims / total_claims * 100) if total_claims > 0 else 0
    
    return {
        'total_claims': total_claims,
        'total_amount': total_amount,
        'fraud_claims': fraud_claims,
        'fraud_amount': fraud_amount,
        'fraud_rate': fraud_rate
    }

# Plot fraud vs legitimate claims over time with weekly aggregation
def plot_fraud_trend(df):
    weekly_counts = df.groupby([pd.Grouper(key='claim_date', freq='W'), 'fraud_detected']).size().reset_index(name='count')
    weekly_counts['Type'] = weekly_counts['fraud_detected'].map({0: 'Legitimate', 1: 'Fraud'})
    
    fig = px.line(weekly_counts, x='claim_date', y='count', color='Type',
                  title='Weekly Claim Volume: Fraud vs Legitimate',
                  color_discrete_map={'Legitimate': '#00CC96', 'Fraud': '#EF553B'},
                  markers=True)
    
    fig.update_traces(line=dict(width=3))  # Thicker lines
    fig.update_layout(
        xaxis_title="Week", 
        yaxis_title="Number of Claims",
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig


# Plot breakdown of fraud rules triggered
def plot_fraud_by_rule(df):
    fraud_df = df[df['fraud_detected'] == 1].copy()
    all_rules = []
    for rules in fraud_df['rules_triggered'].dropna():
        all_rules.extend([r.strip() for r in rules.split(',')])
        
    rule_counts = pd.Series(all_rules).value_counts().reset_index()
    rule_counts.columns = ['Rule', 'Count']
    
    fig = px.bar(rule_counts, x='Count', y='Rule', orientation='h',
                 title='Most Common Fraud Rules Triggered',
                 color='Count', color_continuous_scale='Reds')
    
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

# Plot distribution of claim amounts
def plot_amount_distribution(df):
    fig = px.histogram(df, x='claim_amount', color='fraud_detected',
                       title='Claim Amount Distribution',
                       nbins=50, log_y=True,
                       labels={'fraud_detected': 'Is Fraud'},
                       color_discrete_map={0: '#00CC96', 1: '#EF553B'})
    
    return fig
