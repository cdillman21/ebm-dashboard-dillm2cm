# Data Sources for Employee Compensation & Retention Research

## Logic Model Variables
- **X (Independent Variable)**: Employee Compensation Packages
- **M (Mediator Variables)**: Employee Satisfaction & Manager Training
- **Y (Dependent Variable)**: Employee Retention

---

## 🏛️ BUREAU OF LABOR STATISTICS (BLS) DATASETS

### 1. **Job Openings and Labor Turnover Survey (JOLTS)**
**URL**: https://www.bls.gov/jlt/

**Related to**: **Y - Employee Retention** (PRIMARY)

**Key Variables**:
- **Hires Rate** (by industry, monthly)
- **Separations Rate** (total, quits, layoffs)
  - Quits Rate (voluntary turnover - key retention measure)
  - Layoffs and Discharges Rate
- **Job Openings Rate**
- **Industry breakdowns** (all NAICS sectors)
- **Firm size categories**
- **Geographic data** (national and state-level)

**Time Period**: December 2000 - present (monthly data)

**Why It's Useful**: 
- Quits rate is a direct measure of voluntary turnover (inverse of retention)
- Can analyze retention patterns across industries and time periods
- Shows labor market tightness which affects retention

**Data Access**: https://www.bls.gov/jlt/data.htm

---

### 2. **Employment Cost Index (ECI)**
**URL**: https://www.bls.gov/ncs/ect/

**Related to**: **X - Employee Compensation** (PRIMARY)

**Key Variables**:
- **Total Compensation Costs** (wages + benefits)
- **Wages and Salaries** (by occupation, industry)
- **Benefits Costs** broken down by:
  - Health insurance
  - Paid leave (vacation, sick, holidays)
  - Retirement and savings
  - Supplemental pay (bonuses, overtime)
  - Legally required benefits
- **Percent change** (3-month and 12-month)
- **Industry classifications** (NAICS)
- **Occupational groups** (management, professional, service, etc.)
- **Private vs. public sector**
- **Union vs. non-union**

**Time Period**: 1976 - present (quarterly data)

**Why It's Useful**:
- Comprehensive compensation data beyond just wages
- Shows trends in total cost to employer
- Can isolate specific compensation components

**Data Access**: https://www.bls.gov/ncs/data.htm

---

### 3. **National Compensation Survey (NCS)**
**URL**: https://www.bls.gov/ncs/

**Related to**: **X - Employee Compensation** (PRIMARY)

**Key Variables**:
- **Employer Costs for Employee Compensation (ECEC)**
  - Cost per hour worked
  - Wages and salaries percentage
  - Benefits percentage (by type)
- **Employee Benefits Survey (NCS-EB)**
  - Access to benefits (percentage of workers)
  - Take-up rates
  - Specific benefit details (retirement plan types, health insurance coverage levels)
- **By occupation and industry**
- **By establishment size**
- **By geographic area**
- **Union vs. non-union status**

**Time Period**: 2004 - present

**Why It's Useful**:
- Detailed breakdown of what employees actually receive
- Shows access vs. participation in benefits
- Can identify trends in compensation packages for early-career workers

**Data Access**: https://www.bls.gov/ncs/data.htm

---

### 4. **Occupational Employment and Wage Statistics (OEWS)**
**URL**: https://www.bls.gov/oes/

**Related to**: **X - Employee Compensation** (SUPPLEMENTAL)

**Key Variables**:
- **Employment levels** by occupation
- **Wage estimates**:
  - Mean annual wages
  - Median annual wages
  - Wage percentiles (10th, 25th, 75th, 90th)
- **Industry classification** (NAICS codes)
- **Geographic area** (national, state, metropolitan)
- **Detailed occupation codes** (SOC system)

**Time Period**: 1988 - present (annual, May reference period)

**Why It's Useful**:
- Granular wage data by specific occupations
- Can identify entry-level positions
- Shows wage distribution and competitiveness

**Data Access**: https://www.bls.gov/oes/tables.htm

---

## 📊 USA FACTS

### 5. **USAFacts Economy Data**
**URL**: https://usafacts.org/economy/

**Related to**: **X - Compensation** & **Y - Employment** (CONTEXTUAL)

**Key Variables**:
- **Federal spending on labor programs**
- **Unemployment insurance data**
- **Tax data** affecting take-home pay
- **Inflation indicators** (CPI)
- **Cost of living by state**
- **Government employment data**

**Time Period**: Varies by dataset (primarily 2000-present)

**Why It's Useful**:
- Contextual economic data
- Shows purchasing power of wages
- Government intervention in labor markets

**Data Access**: https://usafacts.org/data/

---

## 🌍 WORLD BANK

### 6. **World Development Indicators (WDI)**
**URL**: https://databank.worldbank.org/source/world-development-indicators

**Related to**: **X - Compensation**, **Y - Employment** (INTERNATIONAL COMPARISON)

**Key Variables** (for US comparisons):
- **Labor force participation rate**
- **Unemployment rate** (total and youth)
- **Employment to population ratio**
- **Wage and salaried workers** (% of employment)
- **Part-time employment**
- **GDP per capita** (PPP)
- **Income inequality** (Gini coefficient)

**Time Period**: 1960 - present (annual)

**Why It's Useful**:
- International benchmarking
- Long-term trend analysis
- Economic context for US labor market

**Data Access**: https://databank.worldbank.org/

---

## 🏛️ ADDITIONAL US GOVERNMENT DATABASES

### 7. **Federal Reserve Economic Data (FRED)**
**URL**: https://fred.stlouisfed.org/

**Related to**: **X - Compensation**, **Y - Retention**, **M - Satisfaction** (COMPREHENSIVE)

**Key Variables**:
- **Average Hourly Earnings** (all employees, production workers)
- **Employment Cost Index** (links to BLS data)
- **Quit Rate** (from JOLTS)
- **Job Openings Rate** (from JOLTS)
- **Real median household income**
- **Consumer Price Index** (inflation)
- **Labor force participation**
- **Unemployment rate** by demographics

**Time Period**: Varies (many series from 1940s-present)

**Why It's Useful**:
- Easy data visualization and download
- Combines multiple government sources
- Can create custom charts and analysis

**Data Access**: https://fred.stlouisfed.org/categories

---

### 8. **Census Bureau - American Community Survey (ACS)**
**URL**: https://www.census.gov/programs-surveys/acs/data.html

**Related to**: **X - Compensation**, **Y - Employment Status** (DEMOGRAPHIC)

**Key Variables**:
- **Median earnings** by occupation, industry, education
- **Employment status** by demographics
- **Health insurance coverage** (employer vs. other)
- **Commuting costs**
- **Educational attainment** by employment
- **Age cohorts** (can isolate early career workers 22-30)

**Time Period**: 2005 - present (annual)

**Why It's Useful**:
- Demographic breakdown of compensation
- Can isolate "early career" workers
- Geographic granularity (state, metro, county)

**Data Access**: https://data.census.gov/

---

### 9. **Office of Personnel Management (OPM) - Federal Employee Viewpoint Survey (FEVS)**
**URL**: https://www.opm.gov/fevs/

**Related to**: **M - Employee Satisfaction** (PRIMARY for Government)

**Key Variables**:
- **Job satisfaction scores**
- **Engagement index**
- **Supervisor effectiveness** (manager quality)
- **Work-life balance** ratings
- **Pay satisfaction**
- **Intent to stay** (retention indicator)
- **Training and development** opportunities
- **Demographics** (tenure, age, supervisory status)

**Time Period**: 2002 - present (annual)

**Why It's Useful**:
- Direct measure of employee satisfaction
- Links satisfaction to retention intent
- Shows impact of management quality
- Large sample size (400,000+ federal employees)

**Data Access**: https://www.opm.gov/fevs/reports/

---

### 10. **Bureau of Labor Statistics - Employee Tenure Data**
**URL**: https://www.bls.gov/news.release/tenure.htm

**Related to**: **Y - Employee Retention** (SUPPLEMENTAL)

**Key Variables**:
- **Median years of tenure** with current employer
- **Distribution of tenure** (less than 1 year, 1-5 years, 5-10 years, etc.)
- **By age group** (can focus on younger workers)
- **By industry**
- **By occupation**
- **Full-time vs. part-time**

**Time Period**: 1983 - present (biennial, January survey)

**Why It's Useful**:
- Direct measure of retention (tenure)
- Can analyze early-career workers specifically
- Shows turnover patterns by industry

**Data Access**: https://www.bls.gov/cps/tables.htm#tenure

---

## 📈 RECOMMENDED DATA COLLECTION STRATEGY

### For Your Logic Model:

#### **X (Employee Compensation Packages)**
**Primary Sources**:
1. Employment Cost Index (ECI) - quarterly compensation trends
2. National Compensation Survey - detailed benefit packages
3. OEWS - wage levels by occupation

**Variables to Extract**:
- Total compensation (wages + benefits) by industry/occupation
- Specific benefit components (health, retirement, paid leave)
- Wage percentiles for entry-level positions
- Year-over-year changes in compensation

#### **M (Employee Satisfaction & Manager Training)**
**Primary Sources**:
1. Federal Employee Viewpoint Survey (FEVS) - satisfaction measures
2. (You may need to supplement with academic datasets like GSS, Gallup Workplace Survey, or conduct your own survey)

**Variables to Extract**:
- Overall job satisfaction scores
- Supervisor/manager effectiveness ratings
- Training and development opportunities
- Work-life balance indicators
- Pay satisfaction

#### **Y (Employee Retention)**
**Primary Sources**:
1. JOLTS - quits rate (inverse measure of retention)
2. Employee Tenure Data - median tenure
3. JOLTS - hires and separations rates

**Variables to Extract**:
- Voluntary turnover rate (quits rate)
- Median employee tenure
- Separation rates by reason
- Hires-to-separations ratio

---

## 💡 ANALYSIS RECOMMENDATIONS

### 1. **Time Series Analysis**
- Use JOLTS monthly data (2000-2025) to track retention trends
- Correlate with ECI quarterly data on compensation changes
- Identify lag effects (does compensation change in Q1 affect quits in Q2-Q3?)

### 2. **Cross-Sectional Analysis**
- Compare industries with high compensation vs. low compensation
- Analyze retention rates across these industries
- Control for other factors (firm size, geography)

### 3. **Early Career Focus**
- Use ACS to isolate workers aged 22-30
- Filter OEWS for entry-level occupations (0-2 years experience)
- Analyze tenure data for workers with <5 years at current employer

### 4. **Mediator Analysis**
- Use FEVS satisfaction data as mediator
- Test if compensation → satisfaction → retention pathway exists
- Control for manager training/quality variables

---

## 📥 DATA DOWNLOAD TIPS

1. **BLS Data Tools**: Use the "Multi-Screen Data Search" for custom queries
2. **FRED**: Create custom charts and export to Excel/CSV
3. **Census Data**: Use data.census.gov with table filters for specific variables
4. **API Access**: Many of these sources offer API access for automated data collection

---

## 🔗 QUICK LINKS SUMMARY

| Dataset | URL | Primary Variable |
|---------|-----|------------------|
| JOLTS | https://www.bls.gov/jlt/data.htm | Y - Retention (quits rate) |
| Employment Cost Index | https://www.bls.gov/ncs/ect/ | X - Compensation |
| National Compensation Survey | https://www.bls.gov/ncs/data.htm | X - Benefits packages |
| OEWS | https://www.bls.gov/oes/tables.htm | X - Wages by occupation |
| FEVS | https://www.opm.gov/fevs/reports/ | M - Satisfaction |
| Employee Tenure | https://www.bls.gov/cps/tables.htm#tenure | Y - Retention (tenure) |
| FRED | https://fred.stlouisfed.org/ | X, M, Y - Multiple |
| American Community Survey | https://data.census.gov/ | X, Y - Demographics |

---

**Last Updated**: October 28, 2025
**Created for**: EBM Dashboard - Compensation & Retention Research
