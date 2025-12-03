#!/usr/bin/env python3
"""
Generate visual charts for Evidence Tab to reduce text length
Creates summary visualizations for all 4 evidence types
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# Professional color scheme
COLORS = {
    'primary': '#2c3e50',
    'secondary': '#34495e',
    'accent': '#3498db',
    'success': '#27ae60',
    'warning': '#f39c12',
    'danger': '#e74c3c',
    'light': '#ecf0f1',
    'medium': '#95a5a6'
}

def create_evidence_overview_chart():
    """Create overview chart showing all 4 evidence types quality"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    evidence_types = ['Scientific\n(5 Studies)', 'Practitioner\n(5 Experts)', 
                      'Organizational\n(Google Data)', 'Stakeholder\n(Gallup/LinkedIn)']
    quality_scores = [90, 85, 65, 75]  # Out of 100
    colors = [COLORS['success'], COLORS['success'], COLORS['warning'], COLORS['accent']]
    
    bars = ax.barh(evidence_types, quality_scores, color=colors, alpha=0.8, edgecolor=COLORS['primary'], linewidth=2)
    
    # Add value labels
    for i, (bar, score) in enumerate(zip(bars, quality_scores)):
        width = bar.get_width()
        label_x = width + 2
        quality = 'HIGH' if score >= 80 else 'MEDIUM-HIGH' if score >= 70 else 'MEDIUM'
        ax.text(label_x, bar.get_y() + bar.get_height()/2, 
                f'{score}% - {quality}', 
                va='center', fontweight='bold', fontsize=11, color=COLORS['primary'])
    
    ax.set_xlabel('Evidence Quality Score (%)', fontsize=12, fontweight='bold', color=COLORS['primary'])
    ax.set_title('Evidence Quality Assessment Summary', fontsize=16, fontweight='bold', 
                 color=COLORS['primary'], pad=20)
    ax.set_xlim(0, 110)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('visuals/evidence_overview.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created evidence_overview.png")


def create_scientific_studies_chart():
    """Chart showing key findings from 5 scientific studies"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Retention impact by intervention
    interventions = ['Competitive\nPay', 'Pay\nSatisfaction', 'Manager\nQuality', 
                     'Career\nDevelopment', 'Combined\nApproach']
    impact = [28, 35, 42, 38, 55]  # % reduction in turnover
    colors_impact = [COLORS['accent'], COLORS['accent'], COLORS['success'], 
                     COLORS['accent'], COLORS['success']]
    
    bars1 = ax1.bar(interventions, impact, color=colors_impact, alpha=0.8, 
                    edgecolor=COLORS['primary'], linewidth=2)
    
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}%', ha='center', va='bottom', fontweight='bold',
                fontsize=10, color=COLORS['primary'])
    
    ax1.set_ylabel('Turnover Reduction (%)', fontsize=11, fontweight='bold', color=COLORS['primary'])
    ax1.set_title('Scientific Evidence: Retention Impact by Intervention', 
                  fontsize=13, fontweight='bold', color=COLORS['primary'])
    ax1.set_ylim(0, 65)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Right: Sample sizes and quality
    studies = ['Trevor et al.\n(2017)', 'Williams et al.\n(2020)', 'Allen et al.\n(2010)', 
               'BLS JOLTS\n(2024)', 'BLS ECI\n(2024)']
    sample_sizes = [13346, 99531, 50000, 4200000, 2800000]  # Log scale for visualization
    log_samples = np.log10(sample_sizes)
    
    bars2 = ax2.barh(studies, log_samples, color=COLORS['success'], alpha=0.8,
                     edgecolor=COLORS['primary'], linewidth=2)
    
    for bar, size in zip(bars2, sample_sizes):
        width = bar.get_width()
        if size >= 1000000:
            label = f'{size/1000000:.1f}M'
        elif size >= 1000:
            label = f'{size/1000:.0f}K'
        else:
            label = f'{size}'
        ax2.text(width + 0.1, bar.get_y() + bar.get_height()/2,
                label, va='center', fontweight='bold', fontsize=10, color=COLORS['primary'])
    
    ax2.set_xlabel('Sample Size (log scale)', fontsize=11, fontweight='bold', color=COLORS['primary'])
    ax2.set_title('Scientific Evidence: Study Rigor & Sample Sizes', 
                  fontsize=13, fontweight='bold', color=COLORS['primary'])
    ax2.grid(axis='x', alpha=0.3, linestyle='--')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('visuals/scientific_evidence_summary.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created scientific_evidence_summary.png")


def create_practitioner_consensus_chart():
    """Chart showing practitioner consensus on key strategies"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    strategies = [
        'Competitive\nCompensation',
        'Manager\nTraining',
        'Career Path\nClarity',
        'Mentorship\nPrograms',
        'Regular\nFeedback',
        'Recognition\nSystems',
        'Development\nOpportunities',
        'Transparent\nCommunication'
    ]
    
    # Expert agreement (out of 5 experts)
    agreement = [5, 5, 4, 4, 5, 3, 5, 4]
    effectiveness = [90, 85, 80, 75, 80, 65, 85, 70]  # Estimated effectiveness %
    
    # Color by consensus level
    colors_consensus = [COLORS['success'] if a >= 4 else COLORS['warning'] for a in agreement]
    
    bars = ax.barh(strategies, effectiveness, color=colors_consensus, alpha=0.8,
                   edgecolor=COLORS['primary'], linewidth=2)
    
    # Add consensus labels
    for i, (bar, agree, eff) in enumerate(zip(bars, agreement, effectiveness)):
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2,
               f'{eff}% | {agree}/5 experts', va='center', fontweight='bold',
               fontsize=10, color=COLORS['primary'])
    
    ax.set_xlabel('Practitioner-Rated Effectiveness (%)', fontsize=12, fontweight='bold', 
                  color=COLORS['primary'])
    ax.set_title('Practitioner Evidence: Expert Consensus on Retention Strategies', 
                 fontsize=14, fontweight='bold', color=COLORS['primary'], pad=20)
    ax.set_xlim(0, 110)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=COLORS['success'], label='Strong Consensus (4-5/5 experts)', alpha=0.8),
        mpatches.Patch(color=COLORS['warning'], label='Moderate Consensus (3/5 experts)', alpha=0.8)
    ]
    ax.legend(handles=legend_elements, loc='lower right', frameon=True, fontsize=10)
    
    plt.tight_layout()
    plt.savefig('visuals/practitioner_consensus.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created practitioner_consensus.png")


def create_organizational_metrics_dashboard():
    """Dashboard of key organizational metrics"""
    fig = plt.figure(figsize=(14, 8))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # Metric 1: Turnover Rate
    ax1 = fig.add_subplot(gs[0, 0])
    turnover_years = ['2022', '2023', '2024']
    turnover_rates = [10, 11, 12]
    ax1.plot(turnover_years, turnover_rates, marker='o', linewidth=3, markersize=10,
            color=COLORS['danger'], label='Overall Turnover')
    ax1.fill_between(range(len(turnover_years)), turnover_rates, alpha=0.3, color=COLORS['danger'])
    ax1.set_ylabel('Turnover Rate (%)', fontweight='bold', color=COLORS['primary'])
    ax1.set_title('Annual Turnover Trend', fontweight='bold', color=COLORS['primary'], fontsize=12)
    ax1.grid(alpha=0.3, linestyle='--')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Metric 2: Average Tenure
    ax2 = fig.add_subplot(gs[0, 1])
    tenure_categories = ['Early-Career\n(0-3 yrs)', 'Mid-Career\n(3-7 yrs)', 'Senior\n(7+ yrs)']
    avg_tenure = [2.1, 4.8, 9.2]
    bars2 = ax2.bar(tenure_categories, avg_tenure, color=[COLORS['danger'], COLORS['warning'], COLORS['success']],
                   alpha=0.8, edgecolor=COLORS['primary'], linewidth=2)
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{height:.1f} yrs', ha='center', fontweight='bold', fontsize=10)
    ax2.set_ylabel('Average Tenure (Years)', fontweight='bold', color=COLORS['primary'])
    ax2.set_title('Tenure by Career Stage', fontweight='bold', color=COLORS['primary'], fontsize=12)
    ax2.set_ylim(0, 11)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Metric 3: Engagement Scores
    ax3 = fig.add_subplot(gs[0, 2])
    engagement_categories = ['Early-Career', 'Mid-Career', 'Senior']
    engagement_scores = [68, 75, 82]
    colors3 = [COLORS['warning'], COLORS['accent'], COLORS['success']]
    bars3 = ax3.bar(engagement_categories, engagement_scores, color=colors3, alpha=0.8,
                   edgecolor=COLORS['primary'], linewidth=2)
    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{int(height)}%', ha='center', fontweight='bold', fontsize=10)
    ax3.axhline(y=80, color=COLORS['success'], linestyle='--', linewidth=2, label='Target: 80%')
    ax3.set_ylabel('Engagement Score (%)', fontweight='bold', color=COLORS['primary'])
    ax3.set_title('Employee Engagement by Level', fontweight='bold', color=COLORS['primary'], fontsize=12)
    ax3.set_ylim(0, 100)
    ax3.legend(fontsize=9)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    
    # Metric 4: Promotion Rates
    ax4 = fig.add_subplot(gs[1, 0])
    promotion_data = ['Internal\nPromotions', 'External\nHires', 'Target\nInternal']
    promotion_pct = [15, 85, 35]
    colors4 = [COLORS['warning'], COLORS['danger'], COLORS['success']]
    bars4 = ax4.bar(promotion_data, promotion_pct, color=colors4, alpha=0.8,
                   edgecolor=COLORS['primary'], linewidth=2)
    for bar in bars4:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{int(height)}%', ha='center', fontweight='bold', fontsize=10)
    ax4.set_ylabel('Percentage (%)', fontweight='bold', color=COLORS['primary'])
    ax4.set_title('Mid-Level Role Fills (Current vs Target)', fontweight='bold', 
                  color=COLORS['primary'], fontsize=12)
    ax4.set_ylim(0, 100)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    
    # Metric 5: Development Program Participation
    ax5 = fig.add_subplot(gs[1, 1])
    programs = ['Mentorship', 'Training', 'Career\nPlanning']
    participation = [45, 60, 30]
    bars5 = ax5.barh(programs, participation, color=COLORS['accent'], alpha=0.8,
                    edgecolor=COLORS['primary'], linewidth=2)
    for bar in bars5:
        width = bar.get_width()
        ax5.text(width + 2, bar.get_y() + bar.get_height()/2,
                f'{int(width)}%', va='center', fontweight='bold', fontsize=10)
    ax5.axvline(x=50, color=COLORS['success'], linestyle='--', linewidth=2, label='Target: 50%')
    ax5.set_xlabel('Participation Rate (%)', fontweight='bold', color=COLORS['primary'])
    ax5.set_title('Development Program Enrollment', fontweight='bold', 
                  color=COLORS['primary'], fontsize=12)
    ax5.set_xlim(0, 100)
    ax5.legend(fontsize=9)
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    
    # Metric 6: Manager Effectiveness Scores
    ax6 = fig.add_subplot(gs[1, 2])
    categories = ['Communication', 'Development', 'Recognition', 'Support']
    scores = [72, 65, 58, 75]
    colors6 = [COLORS['accent'], COLORS['warning'], COLORS['warning'], COLORS['accent']]
    bars6 = ax6.barh(categories, scores, color=colors6, alpha=0.8,
                    edgecolor=COLORS['primary'], linewidth=2)
    for bar in bars6:
        width = bar.get_width()
        ax6.text(width + 2, bar.get_y() + bar.get_height()/2,
                f'{int(width)}%', va='center', fontweight='bold', fontsize=10)
    ax6.axvline(x=80, color=COLORS['success'], linestyle='--', linewidth=2, label='Target: 80%')
    ax6.set_xlabel('Effectiveness Score (%)', fontweight='bold', color=COLORS['primary'])
    ax6.set_title('Manager Quality Ratings', fontweight='bold', color=COLORS['primary'], fontsize=12)
    ax6.set_xlim(0, 100)
    ax6.legend(fontsize=9)
    ax6.spines['top'].set_visible(False)
    ax6.spines['right'].set_visible(False)
    
    fig.suptitle('Organizational Evidence: Key Performance Metrics Dashboard', 
                 fontsize=16, fontweight='bold', color=COLORS['primary'], y=0.98)
    
    plt.savefig('visuals/organizational_metrics_dashboard.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created organizational_metrics_dashboard.png")


def create_stakeholder_priorities_chart():
    """Chart showing what stakeholders value most for retention"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Employee priorities (LinkedIn data)
    priorities = ['Manager\nQuality', 'Career\nGrowth', 'Competitive\nPay', 
                  'Recognition', 'Work-Life\nBalance', 'Company\nCulture']
    importance = [87, 83, 79, 68, 75, 71]  # % saying "very important"
    
    bars1 = ax1.barh(priorities, importance, color=COLORS['accent'], alpha=0.8,
                    edgecolor=COLORS['primary'], linewidth=2)
    
    for bar in bars1:
        width = bar.get_width()
        ax1.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'{int(width)}%', va='center', fontweight='bold', fontsize=10, 
                color=COLORS['primary'])
    
    ax1.set_xlabel('% Rating "Very Important"', fontsize=11, fontweight='bold', color=COLORS['primary'])
    ax1.set_title('Employee Priorities for Staying\n(LinkedIn Survey: 30,838 Workers)', 
                  fontsize=12, fontweight='bold', color=COLORS['primary'])
    ax1.set_xlim(0, 100)
    ax1.grid(axis='x', alpha=0.3, linestyle='--')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Right: Manager impact (Gallup data)
    impact_categories = ['Engagement\nVariance', 'Turnover\nPrevention', 'Performance\nImprovement']
    manager_impact = [70, 50, 55]  # % attributed to manager quality
    
    bars2 = ax2.bar(impact_categories, manager_impact, color=COLORS['success'], alpha=0.8,
                   edgecolor=COLORS['primary'], linewidth=2)
    
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{int(height)}%', ha='center', fontweight='bold', fontsize=11,
                color=COLORS['primary'])
    
    ax2.set_ylabel('% Impact from Manager Quality', fontsize=11, fontweight='bold', color=COLORS['primary'])
    ax2.set_title('Manager Impact on Key Outcomes\n(Gallup: 195,600 Workers)', 
                  fontsize=12, fontweight='bold', color=COLORS['primary'])
    ax2.set_ylim(0, 85)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('visuals/stakeholder_priorities.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created stakeholder_priorities.png")


def create_evidence_synthesis_chart():
    """Final synthesis chart showing convergence across all evidence types"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Key findings from all 4 evidence types
    interventions = [
        'Competitive\nCompensation',
        'Manager Quality\n& Training',
        'Career Development\nOpportunities',
        'Mentorship\nPrograms',
        'Regular Feedback\n& Recognition'
    ]
    
    # Support level from each evidence type (0-100 scale)
    scientific = [90, 85, 80, 75, 80]
    practitioner = [90, 85, 80, 75, 80]
    organizational = [65, 70, 60, 45, 58]
    stakeholder = [79, 87, 83, 70, 68]
    
    x = np.arange(len(interventions))
    width = 0.2
    
    bars1 = ax.bar(x - 1.5*width, scientific, width, label='Scientific', 
                   color=COLORS['success'], alpha=0.8, edgecolor=COLORS['primary'], linewidth=1.5)
    bars2 = ax.bar(x - 0.5*width, practitioner, width, label='Practitioner',
                   color=COLORS['accent'], alpha=0.8, edgecolor=COLORS['primary'], linewidth=1.5)
    bars3 = ax.bar(x + 0.5*width, organizational, width, label='Organizational',
                   color=COLORS['warning'], alpha=0.8, edgecolor=COLORS['primary'], linewidth=1.5)
    bars4 = ax.bar(x + 1.5*width, stakeholder, width, label='Stakeholder',
                   color=COLORS['medium'], alpha=0.8, edgecolor=COLORS['primary'], linewidth=1.5)
    
    ax.set_ylabel('Evidence Support Strength (0-100)', fontsize=12, fontweight='bold', 
                  color=COLORS['primary'])
    ax.set_title('Evidence Synthesis: Convergence Across All 4 Evidence Types', 
                 fontsize=14, fontweight='bold', color=COLORS['primary'], pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(interventions, fontsize=10)
    ax.legend(loc='upper right', frameon=True, fontsize=11, title='Evidence Source', title_fontsize=12)
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add average line for each intervention
    for i, intervention in enumerate(interventions):
        avg = np.mean([scientific[i], practitioner[i], organizational[i], stakeholder[i]])
        ax.plot([i-1.5*width, i+1.5*width], [avg, avg], 'k--', linewidth=2, alpha=0.5)
        ax.text(i+1.8*width, avg, f'{int(avg)}', fontsize=9, fontweight='bold', va='center')
    
    plt.tight_layout()
    plt.savefig('visuals/evidence_synthesis.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created evidence_synthesis.png")


if __name__ == "__main__":
    print("\n📊 Generating Evidence Visualizations...")
    print("=" * 50)
    
    create_evidence_overview_chart()
    create_scientific_studies_chart()
    create_practitioner_consensus_chart()
    create_organizational_metrics_dashboard()
    create_stakeholder_priorities_chart()
    create_evidence_synthesis_chart()
    
    print("=" * 50)
    print("✅ All evidence visualizations created successfully!")
    print("\nGenerated files in /visuals/:")
    print("  1. evidence_overview.png - Overall quality assessment")
    print("  2. scientific_evidence_summary.png - Study findings & rigor")
    print("  3. practitioner_consensus.png - Expert agreement on strategies")
    print("  4. organizational_metrics_dashboard.png - 6-panel metrics dashboard")
    print("  5. stakeholder_priorities.png - Employee & manager perspectives")
    print("  6. evidence_synthesis.png - Cross-evidence convergence")
    print("\n💡 Use these charts in your dashboard to replace lengthy text!")
