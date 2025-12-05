#!/usr/bin/env python3
"""
Generate Milestone 3 Visualizations for EBM Dashboard
Creates professional charts for AGGREGATE, APPLY, and ASSESS phases
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Professional color scheme (matching dashboard)
PRIMARY_COLOR = '#2c3e50'
ACCENT_COLOR = '#3498db'
SUCCESS_COLOR = '#27ae60'
WARNING_COLOR = '#f39c12'
DANGER_COLOR = '#e74c3c'
LIGHT_BG = '#ecf0f1'

def create_bayesian_journey_chart():
    """Chart 1: Bayesian Confidence Journey (30% → 85%)"""
    
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='white')
    
    # Data points
    stages = ['Initial\nBelief', 'After\nScientific', 'After\nPractitioner', 'After\nOrganizational', 'After\nStakeholder']
    confidence = [30, 55, 72, 77, 85]
    boosts = [0, 25, 17, 5, 8]
    
    # Create stepped line chart
    x_positions = range(len(stages))
    
    # Plot confidence line
    ax.plot(x_positions, confidence, marker='o', linewidth=3, markersize=12, 
            color=ACCENT_COLOR, label='Confidence Level')
    
    # Add confidence boost annotations
    for i in range(1, len(stages)):
        # Arrow showing boost
        ax.annotate('', xy=(x_positions[i], confidence[i]), 
                   xytext=(x_positions[i-1], confidence[i-1]),
                   arrowprops=dict(arrowstyle='->', lw=2, color=SUCCESS_COLOR, alpha=0.6))
        
        # Boost amount text
        mid_y = (confidence[i] + confidence[i-1]) / 2
        ax.text(x_positions[i] - 0.5, mid_y + 3, f'+{boosts[i]}%', 
               fontsize=11, fontweight='bold', color=SUCCESS_COLOR,
               ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Highlight final confidence
    ax.scatter([x_positions[-1]], [confidence[-1]], s=400, c=SUCCESS_COLOR, 
              alpha=0.3, zorder=2)
    ax.text(x_positions[-1], confidence[-1] + 5, '85% FINAL', 
           fontsize=13, fontweight='bold', ha='center', color=SUCCESS_COLOR)
    
    # Add reference zones
    ax.axhspan(0, 40, alpha=0.1, color=DANGER_COLOR, label='Low Confidence')
    ax.axhspan(40, 70, alpha=0.1, color=WARNING_COLOR, label='Moderate Confidence')
    ax.axhspan(70, 100, alpha=0.1, color=SUCCESS_COLOR, label='High Confidence')
    
    # Formatting
    ax.set_xticks(x_positions)
    ax.set_xticklabels(stages, fontsize=11)
    ax.set_ylabel('Confidence Level (%)', fontsize=13, fontweight='bold')
    ax.set_title('Bayesian Reasoning: Evidence-Based Confidence Journey', 
                fontsize=15, fontweight='bold', pad=20, color=PRIMARY_COLOR)
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    
    # Add total gain annotation
    ax.text(2, 15, f'Total Gain: +55 percentage points', 
           fontsize=12, fontweight='bold', ha='center',
           bbox=dict(boxstyle='round,pad=0.5', facecolor=ACCENT_COLOR, 
                    edgecolor='none', alpha=0.2))
    
    plt.tight_layout()
    plt.savefig('visuals/bayesian_confidence_journey.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created bayesian_confidence_journey.png")
    plt.close()


def create_logic_model_diagram():
    """Chart 2: Logic Model X → M → Y Diagram"""
    
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.3, 'Logic Model: How Retention Acceleration Program Works', 
           fontsize=16, fontweight='bold', ha='center', color=PRIMARY_COLOR)
    
    # X - Independent Variable (Intervention)
    x_box = FancyBboxPatch((0.3, 6), 2.5, 2, boxstyle="round,pad=0.1", 
                           facecolor=ACCENT_COLOR, edgecolor=PRIMARY_COLOR, linewidth=2, alpha=0.8)
    ax.add_patch(x_box)
    ax.text(1.55, 7.6, 'X: INTERVENTION', fontsize=12, fontweight='bold', 
           ha='center', color='white')
    ax.text(1.55, 7.2, 'Manager Training', fontsize=10, ha='center', color='white')
    ax.text(1.55, 6.85, '(Coaching, Feedback,', fontsize=9, ha='center', color='white')
    ax.text(1.55, 6.5, 'Career Development)', fontsize=9, ha='center', color='white')
    ax.text(1.55, 6.1, '+', fontsize=11, ha='center', color='white', fontweight='bold')
    ax.text(1.55, 5.75, 'Competitive Comp', fontsize=10, ha='center', color='white')
    ax.text(1.55, 5.4, '(90th percentile)', fontsize=9, ha='center', color='white', style='italic')
    
    # Arrow X → M
    arrow1 = FancyArrowPatch((2.9, 7), (3.8, 7), arrowstyle='->', mutation_scale=30, 
                            linewidth=3, color=PRIMARY_COLOR)
    ax.add_patch(arrow1)
    ax.text(3.35, 7.3, 'Causes', fontsize=9, ha='center', style='italic', color=PRIMARY_COLOR)
    
    # M - Mediators (Mechanisms)
    m_box = FancyBboxPatch((3.8, 5.5), 2.8, 3, boxstyle="round,pad=0.1", 
                           facecolor=WARNING_COLOR, edgecolor=PRIMARY_COLOR, linewidth=2, alpha=0.8)
    ax.add_patch(m_box)
    ax.text(5.2, 8.1, 'M: MEDIATORS', fontsize=12, fontweight='bold', 
           ha='center', color='white')
    ax.text(5.2, 7.75, '(How It Works)', fontsize=9, ha='center', color='white', style='italic')
    
    # Three mediators
    ax.text(5.2, 7.3, 'M1: Job Satisfaction ↑', fontsize=10, ha='center', color='white')
    ax.text(5.2, 6.95, '(Fair pay removes anxiety)', fontsize=8, ha='center', color='white', alpha=0.9)
    
    ax.text(5.2, 6.5, 'M2: Manager Quality ↑', fontsize=10, ha='center', color='white')
    ax.text(5.2, 6.15, '(Better coaching & feedback)', fontsize=8, ha='center', color='white', alpha=0.9)
    
    ax.text(5.2, 5.7, 'M3: Career Growth ↑', fontsize=10, ha='center', color='white')
    ax.text(5.2, 5.35, '(Visible development path)', fontsize=8, ha='center', color='white', alpha=0.9)
    
    # Arrow M → Y
    arrow2 = FancyArrowPatch((6.7, 7), (7.6, 7), arrowstyle='->', mutation_scale=30, 
                            linewidth=3, color=PRIMARY_COLOR)
    ax.add_patch(arrow2)
    ax.text(7.15, 7.3, 'Leads to', fontsize=9, ha='center', style='italic', color=PRIMARY_COLOR)
    
    # Y - Dependent Variable (Outcome)
    y_box = FancyBboxPatch((7.6, 6), 2.2, 2, boxstyle="round,pad=0.1", 
                           facecolor=SUCCESS_COLOR, edgecolor=PRIMARY_COLOR, linewidth=2, alpha=0.8)
    ax.add_patch(y_box)
    ax.text(8.7, 7.6, 'Y: OUTCOME', fontsize=12, fontweight='bold', 
           ha='center', color='white')
    ax.text(8.7, 7.15, 'Retention Rate', fontsize=11, ha='center', color='white')
    ax.text(8.7, 6.7, '60% → 75%+', fontsize=13, ha='center', color='white', fontweight='bold')
    ax.text(8.7, 6.25, 'Over 24 Months', fontsize=9, ha='center', color='white', style='italic')
    
    # Assumptions box at bottom
    assumptions_box = FancyBboxPatch((0.5, 0.5), 9, 3.5, boxstyle="round,pad=0.15", 
                                     facecolor=LIGHT_BG, edgecolor=PRIMARY_COLOR, 
                                     linewidth=1.5, linestyle='--', alpha=0.6)
    ax.add_patch(assumptions_box)
    
    ax.text(5, 3.7, 'KEY ASSUMPTIONS:', fontsize=11, fontweight='bold', 
           ha='center', color=PRIMARY_COLOR)
    
    assumptions = [
        '• Manager quality is trainable (managers can learn and apply skills)',
        '• Manager quality drives retention (causal relationship, not just correlation)',
        '• Compensation is necessary foundation (can\'t train way out of pay problem)',
        '• Combined approach is synergistic (manager training + comp > sum of parts)',
        '• Results generalize to our context (pilot tests this assumption)'
    ]
    
    y_pos = 3.2
    for assumption in assumptions:
        ax.text(5, y_pos, assumption, fontsize=9, ha='center', color=PRIMARY_COLOR)
        y_pos -= 0.45
    
    # Moderators note
    ax.text(5, 0.8, 'MODERATORS: Manager willingness, organizational culture, labor market conditions, economic factors', 
           fontsize=8, ha='center', color=PRIMARY_COLOR, style='italic', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('visuals/logic_model_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created logic_model_diagram.png")
    plt.close()


def create_implementation_timeline():
    """Chart 3: 5-Phase Implementation Timeline (Gantt-style)"""
    
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='white')
    
    # Phases with durations
    phases = [
        ('Phase 1: Preparation', 0, 1, ACCENT_COLOR),
        ('Phase 2: Pilot', 1, 4, WARNING_COLOR),
        ('Phase 3: Evaluation & Scale Decision', 4, 5, '#9b59b6'),
        ('Phase 4: Full Rollout', 5, 18, SUCCESS_COLOR),
        ('Phase 5: Sustainability', 18, 24, '#34495e')
    ]
    
    # Key milestones
    milestones = [
        (1, 'Budget Approved'),
        (2, 'Training Launched'),
        (3, 'Compensation Adjusted'),
        (4, 'Pilot Complete'),
        (5, 'Scale Decision'),
        (9, 'All Managers Trained'),
        (12, '12-Month Evaluation'),
        (18, 'Full Impact Expected'),
        (24, 'Program Self-Sustaining')
    ]
    
    # Draw phase bars
    for i, (phase_name, start, end, color) in enumerate(phases):
        ax.barh(i, end - start, left=start, height=0.6, 
               color=color, alpha=0.8, edgecolor=PRIMARY_COLOR, linewidth=1.5)
        
        # Phase label
        duration = end - start
        mid_point = start + duration / 2
        ax.text(mid_point, i, f'{phase_name}\n({duration} months)', 
               ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Add milestone markers
    milestone_y = len(phases) + 0.5
    for month, label in milestones:
        ax.plot([month, month], [-0.5, len(phases) - 0.5], 
               'k--', alpha=0.3, linewidth=1)
        ax.scatter(month, milestone_y, s=150, c=DANGER_COLOR, 
                  marker='v', zorder=5, edgecolors='white', linewidth=2)
        ax.text(month, milestone_y + 0.3, label, 
               rotation=45, ha='left', va='bottom', fontsize=8, color=PRIMARY_COLOR)
    
    # Formatting
    ax.set_yticks(range(len(phases)))
    ax.set_yticklabels(['' for _ in phases])
    ax.set_xlabel('Timeline (Months)', fontsize=13, fontweight='bold')
    ax.set_title('Retention Acceleration Program: 24-Month Implementation Timeline', 
                fontsize=15, fontweight='bold', pad=20, color=PRIMARY_COLOR)
    ax.set_xlim(0, 25)
    ax.set_ylim(-0.8, len(phases) + 1.5)
    ax.grid(True, axis='x', alpha=0.3, linestyle=':')
    
    # Add decision points
    decision_points = [(5, 'DECISION:\nScale or Stop?'), (12, 'DECISION:\nContinue\nor Adjust?'), (18, 'DECISION:\nSustain?')]
    for month, decision in decision_points:
        ax.text(month, -1.2, decision, ha='center', va='top', fontsize=9, 
               color=DANGER_COLOR, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                        edgecolor=DANGER_COLOR, linewidth=2))
    
    # Add cost markers
    cost_notes = [
        (2.5, len(phases) + 1.2, 'Pilot: $155K'),
        (11.5, len(phases) + 1.2, 'Year 1 Total: $610K'),
        (21, len(phases) + 1.2, 'Ongoing: $160K/yr')
    ]
    for x, y, text in cost_notes:
        ax.text(x, y, text, ha='center', va='center', fontsize=9, 
               bbox=dict(boxstyle='round,pad=0.4', facecolor=ACCENT_COLOR, 
                        alpha=0.2, edgecolor=ACCENT_COLOR, linewidth=1.5))
    
    plt.tight_layout()
    plt.savefig('visuals/implementation_timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created implementation_timeline.png")
    plt.close()


def create_roi_projection():
    """Chart 4: 3-Year ROI Projection"""
    
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='white')
    
    years = ['Year 1', 'Year 2', 'Year 3', '3-Year Total']
    
    # Financial data
    investment = [610, 160, 160, 930]  # Cumulative would be 930K
    savings = [600, 600, 600, 1800]     # Annual savings
    net_benefit = [-10, 440, 440, 870]  # Savings - Investment
    
    x = np.arange(len(years))
    width = 0.25
    
    # Create grouped bars
    bars1 = ax.bar(x - width, investment, width, label='Investment', 
                   color=DANGER_COLOR, alpha=0.8, edgecolor=PRIMARY_COLOR, linewidth=1.5)
    bars2 = ax.bar(x, savings, width, label='Turnover Cost Savings', 
                   color=SUCCESS_COLOR, alpha=0.8, edgecolor=PRIMARY_COLOR, linewidth=1.5)
    bars3 = ax.bar(x + width, net_benefit, width, label='Net Benefit', 
                   color=ACCENT_COLOR, alpha=0.8, edgecolor=PRIMARY_COLOR, linewidth=1.5)
    
    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            if height != 0:
                label = f'${abs(height)}K' if height > 0 else f'-${abs(height)}K'
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       label, ha='center', va='bottom' if height > 0 else 'top',
                       fontsize=10, fontweight='bold')
    
    # Add break-even line
    ax.axhline(y=0, color='black', linestyle='-', linewidth=2, alpha=0.5)
    ax.text(3.5, 50, 'Break-Even Line', fontsize=9, style='italic')
    
    # Formatting
    ax.set_ylabel('Amount ($K)', fontsize=13, fontweight='bold')
    ax.set_title('Retention Acceleration Program: 3-Year ROI Projection', 
                fontsize=15, fontweight='bold', pad=20, color=PRIMARY_COLOR)
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=12)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
    ax.grid(True, axis='y', alpha=0.3, linestyle='--')
    
    # Add ROI summary box
    summary_text = 'ROI Summary:\n• Year 1: Break-even (~0% ROI)\n• Year 2: 275% ROI ($440K return on $160K)\n• Year 3: 275% ROI (sustained)\n• 3-Year Total: 94% ROI ($870K net benefit)'
    ax.text(0.02, 0.98, summary_text, transform=ax.transAxes,
           fontsize=10, verticalalignment='top',
           bbox=dict(boxstyle='round,pad=0.8', facecolor=LIGHT_BG, 
                    edgecolor=PRIMARY_COLOR, linewidth=2, alpha=0.9))
    
    # Add prevented departures annotation
    ax.text(2.5, -200, '12 prevented departures/year × $50K cost = $600K annual savings', 
           ha='center', fontsize=10, style='italic', color=PRIMARY_COLOR,
           bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('visuals/roi_projection.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created roi_projection.png")
    plt.close()


def create_evaluation_framework():
    """Chart 5: Evaluation Framework - KPIs Dashboard"""
    
    fig, ax = plt.subplots(figsize=(14, 10), facecolor='white')
    
    # Three KPI categories
    categories = {
        'Outcome KPIs': [
            ('Retention Rate', '60% → 75%+', '15 pts', SUCCESS_COLOR),
            ('Engagement Scores', 'Baseline → +20 pts', '+20 pts', SUCCESS_COLOR),
            ('Manager Effectiveness', 'Baseline → +30 pts', '+30 pts', SUCCESS_COLOR),
            ('Job Satisfaction', 'Baseline → +15 pts', '+15 pts', WARNING_COLOR),
            ('Career Growth', 'Baseline → +20 pts', '+20 pts', WARNING_COLOR)
        ],
        'Process KPIs': [
            ('Training Attendance', '90%+ complete', '90%', ACCENT_COLOR),
            ('Skill Application', '80%+ doing 1-on-1s', '80%', ACCENT_COLOR),
            ('Budget Adherence', '≤$610K Year 1', '$610K', ACCENT_COLOR),
            ('Manager Satisfaction', '70%+ "valuable"', '70%', WARNING_COLOR)
        ],
        'Impact KPIs': [
            ('Turnover Cost Savings', '$600K annual', '$600K', SUCCESS_COLOR),
            ('Promotion Rate', '+20-30% increase', '+25%', SUCCESS_COLOR),
            ('Productivity', '+10-15% improvement', '+12%', WARNING_COLOR)
        ]
    }
    
    # Layout
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Evaluation Framework: Key Performance Indicators', 
           fontsize=16, fontweight='bold', ha='center', color=PRIMARY_COLOR)
    
    # Draw three columns
    column_x = [1, 4.2, 7.4]
    column_titles = list(categories.keys())
    
    for col_idx, (x_pos, title) in enumerate(zip(column_x, column_titles)):
        # Column header
        header_box = FancyBboxPatch((x_pos - 0.4, 8.3), 2.8, 0.6, 
                                    boxstyle="round,pad=0.05",
                                    facecolor=PRIMARY_COLOR, edgecolor='none', alpha=0.9)
        ax.add_patch(header_box)
        ax.text(x_pos + 1, 8.6, title, fontsize=12, fontweight='bold', 
               ha='center', va='center', color='white')
        
        # KPI boxes
        kpis = categories[title]
        y_start = 7.8
        box_height = 0.8
        spacing = 0.2
        
        for i, (kpi_name, target, value, color) in enumerate(kpis):
            y_pos = y_start - i * (box_height + spacing)
            
            # KPI box
            kpi_box = FancyBboxPatch((x_pos - 0.4, y_pos - box_height), 2.8, box_height,
                                     boxstyle="round,pad=0.05",
                                     facecolor=color, edgecolor=PRIMARY_COLOR, 
                                     linewidth=1.5, alpha=0.3)
            ax.add_patch(kpi_box)
            
            # KPI name
            ax.text(x_pos + 1, y_pos - 0.25, kpi_name, 
                   fontsize=9, fontweight='bold', ha='center', color=PRIMARY_COLOR)
            
            # Target value
            ax.text(x_pos + 1, y_pos - 0.55, f'Target: {target}', 
                   fontsize=8, ha='center', color=PRIMARY_COLOR, style='italic')
    
    # Measurement approach box at bottom
    measurement_box = FancyBboxPatch((0.5, 0.3), 9, 2.5, boxstyle="round,pad=0.1",
                                     facecolor=LIGHT_BG, edgecolor=PRIMARY_COLOR, 
                                     linewidth=2, alpha=0.6)
    ax.add_patch(measurement_box)
    
    ax.text(5, 2.5, 'MEASUREMENT APPROACH', fontsize=12, fontweight='bold', 
           ha='center', color=PRIMARY_COLOR)
    
    ax.text(5, 2.1, 'Quantitative: Quarterly pulse surveys (engagement, manager effectiveness, job satisfaction, career growth)', 
           fontsize=9, ha='center', color=PRIMARY_COLOR)
    ax.text(5, 1.8, 'Quantitative: HRIS data (retention rates, turnover, promotions, compensation)', 
           fontsize=9, ha='center', color=PRIMARY_COLOR)
    ax.text(5, 1.5, 'Qualitative: Manager interviews, employee focus groups, exit interviews, observations', 
           fontsize=9, ha='center', color=PRIMARY_COLOR)
    ax.text(5, 1.2, 'Mixed Methods: Integration of quantitative results with qualitative insights for comprehensive understanding', 
           fontsize=9, ha='center', color=PRIMARY_COLOR)
    
    ax.text(5, 0.7, 'Evaluation Design: Quasi-experimental (pilot vs. control) + Before-and-after + Longitudinal (24 months)', 
           fontsize=9, ha='center', color=PRIMARY_COLOR, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                    edgecolor=ACCENT_COLOR, linewidth=2))
    
    plt.tight_layout()
    plt.savefig('visuals/evaluation_framework.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created evaluation_framework.png")
    plt.close()


def create_7questions_summary():
    """Chart 6: 7 Questions Framework Summary"""
    
    fig, ax = plt.subplots(figsize=(14, 10), facecolor='white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, '7 Questions Framework: Critical Assessment Results', 
           fontsize=16, fontweight='bold', ha='center', color=PRIMARY_COLOR)
    
    # Questions with answers
    questions = [
        ('1. Generalizability', 'Can we apply this evidence to our situation?', 
         'YES (75% confidence) - PICOC analysis shows strong match', SUCCESS_COLOR),
        
        ('2. Expected Value', 'Do benefits outweigh costs?', 
         'YES - $600K annual savings vs. $610K Year 1 investment (break-even Year 1, 200% ROI Years 2-3)', SUCCESS_COLOR),
        
        ('3. Alternatives', 'Is this the best bang for buck?', 
         'YES - Combined approach prevents 12 departures/yr vs. 5-8 for alternatives', SUCCESS_COLOR),
        
        ('4. Risk', 'What could go wrong?', 
         'Manager resistance (60% likely), Budget constraints (50%), Impatience (65%) - All mitigated by pilot', WARNING_COLOR),
        
        ('5. Trustworthiness', 'How much can we trust this evidence?', 
         'MEDIUM-HIGH (75%) - Strong scientific evidence, validated by practitioner consensus', SUCCESS_COLOR),
        
        ('6. Communication', 'How do we explain to stakeholders?', 
         'Tailored messaging: Executives (ROI), Managers (development), Employees (support)', ACCENT_COLOR),
        
        ('7. Continuous Learning', 'How will we know if it\'s working?', 
         'Quarterly measurement (engagement, manager effectiveness, retention) + Decision points at 3, 6, 12, 18 months', ACCENT_COLOR)
    ]
    
    y_start = 8.8
    box_height = 1.15
    spacing = 0.05
    
    for i, (question_num, question, answer, color) in enumerate(questions):
        y_pos = y_start - i * (box_height + spacing)
        
        # Question box
        question_box = FancyBboxPatch((0.3, y_pos - box_height), 9.4, box_height,
                                      boxstyle="round,pad=0.08",
                                      facecolor=color, edgecolor=PRIMARY_COLOR,
                                      linewidth=2, alpha=0.2)
        ax.add_patch(question_box)
        
        # Question number and text
        ax.text(0.6, y_pos - 0.3, question_num, 
               fontsize=11, fontweight='bold', ha='left', color=PRIMARY_COLOR)
        ax.text(2.2, y_pos - 0.3, question, 
               fontsize=10, fontweight='bold', ha='left', color=PRIMARY_COLOR, style='italic')
        
        # Answer
        ax.text(5, y_pos - 0.75, answer, 
               fontsize=9, ha='center', color=PRIMARY_COLOR,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
    
    # Overall verdict box
    verdict_box = FancyBboxPatch((1, 0.3), 8, 0.9, boxstyle="round,pad=0.1",
                                 facecolor=SUCCESS_COLOR, edgecolor=PRIMARY_COLOR,
                                 linewidth=3, alpha=0.8)
    ax.add_patch(verdict_box)
    
    ax.text(5, 0.9, 'OVERALL VERDICT: PROCEED WITH PILOT', 
           fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(5, 0.5, 'Evidence supports intervention | Pilot mitigates risks | ROI compelling | Implementation feasible', 
           fontsize=10, ha='center', color='white', style='italic')
    
    plt.tight_layout()
    plt.savefig('visuals/7questions_summary.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Created 7questions_summary.png")
    plt.close()


def main():
    print("\n📊 Generating Milestone 3 Visualizations...\n")
    
    # Create all charts
    create_bayesian_journey_chart()
    create_logic_model_diagram()
    create_implementation_timeline()
    create_roi_projection()
    create_evaluation_framework()
    create_7questions_summary()
    
    print("\n✅ All Milestone 3 visualizations created successfully!")
    print("   Files saved to: visuals/")
    print("\n   Created 6 charts:")
    print("   1. bayesian_confidence_journey.png - Confidence evolution 30%→85%")
    print("   2. logic_model_diagram.png - X→M→Y causal framework")
    print("   3. implementation_timeline.png - 24-month Gantt chart")
    print("   4. roi_projection.png - 3-year financial analysis")
    print("   5. evaluation_framework.png - KPIs dashboard")
    print("   6. 7questions_summary.png - Critical assessment results")

if __name__ == "__main__":
    main()
