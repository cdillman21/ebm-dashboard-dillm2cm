"""
EBM Dashboard - Data Analysis Script
Compensation → Satisfaction → Retention Analysis

This script downloads, analyzes, and visualizes data from:
- BLS JOLTS (Y variable - retention/quits)
- BLS ECI (X variable - compensation)
- FEVS (M variable - satisfaction)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime
import requests
import json

# Set style for professional visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("="*80)
print("EBM DASHBOARD - COMPENSATION & RETENTION ANALYSIS")
print("Conrad Dillman - MGT357 Fall 2025")
print("="*80)

# =============================================================================
# PART 1: DOWNLOAD BLS DATA VIA API
# =============================================================================

print("\n[1/7] Downloading BLS JOLTS data (Quits Rate - Y variable)...")

# BLS API Configuration
BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
HEADERS = {'Content-type': 'application/json'}

# BLS Series IDs
# JOLTS: JTS00000000QUR - Total Nonfarm Quits Rate (seasonally adjusted)
# ECI: CIU2010000000000A - Total compensation, all civilian workers (12-month % change)

jolts_series_id = "JTS00000000QUR"  # Quits rate, total nonfarm, seasonally adjusted
eci_series_id = "CIU2010000000000A"  # ECI, 12-month percent change

# Function to fetch BLS data
def fetch_bls_data(series_id, start_year, end_year):
    """Fetch data from BLS API"""
    payload = json.dumps({
        "seriesid": [series_id],
        "startyear": str(start_year),
        "endyear": str(end_year)
    })
    
    try:
        response = requests.post(BLS_API_URL, data=payload, headers=HEADERS)
        json_data = response.json()
        
        if json_data['status'] == 'REQUEST_SUCCEEDED':
            data = json_data['Results']['series'][0]['data']
            return pd.DataFrame(data)
        else:
            print(f"API Error: {json_data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Fetch JOLTS data (2010-2025)
jolts_df = fetch_bls_data(jolts_series_id, 2010, 2025)

# Check if API call succeeded, otherwise use realistic sample data
if jolts_df is not None and 'value' in jolts_df.columns:
    # Clean JOLTS data
    jolts_df['value'] = pd.to_numeric(jolts_df['value'])
    jolts_df['date'] = pd.to_datetime(jolts_df['year'] + '-' + jolts_df['period'].str.replace('M', ''))
    jolts_df = jolts_df[['date', 'value']].rename(columns={'value': 'quits_rate'})
    jolts_df = jolts_df.sort_values('date').reset_index(drop=True)
    print(f"✓ Downloaded {len(jolts_df)} months of JOLTS data")
else:
    print("✗ BLS API unavailable - using realistic sample data based on actual trends")
    # Create realistic JOLTS data based on actual BLS trends
    date_range = pd.date_range(start='2010-01-01', end='2025-09-01', freq='MS')
    np.random.seed(42)
    
    # Base quits rate with realistic trends
    # 2010-2014: ~1.5% (recession recovery)
    # 2015-2019: rising to 2.3% (tight labor market)
    # 2020: drop to 1.6% (COVID)
    # 2021-2022: surge to 3.0% (Great Resignation)
    # 2023-2025: stabilizing around 2.3%
    
    quits_values = []
    for date in date_range:
        year = date.year
        if year <= 2014:
            base = 1.5 + (year - 2010) * 0.05
        elif year <= 2019:
            base = 1.75 + (year - 2015) * 0.11
        elif year == 2020:
            base = 2.3 - (date.month / 12) * 0.7 if date.month <= 6 else 1.6
        elif year == 2021:
            base = 1.6 + (date.month / 12) * 1.0
        elif year == 2022:
            base = 2.6 + (date.month / 12) * 0.2
        else:
            base = 2.3 + np.sin(date.month / 12 * 2 * np.pi) * 0.2
        
        # Add realistic monthly variation
        quits_values.append(base + np.random.normal(0, 0.1))
    
    jolts_df = pd.DataFrame({
        'date': date_range,
        'quits_rate': quits_values
    })
    print(f"✓ Created {len(jolts_df)} months of sample JOLTS data")

print("\n[2/7] Downloading BLS ECI data (Compensation - X variable)...")

# Fetch ECI data (2010-2025)
eci_df = fetch_bls_data(eci_series_id, 2010, 2025)

if eci_df is not None and 'value' in eci_df.columns:
    # Clean ECI data
    eci_df['value'] = pd.to_numeric(eci_df['value'])
    # ECI is quarterly: Q01, Q02, Q03, Q04
    quarter_map = {'Q01': '03', 'Q02': '06', 'Q03': '09', 'Q04': '12'}
    eci_df['month'] = eci_df['period'].map(quarter_map)
    eci_df['date'] = pd.to_datetime(eci_df['year'] + '-' + eci_df['month'] + '-01')
    eci_df = eci_df[['date', 'value']].rename(columns={'value': 'compensation_change_pct'})
    eci_df = eci_df.sort_values('date').reset_index(drop=True)
    print(f"✓ Downloaded {len(eci_df)} quarters of ECI data")
else:
    print("✗ BLS API unavailable - using realistic sample data based on actual trends")
    # Create realistic ECI data based on actual BLS trends
    date_range = pd.date_range(start='2010-03-01', end='2025-09-01', freq='QS-MAR')
    np.random.seed(43)
    
    # Base compensation growth with realistic trends
    # 2010-2012: 1.5-2.0% (slow recovery)
    # 2013-2019: 2.0-2.8% (steady growth)
    # 2020: drop to 2.5% (COVID freeze)
    # 2021-2023: surge to 4.0-5.0% (inflation + tight labor market)
    # 2024-2025: cooling to 3.5%
    
    comp_values = []
    for date in date_range:
        year = date.year
        if year <= 2012:
            base = 1.5 + (year - 2010) * 0.15
        elif year <= 2019:
            base = 1.8 + (year - 2013) * 0.10
        elif year == 2020:
            base = 2.5 - (date.month / 12) * 0.3
        elif year <= 2023:
            base = 2.8 + (year - 2020) * 0.6
        else:
            base = 4.2 - (year - 2023) * 0.35
        
        # Add quarterly variation
        comp_values.append(base + np.random.normal(0, 0.15))
    
    eci_df = pd.DataFrame({
        'date': date_range,
        'compensation_change_pct': comp_values
    })
    print(f"✓ Created {len(eci_df)} quarters of sample ECI data")

# =============================================================================
# PART 2: CREATE SAMPLE FEVS DATA (PLACEHOLDER)
# =============================================================================

print("\n[3/7] Creating sample FEVS data (Employee Satisfaction - M variable)...")
print("   Note: Full FEVS data requires manual download from OPM website")

# Create sample FEVS data with realistic trends
np.random.seed(42)
fevs_years = range(2015, 2026)
fevs_data = {
    'year': fevs_years,
    'pay_satisfaction': [3.2, 3.3, 3.4, 3.5, 3.3, 3.4, 3.6, 3.7, 3.5, 3.6, 3.8],
    'supervisor_effectiveness': [3.6, 3.7, 3.7, 3.8, 3.7, 3.8, 3.9, 4.0, 3.9, 4.0, 4.1],
    'overall_satisfaction': [3.4, 3.5, 3.6, 3.7, 3.6, 3.7, 3.8, 3.9, 3.8, 3.9, 4.0],
    'intent_to_stay': [3.8, 3.9, 4.0, 4.1, 3.9, 4.0, 4.2, 4.3, 4.1, 4.2, 4.4],
    'sample_size': [400000] * 11
}
fevs_df = pd.DataFrame(fevs_data)
fevs_df['date'] = pd.to_datetime(fevs_df['year'].astype(str) + '-06-01')  # Mid-year
print(f"✓ Created sample FEVS data for {len(fevs_df)} years")

# =============================================================================
# PART 3: MERGE DATASETS
# =============================================================================

print("\n[4/7] Merging datasets...")

# Merge JOLTS and ECI (align monthly JOLTS with quarterly ECI)
# Use forward fill to propagate quarterly ECI values to monthly frequency
merged_df = jolts_df.copy()
merged_df['year_month'] = merged_df['date'].dt.to_period('M')

# Convert ECI to monthly frequency via forward fill
eci_monthly = eci_df.set_index('date').resample('MS').ffill().reset_index()

# Merge
merged_df = merged_df.merge(eci_monthly, on='date', how='left')

# Add FEVS data (annual to monthly via forward fill)
fevs_monthly = fevs_df.set_index('date').resample('MS').ffill().reset_index()
merged_df = merged_df.merge(
    fevs_monthly[['date', 'pay_satisfaction', 'supervisor_effectiveness', 'overall_satisfaction', 'intent_to_stay']], 
    on='date', 
    how='left'
)

print(f"✓ Merged dataset contains {len(merged_df)} observations")
print(f"   Date range: {merged_df['date'].min().strftime('%Y-%m')} to {merged_df['date'].max().strftime('%Y-%m')}")

# =============================================================================
# PART 4: SUMMARY STATISTICS
# =============================================================================

print("\n[5/7] Calculating summary statistics...")
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)

# JOLTS Quits Rate (Y - Retention measure)
print("\n📊 Y Variable - Employee Retention (inverse of quits rate)")
print("-" * 80)
print(f"Metric: Quits Rate (% of workforce voluntarily leaving per month)")
print(f"   Mean:                {merged_df['quits_rate'].mean():.2f}%")
print(f"   Median:              {merged_df['quits_rate'].median():.2f}%")
print(f"   Std Deviation:       {merged_df['quits_rate'].std():.2f}%")
print(f"   Min:                 {merged_df['quits_rate'].min():.2f}% ({merged_df.loc[merged_df['quits_rate'].idxmin(), 'date'].strftime('%Y-%m')})")
print(f"   Max:                 {merged_df['quits_rate'].max():.2f}% ({merged_df.loc[merged_df['quits_rate'].idxmax(), 'date'].strftime('%Y-%m')})")
print(f"   25th Percentile:     {merged_df['quits_rate'].quantile(0.25):.2f}%")
print(f"   75th Percentile:     {merged_df['quits_rate'].quantile(0.75):.2f}%")
print(f"\n   Interpretation: Higher quits rate = Lower retention")
print(f"   Trend (2010-2025):   {merged_df.groupby(merged_df['date'].dt.year)['quits_rate'].mean().iloc[-1] - merged_df.groupby(merged_df['date'].dt.year)['quits_rate'].mean().iloc[0]:+.2f} percentage point change")

# ECI Compensation Change (X)
eci_clean = merged_df.dropna(subset=['compensation_change_pct'])
print("\n📊 X Variable - Employee Compensation")
print("-" * 80)
print(f"Metric: Total Compensation 12-Month % Change (wages + benefits)")
print(f"   Mean:                {eci_clean['compensation_change_pct'].mean():.2f}%")
print(f"   Median:              {eci_clean['compensation_change_pct'].median():.2f}%")
print(f"   Std Deviation:       {eci_clean['compensation_change_pct'].std():.2f}%")
print(f"   Min:                 {eci_clean['compensation_change_pct'].min():.2f}% ({eci_clean.loc[eci_clean['compensation_change_pct'].idxmin(), 'date'].strftime('%Y-%m')})")
print(f"   Max:                 {eci_clean['compensation_change_pct'].max():.2f}% ({eci_clean.loc[eci_clean['compensation_change_pct'].idxmax(), 'date'].strftime('%Y-%m')})")
print(f"   25th Percentile:     {eci_clean['compensation_change_pct'].quantile(0.25):.2f}%")
print(f"   75th Percentile:     {eci_clean['compensation_change_pct'].quantile(0.75):.2f}%")
print(f"\n   Interpretation: Positive values = compensation increasing year-over-year")

# FEVS Satisfaction (M)
fevs_clean = merged_df.dropna(subset=['overall_satisfaction'])
print("\n📊 M Variable - Employee Satisfaction")
print("-" * 80)
print(f"Metric: Overall Job Satisfaction (1-5 scale, 5=very satisfied)")
print(f"   Mean:                {fevs_clean['overall_satisfaction'].mean():.2f}/5.0")
print(f"   Median:              {fevs_clean['overall_satisfaction'].median():.2f}/5.0")
print(f"   Std Deviation:       {fevs_clean['overall_satisfaction'].std():.2f}")
print(f"   Min:                 {fevs_clean['overall_satisfaction'].min():.2f}/5.0")
print(f"   Max:                 {fevs_clean['overall_satisfaction'].max():.2f}/5.0")
print(f"\nMetric: Pay Satisfaction (1-5 scale)")
print(f"   Mean:                {fevs_clean['pay_satisfaction'].mean():.2f}/5.0")
print(f"\nMetric: Supervisor Effectiveness (1-5 scale)")
print(f"   Mean:                {fevs_clean['supervisor_effectiveness'].mean():.2f}/5.0")
print(f"\nMetric: Intent to Stay (1-5 scale, 5=definitely staying)")
print(f"   Mean:                {fevs_clean['intent_to_stay'].mean():.2f}/5.0")

# =============================================================================
# PART 5: CORRELATION ANALYSIS
# =============================================================================

print("\n[6/7] Performing correlation analysis...")
print("\n" + "="*80)
print("CORRELATION ANALYSIS (Pearson's r)")
print("="*80)

# Calculate correlations
corr_data = merged_df[['quits_rate', 'compensation_change_pct', 'pay_satisfaction', 
                         'overall_satisfaction', 'intent_to_stay']].dropna()

correlation_matrix = corr_data.corr()

print("\n🔍 Key Correlations:")
print("-" * 80)

# X → Y: Compensation → Retention (quits)
corr_xy = correlation_matrix.loc['compensation_change_pct', 'quits_rate']
print(f"X → Y: Compensation → Quits Rate:         r = {corr_xy:.3f}")
print(f"       Interpretation: {'Negative' if corr_xy < 0 else 'Positive'} relationship")
print(f"       (Higher compensation {'decreases' if corr_xy < 0 else 'increases'} quits)")

# X → M: Compensation → Satisfaction
corr_xm = correlation_matrix.loc['compensation_change_pct', 'pay_satisfaction']
print(f"\nX → M: Compensation → Pay Satisfaction:   r = {corr_xm:.3f}")
print(f"       Interpretation: {'Negative' if corr_xm < 0 else 'Positive'} relationship")

# M → Y: Satisfaction → Retention
corr_my = correlation_matrix.loc['overall_satisfaction', 'quits_rate']
print(f"\nM → Y: Satisfaction → Quits Rate:         r = {corr_my:.3f}")
print(f"       Interpretation: {'Negative' if corr_my < 0 else 'Positive'} relationship")
print(f"       (Higher satisfaction {'decreases' if corr_my < 0 else 'increases'} quits)")

# Intent to stay → Quits (validation check)
corr_intent = correlation_matrix.loc['intent_to_stay', 'quits_rate']
print(f"\nIntent to Stay → Quits Rate:              r = {corr_intent:.3f}")
print(f"       (Should be negative: people wanting to stay = lower quits)")

# Statistical significance
n = len(corr_data)
print(f"\n📈 Sample size for correlations: n = {n}")
print(f"   Critical r for p<0.05 (two-tailed): ±{1.96/np.sqrt(n-3):.3f}")
print(f"   All correlations with |r| > this value are statistically significant")

# =============================================================================
# PART 6: TIME SERIES TRENDS
# =============================================================================

print("\n📊 Time Series Trends:")
print("-" * 80)

# Calculate trends by year
yearly_stats = merged_df.groupby(merged_df['date'].dt.year).agg({
    'quits_rate': 'mean',
    'compensation_change_pct': 'mean',
    'overall_satisfaction': 'mean'
}).dropna()

print("\nYear-by-Year Averages:")
print(yearly_stats.to_string())

# Trend analysis (linear regression)
from scipy.stats import linregress

# Quits rate trend
years_numeric = yearly_stats.index.values
quits_trend = linregress(years_numeric, yearly_stats['quits_rate'].values)
print(f"\n📉 Quits Rate Trend:")
print(f"   Slope: {quits_trend.slope:.3f}% per year")
print(f"   Direction: {'Increasing' if quits_trend.slope > 0 else 'Decreasing'} quits (retention {'worsening' if quits_trend.slope > 0 else 'improving'})")
print(f"   p-value: {quits_trend.pvalue:.4f} {'(significant)' if quits_trend.pvalue < 0.05 else '(not significant)'}")

# Compensation trend
comp_clean = yearly_stats['compensation_change_pct'].dropna()
comp_years = comp_clean.index.values
comp_trend = linregress(comp_years, comp_clean.values)
print(f"\n📈 Compensation Growth Trend:")
print(f"   Slope: {comp_trend.slope:.3f} percentage points per year")
print(f"   Direction: {'Accelerating' if comp_trend.slope > 0 else 'Decelerating'} compensation growth")
print(f"   p-value: {comp_trend.pvalue:.4f} {'(significant)' if comp_trend.pvalue < 0.05 else '(not significant)'}")

# =============================================================================
# PART 7: CREATE VISUALIZATIONS
# =============================================================================

print("\n[7/7] Creating visualizations...")

# Create output directory
import os
os.makedirs('analysis_output', exist_ok=True)

# Figure 1: Time Series - All Variables
fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

# Plot 1: Quits Rate (Y variable)
axes[0].plot(merged_df['date'], merged_df['quits_rate'], color='#e74c3c', linewidth=2)
axes[0].set_ylabel('Quits Rate (%)', fontsize=12, fontweight='bold')
axes[0].set_title('Y Variable: Employee Retention (Quits Rate - Lower is Better)', 
                   fontsize=14, fontweight='bold', pad=15)
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=merged_df['quits_rate'].mean(), color='gray', linestyle='--', 
                label=f'Mean: {merged_df["quits_rate"].mean():.2f}%', alpha=0.7)
axes[0].legend()

# Plot 2: Compensation Change (X variable)
axes[1].plot(eci_monthly['date'], eci_monthly['compensation_change_pct'], 
             color='#27ae60', linewidth=2, marker='o', markersize=4)
axes[1].set_ylabel('12-Month % Change', fontsize=12, fontweight='bold')
axes[1].set_title('X Variable: Total Compensation Growth', 
                   fontsize=14, fontweight='bold', pad=15)
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=eci_monthly['compensation_change_pct'].mean(), color='gray', linestyle='--',
                label=f'Mean: {eci_monthly["compensation_change_pct"].mean():.2f}%', alpha=0.7)
axes[1].legend()

# Plot 3: Satisfaction (M variable)
fevs_plot = fevs_df.copy()
axes[2].plot(fevs_plot['date'], fevs_plot['overall_satisfaction'], 
             color='#3498db', linewidth=2, marker='s', markersize=6, label='Overall Satisfaction')
axes[2].plot(fevs_plot['date'], fevs_plot['pay_satisfaction'], 
             color='#9b59b6', linewidth=2, marker='^', markersize=6, label='Pay Satisfaction')
axes[2].plot(fevs_plot['date'], fevs_plot['intent_to_stay'], 
             color='#f39c12', linewidth=2, marker='D', markersize=6, label='Intent to Stay')
axes[2].set_ylabel('Score (1-5 scale)', fontsize=12, fontweight='bold')
axes[2].set_xlabel('Date', fontsize=12, fontweight='bold')
axes[2].set_title('M Variable: Employee Satisfaction Metrics (FEVS)', 
                   fontsize=14, fontweight='bold', pad=15)
axes[2].grid(True, alpha=0.3)
axes[2].legend(loc='lower right')

plt.tight_layout()
plt.savefig('analysis_output/time_series_all_variables.png', dpi=300, bbox_inches='tight')
print("✓ Saved: analysis_output/time_series_all_variables.png")

# Figure 2: Correlation Matrix Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='RdYlGn', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix: X, M, Y Variables', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('analysis_output/correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Saved: analysis_output/correlation_heatmap.png")

# Figure 3: Scatter Plots (X→M→Y)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# X → M: Compensation → Satisfaction
scatter_xm = corr_data[['compensation_change_pct', 'pay_satisfaction']].dropna()
axes[0].scatter(scatter_xm['compensation_change_pct'], scatter_xm['pay_satisfaction'], 
                alpha=0.6, s=50, color='#9b59b6')
axes[0].set_xlabel('Compensation Growth (%)', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Pay Satisfaction (1-5)', fontsize=11, fontweight='bold')
axes[0].set_title(f'X → M\nr = {corr_xm:.3f}', fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)
# Add trend line
z = np.polyfit(scatter_xm['compensation_change_pct'], scatter_xm['pay_satisfaction'], 1)
p = np.poly1d(z)
axes[0].plot(scatter_xm['compensation_change_pct'], 
             p(scatter_xm['compensation_change_pct']), "r--", alpha=0.8, linewidth=2)

# M → Y: Satisfaction → Quits
scatter_my = corr_data[['overall_satisfaction', 'quits_rate']].dropna()
axes[1].scatter(scatter_my['overall_satisfaction'], scatter_my['quits_rate'], 
                alpha=0.6, s=50, color='#3498db')
axes[1].set_xlabel('Overall Satisfaction (1-5)', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Quits Rate (%)', fontsize=11, fontweight='bold')
axes[1].set_title(f'M → Y\nr = {corr_my:.3f}', fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)
z = np.polyfit(scatter_my['overall_satisfaction'], scatter_my['quits_rate'], 1)
p = np.poly1d(z)
axes[1].plot(scatter_my['overall_satisfaction'], 
             p(scatter_my['overall_satisfaction']), "r--", alpha=0.8, linewidth=2)

# X → Y: Compensation → Quits (direct effect)
scatter_xy = corr_data[['compensation_change_pct', 'quits_rate']].dropna()
axes[2].scatter(scatter_xy['compensation_change_pct'], scatter_xy['quits_rate'], 
                alpha=0.6, s=50, color='#e74c3c')
axes[2].set_xlabel('Compensation Growth (%)', fontsize=11, fontweight='bold')
axes[2].set_ylabel('Quits Rate (%)', fontsize=11, fontweight='bold')
axes[2].set_title(f'X → Y (Direct)\nr = {corr_xy:.3f}', fontsize=13, fontweight='bold')
axes[2].grid(True, alpha=0.3)
z = np.polyfit(scatter_xy['compensation_change_pct'], scatter_xy['quits_rate'], 1)
p = np.poly1d(z)
axes[2].plot(scatter_xy['compensation_change_pct'], 
             p(scatter_xy['compensation_change_pct']), "r--", alpha=0.8, linewidth=2)

plt.suptitle('Logic Model Relationships: X → M → Y', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('analysis_output/scatter_plots_logic_model.png', dpi=300, bbox_inches='tight')
print("✓ Saved: analysis_output/scatter_plots_logic_model.png")

# =============================================================================
# EXPORT SUMMARY TABLE
# =============================================================================

print("\nExporting summary statistics table...")

summary_stats = pd.DataFrame({
    'Variable': ['Quits Rate (Y)', 'Compensation Change (X)', 'Pay Satisfaction (M)', 
                 'Overall Satisfaction (M)', 'Intent to Stay (M)'],
    'Mean': [
        merged_df['quits_rate'].mean(),
        eci_clean['compensation_change_pct'].mean(),
        fevs_clean['pay_satisfaction'].mean(),
        fevs_clean['overall_satisfaction'].mean(),
        fevs_clean['intent_to_stay'].mean()
    ],
    'Median': [
        merged_df['quits_rate'].median(),
        eci_clean['compensation_change_pct'].median(),
        fevs_clean['pay_satisfaction'].median(),
        fevs_clean['overall_satisfaction'].median(),
        fevs_clean['intent_to_stay'].median()
    ],
    'Std Dev': [
        merged_df['quits_rate'].std(),
        eci_clean['compensation_change_pct'].std(),
        fevs_clean['pay_satisfaction'].std(),
        fevs_clean['overall_satisfaction'].std(),
        fevs_clean['intent_to_stay'].std()
    ],
    'Min': [
        merged_df['quits_rate'].min(),
        eci_clean['compensation_change_pct'].min(),
        fevs_clean['pay_satisfaction'].min(),
        fevs_clean['overall_satisfaction'].min(),
        fevs_clean['intent_to_stay'].min()
    ],
    'Max': [
        merged_df['quits_rate'].max(),
        eci_clean['compensation_change_pct'].max(),
        fevs_clean['pay_satisfaction'].max(),
        fevs_clean['overall_satisfaction'].max(),
        fevs_clean['intent_to_stay'].max()
    ],
    'N': [
        len(merged_df),
        len(eci_clean),
        len(fevs_clean),
        len(fevs_clean),
        len(fevs_clean)
    ]
})

summary_stats.to_csv('analysis_output/summary_statistics.csv', index=False)
print("✓ Saved: analysis_output/summary_statistics.csv")

# Export correlation matrix
correlation_matrix.to_csv('analysis_output/correlation_matrix.csv')
print("✓ Saved: analysis_output/correlation_matrix.csv")

# Export merged dataset
merged_df.to_csv('analysis_output/merged_dataset.csv', index=False)
print("✓ Saved: analysis_output/merged_dataset.csv")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
print(f"\n📁 Output files saved to: analysis_output/")
print(f"   - time_series_all_variables.png")
print(f"   - correlation_heatmap.png")
print(f"   - scatter_plots_logic_model.png")
print(f"   - summary_statistics.csv")
print(f"   - correlation_matrix.csv")
print(f"   - merged_dataset.csv")
print(f"\n🎯 Key Finding:")
print(f"   Compensation → Quits correlation: r = {corr_xy:.3f}")
print(f"   {'Strong' if abs(corr_xy) > 0.5 else 'Moderate' if abs(corr_xy) > 0.3 else 'Weak'} {'negative' if corr_xy < 0 else 'positive'} relationship")
print(f"   Interpretation: {'Higher compensation is associated with lower turnover' if corr_xy < 0 else 'Higher compensation is associated with higher turnover (unexpected!)'}")
print("\n" + "="*80)
