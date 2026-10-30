# Try it

All numerical examples are synthetic. These checks concern observable behavior, not whether the assistant matches a preferred sentence word for word.

## 1. A results paragraph

Request:

> Use this skill to polish the passage below. Preserve the supplied evidence and improve the argument.
>
> We find a positive effect. We report this in Panel B. We add a control and the estimate is smaller. We conclude that the result is robust.
>
> Evidence: Panel B belongs to Table 4. The baseline coefficient is 0.08 (SE 0.02). Adding the historical control reduces it to 0.01 (SE 0.03), on the same sample. The outcome is completed schooling years. Exposure is a one-standard-deviation increase in district program intensity.

Check whether the response makes the comparison intelligible, identifies the table, preserves the scale and uncertainty, and explains the change in the estimate.

## 2. An IV interpretation

Request:

> Revise this IV paragraph for an empirical economics paper.
>
> Our IV coefficient is much larger than OLS. This proves that measurement error explains the discrepancy.
>
> Evidence: OLS is 0.04 (SE 0.01), IV is 0.24 (SE 0.07), on the same sample and scale. The instrument measures a historical supply change. There is no independent validation sample for measurement error. No evidence is supplied about which districts have higher treatment responses.

Check whether the response offers a constructive explanation while keeping facts, possible mechanisms and identifying assumptions distinct.

## 3. A concise abstract

Request:

> Rewrite this abstract using the supplied facts. Keep the main contribution and all three declared core outcomes. Include the sample scale, but omit the full regression formula and the fixed-effect list.
>
> Facts: 2.4 million census observations; a school-building program; a cohort comparison across districts with different program exposure. Baseline estimates show statistically significant gains in schooling years, formal schooling and primary completion. The data also document local implementation. The supplied evidence does not identify a causal effect of household preferences.

Check whether the result is readable, motivated, complete about the core outcomes, and faithful to the evidence.
