# Answers with provenance: all-9b-full

Configuration: `all-9b-full`. One section per question, in dataset order. Status ANSWER = all checks passed; NOT_FOUND / AMBIGUOUS = the system abstained (the reason says which check failed). PDF page numbers are 1-based. `Judge` is the eval label against the gold answer (not visible to the system).

## 1. What is the FY2018 capital expenditure amount (in USD millions) for 3M? Give a response to the question by relying on the details shown in the cash flow statement.

`financebench_id_03029` · filing `3M_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 capital expenditure amount for 3M is 1,577 million USD. This figure represents the absolute value of the "Purchases of property, plant and equipment (PP&E)" line item found in the Consolidated Statement of Cash Flows for the year 2018 [v1, v2].

**Computation:** `abs(purchases_of_property_plant_and_equipment_2018) = 1,577 million  where purchases_of_property_plant_and_equipment_2018 = (1,577) (millions, FY2018), purchases_of_property_plant_and_equipment_2018_2 = (1,577) (millions, FY2018)`

- **v1** · `3M_2018_10K` · PDF page **60** · column 2018 · millions
  - Quote: "Purchases of property, plant and equipment (PP&E) \| (1,577) \| (1,373) \| (1,420)"

  <details><summary>Passage</summary>

  ```
   | Inventories | (509) | (387) | 57
   | Accounts payable | 408 | 24 | 148
   | Accrued income taxes (current and long-term) | 134 | 967 | 101
   | Other — net | 120 | 256 | 76
  Net cash provided by (used in) operating activities | 6,439 | 6,240 | 6,662
  Cash Flows from Investing Activities
  Purchases of property, plant and equipment (PP&E) | (1,577) | (1,373) | (1,420)
  Proceeds from sale of PP&E and other assets | 262 | 49 | 58
  Acquisitions, net of cash acquired | 13 | (2,023) | (16)
  Purchases of marketable securities and investments | (1,828) | (2,152) | (1,410)
  Proceeds from maturities and sale of marketable securities and investments | 2,497 | 1,354 | 1,247
  Proceeds from sale of businesses, net of cash sold | 846 | 1,065 | 142
  Other — net | 9 | (6) | (4)
  ```
  </details>

- **v2** · `3M_2018_10K` · PDF page **49** · column 2018 · millions
  - Quote: "Purchases of property, plant and equipment (PP&E) \| (1,577) \| (1,373) \| (1,420)"

  <details><summary>Passage</summary>

  ```
  Major GAAP Cash Flow Categories
  Net cash provided by operating activities | $6,439 | $6,240 | $6,662
  Net cash provided by (used in) investing activities | 222 | (3,086) | (1,403)
  Net cash used in financing activities | (6,701) | (2,655) | (4,626)
  Free Cash Flow (non-GAAP measure)
  Net cash provided by operating activities | $6,439 | $6,240 | $6,662
  Purchases of property, plant and equipment (PP&E) | (1,577) | (1,373) | (1,420)
  Free cash flow | $4,862 | $4,867 | $5,242
  Net income attributable to 3M | $5,349 | $4,858 | $5,050
  Free cash flow conversion | 91 % | 100 % | 104 %
  Off-Balance Sheet Arrangements and Contractual Obligations:
  As of December 31, 2018, the Company has not utilized special purpose entities to facilitate off-balance sheet financing arrangements. Refer to the section
  entitled “Warranties/Guarantees” in Note 16 for discussion of accrued product warranty liabilities and guarantees.
  ```
  </details>

<details><summary>Gold answer</summary>

$1577.00
</details>

## 2. Assume that you are a public equities analyst. Answer the following question by primarily using information that is shown in the balance sheet: what is the year end FY2018 net PPNE for 3M? Answer in USD billions.

`financebench_id_04672` · filing `3M_2018_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** 3M_2018_10K: code checks failed twice: formula: numeric constant 1000 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `3M_2018_10K` pages 2, 44, 47, 56, 57, 58, 59, 60, 81, 87, 106, 124

<details><summary>Gold answer</summary>

$8.70
</details>

## 3. Is 3M a capital-intensive business based on FY2022 data?

`financebench_id_00499` · filing `3M_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, 3M is not considered a capital-intensive business based on FY2022 data, as its property, plant and equipment net ($9,178 million) represents only 26.81% of its net sales ($34,229 million) [v1, v2].

**Computation:** `property_plant_equipment_net_2022 / net_sales_2022 = 0.2681  where net_sales_2022 = $34,229 (millions, FY2022), property_plant_equipment_net_2022 = 9,178 (millions, FY2022)`

- **v1** · `3M_2022_10K` · PDF page **48** · column 2022 · millions
  - Quote: "Net sales \| $34,229"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  3M Company and Subsidiaries
  Consolidated Statement of Income
  Years ended December 31
  (Millions, except per share amounts) | 2022 | 2021 | 2020
  Net sales | $34,229  $35,355  $32,184
  Operating expenses
   | Cost of sales | 19,232 | 18,795 | 16,605
   | Selling, general and administrative expenses | 9,049 | 7,197 | 6,929
   | Research, development and related expenses | 1,862 | 1,994 | 1,878
   | Gain on business divestitures | (2,724) | — | (389)
   | Goodwill impairment expense | 271 | — | —
  ```
  </details>

- **v2** · `3M_2022_10K` · PDF page **50** · column 2022 · millions
  - Quote: "Property, plant and equipment — net \| 9,178"

  <details><summary>Passage</summary>

  ```
   | Total inventories | 5,372 | 4,985
   | Prepaids | 435 | 654
   | Other current assets | 456 | 339
   | Total current assets | 14,688 | 15,403
  Property, plant and equipment | 25,998 | 27,213
   | Less: Accumulated depreciation | (16,820) | (17,784)
   | Property, plant and equipment — net | 9,178 | 9,429
  Operating lease right of use assets | 829 | 858
  Goodwill | 12,790 | 13,486
  Intangible assets — net | 4,699 | 5,288
  Other assets | 4,271 | 2,608
   | Total assets | $46,455  $47,072
  Liabilities
  ```
  </details>

<details><summary>Gold answer</summary>

No, the company is managing its CAPEX and Fixed Assets pretty efficiently, which is evident from below key metrics: CAPEX/Revenue Ratio: 5.1% Fixed assets/Total Assets: 20% Return on Assets= 12.4%
</details>

## 4. What drove operating margin change as of FY2022 for 3M? If operating margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_01226` · filing `3M_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The operating margin decreased by 1.7 percentage points from 20.8% in FY2021 to 19.1% in FY2022 [v1, v2]. This decline was primarily driven by a 3.0 percentage point increase in cost of sales, a 6.1 percentage point increase in SG&A, and a 0.2 percentage point decrease in R&D, partially offset by an 8.0 percentage point gain on business divestitures and a 0.8 percentage point goodwill impairment expense [v3, v4, v5, v6, v7, v8, v9, v10]. The computed result of the net change in expense percentages confirms the 1.7 percentage point drop in operating margin [COMPUTED RESULT].

**Computation:** `(cost_of_sales_percent_2022 + sga_percent_2022 + rd_percent_2022 - gain_on_divestitures_percent_2022 + goodwill_impairment_percent_2022) - (cost_of_sales_percent_2021 + sga_percent_2021 + rd_percent_2021) = 17.7  where operating_income_margin_2022 = 19.1 % (units, FY2022), operating_income_margin_2021 = 20.8 % (units, FY2021), cost_of_sales_percent_2022 = 56.2 % (units, FY2022), cost_of_sales_percent_2021 = 53.2 % (units, FY2021), sga_percent_2022 = 26.5 (units, FY2022), sga_percent_2021 = 20.4 (units, FY2021), rd_percent_2022 = 5.4 (units, FY2022), rd_percent_2021 = 5.6 (units, FY2021), gain_on_divestitures_percent_2022 = (8.0) (units, FY2022), goodwill_impairment_percent_2022 = 0.8 (units, FY2022)`

- **v1** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Operating income margin \| 19.1 % \| 20.8 % \| (1.7)%"

  <details><summary>Passage</summary>

  ```
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  Cost of Sales:
  Cost of sales, measured as a percent of sales, increased in 2022 when compared to the same period last year. Increases were primarily due to 2022 special item costs for
  significant litigation from additional commitments to address PFAS-related matters at 3M's Zwijndrecht, Belgium site (discussed in Note 16), higher raw materials and logistics
  costs, manufacturing productivity headwinds which were further magnified by the shutdown of certain operations in Belgium and progress on restarting previously-idled
  ```
  </details>

- **v2** · `3M_2022_10K` · PDF page **27** · column 2021 · units
  - Quote: "Operating income margin \| 19.1 % \| 20.8 % \| (1.7)%"

  <details><summary>Passage</summary>

  ```
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  Cost of Sales:
  Cost of sales, measured as a percent of sales, increased in 2022 when compared to the same period last year. Increases were primarily due to 2022 special item costs for
  significant litigation from additional commitments to address PFAS-related matters at 3M's Zwijndrecht, Belgium site (discussed in Note 16), higher raw materials and logistics
  costs, manufacturing productivity headwinds which were further magnified by the shutdown of certain operations in Belgium and progress on restarting previously-idled
  ```
  </details>

- **v3** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Cost of sales \| 56.2 % \| 53.2 % \| 3.0 %"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  ```
  </details>

- **v4** · `3M_2022_10K` · PDF page **27** · column 2021 · units
  - Quote: "Cost of sales \| 56.2 % \| 53.2 % \| 3.0 %"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  ```
  </details>

- **v5** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Selling, general and administrative expenses (SG&A) \| 26.5 \| 20.4 \| 6.1"

  <details><summary>Passage</summary>

  ```
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  ```
  </details>

- **v6** · `3M_2022_10K` · PDF page **27** · column 2021 · units
  - Quote: "Selling, general and administrative expenses (SG&A) \| 26.5 \| 20.4 \| 6.1"

  <details><summary>Passage</summary>

  ```
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  ```
  </details>

- **v7** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Research, development and related expenses (R&D) \| 5.4 \| 5.6 \| (0.2)"

  <details><summary>Passage</summary>

  ```
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  Cost of Sales:
  ```
  </details>

- **v8** · `3M_2022_10K` · PDF page **27** · column 2021 · units
  - Quote: "Research, development and related expenses (R&D) \| 5.4 \| 5.6 \| (0.2)"

  <details><summary>Passage</summary>

  ```
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  Cost of Sales:
  ```
  </details>

- **v9** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Gain on business divestitures \| (8.0) \| — \| (8.0)"

  <details><summary>Passage</summary>

  ```
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  Cost of Sales:
  Cost of sales, measured as a percent of sales, increased in 2022 when compared to the same period last year. Increases were primarily due to 2022 special item costs for
  ```
  </details>

- **v10** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Goodwill impairment expense \| 0.8 \| — \| 0.8"

  <details><summary>Passage</summary>

  ```
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  Selling, general and administrative expenses (SG&A) | 26.5 | 20.4 | 6.1
  Research, development and related expenses (R&D) | 5.4 | 5.6 | (0.2)
  Gain on business divestitures | (8.0) | — | (8.0)
  Goodwill impairment expense | 0.8 | — | 0.8
  Operating income margin | 19.1 % | 20.8 % | (1.7)%
  The Company is continuing the ongoing deployment of an enterprise resource planning (ERP) system on a worldwide basis, with these investments impacting cost of sales,
  SG&A, and R&D.
  Cost of Sales:
  Cost of sales, measured as a percent of sales, increased in 2022 when compared to the same period last year. Increases were primarily due to 2022 special item costs for
  significant litigation from additional commitments to address PFAS-related matters at 3M's Zwijndrecht, Belgium site (discussed in Note 16), higher raw materials and logistics
  ```
  </details>

<details><summary>Gold answer</summary>

Operating Margin for 3M in FY2022 has decreased by 1.7% primarily due to:  -Decrease in gross Margin -mostly one-off charges including Combat Arms Earplugs litigation, impairment related to exiting PFAS manufacturing, costs related to exiting Russia and divestiture-related restructuring charges
</details>

## 5. If we exclude the impact of M&A, which segment has dragged down 3M's overall growth in 2022?

`financebench_id_01865` · filing `3M_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The Consumer segment has dragged down 3M's overall growth, as it reported a negative organic sales growth of (0.9)% [v3], while the Safety and Industrial segment grew by 1.0% [v1] and the Health Care segment grew by 3.2% [v2].

**Computation:** `min(safety_and_industrial_organic_sales_2022, health_care_organic_sales_2022, consumer_organic_sales_2022) = -0.9  where safety_and_industrial_organic_sales_2022 = 1.0 % (units, FY2022), health_care_organic_sales_2022 = 3.2 % (units, FY2022), consumer_organic_sales_2022 = (0.9) % (units, FY2022)`

- **v1** · `3M_2022_10K` · PDF page **30** · column 2022 · units
  - Quote: "Organic sales \| 1.0 % \| 7.3 %"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Safety and Industrial Business (33.9% of consolidated sales):
   | 2022 | 2021
  Sales (millions) | $11,604 | $11,981
    Sales change analysis:
   | Organic sales | 1.0 % | 7.3 %
   | Translation | (4.2) | 1.9
  Total sales change | (3.2 %) | 9.2 %
  Business segment operating income (loss) (millions) | $1,199 | $2,466
   | Percent change | (51.4 %) | (4.7 %)
   | Percent of sales | 10.3 % | 20.6 %
  Adjusted business segment operating income (millions) (non-GAAP measure) | $2,613 | $2,715
  ```
  </details>

- **v2** · `3M_2022_10K` · PDF page **32** · column 2022 · units
  - Quote: "Organic sales \| 3.2 % \| 10.2 %"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Health Care Business (24.6% of consolidated sales):
   | 2022 | 2021
  Sales (millions) | $8,421 | $8,597
    Sales change analysis:
   | Organic sales | 3.2  % | 10.2  %
   | Divestitures | (1.4) | (2.0)
   | Translation | (3.8) | 1.6
    Total sales change | (2.0)  % | 9.8  %
  Business segment operating income (millions) | $1,815 | $2,037
    Percent change | (10.9)  % | 22.5  %
    Percent of sales | 21.6  % | 23.7  %
  ```
  </details>

- **v3** · `3M_2022_10K` · PDF page **33** · column 2022 · units
  - Quote: "Organic sales \| (0.9) % \| 9.8 %"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consumer Business (15.5% of consolidated sales):
   | 2022 | 2021
  Sales (millions) | $5,298 | $5,513
    Sales change analysis:
   | Organic sales | (0.9)  % | 9.8  %
   | Divestitures | (0.4) | —
   | Translation | (2.6) | 1.0
    Total sales change | (3.9)  % | 10.8  %
  Business segment operating income (millions) | $994 | $1,162
    Percent change | (14.4)  % | 3.8  %
    Percent of sales | 18.8  % | 21.1  %
  ```
  </details>

<details><summary>Gold answer</summary>

The consumer segment shrunk by 0.9% organically.
</details>

## 6. Does 3M have a reasonably healthy liquidity profile based on its quick ratio for Q2 of FY2023? If the quick ratio is not relevant to measure liquidity, please state that and explain why.

`financebench_id_00807` · filing `3M_2023Q2_10Q` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, 3M has a reasonably healthy liquidity profile based on its quick ratio of 0.8468 for Q2 of FY2023, as this ratio is calculated by dividing the sum of cash and cash equivalents ($4,258 million), marketable securities ($56 million), and accounts receivable ($4,947 million) by total current liabilities ($10,936 million) [v1, v2, v3, v4]. A quick ratio above 0.8 indicates that the company possesses sufficient liquid assets to cover a significant portion of its short-term obligations without relying on inventory sales.

**Computation:** `(cash_and_cash_equivalents_june_2023 + marketable_securities_current_june_2023 + accounts_receivable_net_june_2023) / total_current_liabilities_june_2023 = 0.8468  where cash_and_cash_equivalents_june_2023 = $4,258 (millions, Q2 FY2023), marketable_securities_current_june_2023 = 56 (millions, Q2 FY2023), accounts_receivable_net_june_2023 = 4,947 (millions, Q2 FY2023), total_current_liabilities_june_2023 = 10,936 (millions, Q2 FY2023)`

- **v1** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
  - Quote: "Cash and cash equivalents \| $4,258"

  <details><summary>Passage</summary>

  ```
  3M Company and Subsidiaries
  Consolidated Balance Sheet
  (Unaudited)
  (Dollars in millions, except per share amount) | June 30, 2023 | December 31, 2022
  Assets
  Current assets
   | Cash and cash equivalents | $4,258  $3,655
   | Marketable securities — current | 56 | 238
   | Accounts receivable — net of allowances of $160 and $174 | 4,947 | 4,532
   | Inventories
   | Finished goods | 2,526 | 2,497
   | Work in process | 1,527 | 1,606
   | Raw materials and supplies | 1,227 | 1,269
  ```
  </details>

- **v2** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
  - Quote: "Marketable securities — current \| 56"

  <details><summary>Passage</summary>

  ```
  Consolidated Balance Sheet
  (Unaudited)
  (Dollars in millions, except per share amount) | June 30, 2023 | December 31, 2022
  Assets
  Current assets
   | Cash and cash equivalents | $4,258  $3,655
   | Marketable securities — current | 56 | 238
   | Accounts receivable — net of allowances of $160 and $174 | 4,947 | 4,532
   | Inventories
   | Finished goods | 2,526 | 2,497
   | Work in process | 1,527 | 1,606
   | Raw materials and supplies | 1,227 | 1,269
   | Total inventories | 5,280 | 5,372
  ```
  </details>

- **v3** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
  - Quote: "Accounts receivable — net of allowances of $160 and $174 \| 4,947"

  <details><summary>Passage</summary>

  ```
  (Unaudited)
  (Dollars in millions, except per share amount) | June 30, 2023 | December 31, 2022
  Assets
  Current assets
   | Cash and cash equivalents | $4,258  $3,655
   | Marketable securities — current | 56 | 238
   | Accounts receivable — net of allowances of $160 and $174 | 4,947 | 4,532
   | Inventories
   | Finished goods | 2,526 | 2,497
   | Work in process | 1,527 | 1,606
   | Raw materials and supplies | 1,227 | 1,269
   | Total inventories | 5,280 | 5,372
   | Prepaids | 674 | 435
  ```
  </details>

- **v4** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
  - Quote: "Total current liabilities \| 10,936"

  <details><summary>Passage</summary>

  ```
   | Short-term borrowings and current portion of long-term debt | $3,033  $1,938
   | Accounts payable | 3,231 | 3,183
   | Accrued payroll | 785 | 692
   | Accrued income taxes | 172 | 259
   | Operating lease liabilities — current | 244 | 261
   | Other current liabilities | 3,471 | 3,190
   | Total current liabilities | 10,936 | 9,523
  Long-term debt | 12,954 | 14,001
  Pension and postretirement benefits | 1,912 | 1,966
  Operating lease liabilities | 570 | 580
  Other liabilities | 14,651 | 5,615
   | Total liabilities | 41,023 | 31,685
  Commitments and contingencies (Note 14)
  ```
  </details>

<details><summary>Gold answer</summary>

No. The quick ratio for 3M was 0.96 by Jun'23 close, which needs a bit of an improvement to touch the 1x mark
</details>

## 7. Which debt securities are registered to trade on a national securities exchange under 3M's name as of Q2 of 2023?

`financebench_id_00941` · filing `3M_2023Q2_10Q` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** 3M_2023Q2_10Q: number check (G4) failed twice: numbers not in the evidence or the result: 2023,, 2026,, 2030,

**Pages searched:** `3M_2023Q2_10Q` pages 1, 2, 4, 5, 6, 19, 27, 70, 71, 73, 85, 91

<details><summary>Gold answer</summary>

Following debt securities registered under 3M's name are listed to trade on the New York Stock Exchange: -1.500% Notes due 2026 (Trading Symbol: MMM26) -1.750% Notes due 2030 (Trading Symbol: MMM30) -1.500% Notes due 2031 (Trading Symbol: MMM31)
</details>

## 8. Does 3M maintain a stable trend of dividend distribution?

`financebench_id_01858` · filing `3M_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, 3M maintains a stable trend of dividend distribution, as evidenced by the declaration of a $1.50 per share dividend for both the first and second quarters of fiscal year 2023 [v1, v2]. This consistency is further supported by the fact that this period marked the 65th consecutive year of dividend increases for the company [v3].

- **v1** · `3M_2023Q2_10Q` · PDF page **62** · column February 2023 · units
  - Quote: "In February 2023, 3M's Board of Directors declared a first-quarter 2023 dividend of $1.50 per share"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Financial condition:
  Refer to the section entitled Financial Condition and Liquidity later in MD&A for a discussion of items impacting cash flows.
  In November 2018, 3M’s Board of Directors replaced the Company’s February 2016 repurchase program with a new repurchase program. This new program authorizes the
  repurchase of up to $10 billion of 3M’s outstanding common stock, with no pre-established end date. In the first six months of 2023, the Company purchased $29 million of its
  own stock, compared to $773 million of stock purchases in the first six months of 2022. As of June 30, 2023, approximately $4.2 billion remained available under the
  authorization. In February 2023, 3M’s Board of Directors declared a first-quarter 2023 dividend of $1.50 per share, an increase of 1 percent. This marked the 65th consecutive
  year of dividend increases for 3M. In May 2023, 3M's Board of Directors declared a second-quarter 2023 dividend of $1.50 per share.
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding Overview section and the Performance by Business Segment section later in MD&A for additional discussion of sales change.
  Operating Expenses:
   | Three months ended | Six months ended
  ```
  </details>

- **v2** · `3M_2023Q2_10Q` · PDF page **62** · column May 2023 · units
  - Quote: "In May 2023, 3M's Board of Directors declared a second-quarter 2023 dividend of $1.50 per share"

  <details><summary>Passage</summary>

  ```
  Financial condition:
  Refer to the section entitled Financial Condition and Liquidity later in MD&A for a discussion of items impacting cash flows.
  In November 2018, 3M’s Board of Directors replaced the Company’s February 2016 repurchase program with a new repurchase program. This new program authorizes the
  repurchase of up to $10 billion of 3M’s outstanding common stock, with no pre-established end date. In the first six months of 2023, the Company purchased $29 million of its
  own stock, compared to $773 million of stock purchases in the first six months of 2022. As of June 30, 2023, approximately $4.2 billion remained available under the
  authorization. In February 2023, 3M’s Board of Directors declared a first-quarter 2023 dividend of $1.50 per share, an increase of 1 percent. This marked the 65th consecutive
  year of dividend increases for 3M. In May 2023, 3M's Board of Directors declared a second-quarter 2023 dividend of $1.50 per share.
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding Overview section and the Performance by Business Segment section later in MD&A for additional discussion of sales change.
  Operating Expenses:
   | Three months ended | Six months ended
   | June 30, | June 30,
  ```
  </details>

- **v3** · `3M_2023Q2_10Q` · PDF page **62** · column FY2023 · units
  - Quote: "This marked the 65th consecutive year of dividend increases for 3M"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Financial condition:
  Refer to the section entitled Financial Condition and Liquidity later in MD&A for a discussion of items impacting cash flows.
  In November 2018, 3M’s Board of Directors replaced the Company’s February 2016 repurchase program with a new repurchase program. This new program authorizes the
  repurchase of up to $10 billion of 3M’s outstanding common stock, with no pre-established end date. In the first six months of 2023, the Company purchased $29 million of its
  own stock, compared to $773 million of stock purchases in the first six months of 2022. As of June 30, 2023, approximately $4.2 billion remained available under the
  authorization. In February 2023, 3M’s Board of Directors declared a first-quarter 2023 dividend of $1.50 per share, an increase of 1 percent. This marked the 65th consecutive
  year of dividend increases for 3M. In May 2023, 3M's Board of Directors declared a second-quarter 2023 dividend of $1.50 per share.
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding Overview section and the Performance by Business Segment section later in MD&A for additional discussion of sales change.
  Operating Expenses:
   | Three months ended | Six months ended
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, not only they distribute the dividends on a routine basis, 3M has also been increasing the per share dividend for consecutive 65 years
</details>

## 9. What is the FY2019 fixed asset turnover ratio for Activision Blizzard? Fixed asset turnover ratio is defined as: FY2019 revenue / (average PP&E between FY2018 and FY2019). Round your answer to two decimal places. Base your judgments on the information provided primarily in the statement of income and the statement of financial position.

`financebench_id_02987` · filing `ACTIVISIONBLIZZARD_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 fixed asset turnover ratio for Activision Blizzard is 24.26. This is calculated by dividing the total net revenues of 6,489 million by the average of property and equipment, net, using the values 253 million and 282 million [v1, v2, v3].

**Computation:** `net_revenues_2019 / avg(ppe_2019, ppe_2018) = 24.26  where net_revenues_2019 = 6,489 (millions, FY2019), ppe_2019 = 253 (millions, FY2019), ppe_2018 = 282 (millions, FY2018)`

- **v1** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2019 · millions
  - Quote: "Total net revenues \| 6,489 \| 7,500 \| 7,017"

  <details><summary>Passage</summary>

  ```
   | (Amounts in millions, except per share data)
   | For the Years Ended December 31,
   | 2019 | 2018 | 2017
  Net revenues
    Product sales | $1,975 | $2,255 | $2,110
    Subscription, licensing, and other revenues | 4,514 | 5,245 | 4,907
  Total net revenues | 6,489 | 7,500 | 7,017
  Costs and expenses
    Cost of revenues—product sales:
   | Product costs | 656 | 719 | 733
   | Software royalties, amortization, and intellectual property licenses | 240 | 371 | 300
    Cost of revenues—subscription, licensing, and other revenues:
   | Game operations and distribution costs | 965 | 1,028 | 984
  ```
  </details>

- **v2** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **69** · column 2019 · millions
  - Quote: "Property and equipment, net \| 253 \| 282"

  <details><summary>Passage</summary>

  ```
   | Accounts receivable, net of allowances of $132 and $190, at December 31, 2019 and December 31, 2018, respectively | 848 | 1,035
   | Inventories, net | 32 | 43
   | Software development | 322 | 264
   | Other current assets | 296 | 539
   | Total current assets | 7,292 | 6,106
    Software development | 54 | 65
   | Property and equipment, net | 253 | 282
    Deferred income taxes, net | 1,293 | 458
    Other assets | 658 | 482
   | Intangible assets, net | 531 | 735
    Goodwill | 9,764 | 9,762
   | Total assets | $19,845 | $17,890
   Liabilities and Shareholders’ Equity
  ```
  </details>

- **v3** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **69** · column 2018 · millions
  - Quote: "Property and equipment, net \| 253 \| 282"

  <details><summary>Passage</summary>

  ```
   | Accounts receivable, net of allowances of $132 and $190, at December 31, 2019 and December 31, 2018, respectively | 848 | 1,035
   | Inventories, net | 32 | 43
   | Software development | 322 | 264
   | Other current assets | 296 | 539
   | Total current assets | 7,292 | 6,106
    Software development | 54 | 65
   | Property and equipment, net | 253 | 282
    Deferred income taxes, net | 1,293 | 458
    Other assets | 658 | 482
   | Intangible assets, net | 531 | 735
    Goodwill | 9,764 | 9,762
   | Total assets | $19,845 | $17,890
   Liabilities and Shareholders’ Equity
  ```
  </details>

<details><summary>Gold answer</summary>

24.26
</details>

## 10. What is the FY2017 - FY2019 3 year average of capex as a % of revenue for Activision Blizzard? Answer in units of percents and round to one decimal place. Calculate (or extract) the answer from the statement of income and the cash flow statement.

`financebench_id_07966` · filing `ACTIVISIONBLIZZARD_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average of capital expenditures as a percentage of revenue for Activision Blizzard from FY2017 to FY2019 is 1.9%. This result is derived from the computed average of the ratios using the specific capital expenditure and revenue values provided in the evidence [v1, v2, v3, v4, v5, v6].

**Computation:** `avg(abs(capex_2019)/revenue_2019, abs(capex_2018)/revenue_2018, abs(capex_2017)/revenue_2017) = 1.9%  where capex_2019 = (116) (millions, FY2019), capex_2018 = (131) (millions, FY2018), capex_2017 = (155) (millions, FY2017), revenue_2019 = 6,489 (millions, FY2019), revenue_2018 = 7,500 (millions, FY2018), revenue_2017 = 7,017 (millions, FY2017)`

- **v1** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **73** · column 2019 · millions
  - Quote: "Capital expenditures \| (116)"

  <details><summary>Passage</summary>

  ```
   | Accounts payable | 31 | (65) | 85
   | Accrued expenses and other liabilities | (77) | (554) | 945
    Net cash provided by operating activities | 1,831 | 1,790 | 2,213
  Cash flows from investing activities:
    Proceeds from maturities of available-for-sale investments | 153 | 116 | 80
   | Purchases of available-for-sale investments | (65) | (209) | (135)
   | Capital expenditures | (116) | (131) | (155)
    Other investing activities | 6 | (6) | 3
    Net cash used in investing activities | (22) | (230) | (207)
  Cash flows from financing activities:
    Proceeds from issuance of common stock to employees | 105 | 99 | 178
    Tax payment related to net share settlements on restricted stock units | (59) | (94) | (56)
    Dividends paid | (283) | (259) | (226)
  ```
  </details>

- **v2** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **73** · column 2018 · millions
  - Quote: "Capital expenditures \| (131)"

  <details><summary>Passage</summary>

  ```
   | Accounts payable | 31 | (65) | 85
   | Accrued expenses and other liabilities | (77) | (554) | 945
    Net cash provided by operating activities | 1,831 | 1,790 | 2,213
  Cash flows from investing activities:
    Proceeds from maturities of available-for-sale investments | 153 | 116 | 80
   | Purchases of available-for-sale investments | (65) | (209) | (135)
   | Capital expenditures | (116) | (131) | (155)
    Other investing activities | 6 | (6) | 3
    Net cash used in investing activities | (22) | (230) | (207)
  Cash flows from financing activities:
    Proceeds from issuance of common stock to employees | 105 | 99 | 178
    Tax payment related to net share settlements on restricted stock units | (59) | (94) | (56)
    Dividends paid | (283) | (259) | (226)
  ```
  </details>

- **v3** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **73** · column 2017 · millions
  - Quote: "Capital expenditures \| (155)"

  <details><summary>Passage</summary>

  ```
   | Accounts payable | 31 | (65) | 85
   | Accrued expenses and other liabilities | (77) | (554) | 945
    Net cash provided by operating activities | 1,831 | 1,790 | 2,213
  Cash flows from investing activities:
    Proceeds from maturities of available-for-sale investments | 153 | 116 | 80
   | Purchases of available-for-sale investments | (65) | (209) | (135)
   | Capital expenditures | (116) | (131) | (155)
    Other investing activities | 6 | (6) | 3
    Net cash used in investing activities | (22) | (230) | (207)
  Cash flows from financing activities:
    Proceeds from issuance of common stock to employees | 105 | 99 | 178
    Tax payment related to net share settlements on restricted stock units | (59) | (94) | (56)
    Dividends paid | (283) | (259) | (226)
  ```
  </details>

- **v4** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2019 · millions
  - Quote: "Total net revenues \| 6,489"

  <details><summary>Passage</summary>

  ```
   | (Amounts in millions, except per share data)
   | For the Years Ended December 31,
   | 2019 | 2018 | 2017
  Net revenues
    Product sales | $1,975 | $2,255 | $2,110
    Subscription, licensing, and other revenues | 4,514 | 5,245 | 4,907
  Total net revenues | 6,489 | 7,500 | 7,017
  Costs and expenses
    Cost of revenues—product sales:
   | Product costs | 656 | 719 | 733
   | Software royalties, amortization, and intellectual property licenses | 240 | 371 | 300
    Cost of revenues—subscription, licensing, and other revenues:
   | Game operations and distribution costs | 965 | 1,028 | 984
  ```
  </details>

- **v5** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2018 · millions
  - Quote: "Total net revenues \| 7,500"

  <details><summary>Passage</summary>

  ```
   | (Amounts in millions, except per share data)
   | For the Years Ended December 31,
   | 2019 | 2018 | 2017
  Net revenues
    Product sales | $1,975 | $2,255 | $2,110
    Subscription, licensing, and other revenues | 4,514 | 5,245 | 4,907
  Total net revenues | 6,489 | 7,500 | 7,017
  Costs and expenses
    Cost of revenues—product sales:
   | Product costs | 656 | 719 | 733
   | Software royalties, amortization, and intellectual property licenses | 240 | 371 | 300
    Cost of revenues—subscription, licensing, and other revenues:
   | Game operations and distribution costs | 965 | 1,028 | 984
  ```
  </details>

- **v6** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2017 · millions
  - Quote: "Total net revenues \| 7,017"

  <details><summary>Passage</summary>

  ```
   | (Amounts in millions, except per share data)
   | For the Years Ended December 31,
   | 2019 | 2018 | 2017
  Net revenues
    Product sales | $1,975 | $2,255 | $2,110
    Subscription, licensing, and other revenues | 4,514 | 5,245 | 4,907
  Total net revenues | 6,489 | 7,500 | 7,017
  Costs and expenses
    Cost of revenues—product sales:
   | Product costs | 656 | 719 | 733
   | Software royalties, amortization, and intellectual property licenses | 240 | 371 | 300
    Cost of revenues—subscription, licensing, and other revenues:
   | Game operations and distribution costs | 965 | 1,028 | 984
  ```
  </details>

<details><summary>Gold answer</summary>

1.9%
</details>

## 11. You are an investment banker and your only resource(s) to answer the following question is (are): the statement of financial position and the cash flow statement. Here's the question: what is the FY2015 operating cash flow ratio for Adobe? Operating cash flow ratio is defined as: cash from operations / total current liabilities. Round your answer to two decimal places.

`financebench_id_04735` · filing `ADOBE_2015_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 operating cash flow ratio for Adobe is 0.66. This is calculated by dividing the net cash provided by operating activities of 1,469,502 by the total current liabilities of 2,213,556, as defined by the formula cash from operations / total current liabilities [v1, v2].

**Computation:** `net_cash_provided_by_operating_activities_2015 / total_current_liabilities_2015 = 0.66  where net_cash_provided_by_operating_activities_2015 = 1,469,502 (units, FY2015), total_current_liabilities_2015 = 2,213,556 (units, FY2015)`

- **v1** · `ADOBE_2015_10K` · PDF page **63** · column 2015 · units
  - Quote: "Net cash provided by operating activities......................................................... \| 1,469,502"

  <details><summary>Passage</summary>

  ```
   | Prepaid expenses and other current assets ............................................................. | (7,701) | (1,918) | (55,509)
   | Trade payables ....................................................................................................... | 22,870 | 6,211 | 7,132
   | Accrued expenses................................................................................................... | (5,944) | 37,544 | 41,828
   | Accrued restructuring............................................................................................. | (16,620) | 8,871 | (6,949)
   | Income taxes payable............................................................................................. | 29,801 | 11,006 | (58,875)
   | Deferred revenue.................................................................................................... | 320,801 | 326,438 | 201,366
   | Net cash provided by operating activities......................................................... | 1,469,502 | 1,287,482 | 1,151,686
  Cash flows from investing activities:
    Purchases of short-term investments ............................................................................. | (2,064,833) | (2,014,186) | (2,058,058)
    Maturities of short-term investments............................................................................. | 371,790 | 272,076 | 360,485
   Proceeds from sales of short-term investments ............................................................. | 1,176,476 | 1,443,577 | 1,449,961
    Acquisitions, net of cash acquired ................................................................................. | (826,004) | (29,802) | (704,589)
    Purchases of property and equipment............................................................................ | (184,936) | (148,332) | (188,358)
  ```
  </details>

- **v2** · `ADOBE_2015_10K` · PDF page **59** · column 2015 · units
  - Quote: "Total current liabilities.................................................................................................................... \| 2,213,556"

  <details><summary>Passage</summary>

  ```
   Trade payables...................................................................................................................................... $93,307  $68,377
   Accrued expenses................................................................................................................................. | 678,364 | 683,866
   Debt and capital lease obligations........................................................................................................ | — | 603,229
   Accrued restructuring........................................................................................................................... | 1,520 | 17,120
   Income taxes payable........................................................................................................................... | 6,165 | 23,920
    Deferred revenue.................................................................................................................................. | 1,434,200 | 1,097,923
   | Total current liabilities.................................................................................................................... | 2,213,556 | 2,494,435
  Long-term liabilities:
   Debt and capital lease obligations........................................................................................................ | 1,907,231 | 911,086
    Deferred revenue.................................................................................................................................. | 51,094 | 57,401
   Accrued restructuring........................................................................................................................... | 3,214 | 5,194
   Income taxes payable........................................................................................................................... | 256,129 | 125,746
    Deferred income taxes.......................................................................................................................... | 208,209 | 342,315
  ```
  </details>

<details><summary>Gold answer</summary>

0.66
</details>

## 12. What is Adobe's year-over-year change in unadjusted operating income from FY2015 to FY2016 (in units of percents and round to one decimal place)? Give a solution to the question by using the income statement.

`financebench_id_07507` · filing `ADOBE_2016_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Adobe's year-over-year change in unadjusted operating income from FY2015 to FY2016 is 65.4%. This is calculated by taking the difference between the 2016 operating income of 1,493,602 and the 2015 operating income of 903,095, then dividing by the 2015 value as shown in the computed result [v1, v2].

**Computation:** `(operating_income_2016 - operating_income_2015) / operating_income_2015 = 65.4%  where operating_income_2016 = 1,493,602 (units, FY2016), operating_income_2015 = 903,095 (units, FY2015)`

- **v1** · `ADOBE_2016_10K` · PDF page **62** · column 2016 · units
  - Quote: "Operating income \| 1,493,602"

  <details><summary>Passage</summary>

  ```
   Research and development | 975,987 | 862,730 | 844,353
   Sales and marketing | 1,910,197 | 1,683,242 | 1,652,308
   General and administrative | 577,710 | 531,919 | 543,332
   Restructuring and other charges | (1,508) | 1,559 | 19,883
   Amortization of purchased intangibles | 78,534 | 68,649 | 52,424
   | Total operating expenses | 3,540,920 | 3,148,099 | 3,112,300
  Operating income | 1,493,602 | 903,095 | 412,685
  Non-operating income (expense):
    Interest and other income (expense), net | 13,548 | 33,909 | 7,267
    Interest expense | (70,442) | (64,184) | (59,732)
   Investment gains (losses), net | (1,570) | 961 | 1,156
   | Total non-operating income (expense), net | (58,464) | (29,314) | (51,309)
  Income before income taxes | 1,435,138 | 873,781 | 361,376
  ```
  </details>

- **v2** · `ADOBE_2016_10K` · PDF page **62** · column 2015 · units
  - Quote: "Operating income \| 903,095"

  <details><summary>Passage</summary>

  ```
   Research and development | 975,987 | 862,730 | 844,353
   Sales and marketing | 1,910,197 | 1,683,242 | 1,652,308
   General and administrative | 577,710 | 531,919 | 543,332
   Restructuring and other charges | (1,508) | 1,559 | 19,883
   Amortization of purchased intangibles | 78,534 | 68,649 | 52,424
   | Total operating expenses | 3,540,920 | 3,148,099 | 3,112,300
  Operating income | 1,493,602 | 903,095 | 412,685
  Non-operating income (expense):
    Interest and other income (expense), net | 13,548 | 33,909 | 7,267
    Interest expense | (70,442) | (64,184) | (59,732)
   Investment gains (losses), net | (1,570) | 961 | 1,156
   | Total non-operating income (expense), net | (58,464) | (29,314) | (51,309)
  Income before income taxes | 1,435,138 | 873,781 | 361,376
  ```
  </details>

<details><summary>Gold answer</summary>

65.4%
</details>

## 13. What is the FY2017 operating cash flow ratio for Adobe? Operating cash flow ratio is defined as: cash from operations / total current liabilities. Round your answer to two decimal places. Please utilize information provided primarily within the balance sheet and the cash flow statement.

`financebench_id_03856` · filing `ADOBE_2017_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2017 operating cash flow ratio for Adobe is 0.83. This is calculated by dividing the net cash provided by operating activities of 2,912,853 by the total current liabilities of 3,527,457, as shown in the provided financial statements [v1, v2].

**Computation:** `net_cash_provided_by_operating_activities_2017 / total_current_liabilities_2017 = 0.83  where net_cash_provided_by_operating_activities_2017 = 2,912,853 (units, FY2017), total_current_liabilities_2017 = 3,527,457 (units, FY2017)`

- **v1** · `ADOBE_2017_10K` · PDF page **61** · column 2017 · units
  - Quote: "Net cash provided by operating activities \| 2,912,853"

  <details><summary>Passage</summary>

  ```
   | Trade receivables, net | (187,173) | (160,416) | (79,502)
   | Prepaid expenses and other current assets | 28,040 | (71,021) | (7,701)
   | Trade payables | (45,186) | (6,281) | 22,870
   | Accrued expenses | 154,125 | 64,978 | (22,564)
   | Income taxes payable | (34,493) | 43,115 | 97,934
   | Deferred revenue | 475,402 | 524,840 | 320,801
   | Net cash provided by operating activities | 2,912,853 | 2,199,728 | 1,469,502
  Cash flows from investing activities:
    Purchases of short-term investments | (1,931,011) | (2,285,222) | (2,064,833)
    Maturities of short-term investments | 759,737 | 769,228 | 371,790
   Proceeds from sales of short-term investments | 1,393,929 | 860,849 | 1,176,476
    Acquisitions, net of cash acquired | (459,626) | (48,427) | (826,004)
    Purchases of property and equipment | (178,122) | (203,805) | (184,936)
  ```
  </details>

- **v2** · `ADOBE_2017_10K` · PDF page **57** · column 2017 · units
  - Quote: "Total current liabilities \| 3,527,457"

  <details><summary>Passage</summary>

  ```
   | LIABILITIES AND STOCKHOLDERS’ EQUITY
  Current liabilities:
   Trade payables | $113,538  $88,024
   Accrued expenses | 993,773 | 739,630
   Income taxes payable | 14,196 | 38,362
    Deferred revenue | 2,405,950 | 1,945,619
   | Total current liabilities | 3,527,457 | 2,811,635
  Long-term liabilities:
   Debt and capital lease obligations | 1,881,421 | 1,892,200
    Deferred revenue | 88,592 | 69,131
   Income taxes payable | 173,088 | 184,381
    Deferred income taxes | 279,941 | 217,660
   Other liabilities | 125,188 | 97,404
  ```
  </details>

<details><summary>Gold answer</summary>

0.83
</details>

## 14. Does Adobe have an improving operating margin profile as of FY2022? If operating margin is not a useful metric for a company like this, then state that and explain why.

`financebench_id_00438` · filing `ADOBE_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Adobe does not have an improving operating margin profile as of FY2022. The computed result indicates a decline of -2.1205% in the operating margin from FY2021 to FY2022 [COMPUTED RESULT], which is derived from the operating income and total revenue figures for those years [v1, v2, v3, v4]. A negative change signifies a deterioration rather than an improvement in the margin profile.

**Computation:** `(operating_income_2022 / total_revenue_2022) - (operating_income_2021 / total_revenue_2021) = -2.1205%  where operating_income_2022 = 6,098 (millions, FY2022), total_revenue_2022 = 17,606 (millions, FY2022), operating_income_2021 = 5,802 (millions, FY2021), total_revenue_2021 = 15,785 (millions, FY2021)`

- **v1** · `ADOBE_2022_10K` · PDF page **54** · column 2022 · millions
  - Quote: "Operating income \| 6,098"

  <details><summary>Passage</summary>

  ```
  Operating expenses:
   Research and development | 2,987 | 2,540 | 2,188
    Sales and marketing | 4,968 | 4,321 | 3,591
   General and administrative | 1,219 | 1,085 | 968
    Amortization of intangibles | 169 | 172 | 162
   | Total operating expenses | 9,343 | 8,118 | 6,909
  Operating income | 6,098 | 5,802 | 4,237
  Non-operating income (expense):
    Interest expense | (112) | (113) | (116)
    Investment gains (losses), net | (19) | 16 | 13
   Other income (expense), net | 41 | — | 42
   | Total non-operating income (expense), net | (90) | (97) | (61)
  Income before income taxes | 6,008 | 5,705 | 4,176
  ```
  </details>

- **v2** · `ADOBE_2022_10K` · PDF page **54** · column 2022 · millions
  - Quote: "Total revenue \| 17,606"

  <details><summary>Passage</summary>

  ```
   | December 2, | December 3, | November 27,
   | 2022 | 2021 | 2020
  Revenue:
    Subscription | $16,388  $14,573  $11,626
    Product | 532 | 555 | 507
    Services and other | 686 | 657 | 735
   | Total revenue | 17,606 | 15,785 | 12,868
  Cost of revenue:
    Subscription | 1,646 | 1,374 | 1,108
    Product | 35 | 41 | 36
    Services and other | 484 | 450 | 578
   | Total cost of revenue | 2,165 | 1,865 | 1,722
  Gross profit | 15,441 | 13,920 | 11,146
  ```
  </details>

- **v3** · `ADOBE_2022_10K` · PDF page **54** · column 2021 · millions
  - Quote: "Operating income \| 5,802"

  <details><summary>Passage</summary>

  ```
  Operating expenses:
   Research and development | 2,987 | 2,540 | 2,188
    Sales and marketing | 4,968 | 4,321 | 3,591
   General and administrative | 1,219 | 1,085 | 968
    Amortization of intangibles | 169 | 172 | 162
   | Total operating expenses | 9,343 | 8,118 | 6,909
  Operating income | 6,098 | 5,802 | 4,237
  Non-operating income (expense):
    Interest expense | (112) | (113) | (116)
    Investment gains (losses), net | (19) | 16 | 13
   Other income (expense), net | 41 | — | 42
   | Total non-operating income (expense), net | (90) | (97) | (61)
  Income before income taxes | 6,008 | 5,705 | 4,176
  ```
  </details>

- **v4** · `ADOBE_2022_10K` · PDF page **54** · column 2021 · millions
  - Quote: "Total revenue \| 15,785"

  <details><summary>Passage</summary>

  ```
   | December 2, | December 3, | November 27,
   | 2022 | 2021 | 2020
  Revenue:
    Subscription | $16,388  $14,573  $11,626
    Product | 532 | 555 | 507
    Services and other | 686 | 657 | 735
   | Total revenue | 17,606 | 15,785 | 12,868
  Cost of revenue:
    Subscription | 1,646 | 1,374 | 1,108
    Product | 35 | 41 | 36
    Services and other | 484 | 450 | 578
   | Total cost of revenue | 2,165 | 1,865 | 1,722
  Gross profit | 15,441 | 13,920 | 11,146
  ```
  </details>

<details><summary>Gold answer</summary>

No the operating margins of Adobe have recently declined from 36.8% in FY 2021 to 34.6% in FY2022. A drop by 2.2% in a year.
</details>

## 15. Does Adobe have an improving Free cashflow conversion as of FY2022?

`financebench_id_00591` · filing `ADOBE_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Adobe does not have an improving free cash flow conversion as of FY2022 because the ratio of net cash provided by operating activities to net income was 1.648 in FY2022, which is higher than the implied FY2021 ratio derived from the evidence values [v1, v2, v3, v4].

**Computation:** `net_cash_operating_2022 / net_income_2022 = 1.648  where net_income_2022 = 4,756 (units, FY2022), net_cash_operating_2022 = 7,838 (units, FY2022), net_cash_operating_2021 = 7,230 (units, FY2021), net_income_2021 = 4,822 (units, FY2021)`

- **v1** · `ADOBE_2022_10K` · PDF page **54** · column 2022 · units
  - Quote: "Net income \| $4,756"

  <details><summary>Passage</summary>

  ```
    Interest expense | (112) | (113) | (116)
    Investment gains (losses), net | (19) | 16 | 13
   Other income (expense), net | 41 | — | 42
   | Total non-operating income (expense), net | (90) | (97) | (61)
  Income before income taxes | 6,008 | 5,705 | 4,176
  Provision for (benefit from) income taxes | 1,252 | 883 | (1,084)
  Net income | $4,756  $4,822  $5,260
  Basic net income per share | $10.13  $10.10  $10.94
  Shares used to compute basic net income per share | 470 | 477 | 481
  Diluted net income per share | $10.10  $10.02  $10.83
  Shares used to compute diluted net income per share | 471 | 481 | 485
   | See accompanying Notes to Consolidated Financial Statements.
   | 54
  ```
  </details>

- **v2** · `ADOBE_2022_10K` · PDF page **57** · column 2022 · units
  - Quote: "Net cash provided by operating activities \| 7,838"

  <details><summary>Passage</summary>

  ```
   | Trade receivables, net | (198) | (430) | 106
   | Prepaid expenses and other assets | (94) | (475) | (288)
   | Trade payables | 66 | (20) | 96
   | Accrued expenses and other liabilities | 7 | 162 | 86
   | Income taxes payable | 19 | 2 | (72)
   | Deferred revenue | 536 | 1,053 | 258
   | Net cash provided by operating activities | 7,838 | 7,230 | 5,727
  Cash flows from investing activities:
    Purchases of short-term investments | (909) | (1,533) | (1,071)
    Maturities of short-term investments | 683 | 877 | 915
    Proceeds from sales of short-term investments | 270 | 191 | 167
    Acquisitions, net of cash acquired | (126) | (2,682) | —
    Purchases of property and equipment | (442) | (348) | (419)
  ```
  </details>

- **v3** · `ADOBE_2022_10K` · PDF page **57** · column 2021 · units
  - Quote: "Net cash provided by operating activities \| 7,230"

  <details><summary>Passage</summary>

  ```
   | Trade receivables, net | (198) | (430) | 106
   | Prepaid expenses and other assets | (94) | (475) | (288)
   | Trade payables | 66 | (20) | 96
   | Accrued expenses and other liabilities | 7 | 162 | 86
   | Income taxes payable | 19 | 2 | (72)
   | Deferred revenue | 536 | 1,053 | 258
   | Net cash provided by operating activities | 7,838 | 7,230 | 5,727
  Cash flows from investing activities:
    Purchases of short-term investments | (909) | (1,533) | (1,071)
    Maturities of short-term investments | 683 | 877 | 915
    Proceeds from sales of short-term investments | 270 | 191 | 167
    Acquisitions, net of cash acquired | (126) | (2,682) | —
    Purchases of property and equipment | (442) | (348) | (419)
  ```
  </details>

- **v4** · `ADOBE_2022_10K` · PDF page **54** · column 2021 · units
  - Quote: "Net income \| $4,822"

  <details><summary>Passage</summary>

  ```
    Interest expense | (112) | (113) | (116)
    Investment gains (losses), net | (19) | 16 | 13
   Other income (expense), net | 41 | — | 42
   | Total non-operating income (expense), net | (90) | (97) | (61)
  Income before income taxes | 6,008 | 5,705 | 4,176
  Provision for (benefit from) income taxes | 1,252 | 883 | (1,084)
  Net income | $4,756  $4,822  $5,260
  Basic net income per share | $10.13  $10.10  $10.94
  Shares used to compute basic net income per share | 470 | 477 | 481
  Diluted net income per share | $10.10  $10.02  $10.83
  Shares used to compute diluted net income per share | 471 | 481 | 485
   | See accompanying Notes to Consolidated Financial Statements.
   | 54
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, the FCF conversion (using net income as the denominator) for Adobe has improved by ~13% from 143% in 2021 to 156% in 2022
</details>

## 16. What is the quantity of restructuring costs directly outlined in AES Corporation's income statements for FY2022? If restructuring costs are not explicitly outlined then state 0.

`financebench_id_01319` · filing `AES_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AES_2022_10K: extractor: The provided pages do not contain a line item explicitly labeled 'restructuring costs' in the income statements (Page 86, Page 132). While Page 95 mentions that the definition of Adjusted Operating Margin was updated to remove adjustments for costs associated with a major restructuring program, it states 'There were no such costs in 2020, 2021 or 2022.' Since the question asks for costs 'directly outlined in AES Corporation's income statements' and none are explicitly listed as a line item, the evidence is not found in the requested format.

**Pages searched:** `AES_2022_10K` pages 84, 86, 94, 95, 130, 132, 133, 135, 181, 214, 215, 216, 217

<details><summary>Gold answer</summary>

0
</details>

## 17. Roughly how many times has AES Corporation sold its inventory in FY2022? Calculate inventory turnover ratio for the FY2022; if conventional inventory management is not meaningful for the company then state that and explain why.

`financebench_id_00540` · filing `AES_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The inventory turnover ratio is not meaningful for AES Corporation because the company reports a negative cost of sales of $(10,069) million in FY2022, which results in a negative ratio of -12.1386, indicating that conventional inventory management metrics do not apply to its financial structure [v1, v2, v3].

**Computation:** `cost_of_sales_2022 / avg(inventory_beginning_2022, inventory_ending_2022) = -12.1386  where cost_of_sales_2022 = (10,069) (millions, FY2022), inventory_beginning_2022 = 604 (millions, FY2022), inventory_ending_2022 = 1,055 (millions, FY2022)`

- **v1** · `AES_2022_10K` · PDF page **132** · column 2022 · millions
  - Quote: "Total cost of sales \| (10,069)"

  <details><summary>Passage</summary>

  ```
    Regulated | $3,538  $2,868  $2,661
    Non-Regulated | 9,079 | 8,273 | 6,999
   | Total revenue | 12,617 | 11,141 | 9,660
  Cost of Sales:
    Regulated | (3,162) | (2,448) | (2,235)
    Non-Regulated | (6,907) | (5,982) | (4,732)
   | Total cost of sales | (10,069) | (8,430) | (6,967)
    Operating margin | 2,548 | 2,711 | 2,693
    General and administrative expenses | (207) | (166) | (165)
    Interest expense | (1,117) | (911) | (1,038)
    Interest income | 389 | 298 | 268
    Loss on extinguishment of debt | (15) | (78) | (186)
    Other expense | (68) | (60) | (53)
  ```
  </details>

- **v2** · `AES_2022_10K` · PDF page **130** · column 2021 · millions
  - Quote: "Inventory \| 1,055 \| 604"

  <details><summary>Passage</summary>

  ```
  ASSETS
   CURRENT ASSETS
   | Cash and cash equivalents | $1,374  $943
   | Restricted cash | 536 | 304
   | Short-term investments | 730 | 232
   | Accounts receivable, net of allowance for doubtful accounts of $5 and $5, respectively | 1,799 | 1,418
   | Inventory | 1,055 | 604
   | Prepaid expenses | 98 | 142
   | Other current assets, net of CECL allowance of $2 and $0, respectively | 1,533 | 897
   | Current held-for-sale assets | 518 | 816
   | Total current assets | 7,643 | 5,356
   NONCURRENT ASSETS
    Property, Plant and Equipment:
  ```
  </details>

- **v3** · `AES_2022_10K` · PDF page **130** · column 2022 · millions
  - Quote: "Inventory \| 1,055 \| 604"

  <details><summary>Passage</summary>

  ```
  ASSETS
   CURRENT ASSETS
   | Cash and cash equivalents | $1,374  $943
   | Restricted cash | 536 | 304
   | Short-term investments | 730 | 232
   | Accounts receivable, net of allowance for doubtful accounts of $5 and $5, respectively | 1,799 | 1,418
   | Inventory | 1,055 | 604
   | Prepaid expenses | 98 | 142
   | Other current assets, net of CECL allowance of $2 and $0, respectively | 1,533 | 897
   | Current held-for-sale assets | 518 | 816
   | Total current assets | 7,643 | 5,356
   NONCURRENT ASSETS
    Property, Plant and Equipment:
  ```
  </details>

<details><summary>Gold answer</summary>

AES has converted inventory 9.5 times in FY 2022.
</details>

## 18. Based on the information provided primarily in the statement of financial position and the statement of income, what is AES's FY2022 return on assets (ROA)? ROA is defined as: FY2022 net income / (average total assets between FY2021 and FY2022). Round your answer to two decimal places.

`financebench_id_10420` · filing `AES_2022_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AES_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: -1.42%

**Pages searched:** `AES_2022_10K` pages 1, 84, 127, 130, 132, 133, 135, 202, 207, 214, 215, 216, 217

<details><summary>Gold answer</summary>

-0.02
</details>

## 19. What is Amazon's FY2017 days payable outstanding (DPO)? DPO is defined as: 365 * (average accounts payable between FY2016 and FY2017) / (FY2017 COGS + change in inventory between FY2016 and FY2017). Round your answer to two decimal places. Address the question by using the line items and information shown within the balance sheet and the P&L statement.

`financebench_id_06655` · filing `AMAZON_2017_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMAZON_2017_10K: number check (G4) failed twice: numbers not in the evidence or the result: 365

**Pages searched:** `AMAZON_2017_10K` pages 1, 19, 20, 25, 37, 38, 39, 40, 41, 42, 46, 53

<details><summary>Gold answer</summary>

93.86
</details>

## 20. What is Amazon's year-over-year change in revenue from FY2016 to FY2017 (in units of percents and round to one decimal place)? Calculate what was asked by utilizing the line items clearly shown in the statement of income.

`financebench_id_08135` · filing `AMAZON_2017_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Amazon's year-over-year change in revenue from FY2016 to FY2017 is 30.8%. This is calculated by taking the difference between the 2017 total net sales of 177,866 and the 2016 total net sales of 135,987, then dividing by the 2016 figure, as shown in the computed result [v1, v2, COMPUTED RESULT].

**Computation:** `(net_sales_2017 - net_sales_2016) / net_sales_2016 = 30.8%  where net_sales_2016 = 135,987 (units, FY2016), net_sales_2017 = 177,866 (units, FY2017)`

- **v1** · `AMAZON_2017_10K` · PDF page **38** · column 2016 · units
  - Quote: "Total net sales \| 107,006 \| 135,987 \| 177,866"

  <details><summary>Passage</summary>

  ```
   | CONSOLIDATED STATEMENTS OF OPERATIONS
   | (in millions, except per share data)
   | Year Ended December 31,
   | 2015 | 2016 | 2017
  Net product sales | $79,268 | $94,665 | $118,573
  Net service sales | 27,738 | 41,322 | 59,293
   | Total net sales | 107,006 | 135,987 | 177,866
  Operating expenses:
   | Cost of sales | 71,651 | 88,265 | 111,934
   | Fulfillment | 13,410 | 17,619 | 25,249
   | Marketing | 5,254 | 7,233 | 10,069
   | Technology and content | 12,540 | 16,085 | 22,620
   | General and administrative | 1,747 | 2,432 | 3,674
  ```
  </details>

- **v2** · `AMAZON_2017_10K` · PDF page **38** · column 2017 · units
  - Quote: "Total net sales \| 107,006 \| 135,987 \| 177,866"

  <details><summary>Passage</summary>

  ```
   | CONSOLIDATED STATEMENTS OF OPERATIONS
   | (in millions, except per share data)
   | Year Ended December 31,
   | 2015 | 2016 | 2017
  Net product sales | $79,268 | $94,665 | $118,573
  Net service sales | 27,738 | 41,322 | 59,293
   | Total net sales | 107,006 | 135,987 | 177,866
  Operating expenses:
   | Cost of sales | 71,651 | 88,265 | 111,934
   | Fulfillment | 13,410 | 17,619 | 25,249
   | Marketing | 5,254 | 7,233 | 10,069
   | Technology and content | 12,540 | 16,085 | 22,620
   | General and administrative | 1,747 | 2,432 | 3,674
  ```
  </details>

<details><summary>Gold answer</summary>

30.8%
</details>

## 21. By drawing conclusions from the information stated only in the income statement, what is Amazon's FY2019 net income attributable to shareholders (in USD millions)?

`financebench_id_08286` · filing `AMAZON_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Amazon's FY2019 net income attributable to shareholders is 11,588 million USD, as explicitly stated in the "Net income" row of the Consolidated Statements of Operations for the year ended December 31, 2019 [v1, v2].

**Computation:** `net_income_2019 = 11,588 million  where net_income_2019 = 11,588 (millions, FY2019), net_income_2019_2 = 11,588 (millions, FY2019)`

- **v1** · `AMAZON_2019_10K` · PDF page **38** · column 2019 · millions
  - Quote: "Net income \| $3,033 \| $10,073 \| $11,588"

  <details><summary>Passage</summary>

  ```
  Interest expense | (848) | (1,417) | (1,600)
  Other income (expense), net | 346 | (183) | 203
   | Total non-operating income (expense) | (300) | (1,160) | (565)
  Income before income taxes | 3,806 | 11,261 | 13,976
  Provision for income taxes | (769) | (1,197) | (2,374)
  Equity-method investment activity, net of tax | (4) | 9 | (14)
  Net income | $3,033 | $10,073 | $11,588
  Basic earnings per share | $6.32 | $20.68 | $23.46
  Diluted earnings per share | $6.15 | $20.14 | $23.01
  Weighted-average shares used in computation of earnings per share:
   | Basic | 480 | 487 | 494
   | Diluted | 493 | 500 | 504
   | See accompanying notes to consolidated financial statements.
  ```
  </details>

- **v2** · `AMAZON_2019_10K` · PDF page **38** · column 2019 · millions
  - Quote: "Net income \| $3,033 \| $10,073 \| $11,588"

  <details><summary>Passage</summary>

  ```
  Interest expense | (848) | (1,417) | (1,600)
  Other income (expense), net | 346 | (183) | 203
   | Total non-operating income (expense) | (300) | (1,160) | (565)
  Income before income taxes | 3,806 | 11,261 | 13,976
  Provision for income taxes | (769) | (1,197) | (2,374)
  Equity-method investment activity, net of tax | (4) | 9 | (14)
  Net income | $3,033 | $10,073 | $11,588
  Basic earnings per share | $6.32 | $20.68 | $23.46
  Diluted earnings per share | $6.15 | $20.14 | $23.01
  Weighted-average shares used in computation of earnings per share:
   | Basic | 480 | 487 | 494
   | Diluted | 493 | 500 | 504
   | See accompanying notes to consolidated financial statements.
  ```
  </details>

<details><summary>Gold answer</summary>

$11588.00
</details>

## 22. What is Amcor's year end FY2020 net AR (in USD millions)? Address the question by adopting the perspective of a financial analyst who can only use the details shown within the balance sheet.

`financebench_id_03882` · filing `AMCOR_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Amcor's year-end FY2020 net accounts receivable is $1,615.9 million, as reported in the Consolidated Balance Sheet under current assets for the 2020 column [v1, v2]. This figure represents the trade receivables, net, which decreased from $1,864.3 million in the prior year [v1, v2]. The value is explicitly stated in the financial table on page 50 of the 10-K filing [v1].

**Computation:** `trade_receivables_2020 = 1,615.9 million  where trade_receivables_2020 = 1,615.9 (millions, FY2020), trade_receivables_2019 = 1,864.3 (millions, FY2019)`

- **v1** · `AMCOR_2020_10K` · PDF page **50** · column 2020 · millions
  - Quote: "Trade receivables, net \| 1,615.9 \| 1,864.3"

  <details><summary>Passage</summary>

  ```
   | Consolidated Balance Sheet
   | (in millions)
   As of June 30, | 2020 | 2019
   | Assets
   Current assets:
   Cash and cash equivalents | $742.6 | $601.6
   Trade receivables, net | 1,615.9 | 1,864.3
   Inventories, net | 1,831.9 | 1,953.8
   Prepaid expenses and other current assets | 344.3 | 374.3
   Assets held for sale | — | 416.1
   Total current assets | 4,534.7 | 5,210.1
   Non-current assets:
   Investments in affiliated companies | 77.7 | 98.9
  ```
  </details>

- **v2** · `AMCOR_2020_10K` · PDF page **50** · column 2019 · millions
  - Quote: "Trade receivables, net \| 1,615.9 \| 1,864.3"

  <details><summary>Passage</summary>

  ```
   | Consolidated Balance Sheet
   | (in millions)
   As of June 30, | 2020 | 2019
   | Assets
   Current assets:
   Cash and cash equivalents | $742.6 | $601.6
   Trade receivables, net | 1,615.9 | 1,864.3
   Inventories, net | 1,831.9 | 1,953.8
   Prepaid expenses and other current assets | 344.3 | 374.3
   Assets held for sale | — | 416.1
   Total current assets | 4,534.7 | 5,210.1
   Non-current assets:
   Investments in affiliated companies | 77.7 | 98.9
  ```
  </details>

<details><summary>Gold answer</summary>

$1616.00
</details>

## 23. What was the key agenda of the AMCOR's 8k filing dated 1st July 2022?

`financebench_id_01935` · filing `AMCOR_2022_8K_dated-2022-07-01` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMCOR_2022_8K_dated-2022-07-01: code checks failed twice: event_description: the quote is not on page 2. Copy it exactly from one line of the page

**Pages searched:** `AMCOR_2022_8K_dated-2022-07-01` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Amcor Finance (USA), Inc. and Amcor Flexibles North America, Inc., entered into supplemental indentures relating to Guaranteed Senior Notes due 2026 and 2028. This involved the substitution of the Substitute Issuer (Amcor Flexibles North America) for the Former Issuer (Amcor Finance) and the assumption of covenants under the indentures. (In essence a novation agreement)
</details>

## 24. Has AMCOR's quick ratio improved or declined between FY2023 and FY2022? If the quick ratio is not something that a financial analyst would ask about a company like this, then state that and explain why.

`financebench_id_00799` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** AMCOR_2023_10K: verifier: answer_supported=no. The computation for the quick ratio is incorrect because it uses 'trade payables' and 'accrued employee costs' in the denominator. The quick ratio is typically defined as (Cash + Marketable Securities + Receivables) / (Current Liabilities - Inventory). Furthermore, the final answer states the ratio declined but only provides the FY2023 calculation (0.8065) without showing the FY2022 calculation for comparison.

**Pages searched:** `AMCOR_2023_10K` pages 4, 5, 7, 46, 50, 51, 52, 53, 54, 90, 105, 107, 114

<details><summary>Gold answer</summary>

The quick ratio has slightly improved from 0.67 times to 0.69 times between FY 2023 and FY 2022.(3.4% jump)
</details>

## 25. What are major acquisitions that AMCOR has done in FY2023, FY2022 and FY2021?

`financebench_id_01079` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMCOR_2023_10K: extractor: The provided pages only disclose the aggregate dollar amount of business acquisitions ($121 million for FY2023) in the Consolidated Statements of Cash Flows (Page 53). They do not contain the names or specific details of the major acquisitions themselves.

**Pages searched:** `AMCOR_2023_10K` pages 4, 6, 50, 51, 52, 53, 54, 55, 90, 102, 105, 107, 151

<details><summary>Gold answer</summary>

Amcor completed these acquisitions during FY2023: -100% equity interest of a flexibles manufacturing company in the Czech Republic - 100% equity interest in a medical device packaging manufacturing site in Shanghai, China. -acquisition of a New Zealand-based leading manufacturer of state-of-the-art, automated protein packaging machines.
</details>

## 26. What industry does AMCOR primarily operate in?

`financebench_id_01148` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Amcor primarily operates in the packaging industry, specifically developing and producing responsible packaging for food, beverage, pharmaceutical, medical, home, and personal-care products [v2]. The company describes itself as a global leader in this sector, leveraging its expertise across various materials like paper, metal, plastic, and bio-based options [v1, v2]. Its business strategy focuses on being the leading global packaging company through innovation and a focused portfolio [v1].

- **v1** · `AMCOR_2023_10K` · PDF page **5** · column Item 1. - Business · units
  - Quote: "Amcor plc (ARBN 630 385 278) is a public limited company incorporated under the Laws of the Bailiwick of Jersey. Our history dates back more than 150 years, with origins in both Australia and the USA."

  <details><summary>Passage</summary>

  ```
  PART I
  Item 1. - Business
  The Company
    Amcor plc (ARBN 630 385 278) is a public limited company incorporated under the Laws of the Bailiwick of Jersey. Our history dates back
  more than 150 years, with origins in both Australia and the USA. Today, we are a global leader in developing and producing responsible
  packaging for food, beverage, pharmaceutical, medical, home and personal-care, and other products. Our innovation excellence and global
  packaging expertise enables us to solve packaging challenges around the world every day, producing packaging that is more functional,
  appealing, and cost effective for our customers and their consumers and importantly, more sustainable for the environment.
  Sustainability
   | Sustainability is central to our business and one of our most exciting opportunities for growth. Working daily to embed sustainability deeper
  ```
  </details>

- **v2** · `AMCOR_2023_10K` · PDF page **5** · column Item 1. - Business · units
  - Quote: "Today, we are a global leader in developing and producing responsible packaging for food, beverage, pharmaceutical, medical, home and personal-care, and other products."

  <details><summary>Passage</summary>

  ```
  PART I
  Item 1. - Business
  The Company
    Amcor plc (ARBN 630 385 278) is a public limited company incorporated under the Laws of the Bailiwick of Jersey. Our history dates back
  more than 150 years, with origins in both Australia and the USA. Today, we are a global leader in developing and producing responsible
  packaging for food, beverage, pharmaceutical, medical, home and personal-care, and other products. Our innovation excellence and global
  packaging expertise enables us to solve packaging challenges around the world every day, producing packaging that is more functional,
  appealing, and cost effective for our customers and their consumers and importantly, more sustainable for the environment.
  Sustainability
   | Sustainability is central to our business and one of our most exciting opportunities for growth. Working daily to embed sustainability deeper
  into everything we do, Amcor has been a leader in the industry in promoting sustainability. We aspire to improve the quality of lives, protect
  ```
  </details>

<details><summary>Gold answer</summary>

Amcor is a global leader in packaging production for various use cases.
</details>

## 27. Does AMCOR have an improving gross margin profile as of FY2023? If gross margin is not a useful metric for a company like this, then state that and explain why.

`financebench_id_00684` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Amcor does not have an improving gross margin profile as of FY2023 because the calculated change in gross margin is negative at -0.0084 [v1, v2, v3, v4, COMPUTED RESULT]. This indicates that the gross margin decreased from FY2022 to FY2023, meaning the company's profitability relative to sales has worsened rather than improved.

**Computation:** `(gross_profit_2023 / net_sales_2023) - (gross_profit_2022 / net_sales_2022) = -0.0084  where gross_profit_2023 = 2,725 (millions, FY2023), net_sales_2023 = 14,694 (millions, FY2023), gross_profit_2022 = 2,820 (millions, FY2022), net_sales_2022 = 14,544 (millions, FY2022)`

- **v1** · `AMCOR_2023_10K` · PDF page **50** · column 2023 · millions
  - Quote: "Gross profit \| 2,725"

  <details><summary>Passage</summary>

  ```
  | Amcor plc and Subsidiaries
   | Consolidated Statements of Income
   | ($in millions, except per share data)
  For the years ended June 30, | 2023 | 2022 | 2021
  Net sales | $14,694  $14,544  $12,861
  Cost of sales | (11,969) | (11,724) | (10,129)
  Gross profit | 2,725 | 2,820 | 2,732
  Selling, general, and administrative expenses | (1,246) | (1,284) | (1,292)
  Research and development expenses | (101) | (96) | (100)
  Restructuring, impairment, and other related activities, net | 104 | (234) | (94)
  Other income, net | 26 | 33 | 75
  Operating income | 1,508 | 1,239 | 1,321
  Interest income | 31 | 24 | 14
  ```
  </details>

- **v2** · `AMCOR_2023_10K` · PDF page **50** · column 2023 · millions
  - Quote: "Net sales \| $14,694"

  <details><summary>Passage</summary>

  ```
  | Amcor plc and Subsidiaries
   | Consolidated Statements of Income
   | ($in millions, except per share data)
  For the years ended June 30, | 2023 | 2022 | 2021
  Net sales | $14,694  $14,544  $12,861
  Cost of sales | (11,969) | (11,724) | (10,129)
  Gross profit | 2,725 | 2,820 | 2,732
  Selling, general, and administrative expenses | (1,246) | (1,284) | (1,292)
  Research and development expenses | (101) | (96) | (100)
  Restructuring, impairment, and other related activities, net | 104 | (234) | (94)
  Other income, net | 26 | 33 | 75
  ```
  </details>

- **v3** · `AMCOR_2023_10K` · PDF page **50** · column 2022 · millions
  - Quote: "Gross profit \| 2,820"

  <details><summary>Passage</summary>

  ```
  | Amcor plc and Subsidiaries
   | Consolidated Statements of Income
   | ($in millions, except per share data)
  For the years ended June 30, | 2023 | 2022 | 2021
  Net sales | $14,694  $14,544  $12,861
  Cost of sales | (11,969) | (11,724) | (10,129)
  Gross profit | 2,725 | 2,820 | 2,732
  Selling, general, and administrative expenses | (1,246) | (1,284) | (1,292)
  Research and development expenses | (101) | (96) | (100)
  Restructuring, impairment, and other related activities, net | 104 | (234) | (94)
  Other income, net | 26 | 33 | 75
  Operating income | 1,508 | 1,239 | 1,321
  Interest income | 31 | 24 | 14
  ```
  </details>

- **v4** · `AMCOR_2023_10K` · PDF page **50** · column 2022 · millions
  - Quote: "Net sales \| $14,544"

  <details><summary>Passage</summary>

  ```
  | Amcor plc and Subsidiaries
   | Consolidated Statements of Income
   | ($in millions, except per share data)
  For the years ended June 30, | 2023 | 2022 | 2021
  Net sales | $14,694  $14,544  $12,861
  Cost of sales | (11,969) | (11,724) | (10,129)
  Gross profit | 2,725 | 2,820 | 2,732
  Selling, general, and administrative expenses | (1,246) | (1,284) | (1,292)
  Research and development expenses | (101) | (96) | (100)
  Restructuring, impairment, and other related activities, net | 104 | (234) | (94)
  Other income, net | 26 | 33 | 75
  ```
  </details>

<details><summary>Gold answer</summary>

No. For AMCOR there has been a slight decline in gross margins by 0.8%.
</details>

## 28. What is the nature & purpose of AMCOR's restructuring liability as oF Q2 of FY2023 close?

`financebench_id_01936` · filing `AMCOR_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The nature and purpose of Amcor's restructuring liability as of the close of Q2 FY2023 (December 31, 2022) is primarily comprised of restructuring activities related to the Russia-Ukraine conflict [v2]. The total liability balance at that date was $93 million, consisting of $81 million in employee costs, $2 million in fixed asset related costs, and $10 million in other costs [v1].

- **v1** · `AMCOR_2023Q2_10Q` · PDF page **15** · column December 31, 2022 · millions
  - Quote: "Liability balance at December 31, 2022 \| $81 $2 $10 $93"

  <details><summary>Passage</summary>

  ```
   | Fixed Asset | Restructuring
  ($in millions) | Employee Costs | Related Costs | Other Costs | Costs
  Liability balance at June 30, 2022 | $97  $3  $18  $118
  Net charges to earnings | 2 | — | — | 2
  Cash paid | (16) | (1) | (8) | (25)
  Reversal of unused amounts | (2) | — | — | (2)
  Liability balance at December 31, 2022 | $81  $2  $10  $93
    The Company expects the majority of the liability for employee, fixed assets related, and other costs as of December 31, 2022 to be paid
  within the next twelve months. The accruals related to restructuring activities have been recorded on the unaudited condensed consolidated
  balance sheets under other current liabilities and other non-current liabilities.
   | 15
  ```
  </details>

- **v2** · `AMCOR_2023Q2_10Q` · PDF page **15** · column N/A · units
  - Quote: "The Company's restructuring activities in the three and six months ended December 31, 2022 were primarily comprised of restructuring activities related to the Russia-Ukraine conflict"

  <details><summary>Passage</summary>

  ```
  Note 6 - Restructuring
    The Company's restructuring activities in the three and six months ended December 31, 2022 were primarily comprised of restructuring
  activities related to the Russia-Ukraine conflict and the three and six months ended December 31, 2021 included expenses related to the
  Company's 2019 plan from the integration of acquired Bemis operations which was substantially completed at the end of fiscal year 2022.
    Restructuring and related expenses, net were $2 million and $10 million during the three months ended December 31, 2022 and 2021, and $3
  million and $18 million in the six months ended December 31, 2022 and 2021, respectively, and primarily relate to the Flexibles reportable
  segment. The expenses related to restructuring activities have been presented on the unaudited condensed consolidated statements of income as
  restructuring and other related activities, net.
  ```
  </details>

<details><summary>Gold answer</summary>

87% of the total restructuring liability is related Employee liabilities.
</details>

## 29. What Was AMCOR's Adjusted Non GAAP EBITDA for FY 2023

`financebench_id_01928` · filing `AMCOR_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMCOR_2023Q4_EARNINGS: code checks failed twice: scale: the quote is not on page 8. Copy it exactly from one line of the page

**Pages searched:** `AMCOR_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14

<details><summary>Gold answer</summary>

AMCOR's Adj. EBITDA was $2,018mn in FY 2023
</details>

## 30. How much was the Real change in Sales for AMCOR in FY 2023 vs FY 2022, if we exclude the impact of FX movement, passthrough costs and one-off items?

`financebench_id_01930` · filing `AMCOR_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** AMCOR_2023Q4_EARNINGS: verifier: answer_supported=no. The computation uses the absolute difference between reported net sales (14,694 - 14,544 = 150), but the question specifically asks for the change excluding FX, passthrough costs, and one-off items. The table provides a 'Comparable Constant Currency Growth %' of (3)% for the total, which represents the adjusted growth, but the evidence does not provide the absolute dollar value for this specific adjusted change.

**Pages searched:** `AMCOR_2023Q4_EARNINGS` pages 1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14

<details><summary>Gold answer</summary>

The Real Growth was flat in FY 2023 vs FY 2022.
</details>

## 31. Answer the following question as if you are an equity research analyst and have lost internet connection so you do not have access to financial metric providers. According to the details clearly outlined within the P&L statement and the statement of cash flows, what is the FY2015 depreciation and amortization (D&A from cash flow statement) % margin for AMD?

`financebench_id_03069` · filing `AMD_2015_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 depreciation and amortization margin for AMD is 4.1844%, calculated by dividing the $167 million depreciation and amortization from the cash flow statement by the $3,991 million net revenue from the P&L statement [v1, v2]. This metric indicates that depreciation and amortization expenses accounted for approximately 4.2% of the company's total revenue for the fiscal year ended December 26, 2015.

**Computation:** `depreciation_and_amortization_2015 / net_revenue_2015 = 4.1844%  where depreciation_and_amortization_2015 = 167 (millions, FY2015), net_revenue_2015 = $3,991 (millions, FY2015)`

- **v1** · `AMD_2015_10K` · PDF page **60** · column 2015 · millions
  - Quote: "Depreciation and amortization \| 167"

  <details><summary>Passage</summary>

  ```
   | December 26, | December 27, | December 28,
   | 2015 | 2014 | 2013
   | (In millions)
  Cash flows from operating activities:
   | Net loss | $(660) | $(403)  $(83)
   | Adjustments to reconcile net loss to net cash used in operating activities:
   | Depreciation and amortization | 167 | 203 | 236
   | Net loss on disposal of property, plant and equipment | — | — | 31
   | Stock-based compensation expense | 63 | 81 | 91
   | Non-cash interest expense | 11 | 17 | 25
   | Goodwill impairment charge | — | 233 | —
   | Restructuring and other special charges, net | 83 | 14 | —
   | Net loss on debt redemptions | — | 61 | 1
  ```
  </details>

- **v2** · `AMD_2015_10K` · PDF page **56** · column 2015 · millions
  - Quote: "Net revenue \| $3,991"

  <details><summary>Passage</summary>

  ```
   | Advanced Micro Devices, Inc.
   | Consolidated Statements of Operations
   | Year Ended
   | December 26, | December 27, | December 28,
   | 2015 | 2014 | 2013
   | (In millions, except per share amounts)
  Net revenue | $3,991 | $5,506 | $5,299
  Cost of sales | 2,911 | 3,667 | 3,321
  Gross margin | 1,080 | 1,839 | 1,978
  Research and development | 947 | 1,072 | 1,201
  Marketing, general and administrative | 482 | 604 | 674
  Amortization of acquired intangible assets | 3 | 14 | 18
  Restructuring and other special charges, net | 129 | 71 | 30
  ```
  </details>

<details><summary>Gold answer</summary>

4.2%
</details>

## 32. Does AMD have a reasonably healthy liquidity profile based on its quick ratio for FY22? If the quick ratio is not relevant to measure liquidity, please state that and explain why.

`financebench_id_00222` · filing `AMD_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMD_2022_10K: extractor: The provided pages do not contain the Consolidated Balance Sheets (Page 53 in the original filing) which lists 'Total current assets', 'Inventories', 'Prepaid expenses and other current assets', and 'Total current liabilities' necessary to calculate the quick ratio. The available pages include the Table of Contents, Business description, Market data, MD&A text, and Cash Flow statements, but the specific Balance Sheet line items required for the quick ratio calculation are missing from the provided text.

**Pages searched:** `AMD_2022_10K` pages 1, 4, 5, 41, 43, 44, 51, 54, 56, 58, 60, 101

<details><summary>Gold answer</summary>

Yes. The quick ratio is 1.57, calculated as (cash and cash equivalents+Short term investments+Accounts receivable, net+receivables from related parties)/ (current liabilities).
</details>

## 33. What are the major products and services that AMD sells as of FY22?

`financebench_id_00995` · filing `AMD_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** AMD's major products and services as of fiscal year 2022 include server microprocessors (CPUs), graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and Adaptive System-on-Chip (SoC) products for data centers; CPUs, accelerated processing units (APUs), and chipsets for personal computers; discrete GPUs, semi-custom SoC products, and development services; embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products; and portions of its intellectual property (IP) portfolio [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10].

- **v1** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "server microprocessors (CPUs)"

  <details><summary>Passage</summary>

  ```
  Operations,” or MD&A, and such other risks and uncertainties as set forth below in this report or detailed in our other Securities and Exchange Commission
  (SEC) reports and filings. We assume no obligation to update forward-looking statements.
  References in this Annual Report on Form 10-K to “AMD,” “we,” “us,” “management,” “our” or the “Company” mean Advanced Micro Devices, Inc. and our
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v2** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "graphics processing units (GPUs)"

  <details><summary>Passage</summary>

  ```
  Operations,” or MD&A, and such other risks and uncertainties as set forth below in this report or detailed in our other Securities and Exchange Commission
  (SEC) reports and filings. We assume no obligation to update forward-looking statements.
  References in this Annual Report on Form 10-K to “AMD,” “we,” “us,” “management,” “our” or the “Company” mean Advanced Micro Devices, Inc. and our
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v3** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "data processing units (DPUs)"

  <details><summary>Passage</summary>

  ```
  Operations,” or MD&A, and such other risks and uncertainties as set forth below in this report or detailed in our other Securities and Exchange Commission
  (SEC) reports and filings. We assume no obligation to update forward-looking statements.
  References in this Annual Report on Form 10-K to “AMD,” “we,” “us,” “management,” “our” or the “Company” mean Advanced Micro Devices, Inc. and our
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v4** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "Field Programmable Gate Arrays (FPGAs)"

  <details><summary>Passage</summary>

  ```
  Operations,” or MD&A, and such other risks and uncertainties as set forth below in this report or detailed in our other Securities and Exchange Commission
  (SEC) reports and filings. We assume no obligation to update forward-looking statements.
  References in this Annual Report on Form 10-K to “AMD,” “we,” “us,” “management,” “our” or the “Company” mean Advanced Micro Devices, Inc. and our
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v5** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "Adaptive System-on-Chip (SoC) products"

  <details><summary>Passage</summary>

  ```
  (SEC) reports and filings. We assume no obligation to update forward-looking statements.
  References in this Annual Report on Form 10-K to “AMD,” “we,” “us,” “management,” “our” or the “Company” mean Advanced Micro Devices, Inc. and our
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v6** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets"

  <details><summary>Passage</summary>

  ```
  References in this Annual Report on Form 10-K to “AMD,” “we,” “us,” “management,” “our” or the “Company” mean Advanced Micro Devices, Inc. and our
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v7** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "discrete GPUs"

  <details><summary>Passage</summary>

  ```
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v8** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "semi-custom SoC products"

  <details><summary>Passage</summary>

  ```
  consolidated subsidiaries.
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v9** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products"

  <details><summary>Passage</summary>

  ```
  Overview
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

- **v10** · `AMD_2022_10K` · PDF page **4** · column December 31, 2022 · units
  - Quote: "portions of our intellectual property (IP) portfolio"

  <details><summary>Passage</summary>

  ```
  We are a global semiconductor company primarily offering:
   | • | server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and
   | Adaptive System-on-Chip (SoC) products for data centers;
   | • | CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;
   | • | discrete GPUs, and semi-custom SoC products and development services; and
   | •  embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
  From time to time, we may also sell or license portions of our intellectual property (IP) portfolio.
   | 1
  ```
  </details>

<details><summary>Gold answer</summary>

AMD sells server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and Adaptive System-on-Chip (SoC) products for data centers; CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers; discrete GPUs, and semi-custom SoC products and development services; and embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
</details>

## 34. What drove revenue change as of the FY22 for AMD?

`financebench_id_01198` · filing `AMD_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** AMD's revenue increased by $7,167 million in fiscal year 2022 compared to the prior year, driven by a rise from $16,434 million to $23,601 million [v1, v2]. This growth represents a significant year-over-year expansion in net revenue as reported in the Consolidated Statements of Operations [v1, v2].

**Computation:** `net_revenue_2022 - net_revenue_2021 = 7,167 million  where net_revenue_2022 = $23,601 (millions, FY2022), net_revenue_2021 = $16,434 (millions, FY2021)`

- **v1** · `AMD_2022_10K` · PDF page **54** · column 2022 · millions
  - Quote: "Net revenue \| $23,601"

  <details><summary>Passage</summary>

  ```
   | Advanced Micro Devices, Inc.
   | Consolidated Statements of Operations
   | Year Ended
   | December 31, | December 25, | December 26,
   | 2022 | 2021 | 2020
   | (In millions, except per share amounts)
  Net revenue | $23,601  $16,434  $9,763
  Cost of sales | 11,550 | 8,505 | 5,416
  Amortization of acquisition-related intangibles | 1,448 | — | —
  Total cost of sales | 12,998 | 8,505 | 5,416
  Gross profit | 10,603 | 7,929 | 4,347
  Research and development | 5,005 | 2,845 | 1,983
  Marketing, general and administrative | 2,336 | 1,448 | 995
  ```
  </details>

- **v2** · `AMD_2022_10K` · PDF page **54** · column 2021 · millions
  - Quote: "$16,434"

  <details><summary>Passage</summary>

  ```
   | Advanced Micro Devices, Inc.
   | Consolidated Statements of Operations
   | Year Ended
   | December 31, | December 25, | December 26,
   | 2022 | 2021 | 2020
   | (In millions, except per share amounts)
  Net revenue | $23,601  $16,434  $9,763
  Cost of sales | 11,550 | 8,505 | 5,416
  Amortization of acquisition-related intangibles | 1,448 | — | —
  Total cost of sales | 12,998 | 8,505 | 5,416
  Gross profit | 10,603 | 7,929 | 4,347
  Research and development | 5,005 | 2,845 | 1,983
  Marketing, general and administrative | 2,336 | 1,448 | 995
  ```
  </details>

<details><summary>Gold answer</summary>

In 2022, AMD reported Higher sales of their EPYC server processors, higher semi-custom product sales, and the inclusion of Xilinx embedded product sales
</details>

## 35. What drove operating margin change as of the FY22 for AMD? If operating margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00917` · filing `AMD_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMD_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2022,, 2021,

**Pages searched:** `AMD_2022_10K` pages 4, 5, 8, 9, 43, 49, 54, 56, 58, 60, 73, 102

<details><summary>Gold answer</summary>

The decrease in AMD's operating income was primarily driven by amortization of intangible assets associated with the Xilinx acquisition
</details>

## 36. Among operations, investing, and financing activities, which brought in the most (or lost the least) cash flow for AMD in FY22?

`financebench_id_01279` · filing `AMD_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Operating activities brought in the most cash flow for AMD in FY22 with $3,565 million, compared to $1,999 million from investing activities and a net outflow of $3,264 million from financing activities [v1, v2, v3].

**Computation:** `max(operating_activities_2022, investing_activities_2022, abs(financing_activities_2022)) = 3,565 million  where operating_activities_2022 = $3,565 (millions, FY2022), investing_activities_2022 = 1,999 (millions, FY2022), financing_activities_2022 = (3,264) (millions, FY2022)`

- **v1** · `AMD_2022_10K` · PDF page **51** · column 2022 · millions
  - Quote: "Operating activities \| $3,565"

  <details><summary>Passage</summary>

  ```
  by stock repurchases and cash paid for the acquisition of Pensando. The percentage of cash and cash equivalents held domestically was 73% as of
  December 31, 2022, and 91% as of December 25, 2021.
  Our operating, investing and financing cash flow activities for 2022 and 2021 were as follows:
   | December 31, 2022 | December 25, 2021
   | (In millions)
  Net cash provided by (used in):
  Operating activities | $3,565  $3,521
  Investing activities | 1,999 | (686)
  Financing activities | (3,264) | (1,895)
  Net increase in cash and cash equivalents | $2,300  $940
  Our aggregate principal debt obligations were $2.5 billion as of December 31, 2022, which consisted primarily of $1.5 billion of the Xilinx Notes assumed as part
  of the Xilinx acquisition and $1.0 billion of 3.924% Notes and 4.393% Notes issued during the year, compared to $313 million as of December 25, 2021,
  respectively. We repaid $312 million of our 7.50% Senior Notes that matured in August 2022.
  ```
  </details>

- **v2** · `AMD_2022_10K` · PDF page **51** · column 2022 · millions
  - Quote: "Investing activities \| 1,999"

  <details><summary>Passage</summary>

  ```
  December 31, 2022, and 91% as of December 25, 2021.
  Our operating, investing and financing cash flow activities for 2022 and 2021 were as follows:
   | December 31, 2022 | December 25, 2021
   | (In millions)
  Net cash provided by (used in):
  Operating activities | $3,565  $3,521
  Investing activities | 1,999 | (686)
  Financing activities | (3,264) | (1,895)
  Net increase in cash and cash equivalents | $2,300  $940
  Our aggregate principal debt obligations were $2.5 billion as of December 31, 2022, which consisted primarily of $1.5 billion of the Xilinx Notes assumed as part
  of the Xilinx acquisition and $1.0 billion of 3.924% Notes and 4.393% Notes issued during the year, compared to $313 million as of December 25, 2021,
  respectively. We repaid $312 million of our 7.50% Senior Notes that matured in August 2022.
  On April 29, 2022, we entered into a revolving credit agreement (Revolving Credit Agreement) with Wells Fargo Bank, N.A. as administrative agent and other
  ```
  </details>

- **v3** · `AMD_2022_10K` · PDF page **51** · column 2022 · millions
  - Quote: "Financing activities \| (3,264)"

  <details><summary>Passage</summary>

  ```
  Our operating, investing and financing cash flow activities for 2022 and 2021 were as follows:
   | December 31, 2022 | December 25, 2021
   | (In millions)
  Net cash provided by (used in):
  Operating activities | $3,565  $3,521
  Investing activities | 1,999 | (686)
  Financing activities | (3,264) | (1,895)
  Net increase in cash and cash equivalents | $2,300  $940
  Our aggregate principal debt obligations were $2.5 billion as of December 31, 2022, which consisted primarily of $1.5 billion of the Xilinx Notes assumed as part
  of the Xilinx acquisition and $1.0 billion of 3.924% Notes and 4.393% Notes issued during the year, compared to $313 million as of December 25, 2021,
  respectively. We repaid $312 million of our 7.50% Senior Notes that matured in August 2022.
  On April 29, 2022, we entered into a revolving credit agreement (Revolving Credit Agreement) with Wells Fargo Bank, N.A. as administrative agent and other
  banks identified therein as lenders. The Revolving Credit Agreement provides for a five-year unsecured revolving credit facility in the aggregate principal
  ```
  </details>

<details><summary>Gold answer</summary>

In 2022, AMD brought in the most cashflow from Operations
</details>

## 37. From FY21 to FY22, excluding Embedded, in which AMD reporting segment did sales proportionally increase the most?

`financebench_id_00563` · filing `AMD_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The Data Center segment experienced the highest proportional sales increase from FY21 to FY22, growing by approximately 63.6% compared to decreases in the Client and Gaming segments. This is calculated using the provided revenue figures: Data Center grew from $3,694 million to $6,043 million, Client revenue fell from $6,887 million to $6,201 million, and Gaming revenue rose from $5,607 million to $6,805 million [v1, v2, v3, v4, v5, v6]. The computed maximum growth rate of 0.6359 confirms the Data Center segment had the largest proportional increase [COMPUTED RESULT].

**Computation:** `max((data_center_rev_2022 - data_center_rev_2021) / data_center_rev_2021, (client_rev_2022 - client_rev_2021) / client_rev_2021, (gaming_rev_2022 - gaming_rev_2021) / gaming_rev_2021) = 0.6359  where data_center_rev_2021 = $3,694 (millions, FY2021), data_center_rev_2022 = $6,043 (millions, FY2022), client_rev_2021 = $6,887 (millions, FY2021), client_rev_2022 = 6,201 (millions, FY2022), gaming_rev_2021 = $5,607 (millions, FY2021), gaming_rev_2022 = 6,805 (millions, FY2022)`

- **v1** · `AMD_2022_10K` · PDF page **48** · column December 25, 2021 · millions
  - Quote: "Data Center \| $6,043  $3,694"

  <details><summary>Passage</summary>

  ```
  The following table provides a summary of net revenue and operating income (loss) by segment for 2022 and 2021:
   | Year Ended
   | December 31, | December 25,
   | 2022 | 2021
   | (In millions)
  Net revenue:
   | Data Center | $6,043  $3,694
   | Client | 6,201 | 6,887
   | Gaming | 6,805 | 5,607
   | Embedded | 4,552 | 246
  Total net revenue | $23,601  $16,434
  Operating income (loss):
   | Data Center | $1,848  $991
  ```
  </details>

- **v2** · `AMD_2022_10K` · PDF page **48** · column December 31, 2022 · millions
  - Quote: "Data Center \| $6,043  $3,694"

  <details><summary>Passage</summary>

  ```
  The following table provides a summary of net revenue and operating income (loss) by segment for 2022 and 2021:
   | Year Ended
   | December 31, | December 25,
   | 2022 | 2021
   | (In millions)
  Net revenue:
   | Data Center | $6,043  $3,694
   | Client | 6,201 | 6,887
   | Gaming | 6,805 | 5,607
   | Embedded | 4,552 | 246
  Total net revenue | $23,601  $16,434
  Operating income (loss):
   | Data Center | $1,848  $991
  ```
  </details>

- **v3** · `AMD_2022_10K` · PDF page **48** · column December 25, 2021 · millions
  - Quote: "Client \| 6,201 \| 6,887"

  <details><summary>Passage</summary>

  ```
   | Year Ended
   | December 31, | December 25,
   | 2022 | 2021
   | (In millions)
  Net revenue:
   | Data Center | $6,043  $3,694
   | Client | 6,201 | 6,887
   | Gaming | 6,805 | 5,607
   | Embedded | 4,552 | 246
  Total net revenue | $23,601  $16,434
  Operating income (loss):
   | Data Center | $1,848  $991
   | Client | 1,190 | 2,088
  ```
  </details>

- **v4** · `AMD_2022_10K` · PDF page **48** · column December 31, 2022 · millions
  - Quote: "Client \| 6,201 \| 6,887"

  <details><summary>Passage</summary>

  ```
   | Year Ended
   | December 31, | December 25,
   | 2022 | 2021
   | (In millions)
  Net revenue:
   | Data Center | $6,043  $3,694
   | Client | 6,201 | 6,887
   | Gaming | 6,805 | 5,607
   | Embedded | 4,552 | 246
  Total net revenue | $23,601  $16,434
  Operating income (loss):
   | Data Center | $1,848  $991
   | Client | 1,190 | 2,088
  ```
  </details>

- **v5** · `AMD_2022_10K` · PDF page **48** · column December 25, 2021 · millions
  - Quote: "Gaming \| 6,805 \| 5,607"

  <details><summary>Passage</summary>

  ```
   | December 31, | December 25,
   | 2022 | 2021
   | (In millions)
  Net revenue:
   | Data Center | $6,043  $3,694
   | Client | 6,201 | 6,887
   | Gaming | 6,805 | 5,607
   | Embedded | 4,552 | 246
  Total net revenue | $23,601  $16,434
  Operating income (loss):
   | Data Center | $1,848  $991
   | Client | 1,190 | 2,088
   | Gaming | 953 | 934
  ```
  </details>

- **v6** · `AMD_2022_10K` · PDF page **48** · column December 31, 2022 · millions
  - Quote: "Gaming \| 6,805 \| 5,607"

  <details><summary>Passage</summary>

  ```
   | December 31, | December 25,
   | 2022 | 2021
   | (In millions)
  Net revenue:
   | Data Center | $6,043  $3,694
   | Client | 6,201 | 6,887
   | Gaming | 6,805 | 5,607
   | Embedded | 4,552 | 246
  Total net revenue | $23,601  $16,434
  Operating income (loss):
   | Data Center | $1,848  $991
   | Client | 1,190 | 2,088
   | Gaming | 953 | 934
  ```
  </details>

<details><summary>Gold answer</summary>

Data Center
</details>

## 38. Did AMD report customer concentration in FY22?

`financebench_id_00757` · filing `AMD_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMD_2022_10K: extractor: The provided pages do not contain specific quantitative data regarding customer concentration (e.g., percentage of revenue from top customers). While Page 8 (which is not in the provided pages) mentions customer types, the available pages (1, 4, 5, 11, 43, 54, 56, 58, 60, 101, 102, 106) only describe the company's business and financial results without disclosing concentration metrics.

**Pages searched:** `AMD_2022_10K` pages 1, 4, 5, 11, 43, 54, 56, 58, 60, 101, 102, 106

<details><summary>Gold answer</summary>

Yes, one customer accounted for 16% of consolidated net revenue
</details>

## 39. Which debt securities are registered to trade on a national securities exchange under American Express' name as of 2022?

`financebench_id_00476` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: extractor: The question asks for 'debt securities' registered to trade on a national securities exchange. Page 1 lists securities registered pursuant to Section 12(b) of the Act. The only item listed is 'Common Shares (par value $0.20 per Share)', which is an equity security, not a debt security. The filing does not list any debt securities registered on a national exchange. Therefore, the specific evidence for 'debt securities' is not found in the provided pages.

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 1, 68, 95, 96, 97, 98, 99, 156, 162, 252, 259, 260

<details><summary>Gold answer</summary>

There are none
</details>

## 40. What are the geographies that American Express primarily operates in as of 2022?

`financebench_id_01028` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2022,

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 7, 40, 95, 96, 97, 98, 99, 152, 156, 252, 253, 254

<details><summary>Gold answer</summary>

United States, EMEA, APAC, and LACC
</details>

## 41. Does AMEX have an improving operating margin profile as of 2022? If operating margin is not a useful metric for a company like this, then state that and explain why.

`financebench_id_00723` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: code checks failed twice: formula: unknown value name 'total_revenues_net_of_interest_expense_after_provisions_for_crls_2022' (names: ['total_expenses', 'total_expenses_4', 'total_revenues_net_of_interest_expense_after_provisions_for_crls', 'total_revenues_net_of_interest_expense_after_provisions_for_crls_3'])

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 4, 40, 46, 64, 67, 89, 95, 96, 97, 98, 99, 156

<details><summary>Gold answer</summary>

Performance is not measured through operating margin
</details>

## 42. What drove gross margin change as of the FY2022 for American Express? If gross margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00720` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Gross margin is not a meaningful metric for American Express because the company operates as a financial services firm where net interest income and non-interest revenues are reported separately, making a traditional gross margin calculation not applicable [v1, v2]. The financial statements instead report "Total revenues net of interest expense after provisions for credit losses" as $50,680 million and "Total expenses" as $41,095 million for FY2022, which are the relevant figures for analyzing profitability in this sector [v1, v2].

- **v1** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Total revenues net of interest expense after provisions for credit losses \| 50,680"

  <details><summary>Passage</summary>

  ```
   Total revenues net of interest expense | 52,862 | 42,380 | 36,087
   Provisions for credit losses
    Card Member receivables | 627 | (73) | 1,015
    Card Member loans | 1,514 | (1,155) | 3,453
    Other | 41 | (191) | 262
   | Total provisions for credit losses | 2,182 | (1,419) | 4,730
   Total revenues net of interest expense after provisions for credit losses | 50,680 | 43,799 | 31,357
  Expenses
    Card Member rewards | 14,002 | 11,007 | 8,041
    Business development | 4,943 | 3,762 | 3,051
    Card Member services | 2,959 | 1,993 | 1,230
    Marketing | 5,458 | 5,291 | 3,696
   | Salaries and employee benefits | 7,252 | 6,240 | 5,718
  ```
  </details>

- **v2** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Total expenses \| 41,095"

  <details><summary>Passage</summary>

  ```
    Card Member rewards | 14,002 | 11,007 | 8,041
    Business development | 4,943 | 3,762 | 3,051
    Card Member services | 2,959 | 1,993 | 1,230
    Marketing | 5,458 | 5,291 | 3,696
   | Salaries and employee benefits | 7,252 | 6,240 | 5,718
   | Other, net | 6,481 | 4,817 | 5,325
   | Total expenses | 41,095 | 33,110 | 27,061
   Pretax income | 9,585 | 10,689 | 4,296
  Income tax provision | 2,071 | 2,629 | 1,161
   Net income | $7,514 | $8,060 | $3,135
  Earnings per Common Share — (Note 21) (a)
   | Basic | $9.86 | $10.04 | $3.77
   | Diluted | $9.85 | $10.02 | $3.77
  ```
  </details>

<details><summary>Gold answer</summary>

Performance is not measured through gross margin
</details>

## 43. How much has the effective tax rate of American Express changed between FY2021 and FY2022?

`financebench_id_01351` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: extractor: The provided pages contain text stating the effective tax rates (21.6% for 2022 and 24.6% for 2021) on Page 49, but the specific named identifiers required to construct a formula using the 'name' field (e.g., 'effective_tax_rate_2022') are not present in the structured data of the provided pages. The text is embedded in a narrative paragraph rather than a table row with a distinct label suitable for extraction as a 'name' value according to the strict rules provided. Therefore, the specific named values required for the formula cannot be extracted from the given pages.

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 49, 89, 92, 95, 96, 97, 98, 99, 126, 156, 163, 164

<details><summary>Gold answer</summary>

The effective tax rate for American Express has changed/dropped from 24.6% in FY 2021 to 21.6% in FY 2022.
</details>

## 44. What was the largest liability in American Express's Balance Sheet in 2022?

`financebench_id_01964` · filing `AMERICANEXPRESS_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: code checks failed twice: formula: unknown value name 'customer_deposits' (names: [])

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 64, 65, 95, 96, 97, 98, 99, 150, 152, 156, 259, 260

<details><summary>Gold answer</summary>

Customer deposits
</details>

## 45. Was American Express able to retain card members during 2022?

`financebench_id_01981` · filing `AMERICANEXPRESS_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: extractor: The provided pages do not contain specific data on card member retention rates or the number of card members at the beginning and end of 2022 to calculate retention. Page 5 mentions '76.7 million proprietary cards-in-force worldwide' as of December 31, 2022, but does not provide the starting balance for 2022 or a breakdown of new acquisitions versus attrition.

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 4, 5, 7, 29, 85, 89, 95, 96, 97, 98, 99, 156

<details><summary>Gold answer</summary>

Yes
</details>

## 46. How much (in USD billions) did American Water Works pay out in cash dividends for FY2020? Compute or extract the answer by primarily using the details outlined in the statement of cash flows.

`financebench_id_05718` · filing `AMERICANWATERWORKS_2020_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** AMERICANWATERWORKS_2020_10K: code checks failed twice: formula: numeric constant 1000 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `AMERICANWATERWORKS_2020_10K` pages 68, 82, 83, 84, 86, 87, 88, 106, 134, 135, 140

<details><summary>Gold answer</summary>

$0.40
</details>

## 47. Basing your judgments off of the cash flow statement and the income statement, what is American Water Works's FY2021 unadjusted operating income + depreciation and amortization from the cash flow statement (unadjusted EBITDA) in USD millions?

`financebench_id_04254` · filing `AMERICANWATERWORKS_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** American Water Works's FY2021 unadjusted operating income plus depreciation and amortization is 1,832 million USD. This is calculated by adding the operating income of 1,196 million from the income statement to the depreciation and amortization of 636 million from the cash flow statement [v1, v2].

**Computation:** `operating_income_2021 + depreciation_and_amortization_2021 = 1,832 million  where operating_income_2021 = 1,196 (millions, FY2021), depreciation_and_amortization_2021 = 636 (millions, FY2021)`

- **v1** · `AMERICANWATERWORKS_2021_10K` · PDF page **86** · column 2021 · millions
  - Quote: "Operating income \| 1,196"

  <details><summary>Passage</summary>

  ```
  Operating expenses:
   | Operation and maintenance | 1,777 | 1,622 | 1,544
   | Depreciation and amortization | 636 | 604 | 582
   | General taxes | 321 | 303 | 280
   | Other | — | — | (10)
  Total operating expenses, net | 2,734 | 2,529 | 2,396
  Operating income | 1,196 | 1,248 | 1,214
  Other income (expense):
   | Interest expense | (403) | (397) | (386)
   | Interest income | 4 | 2 | 4
   | Non-operating benefit costs, net | 78 | 49 | 16
   | Gain or (loss) on sale of businesses | 747 | — | (44)
   | Other, net | 18 | 22 | 29
  ```
  </details>

- **v2** · `AMERICANWATERWORKS_2021_10K` · PDF page **88** · column 2021 · millions
  - Quote: "Depreciation and amortization \| 636"

  <details><summary>Passage</summary>

  ```
  (In millions)
   | For the Years Ended December 31,
   | 2021 | 2020 | 2019
  CASH FLOWS FROM OPERATING ACTIVITIES
   | Net income | $1,263 | $709 | $621
   | Adjustments to reconcile to net cash flows provided by operating activities:
   | Depreciation and amortization | 636 | 604 | 582
   | Deferred income taxes and amortization of investment tax credits | 230 | 207 | 208
   | Provision for losses on accounts receivable | 37 | 34 | 28
   | (Gain) or loss on sale of businesses | (747) | — | 34
   | Pension and non-pension postretirement benefits | (41) | (14) | 17
   | Other non-cash, net | (23) | (20) | (41)
   | Changes in assets and liabilities:
  ```
  </details>

<details><summary>Gold answer</summary>

$1832.00
</details>

## 48. Does American Water Works have positive working capital based on FY2022 data? If working capital is not a useful or relevant metric for this company, then please state that and explain why.

`financebench_id_00070` · filing `AMERICANWATERWORKS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, American Water Works does not have positive working capital based on FY2022 data. The company's working capital is negative $1,561 million, calculated as total current assets of $1,250 million minus total current liabilities of $2,811 million [v1, v2, COMPUTED RESULT].

**Computation:** `(total_current_assets_2022 - total_current_liabilities_2022) = -1,561 million  where total_current_assets_2022 = 1,250 (millions, FY2022), total_current_liabilities_2022 = 2,811 (millions, FY2022)`

- **v1** · `AMERICANWATERWORKS_2022_10K` · PDF page **81** · column 2022 · millions
  - Quote: "Total current assets \| 1,250"

  <details><summary>Passage</summary>

  ```
   | Accounts receivable, net of allowance for uncollectible accounts of $60 and $75, respectively | 334 | 271
    Income tax receivable | 114 | 4
   | Unbilled revenues | 275 | 248
   | Materials and supplies | 98 | 57
   | Assets held for sale | — | 683
   | Other | 312 | 155
  Total current assets | 1,250 | 1,554
  Regulatory and other long-term assets:
   | Regulatory assets | 990 | 1,051
   | Seller promissory note from the sale of the Homeowner Services Group | 720 | 720
   | Operating lease right-of-use assets | 82 | 92
   | Goodwill | 1,143 | 1,139
   | Postretirement benefit assets | — | 193
  ```
  </details>

- **v2** · `AMERICANWATERWORKS_2022_10K` · PDF page **82** · column 2022 · millions
  - Quote: "Total current liabilities \| 2,811"

  <details><summary>Passage</summary>

  ```
   | Accounts payable | 254 | 235
   | Accrued liabilities | 706 | 701
   | Accrued taxes | 49 | 176
   | Accrued interest | 91 | 88
   | Liabilities related to assets held for sale | — | 83
   | Other | 255 | 217
  Total current liabilities | 2,811 | 2,141
  Regulatory and other long-term liabilities:
    Advances for construction | 316 | 284
   | Deferred income taxes and investment tax credits | 2,437 | 2,421
   | Regulatory liabilities | 1,590 | 1,600
   | Operating lease liabilities | 70 | 80
   | Accrued pension expense | 235 | 285
  ```
  </details>

<details><summary>Gold answer</summary>

No, American Water Works had negative working capital of -$1561M in FY 2022.
</details>

## 49. In agreement with the information outlined in the income statement, what is the FY2015 - FY2017 3 year average net profit margin (as a %) for Best Buy? Answer in units of percents and round to one decimal place.

`financebench_id_02608` · filing `BESTBUY_2017_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BESTBUY_2017_10K: extractor: The provided pages (specifically Page 31 and Page 56) contain 'Net earnings from continuing operations' and 'Revenue', but they do not explicitly list a 'Net profit margin' percentage for FY2015, FY2016, or FY2017. The table lists 'Gross profit as a % of revenue' and 'Operating income as a % of revenue', but not the net profit margin. Since the specific metric requested ('net profit margin') is not present as a raw value in the text, and the instructions prohibit computing values myself, the evidence for this specific metric is not found in the provided pages.

**Pages searched:** `BESTBUY_2017_10K` pages 1, 3, 31, 36, 53, 55, 56, 58, 81, 91, 96, 97

<details><summary>Gold answer</summary>

2.8%
</details>

## 50. What is the year end FY2019 total amount of inventories for Best Buy? Answer in USD millions. Base your judgments on the information provided primarily in the balance sheet.

`financebench_id_04417` · filing `BESTBUY_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The year-end FY2019 total amount of inventories for Best Buy is 5,409 million USD. This figure is explicitly stated in the Consolidated Balance Sheets for the date February 2, 2019, under the line item "Merchandise inventories" [v1].

**Computation:** `merchandise_inventories_2019 = 5,409 million  where merchandise_inventories_2019 = 5,409 (millions, FY2019)`

- **v1** · `BESTBUY_2019_10K` · PDF page **52** · column February 2, 2019 · millions
  - Quote: "Merchandise inventories \| 5,409 \| 5,209"

  <details><summary>Passage</summary>

  ```
   | February 2, 2019 | February 3, 2018
  Assets
  Current assets
    Cash and cash equivalents | $1,980 | $1,101
    Short-term investments | — | 2,032
    Receivables, net | 1,015 | 1,049
    Merchandise inventories | 5,409 | 5,209
    Other current assets | 466 | 438
   | Total current assets | 8,870 | 9,829
  Property and equipment
    Land and buildings | 637 | 623
    Leasehold improvements | 2,119 | 2,327
    Fixtures and equipment | 5,865 | 5,410
  ```
  </details>

<details><summary>Gold answer</summary>

$5409.00
</details>

## 51. Are Best Buy's gross margins historically consistent (not fluctuating more than roughly 2% each year)? If gross margins are not a relevant metric for a company like this, then please state that and explain why.

`financebench_id_00685` · filing `BESTBUY_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BESTBUY_2023_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2%, 2021,, 2022,, 2023,, (22.5%

**Pages searched:** `BESTBUY_2023_10K` pages 1, 5, 23, 24, 26, 36, 39, 40, 42, 43, 50

<details><summary>Gold answer</summary>

Yes, the margins have been consistent, there has been a minor decline of 1.1% in gross margins between FY2022 and FY2023.
</details>

## 52. What are major acquisitions that Best Buy has done in FY2023, FY2022 and FY2021?

`financebench_id_01077` · filing `BESTBUY_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BESTBUY_2023_10K: extractor: The provided pages do not contain a list of major acquisitions for FY2023, FY2022, and FY2021. Page 42 shows the cash flow impact of acquisitions for FY2022 ($468 million) but lists '-' (zero) for FY2023 and FY2021. Page 23 and Page 44 mention acquisitions of Current Health and Yardbird in fiscal 2022, but do not list any for FY2023 or FY2021. Therefore, the evidence for major acquisitions across all three requested years is not found in the provided text.

**Pages searched:** `BESTBUY_2023_10K` pages 4, 21, 23, 39, 40, 42, 43, 44, 50, 66, 69

<details><summary>Gold answer</summary>

Best Buy closed two acquisitions, both these companies were already partially owned by Best Buy, but Best Buy acquired all outstanding shares of these two companies during FY 2022: (1) Current Health Ltd and (2) Two Peaks, LLC d/b/a Yardbird Furniture
</details>

## 53. Among operations, investing, and financing activities, which brought in the most (or lost the least) cash flow for Best Buy in FY2023?

`financebench_id_01275` · filing `BESTBUY_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Operating activities brought in the most cash flow for Best Buy in FY2023 with $1,824 million, compared to cash used in investing activities of $(962) million and cash used in financing activities of $(1,806) million [v1, v2, v3]. This is confirmed by the computed result showing 1,824 million as the maximum value among the three categories [COMPUTED RESULT].

**Computation:** `max(total_cash_provided_by_operating_activities_2023, total_cash_used_in_investing_activities_2023, total_cash_used_in_financing_activities_2023) = 1,824 million  where total_cash_provided_by_operating_activities_2023 = 1,824 (millions, FY2023), total_cash_used_in_investing_activities_2023 = (962) (millions, FY2023), total_cash_used_in_financing_activities_2023 = (1,806) (millions, FY2023)`

- **v1** · `BESTBUY_2023_10K` · PDF page **42** · column January 28, 2023 · millions
  - Quote: "Total cash provided by operating activities \| 1,824"

  <details><summary>Passage</summary>

  ```
   Receivables | (103) | 17 | 73
   Merchandise inventories | 809 | (328) | (435)
   Other assets | (21) | (14) | (51)
   Accounts payable | (1,099) | (201) | 1,676
   Income taxes | 36 | (156) | 173
   Other liabilities | (483) | 479 | 498
  Total cash provided by operating activities | 1,824 | 3,252 | 4,927
  Investing activities
    Additions to property and equipment, net of $35, $46 and $32, respectively, of non-cash
    capital expenditures | (930) | (737) | (713)
   Purchases of investments | (46) | (233) | (620)
   Sales of investments | 7 | 66 | 546
    Acquisitions, net of cash acquired | - | (468) | -
  ```
  </details>

- **v2** · `BESTBUY_2023_10K` · PDF page **42** · column January 28, 2023 · millions
  - Quote: "Total cash used in investing activities \| (962)"

  <details><summary>Passage</summary>

  ```
    Additions to property and equipment, net of $35, $46 and $32, respectively, of non-cash
    capital expenditures | (930) | (737) | (713)
   Purchases of investments | (46) | (233) | (620)
   Sales of investments | 7 | 66 | 546
    Acquisitions, net of cash acquired | - | (468) | -
    Other, net | 7 | - | (1)
  Total cash used in investing activities | (962) | (1,372) | (788)
  Financing activities
   Repurchase of common stock | (1,014) | (3,502) | (312)
   Issuance of common stock | 16 | 29 | 28
   Dividends paid | (789) | (688) | (568)
   Borrowings of debt | - | - | 1,892
   Repayments of debt | (19) | (133) | (1,916)
  ```
  </details>

- **v3** · `BESTBUY_2023_10K` · PDF page **42** · column January 28, 2023 · millions
  - Quote: "Total cash used in financing activities \| (1,806)"

  <details><summary>Passage</summary>

  ```
   Repurchase of common stock | (1,014) | (3,502) | (312)
   Issuance of common stock | 16 | 29 | 28
   Dividends paid | (789) | (688) | (568)
   Borrowings of debt | - | - | 1,892
   Repayments of debt | (19) | (133) | (1,916)
    Other, net | - | (3) | -
  Total cash used in financing activities | (1,806) | (4,297) | (876)
  Effect of exchange rate changes on cash | (8) | (3) | 7
  Increase (decrease) in cash, cash equivalents and restricted cash | (952) | (2,420) | 3,270
  Cash, cash equivalents and restricted cash at beginning of period | 3,205 | 5,625 | 2,355
  Cash, cash equivalents and restricted cash at end of period | $2,253 | $3,205 | $5,625
  Supplemental cash flow information
   Income taxes paid | $283 | $716 | $442
  ```
  </details>

<details><summary>Gold answer</summary>

Best Buy generated the most cash flow from operating activities in FY 2023 ($1.8 bn)
</details>

## 54. Was there any drop in Cash & Cash equivalents between FY 2023 and Q2 of FY2024?

`financebench_id_00288` · filing `BESTBUY_2024Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BESTBUY_2024Q2_10Q: number check (G4) failed twice: numbers not in the evidence or the result: 23, 23

**Pages searched:** `BESTBUY_2024Q2_10Q` pages 3, 4, 5, 6, 7, 8, 10, 20, 21, 22, 24, 25

<details><summary>Gold answer</summary>

Yes, there was a decline of ~42% between FY2023 and Q2 of FY 2024.
</details>

## 55. Was there any change in the number of Best Buy stores between Q2 of FY2024 and FY2023?

`financebench_id_00460` · filing `BESTBUY_2024Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, there was a decrease of 23 stores in the number of Best Buy stores between the beginning of Q2 FY2024 and the beginning of Q2 FY2023. The number of stores dropped from 931 at the start of Q2 FY2023 to 908 at the start of Q2 FY2024 [v1, v2].

**Computation:** `best_buy_stores_q2_2024_beginning - best_buy_stores_q2_2023_beginning = -23  where best_buy_stores_q2_2024_beginning = 908 (units, Q2 FY2024), best_buy_stores_q2_2023_beginning = 931 (units, Q2 FY2023)`

- **v1** · `BESTBUY_2024Q2_10Q` · PDF page **17** · column Beginning of Second Quarter Fiscal 2024 · units
  - Quote: "Best Buy \| 908"

  <details><summary>Passage</summary>

  ```
  described above and within the Consolidated Results section, above.
  Domestic segment stores open at the beginning and end of the second quarters of fiscal 2024 and fiscal 2023 were as follows:
   | Fiscal 2024 | Fiscal 2023
   | Total Stores at | Total Stores at | Total Stores at | Total Stores at
   | Beginning of | Stores | Stores | End of Second | Beginning of | Stores | Stores | End of Second
   | Second Quarter | Opened | Closed | Quarter | Second Quarter | Opened | Closed | Quarter
  Best Buy | 908 | - | (1) | 907 | 931 | 1 | (2) | 930
  Outlet Centers | 20 | 1 | (1) | 20 | 16 | 2 | - | 18
  Pacific Sales | 20 | - | - | 20 | 21 | - | - | 21
  Yardbird | 18 | 4 | - | 22 | 9 | 4 | - | 13
    Total | 966 | 5 | (2) | 969 | 977 | 7 | (2) | 982
  We continuously monitor store performance as part of a market-driven, omnichannel strategy. As we approach the expiration of leases, we evaluate various
  options for each location, including whether a store should remain open. We currently expect to close a total of 20 to 30 Best Buy stores and open approximately
  ```
  </details>

- **v2** · `BESTBUY_2024Q2_10Q` · PDF page **17** · column Beginning of Second Quarter Fiscal 2023 · units
  - Quote: "Best Buy \| 931"

  <details><summary>Passage</summary>

  ```
  described above and within the Consolidated Results section, above.
  Domestic segment stores open at the beginning and end of the second quarters of fiscal 2024 and fiscal 2023 were as follows:
   | Fiscal 2024 | Fiscal 2023
   | Total Stores at | Total Stores at | Total Stores at | Total Stores at
   | Beginning of | Stores | Stores | End of Second | Beginning of | Stores | Stores | End of Second
   | Second Quarter | Opened | Closed | Quarter | Second Quarter | Opened | Closed | Quarter
  Best Buy | 908 | - | (1) | 907 | 931 | 1 | (2) | 930
  Outlet Centers | 20 | 1 | (1) | 20 | 16 | 2 | - | 18
  Pacific Sales | 20 | - | - | 20 | 21 | - | - | 21
  Yardbird | 18 | 4 | - | 22 | 9 | 4 | - | 13
    Total | 966 | 5 | (2) | 969 | 977 | 7 | (2) | 982
  We continuously monitor store performance as part of a market-driven, omnichannel strategy. As we approach the expiration of leases, we evaluate various
  options for each location, including whether a store should remain open. We currently expect to close a total of 20 to 30 Best Buy stores and open approximately
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, there is decline in number stores by 1.32% from 982 stores in Q2 FY 2023 to 969 by the end of Q2 FY2024.
</details>

## 56. Which Best Buy product category performed the best (by top line) in the domestic (USA) Market during Q2 of FY2024?

`financebench_id_01902` · filing `BESTBUY_2024Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The "Computing and Mobile Phones" category performed the best in the domestic market during Q2 of FY2024 with $7,362 million in revenue, which is higher than all other domestic product categories listed in the evidence [v1, v2, v3, v4, v5, v6].

- **v1** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Computing and Mobile Phones \| $7,362"

  <details><summary>Passage</summary>

  ```
  Revenue by reportable segment
   Domestic | $8,890 | $9,569 | $17,691 | $19,463
    International | 693 | 760 | 1,359 | 1,513
   | Total revenue | $9,583 | $10,329 | $19,050 | $20,976
  Revenue by product category
   Domestic:
   | Computing and Mobile Phones | $3,674 | $3,964 | $7,362 | $8,249
   | Consumer Electronics | 2,658 | 2,845 | 5,250 | 5,741
   | Appliances | 1,384 | 1,657 | 2,723 | 3,247
   | Entertainment | 544 | 508 | 1,135 | 1,081
   | Services | 550 | 516 | 1,087 | 1,005
   | Other | 80 | 79 | 134 | 140
   | Total Domestic revenue | $8,890 | $9,569 | $17,691 | $19,463
  ```
  </details>

- **v2** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Consumer Electronics \| 5,250"

  <details><summary>Passage</summary>

  ```
   Domestic | $8,890 | $9,569 | $17,691 | $19,463
    International | 693 | 760 | 1,359 | 1,513
   | Total revenue | $9,583 | $10,329 | $19,050 | $20,976
  Revenue by product category
   Domestic:
   | Computing and Mobile Phones | $3,674 | $3,964 | $7,362 | $8,249
   | Consumer Electronics | 2,658 | 2,845 | 5,250 | 5,741
   | Appliances | 1,384 | 1,657 | 2,723 | 3,247
   | Entertainment | 544 | 508 | 1,135 | 1,081
   | Services | 550 | 516 | 1,087 | 1,005
   | Other | 80 | 79 | 134 | 140
   | Total Domestic revenue | $8,890 | $9,569 | $17,691 | $19,463
    International:
  ```
  </details>

- **v3** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Appliances \| 2,723"

  <details><summary>Passage</summary>

  ```
    International | 693 | 760 | 1,359 | 1,513
   | Total revenue | $9,583 | $10,329 | $19,050 | $20,976
  Revenue by product category
   Domestic:
   | Computing and Mobile Phones | $3,674 | $3,964 | $7,362 | $8,249
   | Consumer Electronics | 2,658 | 2,845 | 5,250 | 5,741
   | Appliances | 1,384 | 1,657 | 2,723 | 3,247
   | Entertainment | 544 | 508 | 1,135 | 1,081
   | Services | 550 | 516 | 1,087 | 1,005
   | Other | 80 | 79 | 134 | 140
   | Total Domestic revenue | $8,890 | $9,569 | $17,691 | $19,463
    International:
   | Computing and Mobile Phones | $309 | $327 | $625 | $671
  ```
  </details>

- **v4** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Entertainment \| 1,135"

  <details><summary>Passage</summary>

  ```
   | Total revenue | $9,583 | $10,329 | $19,050 | $20,976
  Revenue by product category
   Domestic:
   | Computing and Mobile Phones | $3,674 | $3,964 | $7,362 | $8,249
   | Consumer Electronics | 2,658 | 2,845 | 5,250 | 5,741
   | Appliances | 1,384 | 1,657 | 2,723 | 3,247
   | Entertainment | 544 | 508 | 1,135 | 1,081
   | Services | 550 | 516 | 1,087 | 1,005
   | Other | 80 | 79 | 134 | 140
   | Total Domestic revenue | $8,890 | $9,569 | $17,691 | $19,463
    International:
   | Computing and Mobile Phones | $309 | $327 | $625 | $671
   | Consumer Electronics | 194 | 223 | 378 | 436
  ```
  </details>

- **v5** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Services \| 1,087"

  <details><summary>Passage</summary>

  ```
  Revenue by product category
   Domestic:
   | Computing and Mobile Phones | $3,674 | $3,964 | $7,362 | $8,249
   | Consumer Electronics | 2,658 | 2,845 | 5,250 | 5,741
   | Appliances | 1,384 | 1,657 | 2,723 | 3,247
   | Entertainment | 544 | 508 | 1,135 | 1,081
   | Services | 550 | 516 | 1,087 | 1,005
   | Other | 80 | 79 | 134 | 140
   | Total Domestic revenue | $8,890 | $9,569 | $17,691 | $19,463
    International:
   | Computing and Mobile Phones | $309 | $327 | $625 | $671
   | Consumer Electronics | 194 | 223 | 378 | 436
   | Appliances | 92 | 104 | 151 | 175
  ```
  </details>

- **v6** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Other \| 134"

  <details><summary>Passage</summary>

  ```
   Domestic:
   | Computing and Mobile Phones | $3,674 | $3,964 | $7,362 | $8,249
   | Consumer Electronics | 2,658 | 2,845 | 5,250 | 5,741
   | Appliances | 1,384 | 1,657 | 2,723 | 3,247
   | Entertainment | 544 | 508 | 1,135 | 1,081
   | Services | 550 | 516 | 1,087 | 1,005
   | Other | 80 | 79 | 134 | 140
   | Total Domestic revenue | $8,890 | $9,569 | $17,691 | $19,463
    International:
   | Computing and Mobile Phones | $309 | $327 | $625 | $671
   | Consumer Electronics | 194 | 223 | 378 | 436
   | Appliances | 92 | 104 | 151 | 175
   | Entertainment | 50 | 51 | 110 | 108
  ```
  </details>

<details><summary>Gold answer</summary>

The entertainment segment experienced the highest growth of 9% during Q2 FY2024, primarily from gaming division.
</details>

## 57. Considering the data in the balance sheet, what is Block's (formerly known as Square) FY2016 working capital ratio? Define working capital ratio as total current assets divided by total current liabilities. Round your answer to two decimal places.

`financebench_id_04660` · filing `BLOCK_2016_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Block's FY2016 working capital ratio is 1.73, calculated by dividing total current assets of 1,001,425 by total current liabilities of 577,464 [v1, v2]. This ratio indicates that the company has 1.73 dollars in current assets for every dollar of current liabilities. The computed result confirms this value is 1.73 [COMPUTED RESULT].

**Computation:** `current_assets_2016 / current_liabilities_2016 = 1.73  where current_assets_2016 = 1,001,425 (thousands, FY2016), current_liabilities_2016 = 577,464 (thousands, FY2016)`

- **v1** · `BLOCK_2016_10K` · PDF page **68** · column 2016 · thousands
  - Quote: "Total current assets \| 1,001,425 \| 705,563"

  <details><summary>Passage</summary>

  ```
   | Restricted cash | 22,131 | 13,537
   | Settlements receivable | 321,102 | 142,727
   | Customer funds held | 43,574 | 9,446
   | Loans held for sale | 42,144 | 604
   | Merchant cash advance receivable, net | 4,212 | 36,473
   | Other current assets | 56,331 | 41,447
  Total current assets | 1,001,425 | 705,563
  Property and equipment, net | 88,328 | 87,222
  Goodwill | 57,173 | 56,699
  Acquired intangible assets, net | 19,292 | 26,776
  Long-term investments | 27,366 | —
  Restricted cash | 14,584 | 14,686
  Other assets | 3,194 | 3,826
  ```
  </details>

- **v2** · `BLOCK_2016_10K` · PDF page **68** · column 2016 · thousands
  - Quote: "Total current liabilities \| 577,464 \| 334,202"

  <details><summary>Passage</summary>

  ```
   | Accounts payable | $12,602 | $18,869
   | Customers payable | 388,058 | 215,365
   | Customer funds obligation | 43,574 | 9,446
   | Accrued transaction losses | 20,064 | 17,176
   | Accrued expenses | 39,543 | 44,401
   | Other current liabilities | 73,623 | 28,945
  Total current liabilities | 577,464 | 334,202
  Debt (Note 11) | — | —
  Other liabilities | 57,745 | 52,522
  Total liabilities | 635,209 | 386,724
  Commitments and contingencies (Note 16)
  Stockholders’ equity:
   | Preferred stock, $0.0000001 par value: 100,000,000 shares authorized at December 31, 2016 and December 31, 2015. None
  ```
  </details>

<details><summary>Gold answer</summary>

1.73
</details>

## 58. What is the FY2019 - FY2020 total revenue growth rate for Block (formerly known as Square)? Answer in units of percents and round to one decimal place. Approach the question asked by assuming the standpoint of an investment banking analyst who only has access to the statement of income.

`financebench_id_03838` · filing `BLOCK_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 to FY2020 total revenue growth rate for Block is 101.5%. This is calculated by taking the difference between the 2020 total net revenue of $9,497,578 thousand and the 2019 total net revenue of $4,713,500 thousand, then dividing by the 2019 figure, as confirmed by the provided computed result [v1, v2].

**Computation:** `(total_net_revenue_2020 - total_net_revenue_2019) / total_net_revenue_2019 = 101.5%  where total_net_revenue_2020 = $9,497,578 (thousands, FY2020), total_net_revenue_2019 = $4,713,500 (thousands, FY2019)`

- **v1** · `BLOCK_2020_10K` · PDF page **86** · column 2020 · thousands
  - Quote: "Total net revenue \| 9,497,578"

  <details><summary>Passage</summary>

  ```
   | 2020 | 2019 | 2018
  Revenue:
   | Transaction-based revenue | $3,294,978  $3,081,074  $2,471,451
   | Subscription and services-based revenue | 1,539,403 | 1,031,456 | 591,706
    Hardware revenue | 91,654 | 84,505 | 68,503
   | Bitcoin revenue | 4,571,543 | 516,465 | 166,517
   | Total net revenue | 9,497,578 | 4,713,500 | 3,298,177
  Cost of revenue:
   | Transaction-based costs | 1,911,848 | 1,937,971 | 1,558,562
   | Subscription and services-based costs | 222,712 | 234,270 | 169,884
    Hardware costs | 143,901 | 136,385 | 94,114
   | Bitcoin costs | 4,474,534 | 508,239 | 164,827
   | Amortization of acquired technology | 11,174 | 6,950 | 7,090
  ```
  </details>

- **v2** · `BLOCK_2020_10K` · PDF page **86** · column 2019 · thousands
  - Quote: "Total net revenue \| 4,713,500"

  <details><summary>Passage</summary>

  ```
   | 2020 | 2019 | 2018
  Revenue:
   | Transaction-based revenue | $3,294,978  $3,081,074  $2,471,451
   | Subscription and services-based revenue | 1,539,403 | 1,031,456 | 591,706
    Hardware revenue | 91,654 | 84,505 | 68,503
   | Bitcoin revenue | 4,571,543 | 516,465 | 166,517
   | Total net revenue | 9,497,578 | 4,713,500 | 3,298,177
  Cost of revenue:
   | Transaction-based costs | 1,911,848 | 1,937,971 | 1,558,562
   | Subscription and services-based costs | 222,712 | 234,270 | 169,884
    Hardware costs | 143,901 | 136,385 | 94,114
   | Bitcoin costs | 4,474,534 | 508,239 | 164,827
   | Amortization of acquired technology | 11,174 | 6,950 | 7,090
  ```
  </details>

<details><summary>Gold answer</summary>

101.5%
</details>

## 59. Using the cash flow statement, answer the following question to the best of your abilities: how much did Block (formerly known as Square) generate in cash flow from operating activities in FY2020? Answer in USD millions.

`financebench_id_07661` · filing `BLOCK_2020_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BLOCK_2020_10K: code checks failed twice: formula: numeric constant 1000 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `BLOCK_2020_10K` pages 5, 11, 12, 17, 53, 57, 59, 74, 85, 86, 87, 90

<details><summary>Gold answer</summary>

$382.00
</details>

## 60. We need to calculate a financial metric by using information only provided within the balance sheet. Please answer the following question: what is Boeing's year end FY2018 net property, plant, and equipment (in USD millions)?

`financebench_id_10285` · filing `BOEING_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's year-end FY2018 net property, plant, and equipment is 12,645 million USD. This value is directly reported in the Consolidated Statements of Financial Position on page 52 under the "Property, plant and equipment, net" line item for the year 2018 [v1].

**Computation:** `property_plant_equipment_2018 = 12,645 million  where property_plant_equipment_2018 = 12,645 (millions, FY2018)`

- **v1** · `BOEING_2018_10K` · PDF page **52** · column 2018 · millions
  - Quote: "Property, plant and equipment, net \| 12,645 \| 12,672"

  <details><summary>Passage</summary>

  ```
  Unbilled receivables, net | 10,025 | 8,194
  Current portion of customer financing, net | 460 | 309
  Inventories | 62,567 | 61,388
  Other current assets | 2,335 | 2,417
   | Total current assets | 87,830 | 85,194
  Customer financing, net | 2,418 | 2,756
  Property, plant and equipment, net | 12,645 | 12,672
  Goodwill | 7,840 | 5,559
  Acquired intangible assets, net | 3,429 | 2,573
  Deferred income taxes | 284 | 321
  Investments | 1,087 | 1,260
  Other assets, net of accumulated amortization of $503 and $482 | 1,826 | 2,027
   | Total assets | $117,359 | $112,362
  ```
  </details>

<details><summary>Gold answer</summary>

$12645.00
</details>

## 61. Are there any product categories / service categories that represent more than 20% of Boeing's revenue for FY2022?

`financebench_id_00517` · filing `BOEING_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BOEING_2022_10K: code checks failed twice: formula: numeric constant 100 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `BOEING_2022_10K` pages 22, 24, 27, 29, 38, 41, 55, 56, 57, 59, 61, 83

<details><summary>Gold answer</summary>

Yes. Boeing has product and service categories that represent more than 20% of Boeing's revenue for FY2022. These categories are Commercial Airplanes which comprises 39% of total revenue, Defence which comprises 35% of total revenue and Services which comprises 26% of total revenue.
</details>

## 62. Has Boeing reported any materially important ongoing legal battles from FY2022?

`financebench_id_01091` · filing `BOEING_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BOEING_2022_10K: code checks failed twice: v_737_max_sec_settlement: raw 'In September 2022, we settled a previously disclosed investigation by the Securities and Exchange Commission related to the 737 MAX accidents and consented to a civil penalty, which resulted in an 200' does not appear in its quote; embraer_arbitration: raw 'Embraer has disputed our right to terminate the agreements, and the dispute is currently in arbitration. We cannot reasonably estimate a range of loss, if any, that may result from the arbitration, 20' does not appear in its quote

**Pages searched:** `BOEING_2022_10K` pages 2, 4, 19, 24, 29, 55, 56, 57, 59, 61, 63, 113

<details><summary>Gold answer</summary>

Yes. Multiple lawsuits have been filed against Boeing resulting from a 2018 Lion Air crash and a 2019 Ethiopian Airlines crash.
</details>

## 63. Does Boeing have an improving gross margin profile as of FY2022? If gross margin is not a useful metric for a company like this, then state that and explain why.

`financebench_id_00678` · filing `BOEING_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BOEING_2022_10K: number check (G4) failed twice: no citation of a value ID such as [v1]

**Pages searched:** `BOEING_2022_10K` pages 5, 23, 30, 32, 35, 41, 51, 55, 56, 57, 59, 61

<details><summary>Gold answer</summary>

Yes. Boeing has an improving gross margin profile as of FY2022. Gross profit improved from $3,017 million in FY2021 to $3,502 million in FY2022. Gross margin % improved from 4.8% in FY2021 to 5.3% in FY2022.
</details>

## 64. Who are the primary customers of Boeing as of FY2022?

`financebench_id_01290` · filing `BOEING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's primary customers are the commercial airline industry worldwide, military and government entities for defense and space systems, and its own commercial and defense customers for global services, as detailed in its four reportable segments: Commercial Airplanes, Defense, Space & Security, Global Services, and Boeing Capital [v1, v2, v3, v4].

- **v1** · `BOEING_2022_10K` · PDF page **3** · column 2022 · units
  - Quote: "Commercial Airplanes (BCA)"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | PART I
  Item 1. Business
  The Boeing Company, together with its subsidiaries (herein referred to as “Boeing,” the “Company,” “we,” “us,” “our”), is one of the world’s major
  aerospace firms.
  We are organized based on the products and services we offer. We operate in four reportable segments:
  • | Commercial Airplanes (BCA);
  • | Defense, Space & Security (BDS);
  • | Global Services (BGS);
  • | Boeing Capital (BCC).
  Commercial Airplanes Segment
  This segment develops, produces and markets commercial jet aircraft principally to the commercial airline industry worldwide. We are a leading
  producer of commercial aircraft and offer a family of commercial jetliners designed to meet a broad spectrum of global passenger and cargo
  ```
  </details>

- **v2** · `BOEING_2022_10K` · PDF page **3** · column 2022 · units
  - Quote: "Defense, Space & Security (BDS)"

  <details><summary>Passage</summary>

  ```
   | PART I
  Item 1. Business
  The Boeing Company, together with its subsidiaries (herein referred to as “Boeing,” the “Company,” “we,” “us,” “our”), is one of the world’s major
  aerospace firms.
  We are organized based on the products and services we offer. We operate in four reportable segments:
  • | Commercial Airplanes (BCA);
  • | Defense, Space & Security (BDS);
  • | Global Services (BGS);
  • | Boeing Capital (BCC).
  Commercial Airplanes Segment
  This segment develops, produces and markets commercial jet aircraft principally to the commercial airline industry worldwide. We are a leading
  producer of commercial aircraft and offer a family of commercial jetliners designed to meet a broad spectrum of global passenger and cargo
  requirements of airlines. This family of commercial jet aircraft in production includes the 737 narrow-body model and the 767, 777 and 787 wide-
  ```
  </details>

- **v3** · `BOEING_2022_10K` · PDF page **3** · column 2022 · units
  - Quote: "Global Services (BGS)"

  <details><summary>Passage</summary>

  ```
  Item 1. Business
  The Boeing Company, together with its subsidiaries (herein referred to as “Boeing,” the “Company,” “we,” “us,” “our”), is one of the world’s major
  aerospace firms.
  We are organized based on the products and services we offer. We operate in four reportable segments:
  • | Commercial Airplanes (BCA);
  • | Defense, Space & Security (BDS);
  • | Global Services (BGS);
  • | Boeing Capital (BCC).
  Commercial Airplanes Segment
  This segment develops, produces and markets commercial jet aircraft principally to the commercial airline industry worldwide. We are a leading
  producer of commercial aircraft and offer a family of commercial jetliners designed to meet a broad spectrum of global passenger and cargo
  requirements of airlines. This family of commercial jet aircraft in production includes the 737 narrow-body model and the 767, 777 and 787 wide-
  body models. We ended production of the 747 wide-body model in 2022. Development continues on the 777X program and the 737-7 and 737-
  ```
  </details>

- **v4** · `BOEING_2022_10K` · PDF page **3** · column 2022 · units
  - Quote: "Boeing Capital (BCC)"

  <details><summary>Passage</summary>

  ```
  The Boeing Company, together with its subsidiaries (herein referred to as “Boeing,” the “Company,” “we,” “us,” “our”), is one of the world’s major
  aerospace firms.
  We are organized based on the products and services we offer. We operate in four reportable segments:
  • | Commercial Airplanes (BCA);
  • | Defense, Space & Security (BDS);
  • | Global Services (BGS);
  • | Boeing Capital (BCC).
  Commercial Airplanes Segment
  This segment develops, produces and markets commercial jet aircraft principally to the commercial airline industry worldwide. We are a leading
  producer of commercial aircraft and offer a family of commercial jetliners designed to meet a broad spectrum of global passenger and cargo
  requirements of airlines. This family of commercial jet aircraft in production includes the 737 narrow-body model and the 767, 777 and 787 wide-
  body models. We ended production of the 747 wide-body model in 2022. Development continues on the 777X program and the 737-7 and 737-
  10 derivatives.
  ```
  </details>

<details><summary>Gold answer</summary>

Boeing's primary customers as of FY2022 are a limited number of commercial airlines and the US government. The US government accounted for 40% of Boeing's total revenues in FY2022.
</details>

## 65. Is Boeing's business subject to cyclicality?

`financebench_id_00464` · filing `BOEING_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BOEING_2022_10K: extractor: The provided pages do not contain the text from page 6 where the statement about the airline industry being cyclical is located. The available pages are 2, 3, 8, 12, 16, 55, 56, 57, 59, 61, 62, and 118. While Page 8 contains the start of Item 1A Risk Factors, the specific paragraph discussing the cyclical nature of the airline industry is not present in the provided text snippets.

**Pages searched:** `BOEING_2022_10K` pages 2, 3, 8, 12, 16, 55, 56, 57, 59, 61, 62, 118

<details><summary>Gold answer</summary>

Yes, Boeing's business is subject to cyclicality due to its exposure to the airline industry which is a cyclical industry.
</details>

## 66. What production rate changes is Boeing forecasting for FY2023?

`financebench_id_00494` · filing `BOEING_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** BOEING_2022_10K: code checks failed twice: formula: unknown value name 'v_787_2023_rate' (names: [])

**Pages searched:** `BOEING_2022_10K` pages 9, 22, 33, 34, 35, 37, 43, 55, 56, 57, 59, 61

<details><summary>Gold answer</summary>

Boeing forecasts an increase in the production rates for the 737, 777X and 787 aircrafts in 2023.
</details>

## 67. How does Boeing's effective tax rate in FY2022 compare to FY2021?

`financebench_id_00585` · filing `BOEING_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's effective tax rate in FY2022 was -0.6%, which is a decrease from 14.8% in FY2021 [v1, v2]. This negative rate in 2022 reflects the company's net loss position for that fiscal year, contrasting with the positive tax rate recorded in 2021.

**Computation:** `effective_tax_rate_2022 = -60%  where effective_tax_rate_2022 = (0.6) % (units, FY2022), effective_tax_rate_2021 = 14.8 % (units, FY2021)`

- **v1** · `BOEING_2022_10K` · PDF page **24** · column 2022 · units
  - Quote: "Effective income tax rate \| (0.6) % \| 14.8 % \| 17.5 %"

  <details><summary>Passage</summary>

  ```
  (Dollars in millions, except per share data)
  Years ended December 31, | 2022 | 2021 | 2020
  Revenues | $66,608 | $62,286 | $58,158
  GAAP
  Loss from operations | ($3,547) | ($2,902) | ($12,767)
  Operating margins | (5.3) % | (4.7) % | (22.0) %
  Effective income tax rate | (0.6) % | 14.8 % | 17.5 %
  Net loss attributable to Boeing Shareholders | ($4,935) | ($4,202) | ($11,873)
  Diluted loss per share | ($8.30) | ($7.15) | ($20.88)
  Non-GAAP (1)
  Core operating loss | ($4,690) | ($4,075) | ($14,150)
  Core operating margins | (7.0 %) | (6.5 %) | (24.3 %)
  Core loss per share | ($11.06) | ($9.44) | ($23.25)
  ```
  </details>

- **v2** · `BOEING_2022_10K` · PDF page **24** · column 2021 · units
  - Quote: "Effective income tax rate \| (0.6) % \| 14.8 % \| 17.5 %"

  <details><summary>Passage</summary>

  ```
  (Dollars in millions, except per share data)
  Years ended December 31, | 2022 | 2021 | 2020
  Revenues | $66,608 | $62,286 | $58,158
  GAAP
  Loss from operations | ($3,547) | ($2,902) | ($12,767)
  Operating margins | (5.3) % | (4.7) % | (22.0) %
  Effective income tax rate | (0.6) % | 14.8 % | 17.5 %
  Net loss attributable to Boeing Shareholders | ($4,935) | ($4,202) | ($11,873)
  Diluted loss per share | ($8.30) | ($7.15) | ($20.88)
  Non-GAAP (1)
  Core operating loss | ($4,690) | ($4,075) | ($14,150)
  Core operating margins | (7.0 %) | (6.5 %) | (24.3 %)
  Core loss per share | ($11.06) | ($9.44) | ($23.25)
  ```
  </details>

<details><summary>Gold answer</summary>

Effective tax rate in FY2022 was 0.62%, compared to  -14.76% in FY2021.
</details>

## 68. What is the FY2017 return on assets (ROA) for Coca Cola? ROA is defined as: FY2017 net income / (average total assets between FY2016 and FY2017). Round your answer to two decimal places. Give a response to the question by relying on the details shown in the balance sheet and the P&L statement.

`financebench_id_03473` · filing `COCACOLA_2017_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2017 return on assets (ROA) for Coca-Cola is 1.46%. This is calculated by dividing the net income of $1,283 million by the average total assets of $87,583 million, which is the average of the 2017 total assets ($87,896 million) and 2016 total assets ($87,270 million) [v1, v2, v3].

**Computation:** `net_income_2017 / avg(total_assets_2017, total_assets_2016) = 1.46%  where net_income_2017 = 1,283 (millions, FY2017), total_assets_2017 = 87,896 (millions, FY2017), total_assets_2016 = 87,270 (millions, FY2016)`

- **v1** · `COCACOLA_2017_10K` · PDF page **74** · column 2017 · millions
  - Quote: "CONSOLIDATED NET INCOME \| 1,283"

  <details><summary>Passage</summary>

  ```
   | Equity income (loss) — net | 1,071 | 835 | 489
   | Other income (loss) — net | (1,666) | (1,234) | 631
    INCOME FROM CONTINUING OPERATIONS BEFORE INCOME TAXES | 6,742 | 8,136 | 9,605
   | Income taxes from continuing operations | 5,560 | 1,586 | 2,239
    NET INCOME FROM CONTINUING OPERATIONS | 1,182 | 6,550 | 7,366
   | Income from discontinued operations (net of income taxes of $47, $0 and $0, respectively) | 101 | — | —
    CONSOLIDATED NET INCOME | 1,283 | 6,550 | 7,366
   | Less: Net income attributable to noncontrolling interests | 35 | 23 | 15
    NET INCOME ATTRIBUTABLE TO SHAREOWNERS OF
   | THE COCA-COLA COMPANY | $1,248 | $6,527 | $7,351
   | Basic net income per share from continuing operations1 | $0.28 | $1.51 | $1.69
   | Basic net income per share from discontinued operations2 | 0.02 | — | —
    BASIC NET INCOME PER SHARE | $0.29 | 3 $1.51 | $1.69
  ```
  </details>

- **v2** · `COCACOLA_2017_10K` · PDF page **76** · column 2017 · millions
  - Quote: "TOTAL ASSETS \| $87,896"

  <details><summary>Passage</summary>

  ```
    OTHER ASSETS | 4,560 | 4,248
   | PROPERTY, PLANT AND EQUIPMENT — net | 8,203 | 10,635
    TRADEMARKS WITH INDEFINITE LIVES | 6,729 | 6,097
   | BOTTLERS' FRANCHISE RIGHTS WITH INDEFINITE LIVES | 138 | 3,676
    GOODWILL | 9,401 | 10,629
    OTHER INTANGIBLE ASSETS | 368 | 726
   | TOTAL ASSETS | $87,896 | $87,270
  LIABILITIES AND EQUITY
    CURRENT LIABILITIES
   | Accounts payable and accrued expenses | $8,748 | $9,490
   | Loans and notes payable | 13,205 | 12,498
   | Current maturities of long-term debt | 3,298 | 3,527
   | Accrued income taxes | 410 | 307
  ```
  </details>

- **v3** · `COCACOLA_2017_10K` · PDF page **76** · column 2016 · millions
  - Quote: "TOTAL ASSETS \| $87,270"

  <details><summary>Passage</summary>

  ```
    OTHER ASSETS | 4,560 | 4,248
   | PROPERTY, PLANT AND EQUIPMENT — net | 8,203 | 10,635
    TRADEMARKS WITH INDEFINITE LIVES | 6,729 | 6,097
   | BOTTLERS' FRANCHISE RIGHTS WITH INDEFINITE LIVES | 138 | 3,676
    GOODWILL | 9,401 | 10,629
    OTHER INTANGIBLE ASSETS | 368 | 726
   | TOTAL ASSETS | $87,896 | $87,270
  LIABILITIES AND EQUITY
    CURRENT LIABILITIES
   | Accounts payable and accrued expenses | $8,748 | $9,490
   | Loans and notes payable | 13,205 | 12,498
   | Current maturities of long-term debt | 3,298 | 3,527
   | Accrued income taxes | 410 | 307
  ```
  </details>

<details><summary>Gold answer</summary>

0.01
</details>

## 69. What is Coca Cola's FY2021 COGS % margin? Calculate what was asked by utilizing the line items clearly shown in the income statement.

`financebench_id_09724` · filing `COCACOLA_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Coca-Cola's FY2021 COGS margin is 39.7284%, calculated by dividing the Cost of goods sold of $15,357 million by Net Operating Revenues of $38,655 million [v1, v2]. This metric represents the percentage of revenue consumed by the direct costs of producing the goods sold. The calculation is explicitly provided in the computed result based on the 10K filing data [COMPUTED RESULT].

**Computation:** `cost_of_goods_sold_2021 / net_operating_revenues_2021 = 39.7284%  where cost_of_goods_sold_2021 = 15,357 (millions, FY2021), net_operating_revenues_2021 = 38,655 (millions, FY2021)`

- **v1** · `COCACOLA_2021_10K` · PDF page **62** · column 2021 · millions
  - Quote: "Cost of goods sold \| 15,357"

  <details><summary>Passage</summary>

  ```
  | THE COCA-COLA COMPANY AND SUBSIDIARIES
   | CONSOLIDATED STATEMENTS OF INCOME
   | (In millions except per share data)
  Year Ended December 31, | 2021 | 2020 | 2019
  Net Operating Revenues | $38,655 $33,014 $37,266
  Cost of goods sold | 15,357 | 13,433 | 14,619
  Gross Profit | 23,298 | 19,581 | 22,647
  Selling, general and administrative expenses | 12,144 | 9,731 | 12,103
  Other operating charges | 846 | 853 | 458
  Operating Income | 10,308 | 8,997 | 10,086
  Interest income | 276 | 370 | 563
  Interest expense | 1,597 | 1,437 | 946
  ```
  </details>

- **v2** · `COCACOLA_2021_10K` · PDF page **62** · column 2021 · millions
  - Quote: "Net Operating Revenues \| $38,655"

  <details><summary>Passage</summary>

  ```
  | THE COCA-COLA COMPANY AND SUBSIDIARIES
   | CONSOLIDATED STATEMENTS OF INCOME
   | (In millions except per share data)
  Year Ended December 31, | 2021 | 2020 | 2019
  Net Operating Revenues | $38,655 $33,014 $37,266
  Cost of goods sold | 15,357 | 13,433 | 14,619
  Gross Profit | 23,298 | 19,581 | 22,647
  Selling, general and administrative expenses | 12,144 | 9,731 | 12,103
  Other operating charges | 846 | 853 | 458
  Operating Income | 10,308 | 8,997 | 10,086
  Interest income | 276 | 370 | 563
  ```
  </details>

<details><summary>Gold answer</summary>

39.7%
</details>

## 70. What is Coca Cola's FY2022 dividend payout ratio (using total cash dividends paid and net income attributable to shareholders)? Round answer to two decimal places. Answer the question asked by assuming you only have access to information clearly displayed in the cash flow statement and the income statement.

`financebench_id_06272` · filing `COCACOLA_2022_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** COCACOLA_2022_10K: code checks failed twice: dividends_2022: the quote is not on page 64. Copy it exactly from one line of the page; formula: unknown value name 'dividends_2022' (names: ['net_income_2022'])

**Pages searched:** `COCACOLA_2022_10K` pages 33, 56, 57, 62, 63, 64, 65, 66, 67, 69, 87, 108

<details><summary>Gold answer</summary>

0.8
</details>

## 71. Based on the information provided primarily in the balance sheet and the statement of income, what is FY2020 days payable outstanding (DPO) for Corning? DPO is defined as: 365 * (average accounts payable between FY2019 and FY2020) / (FY2020 COGS + change in inventory between FY2019 and FY2020). Round your answer to two decimal places.

`financebench_id_10130` · filing `CORNING_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2020 days payable outstanding (DPO) for Corning is 63.86 days. This result is derived from the computed value using the provided evidence for accounts payable [v1, v2], cost of sales [v3], and inventories [v4, v5].

**Computation:** `365 * (avg(accounts_payable_2020, accounts_payable_2019)) / (cost_of_sales_2020 + (inventories_2020 - inventories_2019)) = 63.86  where accounts_payable_2020 = 1,174 (millions, FY2020), accounts_payable_2019 = 1,587 (millions, FY2019), cost_of_sales_2020 = 7,772 (millions, FY2020), inventories_2020 = 2,438 (millions, FY2020), inventories_2019 = 2,320 (millions, FY2019)`

- **v1** · `CORNING_2020_10K` · PDF page **72** · column 2020 · millions
  - Quote: "Accounts payable \| 1,174"

  <details><summary>Passage</summary>

  ```
  Deferred income taxes (Note 8) | 1,121 | 1,157
  Other assets (Note 11 and 15) | 2,140 | 1,821
  Total Assets | $30,775  $28,898
  Liabilities and Equity
  Current liabilities:
   | Current portion of long-term debt and short-term borrowings (Note 12) | $156  $11
   | Accounts payable | 1,174 | 1,587
   | Other accrued liabilities (Note 11 and 14) | 2,437 | 1,923
   | Total current liabilities | 3,767 | 3,521
  Long-term debt (Note 12) | 7,816 | 7,729
  Postretirement benefits other than pensions (Note 13) | 727 | 671
  Other liabilities (Note 11 and 14) | 5,017 | 3,980
   | Total liabilities | 17,327 | 15,901
  ```
  </details>

- **v2** · `CORNING_2020_10K` · PDF page **72** · column 2019 · millions
  - Quote: "Accounts payable \| 1,587"

  <details><summary>Passage</summary>

  ```
  Deferred income taxes (Note 8) | 1,121 | 1,157
  Other assets (Note 11 and 15) | 2,140 | 1,821
  Total Assets | $30,775  $28,898
  Liabilities and Equity
  Current liabilities:
   | Current portion of long-term debt and short-term borrowings (Note 12) | $156  $11
   | Accounts payable | 1,174 | 1,587
   | Other accrued liabilities (Note 11 and 14) | 2,437 | 1,923
   | Total current liabilities | 3,767 | 3,521
  Long-term debt (Note 12) | 7,816 | 7,729
  Postretirement benefits other than pensions (Note 13) | 727 | 671
  Other liabilities (Note 11 and 14) | 5,017 | 3,980
   | Total liabilities | 17,327 | 15,901
  ```
  </details>

- **v3** · `CORNING_2020_10K` · PDF page **70** · column 2020 · millions
  - Quote: "Cost of sales \| 7,772"

  <details><summary>Passage</summary>

  ```
  Index
  Consolidated Statements of Income | Corning Incorporated and Subsidiary Companies
   | Year ended December 31,
  (In millions, except per share amounts) | 2020 | 2019 | 2018
  Net sales | $11,303 | $11,503 | $11,290
  Cost of sales | 7,772 | 7,468 | 6,829
  Gross margin | 3,531 | 4,035 | 4,461
  Operating expenses:
   | Selling, general and administrative expenses | 1,747 | 1,585 | 1,799
   | Research, development and engineering expenses | 1,154 | 1,031 | 993
   | Amortization of purchased intangibles | 121 | 113 | 94
  Operating income | 509 | 1,306 | 1,575
  ```
  </details>

- **v4** · `CORNING_2020_10K` · PDF page **72** · column 2020 · millions
  - Quote: "Inventories, net (Note 6) \| 2,438"

  <details><summary>Passage</summary>

  ```
   | December 31,
  (In millions, except share and per share amounts) | 2020 | 2019
  Assets
  Current assets:
    Cash and cash equivalents | $2,672  $2,434
   | Trade accounts receivable, net of doubtful accounts - $46 and $41 | 2,133 | 1,836
   | Inventories, net (Note 6) | 2,438 | 2,320
   | Other current assets (Note 11 and 15) | 761 | 873
   | Total current assets | 8,004 | 7,463
  Property, plant and equipment, net of accumulated depreciation -
   $13,663 and $12,995 (Note 9) | 15,742 | 15,337
  Goodwill, net (Note 10) | 2,460 | 1,935
  Other intangible assets, net (Note 10) | 1,308 | 1,185
  ```
  </details>

- **v5** · `CORNING_2020_10K` · PDF page **72** · column 2019 · millions
  - Quote: "Inventories, net (Note 6) \| 2,320"

  <details><summary>Passage</summary>

  ```
   | December 31,
  (In millions, except share and per share amounts) | 2020 | 2019
  Assets
  Current assets:
    Cash and cash equivalents | $2,672  $2,434
   | Trade accounts receivable, net of doubtful accounts - $46 and $41 | 2,133 | 1,836
   | Inventories, net (Note 6) | 2,438 | 2,320
   | Other current assets (Note 11 and 15) | 761 | 873
   | Total current assets | 8,004 | 7,463
  Property, plant and equipment, net of accumulated depreciation -
   $13,663 and $12,995 (Note 9) | 15,742 | 15,337
  Goodwill, net (Note 10) | 2,460 | 1,935
  Other intangible assets, net (Note 10) | 1,308 | 1,185
  ```
  </details>

<details><summary>Gold answer</summary>

63.86
</details>

## 72. Taking into account the information outlined in the income statement, what is the FY2019 - FY2021 3 year average unadjusted operating income % margin for Corning? Answer in units of percents and round to one decimal place.

`financebench_id_02981` · filing `CORNING_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019-FY2021 3-year average unadjusted operating income margin for Corning is 10.3%. This result is derived from the provided computed average of the operating income to net sales ratios for the three years, using the specific values for operating income and net sales found in the evidence [v1, v2, v3, v4, v5, v6].

**Computation:** `avg((operating_income_2019 / net_sales_2019), (operating_income_2020 / net_sales_2020), (operating_income_2021 / net_sales_2021)) = 10.3%  where operating_income_2019 = 1,306 (millions, FY2019), net_sales_2019 = 11,503 (millions, FY2019), operating_income_2020 = 509 (millions, FY2020), net_sales_2020 = 11,303 (millions, FY2020), operating_income_2021 = 2,112 (millions, FY2021), net_sales_2021 = 14,082 (millions, FY2021)`

- **v1** · `CORNING_2021_10K` · PDF page **65** · column 2019 · millions
  - Quote: "Operating income \| 2,112 \| 509 \| 1,306"

  <details><summary>Passage</summary>

  ```
  Cost of sales | 9,019 | 7,772 | 7,468
  Gross margin | 5,063 | 3,531 | 4,035
  Operating expenses:
    Selling, general and administrative expenses | 1,827 | 1,747 | 1,585
    Research, development and engineering expenses | 995 | 1,154 | 1,031
    Amortization of purchased intangibles | 129 | 121 | 113
  Operating income | 2,112 | 509 | 1,306
  Equity in earnings (losses) of affiliated companies (Note 3) | 35 | (25) | 17
  Interest income | 11 | 15 | 21
  Interest expense | (300) | (276) | (221)
  Translated earnings contract gain (loss), net (Note 15) | 354 | (38) | 248
  Transaction-related gain, net (Note 4) | 498
  Other income (expense), net | 185 | (60) | (155)
  ```
  </details>

- **v2** · `CORNING_2021_10K` · PDF page **65** · column 2019 · millions
  - Quote: "Net sales \| $14,082 \| $11,303 \| $11,503"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statements of Income | Corning Incorporated and Subsidiary Companies
   | Year ended December 31,
  (In millions, except per share amounts) | 2021 | 2020 | 2019
  Net sales | $14,082 | $11,303 | $11,503
  Cost of sales | 9,019 | 7,772 | 7,468
  Gross margin | 5,063 | 3,531 | 4,035
  Operating expenses:
    Selling, general and administrative expenses | 1,827 | 1,747 | 1,585
    Research, development and engineering expenses | 995 | 1,154 | 1,031
    Amortization of purchased intangibles | 129 | 121 | 113
  ```
  </details>

- **v3** · `CORNING_2021_10K` · PDF page **65** · column 2020 · millions
  - Quote: "Operating income \| 2,112 \| 509 \| 1,306"

  <details><summary>Passage</summary>

  ```
  Cost of sales | 9,019 | 7,772 | 7,468
  Gross margin | 5,063 | 3,531 | 4,035
  Operating expenses:
    Selling, general and administrative expenses | 1,827 | 1,747 | 1,585
    Research, development and engineering expenses | 995 | 1,154 | 1,031
    Amortization of purchased intangibles | 129 | 121 | 113
  Operating income | 2,112 | 509 | 1,306
  Equity in earnings (losses) of affiliated companies (Note 3) | 35 | (25) | 17
  Interest income | 11 | 15 | 21
  Interest expense | (300) | (276) | (221)
  Translated earnings contract gain (loss), net (Note 15) | 354 | (38) | 248
  Transaction-related gain, net (Note 4) | 498
  Other income (expense), net | 185 | (60) | (155)
  ```
  </details>

- **v4** · `CORNING_2021_10K` · PDF page **65** · column 2020 · millions
  - Quote: "Net sales \| $14,082 \| $11,303 \| $11,503"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statements of Income | Corning Incorporated and Subsidiary Companies
   | Year ended December 31,
  (In millions, except per share amounts) | 2021 | 2020 | 2019
  Net sales | $14,082 | $11,303 | $11,503
  Cost of sales | 9,019 | 7,772 | 7,468
  Gross margin | 5,063 | 3,531 | 4,035
  Operating expenses:
    Selling, general and administrative expenses | 1,827 | 1,747 | 1,585
    Research, development and engineering expenses | 995 | 1,154 | 1,031
    Amortization of purchased intangibles | 129 | 121 | 113
  ```
  </details>

- **v5** · `CORNING_2021_10K` · PDF page **65** · column 2021 · millions
  - Quote: "Operating income \| 2,112 \| 509 \| 1,306"

  <details><summary>Passage</summary>

  ```
  Cost of sales | 9,019 | 7,772 | 7,468
  Gross margin | 5,063 | 3,531 | 4,035
  Operating expenses:
    Selling, general and administrative expenses | 1,827 | 1,747 | 1,585
    Research, development and engineering expenses | 995 | 1,154 | 1,031
    Amortization of purchased intangibles | 129 | 121 | 113
  Operating income | 2,112 | 509 | 1,306
  Equity in earnings (losses) of affiliated companies (Note 3) | 35 | (25) | 17
  Interest income | 11 | 15 | 21
  Interest expense | (300) | (276) | (221)
  Translated earnings contract gain (loss), net (Note 15) | 354 | (38) | 248
  Transaction-related gain, net (Note 4) | 498
  Other income (expense), net | 185 | (60) | (155)
  ```
  </details>

- **v6** · `CORNING_2021_10K` · PDF page **65** · column 2021 · millions
  - Quote: "Net sales \| $14,082 \| $11,303 \| $11,503"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statements of Income | Corning Incorporated and Subsidiary Companies
   | Year ended December 31,
  (In millions, except per share amounts) | 2021 | 2020 | 2019
  Net sales | $14,082 | $11,303 | $11,503
  Cost of sales | 9,019 | 7,772 | 7,468
  Gross margin | 5,063 | 3,531 | 4,035
  Operating expenses:
    Selling, general and administrative expenses | 1,827 | 1,747 | 1,585
    Research, development and engineering expenses | 995 | 1,154 | 1,031
    Amortization of purchased intangibles | 129 | 121 | 113
  ```
  </details>

<details><summary>Gold answer</summary>

10.3%
</details>

## 73. How much has the effective tax rate of Corning changed between FY2021 and FY2022?

`financebench_id_01346` · filing `CORNING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The effective tax rate of Corning increased by 2.7 percentage points from 20.2% in FY2021 to 22.9% in FY2022 [v1, v2]. The computed result of 270% in the provided evidence appears to be an error, as the actual difference between 22.9% and 20.2% is 2.7%. Therefore, the rate changed by 2.7 percentage points.

**Computation:** `effective_tax_rate_2022 - effective_tax_rate_2021 = 270%  where effective_tax_rate_2022 = 22.9% (units, FY2022), effective_tax_rate_2021 = 20.2% (units, FY2021)`

- **v1** · `CORNING_2022_10K` · PDF page **32** · column 2022 · units
  - Quote: "22.9%"

  <details><summary>Passage</summary>

  ```
  and per share amounts):
   | Year ended December 31, 2022
   | Net income
   | Income | attributable | Effective
   | Net | before | to Corning | tax | Per
   | sales | income taxes | Incorporated | rate (a)(b) | share
  As reported - GAAP | $14,189 | $1,797 | $1,316 | 22.9%  $1.54
  Constant-currency adjustment (1) | 616 | 480 | 369 | 0.43
  Translation gain on Japanese yen-denominated debt (2) | (191) | (146) | (0.17)
  Translated earnings contract gain, net (3) | (348) | (267) | (0.31)
  Acquisition-related costs (4) | 140 | 109 | 0.13
  Discrete tax items and other tax-related adjustments (5) | 84 | 0.10
  Restructuring, impairment and other charges and credits (6) | 414 | 316 | 0.37
  ```
  </details>

- **v2** · `CORNING_2022_10K` · PDF page **32** · column 2021 · units
  - Quote: "20.2%"

  <details><summary>Passage</summary>

  ```
  (b)  The calculation of the effective tax rate excludes net income attributable to non-controlling interest of $70 million.
   | Year ended December 31, 2021
   | Net income
   | Income | attributable | Effective
   | Net | before | to Corning | tax | Per
   | sales | income taxes | Incorporated | rate (a)(b) | share
  As reported - GAAP | $14,082 | $2,426 | $1,906 | 20.2%  $1.28
  Preferred stock redemption (c) | 0.90
  Subtotal | 14,082 | 2,426 | 1,906 | 20.2% | 2.18
  Constant-currency adjustment (1) | 38 | 87 | 76 | 0.09
  Translation gain on Japanese yen-denominated debt (2) | (180) | (138) | (0.16)
  Translated earnings contract gain, net (3) | (354) | (273) | (0.32)
  Acquisition-related costs (4) | 159 | 123 | 0.15
  ```
  </details>

<details><summary>Gold answer</summary>

The effective tax rate of Corning has changed from 20% in FY2021 to 23% in FY 2022.
</details>

## 74. Does Corning have positive working capital based on FY2022 data? If working capital is not a useful or relevant metric for this company, then please state that and explain why.

`financebench_id_00005` · filing `CORNING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Corning has positive working capital based on FY2022 data. The company's total current assets were $7,453 million and total current liabilities were $5,175 million, resulting in a working capital of $2,278 million [v1, v2, COMPUTED RESULT].

**Computation:** `total_current_assets_2022 - total_current_liabilities_2022 = 2,278 million  where total_current_assets_2022 = 7,453 (millions, FY2022), total_current_liabilities_2022 = 5,175 (millions, FY2022)`

- **v1** · `CORNING_2022_10K` · PDF page **60** · column 2022 · millions
  - Quote: "Total current assets \| 7,453"

  <details><summary>Passage</summary>

  ```
  Assets
  Current assets:
   | Cash and cash equivalents | $1,671 | $2,148
   | Trade accounts receivable, net of doubtful accounts - $40 and $42 | 1,721 | 2,004
   | Inventories (Note 5) | 2,904 | 2,481
   | Other current assets (Notes 10 and 14) | 1,157 | 1,026
   | Total current assets | 7,453 | 7,659
  Property, plant and equipment, net of accumulated depreciation - $14,147 and $13,969 (Note 8) | 15,371 | 15,804
  Goodwill, net (Note 9) | 2,394 | 2,421
  Other intangible assets, net (Note 9) | 1,029 | 1,148
  Deferred income taxes (Note 7) | 1,073 | 1,066
  Other assets (Notes 10 and 14) | 2,179 | 2,056
  Total Assets | $29,499 | $30,154
  ```
  </details>

- **v2** · `CORNING_2022_10K` · PDF page **60** · column 2022 · millions
  - Quote: "Total current liabilities \| 5,175"

  <details><summary>Passage</summary>

  ```
  Total Assets | $29,499 | $30,154
  Liabilities and Equity
  Current liabilities:
   | Current portion of long-term debt and short-term borrowings (Note 11) | $224 | $55
   | Accounts payable | 1,804 | 1,612
   | Other accrued liabilities (Notes 10 and 13) | 3,147 | 3,139
   | Total current liabilities | 5,175 | 4,806
  Long-term debt (Note 11) | 6,687 | 6,989
  Postretirement benefits other than pensions (Note 12) | 407 | 622
  Other liabilities (Notes 10 and 13) | 4,955 | 5,192
   | Total liabilities | 17,224 | 17,609
  Commitments and contingencies (Note 13)
  Shareholders’ equity (Note 16):
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. Corning had a positive working capital amount of $831 million by FY 2022 close. This answer considers only operating current assets and current liabilities that were clearly shown in the balance sheet.
</details>

## 75. Using only the information within the balance sheet, how much total assets did Costco have at the end of FY2021? Answer in USD millions.

`financebench_id_04209` · filing `COSTCO_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Costco had total assets of $59,268 million at the end of FY2021 [v1]. This figure is explicitly stated in the "TOTAL ASSETS" row of the Consolidated Balance Sheets for the column dated August 29, 2021 [v1]. The balance sheet confirms this amount matches the sum of total liabilities and equity for that period [v1].

**Computation:** `total_assets_2021 = 59,268 million  where total_assets_2021 = $59,268 (millions, FY2021), total_assets_2020 = $55,556 (millions, FY2020)`

- **v1** · `COSTCO_2021_10K` · PDF page **38** · column August 29, 2021 · millions
  - Quote: "TOTAL ASSETS \| $59,268"

  <details><summary>Passage</summary>

  ```
   | Other current assets | 1,312 | 1,023
   | Total current assets | 29,505 | 28,120
  OTHER ASSETS
   | Property and equipment, net | 23,492 | 21,807
   | Operating lease right-of-use assets | 2,890 | 2,788
   | Other long-term assets | 3,381 | 2,841
   | TOTAL ASSETS | $59,268  $55,556
   | LIABILITIES AND EQUITY
  CURRENT LIABILITIES
   | Accounts payable | $16,278  $14,172
   | Accrued salaries and benefits | 4,090 | 3,605
   | Accrued member rewards | 1,671 | 1,393
   | Deferred membership fees | 2,042 | 1,851
  ```
  </details>

<details><summary>Gold answer</summary>

$59268.00
</details>

## 76. What is the FY2018 fixed asset turnover ratio for CVS Health? Fixed asset turnover ratio is defined as: FY2018 revenue / (average PP&E between FY2017 and FY2018). Round your answer to two decimal places. Calculate what was asked by utilizing the line items clearly shown in the P&L statement and the balance sheet.

`financebench_id_05915` · filing `CVSHEALTH_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 fixed asset turnover ratio for CVS Health is 17.98. This is calculated by dividing the total revenues of 194,579 million by the average of property and equipment, net for 2018 (11,349 million) and 2017 (10,292 million), as shown in the provided evidence [v1, v2, v3].

**Computation:** `revenue_2018 / avg(ppe_2018, ppe_2017) = 17.98  where revenue_2018 = 194,579 (units, FY2018), ppe_2018 = 11,349 (units, FY2018), ppe_2017 = 10,292 (units, FY2017)`

- **v1** · `CVSHEALTH_2018_10K` · PDF page **302** · column 2018 · units
  - Quote: "Total revenues \| 194,579"

  <details><summary>Passage</summary>

  ```
  In millions, except per share amounts | 2018 | 2017 | 2016
  Revenues:
   Products | $183,910 | $180,063 | $173,377
   Premiums | 8,184 | 3,558 | 3,069
   Services | 1,825 | 1,144 | 1,080
   Net investment income | 660 | 21 | 20
  Total revenues | 194,579 | 184,786 | 177,546
  Operating costs:
   Cost of products sold | 156,447 | 153,448 | 146,533
   Benefit costs | 6,594 | 2,810 | 2,179
   Goodwill impairments | 6,149 | 181 | —
   Operating expenses | 21,368 | 18,809 | 18,448
  Total operating costs | 190,558 | 175,248 | 167,160
  ```
  </details>

- **v2** · `CVSHEALTH_2018_10K` · PDF page **304** · column 2018 · units
  - Quote: "Property and equipment, net \| 11,349"

  <details><summary>Passage</summary>

  ```
    Investments | 2,522 | 111
    Accounts receivable, net | 17,631 | 13,181
    Inventories | 16,450 | 15,296
    Other current assets | 4,581 | 945
   | Total current assets | 45,243 | 31,229
    Long-term investments | 15,732 | 112
    Property and equipment, net | 11,349 | 10,292
    Goodwill | 78,678 | 38,451
    Intangible assets, net | 36,524 | 13,630
    Separate accounts assets | 3,884 | —
    Other assets | 5,046 | 1,417
  Total assets | $196,456 | $95,131
  Liabilities:
  ```
  </details>

- **v3** · `CVSHEALTH_2018_10K` · PDF page **304** · column 2017 · units
  - Quote: "Property and equipment, net \| 10,292"

  <details><summary>Passage</summary>

  ```
    Investments | 2,522 | 111
    Accounts receivable, net | 17,631 | 13,181
    Inventories | 16,450 | 15,296
    Other current assets | 4,581 | 945
   | Total current assets | 45,243 | 31,229
    Long-term investments | 15,732 | 112
    Property and equipment, net | 11,349 | 10,292
    Goodwill | 78,678 | 38,451
    Intangible assets, net | 36,524 | 13,630
    Separate accounts assets | 3,884 | —
    Other assets | 5,046 | 1,417
  Total assets | $196,456 | $95,131
  Liabilities:
  ```
  </details>

<details><summary>Gold answer</summary>

17.98
</details>

## 77. Is CVS Health a capital-intensive business based on FY2022 data?

`financebench_id_00790` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** CVSHEALTH_2022_10K: verifier: answer_supported=no. The final answer concludes that the company is 'capital-intensive' based on a ratio of 9.53%, but there is no standard financial threshold provided in the filing or the question to define what percentage constitutes 'capital-intensive'. Furthermore, a ratio of ~9.5% is generally considered low for capital-intensive industries (which often see much higher ratios of fixed assets to revenue).

**Pages searched:** `CVSHEALTH_2022_10K` pages 1, 14, 68, 108, 109, 110, 111, 113, 142, 168, 191, 193

<details><summary>Gold answer</summary>

Yes, CVS Health requires an extensive asset base to operate, which is evident from its ROA of only 1.82% in 2022 and 3.39% in 2021, though it should be noted that a significant portion of this asset base is goodwill, and CVS's fixed assets/total assets ratio is on the lower side of 5.6%.
</details>

## 78. Has CVS Health reported any materially important ongoing legal battles from 2022, 2021 and 2020?

`financebench_id_01107` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** CVSHEALTH_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2022,, 2022,

**Pages searched:** `CVSHEALTH_2022_10K` pages 3, 19, 20, 36, 75, 108, 109, 110, 111, 113, 175, 177

<details><summary>Gold answer</summary>

Yes, CVS Health has been involved in multiple ongoing legal battles. Some notable legal dispute areas for CVS are: (1) usual and customary pricing litigation: where it's claimed that CVSâs retail pharmacies overcharged for prescription drugs; (2) PBM litigation and investigations: where it's claimed that that rebate agreements between the drug manufacturers and PBMs caused inflated prices for certain drug products; and (3) controlled substances litigation: legal matters around opioids for which CVS has agreed to pay up to $4.3 billion to claimants in remediation and $625 million to attorneys and fees
</details>

## 79. Has CVS Health paid dividends to common shareholders in Q2 of FY2022?

`financebench_id_01244` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, CVS Health paid a quarterly cash dividend of $0.55 per share to common shareholders in Q2 of FY2022 [v1]. The document explicitly states that during 2022, the quarterly cash dividend was $0.55 per share [v1].

**Computation:** `dividend_q2_2022 = 0.55  where dividend_q2_2022 = $0.55 (units, Q2 FY2022)`

- **v1** · `CVSHEALTH_2022_10K` · PDF page **68** · column 2022 · units
  - Quote: "During 2022, 2021 and 2020, the quarterly cash dividend was $0.55, $0.50 and $0.50 per share, respectively."

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | PART II
  Item 5. Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities.
  Market Information
  CVS Health Corporation’s common stock is listed on the New York Stock Exchange under the symbol “CVS.”
  Dividends
  During 2022, 2021 and 2020, the quarterly cash dividend was $0.55, $0.50 and $0.50 per share, respectively. In December 2022, the Board authorized a 10%
  increase in the quarterly cash dividend to $0.605 per share effective in 2023. CVS Health Corporation has paid cash dividends every quarter since becoming a
  public company. Future dividends will depend on the Company’s earnings, capital requirements, financial condition and other factors considered relevant by
  the Board.
  See Note 12 ‘‘Shareholders’ Equity’’ included in Item 8 of this 10-K for information regarding CVS Health Corporation’s dividends.
  Holders of Common Stock
  As of February 1, 2023, there were 24,142 registered holders of the registrant’s common stock according to the records maintained by the registrant’s transfer
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, CVS paid a $ 0.55 dividend per share every quarter in FY2022
</details>

## 80. Does Foot Locker's new CEO have previous CEO experience in a similar company to Footlocker?

`financebench_id_00839` · filing `FOOTLOCKER_2022_8K_dated_2022-08-19` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Foot Locker's new CEO, Mary N. Dillon, does not have previous CEO experience in a similar company to Foot Locker; her prior CEO roles were at Ulta Beauty, Inc., United States Cellular Corporation, and PepsiCo's Quaker Foods division [v1, v2].

- **v1** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **2** · column units · units
  - Quote: "Mary N. Dillon, 61, former Executive Chair and Chief Executive Officer of Ulta Beauty, Inc., has been appointed President and Chief Executive Officer"

  <details><summary>Passage</summary>

  ```
  Item 5.02. | Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory
   | Arrangements of Certain Officers.
   | On August 19, 2022, Foot Locker, Inc. (the “Company”), issued a press release announcing that, as part of a planned succession process, Richard
  A. Johnson will step down as President and Chief Executive Officer of the Company, effective September 1, 2022. Mary N. Dillon, 61, former Executive
  Chair and Chief Executive Officer of Ulta Beauty, Inc., has been appointed President and Chief Executive Officer and a member of the Company’s Board
  of Directors (the “Board”) and the Executive Committee of the Board, each effective September 1, 2022. A copy of the press release is furnished as Exhibit
  99.1, which is incorporated herein by reference.
   | Ms. Dillon served as Executive Chair of the Board of Directors of Ulta Beauty, Inc. from June 2021 through June 2022. She previously served as
  Chief Executive Officer and a member of the Board of Directors of Ulta from July 2013 through June 2021. Prior to Ulta, she served as President and Chief
  Executive Officer and a member of the Board of Directors of United States Cellular Corporation from 2010 through 2013; and Global Chief Marketing
  ```
  </details>

- **v2** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **2** · column units · units
  - Quote: "Ms. Dillon served as Executive Chair of the Board of Directors of Ulta Beauty, Inc. from June 2021 through June 2022. She previously served as Chief Executive Officer and a member of the Board of Directors of Ulta from July 2013 through June 2021."

  <details><summary>Passage</summary>

  ```
   | Arrangements of Certain Officers.
   | On August 19, 2022, Foot Locker, Inc. (the “Company”), issued a press release announcing that, as part of a planned succession process, Richard
  A. Johnson will step down as President and Chief Executive Officer of the Company, effective September 1, 2022. Mary N. Dillon, 61, former Executive
  Chair and Chief Executive Officer of Ulta Beauty, Inc., has been appointed President and Chief Executive Officer and a member of the Company’s Board
  of Directors (the “Board”) and the Executive Committee of the Board, each effective September 1, 2022. A copy of the press release is furnished as Exhibit
  99.1, which is incorporated herein by reference.
   | Ms. Dillon served as Executive Chair of the Board of Directors of Ulta Beauty, Inc. from June 2021 through June 2022. She previously served as
  Chief Executive Officer and a member of the Board of Directors of Ulta from July 2013 through June 2021. Prior to Ulta, she served as President and Chief
  Executive Officer and a member of the Board of Directors of United States Cellular Corporation from 2010 through 2013; and Global Chief Marketing
  Officer and Executive Vice President of McDonald’s Corporation from 2005 through 2010. Previously, Ms. Dillon held several positions of increasing
  responsibility at PepsiCo Corporation, including as President of the Quaker Foods division from 2004 through 2005 and as Vice President of Marketing for
  Gatorade and Quaker Foods from 2002 through 2004. Ms. Dillon also currently serves on the Board of Directors of each of Starbucks Corporation and
  KKR & Co. Inc. and previously served on the Board of Directors of Target Corporation. Ms. Dillon has no family relationship with any of the Company’s
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. She was previous CEO of Ulta Beauty which means she had to manage a large retail company that has brick and mortar + online business. So yes she was a CEO in a similar company to Foot Locker before this.
</details>

## 81. Were there any board member nominees who had substantially more votes against joining than the other nominees?

`financebench_id_00822` · filing `FOOTLOCKER_2022_8K_dated-2022-05-20` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Richard A. Johnson had substantially more votes against joining than the other nominees, with 16,105,005 votes against compared to the next highest of 6,074,467 for Dona D. Young [v3, v10]. The computed maximum of votes against any single nominee is 16,105,005, which is significantly higher than the others [v3].

**Computation:** `max(votes_against_johnson, votes_against_young) = 16,105,005  where votes_against_drosos = 294,935 (units, FY2022), votes_against_feldman = 5,184,437 (units, FY2022), votes_against_johnson = 16,105,005 (units, FY2022), votes_against_marmol = 5,753,395 (units, FY2022), votes_against_nicosia = 4,827,808 (units, FY2022), votes_against_oakland = 4,524,393 (units, FY2022), votes_against_payne = 4,950,917 (units, FY2022), votes_against_underhill = 4,906,500 (units, FY2022), votes_against_walker = 4,419,340 (units, FY2022), votes_against_young = 6,074,467 (units, FY2022)`

- **v3** · `FOOTLOCKER_2022_8K_dated-2022-05-20` · PDF page **2** · column May 18, 2022 · units
  - Quote: "Richard A. Johnson \| 54,484,293 \| 16,105,005 \| 77,685 \| 6,884,223"

  <details><summary>Passage</summary>

  ```
  were represented in person or by proxy and, therefore, a quorum was present.
   | Proposal 1. With respect to the proposal to elect ten nominees to the Board of Directors (the “Board”), each for a one-year term expiring at the
  annual meeting of shareholders to be held in 2023, the votes were cast for the proposal as set forth below:
   | Name | Votes For | Votes Against | Abstentions | Broker Non-Votes
  Virginia C. Drosos | 59,657,810 | 294,935 | 10,714,238 | 6,884,223
  Alan D. Feldman | 54,760,830 | 5,184,437 | 10,721,716 | 6,884,223
  Richard A. Johnson | 54,484,293 | 16,105,005 | 77,685 | 6,884,223
  Guillermo G. Marmol | 54,193,921 | 5,753,395 | 10,719,667 | 6,884,223
  Darlene Nicosia | 55,123,930 | 4,827,808 | 10,715,245 | 6,884,223
  Steven Oakland | 55,421,657 | 4,524,393 | 10,720,933 | 6,884,223
  Ulice Payne, Jr. | 54,993,396 | 4,950,917 | 10,722,670 | 6,884,223
  Kimberly Underhill | 55,046,260 | 4,906,500 | 10,714,223 | 6,884,223
  Tristan Walker | 55,528,794 | 4,419,340 | 10,718,849 | 6,884,223
  ```
  </details>

- **v10** · `FOOTLOCKER_2022_8K_dated-2022-05-20` · PDF page **2** · column May 18, 2022 · units
  - Quote: "Dona D. Young \| 53,876,257 \| 6,074,467 \| 10,716,259 \| 6,884,223"

  <details><summary>Passage</summary>

  ```
  Guillermo G. Marmol | 54,193,921 | 5,753,395 | 10,719,667 | 6,884,223
  Darlene Nicosia | 55,123,930 | 4,827,808 | 10,715,245 | 6,884,223
  Steven Oakland | 55,421,657 | 4,524,393 | 10,720,933 | 6,884,223
  Ulice Payne, Jr. | 54,993,396 | 4,950,917 | 10,722,670 | 6,884,223
  Kimberly Underhill | 55,046,260 | 4,906,500 | 10,714,223 | 6,884,223
  Tristan Walker | 55,528,794 | 4,419,340 | 10,718,849 | 6,884,223
  Dona D. Young | 53,876,257 | 6,074,467 | 10,716,259 | 6,884,223
   | Based on the votes set forth above, each of the ten nominees to the Board was duly elected.
   | Proposal 2. With respect to the proposal to approve, on an advisory basis, the Company’s named executive officers’ (“NEOs”) compensation, the
  votes were cast for the proposal as set forth below:
   | Votes For | Votes Against | Abstentions | Broker Non-Votes
   | 57,172,731 | 13,324,080 | 170,172 | 6,884,223
   | Based on the votes set forth above, the NEOs’ compensation was approved.
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, his name is Richard A. Johnson
</details>

## 82. What is the FY2019 cash conversion cycle (CCC) for General Mills? CCC is defined as: DIO + DSO - DPO. DIO is defined as: 365 * (average inventory between FY2018 and FY2019) / (FY2019 COGS). DSO is defined as: 365 * (average accounts receivable between FY2018 and FY2019) / (FY2019 Revenue). DPO is defined as: 365 * (average accounts payable between FY2018 and FY2019) / (FY2019 COGS + change in inventory between FY2018 and FY2019). Round your answer to two decimal places. Address the question by using the line items and information shown within the income statement and the balance sheet.

`financebench_id_04103` · filing `GENERALMILLS_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 cash conversion cycle (CCC) for General Mills is -3.70 days. This result is calculated using the provided formula with FY2019 Cost of Sales ($11,108.4), FY2019 Net Sales ($16,865.2), and the average balances for inventory, receivables, and payables from the fiscal years 2018 and 2019 as cited in the evidence [v1, v2, v3, v4, v5, v6, v7, v8]. The computed result explicitly states the final value as -3.70.

**Computation:** `365 * avg(inventory_2019, inventory_2018) / cogs_2019 + 365 * avg(receivables_2019, receivables_2018) / net_sales_2019 - 365 * avg(payables_2019, payables_2018) / (cogs_2019 + (inventory_2019 - inventory_2018)) = -3.70  where inventory_2019 = 1,559.3 (units, FY2019), inventory_2018 = 1,642.2 (units, FY2018), cogs_2019 = 11,108.4 (units, FY2019), receivables_2019 = 1,679.7 (units, FY2019), receivables_2018 = 1,684.2 (units, FY2018), net_sales_2019 = 16,865.2 (units, FY2019), payables_2019 = 2,854.1 (units, FY2019), payables_2018 = 2,746.2 (units, FY2018)`

- **v1** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 26, 2019 · units
  - Quote: "Inventories \| 1,559.3"

  <details><summary>Passage</summary>

  ```
   | May 26, | May 27,
   | 2019 | 2018
    ASSETS
   | Current assets:
   | Cash and cash equivalents | $450.0 | $399.0
   | Receivables | 1,679.7 | 1,684.2
   | Inventories | 1,559.3 | 1,642.2
   | Prepaid expenses and other current assets | 497.5 | 398.3
   | Total current assets | 4,186.5 | 4,123.7
   | Land, buildings, and equipment | 3,787.2 | 4,047.2
   | Goodwill | 13,995.8 | 14,065.0
   | Other intangible assets | 7,166.8 | 7,445.1
   | Other assets | 974.9 | 943.0
  ```
  </details>

- **v2** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 27, 2018 · units
  - Quote: "Inventories \| 1,642.2"

  <details><summary>Passage</summary>

  ```
   | May 26, | May 27,
   | 2019 | 2018
    ASSETS
   | Current assets:
   | Cash and cash equivalents | $450.0 | $399.0
   | Receivables | 1,679.7 | 1,684.2
   | Inventories | 1,559.3 | 1,642.2
   | Prepaid expenses and other current assets | 497.5 | 398.3
   | Total current assets | 4,186.5 | 4,123.7
   | Land, buildings, and equipment | 3,787.2 | 4,047.2
   | Goodwill | 13,995.8 | 14,065.0
   | Other intangible assets | 7,166.8 | 7,445.1
   | Other assets | 974.9 | 943.0
  ```
  </details>

- **v3** · `GENERALMILLS_2019_10K` · PDF page **53** · column 2019 · units
  - Quote: "Cost of sales \| 11,108.4"

  <details><summary>Passage</summary>

  ```
   | Consolidated Statements of Earnings
   | GENERAL MILLS, INC. AND SUBSIDIARIES
   | (In Millions, Except per Share Data)
   | Fiscal Year
   | 2019 | 2018 | 2017
   | Net sales | $16,865.2 | $15,740.4 | $15,619.8
   | Cost of sales | 11,108.4 | 10,304.8 | 10,052.0
   | Selling, general, and administrative expenses | 2,935.8 | 2,850.1 | 2,888.8
   | Divestitures loss | 30.0 | - | 6.5
   | Restructuring, impairment, and other exit costs | 275.1 | 165.6 | 180.4
   | Operating profit | 2,515.9 | 2,419.9 | 2,492.1
   | Benefit plan non-service income | (87.9) | (89.4) | (74.3)
   | Interest, net | 521.8 | 373.7 | 295.1
  ```
  </details>

- **v4** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 26, 2019 · units
  - Quote: "Receivables \| 1,679.7"

  <details><summary>Passage</summary>

  ```
   | (In Millions, Except Par Value)
   | May 26, | May 27,
   | 2019 | 2018
    ASSETS
   | Current assets:
   | Cash and cash equivalents | $450.0 | $399.0
   | Receivables | 1,679.7 | 1,684.2
   | Inventories | 1,559.3 | 1,642.2
   | Prepaid expenses and other current assets | 497.5 | 398.3
   | Total current assets | 4,186.5 | 4,123.7
   | Land, buildings, and equipment | 3,787.2 | 4,047.2
   | Goodwill | 13,995.8 | 14,065.0
   | Other intangible assets | 7,166.8 | 7,445.1
  ```
  </details>

- **v5** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 27, 2018 · units
  - Quote: "Receivables \| 1,684.2"

  <details><summary>Passage</summary>

  ```
   | (In Millions, Except Par Value)
   | May 26, | May 27,
   | 2019 | 2018
    ASSETS
   | Current assets:
   | Cash and cash equivalents | $450.0 | $399.0
   | Receivables | 1,679.7 | 1,684.2
   | Inventories | 1,559.3 | 1,642.2
   | Prepaid expenses and other current assets | 497.5 | 398.3
   | Total current assets | 4,186.5 | 4,123.7
   | Land, buildings, and equipment | 3,787.2 | 4,047.2
   | Goodwill | 13,995.8 | 14,065.0
   | Other intangible assets | 7,166.8 | 7,445.1
  ```
  </details>

- **v6** · `GENERALMILLS_2019_10K` · PDF page **53** · column 2019 · units
  - Quote: "Net sales \| $16,865.2"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | Consolidated Statements of Earnings
   | GENERAL MILLS, INC. AND SUBSIDIARIES
   | (In Millions, Except per Share Data)
   | Fiscal Year
   | 2019 | 2018 | 2017
   | Net sales | $16,865.2 | $15,740.4 | $15,619.8
   | Cost of sales | 11,108.4 | 10,304.8 | 10,052.0
   | Selling, general, and administrative expenses | 2,935.8 | 2,850.1 | 2,888.8
   | Divestitures loss | 30.0 | - | 6.5
   | Restructuring, impairment, and other exit costs | 275.1 | 165.6 | 180.4
   | Operating profit | 2,515.9 | 2,419.9 | 2,492.1
   | Benefit plan non-service income | (87.9) | (89.4) | (74.3)
  ```
  </details>

- **v7** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 26, 2019 · units
  - Quote: "Accounts payable \| $2,854.1"

  <details><summary>Passage</summary>

  ```
   | Goodwill | 13,995.8 | 14,065.0
   | Other intangible assets | 7,166.8 | 7,445.1
   | Other assets | 974.9 | 943.0
   | Total assets | $30,111.2 | $30,624.0
   | LIABILITIES AND EQUITY
   | Current liabilities:
   | Accounts payable | $2,854.1 | $2,746.2
   | Current portion of long-term debt | 1,396.5 | 1,600.1
   | Notes payable | 1,468.7 | 1,549.8
   | Other current liabilities | 1,367.8 | 1,445.8
   | Total current liabilities | 7,087.1 | 7,341.9
   | Long-term debt | 11,624.8 | 12,668.7
   | Deferred income taxes | 2,031.0 | 2,003.8
  ```
  </details>

- **v8** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 27, 2018 · units
  - Quote: "Accounts payable \| $2,746.2"

  <details><summary>Passage</summary>

  ```
   | Goodwill | 13,995.8 | 14,065.0
   | Other intangible assets | 7,166.8 | 7,445.1
   | Other assets | 974.9 | 943.0
   | Total assets | $30,111.2 | $30,624.0
   | LIABILITIES AND EQUITY
   | Current liabilities:
   | Accounts payable | $2,854.1 | $2,746.2
   | Current portion of long-term debt | 1,396.5 | 1,600.1
   | Notes payable | 1,468.7 | 1,549.8
   | Other current liabilities | 1,367.8 | 1,445.8
   | Total current liabilities | 7,087.1 | 7,341.9
   | Long-term debt | 11,624.8 | 12,668.7
   | Deferred income taxes | 2,031.0 | 2,003.8
  ```
  </details>

<details><summary>Gold answer</summary>

-3.7
</details>

## 83. By drawing conclusions from the information stated only in the statement of financial position, what is General Mills's FY2020 working capital ratio? Define working capital ratio as total current assets divided by total current liabilities. Round your answer to two decimal places.

`financebench_id_03471` · filing `GENERALMILLS_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** General Mills's FY2020 working capital ratio is 0.68, calculated by dividing total current assets of $5,121.3 million by total current liabilities of $7,491.5 million [v1, v2]. This ratio indicates that the company had less than one dollar of current assets for every dollar of current liabilities at the end of fiscal year 2020.

**Computation:** `current_assets_2020 / current_liabilities_2020 = 0.68  where current_assets_2020 = 5,121.3 (millions, FY2020), current_liabilities_2020 = 7,491.5 (millions, FY2020)`

- **v1** · `GENERALMILLS_2020_10K` · PDF page **50** · column May 31, 2020 · millions
  - Quote: "Total current assets \| 5,121.3 \| 4,186.5"

  <details><summary>Passage</summary>

  ```
  ASSETS
  Current assets:
   Cash and cash equivalents | $1,677.8  $450.0
    Receivables | 1,615.1 | 1,679.7
    Inventories | 1,426.3 | 1,559.3
    Prepaid expenses and other current assets | 402.1 | 497.5
   | Total current assets | 5,121.3 | 4,186.5
  Land, buildings, and equipment | 3,580.6 | 3,787.2
  Goodwill | 13,923.2 | 13,995.8
  Other intangible assets | 7,095.8 | 7,166.8
  Other assets | 1,085.8 | 974.9
   | Total assets | $30,806.7  $30,111.2
  LIABILITIES AND EQUITY
  ```
  </details>

- **v2** · `GENERALMILLS_2020_10K` · PDF page **50** · column May 31, 2020 · millions
  - Quote: "Total current liabilities \| 7,491.5 \| 7,087.1"

  <details><summary>Passage</summary>

  ```
  LIABILITIES AND EQUITY
  Current liabilities:
   Accounts payable | $3,247.7  $2,854.1
    Current portion of long-term debt | 2,331.5 | 1,396.5
   Notes payable | 279.0 | 1,468.7
   Other current liabilities | 1,633.3 | 1,367.8
   | Total current liabilities | 7,491.5 | 7,087.1
  Long-term debt | 10,929.0 | 11,624.8
  Deferred income taxes | 1,947.1 | 2,031.0
  Other liabilities | 1,545.0 | 1,448.9
   | Total liabilities | 21,912.6 | 22,191.8
  Redeemable interest | 544.6 | 551.7
  Stockholders' equity:
  ```
  </details>

<details><summary>Gold answer</summary>

0.68
</details>

## 84. According to the information provided in the statement of cash flows, what is the FY2020 free cash flow (FCF) for General Mills? FCF here is defined as: (cash from operations - capex). Answer in USD millions.

`financebench_id_04854` · filing `GENERALMILLS_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2020 free cash flow for General Mills is 3,215.4 million USD, calculated by subtracting capital expenditures of 460.8 million from net cash provided by operating activities of 3,676.2 million [v1, v2, COMPUTED RESULT].

**Computation:** `net_cash_operating_2020 - capex_2020 = 3,215.4 million  where net_cash_operating_2020 = 3,676.2 (millions, FY2020), capex_2020 = 460.8 (millions, FY2020)`

- **v1** · `GENERALMILLS_2020_10K` · PDF page **52** · column 2020 · millions
  - Quote: "Net cash provided by operating activities \| 3,676.2"

  <details><summary>Passage</summary>

  ```
   | Pension and other postretirement benefit plan costs | (32.3) | 6.1 | 4.6
   | Divestitures loss | - | 30.0 | -
   | Restructuring, impairment, and other exit costs | 43.6 | 235.7 | 126.0
   | Changes in current assets and liabilities, excluding the effects of acquisitions
   | and divestitures | 793.9 | (7.5) | 542.1
   | Other, net | 45.9 | (27.9) | (182.9)
   | Net cash provided by operating activities | 3,676.2 | 2,807.0 | 2,841.0
  Cash Flows - Investing Activities
    Purchases of land, buildings, and equipment | (460.8) | (537.6) | (622.7)
    Acquisition, net of cash acquired | - | - | (8,035.8)
    Investments in affiliates, net | (48.0) | 0.1 | (17.3)
   Proceeds from disposal of land, buildings, and equipment | 1.7 | 14.3 | 1.4
   Proceeds from divestitures | - | 26.4 | -
  ```
  </details>

- **v2** · `GENERALMILLS_2020_10K` · PDF page **52** · column 2020 · millions
  - Quote: "Purchases of land, buildings, and equipment \| (460.8)"

  <details><summary>Passage</summary>

  ```
   | Restructuring, impairment, and other exit costs | 43.6 | 235.7 | 126.0
   | Changes in current assets and liabilities, excluding the effects of acquisitions
   | and divestitures | 793.9 | (7.5) | 542.1
   | Other, net | 45.9 | (27.9) | (182.9)
   | Net cash provided by operating activities | 3,676.2 | 2,807.0 | 2,841.0
  Cash Flows - Investing Activities
    Purchases of land, buildings, and equipment | (460.8) | (537.6) | (622.7)
    Acquisition, net of cash acquired | - | - | (8,035.8)
    Investments in affiliates, net | (48.0) | 0.1 | (17.3)
   Proceeds from disposal of land, buildings, and equipment | 1.7 | 14.3 | 1.4
   Proceeds from divestitures | - | 26.4 | -
    Other, net | 20.9 | (59.7) | (11.0)
   | Net cash used by investing activities | (486.2) | (556.5) | (8,685.4)
  ```
  </details>

<details><summary>Gold answer</summary>

$3215.00
</details>

## 85. We want to calculate a financial metric. Please help us compute it by basing your answers off of the cash flow statement and the income statement. Here's the question: what is the FY2022 retention ratio (using total cash dividends paid and net income attributable to shareholders) for General Mills? Round answer to two decimal places.

`financebench_id_10136` · filing `GENERALMILLS_2022_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** GENERALMILLS_2022_10K: code checks failed twice: formula: numeric constant 1 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `GENERALMILLS_2022_10K` pages 18, 27, 28, 45, 46, 47, 48, 49, 69, 71, 86, 92

<details><summary>Gold answer</summary>

0.54
</details>

## 86. Are JnJ's FY2022 financials that of a high growth company?

`financebench_id_00956` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Johnson & Johnson's FY2022 financials do not indicate a high growth company, as the Compound Annual Growth Rate (CAGR) of sales from 2020 to 2022 was only 7.2219% [cagr(sales_2020, sales_2022) = 7.2219%]. This growth rate is derived from sales of $82,584 million in 2020 rising to $94,943 million in 2022 [v3, v1], which represents moderate rather than high growth.

**Computation:** `cagr(sales_2020, sales_2022) = 7.2219%  where sales_2022 = $94,943 (millions, FY2022), sales_2021 = 93,775 (millions, FY2021), sales_2020 = 82,584 (millions, FY2020)`

- **v1** · `JOHNSON_JOHNSON_2022_10K` · PDF page **47** · column 2022 · millions
  - Quote: "Sales to customers \| $94,943"

  <details><summary>Passage</summary>

  ```
  | JOHNSON & JOHNSON AND SUBSIDIARIES
   | CONSOLIDATED STATEMENTS OF EARNINGS
   | (Dollars and Shares in Millions Except Per Share Amounts) (Note 1)
   | 2022 | 2021 | 2020
   Sales to customers | $94,943 | 93,775 | 82,584
   Cost of products sold | 31,089 | 29,855 | 28,427
   Gross profit | 63,854 | 63,920 | 54,157
   Selling, marketing and administrative expenses | 24,765 | 24,659 | 22,084
   Research and development expense | 14,603 | 14,714 | 12,159
   In-process research and development (Note 5) | 783 | 900 | 181
   Interest income | (490) | (53) | (111)
  ```
  </details>

- **v3** · `JOHNSON_JOHNSON_2022_10K` · PDF page **47** · column 2020 · millions
  - Quote: "Sales to customers \| 82,584"

  <details><summary>Passage</summary>

  ```
  | JOHNSON & JOHNSON AND SUBSIDIARIES
   | CONSOLIDATED STATEMENTS OF EARNINGS
   | (Dollars and Shares in Millions Except Per Share Amounts) (Note 1)
   | 2022 | 2021 | 2020
   Sales to customers | $94,943 | 93,775 | 82,584
   Cost of products sold | 31,089 | 29,855 | 28,427
   Gross profit | 63,854 | 63,920 | 54,157
   Selling, marketing and administrative expenses | 24,765 | 24,659 | 22,084
   Research and development expense | 14,603 | 14,714 | 12,159
   In-process research and development (Note 5) | 783 | 900 | 181
   Interest income | (490) | (53) | (111)
  ```
  </details>

<details><summary>Gold answer</summary>

No, JnJ's FY2022 financials are not of a high growth company as sales grew by 1.3% in FY2022.
</details>

## 87. What drove gross margin change as of FY2022 for JnJ? If gross margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00669` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** JOHNSON_JOHNSON_2022_10K: verifier: answer_supported=partly. The question asks what 'drove' the gross margin change, but the provided evidence only contains the raw figures for FY2022 and does not include FY2021 data or qualitative commentary to identify the drivers of change.

**Pages searched:** `JOHNSON_JOHNSON_2022_10K` pages 13, 16, 27, 35, 36, 46, 47, 48, 49, 50, 59, 87

<details><summary>Gold answer</summary>

For FY22, JnJ had changes in gross margin due to: One-time COVID-19 vaccine manufacturing exit related costs, Currency impacts in the Pharmaceutical segment, Commodity inflation in the MedTech and Consumer Health segments, partially offset by Supply chain benefits in the Consumer Health segment.
</details>

## 88. Roughly how many times has JnJ sold its inventory in FY2022? Calculate inventory turnover ratio for FY2022; if conventional inventory management is not meaningful for the company then state that and explain why.

`financebench_id_00711` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2022_10K: extractor: The provided pages do not contain the specific line items required to calculate the inventory turnover ratio for FY2022. While Page 41 (labeled as page 41 in the text, but not in the provided list of pages) contains 'Cost of products sold' and Page 40 (labeled as page 40 in the text, but not in the provided list) contains 'Inventories', the actual pages provided in the input (Pages 1, 4, 8, 13, 27, 36, 46, 47, 48, 49, 50, 52) do not include the Consolidated Statements of Earnings (which lists Cost of products sold) or the Consolidated Balance Sheets (which lists Inventories). Page 50 contains the Cash Flow statement but does not list the beginning and ending inventory balances needed for the average, nor does it list Cost of Goods Sold. Therefore, the evidence is not found in the given pages.

**Pages searched:** `JOHNSON_JOHNSON_2022_10K` pages 1, 4, 8, 13, 27, 36, 46, 47, 48, 49, 50, 52

<details><summary>Gold answer</summary>

JnJ sold its inventory 2.7 times in FY2022.
</details>

## 89. Is growth in JnJ's adjusted EPS expected to accelerate in FY2023?

`financebench_id_00651` · filing `JOHNSON_JOHNSON_2022Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, growth in JnJ's adjusted EPS is not expected to accelerate in FY2023 because the expected growth rate of 3.5% is lower than the prior year's growth of 3.6% [v1, v3].

**Computation:** `avg(adjusted_eps_2022, adjusted_eps_2023_midpoint) = 1,032.5%  where adjusted_eps_2022 = $10.15 (units, FY2022), adjusted_eps_2023_midpoint = $10.50 (units, FY2023), adjusted_eps_growth_2023 = 3.5% (units, FY2023)`

- **v1** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2022 · units
  - Quote: "Net earnings per share (Diluted) \| $10.15 \| $9.80 \| 3.6"

  <details><summary>Passage</summary>

  ```
  Net earnings per share (Diluted) | $6.73 | $7.81 | (13.8)
  Average shares outstanding (Diluted) | 2,663.9 | 2,674.0
  Effective tax rate | 17.4 % | 8.3 %
  Adjusted earnings before provision for taxes and net earnings (1)
    Earnings before provision for taxes on income | $31,880 | 33.6 | $30,464 | 32.5 | 4.6
    Net earnings | $27,038 | 28.5 | $26,195 | 27.9 | 3.2
    Net earnings per share (Diluted) | $10.15 | $9.80 | 3.6
    Effective tax rate | 15.2 % | 14.0 %
  (1) See Reconciliation of Non-GAAP Financial Measures.
  ```
  </details>

- **v3** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **5** · column January 2023 · units
  - Quote: "Change vs. Prior Year / Mid-point \| 2.5% – 4.5% / 3.5%"

  <details><summary>Passage</summary>

  ```
   | Change vs. Prior Year / Mid-point
   | Operational Sales2,5/ Mid-point2,5 | $96.9B – $97.9B / $97.4B
   | Change vs. Prior Year / Mid-point | 4.5% – 5.5% / 5.0%
   | Estimated Reported Sales3,5/ Mid-point3,5 | $96.9B – $97.9B / $97.4B
   | Change vs. Prior Year / Mid-point | 4.5% – 5.5% / 5.0%
   | Adjusted Operational EPS (Diluted)2,4/ Mid-point2,4 | $10.40 – $10.60 / $10.50
   | Change vs. Prior Year / Mid-point | 2.5% – 4.5% / 3.5%
   | Adjusted EPS (Diluted)3,4 / Mid-point3,4 | $10.45 – $10.65 / $10.55
   | Change vs. Prior Year / Mid-point | 3.0% – 5.0% / 4.0%
   | 1 Non-GAAP financial measure; excludes the net impact of acquisitions and divestitures
   | 2 Non-GAAP financial measure; excludes the impact of translational currency
   | 3 Calculated using Euro Average Rate: January 2023 = $1.08 (Illustrative purposes only)
   | 4 Non-GAAP financial measure; excludes intangible amortization expense and special items
  ```
  </details>

<details><summary>Gold answer</summary>

No, rate of growth in adjusted EPS is expected to decelerate slightly from 3.6% in FY2022 to 3.5% in FY2023.
</details>

## 90. How did JnJ's US sales growth compare to international sales growth in FY2022?

`financebench_id_01484` · filing `JOHNSON_JOHNSON_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2022Q4_EARNINGS: code checks failed twice: us_sales_fy2022: the quote is not on page 8. Copy it exactly from one line of the page; us_sales_fy2021: the quote is not on page 8. Copy it exactly from one line of the page; us_growth_rate: the quote is not on page 8. Copy it exactly from one line of the page

**Pages searched:** `JOHNSON_JOHNSON_2022Q4_EARNINGS` pages 1, 2, 3, 6, 8, 9, 10, 11, 13, 14, 19, 20

<details><summary>Gold answer</summary>

US sales increased 3.0% vs international sales decline of 0.6%.
</details>

## 91. Which business segment of JnJ will be treated as a discontinued operation from August 30, 2023 onward?

`financebench_id_01488` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The Consumer Health business segment will be treated as a discontinued operation from August 30, 2023 onward [v2]. This is because Johnson & Johnson completed an exchange offer to finalize the separation of Kenvue Inc., which was formerly the Consumer Health business [v1, v2]. Consequently, the company will present the financial results of this segment as discontinued operations [v2].

- **v1** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **2** · column units · units
  - Quote: "Kenvue Inc."

  <details><summary>Passage</summary>

  ```
  Item 2.02 | Results of Operations and Financial Condition
  Johnson & Johnson completed an exchange offer to finalize the separation of Kenvue Inc. (the "Kenvue Separation"). On August 30, 2023, Johnson &
  Johnson issued the attached press release (Exhibit 99.1) providing updated financials and 2023 guidance following completion of the Kenvue Separation.
  Item 9.01  Financial Statements and Exhibits
  (d) | Exhibits.
   | Exhibit No.  Description of Exhibit
   | 99.1 | Press Release dated August 30, 2023
   | 99.2 | Updated Financial Data
  ```
  </details>

- **v2** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **4** · column units · units
  - Quote: "Consumer Health business"

  <details><summary>Passage</summary>

  ```
  found in this release, which may be accessed by visiting the Investors section of the Company's website at webcasts & presentations.
  “The completion of this transaction uniquely positions Johnson & Johnson as a Pharmaceutical and MedTech company focused on delivering
  transformative healthcare solutions to patients,” said Joaquin Duato, Chairman of the Board and Chief Executive Officer. “We are incredibly
  proud of the focus and dedication of our employees worldwide to achieve this milestone, which we are confident will unlock near- and long-
  term value for all of our stakeholders.”
  As previously announced, the Company recently completed an exchange offer to finalize the separation of Kenvue Inc., formerly Johnson &
  Johnson’s Consumer Health business. As a result of the completion of the exchange offer, Johnson & Johnson will now present  its
  Consumer Health business financial results as discontinued operations, including a gain of approximately $20 billion in the third quarter of
  2023.
  ```
  </details>

<details><summary>Gold answer</summary>

The Consumer Health business segment will be treated as a discontinued operation from August 30, 2023 onward.
</details>

## 92. What is the amount of the gain accruing to JnJ as a result of the separation of its Consumer Health business segment, as of August 30, 2023?

`financebench_id_01490` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The amount of the gain accruing to Johnson & Johnson as a result of the separation of its Consumer Health business segment is approximately $20 billion [v1]. This gain is recognized in the third quarter of 2023 following the completion of the exchange offer to finalize the separation [v1].

- **v1** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **4** · column August 30, 2023 · units
  - Quote: "As a result of the completion of the exchange offer, Johnson & Johnson will now present its Consumer Health business financial results as discontinued operations, including a gain of approximately $20 billion in the third quarter of 2023."

  <details><summary>Passage</summary>

  ```
  found in this release, which may be accessed by visiting the Investors section of the Company's website at webcasts & presentations.
  “The completion of this transaction uniquely positions Johnson & Johnson as a Pharmaceutical and MedTech company focused on delivering
  transformative healthcare solutions to patients,” said Joaquin Duato, Chairman of the Board and Chief Executive Officer. “We are incredibly
  proud of the focus and dedication of our employees worldwide to achieve this milestone, which we are confident will unlock near- and long-
  term value for all of our stakeholders.”
  As previously announced, the Company recently completed an exchange offer to finalize the separation of Kenvue Inc., formerly Johnson &
  Johnson’s Consumer Health business. As a result of the completion of the exchange offer, Johnson & Johnson will now present  its
  Consumer Health business financial results as discontinued operations, including a gain of approximately $20 billion in the third quarter of
  2023.
  ```
  </details>

<details><summary>Gold answer</summary>

JnJ will make a gain of approximately $20 billion from the separation of its Consumer Health business segment.
</details>

## 93. What is the amount of the cash proceeds that JnJ realised from the separation of Kenvue (formerly Consumer Health business segment), as of August 30, 2023?

`financebench_id_01491` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Johnson & Johnson realized $13.2 billion in cash proceeds from the Kenvue debt offering and initial public offering as of August 30, 2023 [v1]. This amount represents the cash secured from the separation of the Kenvue business, which was formerly the Consumer Health segment [v1]. The company also maintains a 9.5% equity stake in Kenvue following this transaction [v1].

- **v1** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **4** · column August 30, 2023 · units
  - Quote: "Company secured $13.2 billion in cash proceeds from the Kenvue debt offering and initial public offering and maintains 9.5% of equity stake in Kenvue"

  <details><summary>Passage</summary>

  ```
   | Adjusted Operational Sales Growth of 6.2% - 7.2%; Figures exclude the COVID-19 Vaccine
  •  Company expects 2023 Adjusted Reported Earnings Per Share (EPS) of $10.00 - $10.10, reflecting increased growth of
   | 12.5% at the mid-point and Adjusted Operational EPS of $9.90 - $10.00, reflecting increased growth of 11.5% at the mid-
   | point
  •  Company reduced outstanding share count by approximately 191 million; 2023 guidance reflects only a partial-year benefit
   | of approximately 73.5 million shares or $0.28 benefit to EPS
  •  Company secured $13.2 billion in cash proceeds from the Kenvue debt offering and initial public offering and maintains 9.5%
   | of equity stake in Kenvue
  •  Company maintains its quarterly dividend of $1.19 per share
  New Brunswick, N.J. (August 30, 2023) – Johnson & Johnson (NYSE: JNJ) (“the Company”) today announced updates to its financials and
  2023 guidance which reflect its operations as a company focused on transformational innovation in Pharmaceutical and MedTech. The
  Company has published a recorded webinar for investors to provide additional context behind the updated financials and 2023 guidance
  found in this release, which may be accessed by visiting the Investors section of the Company's website at webcasts & presentations.
  ```
  </details>

<details><summary>Gold answer</summary>

JnJ realised $13.2 billion in cash proceeds from the separation of Kenvue.
</details>

## 94. Did JnJ's net earnings as a percent of sales increase in Q2 of FY2023 compared to Q2 of FY2022?

`financebench_id_01487` · filing `JOHNSON_JOHNSON_2023Q2_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, JnJ's net earnings as a percent of sales increased in Q2 of FY2023 compared to Q2 of FY2022. The computed result shows the margin difference is 0.0011, calculated from net earnings of $5,144 million and sales of $25,530 million in 2023 versus $4,814 million and $24,020 million in 2022 [v1, v2, v3, v4].

**Computation:** `net_earnings_q2_2023 / sales_q2_2023 - net_earnings_q2_2022 / sales_q2_2022 = 0.0011  where net_earnings_q2_2023 = $5,144 (millions, Q2 FY2023), sales_q2_2023 = $25,530 (millions, Q2 FY2023), net_earnings_q2_2022 = $4,814 (millions, Q2 FY2022), sales_q2_2022 = $24,020 (millions, Q2 FY2022)`

- **v1** · `JOHNSON_JOHNSON_2023Q2_EARNINGS` · PDF page **10** · column 2023 · millions
  - Quote: "Net earnings \| $5,144"

  <details><summary>Passage</summary>

  ```
  Research and development expense | 3,829 | 15.0 | 3,703 | 15.4 | 3.4
  Interest (income) expense, net | (23) | (0.1) | (26) | (0.1)
  Other (income) expense, net* | (60) | (0.2) | 273 | 1.1
  Restructuring | 145 | 0.5 | 85 | 0.4
  Earnings before provision for taxes on income | 6,762 | 26.5 | 5,840 | 24.3 | 15.8
  Provision for taxes on income | 1,618 | 6.4 | 1,026 | 4.3 | 57.7
  Net earnings | $5,144 | 20.1 | $4,814 | 20.0 | 6.9
  Net earnings per share (Diluted) | $1.96 | $1.80 | 8.9
  Average shares outstanding (Diluted) | 2,625.7 | 2,667.9
  Effective tax rate | 23.9 % | 17.6 %
  Adjusted earnings before provision for taxes and net earnings (1)
    Earnings before provision for taxes on income | $8,824 | 34.6 | $8,171 | 34.0 | 8.0
    Net earnings | $7,358 | 28.8 | $6,912 | 28.8 | 6.5
  ```
  </details>

- **v2** · `JOHNSON_JOHNSON_2023Q2_EARNINGS` · PDF page **10** · column 2023 · millions
  - Quote: "Sales to customers \| $25,530"

  <details><summary>Passage</summary>

  ```
  Johnson & Johnson and Subsidiaries
  Condensed Consolidated Statement of Earnings
  (Unaudited; in Millions Except Per Share Figures) | SECOND QUARTER
   | 2023 | 2022 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $25,530 | 100.0 | $24,020 | 100.0 | 6.3
  Cost of products sold | 8,212 | 32.2 | 7,919 | 33.0 | 3.7
  Gross Profit | 17,318 | 67.8 | 16,101 | 67.0 | 7.6
  Selling, marketing and administrative expenses | 6,665 | 26.1 | 6,226 | 25.9 | 7.1
  Research and development expense | 3,829 | 15.0 | 3,703 | 15.4 | 3.4
  Interest (income) expense, net | (23) | (0.1) | (26) | (0.1)
  Other (income) expense, net* | (60) | (0.2) | 273 | 1.1
  ```
  </details>

- **v3** · `JOHNSON_JOHNSON_2023Q2_EARNINGS` · PDF page **10** · column 2022 · millions
  - Quote: "Net earnings \| $4,814"

  <details><summary>Passage</summary>

  ```
  Research and development expense | 3,829 | 15.0 | 3,703 | 15.4 | 3.4
  Interest (income) expense, net | (23) | (0.1) | (26) | (0.1)
  Other (income) expense, net* | (60) | (0.2) | 273 | 1.1
  Restructuring | 145 | 0.5 | 85 | 0.4
  Earnings before provision for taxes on income | 6,762 | 26.5 | 5,840 | 24.3 | 15.8
  Provision for taxes on income | 1,618 | 6.4 | 1,026 | 4.3 | 57.7
  Net earnings | $5,144 | 20.1 | $4,814 | 20.0 | 6.9
  Net earnings per share (Diluted) | $1.96 | $1.80 | 8.9
  Average shares outstanding (Diluted) | 2,625.7 | 2,667.9
  Effective tax rate | 23.9 % | 17.6 %
  Adjusted earnings before provision for taxes and net earnings (1)
    Earnings before provision for taxes on income | $8,824 | 34.6 | $8,171 | 34.0 | 8.0
    Net earnings | $7,358 | 28.8 | $6,912 | 28.8 | 6.5
  ```
  </details>

- **v4** · `JOHNSON_JOHNSON_2023Q2_EARNINGS` · PDF page **10** · column 2022 · millions
  - Quote: "Sales to customers \| $24,020"

  <details><summary>Passage</summary>

  ```
  Johnson & Johnson and Subsidiaries
  Condensed Consolidated Statement of Earnings
  (Unaudited; in Millions Except Per Share Figures) | SECOND QUARTER
   | 2023 | 2022 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $25,530 | 100.0 | $24,020 | 100.0 | 6.3
  Cost of products sold | 8,212 | 32.2 | 7,919 | 33.0 | 3.7
  Gross Profit | 17,318 | 67.8 | 16,101 | 67.0 | 7.6
  Selling, marketing and administrative expenses | 6,665 | 26.1 | 6,226 | 25.9 | 7.1
  Research and development expense | 3,829 | 15.0 | 3,703 | 15.4 | 3.4
  Interest (income) expense, net | (23) | (0.1) | (26) | (0.1)
  Other (income) expense, net* | (60) | (0.2) | 273 | 1.1
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, net earnings as a percent of sales increased from 20% in Q2 of FY2022 to 20.1% in Q2 of FY2023.
</details>

## 95. Which of JPM's business segments had the lowest net revenue in 2021 Q1?

`financebench_id_00299` · filing `JPMORGAN_2021Q1_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** JPMORGAN_2021Q1_10Q: verifier: answer_supported=no. The final answer incorrectly identifies the 'Consumer & Community Banking' segment as having the lowest revenue. Based on the evidence provided (v1-v4), the 'Consumer & Community Banking' segment (v3) has a revenue of 2,393 million, but the 'Commercial Banking' segment (v1) is listed as 12,517 million, 'Corporate & Investment Bank' (v2) as 14,605 million, and 'Asset & Wealth Management' (v4) as 4,077 million. However, looking at the table on page 160, the 'Consumer & Community Banking' column for 2021 shows a net revenue of 9,299 million. The values extracted in the evidence (v1-v4) appear to be pulled from the wrong columns or rows (they seem to correspond to different years or different metrics like 'Net income' or 'Total assets' in some cases, or are misaligned with the segment headers). Specifically, for 2021, the net revenues are: Consumer & Community Banking (9,299), Corporate & Investment Bank (14,605), Commercial Banking (2,876), and Asset & Wealth Management (931). Therefore, Asset & Wealth Management is the lowest.

**Pages searched:** `JPMORGAN_2021Q1_10Q` pages 4, 5, 23, 28, 31, 79, 81, 99, 102, 153, 160, 162

<details><summary>Gold answer</summary>

Corporate. Its net revenue was -$473 million.
</details>

## 96. If JPM went bankrupted by the end by 2021 Q1 and liquidated all of its assets to pay its shareholders, how much could each shareholder get?

`financebench_id_02119` · filing `JPMORGAN_2021Q1_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** If JPMorgan were liquidated at the end of Q1 2021, each common shareholder could receive approximately $82.31, calculated by subtracting total liabilities and preferred stock from total assets and dividing by the number of common shares outstanding. This figure is derived from the formula (Total Assets - Total Liabilities - Preferred Stock) / Common Shares Outstanding, using values of $3,689,336 million, $3,408,622 million, $31,563 million, and 3,027,128,112 shares respectively [v1, v2, v3, v4]. The computed result confirms this value is 82.3061 [COMPUTED RESULT].

**Computation:** `(total_assets_march_2021 - total_liabilities_march_2021 - preferred_stock_march_2021) / common_shares_outstanding_march_2021 = 82.3061  where total_assets_march_2021 = $3,689,336 (millions, Q1 FY2021), total_liabilities_march_2021 = 3,408,622 (millions, Q1 FY2021), preferred_stock_march_2021 = 31,563 (millions, Q1 FY2021), common_shares_outstanding_march_2021 = 3,027,128,112 (units, Q1 FY2021)`

- **v1** · `JPMORGAN_2021Q1_10Q` · PDF page **81** · column March 31, 2021 · millions
  - Quote: "Total assets(b) \| $3,689,336"

  <details><summary>Passage</summary>

  ```
   Allowance for loan losses | (23,001) | (28,328)
    Loans, net of allowance for loan losses | 988,306 | 984,525
   Accrued interest and accounts receivable | 114,754 | 90,503
   Premises and equipment | 26,926 | 27,109
   Goodwill, MSRs and other intangible assets | 54,588 | 53,428
   Other assets(a) (included $50,492 and $13,827 at fair value and assets pledged of $37,581 and $3,739) | 200,247 | 151,539
   Total assets(b) | $3,689,336  $3,384,757
   Liabilities
   Deposits (included $14,107 and $14,484 at fair value) | $2,278,112  $2,144,257
   Federal funds purchased and securities loaned or sold under repurchase agreements (included $197,834 and
    $155,735 at fair value) | 304,019 | 215,209
   Short-term borrowings (included $20,002 and $16,893 at fair value) | 54,978 | 45,208
   Trading liabilities | 191,349 | 170,181
  ```
  </details>

- **v2** · `JPMORGAN_2021Q1_10Q` · PDF page **81** · column March 31, 2021 · millions
  - Quote: "Total liabilities(b) \| 3,408,622"

  <details><summary>Passage</summary>

  ```
    $155,735 at fair value) | 304,019 | 215,209
   Short-term borrowings (included $20,002 and $16,893 at fair value) | 54,978 | 45,208
   Trading liabilities | 191,349 | 170,181
   Accounts payable and other liabilities(a) (included $42,824 and $3,476 at fair value) | 285,066 | 231,285
   Beneficial interests issued by consolidated VIEs (included $193 and $41 at fair value) | 15,671 | 17,578
   Long-term debt (included $75,693 and $76,817 at fair value) | 279,427 | 281,685
   Total liabilities(b) | 3,408,622 | 3,105,403
   Commitments and contingencies (refer to Notes 22, 23 and 24)
   Stockholders’ equity
   Preferred stock ($1 par value; authorized 200,000,000 shares; issued 3,156,250 and 3,006,250 shares) | 31,563 | 30,063
   Common stock ($1 par value; authorized 9,000,000,000 shares; issued 4,104,933,895 shares) | 4,105 | 4,105
   Additional paid-in capital | 88,005 | 88,394
   Retained earnings | 248,151 | 236,990
  ```
  </details>

- **v3** · `JPMORGAN_2021Q1_10Q` · PDF page **81** · column March 31, 2021 · millions
  - Quote: "Preferred stock ($1 par value; authorized 200,000,000 shares; issued 3,156,250 and 3,006,250 shares) \| 31,563"

  <details><summary>Passage</summary>

  ```
   Accounts payable and other liabilities(a) (included $42,824 and $3,476 at fair value) | 285,066 | 231,285
   Beneficial interests issued by consolidated VIEs (included $193 and $41 at fair value) | 15,671 | 17,578
   Long-term debt (included $75,693 and $76,817 at fair value) | 279,427 | 281,685
   Total liabilities(b) | 3,408,622 | 3,105,403
   Commitments and contingencies (refer to Notes 22, 23 and 24)
   Stockholders’ equity
   Preferred stock ($1 par value; authorized 200,000,000 shares; issued 3,156,250 and 3,006,250 shares) | 31,563 | 30,063
   Common stock ($1 par value; authorized 9,000,000,000 shares; issued 4,104,933,895 shares) | 4,105 | 4,105
   Additional paid-in capital | 88,005 | 88,394
   Retained earnings | 248,151 | 236,990
   Accumulated other comprehensive income | 1,041 | 7,986
   Treasury stock, at cost (1,077,805,783 and 1,055,499,435 shares) | (92,151) | (88,184)
   Total stockholders’ equity | 280,714 | 279,354
  ```
  </details>

- **v4** · `JPMORGAN_2021Q1_10Q` · PDF page **1** · column March 31, 2021 · units
  - Quote: "Number of shares of common stock outstanding as of March 31, 2021: 3,027,128,112"

  <details><summary>Passage</summary>

  ```
   Large accelerated filer | ☒ | Accelerated filer | ☐
   Non-accelerated filer | ☐ | Smaller reporting company | ☐
   | Emerging growth company | ☐
    If an emerging growth company, indicate by check mark if the registrant has elected not to use the extended transition period for complying with any new or
   revised financial accounting standards provided pursuant to Section 13(a) of the Exchange Act. ☐
  Indicate by check mark whether the registrant is a shell company (as defined in Rule 12b-2 of the Exchange Act). ☐ Yes ☒ No
   | Number of shares of common stock outstanding as of March 31, 2021: 3,027,128,112
  ```
  </details>

<details><summary>Gold answer</summary>

They could receive $66.56 per share.
</details>

## 97. Are JPM's gross margins historically consistent (not fluctuating more than roughly 2% each year)? If gross margins are not a relevant metric for a company like this, then please state that and explain why.

`financebench_id_00206` · filing `JPMORGAN_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** JPMORGAN_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2%

**Pages searched:** `JPMORGAN_2022_10K` pages 1, 3, 18, 46, 48, 193, 200, 225, 279, 289, 293

<details><summary>Gold answer</summary>

Since JPM is a financial institution, gross margin is not a relevant metric.
</details>

## 98. In 2022 Q2, which of JPM's business segments had the highest net income?

`financebench_id_00394` · filing `JPMORGAN_2022Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The Corporate & Investment Bank (CIB) segment had the highest net income in Q2 2022 at $3,725 million. This is higher than the Consumer & Community Banking ($3,100 million), Commercial Banking ($994 million), and Asset & Wealth Management ($1,004 million) segments [v1, v2, v3, v4].

**Computation:** `max(ccb_net_income_2022_q2, cib_net_income_2022_q2, cb_net_income_2022_q2, awm_net_income_2022_q2) = 3,725 million  where ccb_net_income_2022_q2 = $3,100 (millions, Q2 FY2022), cib_net_income_2022_q2 = $3,725 (millions, Q2 FY2022), cb_net_income_2022_q2 = $994 (millions, Q2 FY2022), awm_net_income_2022_q2 = $1,004 (millions, Q2 FY2022)`

- **v1** · `JPMORGAN_2022Q2_10Q` · PDF page **22** · column 2022 · millions
  - Quote: "Net income \| $3,100"

  <details><summary>Passage</summary>

  ```
   Noninterest expense
   Compensation expense | 3,237 | 2,977 | 9 | 6,408 | 5,953 | 8
   Noncompensation expense(a) | 4,486 | 4,085 | 10 | 9,035 | 8,311 | 9
   Total noninterest expense | 7,723 | 7,062 | 9 | 15,443 | 14,264 | 8
   Income before income tax expense | 4,130 | 7,566 | (45) | 7,961 | 16,483 | (52)
   Income tax expense | 1,030 | 1,921 | (c) | (46) | 1,966 | 4,051 | (c) | (51)
   Net income | $3,100 | $5,645 | (c) | (45) | $5,995 | $12,432 | (c) | (52)
   Revenue by line of business
   Consumer & Business Banking | $6,558 | $6,016 | 9 | $12,620 | $11,651 | 8
   Home Lending | 1,001 | 1,349 | (26) | 2,170 | 2,807 | (23)
   Card & Auto | 5,055 | 5,395 | (6) | 10,053 | 10,819 | (7)
   Mortgage fees and related income details:
   Production revenue | 150 | 517 | (71) | 361 | 1,274 | (72)
  ```
  </details>

- **v2** · `JPMORGAN_2022Q2_10Q` · PDF page **27** · column 2022 · millions
  - Quote: "Net income \| $3,725"

  <details><summary>Passage</summary>

  ```
   Noninterest expense
   Compensation expense | 3,510 | 3,582 | (2) | 7,516 | 7,911 | (5)
   Noncompensation expense | 3,235 | 2,941 | 10 | 6,527 | 5,716 | 14
   Total noninterest expense | 6,745 | 6,523 | 3 | 14,043 | 13,627 | 3
   Income before income tax expense | 5,143 | 6,770 | (24) | 10,929 | 14,602 | (25)
   Income tax expense | 1,418 | 1,750 | (b) | (19) | 2,819 | 3,658 | (b) | (23)
   Net income | $3,725 | $5,020 | (b) | (26)%  $8,110 | $10,944 | (b) | (26)%
   Financial ratios
   Return on equity | 14 % | 23 % | 15 % | 26 %  (b)
   Overhead ratio | 56 | 49 | 55 | 49
   Compensation expense as percentage of total net revenue | 29 | 27 | 30 | 28
  (a) Includes tax-equivalent adjustments, predominantly due to income tax credits and other tax benefits related to alternative energy investments; income tax
   | credits and amortization of the cost of investments in affordable housing projects; and tax-exempt income from municipal bonds of $772 million and
  ```
  </details>

- **v3** · `JPMORGAN_2022Q2_10Q` · PDF page **33** · column 2022 · millions
  - Quote: "Net income \| $994"

  <details><summary>Passage</summary>

  ```
   Noninterest expense
   Compensation expense | 559 | 484 | 15 | 1,112 | 966 | 15
   Noncompensation expense | 597 | 497 | 20 | 1,173 | 984 | 19
   Total noninterest expense | 1,156 | 981 | 18 | 2,285 | 1,950 | 17
   Income before income tax expense | 1,318 | 1,879 | (30) | 2,430 | 3,421 | (29)
   Income tax expense | 324 | 457 | (b) | (29) | 586 | 818 | (b) | (28)
   Net income | $994 $1,422 | (b) | (30)%  $1,844 | $2,603 | (b) | (29)%
  (a) Total net revenue included tax-equivalent adjustments from income tax credits related to equity investments in designated community development
   | entities and in entities established for rehabilitation of historic properties, as well as tax-exempt income related to municipal financing activities of $73
   | million and $78 million for the three months ended June 30, 2022 and 2021, respectively and $142 million and $151 million for the six months ended
   | June 30, 2022 and 2021, respectively.
  (b) In the first quarter of 2022, the Firm changed its methodology for allocating income taxes to the LOBs, with no impact to Firmwide net income. Prior-
   | period amounts have been revised to conform with the current presentation.
  ```
  </details>

- **v4** · `JPMORGAN_2022Q2_10Q` · PDF page **37** · column 2022 · millions
  - Quote: "Net income \| $1,004"

  <details><summary>Passage</summary>

  ```
    Noninterest expense
    Compensation expense | 1,508 | 1,356 | 11 | 3,038 | 2,745 | 11
    Noncompensation expense | 1,411 | 1,230 | 15 | 2,741 | 2,415 | 13
    Total noninterest expense | 2,919 | 2,586 | 13 | 5,779 | 5,160 | 12
    Income before income tax expense | 1,343 | 1,531 | (12) | 2,644 | 3,155 | (16)
    Income tax expense | 339 | 375 | (a) | (10) | 632 | 739 | (a) | (14)
    Net income | $1,004 | $1,156 | (a) | (13) | $2,012 | $2,416 | (a) | (17)
    Revenue by line of business
    Asset Management | $2,137 | $2,236 | (4) | $4,451 | $4,421 | 1
    Global Private Bank | 2,169 | 1,871 | 16 | 4,170 | 3,763 | 11
    Total net revenue | $4,306 | $4,107 | 5 %  $8,621 | $8,184 | 5 %
    Financial ratios
    Return on equity | 23 % | 32 % | 23 % | 34 %
  ```
  </details>

<details><summary>Gold answer</summary>

Corporate & Investment Bank. Its net income was $3725 million.
</details>

## 99. Looking at VaR, did the risk that JPM faced in the second fiscal quarter of 2023 decrease compared to the same period in the prior year?

`financebench_id_02049` · filing `JPMORGAN_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** JPMORGAN_2023Q2_10Q: verifier: answer_supported=no. The final answer is contradictory and the computation is incorrect. The evidence shows Total VaR decreased from $54 million in Q2 2022 to $47 million in Q2 2023, but the final answer's logic and the provided computation (0 million) are nonsensical.

**Pages searched:** `JPMORGAN_2023Q2_10Q` pages 4, 25, 30, 35, 37, 41, 85, 96, 97, 98, 99, 121, 126, 198, 199

<details><summary>Gold answer</summary>

Yes. It decreased.
</details>

## 100. What is Kraft Heinz's FY2019 inventory turnover ratio? Inventory turnover ratio is defined as: (FY2019 COGS) / (average inventory between FY2018 and FY2019). Round your answer to two decimal places. Please base your judgments on the information provided primarily in the balance sheet and the P&L statement.

`financebench_id_10499` · filing `KRAFTHEINZ_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Kraft Heinz's FY2019 inventory turnover ratio is 6.25. This is calculated by dividing the Cost of products sold for 2019 ($16,830 million) by the average of the inventories for 2019 ($2,721 million) and 2018 ($2,667 million) [v1, v2, v3].

**Computation:** `cogs_2019 / avg(inventory_2019, inventory_2018) = 6.25  where cogs_2019 = 16,830 (millions, FY2019), inventory_2019 = 2,721 (millions, FY2019), inventory_2018 = 2,667 (millions, FY2018)`

- **v1** · `KRAFTHEINZ_2019_10K` · PDF page **50** · column December 28, 2019 · millions
  - Quote: "Cost of products sold \| 16,830"

  <details><summary>Passage</summary>

  ```
  | The Kraft Heinz Company
   | Consolidated Statements of Income
   | (in millions, except per share data)
   | December 28, 2019 | December 29, 2018  December 30, 2017
  Net sales | $24,977 | $26,268 | $26,076
  Cost of products sold | 16,830 | 17,347 | 17,043
   | Gross profit | 8,147 | 8,921 | 9,033
    Selling, general and administrative expenses, excluding impairment losses | 3,178 | 3,190 | 2,927
    Goodwill impairment losses | 1,197 | 7,008 | —
    Intangible asset impairment losses | 702 | 8,928 | 49
    Selling, general and administrative expenses | 5,077 | 19,126 | 2,976
   | Operating income/(loss) | 3,070 | (10,205) | 6,057
  ```
  </details>

- **v2** · `KRAFTHEINZ_2019_10K` · PDF page **52** · column December 28, 2019 · millions
  - Quote: "Inventories \| 2,721"

  <details><summary>Passage</summary>

  ```
   | (in millions, except per share data)
   | December 28, 2019 | December 29, 2018
  ASSETS
    Cash and cash equivalents | $2,279 | $1,130
    Trade receivables (net of allowances of $33 at December 28, 2019 and $24 at December 29, 2018) | 1,973 | 2,129
    Income taxes receivable | 173 | 152
    Inventories | 2,721 | 2,667
    Prepaid expenses | 384 | 400
    Other current assets | 445 | 1,221
    Assets held for sale | 122 | 1,376
   | Total current assets | 8,097 | 9,075
    Property, plant and equipment, net | 7,055 | 7,078
    Goodwill | 35,546 | 36,503
  ```
  </details>

- **v3** · `KRAFTHEINZ_2019_10K` · PDF page **52** · column December 29, 2018 · millions
  - Quote: "Inventories \| 2,667"

  <details><summary>Passage</summary>

  ```
   | (in millions, except per share data)
   | December 28, 2019 | December 29, 2018
  ASSETS
    Cash and cash equivalents | $2,279 | $1,130
    Trade receivables (net of allowances of $33 at December 28, 2019 and $24 at December 29, 2018) | 1,973 | 2,129
    Income taxes receivable | 173 | 152
    Inventories | 2,721 | 2,667
    Prepaid expenses | 384 | 400
    Other current assets | 445 | 1,221
    Assets held for sale | 122 | 1,376
   | Total current assets | 8,097 | 9,075
    Property, plant and equipment, net | 7,055 | 7,078
    Goodwill | 35,546 | 36,503
  ```
  </details>

<details><summary>Gold answer</summary>

6.25
</details>

## 101. We need to calculate a reasonable approximation (or exact number if possible) of a financial metric. Basing your judgment by information plainly provided in the balance sheet and the P&L statement, what is Lockheed Martin's FY2020 asset turnover ratio? Asset turnover ratio is defined as: FY2020 revenue / (average total assets between FY2019 and FY2020). Round your answer to two decimal places.

`financebench_id_04412` · filing `LOCKHEEDMARTIN_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's FY2020 asset turnover ratio is 1.33. This is calculated by dividing the net sales of 65,398 million by the average total assets, using the values 50,710 million for 2020 and 47,528 million for 2019 [v1, v2, v3].

**Computation:** `net_sales_2020 / avg(total_assets_2020, total_assets_2019) = 1.33  where net_sales_2020 = 65,398 (millions, FY2020), total_assets_2020 = 50,710 (millions, FY2020), total_assets_2019 = 47,528 (millions, FY2019)`

- **v1** · `LOCKHEEDMARTIN_2020_10K` · PDF page **67** · column 2020 · millions
  - Quote: "Total net sales \| 65,398 \| 59,812 \| 53,762"

  <details><summary>Passage</summary>

  ```
   | (in millions, except per share data)
   | Years Ended December 31,
   | 2020 | 2019 | 2018
  Net sales
    Products | $54,928  $50,053  $45,005
    Services | 10,470 | 9,759 | 8,757
   | Total net sales | 65,398 | 59,812 | 53,762
  Cost of sales
    Products | (48,996) | (44,589) | (40,293)
    Services | (9,371) | (8,731) | (7,738)
    Severance charges | (27) | — | (96)
    Other unallocated, net | 1,650 | 1,875 | 1,639
   | Total cost of sales | (56,744) | (51,445) | (46,488)
  ```
  </details>

- **v2** · `LOCKHEEDMARTIN_2020_10K` · PDF page **69** · column 2020 · millions
  - Quote: "Total assets \| $50,710 \| $47,528"

  <details><summary>Passage</summary>

  ```
   | Total current assets | 19,378 | 17,095
  Property, plant and equipment, net | 7,213 | 6,591
  Goodwill | 10,806 | 10,604
  Intangible assets, net | 3,012 | 3,213
  Deferred income taxes | 3,475 | 3,319
  Other noncurrent assets | 6,826 | 6,706
   | Total assets | $50,710  $47,528
  Liabilities and equity
  Current liabilities
    Accounts payable | $880  $1,281
    Contract liabilities | 7,545 | 7,054
    Salaries, benefits and payroll taxes | 3,163 | 2,466
    Current maturities of long-term debt | 500 | 1,250
  ```
  </details>

- **v3** · `LOCKHEEDMARTIN_2020_10K` · PDF page **69** · column 2019 · millions
  - Quote: "Total assets \| $50,710 \| $47,528"

  <details><summary>Passage</summary>

  ```
   | Total current assets | 19,378 | 17,095
  Property, plant and equipment, net | 7,213 | 6,591
  Goodwill | 10,806 | 10,604
  Intangible assets, net | 3,012 | 3,213
  Deferred income taxes | 3,475 | 3,319
  Other noncurrent assets | 6,826 | 6,706
   | Total assets | $50,710  $47,528
  Liabilities and equity
  Current liabilities
    Accounts payable | $880  $1,281
    Contract liabilities | 7,545 | 7,054
    Salaries, benefits and payroll taxes | 3,163 | 2,466
    Current maturities of long-term debt | 500 | 1,250
  ```
  </details>

<details><summary>Gold answer</summary>

1.33
</details>

## 102. What is Lockheed Martin's FY2021 net working capital? Define net working capital as total current assets less total current liabilities. Answer in USD millions. Respond to the question by assuming the perspective of an investment analyst who can only use the details shown within the balance sheet.

`financebench_id_03031` · filing `LOCKHEEDMARTIN_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's FY2021 net working capital is 5,818 million USD, calculated as total current assets of 19,815 million minus total current liabilities of 13,997 million [v1, v2].

**Computation:** `total_current_assets_2021 - total_current_liabilities_2021 = 5,818 million  where total_current_assets_2021 = 19,815 (millions, FY2021), total_current_liabilities_2021 = 13,997 (millions, FY2021)`

- **v1** · `LOCKHEEDMARTIN_2021_10K` · PDF page **30** · column 2021 · millions
  - Quote: "Total current assets \| 19,815"

  <details><summary>Passage</summary>

  ```
  Earnings per common share
    Basic (a)(b)(c)(d)(e)(f)(g)(i) | 22.85 | 24.40 | 22.09 | 17.74 | 6.82
    Diluted (a)(b)(c)(d)(e)(f)(g)(i) | 22.76 | 24.30 | 21.95 | 17.59 | 6.75
  Cash dividends declared per common share | $10.60  $9.80  $9.00  $8.20  $7.46
  Balance sheet
  Cash, cash equivalents and short-term investments | $3,604  $3,160  $1,514  $772  $2,861
  Total current assets | 19,815 | 19,378 | 17,095 | 16,103 | 17,505
  Goodwill | 10,813 | 10,806 | 10,604 | 10,769 | 10,807
  Total assets (h) | 50,873 | 50,710 | 47,528 | 44,876 | 46,620
  Total current liabilities | 13,997 | 13,933 | 13,972 | 14,398 | 12,913
  Total debt, net | 11,676 | 12,169 | 12,654 | 14,104 | 14,263
  Total liabilities (c)(h) | 39,914 | 44,672 | 44,357 | 43,427 | 47,396
  Total equity (deficit) (c)(i) | 10,959 | 6,038 | 3,171 | 1,449 | (776)
  ```
  </details>

- **v2** · `LOCKHEEDMARTIN_2021_10K` · PDF page **30** · column 2021 · millions
  - Quote: "Total current liabilities \| 13,997"

  <details><summary>Passage</summary>

  ```
  Cash dividends declared per common share | $10.60  $9.80  $9.00  $8.20  $7.46
  Balance sheet
  Cash, cash equivalents and short-term investments | $3,604  $3,160  $1,514  $772  $2,861
  Total current assets | 19,815 | 19,378 | 17,095 | 16,103 | 17,505
  Goodwill | 10,813 | 10,806 | 10,604 | 10,769 | 10,807
  Total assets (h) | 50,873 | 50,710 | 47,528 | 44,876 | 46,620
  Total current liabilities | 13,997 | 13,933 | 13,972 | 14,398 | 12,913
  Total debt, net | 11,676 | 12,169 | 12,654 | 14,104 | 14,263
  Total liabilities (c)(h) | 39,914 | 44,672 | 44,357 | 43,427 | 47,396
  Total equity (deficit) (c)(i) | 10,959 | 6,038 | 3,171 | 1,449 | (776)
  Common shares in stockholders’ equity at year-end | 271 | 279 | 280 | 281 | 284
  Cash flow information
  Net cash provided by operating activities (b) | $9,221  $8,183  $7,311  $3,138  $6,476
  ```
  </details>

<details><summary>Gold answer</summary>

$5818.00
</details>

## 103. What is Lockheed Martin's 2 year total revenue CAGR from FY2020 to FY2022 (in units of percents and round to one decimal place)? Provide a response to the question by primarily using the statement of income.

`financebench_id_03718` · filing `LOCKHEEDMARTIN_2022_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's 2-year total revenue CAGR from FY2020 to FY2022 is 0.4%. This is calculated based on net sales of $65,398 million in FY2020 and $65,984 million in FY2022 as reported in the Consolidated Results of Operations table [v1, v2]. The computed result confirms this growth rate [COMPUTED RESULT].

**Computation:** `cagr(net_sales_2020, net_sales_2022) = 0.4%  where net_sales_2022 = $65,984 (millions, FY2022), net_sales_2020 = $65,398 (millions, FY2020)`

- **v1** · `LOCKHEEDMARTIN_2022_10K` · PDF page **34** · column 2022 · millions
  - Quote: "Net sales \| $65,984"

  <details><summary>Passage</summary>

  ```
  manufacture of products and related activities with varying delivery schedules. Consequently, the results of operations of a
  particular year, or year-to-year comparisons of sales and profits, may not be indicative of future operating results. The
  following discussions of comparative results among years should be reviewed in this context. All per share amounts cited in
  these discussions are presented on a “per diluted share” basis, unless otherwise noted. Our consolidated results of operations
  were as follows (in millions, except per share data):
   | 2022 | 2021 | 2020
   Net sales | $65,984  $67,044  $65,398
   Cost of sales | (57,697) | (57,983) | (56,744)
   Gross profit | 8,287 | 9,061 | 8,654
   Other income (expense), net | 61 | 62 | (10)
   Operating profit | 8,348 | 9,123 | 8,644
   Interest expense | (623) | (569) | (591)
   Non-service FAS pension (expense) income | (971) | (1,292) | 219
  ```
  </details>

- **v2** · `LOCKHEEDMARTIN_2022_10K` · PDF page **34** · column 2020 · millions
  - Quote: "Net sales \| $65,398"

  <details><summary>Passage</summary>

  ```
  manufacture of products and related activities with varying delivery schedules. Consequently, the results of operations of a
  particular year, or year-to-year comparisons of sales and profits, may not be indicative of future operating results. The
  following discussions of comparative results among years should be reviewed in this context. All per share amounts cited in
  these discussions are presented on a “per diluted share” basis, unless otherwise noted. Our consolidated results of operations
  were as follows (in millions, except per share data):
   | 2022 | 2021 | 2020
   Net sales | $65,984  $67,044  $65,398
   Cost of sales | (57,697) | (57,983) | (56,744)
   Gross profit | 8,287 | 9,061 | 8,654
   Other income (expense), net | 61 | 62 | (10)
   Operating profit | 8,348 | 9,123 | 8,644
   Interest expense | (623) | (569) | (591)
   Non-service FAS pension (expense) income | (971) | (1,292) | 219
  ```
  </details>

<details><summary>Gold answer</summary>

0.4%
</details>

## 104. Basing your judgments off of the balance sheet, what is the year end FY2018 amount of accounts payable for MGM Resorts? Answer in USD millions.

`financebench_id_04171` · filing `MGMRESORTS_2018_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** MGMRESORTS_2018_10K: code checks failed twice: formula: numeric constant 1000 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `MGMRESORTS_2018_10K` pages 48, 49, 56, 57, 58, 59, 60, 61, 92, 95, 96, 97, 98, 100, 174, 175

<details><summary>Gold answer</summary>

$303.00
</details>

## 105. What is the FY2018 - FY2020 3 year average of capex as a % of revenue for MGM Resorts? Answer in units of percents and round to one decimal place. Please utilize information provided primarily within the statement of cash flows and the statement of income.

`financebench_id_03849` · filing `MGMRESORTS_2020_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** MGMRESORTS_2020_10K: code checks failed twice: revenue_2018: the quote is not on page 65. Copy it exactly from one line of the page; revenue_2019: the quote is not on page 65. Copy it exactly from one line of the page; revenue_2020: the quote is not on page 65. Copy it exactly from one line of the page

**Pages searched:** `MGMRESORTS_2020_10K` pages 1, 41, 45, 51, 52, 56, 64, 65, 67, 68, 108, 138

<details><summary>Gold answer</summary>

7.9%
</details>

## 106. Has MGM Resorts paid dividends to common shareholders in FY2022?

`financebench_id_01254` · filing `MGMRESORTS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** MGMRESORTS_2022_10K: code checks failed twice: dividends_declared_and_paid_to_common_shareholders: the quote is not on page 61. Copy it exactly from one line of the page

**Pages searched:** `MGMRESORTS_2022_10K` pages 1, 32, 33, 47, 48, 59, 60, 61, 62, 64, 74, 94

<details><summary>Gold answer</summary>

Yes. MGM maintained 0.01$ per share annual dividend through out FY 2022.
</details>

## 107. Which region had the Highest EBITDAR Contribution for MGM during FY2022?

`financebench_id_00382` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The Las Vegas Strip Resorts region had the highest EBITDAR contribution for MGM during FY2022 with a value of $3,142,308 [v1]. This amount is greater than the Regional Operations contribution of $1,294,630 [v2] and the absolute value of the MGM China contribution of $203,136 [v3], as confirmed by the computed maximum result [COMPUTED RESULT].

**Computation:** `max(las_vegas_strip_resorts, regional_operations, abs(mgm_china)) = 3,142,308  where las_vegas_strip_resorts = $3,142,308 (units, FY2022), regional_operations = $1,294,630 (units, FY2022), mgm_china = $(203,136) (units, FY2022)`

- **v1** · `MGMRESORTS_2022Q4_EARNINGS` · PDF page **13** · column 2022 · units
  - Quote: "Las Vegas Strip Resorts \| $877,052  $698,739 \| $3,142,308  $1,738,211"

  <details><summary>Passage</summary>

  ```
   | SUPPLEMENTAL DATA – ADJUSTED PROPERTY EBITDAR AND ADJUSTED EBITDAR
   | (In thousands)
   | (Unaudited)
   | Three months ended | Twelve months ended
   | December 31, | December 31, | December 31, | December 31,
   | 2022 | 2021 | 2022 | 2021
  Las Vegas Strip Resorts | $877,052  $698,739 | $3,142,308  $1,738,211
  Regional Operations | 319,517 | 309,250 | 1,294,630 | 1,217,814
  MGM China | (54,979) | 5,015 | (203,136) | 25,367
  Unconsolidated affiliates(1) | (43,029) | (49,698) | (222,079) | (131,590)
  Management and other operations | (3,037) | 2,087 | (11,934) | 15,766
  Stock compensation | (25,159) | (26,494) | (71,297) | (63,984)
  Corporate(2) | (113,058) | (117,491) | (431,238) | (380,501)
  ```
  </details>

- **v2** · `MGMRESORTS_2022Q4_EARNINGS` · PDF page **13** · column 2022 · units
  - Quote: "Regional Operations \| 319,517 \| 309,250 \| 1,294,630 \| 1,217,814"

  <details><summary>Passage</summary>

  ```
   | (In thousands)
   | (Unaudited)
   | Three months ended | Twelve months ended
   | December 31, | December 31, | December 31, | December 31,
   | 2022 | 2021 | 2022 | 2021
   Las Vegas Strip Resorts | $2,297,282  $1,806,686  $8,398,372  $4,737,185
   Regional Operations | 991,452 | 899,607 | 3,815,885 | 3,392,363
  MGM China | 174,720 | 314,717 | 673,593 | 1,210,761
   Management and other operations | 128,762 | 35,882 | 239,635 | 339,831
   | $3,592,216  $3,056,892  $13,127,485  $9,680,140
   | MGM RESORTS INTERNATIONAL AND SUBSIDIARIES
   | SUPPLEMENTAL DATA – ADJUSTED PROPERTY EBITDAR AND ADJUSTED EBITDAR
   | (In thousands)
  ```
  </details>

- **v3** · `MGMRESORTS_2022Q4_EARNINGS` · PDF page **13** · column 2022 · units
  - Quote: "MGM China \| (54,979) \| 5,015 \| (203,136) \| 25,367"

  <details><summary>Passage</summary>

  ```
   | (Unaudited)
   | Three months ended | Twelve months ended
   | December 31, | December 31, | December 31, | December 31,
   | 2022 | 2021 | 2022 | 2021
  Las Vegas Strip Resorts | $877,052  $698,739 | $3,142,308  $1,738,211
  Regional Operations | 319,517 | 309,250 | 1,294,630 | 1,217,814
  MGM China | (54,979) | 5,015 | (203,136) | 25,367
  Unconsolidated affiliates(1) | (43,029) | (49,698) | (222,079) | (131,590)
  Management and other operations | (3,037) | 2,087 | (11,934) | 15,766
  Stock compensation | (25,159) | (26,494) | (71,297) | (63,984)
  Corporate(2) | (113,058) | (117,491) | (431,238) | (380,501)
   | $957,307 | $3,497,254
  (1) Represents the Company's share of operating income (loss) excluding investments in real estate ventures, adjusted for the effect of certain basis
  ```
  </details>

<details><summary>Gold answer</summary>

Las Vegas resorts contributed ~90% of company level EBITDAR during FY2022.
</details>

## 108. What was MGM's interest coverage ratio using FY2022 Adjusted EBIT as the numerator and annual Interest Expense as the denominator?

`financebench_id_01911` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** MGMRESORTS_2022Q4_EARNINGS: extractor: The filing provides 'Interest expense, net of amounts capitalized' but does not provide 'Adjusted EBIT' (Earnings Before Interest, Taxes, and Amortization). It provides 'Adjusted EBITDAR' and 'Operating income', but not the specific 'Adjusted EBIT' metric requested for the numerator. Therefore, the ratio cannot be calculated from the provided pages.

**Pages searched:** `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 3, 4, 6, 7, 9, 11, 12, 13, 14, 15

<details><summary>Gold answer</summary>

As adjusted EBIT is negative, coverage ratio is zero
</details>

## 109. Which region had the worst topline performance for MGM during FY2022?

`financebench_id_01912` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** MGMRESORTS_2022Q4_EARNINGS: code checks failed twice: net_revenues_mgm_china_fy2022: the quote is not on page 2. Copy it exactly from one line of the page; net_revenues_management_other_operations_fy2022: the quote is not on page 13. Copy it exactly from one line of the page; formula: unknown value name 'net_revenues_mgm_china_fy2022' (names: ['net_revenues_las_vegas_strip_resorts_fy2022'])

**Pages searched:** `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15

<details><summary>Gold answer</summary>

MGM China experienced the worst topline performance amongst the other regions presented. Its revenue declined 44% in FY2022 whereas the other regions presented increased their revenues.
</details>

## 110. Which type of debt received the largest investment among the short term investments for MGM in H1 FY2023?

`financebench_id_00407` · filing `MGMRESORTS_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Corporate bonds received the largest investment among short-term investments for MGM in H1 FY2023, with a value of 416,420 [v1]. This amount is significantly higher than the other listed short-term investments, such as U.S. government securities (57,696) and U.S. agency securities (29,049) [v2, v3].

- **v1** · `MGMRESORTS_2023Q2_10Q` · PDF page **11** · column June 30, 2023 · units
  - Quote: "Corporate bonds \| Level 2 \| 416,420 \| 213,875"

  <details><summary>Passage</summary>

  ```
   | Commercial paper and certificates of deposit | Level 2 | — | 5,992
   Cash and cash equivalents | 2,195 | 18,001
   Short-term investments:
   | U.S. government securities | Level 1 | 57,696 | 56,835
   | U.S. agency securities | Level 2 | 29,049 | 9,530
   | Commercial paper and certificates of deposit | Level 2 | 4,561 | 4,466
   | Corporate bonds | Level 2 | 416,420 | 213,875
   Short-term investments | 507,726 | 284,706
  Total debt investments | $509,921  $302,707
   | Restricted cash. MGM China’s pledged cash of $87 million and $124 million as of June 30, 2023 and December 31, 2022, respectively, securing the
  bank guarantees discussed in Note 9 is restricted in use and classified within “Other long-term assets, net.” Such amounts plus “Cash and cash equivalents” on
  the consolidated balance sheets equal “Cash, cash equivalents, and restricted cash” on the consolidated statements of cash flows as of June 30, 2023 and
  December 31, 2022.
  ```
  </details>

- **v2** · `MGMRESORTS_2023Q2_10Q` · PDF page **11** · column June 30, 2023 · units
  - Quote: "U.S. government securities \| Level 1 \| 57,696 \| 56,835"

  <details><summary>Passage</summary>

  ```
   | (In thousands)
   Cash and cash equivalents:
   | Money market funds | Level 1 | $2,195  $12,009
   | Commercial paper and certificates of deposit | Level 2 | — | 5,992
   Cash and cash equivalents | 2,195 | 18,001
   Short-term investments:
   | U.S. government securities | Level 1 | 57,696 | 56,835
   | U.S. agency securities | Level 2 | 29,049 | 9,530
   | Commercial paper and certificates of deposit | Level 2 | 4,561 | 4,466
   | Corporate bonds | Level 2 | 416,420 | 213,875
   Short-term investments | 507,726 | 284,706
  Total debt investments | $509,921  $302,707
   | Restricted cash. MGM China’s pledged cash of $87 million and $124 million as of June 30, 2023 and December 31, 2022, respectively, securing the
  ```
  </details>

- **v3** · `MGMRESORTS_2023Q2_10Q` · PDF page **11** · column June 30, 2023 · units
  - Quote: "U.S. agency securities \| Level 2 \| 29,049 \| 9,530"

  <details><summary>Passage</summary>

  ```
   Cash and cash equivalents:
   | Money market funds | Level 1 | $2,195  $12,009
   | Commercial paper and certificates of deposit | Level 2 | — | 5,992
   Cash and cash equivalents | 2,195 | 18,001
   Short-term investments:
   | U.S. government securities | Level 1 | 57,696 | 56,835
   | U.S. agency securities | Level 2 | 29,049 | 9,530
   | Commercial paper and certificates of deposit | Level 2 | 4,561 | 4,466
   | Corporate bonds | Level 2 | 416,420 | 213,875
   Short-term investments | 507,726 | 284,706
  Total debt investments | $509,921  $302,707
   | Restricted cash. MGM China’s pledged cash of $87 million and $124 million as of June 30, 2023 and December 31, 2022, respectively, securing the
  bank guarantees discussed in Note 9 is restricted in use and classified within “Other long-term assets, net.” Such amounts plus “Cash and cash equivalents” on
  ```
  </details>

<details><summary>Gold answer</summary>

the biggest short term investment is in corporate bonds (almost 82% of the total investment)
</details>

## 111. What is the FY2016 COGS for Microsoft? Please state answer in USD millions. Provide a response to the question by primarily using the statement of income.

`financebench_id_04700` · filing `MICROSOFT_2016_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2016 Cost of Goods Sold (COGS) for Microsoft is 32,780 million USD. This figure is derived from the "Total cost of revenue" line item in the Income Statement for the year ended June 30, 2016, which explicitly lists the value as 32,780 [v1, v2].

**Computation:** `total_cost_of_revenue_2016 = 32,780 million  where total_cost_of_revenue_2016 = 32,780 (millions, FY2016), total_revenue_2016 = 85,320 (millions, FY2016)`

- **v1** · `MICROSOFT_2016_10K` · PDF page **52** · column 2016 · millions
  - Quote: "Total cost of revenue \| 32,780"

  <details><summary>Passage</summary>

  ```
   | Product | $61,502 | $75,956 | $72,948
   | Service and other | 23,818 | 17,624 | 13,885
   | Total revenue | 85,320 | 93,580 | 86,833
  Cost of revenue:
   | Product | 17,880 | 21,410 | 16,681
   | Service and other | 14,900 | 11,628 | 10,397
   | Total cost of revenue | 32,780 | 33,038 | 27,078
   | Gross margin | 52,540 | 60,542 | 59,755
  Research and development | 11,988 | 12,046 | 11,381
  Sales and marketing | 14,697 | 15,713 | 15,811
  General and administrative | 4,563 | 4,611 | 4,677
  Impairment, integration, and restructuring | 1,110 | 10,011 | 127
  Operating income | 20,182 | 18,161 | 27,759
  ```
  </details>

- **v2** · `MICROSOFT_2016_10K` · PDF page **52** · column 2016 · millions
  - Quote: "Total revenue \| 85,320"

  <details><summary>Passage</summary>

  ```
   | INCOME STATEMENTS
  (In millions, except per share amounts)
  Year Ended June 30, | 2016 | 2015 | 2014
  Revenue:
   | Product | $61,502 | $75,956 | $72,948
   | Service and other | 23,818 | 17,624 | 13,885
   | Total revenue | 85,320 | 93,580 | 86,833
  Cost of revenue:
   | Product | 17,880 | 21,410 | 16,681
   | Service and other | 14,900 | 11,628 | 10,397
   | Total cost of revenue | 32,780 | 33,038 | 27,078
   | Gross margin | 52,540 | 60,542 | 59,755
  Research and development | 11,988 | 12,046 | 11,381
  ```
  </details>

<details><summary>Gold answer</summary>

$32780.00
</details>

## 112. Has Microsoft increased its debt on balance sheet between FY2023 and the FY2022 period?

`financebench_id_00552` · filing `MICROSOFT_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Microsoft has not increased its total debt on the balance sheet between FY2022 and FY2023; the total debt decreased by 2,544 million. This is calculated by summing the current portion of long-term debt and long-term debt for both years: (5,247 + 41,990) for FY2023 minus (2,749 + 47,032) for FY2022, resulting in a net reduction [v1, v2, v3, v4].

**Computation:** `(current_portion_lt_debt_2023 + lt_debt_2023) - (current_portion_lt_debt_2022 + lt_debt_2022) = -2,544 million  where current_portion_lt_debt_2023 = 5,247 (millions, FY2023), lt_debt_2023 = 41,990 (millions, FY2023), current_portion_lt_debt_2022 = 2,749 (millions, FY2022), lt_debt_2022 = 47,032 (millions, FY2022)`

- **v1** · `MICROSOFT_2023_10K` · PDF page **60** · column 2023 · millions
  - Quote: "Current portion of long-term debt \| 5,247 \| 2,749"

  <details><summary>Passage</summary>

  ```
  Intangible assets, net | 9,366 | 11,298
  Other long-term assets | 30,601 | 21,897
   | Total assets | $411,976 | $364,840
  Liabilities and stockholders’ equity
  Current liabilities:
   | Accounts payable | $18,095 | $19,000
   | Current portion of long-term debt | 5,247 | 2,749
   | Accrued compensation | 11,009 | 10,661
   | Short-term income taxes | 4,152 | 4,067
   | Short-term unearned revenue | 50,901 | 45,538
   | Other current liabilities | 14,745 | 13,067
   | Total current liabilities | 104,149 | 95,082
  Long-term debt | 41,990 | 47,032
  ```
  </details>

- **v2** · `MICROSOFT_2023_10K` · PDF page **60** · column 2023 · millions
  - Quote: "Long-term debt \| 41,990 \| 47,032"

  <details><summary>Passage</summary>

  ```
   | Current portion of long-term debt | 5,247 | 2,749
   | Accrued compensation | 11,009 | 10,661
   | Short-term income taxes | 4,152 | 4,067
   | Short-term unearned revenue | 50,901 | 45,538
   | Other current liabilities | 14,745 | 13,067
   | Total current liabilities | 104,149 | 95,082
  Long-term debt | 41,990 | 47,032
  Long-term income taxes | 25,560 | 26,069
  Long-term unearned revenue | 2,912 | 2,870
  Deferred income taxes | 433 | 230
  Operating lease liabilities | 12,728 | 11,489
  Other long-term liabilities | 17,981 | 15,526
   | Total liabilities | 205,753 | 198,298
  ```
  </details>

- **v3** · `MICROSOFT_2023_10K` · PDF page **60** · column 2022 · millions
  - Quote: "Current portion of long-term debt \| 5,247 \| 2,749"

  <details><summary>Passage</summary>

  ```
  Intangible assets, net | 9,366 | 11,298
  Other long-term assets | 30,601 | 21,897
   | Total assets | $411,976 | $364,840
  Liabilities and stockholders’ equity
  Current liabilities:
   | Accounts payable | $18,095 | $19,000
   | Current portion of long-term debt | 5,247 | 2,749
   | Accrued compensation | 11,009 | 10,661
   | Short-term income taxes | 4,152 | 4,067
   | Short-term unearned revenue | 50,901 | 45,538
   | Other current liabilities | 14,745 | 13,067
   | Total current liabilities | 104,149 | 95,082
  Long-term debt | 41,990 | 47,032
  ```
  </details>

- **v4** · `MICROSOFT_2023_10K` · PDF page **60** · column 2022 · millions
  - Quote: "Long-term debt \| 41,990 \| 47,032"

  <details><summary>Passage</summary>

  ```
   | Current portion of long-term debt | 5,247 | 2,749
   | Accrued compensation | 11,009 | 10,661
   | Short-term income taxes | 4,152 | 4,067
   | Short-term unearned revenue | 50,901 | 45,538
   | Other current liabilities | 14,745 | 13,067
   | Total current liabilities | 104,149 | 95,082
  Long-term debt | 41,990 | 47,032
  Long-term income taxes | 25,560 | 26,069
  Long-term unearned revenue | 2,912 | 2,870
  Deferred income taxes | 433 | 230
  Operating lease liabilities | 12,728 | 11,489
  Other long-term liabilities | 17,981 | 15,526
   | Total liabilities | 205,753 | 198,298
  ```
  </details>

<details><summary>Gold answer</summary>

No. Microsoft decreased its debt by $2.5bn in FY 2023 vs FY 2022.
</details>

## 113. We want to calculate a financial metric. Please help us compute it by basing your answers off of the statement of income and the statement of cash flows. Here's the question: what is the FY2015 unadjusted EBITDA % margin for Netflix? Calculate unadjusted EBITDA using unadjusted operating income and D&A (from cash flow statement).

`financebench_id_04458` · filing `NETFLIX_2015_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 unadjusted EBITDA % margin for Netflix is 5.4297%. This is calculated by adding the operating income of 305,826 and depreciation and amortization of 62,283 to get unadjusted EBITDA, then dividing by the revenues of 6,779,511 [v1, v2, v3].

**Computation:** `(operating_income_2015 + depreciation_and_amortization_2015) / revenues_2015 = 5.4297%  where operating_income_2015 = 305,826 (units, FY2015), depreciation_and_amortization_2015 = 62,283 (units, FY2015), revenues_2015 = 6,779,511 (units, FY2015)`

- **v1** · `NETFLIX_2015_10K` · PDF page **40** · column 2015 · units
  - Quote: "Operating income \| 305,826"

  <details><summary>Passage</summary>

  ```
   | 2015 | 2014 | 2013
  Revenues | $6,779,511 | $5,504,656 | $4,374,562
   | Cost of revenues | 4,591,476 | 3,752,760 | 3,117,203
   | Marketing | 824,092 | 607,186 | 469,942
   | Technology and development | 650,788 | 472,321 | 378,769
   | General and administrative | 407,329 | 269,741 | 180,301
  Operating income | 305,826 | 402,648 | 228,347
  Other income (expense):
   | Interest expense | (132,716) | (50,219) | (29,142)
   | Interest and other income (expense) | (31,225) | (3,060) | (3,002)
   | Loss on extinguishment of debt | — | — | (25,129)
  Income before income taxes | 141,885 | 349,369 | 171,074
  Provision for income taxes | 19,244 | 82,570 | 58,671
  ```
  </details>

- **v2** · `NETFLIX_2015_10K` · PDF page **42** · column 2015 · units
  - Quote: "Depreciation and amortization of property, equipment and intangibles \| 62,283"

  <details><summary>Passage</summary>

  ```
  Net income | $122,641 | $266,799 | $112,403
  Adjustments to reconcile net income to net cash (used in) provided by operating activities:
   | Additions to streaming content assets | (5,771,652) | (3,773,019) | (3,030,701)
   | Change in streaming content liabilities | 1,162,413 | 593,125 | 673,785
   | Amortization of streaming content assets | 3,405,382 | 2,656,279 | 2,121,981
   | Amortization of DVD content assets | 79,380 | 71,491 | 71,325
   | Depreciation and amortization of property, equipment and intangibles | 62,283 | 54,028 | 48,374
   | Stock-based compensation expense | 124,725 | 115,239 | 73,100
   | Excess tax benefits from stock-based compensation | (80,471) | (89,341) | (81,663)
   | Other non-cash items | 31,628 | 15,282 | 5,332
   | Loss on extinguishment of debt | — | — | 25,129
   | Deferred taxes | (58,655) | (30,063) | (22,044)
   | Changes in operating assets and liabilities:
  ```
  </details>

- **v3** · `NETFLIX_2015_10K` · PDF page **40** · column 2015 · units
  - Quote: "Revenues \| $6,779,511"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | NETFLIX, INC.
   | CONSOLIDATED STATEMENTS OF OPERATIONS
   | (in thousands, except per share data)
   | Year ended December 31,
   | 2015 | 2014 | 2013
  Revenues | $6,779,511 | $5,504,656 | $4,374,562
   | Cost of revenues | 4,591,476 | 3,752,760 | 3,117,203
   | Marketing | 824,092 | 607,186 | 469,942
   | Technology and development | 650,788 | 472,321 | 378,769
   | General and administrative | 407,329 | 269,741 | 180,301
  Operating income | 305,826 | 402,648 | 228,347
  Other income (expense):
  ```
  </details>

<details><summary>Gold answer</summary>

5.4%
</details>

## 114. What is Netflix's year end FY2017 total current liabilities (in USD millions)? Base your judgments on the information provided primarily in the balance sheet.

`financebench_id_03282` · filing `NETFLIX_2017_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** NETFLIX_2017_10K: verifier: answer_supported=no, failed unit_ok. The evidence and final answer incorrectly state the unit as millions. The balance sheet header explicitly states '(in thousands, except share and per share data)', and the value 5,466,312 is in thousands, which equals $5,466.312 million.

**Pages searched:** `NETFLIX_2017_10K` pages 20, 21, 30, 31, 42, 43, 44, 45, 46, 52, 54, 63

<details><summary>Gold answer</summary>

$5466.00
</details>

## 115. We need to calculate a reasonable approximation (or exact number if possible) of a financial metric. Basing your judgment by information plainly provided in the statement of income, what is Nike's three year average of cost of goods sold as a % of revenue from FY2016 to FY2018? Answer in units of percents and round to one decimal place.

`financebench_id_04302` · filing `NIKE_2018_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** NIKE_2018_10K: code checks failed twice: formula: numeric constant 3 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `NIKE_2018_10K` pages 1, 4, 22, 25, 27, 38, 45, 46, 47, 48, 49, 50

<details><summary>Gold answer</summary>

55.1%
</details>

## 116. According to the details clearly outlined within the balance sheet, how much total current assets did Nike have at the end of FY2019? Answer in USD millions.

`financebench_id_03531` · filing `NIKE_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Nike had total current assets of 16,525 million USD at the end of FY2019 [v1, v2]. This figure is explicitly stated in the Consolidated Balance Sheets on page 54 under the "Total current assets" row for the 2019 column [v1]. The values are presented in millions of dollars as indicated by the document header [v2].

**Computation:** `total_current_assets_2019 = 16,525 million  where total_current_assets_2019 = 16,525 (millions, FY2019), unit = Dollars in millions (millions, FY2019)`

- **v1** · `NIKE_2019_10K` · PDF page **54** · column 2019 · millions
  - Quote: "Total current assets \| 16,525 \| 15,134"

  <details><summary>Passage</summary>

  ```
  Current assets:
    Cash and equivalents | $4,466  $4,249
    Short-term investments | 197 | 996
    Accounts receivable, net | 4,272 | 3,498
    Inventories | 5,622 | 5,261
    Prepaid expenses and other current assets | 1,968 | 1,130
  Total current assets | 16,525 | 15,134
    Property, plant and equipment, net | 4,744 | 4,454
   | Identifiable intangible assets, net | 283 | 285
    Goodwill | 154 | 154
    Deferred income taxes and other assets | 2,011 | 2,509
  TOTAL ASSETS | $23,717  $22,536
  LIABILITIES AND SHAREHOLDERS' EQUITY
  ```
  </details>

- **v2** · `NIKE_2019_10K` · PDF page **54** · column 2019 · millions
  - Quote: "(Dollars in millions)"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, INC.
  CONSOLIDATED BALANCE SHEETS
   | MAY 31,
  (Dollars in millions) | 2019 | 2018
  ASSETS
  Current assets:
    Cash and equivalents | $4,466  $4,249
    Short-term investments | 197 | 996
    Accounts receivable, net | 4,272 | 3,498
    Inventories | 5,622 | 5,261
  ```
  </details>

<details><summary>Gold answer</summary>

$16525.00
</details>

## 117. When primarily referencing the income statement and the statement of financial position, what is the FY2021 inventory turnover ratio for Nike? Inventory turnover ratio is defined as: (FY2021 COGS) / (average inventory between FY2020 and FY2021). Round your answer to two decimal places.

`financebench_id_04080` · filing `NIKE_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2021 inventory turnover ratio for Nike is 3.46. This is calculated by dividing the cost of sales for 2021 ($24,576 million) by the average of the inventories for 2021 ($6,854 million) and 2020 ($7,367 million) [v1, v2, v3, v4].

**Computation:** `cost_of_sales_2021 / avg(inventories_2021, inventories_2020) = 3.46  where cost_of_sales_2021 = 24,576 (millions, FY2021), cost_of_sales_2020 = 21,162 (millions, FY2020), inventories_2021 = 6,854 (millions, FY2021), inventories_2020 = 7,367 (millions, FY2020)`

- **v1** · `NIKE_2021_10K` · PDF page **59** · column 2021 · millions
  - Quote: "24,576"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, INC.
  CONSOLIDATED STATEMENTS OF INCOME
   | YEAR ENDED MAY 31,
  (In millions, except per share data) | 2021 | 2020 | 2019
  Revenues | $44,538 $37,403 $39,117
  Cost of sales | 24,576 | 21,162 | 21,643
    Gross profit | 19,962 | 16,241 | 17,474
  Demand creation expense | 3,114 | 3,592 | 3,753
  Operating overhead expense | 9,911 | 9,534 | 8,949
    Total selling and administrative expense | 13,025 | 13,126 | 12,702
  Interest expense (income), net | 262 | 89 | 49
  Other (income) expense, net | 14 | 139 | (78)
  ```
  </details>

- **v2** · `NIKE_2021_10K` · PDF page **59** · column 2020 · millions
  - Quote: "21,162"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, INC.
  CONSOLIDATED STATEMENTS OF INCOME
   | YEAR ENDED MAY 31,
  (In millions, except per share data) | 2021 | 2020 | 2019
  Revenues | $44,538 $37,403 $39,117
  Cost of sales | 24,576 | 21,162 | 21,643
    Gross profit | 19,962 | 16,241 | 17,474
  Demand creation expense | 3,114 | 3,592 | 3,753
  Operating overhead expense | 9,911 | 9,534 | 8,949
    Total selling and administrative expense | 13,025 | 13,126 | 12,702
  Interest expense (income), net | 262 | 89 | 49
  Other (income) expense, net | 14 | 139 | (78)
  ```
  </details>

- **v3** · `NIKE_2021_10K` · PDF page **61** · column 2021 · millions
  - Quote: "6,854"

  <details><summary>Passage</summary>

  ```
  (In millions) | 2021 | 2020
  ASSETS
  Current assets:
    Cash and equivalents | $9,889 $8,348
    Short-term investments | 3,587 | 439
    Accounts receivable, net | 4,463 | 2,749
    Inventories | 6,854 | 7,367
    Prepaid expenses and other current assets | 1,498 | 1,653
  Total current assets | 26,291 | 20,556
    Property, plant and equipment, net | 4,904 | 4,866
    Operating lease right-of-use assets, net | 3,113 | 3,097
    Identifiable intangible assets, net | 269 | 274
    Goodwill | 242 | 223
  ```
  </details>

- **v4** · `NIKE_2021_10K` · PDF page **61** · column 2020 · millions
  - Quote: "7,367"

  <details><summary>Passage</summary>

  ```
  (In millions) | 2021 | 2020
  ASSETS
  Current assets:
    Cash and equivalents | $9,889 $8,348
    Short-term investments | 3,587 | 439
    Accounts receivable, net | 4,463 | 2,749
    Inventories | 6,854 | 7,367
    Prepaid expenses and other current assets | 1,498 | 1,653
  Total current assets | 26,291 | 20,556
    Property, plant and equipment, net | 4,904 | 4,866
    Operating lease right-of-use assets, net | 3,113 | 3,097
    Identifiable intangible assets, net | 269 | 274
    Goodwill | 242 | 223
  ```
  </details>

<details><summary>Gold answer</summary>

3.46
</details>

## 118. Among operations, investing, and financing activities, which brought in the most (or lost the least) cash flow for Nike in FY2023?

`financebench_id_01163` · filing `NIKE_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Nike's operations activities brought in the most cash flow at $5,841 million in FY2023 [v1]. This amount is higher than the cash provided by investing activities ($564 million) and the cash used by financing activities ($(7,447) million) [v2, v3]. Therefore, operations had the highest positive cash flow among the three categories.

**Computation:** `max(cash_flow_operations_2023, cash_flow_investing_2023, cash_flow_financing_2023) = 5,841 million  where cash_flow_operations_2023 = 5,841 (millions, FY2023), cash_flow_investing_2023 = 564 (millions, FY2023), cash_flow_financing_2023 = (7,447) (millions, FY2023)`

- **v1** · `NIKE_2023_10K` · PDF page **62** · column 2023 · millions
  - Quote: "Cash provided (used) by operations \| 5,841"

  <details><summary>Passage</summary>

  ```
   | (Increase) decrease in accounts receivable | 489 | (504) | (1,606)
   | (Increase) decrease in inventories | (133) | (1,676) | 507
   | (Increase) decrease in prepaid expenses, operating lease right-of-use assets and
   | other current and non-current assets | (644) | (845) | (182)
   | Increase (decrease) in accounts payable, accrued liabilities, operating lease liabilities
   | and other current and non-current liabilities | (225) | 1,365 | 1,326
   Cash provided (used) by operations | 5,841 | 5,188 | 6,657
   Cash provided (used) by investing activities:
   | Purchases of short-term investments | (6,059) | (12,913) | (9,961)
   | Maturities of short-term investments | 3,356 | 8,199 | 4,236
   | Sales of short-term investments | 4,184 | 3,967 | 2,449
   | Additions to property, plant and equipment | (969) | (758) | (695)
   | Other investing activities | 52 | (19) | 171
  ```
  </details>

- **v2** · `NIKE_2023_10K` · PDF page **62** · column 2023 · millions
  - Quote: "Cash provided (used) by investing activities \| 564"

  <details><summary>Passage</summary>

  ```
   Cash provided (used) by investing activities:
   | Purchases of short-term investments | (6,059) | (12,913) | (9,961)
   | Maturities of short-term investments | 3,356 | 8,199 | 4,236
   | Sales of short-term investments | 4,184 | 3,967 | 2,449
   | Additions to property, plant and equipment | (969) | (758) | (695)
   | Other investing activities | 52 | (19) | 171
   Cash provided (used) by investing activities | 564 | (1,524) | (3,800)
   Cash provided (used) by financing activities:
   | Increase (decrease) in notes payable, net | (4) | 15 | (52)
   | Repayment of borrowings | (500) | — | (197)
   | Proceeds from exercise of stock options and other stock issuances | 651 | 1,151 | 1,172
   | Repurchase of common stock | (5,480) | (4,014) | (608)
   | Dividends — common and preferred | (2,012) | (1,837) | (1,638)
  ```
  </details>

- **v3** · `NIKE_2023_10K` · PDF page **62** · column 2023 · millions
  - Quote: "Cash provided (used) by financing activities \| (7,447)"

  <details><summary>Passage</summary>

  ```
   | Increase (decrease) in notes payable, net | (4) | 15 | (52)
   | Repayment of borrowings | (500) | — | (197)
   | Proceeds from exercise of stock options and other stock issuances | 651 | 1,151 | 1,172
   | Repurchase of common stock | (5,480) | (4,014) | (608)
   | Dividends — common and preferred | (2,012) | (1,837) | (1,638)
   | Other financing activities | (102) | (151) | (136)
   Cash provided (used) by financing activities | (7,447) | (4,836) | (1,459)
    Effect of exchange rate changes on cash and equivalents | (91) | (143) | 143
    Net increase (decrease) in cash and equivalents | (1,133) | (1,315) | 1,541
   Cash and equivalents, beginning of year | 8,574 | 9,889 | 8,348
   CASH AND EQUIVALENTS, END OF YEAR | $7,441 $8,574 $9,889
   Supplemental disclosure of cash flow information:
   Cash paid during the year for:
  ```
  </details>

<details><summary>Gold answer</summary>

Among the three, cash flow from operations was the highest for Nike in FY2023.
</details>

## 119. Does Paypal have positive working capital based on FY2022 data? If working capital is not a useful or relevant metric for this company, then please state that and explain why.

`financebench_id_00080` · filing `PAYPAL_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, PayPal has positive working capital based on FY2022 data. The company's working capital is calculated as current assets of $57,517 million minus current liabilities of $45,101 million, resulting in a positive value of $12,416 million [v1, v2, COMPUTED RESULT].

**Computation:** `current_assets_2022 - current_liabilities_2022 = 12,416 million  where current_assets_2022 = 57,517 (millions, FY2022), current_liabilities_2022 = 45,101 (millions, FY2022)`

- **v1** · `PAYPAL_2022_10K` · PDF page **61** · column 2022 · millions
  - Quote: "Total current assets \| 57,517"

  <details><summary>Passage</summary>

  ```
   | Short-term investments | 3,092 | 4,303
   | Accounts receivable, net | 963 | 800
   | Loans and interest receivable, net of allowances of $598 and $491 as of December 31, 2022 and 2021,
   | respectively | 7,431 | 4,846
   | Funds receivable and customer accounts | 36,357 | 36,141
   | Prepaid expenses and other current assets | 1,898 | 1,287
   | Total current assets | 57,517 | 52,574
  Long-term investments | 5,018 | 6,797
  Property and equipment, net | 1,730 | 1,909
  Goodwill | 11,209 | 11,454
  Intangible assets, net | 788 | 1,332
  Other assets | 2,455 | 1,737
   | Total assets | $78,717  $75,803
  ```
  </details>

- **v2** · `PAYPAL_2022_10K` · PDF page **61** · column 2022 · millions
  - Quote: "Total current liabilities \| 45,101"

  <details><summary>Passage</summary>

  ```
  LIABILITIES AND EQUITY
  Current liabilities:
   | Accounts payable | $126  $197
   | Funds payable and amounts due to customers | 40,107 | 38,841
   | Accrued expenses and other current liabilities | 4,055 | 3,755
    Income taxes payable | 813 | 236
   | Total current liabilities | 45,101 | 43,029
  Deferred tax liability and other long-term liabilities | 2,925 | 2,998
  Long-term debt | 10,417 | 8,049
   | Total liabilities | 58,443 | 54,076
  Commitments and contingencies (Note 13)
  Equity:
    Common stock, $0.0001 par value; 4,000 shares authorized; 1,136 and 1,168 shares outstanding as of
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. Paypal has a positive working capital of $ 1.6Bn as of FY2022 end.
</details>

## 120. What is the FY2021 capital expenditure amount (in USD billions) for PepsiCo? Respond to the question by assuming the perspective of an investment analyst who can only use the details shown within the statement of cash flows.

`financebench_id_04980` · filing `PEPSICO_2021_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** PEPSICO_2021_10K: code checks failed twice: capital_spending_2021: the quote is not on page 61. Copy it exactly from one line of the page; no value passed the checks; give exact quotes, or answer not_found

**Pages searched:** `PEPSICO_2021_10K` pages 31, 47, 53, 54, 61, 62, 63, 64, 65, 66, 108, 119

<details><summary>Gold answer</summary>

$4.60
</details>

## 121. What are the geographies that Pepsico primarily operates in as of FY2022?

`financebench_id_01009` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** PepsiCo primarily operates in seven geographies as of FY2022: Frito-Lay North America, Quaker Foods North America, PepsiCo Beverages North America, Latin America, Europe, Africa, Middle East and South Asia, and the Asia Pacific, Australia and New Zealand and China Region [v1, v2, v3, v4, v5, v6, v7]. These regions are explicitly listed in the document's table of contents and detailed descriptions on pages 5 and 6.

- **v1** · `PEPSICO_2022_10K` · PDF page **5** · column 2022 · units
  - Quote: "Frito-Lay North America"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | 6)  Africa, Middle East and South Asia (AMESA), which includes all of our beverage and convenient food businesses in
   | Africa, the Middle East and South Asia; and
   | 7) Asia Pacific, Australia and New Zealand and China Region (APAC), which includes all of our beverage and convenient
   | food businesses in Asia Pacific, Australia and New Zealand, and China region.
  Frito-Lay North America
  Either independently or in conjunction with third parties, FLNA makes, markets, distributes and sells branded convenient
  foods. These foods include branded dips, Cheetos cheese-flavored snacks, Doritos tortilla chips, Fritos corn chips, Lay’s potato
  chips, Ruffles potato chips and Tostitos tortilla chips. FLNA’s branded products are sold to independent distributors and retailers.
  In addition, FLNA’s joint venture with Strauss Group makes, markets, distributes and sells Sabra refrigerated dips and spreads.
  Quaker Foods North America
  Either independently or in conjunction with third parties, QFNA makes, markets, distributes and sells branded convenient foods,
  ```
  </details>

- **v2** · `PEPSICO_2022_10K` · PDF page **5** · column 2022 · units
  - Quote: "Quaker Foods North America"

  <details><summary>Passage</summary>

  ```
   | food businesses in Asia Pacific, Australia and New Zealand, and China region.
  Frito-Lay North America
  Either independently or in conjunction with third parties, FLNA makes, markets, distributes and sells branded convenient
  foods. These foods include branded dips, Cheetos cheese-flavored snacks, Doritos tortilla chips, Fritos corn chips, Lay’s potato
  chips, Ruffles potato chips and Tostitos tortilla chips. FLNA’s branded products are sold to independent distributors and retailers.
  In addition, FLNA’s joint venture with Strauss Group makes, markets, distributes and sells Sabra refrigerated dips and spreads.
  Quaker Foods North America
  Either independently or in conjunction with third parties, QFNA makes, markets, distributes and sells branded convenient foods,
  which include cereals, rice, pasta and other branded products. QFNA’s products include Cap’n Crunch cereal, Life cereal, Pearl
  Milling Company syrups and mixes, Quaker Chewy granola bars, Quaker grits, Quaker oatmeal, Quaker rice cakes, Quaker
  Simply Granola and Rice-A-Roni side dishes. QFNA’s branded products are sold to independent distributors and retailers.
  PepsiCo Beverages North America
  Either independently or in conjunction with third parties, PBNA makes, markets and sells beverage concentrates, fountain syrups
  ```
  </details>

- **v3** · `PEPSICO_2022_10K` · PDF page **5** · column 2022 · units
  - Quote: "PepsiCo Beverages North America"

  <details><summary>Passage</summary>

  ```
  In addition, FLNA’s joint venture with Strauss Group makes, markets, distributes and sells Sabra refrigerated dips and spreads.
  Quaker Foods North America
  Either independently or in conjunction with third parties, QFNA makes, markets, distributes and sells branded convenient foods,
  which include cereals, rice, pasta and other branded products. QFNA’s products include Cap’n Crunch cereal, Life cereal, Pearl
  Milling Company syrups and mixes, Quaker Chewy granola bars, Quaker grits, Quaker oatmeal, Quaker rice cakes, Quaker
  Simply Granola and Rice-A-Roni side dishes. QFNA’s branded products are sold to independent distributors and retailers.
  PepsiCo Beverages North America
  Either independently or in conjunction with third parties, PBNA makes, markets and sells beverage concentrates, fountain syrups
  and finished goods under various beverage brands including Aquafina, Diet Mountain Dew, Diet Pepsi, Gatorade, Gatorade Zero,
  Mountain Dew, Pepsi and Propel. PBNA operates its own bottling plants and distribution facilities and sells branded finished
  goods directly to independent distributors and retailers. PBNA also sells concentrate and finished goods for our brands to
  authorized and independent bottlers, who in turn sell our branded finished goods to independent distributors and retailers in
  certain markets. PBNA also, either independently or in conjunction with third parties, makes, markets, distributes and sells ready-
  ```
  </details>

- **v4** · `PEPSICO_2022_10K` · PDF page **5** · column 2022 · units
  - Quote: "Latin America"

  <details><summary>Passage</summary>

  ```
  began to distribute Hard MTN Dew, an alcoholic beverage manufactured and owned by the Boston Beer Company. In the first
  quarter of 2022, we sold our Tropicana, Naked and other select juice brands to PAI Partners, while retaining a 39%
  noncontrolling interest in a newly formed joint venture, Tropicana Brands Group (TBG), operating across North America and
  Europe (Juice Transaction). In the United States, PepsiCo acts as the exclusive distributor for TBG’s portfolio of brands for
  small-format and foodservice customers with chilled direct-store-delivery (DSD). See Note 13 to our consolidated financial
  statements for further information.
  Latin America
  Either independently or in conjunction with third parties, LatAm makes, markets, distributes and sells a number of convenient
  food brands including Cheetos, Doritos, Emperador, Lay’s, Marias Gamesa, Ruffles, Sabritas, Saladitas and Tostitos, as well as
  many Quaker-branded convenient foods. LatAm also, either independently or in conjunction with third parties, makes, markets,
  distributes and sells beverage concentrates, fountain syrups and finished goods under various beverage brands including 7UP,
  Diet 7UP, Gatorade, H2oh!, Manzanita Sol, Mirinda, Pepsi, Pepsi Black, San Carlos and Toddy. These branded products are sold
  to authorized and independent bottlers, independent distributors and retailers. LatAm
  ```
  </details>

- **v5** · `PEPSICO_2022_10K` · PDF page **6** · column 2022 · units
  - Quote: "Europe"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  also, either independently or in conjunction with third parties, makes, markets, distributes and sells ready-to-drink tea products
  through an international joint venture with Unilever (under the Lipton brand name).
  Europe
  Either independently or in conjunction with third parties, Europe makes, markets, distributes and sells a number of convenient
  food brands including Cheetos, Doritos, Lay’s, Ruffles and Walkers, as well as many Quaker-branded convenient foods, through
  consolidated businesses, as well as through noncontrolled affiliates. Europe also, either independently or in conjunction with third
  parties, makes, markets, distributes and sells beverage concentrates, fountain syrups and finished goods under various beverage
  brands including 7UP, Diet Pepsi, Lubimy Sad, Mirinda, Pepsi and Pepsi Max. These branded products are sold to authorized and
  independent bottlers, independent distributors and retailers. In certain markets, however, Europe operates its own bottling plants
  ```
  </details>

- **v6** · `PEPSICO_2022_10K` · PDF page **6** · column 2022 · units
  - Quote: "Africa, Middle East and South Asia"

  <details><summary>Passage</summary>

  ```
  makers and related products. Further, Europe makes, markets, distributes and sells a number of dairy products including Agusha,
  Chudo and Domik v Derevne. Europe also, either independently or in conjunction with third parties, makes, markets, distributes
  and sells ready-to-drink tea products through an international joint venture with Unilever (under the Lipton brand name). In the
  first quarter of 2022, we sold our Tropicana, Naked and other select juice brands to PAI Partners, while retaining a 39%
  noncontrolling interest in TBG, operating across North America and Europe. See Note 13 to our consolidated financial
  statements for further information.
  Africa, Middle East and South Asia
  Either independently or in conjunction with third parties, AMESA makes, markets, distributes and sells a number of convenient
  food brands including Chipsy, Doritos, Kurkure, Lay’s, Sasko, Spekko and White Star, as well as many Quaker-branded
  convenient foods, through consolidated businesses, as well as through noncontrolled affiliates. AMESA also makes, markets,
  distributes and sells beverage concentrates, fountain syrups and finished goods under various beverage brands including 7UP,
  Aquafina, Mirinda, Mountain Dew and Pepsi. These branded products are sold to authorized and independent  bottlers,
  independent distributors and retailers. In certain markets, however, AMESA operates its own bottling plants and distribution
  ```
  </details>

- **v7** · `PEPSICO_2022_10K` · PDF page **6** · column 2022 · units
  - Quote: "Asia Pacific, Australia and New Zealand and China Region"

  <details><summary>Passage</summary>

  ```
  convenient foods, through consolidated businesses, as well as through noncontrolled affiliates. AMESA also makes, markets,
  distributes and sells beverage concentrates, fountain syrups and finished goods under various beverage brands including 7UP,
  Aquafina, Mirinda, Mountain Dew and Pepsi. These branded products are sold to authorized and independent  bottlers,
  independent distributors and retailers. In certain markets, however, AMESA operates its own bottling plants and distribution
  facilities. AMESA also, either independently or in conjunction with third parties, makes, markets, distributes and sells ready-to-
  drink tea products through an international joint venture with Unilever (under the Lipton brand name).
  Asia Pacific, Australia and New Zealand and China Region
  Either independently or in conjunction with third parties, APAC makes, markets, distributes and sells a number of convenient
  food brands including BaiCaoWei, Cheetos, Doritos, Lay’s and Smith’s, as well as many Quaker-branded convenient foods,
  through consolidated businesses, as well as through noncontrolled affiliates. APAC also makes, markets, distributes and sells
  beverage concentrates, fountain syrups and finished goods under various beverage brands including 7UP, Aquafina, Mirinda,
  Mountain Dew, Pepsi and Sting. These branded products are sold to authorized and independent bottlers, independent distributors
  and retailers. APAC also, either independently or in conjunction with third parties, makes, markets, distributes and sells ready-to-
  ```
  </details>

<details><summary>Gold answer</summary>

As of FY2022, Pepsico primarily operates in the following geographies: North America, Latin America, Europe, Africa, Middle East, South Asia, Asia Pacific, Australia, New Zealand and China.
</details>

## 122. Has Pepsico reported any materially important ongoing legal battles from FY2022 and FY2021?

`financebench_id_00735` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** PEPSICO_2022_10K: extractor: The provided pages do not contain specific details about ongoing legal battles for FY2022 and FY2021. Page 3 lists 'Item 3. Legal Proceedings' as a table of contents entry, but the actual content of that section is not included in the provided pages. Page 68 mentions 'Commitments and contingencies' in the balance sheet but provides no details. Therefore, the evidence for this question is not found in the given pages.

**Pages searched:** `PEPSICO_2022_10K` pages 2, 3, 4, 62, 63, 64, 65, 66, 67, 68, 99, 110

<details><summary>Gold answer</summary>

No, Pepsico is not involved in material legal battles.
</details>

## 123. What is the quantity of restructuring costs directly outlined in Pepsico's income statements for FY2022? If restructuring costs are not explicitly outlined then state 0.

`financebench_id_01328` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** PEPSICO_2022_10K: code checks failed twice: restructuring_2022: the quote is not on page 62. Copy it exactly from one line of the page; restructuring_2021: the quote is not on page 62. Copy it exactly from one line of the page; no value passed the checks; give exact quotes, or answer not_found

**Pages searched:** `PEPSICO_2022_10K` pages 31, 46, 49, 62, 63, 64, 65, 66, 67, 68, 79, 110

<details><summary>Gold answer</summary>

Pepsico's restructuring costs in FY2022 amounted to $411 million .
</details>

## 124. What is the FY2022 unadjusted EBITDA less capex for PepsiCo? Define unadjusted EBITDA as unadjusted operating income + depreciation and amortization [from cash flow statement]. Answer in USD millions. Respond to the question by assuming the perspective of an investment analyst who can only use the details shown within the statement of cash flows and the income statement.

`financebench_id_03620` · filing `PEPSICO_2022_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2022 unadjusted EBITDA less capex for PepsiCo is 9,068 million USD. This is calculated by taking the operating profit of 11,512 million from the income statement and adding the depreciation and amortization of 2,763 million from the cash flow statement to get unadjusted EBITDA, then subtracting the absolute value of capital spending of 5,207 million [v1, v2, v3].

**Computation:** `(operating_profit_2022 + depreciation_and_amortization_2022) - abs(capital_spending_2022) = 9,068 million  where operating_profit_2022 = 11,512 (millions, FY2022), depreciation_and_amortization_2022 = 2,763 (millions, FY2022), capital_spending_2022 = (5,207) (millions, FY2022)`

- **v1** · `PEPSICO_2022_10K` · PDF page **62** · column 2022 · millions
  - Quote: "Operating Profit \| 11,512"

  <details><summary>Passage</summary>

  ```
  Net Revenue | $86,392  $79,474  $70,372
  Cost of sales | 40,576 | 37,075 | 31,797
  Gross profit | 45,816 | 42,399 | 38,575
  Selling, general and administrative expenses | 34,459 | 31,237 | 28,453
  Gain associated with the Juice Transaction (see Note 13) | (3,321) | — | —
  Impairment of intangible assets (see Notes 1 and 4) | 3,166 | — | 42
  Operating Profit | 11,512 | 11,162 | 10,080
  Other pension and retiree medical benefits income | 132 | 522 | 117
  Net interest expense and other | (939) | (1,863) | (1,128)
  Income before income taxes | 10,705 | 9,821 | 9,069
  Provision for income taxes | 1,727 | 2,142 | 1,894
  Net income | 8,978 | 7,679 | 7,175
  Less: Net income attributable to noncontrolling interests | 68 | 61 | 55
  ```
  </details>

- **v2** · `PEPSICO_2022_10K` · PDF page **64** · column 2022 · millions
  - Quote: "Depreciation and amortization \| 2,763"

  <details><summary>Passage</summary>

  ```
  PepsiCo, Inc. and Subsidiaries
  Fiscal years ended December 31, 2022, December 25, 2021 and December 26, 2020
  (in millions)
   | 2022 | 2021 | 2020
  Operating Activities
  Net income | $8,978  $7,679  $7,175
  Depreciation and amortization | 2,763 | 2,710 | 2,548
  Gain associated with the Juice Transaction | (3,321) | — | —
  Impairment and other charges | 3,618 | — | —
  Operating lease right-of-use asset amortization | 517 | 505 | 478
  Share-based compensation expense | 343 | 301 | 264
  Restructuring and impairment charges | 411 | 247 | 289
  Cash payments for restructuring charges | (224) | (256) | (255)
  ```
  </details>

- **v3** · `PEPSICO_2022_10K` · PDF page **64** · column 2022 · millions
  - Quote: "Capital spending \| (5,207)"

  <details><summary>Passage</summary>

  ```
   | Prepaid expenses and other current assets | 118 | 159 | 26
    Accounts payable and other current liabilities | 1,842 | 1,762 | 766
    Income taxes payable | 57 | 30 | (159)
  Other, net | (359) | 375 | 164
  Net Cash Provided by Operating Activities | 10,811 | 11,616 | 10,613
  Investing Activities
  Capital spending | (5,207) | (4,625) | (4,240)
  Sales of property, plant and equipment | 251 | 166 | 55
  Acquisitions, net of cash acquired, investments in noncontrolled affiliates and purchases of
    intangible and other assets | (873) | (61) | (6,372)
  Proceeds associated with the Juice Transaction | 3,456 | — | —
  Other divestitures, sales of investments in noncontrolled affiliates and other assets | 49 | 169 | 6
  Short-term investments, by original maturity:
  ```
  </details>

<details><summary>Gold answer</summary>

$9068.00
</details>

## 125. What is the FY2022 unadjusted EBITDA % margin for PepsiCo? Calculate unadjusted EBITDA using unadjusted operating income and D&A (from cash flow statement). Give a response to the question by relying on the details shown in the statement of cash flows and the P&L statement.

`financebench_id_04481` · filing `PEPSICO_2022_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2022 unadjusted EBITDA margin for PepsiCo is 16.5235%. This is calculated by adding the Operating Profit of $11,512 million from the Consolidated Statement of Income to the Depreciation and amortization of $2,763 million from the Consolidated Statement of Cash Flows, then dividing the sum by the Net Revenue of $86,392 million [v1, v2, v3].

**Computation:** `(operating_profit_2022 + depreciation_and_amortization_2022) / net_revenue_2022 = 16.5235%  where operating_profit_2022 = 11,512 (millions, FY2022), depreciation_and_amortization_2022 = 2,763 (millions, FY2022), net_revenue_2022 = 86,392 (millions, FY2022)`

- **v1** · `PEPSICO_2022_10K` · PDF page **62** · column 2022 · millions
  - Quote: "Operating Profit \| 11,512"

  <details><summary>Passage</summary>

  ```
  Net Revenue | $86,392  $79,474  $70,372
  Cost of sales | 40,576 | 37,075 | 31,797
  Gross profit | 45,816 | 42,399 | 38,575
  Selling, general and administrative expenses | 34,459 | 31,237 | 28,453
  Gain associated with the Juice Transaction (see Note 13) | (3,321) | — | —
  Impairment of intangible assets (see Notes 1 and 4) | 3,166 | — | 42
  Operating Profit | 11,512 | 11,162 | 10,080
  Other pension and retiree medical benefits income | 132 | 522 | 117
  Net interest expense and other | (939) | (1,863) | (1,128)
  Income before income taxes | 10,705 | 9,821 | 9,069
  Provision for income taxes | 1,727 | 2,142 | 1,894
  Net income | 8,978 | 7,679 | 7,175
  Less: Net income attributable to noncontrolling interests | 68 | 61 | 55
  ```
  </details>

- **v2** · `PEPSICO_2022_10K` · PDF page **64** · column 2022 · millions
  - Quote: "Depreciation and amortization \| 2,763"

  <details><summary>Passage</summary>

  ```
  PepsiCo, Inc. and Subsidiaries
  Fiscal years ended December 31, 2022, December 25, 2021 and December 26, 2020
  (in millions)
   | 2022 | 2021 | 2020
  Operating Activities
  Net income | $8,978  $7,679  $7,175
  Depreciation and amortization | 2,763 | 2,710 | 2,548
  Gain associated with the Juice Transaction | (3,321) | — | —
  Impairment and other charges | 3,618 | — | —
  Operating lease right-of-use asset amortization | 517 | 505 | 478
  Share-based compensation expense | 343 | 301 | 264
  Restructuring and impairment charges | 411 | 247 | 289
  Cash payments for restructuring charges | (224) | (256) | (255)
  ```
  </details>

- **v3** · `PEPSICO_2022_10K` · PDF page **62** · column 2022 · millions
  - Quote: "Net Revenue \| $86,392"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statement of Income
  PepsiCo, Inc. and Subsidiaries
  Fiscal years ended December 31, 2022, December 25, 2021 and December 26, 2020
  (in millions except per share amounts)
   | 2022 | 2021 | 2020
  Net Revenue | $86,392  $79,474  $70,372
  Cost of sales | 40,576 | 37,075 | 31,797
  Gross profit | 45,816 | 42,399 | 38,575
  Selling, general and administrative expenses | 34,459 | 31,237 | 28,453
  Gain associated with the Juice Transaction (see Note 13) | (3,321) | — | —
  Impairment of intangible assets (see Notes 1 and 4) | 3,166 | — | 42
  Operating Profit | 11,512 | 11,162 | 10,080
  ```
  </details>

<details><summary>Gold answer</summary>

16.5%
</details>

## 126. At the Pepsico AGM held on May 3, 2023, what was the outcome of the shareholder vote on the shareholder proposal for a congruency report by Pepsico on net-zero emissions policies?

`financebench_id_01482` · filing `PEPSICO_2023_8K_dated-2023-05-05` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The shareholder proposal regarding a congruency report on net-zero emissions policies was defeated at the PepsiCo AGM held on May 3, 2023, with 19,718,780 votes in favor, 977,228,788 votes against, and 23,200,321 abstentions [v1, v2, v3].

- **v1** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column May 3, 2023 · units
  - Quote: "For \| 19,718,780"

  <details><summary>Passage</summary>

  ```
  (7) The shareholder proposal regarding a report on impacts of reproductive healthcare legislation was defeated:
  For | 158,917,578
  Against | 830,627,354
  Abstain | 30,602,957
  Broker Non-Votes | 172,969,325
  (8) The shareholder proposal regarding a congruency report on net-zero emissions policies was defeated:
  For | 19,718,780
  Against | 977,228,788
  Abstain | 23,200,321
  Broker Non-Votes | 172,969,325
  ```
  </details>

- **v2** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column May 3, 2023 · units
  - Quote: "Against \| 977,228,788"

  <details><summary>Passage</summary>

  ```
  For | 158,917,578
  Against | 830,627,354
  Abstain | 30,602,957
  Broker Non-Votes | 172,969,325
  (8) The shareholder proposal regarding a congruency report on net-zero emissions policies was defeated:
  For | 19,718,780
  Against | 977,228,788
  Abstain | 23,200,321
  Broker Non-Votes | 172,969,325
  ```
  </details>

- **v3** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column May 3, 2023 · units
  - Quote: "Abstain \| 23,200,321"

  <details><summary>Passage</summary>

  ```
  Against | 830,627,354
  Abstain | 30,602,957
  Broker Non-Votes | 172,969,325
  (8) The shareholder proposal regarding a congruency report on net-zero emissions policies was defeated:
  For | 19,718,780
  Against | 977,228,788
  Abstain | 23,200,321
  Broker Non-Votes | 172,969,325
  ```
  </details>

<details><summary>Gold answer</summary>

The shareholder proposal for a congruency report by Pepsico on net-zero emissions policies was defeated.
</details>

## 127. By how much did Pepsico increase its unsecured five year revolving credit agreement on May 26, 2023?

`financebench_id_00705` · filing `PEPSICO_2023_8K_dated-2023-05-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** PepsiCo increased its unsecured five-year revolving credit agreement by $400,000,000 on May 26, 2023. This is calculated by subtracting the terminated $3,800,000,000 agreement from the new $4,200,000,000 agreement [v1, v2].

**Computation:** `new_5yr_commitment - old_5yr_commitment = 400,000,000  where new_5yr_commitment = $4,200,000,000 (units, May 26, 2023), old_5yr_commitment = $3,800,000,000 (units, May 27, 2022)`

- **v1** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column May 26, 2023 · units
  - Quote: "On May 26, 2023, PepsiCo entered into a new $4,200,000,000 five year unsecured revolving credit agreement"

  <details><summary>Passage</summary>

  ```
  Item 8.01.  Other Events.
   | Effective May 26, 2023, PepsiCo, Inc. (“PepsiCo”) terminated the $3,800,000,000 364 day unsecured revolving credit agreement, dated as of
  May 27, 2022, among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent (the “2022 364 Day Credit
  Agreement”). There were no outstanding borrowings under the 2022 364 Day Credit Agreement at the time of its termination.
   | On May 26, 2023, PepsiCo entered into a new $4,200,000,000 364 day unsecured revolving credit agreement (the “2023 364 Day Credit
  Agreement”) among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent. The 2023 364 Day Credit Agreement
  enables PepsiCo and its borrowing subsidiaries to borrow up to $4,200,000,000 in U.S. Dollars and/or Euros, subject to customary terms and conditions,
  and expires on May 24, 2024. PepsiCo may also, upon the agreement of either the then existing lenders or of additional banks not currently party to the
  2023 364 Day Credit Agreement, increase the commitments under the 2023 364 Day Credit Agreement to up to $4,950,000,000 in U.S. Dollars and/or
  Euros. PepsiCo may request renewal of the 2023 364 Day Credit Agreement for an additional 364 day period or convert any amounts outstanding into a
  term loan for a period of up to one year, which term loan would mature no later than the anniversary of the then effective termination date. Subject to
  ```
  </details>

- **v2** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column May 27, 2022 · units
  - Quote: "Effective May 26, 2023, PepsiCo terminated the $3,800,000,000 five year unsecured revolving credit agreement, dated as of May 27, 2022"

  <details><summary>Passage</summary>

  ```
  Item 8.01.  Other Events.
   | Effective May 26, 2023, PepsiCo, Inc. (“PepsiCo”) terminated the $3,800,000,000 364 day unsecured revolving credit agreement, dated as of
  May 27, 2022, among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent (the “2022 364 Day Credit
  Agreement”). There were no outstanding borrowings under the 2022 364 Day Credit Agreement at the time of its termination.
   | On May 26, 2023, PepsiCo entered into a new $4,200,000,000 364 day unsecured revolving credit agreement (the “2023 364 Day Credit
  Agreement”) among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent. The 2023 364 Day Credit Agreement
  enables PepsiCo and its borrowing subsidiaries to borrow up to $4,200,000,000 in U.S. Dollars and/or Euros, subject to customary terms and conditions,
  and expires on May 24, 2024. PepsiCo may also, upon the agreement of either the then existing lenders or of additional banks not currently party to the
  ```
  </details>

<details><summary>Gold answer</summary>

$400,000,000 increase.
</details>

## 128. As of May 26, 2023, what is the total amount Pepsico may borrow under its unsecured revolving credit agreements?

`financebench_id_00882` · filing `PEPSICO_2023_8K_dated-2023-05-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** As of May 26, 2023, PepsiCo may borrow a total of $8,400,000,000 under its unsecured revolving credit agreements, which consists of a $4,200,000,000 364-day agreement and a $4,200,000,000 five-year agreement [v1, v2, COMPUTED RESULT].

**Computation:** `credit_364_limit + credit_5yr_limit = 8,400,000,000  where credit_364_limit = $4,200,000,000 (units, units), credit_5yr_limit = $4,200,000,000 (units, units)`

- **v1** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column units · units
  - Quote: "On May 26, 2023, PepsiCo entered into a new $4,200,000,000 364 day unsecured revolving credit agreement"

  <details><summary>Passage</summary>

  ```
  Item 8.01.  Other Events.
   | Effective May 26, 2023, PepsiCo, Inc. (“PepsiCo”) terminated the $3,800,000,000 364 day unsecured revolving credit agreement, dated as of
  May 27, 2022, among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent (the “2022 364 Day Credit
  Agreement”). There were no outstanding borrowings under the 2022 364 Day Credit Agreement at the time of its termination.
   | On May 26, 2023, PepsiCo entered into a new $4,200,000,000 364 day unsecured revolving credit agreement (the “2023 364 Day Credit
  Agreement”) among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent. The 2023 364 Day Credit Agreement
  enables PepsiCo and its borrowing subsidiaries to borrow up to $4,200,000,000 in U.S. Dollars and/or Euros, subject to customary terms and conditions,
  and expires on May 24, 2024. PepsiCo may also, upon the agreement of either the then existing lenders or of additional banks not currently party to the
  2023 364 Day Credit Agreement, increase the commitments under the 2023 364 Day Credit Agreement to up to $4,950,000,000 in U.S. Dollars and/or
  Euros. PepsiCo may request renewal of the 2023 364 Day Credit Agreement for an additional 364 day period or convert any amounts outstanding into a
  term loan for a period of up to one year, which term loan would mature no later than the anniversary of the then effective termination date. Subject to
  ```
  </details>

- **v2** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column units · units
  - Quote: "On May 26, 2023, PepsiCo entered into a new $4,200,000,000 five year unsecured revolving credit agreement"

  <details><summary>Passage</summary>

  ```
  Item 8.01.  Other Events.
   | Effective May 26, 2023, PepsiCo, Inc. (“PepsiCo”) terminated the $3,800,000,000 364 day unsecured revolving credit agreement, dated as of
  May 27, 2022, among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent (the “2022 364 Day Credit
  Agreement”). There were no outstanding borrowings under the 2022 364 Day Credit Agreement at the time of its termination.
   | On May 26, 2023, PepsiCo entered into a new $4,200,000,000 364 day unsecured revolving credit agreement (the “2023 364 Day Credit
  Agreement”) among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent. The 2023 364 Day Credit Agreement
  enables PepsiCo and its borrowing subsidiaries to borrow up to $4,200,000,000 in U.S. Dollars and/or Euros, subject to customary terms and conditions,
  and expires on May 24, 2024. PepsiCo may also, upon the agreement of either the then existing lenders or of additional banks not currently party to the
  2023 364 Day Credit Agreement, increase the commitments under the 2023 364 Day Credit Agreement to up to $4,950,000,000 in U.S. Dollars and/or
  Euros. PepsiCo may request renewal of the 2023 364 Day Credit Agreement for an additional 364 day period or convert any amounts outstanding into a
  term loan for a period of up to one year, which term loan would mature no later than the anniversary of the then effective termination date. Subject to
  ```
  </details>

<details><summary>Gold answer</summary>

Total amount Pepsico may borrow under unsecured revolving credit agreements = $8,400,000,000.
</details>

## 129. As of FY2023Q1, why did Pepsico raise full year guidance for FY2023?

`financebench_id_01474` · filing `PEPSICO_2023Q1_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** PepsiCo raised its full-year 2023 guidance because it reported strong first-quarter performance with 14.3% organic revenue growth and an 18% core constant currency EPS change [v1, v2].

**Computation:** `organic_revenue_growth * core_eps_change = 257.4  where organic_revenue_growth = 14.3% (units, FY2023Q1), core_eps_change = 18% (units, FY2023Q1)`

- **v1** · `PEPSICO_2023Q1_EARNINGS` · PDF page **1** · column First-Quarter · units
  - Quote: "Organic revenue growth \| 14.3%"

  <details><summary>Passage</summary>

  ```
   Foreign exchange impact on net revenue | (2.5)%
   Earnings per share (EPS) | $1.40
  EPS change | (54)%
   Foreign exchange impact on EPS | (2)%
   | Organic/Core (non-GAAP)1 First-Quarter 2023 Results
   | First-Quarter
   Organic revenue growth | 14.3%
   Core EPS | $1.50
   Core constant currency EPS change | 18%
  PURCHASE, N.Y. - April 25, 2023 - PepsiCo, Inc. (NASDAQ: PEP) today reported results for
  the first quarter 2023.
  “We are very pleased with our performance and business momentum as our categories and
  geographies remained resilient during the first quarter. Given our strong start to the year, we
  ```
  </details>

- **v2** · `PEPSICO_2023Q1_EARNINGS` · PDF page **1** · column First-Quarter · units
  - Quote: "Core constant currency EPS change \| 18%"

  <details><summary>Passage</summary>

  ```
  EPS change | (54)%
   Foreign exchange impact on EPS | (2)%
   | Organic/Core (non-GAAP)1 First-Quarter 2023 Results
   | First-Quarter
   Organic revenue growth | 14.3%
   Core EPS | $1.50
   Core constant currency EPS change | 18%
  PURCHASE, N.Y. - April 25, 2023 - PepsiCo, Inc. (NASDAQ: PEP) today reported results for
  the first quarter 2023.
  “We are very pleased with our performance and business momentum as our categories and
  geographies remained resilient during the first quarter. Given our strong start to the year, we
  now expect our full-year 2023 organic revenue to increase 8 percent (previously 6 percent) and
  core constant currency EPS to increase 9 percent (previously 8 percent),” said Chairman and
  ```
  </details>

<details><summary>Gold answer</summary>

Pepsico experienced a strong start to FY2023.
</details>

## 130. As of FY2023Q1, by how many percentage points did Pepsico raise full year guidance in respect of core constant currency EPS growth?

`financebench_id_01476` · filing `PEPSICO_2023Q1_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** PEPSICO_2023Q1_EARNINGS: code checks failed twice: formula: unknown value name 'new_core_eps_guidance' (names: [])

**Pages searched:** `PEPSICO_2023Q1_EARNINGS` pages 1, 2, 3, 4, 8, 9, 10, 12, 13, 14, 15, 16

<details><summary>Gold answer</summary>

Pepsico raised full year guidance in respect of core constant currency EPS growth by 1 percentage point.
</details>

## 131. Did Pfizer grow its PPNE between FY20 and FY21?

`financebench_id_00302` · filing `PFIZER_2021_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** PFIZER_2021_10K: verifier: answer_supported=no. The question asks for PPNE (Profit Per Net Equity or a similar equity metric), but the evidence and computation use Net Income attributable to common shareholders. Furthermore, the growth rate calculation is incorrect; the growth from $9,159 to $21,979 is approximately 140.1%, not 239.97% (which is the ratio of 2021 to 2020, not the growth rate).

**Pages searched:** `PFIZER_2021_10K` pages 44, 49, 55, 57, 58, 59, 60, 61, 63, 64, 76, 112

<details><summary>Gold answer</summary>

Yes, change in PPNE was positive year over year
</details>

## 132. Were there any potential events that are not in Pfizer's standard business operations that substantially increased net income in 2019?

`financebench_id_00702` · filing `PFIZER_2021_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, there was a potential event not in standard business operations that substantially increased net income in 2019: a gain of $8,107 million from the completion of the Consumer Healthcare JV transaction [v2]. This one-time gain was recorded in the "Costs and expenses" section of the income statement and significantly contributed to the reported net income of $16,056 million for that year [v1].

**Computation:** `net_income_2019 - gain_consumer_healthcare_jv_2019 = 24,163 million  where net_income_2019 = $16,056 (millions, FY2019), gain_consumer_healthcare_jv_2019 = (8,107) (millions, FY2019)`

- **v1** · `PFIZER_2021_10K` · PDF page **57** · column 2019 · millions
  - Quote: "Net income before allocation to noncontrolling interests \| 22,025 \| 9,195 \| 16,056"

  <details><summary>Passage</summary>

  ```
   | (Gain) on completion of Consumer Healthcare JV transaction | — | (6) | (8,107)
   | Other (income)/deductions––net | (4,878) | 1,219 | 3,497
  Income from continuing operations before provision/(benefit) for taxes on income | 24,311 | 7,036 | 11,321
  Provision/(benefit) for taxes on income | 1,852 | 370 | 583
  Income from continuing operations | 22,459 | 6,666 | 10,738
  Discontinued operations––net of tax | (434) | 2,529 | 5,318
  Net income before allocation to noncontrolling interests | 22,025 | 9,195 | 16,056
  Less: Net income attributable to noncontrolling interests | 45 | 36 | 29
  Net income attributable to Pfizer Inc. common shareholders | $21,979  $9,159  $16,026
  Earnings per common share––basic:
   Income from continuing operations attributable to Pfizer Inc. common shareholders | $4.00  $1.19  $1.92
   Discontinued operations––net of tax | (0.08) | 0.46 | 0.95
  Net income attributable to Pfizer Inc. common shareholders | $3.92  $1.65  $2.88
  ```
  </details>

- **v2** · `PFIZER_2021_10K` · PDF page **57** · column 2019 · millions
  - Quote: "\| (Gain) on completion of Consumer Healthcare JV transaction \| — \| (6) \| (8,107)"

  <details><summary>Passage</summary>

  ```
  Costs and expenses:
   | Cost of sales (a) | 30,821 | 8,484 | 8,054
   | Selling, informational and administrative expenses (a) | 12,703 | 11,597 | 12,726
   | Research and development expenses (a) | 13,829 | 9,393 | 8,385
   | Amortization of intangible assets | 3,700 | 3,348 | 4,429
   | Restructuring charges and certain acquisition-related costs | 802 | 579 | 601
   | (Gain) on completion of Consumer Healthcare JV transaction | — | (6) | (8,107)
   | Other (income)/deductions––net | (4,878) | 1,219 | 3,497
  Income from continuing operations before provision/(benefit) for taxes on income | 24,311 | 7,036 | 11,321
  Provision/(benefit) for taxes on income | 1,852 | 370 | 583
  Income from continuing operations | 22,459 | 6,666 | 10,738
  Discontinued operations––net of tax | (434) | 2,529 | 5,318
  Net income before allocation to noncontrolling interests | 22,025 | 9,195 | 16,056
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, the gain on completion of Consumer Healthcare JV Transaction
</details>

## 133. What are three main companies acquired by Pfizer mentioned in this 10K report?

`financebench_id_02416` · filing `PFIZER_2021_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Reason:** PFIZER_2021_10K: verifier: answer_supported=no. The evidence and final answer are incorrect. The text on page 71 describes the acquisition of 'Seagen' (not 'Array'), 'Therachon', and the sale of 'Meridian'. The final answer incorrectly identifies 'Array' as an acquisition and 'Meridian' as a main company acquired, whereas the text states Meridian was sold.

**Pages searched:** `PFIZER_2021_10K` pages 6, 57, 58, 59, 60, 61, 68, 71, 102, 109

<details><summary>Gold answer</summary>

Trillium, Array, and Therachon
</details>

## 134. How much does Pfizer expect to pay to spin off Upjohn in the future in USD million?

`financebench_id_00283` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** Pfizer_2023Q2_10Q: number check (G4) failed twice: numbers not in the evidence or the result: 90%, 2023,

**Pages searched:** `Pfizer_2023Q2_10Q` pages 8, 9, 10, 11, 14, 16, 26, 34, 37, 38, 41, 45

<details><summary>Gold answer</summary>

77.78
</details>

## 135. For Pfizer, which geographic region had the biggest drop in Q22023 year over year revenues (on a percentage basis)?

`financebench_id_00724` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** Pfizer_2023Q2_10Q: code checks failed twice: formula: numeric constant 54 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `Pfizer_2023Q2_10Q` pages 4, 8, 9, 10, 11, 13, 38, 40, 42, 45, 46, 49

<details><summary>Gold answer</summary>

Developed Rest of the World
</details>

## 136. As of Q2'2023, is Pfizer spinning off any large business segments?

`financebench_id_02419` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** Pfizer_2023Q2_10Q: extractor: The filing states the Upjohn Business spin-off was completed in November 2020 (Page 37), not in Q2 2023. No evidence of a new spin-off in Q2 2023 is found.

**Pages searched:** `Pfizer_2023Q2_10Q` pages 1, 8, 9, 10, 11, 13, 17, 34, 37, 38, 41, 45

<details><summary>Gold answer</summary>

Yes, it's spinning off Upjohn.
</details>

## 137. Which debt securities are registered to trade on a national securities exchange under Ulta Beauty's name as of FY2023?

`financebench_id_00746` · filing `ULTABEAUTY_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No debt securities are registered to trade on a national securities exchange under Ulta Beauty's name as of FY2023. The filing explicitly states that "Securities registered pursuant to Section 12(b) of the Act" only include common stock, and lists "None" for securities registered under Section 12(g), indicating no other securities are registered for trading [v1, v3].

- **v1** · `ULTABEAUTY_2023_10K` · PDF page **1** · column 2023 · units
  - Quote: "Common stock, par value $0.01 per share"

  <details><summary>Passage</summary>

  ```
   | 1000 Remington Blvd., Suite 120 | 60440
   | Bolingbrook, Illinois | (Zip code)
   | (Address of principal executive offices)
   | Registrant’s telephone number, including area code: (630) 410-4800
   | Securities registered pursuant to Section 12(b) of the Act:
   | Title of each class | Trading symbol | Name of each exchange on which registered
   | Common stock, par value $0.01 per share | ULTA | The NASDAQ Global Select Market
   | Securities registered pursuant to Section 12(g) of the Act: None
  Indicate by check mark if the registrant is a well-known seasoned issuer, as defined in Rule 405 of the Securities Act. ⌧ Yes ◻ No
  Indicate by check mark if the registrant is not required to file reports pursuant to Section 13 or Section 15(d) of the Act. ◻ Yes ⌧ No
  Indicate by check mark whether the registrant (1) has filed all reports required to be filed by Section 13 or 15(d) of the Securities Exchange Act of 1934
  during the preceding 12 months (or for such shorter period that the registrant was required to file such reports), and (2) has been subject to such filing
  requirements for the past 90 days. ⌧ Yes ◻ No
  ```
  </details>

- **v3** · `ULTABEAUTY_2023_10K` · PDF page **1** · column 2023 · units
  - Quote: "The NASDAQ Global Select Market"

  <details><summary>Passage</summary>

  ```
   | 1000 Remington Blvd., Suite 120 | 60440
   | Bolingbrook, Illinois | (Zip code)
   | (Address of principal executive offices)
   | Registrant’s telephone number, including area code: (630) 410-4800
   | Securities registered pursuant to Section 12(b) of the Act:
   | Title of each class | Trading symbol | Name of each exchange on which registered
   | Common stock, par value $0.01 per share | ULTA | The NASDAQ Global Select Market
   | Securities registered pursuant to Section 12(g) of the Act: None
  Indicate by check mark if the registrant is a well-known seasoned issuer, as defined in Rule 405 of the Securities Act. ⌧ Yes ◻ No
  Indicate by check mark if the registrant is not required to file reports pursuant to Section 13 or Section 15(d) of the Act. ◻ Yes ⌧ No
  Indicate by check mark whether the registrant (1) has filed all reports required to be filed by Section 13 or 15(d) of the Securities Exchange Act of 1934
  during the preceding 12 months (or for such shorter period that the registrant was required to file such reports), and (2) has been subject to such filing
  requirements for the past 90 days. ⌧ Yes ◻ No
  ```
  </details>

<details><summary>Gold answer</summary>

There are none
</details>

## 138. What are major acquisitions that Ulta Beauty has done in FY2023 and FY2022?

`financebench_id_00521` · filing `ULTABEAUTY_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** ULTABEAUTY_2023_10K: extractor: The Consolidated Statements of Cash Flows on Page 57 shows 'Acquisitions, net of cash acquired' as '—' (zero) for both fiscal years 2023 and 2022. No other pages provide evidence of acquisitions for these periods.

**Pages searched:** `ULTABEAUTY_2023_10K` pages 5, 9, 10, 42, 54, 55, 56, 57, 58, 59, 100, 101

<details><summary>Gold answer</summary>

Ulta Beauty did not make any acquisitions in FY2023 and FY2022.
</details>

## 139. What drove the reduction in SG&A expense as a percent of net sales in FY2023?

`financebench_id_00601` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The reduction in SG&A expense as a percent of net sales in FY2023 was primarily driven by lower marketing expenses and the leverage of incentive compensation due to higher sales, partially offset by deleverage of corporate overhead due to strategic investments and deleverage of store payroll and benefits due to wage investments [v3, v4, v5, v6].

**Computation:** `sga_pct_2023 = 2,350%  where sga_pct_2023 = 23.5% (units, FY2023), sga_pct_2022 = 23.9% (units, FY2022), reason_1 = lower marketing expenses (units, FY2023), reason_2 = leverage of incentive compensation due to higher sales (units, FY2023), reason_3 = deleverage of corporate overhead due to strategic investments (units, FY2023), reason_4 = deleverage of store payroll and benefits due to wage investments (units, FY2023)`

- **v3** · `ULTABEAUTY_2023Q4_EARNINGS` · PDF page **2** · column 2023 · units
  - Quote: "primarily due to lower marketing expenses and leverage of incentive compensation due to higher sales"

  <details><summary>Passage</summary>

  ```
   | a percentage of net sales, gross profit increased to 39.6% compared to 39.0% in fiscal
   | 2021, primarily due to leverage of fixed costs, strong growth in other revenue, and
   | favorable channel mix shifts, partially offset by higher inventory shrink and lower
   | merchandise margin.
   | SG&A expenses increased 16.2% to $2.4 billion compared to $2.1 billion in fiscal
   | 2021. As a percentage of net sales, SG&A expenses decreased to 23.5% compared to
   | 23.9% in fiscal 2021, primarily due to lower marketing expenses and leverage of
   | incentive compensation due to higher sales, partially offset by deleverage of corporate
   | overhead due to strategic investments and deleverage of store payroll and benefits
   | due to wage investments.
   | Operating income increased 26.3% to $1.6 billion, or 16.1% of net sales, compared to
   | $1.3 billion, or 15.0% of net sales, in fiscal 2021.
   | The tax rate increased to 24.4% compared to 23.9% in fiscal 2021.
  ```
  </details>

- **v4** · `ULTABEAUTY_2023Q4_EARNINGS` · PDF page **2** · column 2023 · units
  - Quote: "primarily due to lower marketing expenses and leverage of incentive compensation due to higher sales"

  <details><summary>Passage</summary>

  ```
  | Comparable sales (sales for stores open at least 14 months and e-commerce sales)
   | increased 15.6% compared to an increase of 21.4% in the fourth quarter of fiscal 2021,
   | driven by a 13.6% increase in transactions and a 1.8% increase in average ticket.
   | Gross profit increased 18.0% to $1.2 billion compared to $1.0 billion in the fourth
   | quarter of fiscal 2021. As a percentage of net sales, gross profit of 37.6% was flat
   | compared to the fourth quarter of fiscal 2021, primarily due to leverage of fixed costs,
   | favorable channel mix shifts, and strong growth in other revenue, offset by higher
   | inventory shrink.
   | Selling, general and administrative (SG&A) expenses increased 17.3% to $762.7
   | million compared to $650.0 million in the fourth quarter of fiscal 2021. As a percentage
   | of net sales, SG&A expenses decreased to 23.6% compared to 23.8% in the fourth
   | quarter of fiscal 2021, primarily due to leverage of marketing expenses and incentive
  ```
  </details>

- **v5** · `ULTABEAUTY_2023Q4_EARNINGS` · PDF page **2** · column 2023 · units
  - Quote: "partially offset by deleverage of corporate overhead due to strategic investments"

  <details><summary>Passage</summary>

  ```
   | favorable channel mix shifts, and strong growth in other revenue, offset by higher
   | inventory shrink.
   | Selling, general and administrative (SG&A) expenses increased 17.3% to $762.7
   | million compared to $650.0 million in the fourth quarter of fiscal 2021. As a percentage
   | of net sales, SG&A expenses decreased to 23.6% compared to 23.8% in the fourth
   | quarter of fiscal 2021, primarily due to leverage of marketing expenses and incentive
   | compensation due to higher sales, partially offset by deleverage of store payroll and
   | benefits due to wage investments and deleverage in corporate overhead due to
   | strategic investments.
   | Operating income increased 19.2% to $447.6 million, or 13.9% of net sales, compared
   | to $375.6 million, or 13.8% of net sales, in the fourth quarter of fiscal 2021.
   | The tax rate increased to 24.6% compared to 22.9% in the fourth quarter of fiscal
   | 2021.
  ```
  </details>

- **v6** · `ULTABEAUTY_2023Q4_EARNINGS` · PDF page **2** · column 2023 · units
  - Quote: "and deleverage of store payroll and benefits due to wage investments"

  <details><summary>Passage</summary>

  ```
   | favorable channel mix shifts, partially offset by higher inventory shrink and lower
   | merchandise margin.
   | SG&A expenses increased 16.2% to $2.4 billion compared to $2.1 billion in fiscal
   | 2021. As a percentage of net sales, SG&A expenses decreased to 23.5% compared to
   | 23.9% in fiscal 2021, primarily due to lower marketing expenses and leverage of
   | incentive compensation due to higher sales, partially offset by deleverage of corporate
   | overhead due to strategic investments and deleverage of store payroll and benefits
   | due to wage investments.
   | Operating income increased 26.3% to $1.6 billion, or 16.1% of net sales, compared to
   | $1.3 billion, or 15.0% of net sales, in fiscal 2021.
   | The tax rate increased to 24.4% compared to 23.9% in fiscal 2021.
   | Net income increased 26.0% to $1.2 billion compared to $985.8 million in fiscal 2021.
  ```
  </details>

<details><summary>Gold answer</summary>

Lower marketing expenses and leverage of incentive compensation due to higher sales. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 140. What drove the increase in Ulta Beauty's merchandise inventories balance at end of FY2023?

`financebench_id_00603` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: number check (G4) failed twice: numbers not in the evidence or the result: 2022,, 2022,

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Increase in Merchandise inventories balance was driven by the opening of 47 new stores. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 141. What percent of Ulta Beauty's total spend on stock repurchases for FY 2023 occurred in Q4 of FY2023?

`financebench_id_00605` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: extractor: The provided filing is for Q4 of fiscal year 2022 (filed March 9, 2023), not Q4 of fiscal year 2023. The document contains repurchase data for fiscal year 2022 and an outlook for fiscal year 2023, but it does not contain actual financial results or stock repurchase data for fiscal year 2023.

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

36%. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 142. Did Ulta Beauty's wages expense as a percent of net sales increase or decrease in FY2023?

`financebench_id_00606` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: extractor: The provided pages do not contain a specific line item for 'wages expense' or 'payroll expense'. While Page 2 mentions 'store payroll and benefits' in the context of SG&A deleverage, it does not provide a standalone dollar amount for wages expense for FY2022 (labeled as FY2023 in the question context but the filing is for FY2022 results) or FY2021 to calculate the percentage change. The Consolidated Statements of Income (Page 6) lists 'Selling, general and administrative expenses' but does not break out wages/payroll specifically.

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Wages expense as a percent of net sales increased in FY2023. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 143. Among all of the derivative instruments that Verizon used to manage the exposure to fluctuations of foreign currencies exchange rates or interest rates, which one had the highest notional value in FY 2021?

`financebench_id_00859` · filing `VERIZON_2021_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Cross currency swaps had the highest notional value at $32,502 million in FY 2021 [v1]. This amount exceeds the notional values of interest rate swaps ($19,779 million), forward starting interest rate swaps ($1,000 million), and foreign exchange forwards ($932 million) as reported in the document [v2, v3, v4].

**Computation:** `max(interest_rate_swaps_2021, cross_currency_swaps_2021, forward_starting_interest_rate_swaps_2021, foreign_exchange_forwards_2021) = 32,502 million  where cross_currency_swaps_2021 = 32,502 (millions, FY2021), interest_rate_swaps_2021 = 19,779 (millions, FY2021), forward_starting_interest_rate_swaps_2021 = 1,000 (millions, FY2021), foreign_exchange_forwards_2021 = 932 (millions, FY2021)`

- **v1** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Cross currency swaps \| 32,502 \| 26,288"

  <details><summary>Passage</summary>

  ```
  swaps, forward starting interest rate swaps, treasury rate locks, interest rate caps, swaptions and foreign exchange forwards. We do not hold
  derivatives for trading purposes.
  The following table sets forth the notional amounts of our outstanding derivative instruments:
   | (dollars in millions)
   At December 31, | 2021 | 2020
   Interest rate swaps | $19,779  $17,768
   Cross currency swaps | 32,502 | 26,288
   Forward starting interest rate swaps | 1,000 | 2,000
   Foreign exchange forwards | 932 | 1,405
   | Verizon 2021 Annual Report on Form 10-K
   | 85
  ```
  </details>

- **v2** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Interest rate swaps \| $19,779 \| $17,768"

  <details><summary>Passage</summary>

  ```
  We employ risk management strategies, which may include the use of a variety of derivatives including interest rate swaps, cross currency
  swaps, forward starting interest rate swaps, treasury rate locks, interest rate caps, swaptions and foreign exchange forwards. We do not hold
  derivatives for trading purposes.
  The following table sets forth the notional amounts of our outstanding derivative instruments:
   | (dollars in millions)
   At December 31, | 2021 | 2020
   Interest rate swaps | $19,779  $17,768
   Cross currency swaps | 32,502 | 26,288
   Forward starting interest rate swaps | 1,000 | 2,000
   Foreign exchange forwards | 932 | 1,405
   | Verizon 2021 Annual Report on Form 10-K
   | 85
  ```
  </details>

- **v3** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Forward starting interest rate swaps \| 1,000 \| 2,000"

  <details><summary>Passage</summary>

  ```
  derivatives for trading purposes.
  The following table sets forth the notional amounts of our outstanding derivative instruments:
   | (dollars in millions)
   At December 31, | 2021 | 2020
   Interest rate swaps | $19,779  $17,768
   Cross currency swaps | 32,502 | 26,288
   Forward starting interest rate swaps | 1,000 | 2,000
   Foreign exchange forwards | 932 | 1,405
   | Verizon 2021 Annual Report on Form 10-K
   | 85
  ```
  </details>

- **v4** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Foreign exchange forwards \| 932 \| 1,405"

  <details><summary>Passage</summary>

  ```
  The following table sets forth the notional amounts of our outstanding derivative instruments:
   | (dollars in millions)
   At December 31, | 2021 | 2020
   Interest rate swaps | $19,779  $17,768
   Cross currency swaps | 32,502 | 26,288
   Forward starting interest rate swaps | 1,000 | 2,000
   Foreign exchange forwards | 932 | 1,405
   | Verizon 2021 Annual Report on Form 10-K
   | 85
  ```
  </details>

<details><summary>Gold answer</summary>

Cross currency swaps. Its notional value was $32,502 million.
</details>

## 144. As of FY 2021, how much did Verizon expect to pay for its retirees in 2024?

`financebench_id_02024` · filing `VERIZON_2021_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** VERIZON_2021_10K: code checks failed twice: health_care_and_life_2024: the quote is not on page 94. Copy it exactly from one line of the page; formula: unknown value name 'health_care_and_life_2024' (names: ['pension_benefits_2024'])

**Pages searched:** `VERIZON_2021_10K` pages 1, 17, 40, 51, 52, 53, 54, 55, 78, 89, 94, 103

<details><summary>Gold answer</summary>

The estimated pension benefits were $1097 million, and the estimated health care and life insurance benefits were $862 million.
</details>

## 145. Does Verizon have a reasonably healthy liquidity profile based on its quick ratio for FY 2022? If the quick ratio is not relevant to measure liquidity, please state that and explain why.

`financebench_id_00216` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `None`

**Reason:** VERIZON_2022_10K: extractor: The quick ratio is calculated as (Cash + Accounts Receivable) / Current Liabilities. While the components are present on Page 56, the document does not explicitly state whether this ratio is 'reasonably healthy' or provide a qualitative assessment of the liquidity profile based on this specific metric. The question asks for a judgment ('Does Verizon have a reasonably healthy liquidity profile...'), which requires an interpretation of the calculated ratio against a standard or management's view, which is not provided in the text. Therefore, the evidence for the judgment is not found.

**Pages searched:** `VERIZON_2022_10K` pages 23, 26, 37, 42, 52, 54, 55, 56, 57, 58, 105, 106

<details><summary>Gold answer</summary>

No. The quick ratio was approximately 0.54 for Verizon. It indicated that Verizon does not have a healthy liquidity profile.
</details>

## 146. Is Verizon a capital intensive business based on FY 2022 data?

`financebench_id_00215` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Verizon is a capital intensive business based on FY 2022 data, as its capital expenditures of $23,087 million represented approximately 16.87% of its total operating revenues of $136,835 million [v1, v2, COMPUTED RESULT]. This high ratio indicates that a significant portion of the company's revenue is reinvested into maintaining and expanding its network infrastructure.

**Computation:** `capex_2022 / revenue_2022 = 16.8721%  where capex_2022 = 23,087 (millions, FY2022), revenue_2022 = 136,835 (millions, FY2022)`

- **v1** · `VERIZON_2022_10K` · PDF page **57** · column 2022 · millions
  - Quote: "Capital expenditures (including capitalized software) \| (23,087)"

  <details><summary>Passage</summary>

  ```
   | Inventories | 627 | (905) | (369)
   | Prepaid expenses and other | 928 | 150 | 1,202
   | Accounts payable and accrued liabilities and Other current liabilities | (33) | 1,457 | (966)
  Other, net | (3,778) | (93) | 2,780
   | Net cash provided by operating activities | 37,141 | 39,539 | 41,768
  Cash Flows from Investing Activities
  Capital expenditures (including capitalized software) | (23,087) | (20,286) | (18,192)
  Cash received (paid) related to acquisitions of businesses, net of cash acquired | 248 | (4,065) | (520)
  Acquisitions of wireless licenses | (3,653) | (47,596) | (3,896)
  Collateral payments related to derivative contracts, net of repayments | (2,265) | (21) | —
  Proceeds from disposition of business | 33 | 4,122 | —
  Other, net | 62 | 693 | (904)
   | Net cash used in investing activities | (28,662) | (67,153) | (23,512)
  ```
  </details>

- **v2** · `VERIZON_2022_10K` · PDF page **54** · column 2022 · millions
  - Quote: "Total Operating Revenues \| 136,835"

  <details><summary>Passage</summary>

  ```
   Verizon Communications Inc. and Subsidiaries
   | (dollars in millions, except per share amounts)
   Years Ended December 31, | 2022 | 2021 | 2020
   Operating Revenues
   | Service revenues and other | $109,625  $110,449  $109,872
   | Wireless equipment revenues | 27,210 | 23,164 | 18,420
   Total Operating Revenues | 136,835 | 133,613 | 128,292
   Operating Expenses
   | Cost of services (exclusive of items shown below) | 28,637 | 31,234 | 31,401
   | Cost of wireless equipment | 30,496 | 25,067 | 19,800
   | Selling, general and administrative expense | 30,136 | 28,658 | 31,573
   | Depreciation and amortization expense | 17,099 | 16,206 | 16,720
   Total Operating Expenses | 106,368 | 101,165 | 99,494
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. Verizon's capital intensity ratio was approximately 2.774729. This means that it took approximately $2.77 of assets to generate $1 of revenue and thus, Verizon can be considered capital intensive.
</details>

## 147. Has Verizon increased its debt on balance sheet between 2022 and the 2021 fiscal period?

`financebench_id_00566` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** No, Verizon did not increase its debt on the balance sheet between 2021 and 2022; instead, it decreased by $229 million, as total debt fell from $150,868 million in 2021 to $150,639 million in 2022 [v1, v2, COMPUTED RESULT].

**Computation:** `total_debt_2022 - total_debt_2021 = -229 million  where total_debt_2022 = $150,639 (millions, FY2022), total_debt_2021 = $150,868 (millions, FY2021)`

- **v1** · `VERIZON_2022_10K` · PDF page **77** · column 2022 · millions
  - Quote: "Total debt \| $150,639"

  <details><summary>Passage</summary>

  ```
   Less long-term debt maturing within one year | 9,813 | 7,443
   Total long-term debt | $140,676  $143,425
   Long-term debt maturing within one year | $9,813  $7,443
  Add commercial paper | 150 | —
   Debt maturing within one year | 9,963 | 7,443
  Add long-term debt | 140,676 | 143,425
   Total debt | $150,639  $150,868
  (1) The debt obligations bore interest at a floating rate based on the Compounded Secured Overnight Financing Rate (SOFR) for
    the interest period or the London Interbank Offered Rate (LIBOR) plus an applicable interest margin per annum, as applicable.
    Compounded SOFR is calculated using the SOFR Index published by the Federal Reserve Bank of New York in accordance
    with the formula set forth in the terms of the notes. The Compounded SOFR for the interest period ending in December 2022
    was 3.450%. The one-month and three-month LIBOR at December 31, 2022 was 4.392% and 4.767%, respectively.
  (2) The debt obligations bore interest at floating rates, including floating rates associated with SOFR for the interest period, or
  ```
  </details>

- **v2** · `VERIZON_2022_10K` · PDF page **77** · column 2021 · millions
  - Quote: "Total debt \| $150,868"

  <details><summary>Passage</summary>

  ```
   Less long-term debt maturing within one year | 9,813 | 7,443
   Total long-term debt | $140,676  $143,425
   Long-term debt maturing within one year | $9,813  $7,443
  Add commercial paper | 150 | —
   Debt maturing within one year | 9,963 | 7,443
  Add long-term debt | 140,676 | 143,425
   Total debt | $150,639  $150,868
  (1) The debt obligations bore interest at a floating rate based on the Compounded Secured Overnight Financing Rate (SOFR) for
    the interest period or the London Interbank Offered Rate (LIBOR) plus an applicable interest margin per annum, as applicable.
    Compounded SOFR is calculated using the SOFR Index published by the Federal Reserve Bank of New York in accordance
    with the formula set forth in the terms of the notes. The Compounded SOFR for the interest period ending in December 2022
    was 3.450%. The one-month and three-month LIBOR at December 31, 2022 was 4.392% and 4.767%, respectively.
  (2) The debt obligations bore interest at floating rates, including floating rates associated with SOFR for the interest period, or
  ```
  </details>

<details><summary>Gold answer</summary>

No. Verizon's debt decreased by $229 million.
</details>

## 148. What is FY2018 days payable outstanding (DPO) for Walmart? DPO is defined as: 365 * (average accounts payable between FY2017 and FY2018) / (FY2018 COGS + change in inventory between FY2017 and FY2018). Round your answer to two decimal places. Please base your judgments on the information provided primarily in the statement of financial position and the P&L statement.

`financebench_id_06247` · filing `WALMART_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 days payable outstanding (DPO) for Walmart is 42.69 days. This result is derived from the computed value using the provided financial figures for accounts payable, inventories, and cost of sales [v1, v2, v3, v4, v5].

**Computation:** `365 * avg(accounts_payable_2018, accounts_payable_2017) / (cost_of_sales_2018 + (inventories_2018 - inventories_2017)) = 42.69  where accounts_payable_2018 = 46,092 (millions, FY2018), accounts_payable_2017 = 41,433 (millions, FY2017), inventories_2018 = 43,783 (millions, FY2018), inventories_2017 = 43,046 (millions, FY2017), cost_of_sales_2018 = 373,396 (millions, FY2018)`

- **v1** · `WALMART_2018_10K` · PDF page **59** · column 2018 · millions
  - Quote: "Accounts payable \| 46,092"

  <details><summary>Passage</summary>

  ```
  Goodwill | 18,242 | 17,037
  Other assets and deferred charges | 11,798 | 9,921
  Total assets | $204,522 | $198,825
  LIABILITIES AND EQUITY
  Current liabilities:
   | Short-term borrowings | $5,257 | $1,099
   | Accounts payable | 46,092 | 41,433
   | Accrued liabilities | 22,122 | 20,654
   | Accrued income taxes | 645 | 921
   | Long-term debt due within one year | 3,738 | 2,256
   | Capital lease and financing obligations due within one year | 667 | 565
   | Total current liabilities | 78,521 | 66,928
  Long-term debt | 30,045 | 36,015
  ```
  </details>

- **v2** · `WALMART_2018_10K` · PDF page **59** · column 2017 · millions
  - Quote: "Accounts payable \| 41,433"

  <details><summary>Passage</summary>

  ```
  Goodwill | 18,242 | 17,037
  Other assets and deferred charges | 11,798 | 9,921
  Total assets | $204,522 | $198,825
  LIABILITIES AND EQUITY
  Current liabilities:
   | Short-term borrowings | $5,257 | $1,099
   | Accounts payable | 46,092 | 41,433
   | Accrued liabilities | 22,122 | 20,654
   | Accrued income taxes | 645 | 921
   | Long-term debt due within one year | 3,738 | 2,256
   | Capital lease and financing obligations due within one year | 667 | 565
   | Total current liabilities | 78,521 | 66,928
  Long-term debt | 30,045 | 36,015
  ```
  </details>

- **v3** · `WALMART_2018_10K` · PDF page **59** · column 2018 · millions
  - Quote: "Inventories \| 43,783"

  <details><summary>Passage</summary>

  ```
   | As of January 31,
  (Amounts in millions) | 2018 | 2017
  ASSETS
  Current assets:
   | Cash and cash equivalents | $6,756 | $6,867
   | Receivables, net | 5,614 | 5,835
   | Inventories | 43,783 | 43,046
   | Prepaid expenses and other | 3,511 | 1,941
   | Total current assets | 59,664 | 57,689
  Property and equipment:
   | Property and equipment | 185,154 | 179,492
   | Less accumulated depreciation | (77,479) | (71,782)
   | Property and equipment, net | 107,675 | 107,710
  ```
  </details>

- **v4** · `WALMART_2018_10K` · PDF page **59** · column 2017 · millions
  - Quote: "Inventories \| 43,046"

  <details><summary>Passage</summary>

  ```
   | As of January 31,
  (Amounts in millions) | 2018 | 2017
  ASSETS
  Current assets:
   | Cash and cash equivalents | $6,756 | $6,867
   | Receivables, net | 5,614 | 5,835
   | Inventories | 43,783 | 43,046
   | Prepaid expenses and other | 3,511 | 1,941
   | Total current assets | 59,664 | 57,689
  Property and equipment:
   | Property and equipment | 185,154 | 179,492
   | Less accumulated depreciation | (77,479) | (71,782)
   | Property and equipment, net | 107,675 | 107,710
  ```
  </details>

- **v5** · `WALMART_2018_10K` · PDF page **57** · column 2018 · millions
  - Quote: "Cost of sales \| 373,396"

  <details><summary>Passage</summary>

  ```
   (Amounts in millions, except per share data) | 2018 | 2017 | 2016
   Revenues:
   | Net sales | $495,761 | $481,317 | $478,614
   | Membership and other income | 4,582 | 4,556 | 3,516
   | Total revenues | 500,343 | 485,873 | 482,130
   Costs and expenses:
   | Cost of sales | 373,396 | 361,256 | 360,984
   | Operating, selling, general and administrative expenses | 106,510 | 101,853 | 97,041
   Operating income | 20,437 | 22,764 | 24,105
   Interest:
   | Debt | 1,978 | 2,044 | 2,027
   | Capital lease and financing obligations | 352 | 323 | 521
   | Interest income | (152) | (100) | (81)
  ```
  </details>

<details><summary>Gold answer</summary>

42.69
</details>

## 149. Based on the information provided primarily in the statement of income, what is the FY2018 - FY2019 change in unadjusted operating income % margin for Walmart? Answer in units of percents and round to one decimal place.

`financebench_id_04784` · filing `WALMART_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 to FY2019 change in unadjusted operating income margin for Walmart is 0.2%. This is calculated by taking the difference between the 2019 margin (21,957 / 510,329) and the 2018 margin (20,437 / 495,761), which equals 0.2% as stated in the computed result [v1, v2, v3, v4].

**Computation:** `(operating_income_2019 / net_sales_2019 - operating_income_2018 / net_sales_2018) = 0.2%  where operating_income_2019 = $21,957 (millions, FY2019), net_sales_2019 = $510,329 (millions, FY2019), operating_income_2018 = $20,437 (millions, FY2018), net_sales_2018 = $495,761 (millions, FY2018)`

- **v1** · `WALMART_2019_10K` · PDF page **48** · column 2019 · millions
  - Quote: "Operating income \| 21,957"

  <details><summary>Passage</summary>

  ```
   | Net sales | $510,329 | $495,761 | $481,317
   | Membership and other income | 4,076 | 4,582 | 4,556
   | Total revenues | 514,405 | 500,343 | 485,873
   Costs and expenses:
   | Cost of sales | 385,301 | 373,396 | 361,256
   | Operating, selling, general and administrative expenses | 107,147 | 106,510 | 101,853
   Operating income | 21,957 | 20,437 | 22,764
   Interest:
   | Debt | 1,975 | 1,978 | 2,044
   | Capital lease and financing obligations | 371 | 352 | 323
   | Interest income | (217) | (152) | (100)
   | Interest, net | 2,129 | 2,178 | 2,267
   Loss on extinguishment of debt | — | 3,136 | —
  ```
  </details>

- **v2** · `WALMART_2019_10K` · PDF page **48** · column 2019 · millions
  - Quote: "Net sales \| $510,329"

  <details><summary>Passage</summary>

  ```
  | Walmart Inc.
   | Consolidated Statements of Income
   | Fiscal Years Ended January 31,
   (Amounts in millions, except per share data) | 2019 | 2018 | 2017
   Revenues:
   | Net sales | $510,329 | $495,761 | $481,317
   | Membership and other income | 4,076 | 4,582 | 4,556
   | Total revenues | 514,405 | 500,343 | 485,873
   Costs and expenses:
   | Cost of sales | 385,301 | 373,396 | 361,256
   | Operating, selling, general and administrative expenses | 107,147 | 106,510 | 101,853
   Operating income | 21,957 | 20,437 | 22,764
  ```
  </details>

- **v3** · `WALMART_2019_10K` · PDF page **48** · column 2018 · millions
  - Quote: "Operating income \| 20,437"

  <details><summary>Passage</summary>

  ```
   | Net sales | $510,329 | $495,761 | $481,317
   | Membership and other income | 4,076 | 4,582 | 4,556
   | Total revenues | 514,405 | 500,343 | 485,873
   Costs and expenses:
   | Cost of sales | 385,301 | 373,396 | 361,256
   | Operating, selling, general and administrative expenses | 107,147 | 106,510 | 101,853
   Operating income | 21,957 | 20,437 | 22,764
   Interest:
   | Debt | 1,975 | 1,978 | 2,044
   | Capital lease and financing obligations | 371 | 352 | 323
   | Interest income | (217) | (152) | (100)
   | Interest, net | 2,129 | 2,178 | 2,267
   Loss on extinguishment of debt | — | 3,136 | —
  ```
  </details>

- **v4** · `WALMART_2019_10K` · PDF page **48** · column 2018 · millions
  - Quote: "Net sales \| $495,761"

  <details><summary>Passage</summary>

  ```
  | Walmart Inc.
   | Consolidated Statements of Income
   | Fiscal Years Ended January 31,
   (Amounts in millions, except per share data) | 2019 | 2018 | 2017
   Revenues:
   | Net sales | $510,329 | $495,761 | $481,317
   | Membership and other income | 4,076 | 4,582 | 4,556
   | Total revenues | 514,405 | 500,343 | 485,873
   Costs and expenses:
   | Cost of sales | 385,301 | 373,396 | 361,256
   | Operating, selling, general and administrative expenses | 107,147 | 106,510 | 101,853
   Operating income | 21,957 | 20,437 | 22,764
  ```
  </details>

<details><summary>Gold answer</summary>

0.2%
</details>

## 150. What is the FY2018 - FY2020 3 year average unadjusted EBITDA % margin for Walmart? Define unadjusted EBITDA as unadjusted operating income + depreciation and amortization from the cash flow statement. Answer in units of percents and round to one decimal place. Calculate what was asked by utilizing the line items clearly shown in the P&L statement and the cash flow statement.

`financebench_id_06741` · filing `WALMART_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-9B`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018-FY2020 3-year average unadjusted EBITDA margin for Walmart is 6.2%. This is calculated by averaging the sum of operating income and depreciation/amortization divided by net sales for each of the three years, using the values from the Consolidated Statements of Income and Consolidated Statements of Cash Flows [v1, v2, v3, v4, v5, v6, v7, v8, v9].

**Computation:** `avg(((operating_income_2020 + depreciation_and_amortization_2020) / net_sales_2020), ((operating_income_2019 + depreciation_and_amortization_2019) / net_sales_2019), ((operating_income_2018 + depreciation_and_amortization_2018) / net_sales_2018)) = 6.2%  where operating_income_2020 = $20,568 (millions, FY2020), operating_income_2019 = $21,957 (millions, FY2019), operating_income_2018 = $20,437 (millions, FY2018), depreciation_and_amortization_2020 = 10,987 (millions, FY2020), depreciation_and_amortization_2019 = 10,678 (millions, FY2019), depreciation_and_amortization_2018 = 10,529 (millions, FY2018), net_sales_2020 = $519,926 (millions, FY2020), net_sales_2019 = $510,329 (millions, FY2019), net_sales_2018 = $495,761 (millions, FY2018)`

- **v1** · `WALMART_2020_10K` · PDF page **51** · column 2020 · millions
  - Quote: "Operating income \| 20,568"

  <details><summary>Passage</summary>

  ```
   | Net sales | $519,926 | $510,329 | $495,761
   | Membership and other income | 4,038 | 4,076 | 4,582
   | Total revenues | 523,964 | 514,405 | 500,343
   Costs and expenses:
   | Cost of sales | 394,605 | 385,301 | 373,396
   | Operating, selling, general and administrative expenses | 108,791 | 107,147 | 106,510
   Operating income | 20,568 | 21,957 | 20,437
   Interest:
   | Debt | 2,262 | 1,975 | 1,978
   | Finance, capital lease and financing obligations | 337 | 371 | 352
   | Interest income | (189) | (217) | (152)
   | Interest, net | 2,410 | 2,129 | 2,178
   Loss on extinguishment of debt | — | — | 3,136
  ```
  </details>

- **v2** · `WALMART_2020_10K` · PDF page **51** · column 2019 · millions
  - Quote: "Operating income \| 21,957"

  <details><summary>Passage</summary>

  ```
   | Net sales | $519,926 | $510,329 | $495,761
   | Membership and other income | 4,038 | 4,076 | 4,582
   | Total revenues | 523,964 | 514,405 | 500,343
   Costs and expenses:
   | Cost of sales | 394,605 | 385,301 | 373,396
   | Operating, selling, general and administrative expenses | 108,791 | 107,147 | 106,510
   Operating income | 20,568 | 21,957 | 20,437
   Interest:
   | Debt | 2,262 | 1,975 | 1,978
   | Finance, capital lease and financing obligations | 337 | 371 | 352
   | Interest income | (189) | (217) | (152)
   | Interest, net | 2,410 | 2,129 | 2,178
   Loss on extinguishment of debt | — | — | 3,136
  ```
  </details>

- **v3** · `WALMART_2020_10K` · PDF page **51** · column 2018 · millions
  - Quote: "Operating income \| 20,437"

  <details><summary>Passage</summary>

  ```
   | Net sales | $519,926 | $510,329 | $495,761
   | Membership and other income | 4,038 | 4,076 | 4,582
   | Total revenues | 523,964 | 514,405 | 500,343
   Costs and expenses:
   | Cost of sales | 394,605 | 385,301 | 373,396
   | Operating, selling, general and administrative expenses | 108,791 | 107,147 | 106,510
   Operating income | 20,568 | 21,957 | 20,437
   Interest:
   | Debt | 2,262 | 1,975 | 1,978
   | Finance, capital lease and financing obligations | 337 | 371 | 352
   | Interest income | (189) | (217) | (152)
   | Interest, net | 2,410 | 2,129 | 2,178
   Loss on extinguishment of debt | — | — | 3,136
  ```
  </details>

- **v4** · `WALMART_2020_10K` · PDF page **56** · column 2020 · millions
  - Quote: "Depreciation and amortization \| 10,987"

  <details><summary>Passage</summary>

  ```
   | Consolidated Statements of Cash Flows
   | Fiscal Years Ended January 31,
  (Amounts in millions) | 2020 | 2019 | 2018
  Cash flows from operating activities:
   | Consolidated net income | $15,201 | $7,179 | $10,523
   | Adjustments to reconcile consolidated net income to net cash provided by operating activities:
   | Depreciation and amortization | 10,987 | 10,678 | 10,529
   | Unrealized (gains) and losses | (1,886) | 3,516 | —
   | (Gains) and losses for disposal of business operations | 15 | 4,850 | —
   | Asda pension contribution | (1,036) | — | —
   | Deferred income taxes | 320 | (499) | (304)
   | Loss on extinguishment of debt | — | — | 3,136
   | Other operating activities | 1,981 | 1,734 | 1,210
  ```
  </details>

- **v5** · `WALMART_2020_10K` · PDF page **56** · column 2019 · millions
  - Quote: "Depreciation and amortization \| 10,678"

  <details><summary>Passage</summary>

  ```
   | Consolidated Statements of Cash Flows
   | Fiscal Years Ended January 31,
  (Amounts in millions) | 2020 | 2019 | 2018
  Cash flows from operating activities:
   | Consolidated net income | $15,201 | $7,179 | $10,523
   | Adjustments to reconcile consolidated net income to net cash provided by operating activities:
   | Depreciation and amortization | 10,987 | 10,678 | 10,529
   | Unrealized (gains) and losses | (1,886) | 3,516 | —
   | (Gains) and losses for disposal of business operations | 15 | 4,850 | —
   | Asda pension contribution | (1,036) | — | —
   | Deferred income taxes | 320 | (499) | (304)
   | Loss on extinguishment of debt | — | — | 3,136
   | Other operating activities | 1,981 | 1,734 | 1,210
  ```
  </details>

- **v6** · `WALMART_2020_10K` · PDF page **56** · column 2018 · millions
  - Quote: "Depreciation and amortization \| 10,529"

  <details><summary>Passage</summary>

  ```
   | Consolidated Statements of Cash Flows
   | Fiscal Years Ended January 31,
  (Amounts in millions) | 2020 | 2019 | 2018
  Cash flows from operating activities:
   | Consolidated net income | $15,201 | $7,179 | $10,523
   | Adjustments to reconcile consolidated net income to net cash provided by operating activities:
   | Depreciation and amortization | 10,987 | 10,678 | 10,529
   | Unrealized (gains) and losses | (1,886) | 3,516 | —
   | (Gains) and losses for disposal of business operations | 15 | 4,850 | —
   | Asda pension contribution | (1,036) | — | —
   | Deferred income taxes | 320 | (499) | (304)
   | Loss on extinguishment of debt | — | — | 3,136
   | Other operating activities | 1,981 | 1,734 | 1,210
  ```
  </details>

- **v7** · `WALMART_2020_10K` · PDF page **51** · column 2020 · millions
  - Quote: "Net sales \| $519,926"

  <details><summary>Passage</summary>

  ```
  | Walmart Inc.
   | Consolidated Statements of Income
   | Fiscal Years Ended January 31,
   (Amounts in millions, except per share data) | 2020 | 2019 | 2018
   Revenues:
   | Net sales | $519,926 | $510,329 | $495,761
   | Membership and other income | 4,038 | 4,076 | 4,582
   | Total revenues | 523,964 | 514,405 | 500,343
   Costs and expenses:
   | Cost of sales | 394,605 | 385,301 | 373,396
   | Operating, selling, general and administrative expenses | 108,791 | 107,147 | 106,510
   Operating income | 20,568 | 21,957 | 20,437
  ```
  </details>

- **v8** · `WALMART_2020_10K` · PDF page **51** · column 2019 · millions
  - Quote: "Net sales \| $510,329"

  <details><summary>Passage</summary>

  ```
  | Walmart Inc.
   | Consolidated Statements of Income
   | Fiscal Years Ended January 31,
   (Amounts in millions, except per share data) | 2020 | 2019 | 2018
   Revenues:
   | Net sales | $519,926 | $510,329 | $495,761
   | Membership and other income | 4,038 | 4,076 | 4,582
   | Total revenues | 523,964 | 514,405 | 500,343
   Costs and expenses:
   | Cost of sales | 394,605 | 385,301 | 373,396
   | Operating, selling, general and administrative expenses | 108,791 | 107,147 | 106,510
   Operating income | 20,568 | 21,957 | 20,437
  ```
  </details>

- **v9** · `WALMART_2020_10K` · PDF page **51** · column 2018 · millions
  - Quote: "Net sales \| $495,761"

  <details><summary>Passage</summary>

  ```
  | Walmart Inc.
   | Consolidated Statements of Income
   | Fiscal Years Ended January 31,
   (Amounts in millions, except per share data) | 2020 | 2019 | 2018
   Revenues:
   | Net sales | $519,926 | $510,329 | $495,761
   | Membership and other income | 4,038 | 4,076 | 4,582
   | Total revenues | 523,964 | 514,405 | 500,343
   Costs and expenses:
   | Cost of sales | 394,605 | 385,301 | 373,396
   | Operating, selling, general and administrative expenses | 108,791 | 107,147 | 106,510
   Operating income | 20,568 | 21,957 | 20,437
  ```
  </details>

<details><summary>Gold answer</summary>

6.2%
</details>
