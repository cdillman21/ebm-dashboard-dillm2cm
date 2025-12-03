# Data Source Barrier Analysis
## Overcoming the 10 Barriers to Evidence-Based Management

**Your Research Model**: (X) Employee Compensation → (M) Employee Satisfaction & Manager Training → (Y) Employee Retention

---

## The 10 Barriers (Modules 9 & 10)

1. **Absence of Logic Model**
2. **Irrelevant Data**
3. **Inaccurate Data**
4. **Missing Contextual Information**
5. **Measurement Error**
6. **Small Number Problem**
7. **Confusing Percentages/Averages**
8. **Misleading Graphs**
9. **Correlations/Regression/Overfitting**
10. **Wide Confidence Intervals**

---

## Barrier-by-Barrier Analysis of Data Sources

### BARRIER 1: Absence of Logic Model
**Risk**: Using data without a clear causal framework

**Best Sources to Overcome**:
- ✅ **JOLTS + ECI + FEVS (Combined Approach)** - You've already created your logic model (X→M→Y), and these sources directly map to each variable
- ✅ **Federal Employee Viewpoint Survey (FEVS)** - Explicitly asks about pay satisfaction, supervisor effectiveness, and intent to stay (all three components of your model)

**Worst Sources**:
- ❌ **USAFacts** - General economic data without clear variable linkages
- ❌ **World Bank** - Too macro-level, doesn't connect to your specific logic

**Recommendation**: ✅ You're safe here - your logic model is already well-defined

---

### BARRIER 2: Irrelevant Data
**Risk**: Collecting data that doesn't measure your actual variables of interest

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - Directly measures quits (voluntary turnover = inverse of retention = your Y variable)
- ✅ **BLS Employment Cost Index (ECI)** - Specifically measures total compensation packages (your X variable)
- ✅ **FEVS** - Directly asks about job satisfaction and manager quality (your M variable)

**Worst Sources**:
- ❌ **World Bank WDI** - International data not directly relevant to US employee retention
- ❌ **Census ACS** - Broad demographic data, harder to isolate compensation-retention relationship

**Recommendation**: Stick with **BLS JOLTS, BLS ECI, and FEVS** - they're the most precisely relevant

---

### BARRIER 3: Inaccurate Data
**Risk**: Data collection methods are flawed or biased

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - Gold standard, mandatory reporting from 21,000+ establishments, rigorous quality controls
- ✅ **BLS ECI** - Probability sample, consistent methodology since 1976, peer-reviewed
- ✅ **BLS OEWS** - 1.1 million establishments surveyed over 3 years, statistically validated

**Moderate Sources**:
- ⚠️ **FEVS** - Self-reported survey, but N=400,000+ so individual bias averages out
- ⚠️ **Census ACS** - Self-reported, but large sample and Census Bureau quality controls

**Worst Sources**:
- ❌ **USAFacts** - Aggregates data from multiple sources (variable quality)

**Recommendation**: **BLS sources are your safest bet** - they have the most rigorous data collection and validation

---

### BARRIER 4: Missing Contextual Information
**Risk**: Data lacks industry, occupation, geography, or demographic context needed for interpretation

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - Provides breakdowns by:
  - Industry (all NAICS sectors)
  - Firm size
  - Region and state
  - Reason for separation (quits vs. layoffs)
  
- ✅ **BLS ECI** - Provides breakdowns by:
  - Industry and occupation
  - Union vs. non-union
  - Public vs. private sector
  - Geographic region
  - Establishment size
  
- ✅ **Census ACS** - Rich demographic context:
  - Age groups (can isolate early career)
  - Education level
  - Occupation and industry
  - Geographic granularity (state/county/metro)

**Worst Sources**:
- ❌ **FRED** - Often shows aggregate totals without detailed breakdowns

**Recommendation**: **BLS JOLTS + ECI combination** gives you the most contextual variables

---

### BARRIER 5: Measurement Error
**Risk**: Variables are measured inconsistently or with poor precision

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - Uses standardized definitions:
  - "Quits" = employee-initiated separations (clear operational definition)
  - Collected monthly with consistent methodology
  
- ✅ **BLS ECI** - Uses same establishments over time (panel data reduces measurement error)
  - Fixed basket of occupations (like CPI for compensation)
  
- ✅ **Employee Tenure Data** - Direct measure from CPS supplement, well-validated

**Moderate Sources**:
- ⚠️ **FEVS** - Likert scales subject to interpretation, but validated instrument
- ⚠️ **OEWS** - Point-in-time estimates (May of each year), not continuous

**Worst Sources**:
- ❌ **USAFacts** - Secondary aggregation can introduce errors

**Recommendation**: **BLS JOLTS and ECI** have the most precise, consistent measurement

---

### BARRIER 6: Small Number Problem
**Risk**: Sample size too small, leading to unreliable estimates or inability to detect effects

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - 21,000+ establishments monthly = millions of employee records
- ✅ **FEVS** - 400,000+ federal employee responses annually
- ✅ **BLS OEWS** - 1.1 million establishments over 3 years
- ✅ **Census ACS** - 3.5 million households annually

**Moderate Sources**:
- ⚠️ **Employee Tenure Data** - 60,000 households in CPS (still large, but smaller than above)

**Worst Sources**:
- ❌ **None of these have small sample problems** - all are nationally representative large-scale surveys

**Recommendation**: **You're safe with any BLS or Census source** - all have massive sample sizes

---

### BARRIER 7: Confusing Percentages/Averages
**Risk**: Misinterpreting rates, not understanding denominators, or confusing means/medians

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - Clear documentation:
  - Rates calculated as: (number of events / total employment) × 100
  - Levels (counts) also provided
  - Seasonally adjusted vs. not seasonally adjusted clearly labeled
  
- ✅ **BLS ECI** - Clear percentage change calculations:
  - 3-month percent change
  - 12-month percent change
  - Index values also provided
  
- ✅ **OEWS** - Provides both:
  - Mean (average) wages
  - Median wages
  - Percentiles (10th, 25th, 75th, 90th)

**Moderate Sources**:
- ⚠️ **FEVS** - Uses means of Likert scales (be careful interpreting 3.7 out of 5)

**Worst Sources**:
- ❌ **USAFacts** - Sometimes presents percentages without clear denominators

**Recommendation**: **BLS sources have excellent documentation** - read the technical notes to avoid confusion

---

### BARRIER 8: Misleading Graphs
**Risk**: Data visualization that distorts trends or relationships

**Best Sources to Overcome**:
- ✅ **FRED (Federal Reserve Economic Data)** - Provides:
  - Raw data download (make your own graphs)
  - Transparent axis labels and scales
  - Option to show multiple series on same scale
  - Can normalize to base year 100
  
- ✅ **BLS Website Charts** - Generally good:
  - Clear axis labels
  - Source data available
  - Seasonally adjusted noted

**Moderate Sources**:
- ⚠️ **USAFacts** - Some infographics can be misleading (use their raw data instead)

**Recommendation**: **Download raw data and create your own visualizations** using the data tables from BLS or FRED - don't rely solely on pre-made charts

---

### BARRIER 9: Correlations/Regression/Overfitting
**Risk**: Finding spurious relationships, confusing correlation with causation, or overfitting models

**Best Sources to Overcome**:
- ✅ **BLS JOLTS + ECI (Time Series)** - Allows you to:
  - Test temporal relationships (does compensation change in Q1 predict quits in Q2?)
  - Use lagged variables to establish temporal precedence
  - Control for seasonal patterns
  - Long time series (2000-2025 for JOLTS) reduces overfitting risk
  
- ✅ **Census ACS (Cross-Sectional)** - Large sample allows you to:
  - Include multiple control variables without overfitting
  - Stratify by industry/occupation/geography
  - Test robustness across subgroups
  
- ✅ **FEVS (Direct Measurement of Mediator)** - Asks about:
  - Both compensation satisfaction AND intent to leave
  - Allows direct test of mediation hypothesis
  - Large N reduces false positive risk

**Moderate Sources**:
- ⚠️ **OEWS** - Annual only, harder to establish temporal relationships
- ⚠️ **Employee Tenure** - Biennial, limited time points

**Recommendation**: **Use JOLTS + ECI time series data** with proper lag structures and control for autocorrelation. For mediator analysis, **FEVS is critical** because it measures X, M, and Y in the same survey (avoiding ecological fallacy)

---

### BARRIER 10: Wide Confidence Intervals
**Risk**: Uncertainty in estimates so large that you can't draw meaningful conclusions

**Best Sources to Overcome**:
- ✅ **BLS JOLTS** - Publishes standard errors and confidence intervals
  - National estimates: very narrow CIs (huge sample)
  - State estimates: wider CIs (use caution)
  - Can calculate statistical significance of changes
  
- ✅ **BLS ECI** - Narrow confidence intervals due to:
  - Panel design (same establishments over time)
  - Large sample size
  - Published standard errors available
  
- ✅ **Census ACS** - Publishes margins of error:
  - 90% confidence intervals for all estimates
  - Very narrow for national/state estimates
  - Wider for small geographic areas or small demographic groups

**Moderate Sources**:
- ⚠️ **OEWS** - CIs available but can be wide for rare occupations or small areas

**Worst Sources**:
- ❌ **FEVS** - Only federal employees (can't generalize to private sector with known confidence)
- ❌ **Employee Tenure** - CIs not always published

**Recommendation**: **Stick with national-level estimates from JOLTS and ECI** for tightest confidence intervals. If using state or industry breakdowns, check published standard errors before drawing conclusions.

---

## 🎯 FINAL RECOMMENDATION: Best Data Source Combination

Based on barrier analysis, here's my recommendation:

### **PRIMARY DATA SOURCES** (Use These)

| Variable | Data Source | Why It Overcomes Barriers |
|----------|-------------|---------------------------|
| **X - Compensation** | **BLS Employment Cost Index (ECI)** | ✅ Large sample (Barrier 6)<br>✅ Accurate, rigorous (Barrier 3)<br>✅ Rich context (Barrier 4)<br>✅ Precise measurement (Barrier 5)<br>✅ Quarterly data for regression (Barrier 9)<br>✅ Narrow CIs (Barrier 10) |
| **Y - Retention** | **BLS JOLTS (Quits Rate)** | ✅ Directly relevant (Barrier 2)<br>✅ Huge sample (Barrier 6)<br>✅ Gold standard accuracy (Barrier 3)<br>✅ Industry/region context (Barrier 4)<br>✅ Monthly data for time series (Barrier 9)<br>✅ Published standard errors (Barrier 10) |
| **M - Satisfaction** | **Federal Employee Viewpoint Survey (FEVS)** | ✅ Directly measures satisfaction (Barrier 2)<br>✅ 400K+ responses (Barrier 6)<br>✅ Links pay satisfaction to retention intent (Barrier 1)<br>✅ Measures all three variables X, M, Y (Barrier 9 - avoids ecological fallacy) |

### **SUPPLEMENTARY SOURCES** (Use for Robustness Checks)

- **BLS Employee Tenure Data** - Alternative measure of Y (retention = median tenure)
- **BLS OEWS** - Additional compensation data (wage levels, not just changes)
- **Census ACS** - Demographic controls and subgroup analysis

### **AVOID OR USE WITH CAUTION**

- ❌ **USAFacts** - Aggregated secondary data (Barriers 3, 4, 7, 8)
- ❌ **World Bank** - Not relevant to US-specific research question (Barrier 2)
- ⚠️ **FRED** - Good for visualization but it's just aggregating BLS data anyway

---

## 📊 Step-by-Step Analysis Plan

### Phase 1: Descriptive Analysis (Overcome Barriers 7, 8)
1. Download **JOLTS quits rate** (2010-2025, monthly, seasonally adjusted)
2. Download **ECI total compensation** (2010-2025, quarterly, private sector)
3. Create clear time series graphs with:
   - Properly labeled axes
   - Source notes
   - Both levels and rates shown
4. Calculate summary statistics (mean, median, SD, range)
5. Document any anomalies or missing data

### Phase 2: Contextual Stratification (Overcome Barriers 2, 4)
1. Break down by **industry** (focus on industries hiring recent grads):
   - Professional and business services
   - Information technology
   - Finance
   - Healthcare
2. Compare **firm size** (small vs. large firms may have different compensation-retention dynamics)
3. Check **regional variation** (cost of living affects compensation value)

### Phase 3: Time Series Correlation (Overcome Barriers 9, 10)
1. Test for **stationarity** (Augmented Dickey-Fuller test)
2. Create **lagged variables**:
   - Does ECI change in Q1 predict JOLTS quits in Q2, Q3, Q4?
   - Test lags of 1, 2, 3, 4 quarters
3. Run **Granger causality test**: Does compensation "Granger-cause" quits?
4. Control for:
   - **Seasonal effects** (use seasonally adjusted data)
   - **Unemployment rate** (FRED) - tight labor markets increase quits regardless of pay
   - **GDP growth** (FRED) - economic conditions confound
5. Report **R-squared, adjusted R-squared, and confidence intervals**
6. Check for **autocorrelation** (Durbin-Watson test) and correct if needed

### Phase 4: Mediation Analysis with FEVS (Overcome Barrier 1, 9)
1. Download **FEVS** responses (2015-2024)
2. Identify relevant survey items:
   - Pay satisfaction (M mediator)
   - Supervisor effectiveness (M mediator - manager training proxy)
   - Intent to stay (Y outcome)
   - Overall satisfaction (M mediator)
3. Run **mediation analysis**:
   - Path A: Pay satisfaction → Overall satisfaction
   - Path B: Overall satisfaction → Intent to stay
   - Path C: Pay satisfaction → Intent to stay (direct effect)
   - Path C': Indirect effect (A × B)
4. Use **bootstrapped confidence intervals** (5,000 iterations) to test significance of mediation
5. Control for demographics (age, tenure, education)

### Phase 5: Robustness Checks (Overcome Barriers 3, 5, 6)
1. **Alternative Y measure**: Use Employee Tenure instead of JOLTS quits - does relationship hold?
2. **Alternative X measure**: Use OEWS wage levels instead of ECI - does relationship hold?
3. **Subgroup analysis**:
   - Does relationship hold for young workers (22-30 from ACS)?
   - Does relationship hold across different industries?
   - Does relationship hold in recessions vs. expansions?
4. **Sensitivity analysis**:
   - Remove outlier quarters (e.g., COVID-19 period 2020-2021)
   - Test different lag structures
   - Try different functional forms (linear, log-linear, quadratic)

---

## ⚠️ LIMITATIONS TO ACKNOWLEDGE

Even with the best data sources, you'll still face some barriers:

### Barrier 9 (Causality) - CANNOT BE FULLY SOLVED WITH OBSERVATIONAL DATA
- **Problem**: You can show correlation and temporal precedence, but not true causation
- **Why**: No random assignment of compensation packages
- **Mitigation**:
  - Use lagged variables (establishes temporal order)
  - Control for confounds (unemployment, GDP, industry)
  - Use FEVS mediation analysis (shows mechanism)
  - Acknowledge in limitations: "Results show association, not causation"

### Barrier 1 (M Variable - Satisfaction) - MEASUREMENT CHALLENGE
- **Problem**: FEVS only covers federal employees, not private sector
- **Why**: No large-scale private sector satisfaction survey with compensation and turnover
- **Mitigation**:
  - Use FEVS for federal employees
  - Argue generalizability (human nature similar across sectors)
  - Look for academic papers using private sector surveys (Gallup, SHRM)
  - Acknowledge limitation: "Mediation tested in federal sector only"

### Barrier 4 (Context) - CANNOT MEASURE EVERYTHING
- **Problem**: Missing data on actual compensation packages (e.g., specific benefits like student loan repayment)
- **Why**: ECI aggregates, doesn't show individual benefit components
- **Mitigation**:
  - Use NCS Employee Benefits Survey for benefit prevalence
  - Acknowledge you're measuring total compensation, not specific package designs
  - Focus on industries where ECI has detailed breakdowns

---

## 🏆 FINAL ANSWER: What to Use

**If I had to pick just ONE combination to overcome the most barriers:**

### **USE: BLS JOLTS + BLS ECI + FEVS**

**Why this combination wins:**

| Barrier | How This Combination Overcomes It |
|---------|-----------------------------------|
| 1. Absence of logic model | ✅ Maps directly to X→M→Y; FEVS measures all three |
| 2. Irrelevant data | ✅ Each source precisely measures one variable |
| 3. Inaccurate data | ✅ All three are gold-standard government surveys |
| 4. Missing context | ✅ Industry, occupation, region, firm size all available |
| 5. Measurement error | ✅ Standardized definitions, consistent methodology |
| 6. Small number problem | ✅ Massive samples (21K establishments, 400K employees) |
| 7. Confusing percentages | ✅ Excellent BLS documentation and technical notes |
| 8. Misleading graphs | ✅ Can download raw data and make your own |
| 9. Correlation/overfitting | ✅ Time series + mediation + large N + controls |
| 10. Wide confidence intervals | ✅ Published standard errors, narrow CIs at national level |

**Data Download Links:**
- JOLTS: https://www.bls.gov/jlt/data.htm (Table 1, quits rate)
- ECI: https://www.bls.gov/ncs/ect/data.htm (Table 1, total compensation)
- FEVS: https://www.opm.gov/fevs/reports/ (Download full dataset)

---

**Created**: October 28, 2025  
**For**: EBM Dashboard - Compensation & Retention Research  
**Purpose**: Barrier-informed data source selection for MGT357
