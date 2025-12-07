# SaaS MRR Growth Analysis – 2024

**Email:** 23f3001448@ds.study.iitm.ac.in  

## Business Context

Our SaaS company is experiencing slowing monthly recurring revenue (MRR) growth.  
The executive team needs a clear, data-driven explanation of current performance and guidance on how to close the gap to the **industry target of 15**.

## Data Used

2024 Quarterly MRR Growth:

- **Q1:** 3.58  
- **Q2:** 5.48  
- **Q3:** 9.31  
- **Q4:** 10.77  

**Average MRR Growth (2024):** **7.29**  
**Industry Target:** **15**

## Analysis Summary

Using the quarterly data, we:

1. Loaded the data into a structured DataFrame (Python / pandas).  
2. Computed the **average MRR growth** for 2024: **7.29**, which is less than half of the industry target (15).  
3. Visualized the quarterly trend with a line chart and overlaid the **industry target** as a benchmark line.  

The visualization file is: `mrr_growth_trend.png`.

## Key Findings

1. **Consistent underperformance vs target**  
   - Every quarter is significantly below the target of 15.  
   - Even in **Q4 (10.77)**, we are still **~4.23 points below** the benchmark.

2. **Improving but insufficient trend**  
   - Growth is increasing quarter-over-quarter (from **3.58 → 10.77**).  
   - Despite the improvement, the current trajectory is not enough to reach or exceed 15 in the near term without intervention.

3. **High risk for strategic goals**  
   - If this pattern continues, annual revenue targets and investor expectations may be missed.  
   - The company’s current growth engine (existing customer base and existing segments) appears to be nearing saturation.

## Business Implications

- The gap between our **average growth (7.29)** and the **industry target (15)** indicates that:
  - Relying only on **current customer segments** is not sufficient.
  - Our current markets may be **saturated or overly competitive**.
  - Without new growth levers, future MRR growth may stagnate further.

## Recommendation: Expand into New Market Segments

To close the gap and move closer to an MRR growth of 15, we recommend:

1. **Expand into new market segments** (core solution)
   - Identify under-served industries and customer profiles that match our product strengths.
   - Pilot targeted go-to-market (GTM) initiatives in 1–2 new verticals.
   - Use pricing and packaging experiments tailored to new segments.

2. **Deepen penetration within existing accounts**
   - Upsell and cross-sell advanced tiers, add-ons, or usage-based upgrades.
   - Introduce value-based pricing aligned with executive-level outcomes.

3. **Optimize acquisition funnel**
   - Improve conversion rates via better qualification, onboarding, and trial experiences.
   - Strengthen marketing in segments with higher LTV/CAC ratios.

## Tools and Implementation Notes

- The analysis was developed with LLM assistance (ChatGPT / code generation) and implemented in **Python**.
- Libraries used:
  - `pandas` for data handling
  - `matplotlib` for the MRR growth vs target visualization
- Script: `mrr_analysis.py`
- Visualization: `mrr_growth_trend.png`

This analysis provides a concise but complete data story:  
we are underperforming vs the industry (7.29 vs 15), improving but not fast enough, and need to **expand into new market segments** to unlock the next phase of growth.
