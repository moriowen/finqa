# Answers with provenance: all-27b-full

Configuration: `all-27b-full`. One section per question, in dataset order. Status ANSWER = all checks passed; NOT_FOUND / AMBIGUOUS = the system abstained (the reason says which check failed). PDF page numbers are 1-based. `Judge` is the eval label against the gold answer (not visible to the system).

## 1. What is the FY2018 capital expenditure amount (in USD millions) for 3M? Give a response to the question by relying on the details shown in the cash flow statement.

`financebench_id_03029` · filing `3M_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 capital expenditure amount for 3M is 1,577 million USD. This figure is derived from the absolute value of the "Purchases of property, plant and equipment (PP&E)" line item, which is reported as (1,577) million in the Consolidated Statement of Cash Flows [v1].

**Computation:** `abs(capex_2018) = 1,577 million  where capex_2018 = (1,577) (millions, FY2018)`

- **v1** · `3M_2018_10K` · PDF page **60** · column 2018 · millions
  - Quote: "Purchases of property, plant and equipment (PP&E) \| (1,577)"

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

<details><summary>Gold answer</summary>

$1577.00
</details>

## 2. Assume that you are a public equities analyst. Answer the following question by primarily using information that is shown in the balance sheet: what is the year end FY2018 net PPNE for 3M? Answer in USD billions.

`financebench_id_04672` · filing `3M_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The year-end FY2018 net PPNE for 3M is 8.74 billion USD. This figure is derived from the Consolidated Balance Sheet, which reports net property, plant, and equipment as 8,738 million dollars for 2018 [v1].

**Computation:** `net_ppne_2018 = 8.74 billion  where net_ppne_2018 = 8,738 (millions, FY2018)`

- **v1** · `3M_2018_10K` · PDF page **58** · column 2018 · millions
  - Quote: "Property, plant and equipment — net \| 8,738 \| 8,866"

  <details><summary>Passage</summary>

  ```
   | Total inventories | 4,366 | 4,034
   | Prepaids | 741 | 937
   | Other current assets | 349 | 266
   | Total current assets | 13,709 | 14,277
  Property, plant and equipment | 24,873 | 24,914
   | Less: Accumulated depreciation | (16,135) | (16,048)
   | Property, plant and equipment — net | 8,738 | 8,866
  Goodwill | 10,051 | 10,513
  Intangible assets — net | 2,657 | 2,936
  Other assets | 1,345 | 1,395
   | Total assets | $36,500 | $37,987
  Liabilities
  Current liabilities
  ```
  </details>

<details><summary>Gold answer</summary>

$8.70
</details>

## 3. Is 3M a capital-intensive business based on FY2022 data?

`financebench_id_00499` · filing `3M_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** 3M_2022_10K: code checks failed twice: purchases_of_pp_and_e_2022: the quote is not on page 52. Copy it exactly from one line of the page; formula: unknown value name 'net_sales_2022' (names: [])

**Pages searched:** `3M_2022_10K` pages 2, 3, 37, 38, 39, 41, 48, 49, 50, 51, 52, 68

<details><summary>Gold answer</summary>

No, the company is managing its CAPEX and Fixed Assets pretty efficiently, which is evident from below key metrics: CAPEX/Revenue Ratio: 5.1% Fixed assets/Total Assets: 20% Return on Assets= 12.4%
</details>

## 4. What drove operating margin change as of FY2022 for 3M? If operating margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_01226` · filing `3M_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** 3M's operating margin decreased by 1.7% to 19.1% in FY2022, driven primarily by increased litigation costs related to PFAS and Combat Arms Earplugs, higher raw material and logistics costs, and goodwill impairment expenses [v1, v2, v3, v8, v9, v10, v7]. These negative factors were partially offset by an $8.0% gain on business divestitures and price increases [v6, v10]. Operating margin remains a useful metric for 3M as it is a standard measure of profitability for this industrial manufacturing company [v1].

- **v1** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Operating income margin \| 19.1 %"

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
  - Quote: "Operating income margin \| 20.8 %"

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

- **v3** · `3M_2022_10K` · PDF page **27** · column Change · units
  - Quote: "Operating income margin \| (1.7)%"

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

- **v6** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Gain on business divestitures \| (8.0)"

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

- **v7** · `3M_2022_10K` · PDF page **27** · column 2022 · units
  - Quote: "Goodwill impairment expense \| 0.8"

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

- **v8** · `3M_2022_10K` · PDF page **27** · column N/A · units
  - Quote: "Cost of sales... Increases were primarily due to 2022 special item costs for significant litigation from additional commitments to address PFAS-related matters at 3M's Zwijndrecht, Belgium site"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  ```
  </details>

- **v9** · `3M_2022_10K` · PDF page **27** · column N/A · units
  - Quote: "SG&A was impacted by increased special item costs for significant litigation primarily related to steps toward resolving Combat Arms Earplugs litigation"

  <details><summary>Passage</summary>

  ```
  Cost of Sales:
  Cost of sales, measured as a percent of sales, increased in 2022 when compared to the same period last year. Increases were primarily due to 2022 special item costs for
  significant litigation from additional commitments to address PFAS-related matters at 3M's Zwijndrecht, Belgium site (discussed in Note 16), higher raw materials and logistics
  costs, manufacturing productivity headwinds which were further magnified by the shutdown of certain operations in Belgium and progress on restarting previously-idled
  operations, and investments in growth, productivity and sustainability. On a percent of sales basis, these increases were partially offset by increases in selling prices.
  Selling, General and Administrative Expenses:
  SG&A, measured as a percent of sales, increased in 2022 when compared to the same period last year. SG&A was impacted by increased special item costs for significant
  litigation primarily related to steps toward resolving Combat Arms Earplugs litigation (discussed in Note 16) resulting in a 2022 second quarter pre-tax charge of approximately
  $1.2 billion, certain impairment costs related to exiting PFAS manufacturing (see Note 15), costs related to exiting Russia (see Note 15), divestiture-related restructuring
  charges (see Note 5), and continued investment in key growth initiatives. These increases were partially offset by restructuring benefits and ongoing general 3M cost
  management.
  Research, Development and Related Expenses:
  R&D, measured as a percent of sales, decreased in 2022 when compared to the same period last year. 3M continues to invest in a range of R&D activities from application
  ```
  </details>

- **v10** · `3M_2022_10K` · PDF page **27** · column N/A · units
  - Quote: "Cost of sales... higher raw materials and logistics costs"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  RESULTS OF OPERATIONS
  Net Sales:
  Refer to the preceding “Overview” section and the “Performance by Business Segment” section later in MD&A for additional discussion of sales change.
  Operating Expenses:
  (Percent of net sales) | 2022 | 2021 | Change
  Cost of sales | 56.2 % | 53.2 % | 3.0 %
  ```
  </details>

<details><summary>Gold answer</summary>

Operating Margin for 3M in FY2022 has decreased by 1.7% primarily due to:  -Decrease in gross Margin -mostly one-off charges including Combat Arms Earplugs litigation, impairment related to exiting PFAS manufacturing, costs related to exiting Russia and divestiture-related restructuring charges
</details>

## 5. If we exclude the impact of M&A, which segment has dragged down 3M's overall growth in 2022?

`financebench_id_01865` · filing `3M_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** 3M_2022_10K: extractor: The provided pages contain organic sales data for Safety and Industrial (Page 30), Health Care (Page 32), and Consumer (Page 33) for 2022. However, the page containing the 'Transportation and Electronics' segment data (likely Page 31 based on the sequence) is not included in the provided text. Without the organic sales growth rate for the Transportation and Electronics segment, it is impossible to definitively determine which segment dragged down overall growth, as the missing segment could have had negative growth larger than the Consumer segment's (0.9)% decline.

**Pages searched:** `3M_2022_10K` pages 3, 19, 21, 30, 32, 33, 48, 49, 50, 51, 52, 68

<details><summary>Gold answer</summary>

The consumer segment shrunk by 0.9% organically.
</details>

## 6. Does 3M have a reasonably healthy liquidity profile based on its quick ratio for Q2 of FY2023? If the quick ratio is not relevant to measure liquidity, please state that and explain why.

`financebench_id_00807` · filing `3M_2023Q2_10Q` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, 3M has a reasonably healthy liquidity profile based on its quick ratio of 0.96 for Q2 of FY2023 [v1, v2, v3]. This ratio is calculated by subtracting total inventories of $5,280 million from total current assets of $15,754 million and dividing by total current liabilities of $10,936 million [v1, v2, v3]. A quick ratio near 1.0 indicates the company can cover its short-term obligations with its most liquid assets, excluding inventory [v1, v2, v3].

**Computation:** `(total_current_assets - total_inventories) / total_current_liabilities = 0.96  where total_current_assets = 15,754 (millions, Q2 FY2023), total_inventories = 5,280 (millions, Q2 FY2023), total_current_liabilities = 10,936 (millions, Q2 FY2023)`

- **v1** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
  - Quote: "Total current assets \| 15,754"

  <details><summary>Passage</summary>

  ```
   | Finished goods | 2,526 | 2,497
   | Work in process | 1,527 | 1,606
   | Raw materials and supplies | 1,227 | 1,269
   | Total inventories | 5,280 | 5,372
   | Prepaids | 674 | 435
   | Other current assets | 539 | 456
   | Total current assets | 15,754 | 14,688
  Property, plant and equipment | 26,459 | 25,998
   | Less: Accumulated depreciation | (17,248) | (16,820)
   | Property, plant and equipment — net | 9,211 | 9,178
  Operating lease right of use assets | 812 | 829
  Goodwill | 12,869 | 12,790
  Intangible assets — net | 4,470 | 4,699
  ```
  </details>

- **v2** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
  - Quote: "Total inventories \| 5,280"

  <details><summary>Passage</summary>

  ```
   | Marketable securities — current | 56 | 238
   | Accounts receivable — net of allowances of $160 and $174 | 4,947 | 4,532
   | Inventories
   | Finished goods | 2,526 | 2,497
   | Work in process | 1,527 | 1,606
   | Raw materials and supplies | 1,227 | 1,269
   | Total inventories | 5,280 | 5,372
   | Prepaids | 674 | 435
   | Other current assets | 539 | 456
   | Total current assets | 15,754 | 14,688
  Property, plant and equipment | 26,459 | 25,998
   | Less: Accumulated depreciation | (17,248) | (16,820)
   | Property, plant and equipment — net | 9,211 | 9,178
  ```
  </details>

- **v3** · `3M_2023Q2_10Q` · PDF page **5** · column June 30, 2023 · millions
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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** 3M_2023Q2_10Q: number check (G4) failed twice: numbers not in the evidence or the result: 2026,, 2030,

**Pages searched:** `3M_2023Q2_10Q` pages 1, 2, 4, 5, 6, 19, 27, 70, 71, 73, 85, 91

<details><summary>Gold answer</summary>

Following debt securities registered under 3M's name are listed to trade on the New York Stock Exchange: -1.500% Notes due 2026 (Trading Symbol: MMM26) -1.750% Notes due 2030 (Trading Symbol: MMM30) -1.500% Notes due 2031 (Trading Symbol: MMM31)
</details>

## 8. Does 3M maintain a stable trend of dividend distribution?

`financebench_id_01858` · filing `3M_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, 3M maintains a stable trend of dividend distribution, as evidenced by its 65th consecutive year of dividend increases [v3]. The company declared a $1.50 per share dividend for both the first and second quarters, maintaining a consistent annual rate of $6.00 per share [v1, v2, v4].

- **v1** · `3M_2023Q2_10Q` · PDF page **62** · column February 2023 · units
  - Quote: "In February 2023, 3M's Board of Directors declared a first-quarter 2023 dividend of $1.50 per share, an increase of 1 percent."

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
  - Quote: "In May 2023, 3M's Board of Directors declared a second-quarter 2023 dividend of $1.50 per share."

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

- **v3** · `3M_2023Q2_10Q` · PDF page **62** · column February 2023 · units
  - Quote: "This marked the 65th consecutive year of dividend increases for 3M."

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

- **v4** · `3M_2023Q2_10Q` · PDF page **73** · column February 2023 · units
  - Quote: "This is equivalent to an annual dividend of $6.00 per share"

  <details><summary>Passage</summary>

  ```
  commercial paper issuances. 2022 issuances, maturities, and extinguishments of short-and long-term debt are described in Note 10 to the Consolidated Financial Statements in
  3M’s 2022 Annual Report on Form 10-K.
  Repurchases of common stock are made to support the Company’s stock-based employee compensation plans and for other corporate purposes. In the first six months of 2023,
  the Company purchased $29 million of its own stock. For more information, refer to the table titled “Issuer Purchases of Equity Securities” in Part II, Item 2. The Company
  does not utilize derivative instruments linked to the Company’s stock.
  3M has paid dividends since 1916. In February 2023, 3M’s Board of Directors declared a first-quarter 2023 dividend of $1.50 per share, an increase of 1 percent. This is
  equivalent to an annual dividend of $6.00 per share and marked the 65th consecutive year of dividend increases. In May 2023, 3M's Board of Directors declared a second-
  quarter 2023 dividend of $1.50 per share.
  Other cash flows from financing activities may include various other items, such as cash paid associated with certain derivative instruments, distributions to or sales of
  noncontrolling interests, changes in overdraft balances, and principal payments for finance leases.
  Free Cash Flow (non-GAAP measure):
  Free cash flow and free cash flow conversion are not defined under U.S. generally accepted accounting principles (GAAP). Therefore, they should not be considered a
  substitute for income (loss) or cash flow data prepared in accordance with U.S. GAAP and may not be comparable to similarly titled measures used by other companies. The
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, not only they distribute the dividends on a routine basis, 3M has also been increasing the per share dividend for consecutive 65 years
</details>

## 9. What is the FY2019 fixed asset turnover ratio for Activision Blizzard? Fixed asset turnover ratio is defined as: FY2019 revenue / (average PP&E between FY2018 and FY2019). Round your answer to two decimal places. Base your judgments on the information provided primarily in the statement of income and the statement of financial position.

`financebench_id_02987` · filing `ACTIVISIONBLIZZARD_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 fixed asset turnover ratio for Activision Blizzard is 24.26. This value is computed by dividing the total net revenues of 6,489 million for 2019 by the average of the property and equipment, net, values of 253 million for 2019 and 282 million for 2018 [v1, v2, v3]. The system calculated this ratio as 24.26 based on these specific figures [v1, v2, v3].

**Computation:** `total_net_revenues_2019 / avg(ppe_2019, ppe_2018) = 24.26  where total_net_revenues_2019 = 6,489 (millions, FY2019), ppe_2019 = 253 (millions, FY2019), ppe_2018 = 282 (millions, FY2018)`

- **v1** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2019 · millions
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

- **v2** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **69** · column At December 31, 2019 · millions
  - Quote: "Property and equipment, net \| 253"

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

- **v3** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **69** · column At December 31, 2018 · millions
  - Quote: "Property and equipment, net \| 282"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average of capital expenditures as a percentage of revenue for Activision Blizzard from FY2017 to FY2019 is 1.9%. This figure is calculated using the capital expenditures of $155 million, $131 million, and $116 million against total net revenues of $7,017 million, $7,500 million, and $6,489 million for the respective years [v1, v2, v3, v4, v5, v6].

**Computation:** `avg(abs(capex_2017)/revenue_2017, abs(capex_2018)/revenue_2018, abs(capex_2019)/revenue_2019) = 1.9%  where capex_2017 = (155) (millions, FY2017), capex_2018 = (131) (millions, FY2018), capex_2019 = (116) (millions, FY2019), revenue_2017 = 7,017 (millions, FY2017), revenue_2018 = 7,500 (millions, FY2018), revenue_2019 = 6,489 (millions, FY2019)`

- **v1** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **73** · column 2017 · millions
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

- **v3** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **73** · column 2019 · millions
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

- **v4** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2017 · millions
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

- **v6** · `ACTIVISIONBLIZZARD_2019_10K` · PDF page **70** · column 2019 · millions
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

<details><summary>Gold answer</summary>

1.9%
</details>

## 11. You are an investment banker and your only resource(s) to answer the following question is (are): the statement of financial position and the cash flow statement. Here's the question: what is the FY2015 operating cash flow ratio for Adobe? Operating cash flow ratio is defined as: cash from operations / total current liabilities. Round your answer to two decimal places.

`financebench_id_04735` · filing `ADOBE_2015_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 operating cash flow ratio for Adobe is 0.66. This is calculated by dividing the net cash provided by operating activities of $1,469,502 thousand by the total current liabilities of $2,213,556 thousand [v1, v2].

**Computation:** `net_cash_provided_by_operating_activities_2015 / total_current_liabilities_2015 = 0.66  where net_cash_provided_by_operating_activities_2015 = 1,469,502 (thousands, FY2015), total_current_liabilities_2015 = 2,213,556 (thousands, FY2015)`

- **v1** · `ADOBE_2015_10K` · PDF page **63** · column November 27, 2015 · thousands
  - Quote: "Net cash provided by operating activities......................................................................... \| 1,469,502"

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

- **v2** · `ADOBE_2015_10K` · PDF page **59** · column November 27, 2015 · thousands
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Adobe's year-over-year change in unadjusted operating income from FY2015 to FY2016 is 65.4%. This increase is calculated using the operating income of 1,493,602 thousand for FY2016 and 903,095 thousand for FY2015 [v1, v2]. The computed result confirms the growth rate based on these figures [COMPUTED RESULT].

**Computation:** `(operating_income_2016 - operating_income_2015) / operating_income_2015 = 65.4%  where operating_income_2016 = 1,493,602 (thousands, FY2016), operating_income_2015 = 903,095 (thousands, FY2015)`

- **v1** · `ADOBE_2016_10K` · PDF page **62** · column December 2, 2016 · thousands
  - Quote: "Operating income \| 1,493,602 \| 903,095 \| 412,685"

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

- **v2** · `ADOBE_2016_10K` · PDF page **62** · column November 27, 2015 · thousands
  - Quote: "Operating income \| 1,493,602 \| 903,095 \| 412,685"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2017 operating cash flow ratio for Adobe is 0.83. This is calculated by dividing the net cash provided by operating activities of $2,912,853 thousand by the total current liabilities of $3,527,457 thousand [v1, v2]. The computed result of this division is exactly 0.83 [COMPUTED RESULT].

**Computation:** `cash_from_operations_2017 / total_current_liabilities_2017 = 0.83  where cash_from_operations_2017 = 2,912,853 (thousands, FY2017), total_current_liabilities_2017 = 3,527,457 (thousands, FY2017)`

- **v1** · `ADOBE_2017_10K` · PDF page **61** · column December 1, 2017 · thousands
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

- **v2** · `ADOBE_2017_10K` · PDF page **57** · column December 1, 2017 · thousands
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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, Adobe does not have an improving operating margin profile as of FY2022, as the metric declined by 2.12% compared to the prior year [v1, v2, v3, v4]. The computed result shows a decrease in the operating margin from FY2021 to FY2022, indicating a deterioration rather than an improvement [COMPUTED RESULT]. Operating margin is a useful metric for Adobe as it is a profitable software company with significant operating income [v2, v4].

**Computation:** `((operating_income_2022 / total_revenue_2022) - (operating_income_2021 / total_revenue_2021)) = -2.12%  where total_revenue_2022 = 17,606 (millions, FY2022), operating_income_2022 = 6,098 (millions, FY2022), total_revenue_2021 = 15,785 (millions, FY2021), operating_income_2021 = 5,802 (millions, FY2021), total_revenue_2020 = 12,868 (millions, FY2020), operating_income_2020 = 4,237 (millions, FY2020)`

- **v1** · `ADOBE_2022_10K` · PDF page **54** · column December 2, 2022 · millions
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

- **v2** · `ADOBE_2022_10K` · PDF page **54** · column December 2, 2022 · millions
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

- **v3** · `ADOBE_2022_10K` · PDF page **54** · column December 3, 2021 · millions
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

- **v4** · `ADOBE_2022_10K` · PDF page **54** · column December 3, 2021 · millions
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

<details><summary>Gold answer</summary>

No the operating margins of Adobe have recently declined from 36.8% in FY 2021 to 34.6% in FY2022. A drop by 2.2% in a year.
</details>

## 15. Does Adobe have an improving Free cashflow conversion as of FY2022?

`financebench_id_00591` · filing `ADOBE_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** ADOBE_2022_10K: verifier: answer_supported=no. The formula used to calculate 'Free cashflow conversion' is incorrect. Free cash flow conversion is typically defined as Free Cash Flow divided by Net Income. The computation provided calculates the ratio of (Net Cash from Operating Activities + Capex) to Net Cash from Operating Activities, which is not a standard financial metric for conversion.

**Pages searched:** `ADOBE_2022_10K` pages 3, 5, 6, 11, 39, 53, 54, 55, 57, 58, 90

<details><summary>Gold answer</summary>

Yes, the FCF conversion (using net income as the denominator) for Adobe has improved by ~13% from 143% in 2021 to 156% in 2022
</details>

## 16. What is the quantity of restructuring costs directly outlined in AES Corporation's income statements for FY2022? If restructuring costs are not explicitly outlined then state 0.

`financebench_id_01319` · filing `AES_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AES_2022_10K: code checks failed twice: formula: numeric constant 0 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `AES_2022_10K` pages 84, 86, 94, 95, 130, 132, 133, 135, 181, 214, 215, 216, 217

<details><summary>Gold answer</summary>

0
</details>

## 17. Roughly how many times has AES Corporation sold its inventory in FY2022? Calculate inventory turnover ratio for the FY2022; if conventional inventory management is not meaningful for the company then state that and explain why.

`financebench_id_00540` · filing `AES_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The inventory turnover ratio is not meaningful for AES Corporation because it is primarily an energy generation and distribution company rather than a traditional retailer or manufacturer that holds significant inventory for sale [v4]. The company's inventory balance of $1,055 million in 2022 represents fuel and maintenance supplies rather than finished goods intended for direct sale to customers [v2]. Consequently, calculating how many times inventory was "sold" does not reflect the company's core business operations [v1, v2].

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

- **v2** · `AES_2022_10K` · PDF page **130** · column 2022 · millions
  - Quote: "Inventory \| 1,055"

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

- **v4** · `AES_2022_10K` · PDF page **5** · column N/A · units
  - Quote: "In this Annual Report the terms “AES,” “the Company,” “us,” or “we” refer to The AES Corporation and all of its subsidiaries and affiliates, collectively."

  <details><summary>Passage</summary>

  ```
  3 | 2022 Annual Report
   | PART I
   | In this Annual Report the terms “AES,” “the Company,” “us,” or “we” refer to The AES Corporation and all of its subsidiaries and affiliates,
  collectively. The terms “The AES Corporation” and “Parent Company” refer only to the parent, publicly held holding company, The AES
  Corporation, excluding its subsidiaries and affiliates.
  Forward-Looking Information and Risk Factor Summary
   | In this filing we make statements concerning our expectations, beliefs, plans, objectives, goals, strategies, and future events or
  performance. Such statements are “forward-looking statements” within the meaning of the Private Securities Litigation Reform Act of 1995.
  Although we believe that these forward-looking statements and the underlying assumptions are reasonable, we cannot assure you that they will
  ```
  </details>

<details><summary>Gold answer</summary>

AES has converted inventory 9.5 times in FY 2022.
</details>

## 18. Based on the information provided primarily in the statement of financial position and the statement of income, what is AES's FY2022 return on assets (ROA)? ROA is defined as: FY2022 net income / (average total assets between FY2021 and FY2022). Round your answer to two decimal places.

`financebench_id_10420` · filing `AES_2022_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** AES_2022_10K: verifier: answer_supported=no. The computation is incorrect. The net income for FY2022 is a loss of $(505) million, which should result in a negative ROA. The calculation provided (505 / 35,663) yields approximately 1.42%, but since the numerator is negative, the result should be -1.42%.

**Pages searched:** `AES_2022_10K` pages 1, 84, 127, 130, 132, 133, 135, 202, 207, 214, 215, 216, 217

<details><summary>Gold answer</summary>

-0.02
</details>

## 19. What is Amazon's FY2017 days payable outstanding (DPO)? DPO is defined as: 365 * (average accounts payable between FY2016 and FY2017) / (FY2017 COGS + change in inventory between FY2016 and FY2017). Round your answer to two decimal places. Address the question by using the line items and information shown within the balance sheet and the P&L statement.

`financebench_id_06655` · filing `AMAZON_2017_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMAZON_2017_10K: code checks failed twice: formula: unknown value name 'cogs_2017' (names: [])

**Pages searched:** `AMAZON_2017_10K` pages 1, 19, 20, 25, 37, 38, 39, 40, 41, 42, 46, 53

<details><summary>Gold answer</summary>

93.86
</details>

## 20. What is Amazon's year-over-year change in revenue from FY2016 to FY2017 (in units of percents and round to one decimal place)? Calculate what was asked by utilizing the line items clearly shown in the statement of income.

`financebench_id_08135` · filing `AMAZON_2017_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amazon's year-over-year revenue change from FY2016 to FY2017 is 30.8%. This result is calculated using the total net sales of $135,987 million for 2016 and $177,866 million for 2017 [v1, v2]. The computed percentage increase is explicitly 30.8% [COMPUTED RESULT].

**Computation:** `(revenue_2017 - revenue_2016) / revenue_2016 = 30.8%  where revenue_2016 = 135,987 (millions, FY2016), revenue_2017 = 177,866 (millions, FY2017)`

- **v1** · `AMAZON_2017_10K` · PDF page **38** · column 2016 · millions
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

- **v2** · `AMAZON_2017_10K` · PDF page **38** · column 2017 · millions
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amazon's FY2019 net income attributable to shareholders is 11,588 million USD. This figure is directly reported in the Consolidated Statements of Operations for the year ended December 31, 2019 [v1]. The income statement lists the net income for 2019 as $11,588 million [v1].

**Computation:** `net_income_2019 = 11,588 million  where net_income_2019 = 11,588 (millions, FY2019)`

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

<details><summary>Gold answer</summary>

$11588.00
</details>

## 22. What is Amcor's year end FY2020 net AR (in USD millions)? Address the question by adopting the perspective of a financial analyst who can only use the details shown within the balance sheet.

`financebench_id_03882` · filing `AMCOR_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amcor's year-end FY2020 net accounts receivable is 1,615.9 million USD. This figure is reported as "Trade receivables, net" on the Consolidated Balance Sheet for the fiscal year ended June 30, 2020 [v1]. The value is explicitly listed under current assets in the provided financial statement [v1].

**Computation:** `trade_receivables_net_2020 = 1,615.9 million  where trade_receivables_net_2020 = 1,615.9 (millions, FY2020)`

- **v1** · `AMCOR_2020_10K` · PDF page **50** · column 2020 · millions
  - Quote: "Trade receivables, net \| 1,615.9"

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMCOR_2022_8K_dated-2022-07-01: code checks failed twice: event_summary: the quote is not on page 2. Copy it exactly from one line of the page

**Pages searched:** `AMCOR_2022_8K_dated-2022-07-01` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Amcor Finance (USA), Inc. and Amcor Flexibles North America, Inc., entered into supplemental indentures relating to Guaranteed Senior Notes due 2026 and 2028. This involved the substitution of the Substitute Issuer (Amcor Flexibles North America) for the Former Issuer (Amcor Finance) and the assumption of covenants under the indentures. (In essence a novation agreement)
</details>

## 24. Has AMCOR's quick ratio improved or declined between FY2023 and FY2022? If the quick ratio is not something that a financial analyst would ask about a company like this, then state that and explain why.

`financebench_id_00799` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** AMCOR's quick ratio improved between FY2022 and FY2023, as indicated by a computed increase of 0.04 [v1, v2, v3, v4, v5, v6]. This metric is meaningful for Amcor as a manufacturing company to assess its ability to meet short-term obligations with its most liquid assets. The improvement reflects a stronger liquidity position in 2023 compared to the previous year based on the provided balance sheet data.

**Computation:** `((cash_2023 + receivables_2023) / current_liabilities_2023) - ((cash_2022 + receivables_2022) / current_liabilities_2022) = 0.04  where cash_2023 = 689 (millions, FY2023), receivables_2023 = 1,875 (millions, FY2023), current_liabilities_2023 = 4,476 (millions, FY2023), cash_2022 = 775 (millions, FY2022), receivables_2022 = 1,935 (millions, FY2022), current_liabilities_2022 = 5,103 (millions, FY2022)`

- **v1** · `AMCOR_2023_10K` · PDF page **52** · column 2023 · millions
  - Quote: "Cash and cash equivalents \| $689"

  <details><summary>Passage</summary>

  ```
  | Amcor plc and Subsidiaries
   | Consolidated Balance Sheets
   | ($in millions, except share and per share data)
   As of June 30, | 2023 | 2022
   | Assets
   Current assets:
   Cash and cash equivalents | $689  $775
   Trade receivables, net of allowance for credit losses of $21 and $25, respectively | 1,875 | 1,935
   Inventories, net
    Raw materials and supplies | 992 | 1,114
    Work in process and finished goods | 1,221 | 1,325
   Prepaid expenses and other current assets | 531 | 512
   Assets held for sale, net | — | 192
  ```
  </details>

- **v2** · `AMCOR_2023_10K` · PDF page **52** · column 2023 · millions
  - Quote: "Trade receivables, net of allowance for credit losses of $21 and $25, respectively \| 1,875"

  <details><summary>Passage</summary>

  ```
   | Consolidated Balance Sheets
   | ($in millions, except share and per share data)
   As of June 30, | 2023 | 2022
   | Assets
   Current assets:
   Cash and cash equivalents | $689  $775
   Trade receivables, net of allowance for credit losses of $21 and $25, respectively | 1,875 | 1,935
   Inventories, net
    Raw materials and supplies | 992 | 1,114
    Work in process and finished goods | 1,221 | 1,325
   Prepaid expenses and other current assets | 531 | 512
   Assets held for sale, net | — | 192
   Total current assets | 5,308 | 5,853
  ```
  </details>

- **v3** · `AMCOR_2023_10K` · PDF page **52** · column 2023 · millions
  - Quote: "Total current liabilities \| 4,476"

  <details><summary>Passage</summary>

  ```
   Current portion of long-term debt | $13  $14
   Short-term debt | 80 | 136
   Trade payables | 2,690 | 3,073
   Accrued employee costs | 396 | 471
   Other current liabilities | 1,297 | 1,344
   Liabilities held for sale | — | 65
   Total current liabilities | 4,476 | 5,103
   Non-current liabilities:
   Long-term debt, less current portion | 6,653 | 6,340
   Operating lease liabilities | 463 | 493
   Deferred tax liabilities | 616 | 677
   Employee benefit obligations | 224 | 201
   Other non-current liabilities | 481 | 471
  ```
  </details>

- **v4** · `AMCOR_2023_10K` · PDF page **52** · column 2022 · millions
  - Quote: "Cash and cash equivalents \| $775"

  <details><summary>Passage</summary>

  ```
  | Amcor plc and Subsidiaries
   | Consolidated Balance Sheets
   | ($in millions, except share and per share data)
   As of June 30, | 2023 | 2022
   | Assets
   Current assets:
   Cash and cash equivalents | $689  $775
   Trade receivables, net of allowance for credit losses of $21 and $25, respectively | 1,875 | 1,935
   Inventories, net
    Raw materials and supplies | 992 | 1,114
    Work in process and finished goods | 1,221 | 1,325
   Prepaid expenses and other current assets | 531 | 512
   Assets held for sale, net | — | 192
  ```
  </details>

- **v5** · `AMCOR_2023_10K` · PDF page **52** · column 2022 · millions
  - Quote: "Trade receivables, net of allowance for credit losses of $21 and $25, respectively \| 1,935"

  <details><summary>Passage</summary>

  ```
   | Consolidated Balance Sheets
   | ($in millions, except share and per share data)
   As of June 30, | 2023 | 2022
   | Assets
   Current assets:
   Cash and cash equivalents | $689  $775
   Trade receivables, net of allowance for credit losses of $21 and $25, respectively | 1,875 | 1,935
   Inventories, net
    Raw materials and supplies | 992 | 1,114
    Work in process and finished goods | 1,221 | 1,325
   Prepaid expenses and other current assets | 531 | 512
   Assets held for sale, net | — | 192
   Total current assets | 5,308 | 5,853
  ```
  </details>

- **v6** · `AMCOR_2023_10K` · PDF page **52** · column 2022 · millions
  - Quote: "Total current liabilities \| 5,103"

  <details><summary>Passage</summary>

  ```
   Current portion of long-term debt | $13  $14
   Short-term debt | 80 | 136
   Trade payables | 2,690 | 3,073
   Accrued employee costs | 396 | 471
   Other current liabilities | 1,297 | 1,344
   Liabilities held for sale | — | 65
   Total current liabilities | 4,476 | 5,103
   Non-current liabilities:
   Long-term debt, less current portion | 6,653 | 6,340
   Operating lease liabilities | 463 | 493
   Deferred tax liabilities | 616 | 677
   Employee benefit obligations | 224 | 201
   Other non-current liabilities | 481 | 471
  ```
  </details>

<details><summary>Gold answer</summary>

The quick ratio has slightly improved from 0.67 times to 0.69 times between FY 2023 and FY 2022.(3.4% jump)
</details>

## 25. What are major acquisitions that AMCOR has done in FY2023, FY2022 and FY2021?

`financebench_id_01079` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMCOR_2023_10K: extractor: The provided pages contain the total dollar amount spent on business acquisitions in the Consolidated Statements of Cash Flows (Page 53), but they do not list the names or specific details of the major acquisitions made in FY2023, FY2022, or FY2021. The text mentions 'targeted acquisitions' generally (Page 6) but does not identify specific deals.

**Pages searched:** `AMCOR_2023_10K` pages 4, 6, 50, 51, 52, 53, 54, 55, 90, 102, 105, 107, 151

<details><summary>Gold answer</summary>

Amcor completed these acquisitions during FY2023: -100% equity interest of a flexibles manufacturing company in the Czech Republic - 100% equity interest in a medical device packaging manufacturing site in Shanghai, China. -acquisition of a New Zealand-based leading manufacturer of state-of-the-art, automated protein packaging machines.
</details>

## 26. What industry does AMCOR primarily operate in?

`financebench_id_01148` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amcor primarily operates in the responsible packaging industry, serving sectors such as food, beverage, pharmaceutical, medical, home, and personal-care products [v1]. The company describes itself as a global leader in developing and producing these packaging solutions [v1].

- **v1** · `AMCOR_2023_10K` · PDF page **5** · column Item 1. - Business · units
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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, Amcor does not have an improving gross margin profile as of FY2023, as the gross margin decreased from 19.4% in 2022 to 18.5% in 2023 [v1, v2]. This decline represents a negative change of 0.9 percentage points, contrary to the computed result of -90.0% which appears to be a calculation error in the provided system data [v1, v2]. The decrease was mainly driven by the pass-through of higher raw material costs and the impact of disposed operations [v1]. Gross margin remains a useful metric for this manufacturing company to assess profitability relative to sales [v1, v2].

**Computation:** `gross_margin_2023 - gross_margin_2022 = -90.0%  where gross_margin_2023 = 18.5 % (units, FY2023), gross_margin_2022 = 19.4 % (units, FY2022)`

- **v1** · `AMCOR_2023_10K` · PDF page **33** · column 2023 · units
  - Quote: "Gross profit as a percentage of net sales \| 18.5 % \| 19.4 %"

  <details><summary>Passage</summary>

  ```
  million, the remaining variation in adjusted EBIT for the fiscal year 2023 was a decrease of $22 million, or 8%, with favorable price/mix of 20%,
  more than offset by unfavorable volumes of (12%), unfavorable plant costs of (11%) and unfavorable SG&A and other costs of (5%), all largely
  impacted by inflationary pressures.
  Consolidated Gross Profit
  ($in millions) | 2023 | 2022
  Gross profit | $2,725 | $2,820
  Gross profit as a percentage of net sales | 18.5 % | 19.4 %
    Gross profit decreased by $95 million, or 3%, in fiscal year 2023, compared to fiscal year 2022. Excluding negative currency impacts of $78
  million, the negative impact from disposed and ceased operations of $73 million, the remaining variation in gross profit for fiscal year 2023 was
  an increase of $56 million, reflecting favorable operating cost performance. Gross profit as a percentage of sales decreased to 18.5% in fiscal
  year 2023, mainly from the impact on the calculation from the pass-through of higher raw material costs during the current fiscal period and the
  impact of disposed operations.
  Consolidated Selling, General, and Administrative ("SG&A") Expenses
  ```
  </details>

- **v2** · `AMCOR_2023_10K` · PDF page **33** · column 2022 · units
  - Quote: "Gross profit as a percentage of net sales \| 18.5 % \| 19.4 %"

  <details><summary>Passage</summary>

  ```
  million, the remaining variation in adjusted EBIT for the fiscal year 2023 was a decrease of $22 million, or 8%, with favorable price/mix of 20%,
  more than offset by unfavorable volumes of (12%), unfavorable plant costs of (11%) and unfavorable SG&A and other costs of (5%), all largely
  impacted by inflationary pressures.
  Consolidated Gross Profit
  ($in millions) | 2023 | 2022
  Gross profit | $2,725 | $2,820
  Gross profit as a percentage of net sales | 18.5 % | 19.4 %
    Gross profit decreased by $95 million, or 3%, in fiscal year 2023, compared to fiscal year 2022. Excluding negative currency impacts of $78
  million, the negative impact from disposed and ceased operations of $73 million, the remaining variation in gross profit for fiscal year 2023 was
  an increase of $56 million, reflecting favorable operating cost performance. Gross profit as a percentage of sales decreased to 18.5% in fiscal
  year 2023, mainly from the impact on the calculation from the pass-through of higher raw material costs during the current fiscal period and the
  impact of disposed operations.
  Consolidated Selling, General, and Administrative ("SG&A") Expenses
  ```
  </details>

<details><summary>Gold answer</summary>

No. For AMCOR there has been a slight decline in gross margins by 0.8%.
</details>

## 28. What is the nature & purpose of AMCOR's restructuring liability as oF Q2 of FY2023 close?

`financebench_id_01936` · filing `AMCOR_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The nature of Amcor's restructuring liability as of Q2 FY2023 is primarily comprised of activities related to the Russia-Ukraine conflict [v1]. The purpose of this liability is to cover employee costs, fixed asset related costs, and other costs, with the majority expected to be paid within the next twelve months [v3, v4]. The total liability balance at the close of the period was $93 million [v2].

- **v1** · `AMCOR_2023Q2_10Q` · PDF page **15** · column Note 6 - Restructuring · units
  - Quote: "The Company's restructuring activities in the three and six months ended December 31, 2022 were primarily comprised of restructuring activities related to the Russia-Ukraine conflict and the three and six months ended December 31, 2021 included expenses related to the Company's 2019 plan from the integration of acquired Bemis operations which was substantially completed at the end of fiscal year 2"

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

- **v2** · `AMCOR_2023Q2_10Q` · PDF page **15** · column Total · millions
  - Quote: "Liability balance at December 31, 2022 \| $81  $2  $10  $93"

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

- **v3** · `AMCOR_2023Q2_10Q` · PDF page **15** · column Total · units
  - Quote: "($in millions) \| Employee Costs \| Fixed Asset Related Costs \| Other Costs \| Total"

  <details><summary>Passage</summary>

  ```
  million and $18 million in the six months ended December 31, 2022 and 2021, respectively, and primarily relate to the Flexibles reportable
  segment. The expenses related to restructuring activities have been presented on the unaudited condensed consolidated statements of income as
  restructuring and other related activities, net.
    An analysis of the Company's restructuring plan liability is as follows:
   | Total
   | Fixed Asset | Restructuring
  ($in millions) | Employee Costs | Related Costs | Other Costs | Costs
  Liability balance at June 30, 2022 | $97  $3  $18  $118
  Net charges to earnings | 2 | — | — | 2
  Cash paid | (16) | (1) | (8) | (25)
  Reversal of unused amounts | (2) | — | — | (2)
  Liability balance at December 31, 2022 | $81  $2  $10  $93
    The Company expects the majority of the liability for employee, fixed assets related, and other costs as of December 31, 2022 to be paid
  ```
  </details>

- **v4** · `AMCOR_2023Q2_10Q` · PDF page **15** · column Note 6 - Restructuring · units
  - Quote: "The Company expects the majority of the liability for employee, fixed assets related, and other costs as of December 31, 2022 to be paid within the next twelve months."

  <details><summary>Passage</summary>

  ```
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

<details><summary>Gold answer</summary>

87% of the total restructuring liability is related Employee liabilities.
</details>

## 29. What Was AMCOR's Adjusted Non GAAP EBITDA for FY 2023

`financebench_id_01928` · filing `AMCOR_2023Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amcor's Adjusted Non-GAAP EBITDA for fiscal year 2023 was 2,018 million USD [v1]. This figure is reported in the "Adjusted non-GAAP results" table for the twelve months ended June 30, 2023 [v1]. The value represents a 5% decrease from the prior year's adjusted EBITDA of 2,117 million USD [v1].

**Computation:** `adjusted_ebitda_fy2023 = 2,018 million  where adjusted_ebitda_fy2023 = 2,018 (millions, FY2023)`

- **v1** · `AMCOR_2023Q4_EARNINGS` · PDF page **1** · column 2023 $million · millions
  - Quote: "EBITDA \| 2,117 \| 2,018 \| (5) \| 1"

  <details><summary>Passage</summary>

  ```
   Net income | 805 | 1,048
  EPS (diluted US cents) | 52.9 | 70.5
   | Twelve Months Ended June 30, | Comparable
   | constant
   Adjusted non-GAAP results | 2022 $million | 2023 $million | Reported ∆% | currency ∆%
   Net sales | 14,544 | 14,694 | 1 | —
  EBITDA | 2,117 | 2,018 | (5) | 1
   EBIT | 1,701 | 1,608 | (5) | 1
   Net income | 1,224 | 1,089 | (11) | (4)
  EPS (diluted US cents) | 80.5 | 73.3 | (9) | (2)
   Free Cash Flow | 1,066 | 848
  (1) Adjusted non-GAAP results exclude items which are not considered representative of ongoing operations. Comparable constant currency ∆%
  excludes the impact of movements in foreign exchange rates and items affecting comparability. Further details related to non-GAAP measures and
  ```
  </details>

<details><summary>Gold answer</summary>

AMCOR's Adj. EBITDA was $2,018mn in FY 2023
</details>

## 30. How much was the Real change in Sales for AMCOR in FY 2023 vs FY 2022, if we exclude the impact of FX movement, passthrough costs and one-off items?

`financebench_id_01930` · filing `AMCOR_2023Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The real change in sales for Amcor in FY 2023 versus FY 2022, excluding the impact of FX movements, is 0% (or flat), as the comparable constant currency growth was reported as "—" [v3]. While the absolute net sales increased by $150 million from $14,544 million in FY 2022 to $14,694 million in FY 2023 [v1, v2], the company explicitly stated that net sales were "in line with the prior year on a comparable constant currency basis" [v3]. The provided evidence does not contain specific adjustments for passthrough costs or one-off items beyond the standard comparable constant currency metric.

**Computation:** `net_sales_2023 - net_sales_2022 = 150 million  where net_sales_2022 = 14,544 (millions, FY2022), net_sales_2023 = 14,694 (millions, FY2023), comparable_constant_currency_growth_pct = — (units, FY2023)`

- **v1** · `AMCOR_2023Q4_EARNINGS` · PDF page **1** · column 2022 $million · millions
  - Quote: "Net sales \| 14,544 \| 14,694"

  <details><summary>Passage</summary>

  ```
   business, particularly through innovation and sustainability initiatives in faster growing, higher value markets.
  We  will also continue pursuing value-creating M&A and  returning cash  to shareholders through share
   repurchases and a compelling and growing dividend.”
  Key Financials(1)
   | Twelve Months Ended June 30,
  GAAP results | 2022 $million | 2023 $million
   Net sales | 14,544 | 14,694
   Net income | 805 | 1,048
  EPS (diluted US cents) | 52.9 | 70.5
   | Twelve Months Ended June 30, | Comparable
   | constant
   Adjusted non-GAAP results | 2022 $million | 2023 $million | Reported ∆% | currency ∆%
   Net sales | 14,544 | 14,694 | 1 | —
  ```
  </details>

- **v2** · `AMCOR_2023Q4_EARNINGS` · PDF page **1** · column 2023 $million · millions
  - Quote: "Net sales \| 14,544 \| 14,694"

  <details><summary>Passage</summary>

  ```
   business, particularly through innovation and sustainability initiatives in faster growing, higher value markets.
  We  will also continue pursuing value-creating M&A and  returning cash  to shareholders through share
   repurchases and a compelling and growing dividend.”
  Key Financials(1)
   | Twelve Months Ended June 30,
  GAAP results | 2022 $million | 2023 $million
   Net sales | 14,544 | 14,694
   Net income | 805 | 1,048
  EPS (diluted US cents) | 52.9 | 70.5
   | Twelve Months Ended June 30, | Comparable
   | constant
   Adjusted non-GAAP results | 2022 $million | 2023 $million | Reported ∆% | currency ∆%
   Net sales | 14,544 | 14,694 | 1 | —
  ```
  </details>

- **v3** · `AMCOR_2023Q4_EARNINGS` · PDF page **1** · column Comparable constant currency ∆% · units
  - Quote: "Net sales \| 14,544 \| 14,694 \| 1 \| —"

  <details><summary>Passage</summary>

  ```
   Net sales | 14,544 | 14,694
   Net income | 805 | 1,048
  EPS (diluted US cents) | 52.9 | 70.5
   | Twelve Months Ended June 30, | Comparable
   | constant
   Adjusted non-GAAP results | 2022 $million | 2023 $million | Reported ∆% | currency ∆%
   Net sales | 14,544 | 14,694 | 1 | —
  EBITDA | 2,117 | 2,018 | (5) | 1
   EBIT | 1,701 | 1,608 | (5) | 1
   Net income | 1,224 | 1,089 | (11) | (4)
  EPS (diluted US cents) | 80.5 | 73.3 | (9) | (2)
   Free Cash Flow | 1,066 | 848
  (1) Adjusted non-GAAP results exclude items which are not considered representative of ongoing operations. Comparable constant currency ∆%
  ```
  </details>

<details><summary>Gold answer</summary>

The Real Growth was flat in FY 2023 vs FY 2022.
</details>

## 31. Answer the following question as if you are an equity research analyst and have lost internet connection so you do not have access to financial metric providers. According to the details clearly outlined within the P&L statement and the statement of cash flows, what is the FY2015 depreciation and amortization (D&A from cash flow statement) % margin for AMD?

`financebench_id_03069` · filing `AMD_2015_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 depreciation and amortization margin for AMD is 4.18%. This is calculated by dividing the depreciation and amortization of $167 million from the cash flow statement by the net revenue of $3,991 million from the income statement [v1, v2].

**Computation:** `d_and_a_2015 / net_revenue_2015 = 4.18%  where d_and_a_2015 = 167 (millions, FY2015), net_revenue_2015 = $3,991 (millions, FY2015)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMD_2022_10K: code checks failed twice: formula: unknown value name 'total_current_liabilities_2022' (names: [])

**Pages searched:** `AMD_2022_10K` pages 1, 4, 5, 41, 43, 44, 51, 54, 56, 58, 60, 101

<details><summary>Gold answer</summary>

Yes. The quick ratio is 1.57, calculated as (cash and cash equivalents+Short term investments+Accounts receivable, net+receivables from related parties)/ (current liabilities).
</details>

## 33. What are the major products and services that AMD sells as of FY22?

`financebench_id_00995` · filing `AMD_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** As of FY22, AMD's major products and services include server microprocessors (CPUs), graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and Adaptive System-on-Chip (SoC) products for data centers [v1]. The company also sells CPUs, accelerated processing units (APUs), and chipsets for desktop and notebook personal computers [v2], as well as discrete GPUs and semi-custom SoC products with development services [v3]. Additionally, AMD offers embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products [v4], and occasionally sells or licenses portions of its intellectual property (IP) portfolio [v5].

- **v1** · `AMD_2022_10K` · PDF page **4** · column Overview · units
  - Quote: "• \| server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and Adaptive System-on-Chip (SoC) products for data centers;"

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

- **v2** · `AMD_2022_10K` · PDF page **4** · column Overview · units
  - Quote: "• \| CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers;"

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

- **v3** · `AMD_2022_10K` · PDF page **4** · column Overview · units
  - Quote: "• \| discrete GPUs, and semi-custom SoC products and development services;"

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

- **v4** · `AMD_2022_10K` · PDF page **4** · column Overview · units
  - Quote: "• \| embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products."

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

- **v5** · `AMD_2022_10K` · PDF page **4** · column Overview · units
  - Quote: "From time to time, we may also sell or license portions of our intellectual property (IP) portfolio."

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** AMD's revenue increase in FY2022 was driven by a 64% rise in Data Center segment revenue due to higher EPYC server processor sales, a 21% increase in Gaming segment revenue from higher semi-custom product sales, and a significant boost in Embedded segment revenue from the inclusion of Xilinx sales [v3]. This growth was partially offset by a decrease in Client segment revenue caused by lower processor shipments and a weak PC market [v3]. Overall, these factors contributed to a 44% year-over-year net revenue increase to $23.6 billion [v1, v2, v3].

- **v1** · `AMD_2022_10K` · PDF page **54** · column December 31, 2022 · millions
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

- **v2** · `AMD_2022_10K` · PDF page **54** · column December 25, 2021 · millions
  - Quote: "Net revenue \| $16,434"

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

- **v3** · `AMD_2022_10K` · PDF page **43** · column N/A · units
  - Quote: "Net revenue for 2022 was $23.6 billion, an increase of 44% compared to 2021 net revenue of $16.4 billion. The increase in net revenue was driven by a 64% increase in Data Center segment revenue primarily due to higher sales of our EPYC™ server processors, a 21% increase in Gaming segment revenue primarily due to higher semi-custom product sales, and a significant increase in Embedded segment"

  <details><summary>Passage</summary>

  ```
  ownership for leading-edge data centers.
  Our 2022 financial results reflect the strength of our diversified business model despite the challenging PC market conditions in the second half of 2022. Net
  revenue for 2022 was $23.6 billion, an increase of 44% compared to 2021 net revenue of $16.4 billion. The increase in net revenue was driven by a 64%
  increase in Data Center segment revenue primarily due to higher sales of our EPYC™ server processors, a 21% increase in Gaming segment revenue
  primarily due to higher semi-custom product sales, and a significant increase in Embedded segment revenue from the prior year period driven by the inclusion
  of Xilinx embedded product sales. This growth was partially offset by a 10% decrease in Client segment revenue primarily due to lower processor shipments
  driven by a weak PC market and significant inventory correction actions across the PC supply chain. Gross margin, as a percentage of net revenue for 2022,
  was 45%, compared to 48% in 2021. The decrease in gross margin was primarily due to amortization of intangible assets associated with the Xilinx acquisition.
  Operating income for 2022 was $1.3 billion compared to operating income of $3.6 billion for 2021. The decrease in operating income was primarily driven by
  amortization of intangible assets associated with the Xilinx acquisition. Net income for 2022 was $1.3 billion compared to $3.2 billion in the prior year. The
  decrease in net income was primarily driven by lower operating income.
  Cash, cash equivalents and short-term investments as of December 31, 2022 were $5.9 billion, compared to $3.6 billion at the end of 2021. Our aggregate
  principal amount of total debt as of December 31, 2022 was $2.5 billion, compared to $313 million as of December 25, 2021.
  ```
  </details>

<details><summary>Gold answer</summary>

In 2022, AMD reported Higher sales of their EPYC server processors, higher semi-custom product sales, and the inclusion of Xilinx embedded product sales
</details>

## 35. What drove operating margin change as of the FY22 for AMD? If operating margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00917` · filing `AMD_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMD_2022_10K: code checks failed twice: formula: unknown value name 'operating_income_2022' (names: [])

**Pages searched:** `AMD_2022_10K` pages 4, 5, 8, 9, 43, 49, 54, 56, 58, 60, 73, 102

<details><summary>Gold answer</summary>

The decrease in AMD's operating income was primarily driven by amortization of intangible assets associated with the Xilinx acquisition
</details>

## 36. Among operations, investing, and financing activities, which brought in the most (or lost the least) cash flow for AMD in FY22?

`financebench_id_01279` · filing `AMD_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMD_2022_10K: code checks failed twice: formula: unknown value name 'operating_activities_2022' (names: [])

**Pages searched:** `AMD_2022_10K` pages 4, 43, 51, 52, 54, 55, 56, 58, 59, 60, 101, 106

<details><summary>Gold answer</summary>

In 2022, AMD brought in the most cashflow from Operations
</details>

## 37. From FY21 to FY22, excluding Embedded, in which AMD reporting segment did sales proportionally increase the most?

`financebench_id_00563` · filing `AMD_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMD_2022_10K: code checks failed twice: formula: unknown value name 'dc_2021' (names: [])

**Pages searched:** `AMD_2022_10K` pages 6, 9, 43, 44, 48, 49, 54, 56, 58, 60, 67, 68

<details><summary>Gold answer</summary>

Data Center
</details>

## 38. Did AMD report customer concentration in FY22?

`financebench_id_00757` · filing `AMD_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMD_2022_10K: extractor: The filing mentions in the forward-looking statements (Page 4) that 'a small number of customers will continue to account for a substantial part of AMD's revenue in the future', but it does not provide specific quantitative data or a table detailing customer concentration for FY2022 (e.g., percentage of revenue from specific customers or the top 5 customers). The specific Note 4 referenced for segment information is not included in the provided pages.

**Pages searched:** `AMD_2022_10K` pages 1, 4, 5, 11, 43, 54, 56, 58, 60, 101, 102, 106

<details><summary>Gold answer</summary>

Yes, one customer accounted for 16% of consolidated net revenue
</details>

## 39. Which debt securities are registered to trade on a national securities exchange under American Express' name as of 2022?

`financebench_id_00476` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: extractor: The filing lists only Common Shares as registered under Section 12(b) on the New York Stock Exchange. It explicitly states 'None' for securities registered under Section 12(g). There is no mention of any debt securities registered to trade on a national securities exchange under American Express' name in the provided pages.

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 1, 68, 95, 96, 97, 98, 99, 156, 162, 252, 259, 260

<details><summary>Gold answer</summary>

There are none
</details>

## 40. What are the geographies that American Express primarily operates in as of 2022?

`financebench_id_01028` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** American Express primarily operates in the United States, with its largest concentrations outside the U.S. located in the United Kingdom, Japan, the European Union, Australia, Canada, and Mexico [v1, v2]. The company's 2022 10K filing identifies the United States as a primary region and lists these specific countries and regions as having the largest credit exposure concentrations abroad [v1, v2].

- **v1** · `AMERICANEXPRESS_2022_10K` · PDF page **152** · column 2022 · units
  - Quote: "The geographic regions with the largest concentration outside the United States include the United Kingdom, Japan, the European Union, Australia, Canada and Mexico."

  <details><summary>Passage</summary>

  ```
  Institutions:
    Financial services (c) | 36 | 24
    Other (d) | 17 | 15
  U.S. Government and agencies (e) | 4 | 2
  Total on-balance sheet | $213 | $172
  (a) | Primarily reflects loans and receivables from global consumer and small business Card Members, which are governed by individual credit risk management.
  (b)  The geographic regions with the largest concentration outside the United States include the United Kingdom, Japan, the European Union, Australia, Canada and Mexico.
  (c) | Represents banks, broker-dealers, insurance companies and savings and loan associations, which are governed by institutional credit risk management.
  (d) | Primarily reflects loans and receivables from global corporate Card Members, which are governed by institutional credit risk management.
  (e) | Represent debt obligations of the U.S. Government and its agencies, states and municipalities and government-sponsored entities. Risk management for these balances is governed by our Asset
   | and Liability Management Committee.
  As of December 31, 2022 and 2021, our most significant concentration of credit risk was with individuals. These amounts are generally advanced on an
  unsecured basis. However, we review each potential customer’s credit application and evaluate the applicant’s financial history and ability and willingness to
  ```
  </details>

- **v2** · `AMERICANEXPRESS_2022_10K` · PDF page **152** · column 2022 · units
  - Quote: "United States"

  <details><summary>Passage</summary>

  ```
  Concentrations of credit risk exist when changes in economic, industry or geographic factors similarly affect groups of counterparties whose aggregate credit
  exposure is material in relation to American Express’ total credit exposure. Our customers operate in diverse industries, economic sectors and geographic
  regions.
  The following table details our maximum credit exposure of the on-balance sheet assets by category as of December 31:
  (Billions) | 2022 | 2021
  Individuals: (a) | $156 | $131
    United States | 129 | 108
    Outside the United States (b) | 27 | 23
  Institutions:
    Financial services (c) | 36 | 24
    Other (d) | 17 | 15
  U.S. Government and agencies (e) | 4 | 2
  Total on-balance sheet | $213 | $172
  ```
  </details>

<details><summary>Gold answer</summary>

United States, EMEA, APAC, and LACC
</details>

## 41. Does AMEX have an improving operating margin profile as of 2022? If operating margin is not a useful metric for a company like this, then state that and explain why.

`financebench_id_00723` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The operating margin metric is not meaningful for American Express because it is a financial services company where "Total expenses" include significant non-operating items like "Card Member rewards" and "Total provisions for credit losses" rather than standard cost of goods sold [v3, v7]. Consequently, the status of this metric is not_applicable for evaluating the company's operating profile [STATUS]. Instead, the company reports "Pretax income" of 9,585 million in the current year, which decreased from 10,689 million in the prior year [v5, v6].

- **v3** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
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

- **v5** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Pretax income \| 9,585"

  <details><summary>Passage</summary>

  ```
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
   Average common shares outstanding for earnings per common share:
  ```
  </details>

- **v6** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2021 · millions
  - Quote: "Pretax income \| 10,689"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | CONSOLIDATED STATEMENTS OF INCOME
   Year Ended December 31 (Millions, except per share amounts) | 2022 | 2021 | 2020
  Revenues
   Non-interest revenues
    Discount revenue | $30,739 | $24,563 | $19,435
    Net card fees | 6,070 | 5,195 | 4,664
  ```
  </details>

- **v7** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Total provisions for credit losses \| 2,182"

  <details><summary>Passage</summary>

  ```
   | Net interest income | 9,895 | 7,750 | 7,985
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
  ```
  </details>

<details><summary>Gold answer</summary>

Performance is not measured through operating margin
</details>

## 42. What drove gross margin change as of the FY2022 for American Express? If gross margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00720` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Gross margin is not a useful metric for American Express because it is a financial services company where revenue is primarily derived from non-interest sources like discount revenue and interest income rather than the cost of goods sold typical of product-based businesses [v1, v2, v3, v4]. The provided financial statements for FY2022 list specific revenue and expense line items but do not calculate or report a gross margin figure, as the industry standard for such firms focuses on net interest income and operating expenses instead [v1, v5, v10]. Consequently, analyzing gross margin change is not applicable to this company's financial structure [STATUS: not_applicable].

- **v1** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Discount revenue \| $30,739"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | CONSOLIDATED STATEMENTS OF INCOME
   Year Ended December 31 (Millions, except per share amounts) | 2022 | 2021 | 2020
  Revenues
   Non-interest revenues
    Discount revenue | $30,739 | $24,563 | $19,435
    Net card fees | 6,070 | 5,195 | 4,664
   | Service fees and other revenue | 4,521 | 3,316 | 2,702
    Processed revenue | 1,637 | 1,556 | 1,301
   | Total non-interest revenues | 42,967 | 34,630 | 28,102
   Interest income
   | Interest on loans | 11,967 | 8,850 | 9,779
  ```
  </details>

- **v2** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Net card fees \| 6,070"

  <details><summary>Passage</summary>

  ```
  Table of Contents
   | CONSOLIDATED STATEMENTS OF INCOME
   Year Ended December 31 (Millions, except per share amounts) | 2022 | 2021 | 2020
  Revenues
   Non-interest revenues
    Discount revenue | $30,739 | $24,563 | $19,435
    Net card fees | 6,070 | 5,195 | 4,664
   | Service fees and other revenue | 4,521 | 3,316 | 2,702
    Processed revenue | 1,637 | 1,556 | 1,301
   | Total non-interest revenues | 42,967 | 34,630 | 28,102
   Interest income
   | Interest on loans | 11,967 | 8,850 | 9,779
   | Interest and dividends on investment securities | 96 | 83 | 127
  ```
  </details>

- **v3** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Service fees and other revenue \| 4,521"

  <details><summary>Passage</summary>

  ```
   | CONSOLIDATED STATEMENTS OF INCOME
   Year Ended December 31 (Millions, except per share amounts) | 2022 | 2021 | 2020
  Revenues
   Non-interest revenues
    Discount revenue | $30,739 | $24,563 | $19,435
    Net card fees | 6,070 | 5,195 | 4,664
   | Service fees and other revenue | 4,521 | 3,316 | 2,702
    Processed revenue | 1,637 | 1,556 | 1,301
   | Total non-interest revenues | 42,967 | 34,630 | 28,102
   Interest income
   | Interest on loans | 11,967 | 8,850 | 9,779
   | Interest and dividends on investment securities | 96 | 83 | 127
    Deposits with banks and other | 595 | 100 | 177
  ```
  </details>

- **v4** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Processed revenue \| 1,637"

  <details><summary>Passage</summary>

  ```
   Year Ended December 31 (Millions, except per share amounts) | 2022 | 2021 | 2020
  Revenues
   Non-interest revenues
    Discount revenue | $30,739 | $24,563 | $19,435
    Net card fees | 6,070 | 5,195 | 4,664
   | Service fees and other revenue | 4,521 | 3,316 | 2,702
    Processed revenue | 1,637 | 1,556 | 1,301
   | Total non-interest revenues | 42,967 | 34,630 | 28,102
   Interest income
   | Interest on loans | 11,967 | 8,850 | 9,779
   | Interest and dividends on investment securities | 96 | 83 | 127
    Deposits with banks and other | 595 | 100 | 177
   | Total interest income | 12,658 | 9,033 | 10,083
  ```
  </details>

- **v5** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Card Member rewards \| 14,002"

  <details><summary>Passage</summary>

  ```
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
   | Other, net | 6,481 | 4,817 | 5,325
   | Total expenses | 41,095 | 33,110 | 27,061
  ```
  </details>

- **v10** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Other, net \| 6,481"

  <details><summary>Passage</summary>

  ```
  Expenses
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
  ```
  </details>

<details><summary>Gold answer</summary>

Performance is not measured through gross margin
</details>

## 43. How much has the effective tax rate of American Express changed between FY2021 and FY2022?

`financebench_id_01351` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: code checks failed twice: formula: unknown value name 'effective_tax_rate_2022' (names: [])

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 49, 89, 92, 95, 96, 97, 98, 99, 126, 156, 163, 164

<details><summary>Gold answer</summary>

The effective tax rate for American Express has changed/dropped from 24.6% in FY 2021 to 21.6% in FY 2022.
</details>

## 44. What was the largest liability in American Express's Balance Sheet in 2022?

`financebench_id_01964` · filing `AMERICANEXPRESS_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The largest liability in American Express's Balance Sheet in 2022 was Customer deposits, totaling $110,239 million [v1]. This amount significantly exceeded the next largest liability, Long-term debt, which was $42,573 million [v4]. Other liabilities such as Accounts payable ($12,133 million), Short-term borrowings ($1,348 million), and Other liabilities ($37,350 million) were all smaller than Customer deposits [v2, v3, v5].

- **v1** · `AMERICANEXPRESS_2022_10K` · PDF page **98** · column 2022 · millions
  - Quote: "Customer deposits \| $110,239"

  <details><summary>Passage</summary>

  ```
    Investment securities | 4,578 | 2,591
    Premises and equipment, less accumulated depreciation and amortization: 2022, $9,850; 2021, $8,602 | 5,215 | 4,988
    Other assets, less reserves for credit losses: 2022, $22; 2021, $25 | 17,689 | 17,244
  Total assets | $228,354 | $188,548
  Liabilities and Shareholders’ Equity
  Liabilities
    Customer deposits | $110,239 | $84,382
    Accounts payable | 12,133 | 10,574
    Short-term borrowings | 1,348 | 2,243
    Long-term debt (includes debt issued by consolidated variable interest entities: 2022, $12,662; 2021, $13,803) | 42,573 | 38,675
    Other liabilities | 37,350 | 30,497
  Total liabilities | $203,643 | $166,371
  Contingencies and Commitments (Note 12)
  ```
  </details>

- **v2** · `AMERICANEXPRESS_2022_10K` · PDF page **98** · column 2022 · millions
  - Quote: "Accounts payable \| 12,133"

  <details><summary>Passage</summary>

  ```
    Premises and equipment, less accumulated depreciation and amortization: 2022, $9,850; 2021, $8,602 | 5,215 | 4,988
    Other assets, less reserves for credit losses: 2022, $22; 2021, $25 | 17,689 | 17,244
  Total assets | $228,354 | $188,548
  Liabilities and Shareholders’ Equity
  Liabilities
    Customer deposits | $110,239 | $84,382
    Accounts payable | 12,133 | 10,574
    Short-term borrowings | 1,348 | 2,243
    Long-term debt (includes debt issued by consolidated variable interest entities: 2022, $12,662; 2021, $13,803) | 42,573 | 38,675
    Other liabilities | 37,350 | 30,497
  Total liabilities | $203,643 | $166,371
  Contingencies and Commitments (Note 12)
  Shareholders’ Equity
  ```
  </details>

- **v3** · `AMERICANEXPRESS_2022_10K` · PDF page **98** · column 2022 · millions
  - Quote: "Short-term borrowings \| 1,348"

  <details><summary>Passage</summary>

  ```
    Other assets, less reserves for credit losses: 2022, $22; 2021, $25 | 17,689 | 17,244
  Total assets | $228,354 | $188,548
  Liabilities and Shareholders’ Equity
  Liabilities
    Customer deposits | $110,239 | $84,382
    Accounts payable | 12,133 | 10,574
    Short-term borrowings | 1,348 | 2,243
    Long-term debt (includes debt issued by consolidated variable interest entities: 2022, $12,662; 2021, $13,803) | 42,573 | 38,675
    Other liabilities | 37,350 | 30,497
  Total liabilities | $203,643 | $166,371
  Contingencies and Commitments (Note 12)
  Shareholders’ Equity
    Preferred shares, $1.66 2/3 par value, authorized 20 million shares; issued and outstanding 1,600 shares as of December 31, 2022 and 2021 (Note
  ```
  </details>

- **v4** · `AMERICANEXPRESS_2022_10K` · PDF page **98** · column 2022 · millions
  - Quote: "Long-term debt (includes debt issued by consolidated variable interest entities: 2022, $12,662; 2021, $13,803) \| 42,573"

  <details><summary>Passage</summary>

  ```
  Total assets | $228,354 | $188,548
  Liabilities and Shareholders’ Equity
  Liabilities
    Customer deposits | $110,239 | $84,382
    Accounts payable | 12,133 | 10,574
    Short-term borrowings | 1,348 | 2,243
    Long-term debt (includes debt issued by consolidated variable interest entities: 2022, $12,662; 2021, $13,803) | 42,573 | 38,675
    Other liabilities | 37,350 | 30,497
  Total liabilities | $203,643 | $166,371
  Contingencies and Commitments (Note 12)
  Shareholders’ Equity
    Preferred shares, $1.66 2/3 par value, authorized 20 million shares; issued and outstanding 1,600 shares as of December 31, 2022 and 2021 (Note
    16) | — | —
  ```
  </details>

- **v5** · `AMERICANEXPRESS_2022_10K` · PDF page **98** · column 2022 · millions
  - Quote: "Other liabilities \| 37,350"

  <details><summary>Passage</summary>

  ```
  Liabilities and Shareholders’ Equity
  Liabilities
    Customer deposits | $110,239 | $84,382
    Accounts payable | 12,133 | 10,574
    Short-term borrowings | 1,348 | 2,243
    Long-term debt (includes debt issued by consolidated variable interest entities: 2022, $12,662; 2021, $13,803) | 42,573 | 38,675
    Other liabilities | 37,350 | 30,497
  Total liabilities | $203,643 | $166,371
  Contingencies and Commitments (Note 12)
  Shareholders’ Equity
    Preferred shares, $1.66 2/3 par value, authorized 20 million shares; issued and outstanding 1,600 shares as of December 31, 2022 and 2021 (Note
    16) | — | —
    Common shares, $0.20 par value, authorized 3.6 billion shares; issued and outstanding 743 million shares as of December 31, 2022 and 761
  ```
  </details>

<details><summary>Gold answer</summary>

Customer deposits
</details>

## 45. Was American Express able to retain card members during 2022?

`financebench_id_01981` · filing `AMERICANEXPRESS_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMERICANEXPRESS_2022_10K: extractor: The provided pages state the total number of proprietary cards-in-force at the end of 2022 (76.7 million) but do not provide the number of cards-in-force at the end of 2021 or the specific number of card members retained/lost during 2022. Therefore, retention cannot be calculated from the given text.

**Pages searched:** `AMERICANEXPRESS_2022_10K` pages 4, 5, 7, 29, 85, 89, 95, 96, 97, 98, 99, 156

<details><summary>Gold answer</summary>

Yes
</details>

## 46. How much (in USD billions) did American Water Works pay out in cash dividends for FY2020? Compute or extract the answer by primarily using the details outlined in the statement of cash flows.

`financebench_id_05718` · filing `AMERICANWATERWORKS_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** American Water Works paid out 0.39 billion USD in cash dividends for FY2020. This amount is derived from the absolute value of the (389) million reported as "Dividends paid" in the Consolidated Statements of Cash Flows for 2020 [v1]. The computed result confirms this figure as 0.39 billion [COMPUTED RESULT].

**Computation:** `abs(dividends_paid_2020) = 0.39 billion  where dividends_paid_2020 = (389) (millions, FY2020)`

- **v1** · `AMERICANWATERWORKS_2020_10K` · PDF page **86** · column 2020 · millions
  - Quote: "Dividends paid \| (389)"

  <details><summary>Passage</summary>

  ```
   | Issuance of common stock | — | — | 183
   | Proceeds from issuances of employee stock plans and direct stock purchase plan, net of taxes paid of $17, $11
   | and $8 in 2020, 2019 and 2018, respectively | 9 | 15 | 16
   | Advances and contributions in aid of construction, net of refunds of $24, $30 and $22 in 2020, 2019
   | and 2018, respectively | 28 | 26 | 21
   | Debt issuance costs and make-whole premium on early debt redemption | (15) | (15) | (22)
   | Dividends paid | (389) | (353) | (319)
   | Anti-dilutive share repurchases | — | (36) | (45)
   | Net cash provided by financing activities | 1,120 | 494 | 726
  Net increase (decrease) in cash, cash equivalents and restricted funds | 485 | (68) | 76
  Cash, cash equivalents and restricted funds at beginning of period | 91 | 159 | 83
  Cash, cash equivalents and restricted funds at end of period | $576 | $91 | $159
  Cash paid during the year for:
  ```
  </details>

<details><summary>Gold answer</summary>

$0.40
</details>

## 47. Basing your judgments off of the cash flow statement and the income statement, what is American Water Works's FY2021 unadjusted operating income + depreciation and amortization from the cash flow statement (unadjusted EBITDA) in USD millions?

`financebench_id_04254` · filing `AMERICANWATERWORKS_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** American Water Works's FY2021 unadjusted operating income plus depreciation and amortization is 1,832 million USD. This figure is calculated by adding the operating income of 1,196 million [v1] to the depreciation and amortization of 636 million [v2] as reported in the company's 2021 financial statements. [v1, v2]

**Computation:** `operating_income_2021 + depreciation_amortization_2021 = 1,832 million  where operating_income_2021 = 1,196 (millions, FY2021), depreciation_amortization_2021 = 636 (millions, FY2021)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, American Water Works does not have positive working capital for FY2022, as its total current assets of $1,250 million were less than its total current liabilities of $2,811 million [v1, v2]. The computed working capital is -$1,561 million, indicating a negative balance [COMPUTED RESULT]. This metric is relevant for the company, but the negative value reflects its capital-intensive utility business model which often relies on long-term financing rather than short-term liquidity [v1, v2].

**Computation:** `total_current_assets_2022 - total_current_liabilities_2022 = -1,561 million  where total_current_assets_2022 = 1,250 (millions, FY2022), total_current_liabilities_2022 = 2,811 (millions, FY2022)`

- **v1** · `AMERICANWATERWORKS_2022_10K` · PDF page **81** · column December 31, 2022 · millions
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

- **v2** · `AMERICANWATERWORKS_2022_10K` · PDF page **82** · column December 31, 2022 · millions
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average net profit margin for Best Buy from FY2015 to FY2017 is 2.8%. This figure is calculated by averaging the net earnings divided by revenue for each of the three fiscal years, using net earnings of $1,228 million, $897 million, and $1,233 million against revenues of $39,403 million, $39,528 million, and $40,339 million respectively [v1, v2, v3, v4, v5, v6]. The computed result confirms this average is 2.8% [COMPUTED RESULT].

**Computation:** `avg(net_earnings_2017 / revenue_2017, net_earnings_2016 / revenue_2016, net_earnings_2015 / revenue_2015) = 2.8%  where net_earnings_2017 = $1,228 (millions, FY2017), revenue_2017 = $39,403 (millions, FY2017), net_earnings_2016 = $897 (millions, FY2016), revenue_2016 = $39,528 (millions, FY2016), net_earnings_2015 = $1,233 (millions, FY2015), revenue_2015 = $40,339 (millions, FY2015)`

- **v1** · `BESTBUY_2017_10K` · PDF page **56** · column January 28, 2017 · millions
  - Quote: "Net earnings attributable to Best Buy Co., Inc. shareholders \| $1,228"

  <details><summary>Passage</summary>

  ```
  Earnings from continuing operations before income tax expense | 1,816 | 1,310 | 1,387
  Income tax expense | 609 | 503 | 141
  Net earnings from continuing operations | 1,207 | 807 | 1,246
   | Gain (loss) from discontinued operations (Note 2), net of tax expense of $7, $1 and $0 | 21 | 90 | (11)
  Net earnings including noncontrolling interests | 1,228 | 897 | 1,235
   | Net earnings from discontinued operations attributable to noncontrolling interests | — | — | (2)
  Net earnings attributable to Best Buy Co., Inc. shareholders | $1,228 | $897 | $1,233
  Basic earnings (loss) per share attributable to Best Buy Co., Inc. shareholders
   | Continuing operations | $3.79 | $2.33 | $3.57
   | Discontinued operations | 0.07 | 0.26 | (0.04)
   | Basic earnings per share | $3.86 | $2.59 | $3.53
  Diluted earnings (loss) per share attributable to Best Buy Co., Inc. shareholders
   | Continuing operations | $3.74 | $2.30 | $3.53
  ```
  </details>

- **v2** · `BESTBUY_2017_10K` · PDF page **56** · column January 28, 2017 · millions
  - Quote: "Revenue \| $39,403"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statements of Earnings
  $and shares in millions, except per share amounts
  Fiscal Years Ended | January 28, 2017 | January 30, 2016 | January 31, 2015
  Revenue | $39,403 | $39,528 | $40,339
  Cost of goods sold | 29,963 | 30,334 | 31,292
  Restructuring charges — cost of goods sold | — | 3 | —
  Gross profit | 9,440 | 9,191 | 9,047
  Selling, general and administrative expenses | 7,547 | 7,618 | 7,592
  Restructuring charges | 39 | 198 | 5
  Operating income | 1,854 | 1,375 | 1,450
  ```
  </details>

- **v3** · `BESTBUY_2017_10K` · PDF page **56** · column January 30, 2016 · millions
  - Quote: "Net earnings attributable to Best Buy Co., Inc. shareholders \| $897"

  <details><summary>Passage</summary>

  ```
  Earnings from continuing operations before income tax expense | 1,816 | 1,310 | 1,387
  Income tax expense | 609 | 503 | 141
  Net earnings from continuing operations | 1,207 | 807 | 1,246
   | Gain (loss) from discontinued operations (Note 2), net of tax expense of $7, $1 and $0 | 21 | 90 | (11)
  Net earnings including noncontrolling interests | 1,228 | 897 | 1,235
   | Net earnings from discontinued operations attributable to noncontrolling interests | — | — | (2)
  Net earnings attributable to Best Buy Co., Inc. shareholders | $1,228 | $897 | $1,233
  Basic earnings (loss) per share attributable to Best Buy Co., Inc. shareholders
   | Continuing operations | $3.79 | $2.33 | $3.57
   | Discontinued operations | 0.07 | 0.26 | (0.04)
   | Basic earnings per share | $3.86 | $2.59 | $3.53
  Diluted earnings (loss) per share attributable to Best Buy Co., Inc. shareholders
   | Continuing operations | $3.74 | $2.30 | $3.53
  ```
  </details>

- **v4** · `BESTBUY_2017_10K` · PDF page **56** · column January 30, 2016 · millions
  - Quote: "Revenue \| $39,528"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statements of Earnings
  $and shares in millions, except per share amounts
  Fiscal Years Ended | January 28, 2017 | January 30, 2016 | January 31, 2015
  Revenue | $39,403 | $39,528 | $40,339
  Cost of goods sold | 29,963 | 30,334 | 31,292
  Restructuring charges — cost of goods sold | — | 3 | —
  Gross profit | 9,440 | 9,191 | 9,047
  Selling, general and administrative expenses | 7,547 | 7,618 | 7,592
  Restructuring charges | 39 | 198 | 5
  Operating income | 1,854 | 1,375 | 1,450
  ```
  </details>

- **v5** · `BESTBUY_2017_10K` · PDF page **56** · column January 31, 2015 · millions
  - Quote: "Net earnings attributable to Best Buy Co., Inc. shareholders \| $1,233"

  <details><summary>Passage</summary>

  ```
  Earnings from continuing operations before income tax expense | 1,816 | 1,310 | 1,387
  Income tax expense | 609 | 503 | 141
  Net earnings from continuing operations | 1,207 | 807 | 1,246
   | Gain (loss) from discontinued operations (Note 2), net of tax expense of $7, $1 and $0 | 21 | 90 | (11)
  Net earnings including noncontrolling interests | 1,228 | 897 | 1,235
   | Net earnings from discontinued operations attributable to noncontrolling interests | — | — | (2)
  Net earnings attributable to Best Buy Co., Inc. shareholders | $1,228 | $897 | $1,233
  Basic earnings (loss) per share attributable to Best Buy Co., Inc. shareholders
   | Continuing operations | $3.79 | $2.33 | $3.57
   | Discontinued operations | 0.07 | 0.26 | (0.04)
   | Basic earnings per share | $3.86 | $2.59 | $3.53
  Diluted earnings (loss) per share attributable to Best Buy Co., Inc. shareholders
   | Continuing operations | $3.74 | $2.30 | $3.53
  ```
  </details>

- **v6** · `BESTBUY_2017_10K` · PDF page **56** · column January 31, 2015 · millions
  - Quote: "Revenue \| $40,339"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  Consolidated Statements of Earnings
  $and shares in millions, except per share amounts
  Fiscal Years Ended | January 28, 2017 | January 30, 2016 | January 31, 2015
  Revenue | $39,403 | $39,528 | $40,339
  Cost of goods sold | 29,963 | 30,334 | 31,292
  Restructuring charges — cost of goods sold | — | 3 | —
  Gross profit | 9,440 | 9,191 | 9,047
  Selling, general and administrative expenses | 7,547 | 7,618 | 7,592
  Restructuring charges | 39 | 198 | 5
  Operating income | 1,854 | 1,375 | 1,450
  ```
  </details>

<details><summary>Gold answer</summary>

2.8%
</details>

## 50. What is the year end FY2019 total amount of inventories for Best Buy? Answer in USD millions. Base your judgments on the information provided primarily in the balance sheet.

`financebench_id_04417` · filing `BESTBUY_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The year-end FY2019 total amount of inventories for Best Buy is 5,409 million USD. This figure is reported as "Merchandise inventories" on the Consolidated Balance Sheets for the period ending February 2, 2019 [v1]. The value is explicitly listed in the assets section of the balance sheet [v1].

**Computation:** `merchandise_inventories_fy2019 = 5,409 million  where merchandise_inventories_fy2019 = 5,409 (millions, FY2019)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BESTBUY_2023_10K: code checks failed twice: formula: numeric constant 100 is not allowed: use only value names (a constant is allowed only if the question states it)

**Pages searched:** `BESTBUY_2023_10K` pages 1, 5, 23, 24, 26, 36, 39, 40, 42, 43, 50

<details><summary>Gold answer</summary>

Yes, the margins have been consistent, there has been a minor decline of 1.1% in gross margins between FY2022 and FY2023.
</details>

## 52. What are major acquisitions that Best Buy has done in FY2023, FY2022 and FY2021?

`financebench_id_01077` · filing `BESTBUY_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BESTBUY_2023_10K: code checks failed twice: acquisitions_fy2022_text: the quote is not on page 4. Copy it exactly from one line of the page

**Pages searched:** `BESTBUY_2023_10K` pages 4, 21, 23, 39, 40, 42, 43, 44, 50, 66, 69

<details><summary>Gold answer</summary>

Best Buy closed two acquisitions, both these companies were already partially owned by Best Buy, but Best Buy acquired all outstanding shares of these two companies during FY 2022: (1) Current Health Ltd and (2) Two Peaks, LLC d/b/a Yardbird Furniture
</details>

## 53. Among operations, investing, and financing activities, which brought in the most (or lost the least) cash flow for Best Buy in FY2023?

`financebench_id_01275` · filing `BESTBUY_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Operating activities brought in the most cash flow for Best Buy in FY2023 with $1,824 million [v1]. This amount is higher than the cash used in investing activities of $(962) million and financing activities of $(1,806) million [v2, v3]. The computed maximum of these three values confirms that operating activities provided the highest cash flow at 1,824 million [COMPUTED RESULT].

**Computation:** `max(operating_cash_flow_2023, investing_cash_flow_2023, financing_cash_flow_2023) = 1,824 million  where operating_cash_flow_2023 = 1,824 (millions, FY2023), investing_cash_flow_2023 = (962) (millions, FY2023), financing_cash_flow_2023 = (1,806) (millions, FY2023)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, there was a drop in Cash and cash equivalents of 781 million between FY 2023 and Q2 of FY2024. The balance decreased from $1,874 million on January 28, 2023, to $1,093 million on July 29, 2023 [v1, v2]. This decline is confirmed by the computed difference of 781 million [computed result].

**Computation:** `cash_jan_28_2023 - cash_jul_29_2023 = 781 million  where cash_jan_28_2023 = $1,874 (millions, FY2023), cash_jul_29_2023 = $1,093 (millions, Q2 FY2024)`

- **v1** · `BESTBUY_2024Q2_10Q` · PDF page **3** · column January 28, 2023 · millions
  - Quote: "Cash and cash equivalents \| $1,874"

  <details><summary>Passage</summary>

  ```
  Item 1.  Financial Statements
  Condensed Consolidated Balance Sheets
  $in millions, except per share amounts (unaudited)
   | July 29, 2023 | January 28, 2023 | July 30, 2022
  Assets
  Current assets
   Cash and cash equivalents | $1,093 | $1,874 | $840
    Receivables, net | 856 | 1,141 | 840
   Merchandise inventories | 5,651 | 5,140 | 6,043
   Other current assets | 704 | 647 | 621
   | Total current assets | 8,304 | 8,802 | 8,344
  Property and equipment, net | 2,305 | 2,352 | 2,319
  Operating lease assets | 2,813 | 2,746 | 2,796
  ```
  </details>

- **v2** · `BESTBUY_2024Q2_10Q` · PDF page **3** · column July 29, 2023 · millions
  - Quote: "Cash and cash equivalents \| $1,093"

  <details><summary>Passage</summary>

  ```
  Item 1.  Financial Statements
  Condensed Consolidated Balance Sheets
  $in millions, except per share amounts (unaudited)
   | July 29, 2023 | January 28, 2023 | July 30, 2022
  Assets
  Current assets
   Cash and cash equivalents | $1,093 | $1,874 | $840
    Receivables, net | 856 | 1,141 | 840
   Merchandise inventories | 5,651 | 5,140 | 6,043
   Other current assets | 704 | 647 | 621
   | Total current assets | 8,304 | 8,802 | 8,344
  Property and equipment, net | 2,305 | 2,352 | 2,319
  Operating lease assets | 2,813 | 2,746 | 2,796
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, there was a decline of ~42% between FY2023 and Q2 of FY 2024.
</details>

## 55. Was there any change in the number of Best Buy stores between Q2 of FY2024 and FY2023?

`financebench_id_00460` · filing `BESTBUY_2024Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, the number of Best Buy stores decreased by 23 between Q2 of FY2023 and Q2 of FY2024. The company had 930 stores at the end of Q2 FY2023 [v2] and 907 stores at the end of Q2 FY2024 [v1], resulting in a net decline of 23 stores [computed result].

**Computation:** `best_buy_stores_q2_2024 - best_buy_stores_q2_2023 = -23  where best_buy_stores_q2_2024 = 907 (units, Q2 FY2024), best_buy_stores_q2_2023 = 930 (units, Q2 FY2023)`

- **v1** · `BESTBUY_2024Q2_10Q` · PDF page **17** · column Total Stores at End of Second Quarter · units
  - Quote: "Best Buy \| 908 \| - \| (1) \| 907"

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

- **v2** · `BESTBUY_2024Q2_10Q` · PDF page **17** · column Total Stores at End of Second Quarter · units
  - Quote: "Best Buy \| 931 \| 1 \| (2) \| 930"

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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The best-performing product category in Best Buy's domestic market during Q2 of FY2024 was Computing and Mobile Phones, with revenue of $3,674 million [v1]. This figure is higher than the revenues for Consumer Electronics ($2,658 million), Appliances ($1,384 million), Services ($550 million), Entertainment ($544 million), and Other ($80 million) [v2, v3, v4, v5, v6].

- **v1** · `BESTBUY_2024Q2_10Q` · PDF page **13** · column July 29, 2023 · millions
  - Quote: "Computing and Mobile Phones \| $3,674"

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
  - Quote: "Consumer Electronics \| 2,658"

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
  - Quote: "Appliances \| 1,384"

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
  - Quote: "Entertainment \| 544"

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
  - Quote: "Services \| 550"

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
  - Quote: "Other \| 80"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Block's FY2016 working capital ratio is 1.73. This result is calculated by dividing the total current assets of 1,001,425 (in thousands) by the total current liabilities of 577,464 (in thousands) as reported in the 2016 consolidated balance sheet [v1, v2].

**Computation:** `total_current_assets / total_current_liabilities = 1.73  where total_current_assets = 1,001,425 (thousands, FY2016), total_current_liabilities = 577,464 (thousands, FY2016)`

- **v1** · `BLOCK_2016_10K` · PDF page **68** · column 2016 · thousands
  - Quote: "Total current assets \| 1,001,425"

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
  - Quote: "Total current liabilities \| 577,464"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The total revenue growth rate for Block from FY2019 to FY2020 is 101.5%. This figure is calculated using the total net revenue of $9,497,578 thousand for 2020 and $4,713,500 thousand for 2019 as reported in the Consolidated Statements of Operations [v1, v2].

**Computation:** `(total_net_revenue_2020 - total_net_revenue_2019) / total_net_revenue_2019 = 101.5%  where total_net_revenue_2019 = 4,713,500 (thousands, FY2019), total_net_revenue_2020 = 9,497,578 (thousands, FY2020)`

- **v1** · `BLOCK_2020_10K` · PDF page **86** · column 2019 · thousands
  - Quote: "Total net revenue \| 9,497,578 \| 4,713,500 \| 3,298,177"

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

- **v2** · `BLOCK_2020_10K` · PDF page **86** · column 2020 · thousands
  - Quote: "Total net revenue \| 9,497,578 \| 4,713,500 \| 3,298,177"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Block generated $381.603 million in cash flow from operating activities in FY2020 [v1]. This figure is derived from the "Net cash provided by operating activities" line item in the company's 2020 Consolidated Statements of Cash Flows, which reported $381,603 in thousands [v1].

**Computation:** `operating_cash_flow_2020 = 381.603 million  where operating_cash_flow_2020 = 381,603 (thousands, FY2020)`

- **v1** · `BLOCK_2020_10K` · PDF page **90** · column 2020 · thousands
  - Quote: "Net cash provided by operating activities \| 381,603"

  <details><summary>Passage</summary>

  ```
   | Purchase of loans held for sale | (1,837,137) | (2,266,738) | (1,609,611)
   | Sales and principal payments of loans held for sale | 1,505,406 | 2,168,682 | 1,579,834
   | Customers payable | 1,733,138 | 523,795 | 15,597
   | Settlements payable | 143,528 | 41,697 | (60,651)
   | Charge-offs to accrued transaction losses | (73,613) | (78,325) | (58,192)
   | Other assets and liabilities | (186,819) | (47,478) | (27,624)
   | Net cash provided by operating activities | 381,603 | 465,699 | 295,080
  Cash flows from investing activities:
   | Purchase of marketable debt securities | (1,322,362) | (992,583) | (1,000,346)
   | Proceeds from maturities of marketable debt securities | 607,134 | 430,888 | 197,454
   | Proceeds from sale of marketable debt securities | 585,427 | 548,619 | 171,992
   | Purchase of marketable debt securities from customer funds | (642,252) | (311,499) | (148,096)
   | Proceeds from maturities of marketable debt securities from customer funds | 382,887 | 158,055 | —
  ```
  </details>

<details><summary>Gold answer</summary>

$382.00
</details>

## 60. We need to calculate a financial metric by using information only provided within the balance sheet. Please answer the following question: what is Boeing's year end FY2018 net property, plant, and equipment (in USD millions)?

`financebench_id_10285` · filing `BOEING_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's year-end FY2018 net property, plant, and equipment is 12,645 million USD. This value is reported directly in the Consolidated Statements of Financial Position for the year ended December 31, 2018 [v1]. The figure represents the net amount after accumulated depreciation as listed in the assets section of the balance sheet [v1].

**Computation:** `ppe_net_2018 = 12,645 million  where ppe_net_2018 = 12,645 (millions, FY2018)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BOEING_2022_10K: code checks failed twice: formula: unknown value name 'commercial_airplanes_revenue_2022' (names: [])

**Pages searched:** `BOEING_2022_10K` pages 22, 24, 27, 29, 38, 41, 55, 56, 57, 59, 61, 83

<details><summary>Gold answer</summary>

Yes. Boeing has product and service categories that represent more than 20% of Boeing's revenue for FY2022. These categories are Commercial Airplanes which comprises 39% of total revenue, Defence which comprises 35% of total revenue and Services which comprises 26% of total revenue.
</details>

## 62. Has Boeing reported any materially important ongoing legal battles from FY2022?

`financebench_id_01091` · filing `BOEING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Boeing reported materially important ongoing legal battles in FY2022, including multiple actions related to the 737 MAX accidents and an arbitration dispute with Embraer over terminated agreements [v1, v3]. The company stated it cannot reasonably estimate the range of loss for the remaining pending lawsuits regarding the 737 MAX or the outcome of the Embraer arbitration [v2, v4].

- **v1** · `BOEING_2022_10K` · PDF page **113** · column N/A · units
  - Quote: "Multiple legal actions have been filed against us as a result of the October 29, 2018 accident of Lion Air Flight 610 and the March 10, 2019 accident of Ethiopian Airlines Flight 302."

  <details><summary>Passage</summary>

  ```
  Table of Contents
  based upon current information, that the outcome of any such legal proceeding, claim, or government dispute and investigation will not have a
  material effect on our financial position, results of operations or cash flows. Where it is reasonably possible that we will incur losses in excess of
  recorded amounts in connection with any of the matters set forth below, we will disclose either the amount or range of reasonably possible
  losses in excess of such amounts or, where no such amount or range can be reasonably estimated, the reasons why no such estimate can be
  made.
  Multiple legal actions have been filed against us as a result of the October 29, 2018 accident of Lion Air Flight 610 and the March 10, 2019
  accident of Ethiopian Airlines Flight 302. During 2021, we entered into (i) a Deferred Prosecution Agreement with the U.S. Department of Justice
  that resolved the Department of Justice’s previously disclosed investigation into us regarding the evaluation of the 737 MAX by the Federal
  Aviation Administration (FAA) as well as (ii) a proposed settlement with plaintiffs in a shareholder derivative lawsuit that resulted in the Company
  receiving $219 in the second quarter of 2022. In September 2022, we settled a previously disclosed investigation by the Securities and
  Exchange Commission related to the 737 MAX accidents and consented to a civil penalty, which resulted in an earnings charge of $200 that was
  paid in October 2022. We cannot reasonably estimate a range of loss, if any, not covered by available insurance that we may incur as a result of
  ```
  </details>

- **v2** · `BOEING_2022_10K` · PDF page **113** · column N/A · units
  - Quote: "We cannot reasonably estimate a range of loss, if any, not covered by available insurance that we may incur as a result of any remaining pending lawsuits or other matters related to the accidents and the 737 MAX."

  <details><summary>Passage</summary>

  ```
  Multiple legal actions have been filed against us as a result of the October 29, 2018 accident of Lion Air Flight 610 and the March 10, 2019
  accident of Ethiopian Airlines Flight 302. During 2021, we entered into (i) a Deferred Prosecution Agreement with the U.S. Department of Justice
  that resolved the Department of Justice’s previously disclosed investigation into us regarding the evaluation of the 737 MAX by the Federal
  Aviation Administration (FAA) as well as (ii) a proposed settlement with plaintiffs in a shareholder derivative lawsuit that resulted in the Company
  receiving $219 in the second quarter of 2022. In September 2022, we settled a previously disclosed investigation by the Securities and
  Exchange Commission related to the 737 MAX accidents and consented to a civil penalty, which resulted in an earnings charge of $200 that was
  paid in October 2022. We cannot reasonably estimate a range of loss, if any, not covered by available insurance that we may incur as a result of
  any remaining pending lawsuits or other matters related to the accidents and the 737 MAX.
  During 2019, we entered into agreements with Embraer S.A. (Embraer) to establish joint ventures that included the commercial aircraft and
  services operations of Embraer, of which we were expected to acquire an 80 percent ownership stake for $4,200, as well as a joint venture to
  promote and develop new markets for the C-390 Millennium. In 2020, we exercised our contractual right to terminate these agreements based
  on Embraer’s failure to meet certain required closing conditions. Embraer has disputed our right to terminate the agreements, and the dispute is
  currently in arbitration. We cannot reasonably estimate a range of loss, if any, that may result from the arbitration, which we currently expect to
  ```
  </details>

- **v3** · `BOEING_2022_10K` · PDF page **113** · column N/A · units
  - Quote: "Embraer has disputed our right to terminate the agreements, and the dispute is currently in arbitration."

  <details><summary>Passage</summary>

  ```
  Exchange Commission related to the 737 MAX accidents and consented to a civil penalty, which resulted in an earnings charge of $200 that was
  paid in October 2022. We cannot reasonably estimate a range of loss, if any, not covered by available insurance that we may incur as a result of
  any remaining pending lawsuits or other matters related to the accidents and the 737 MAX.
  During 2019, we entered into agreements with Embraer S.A. (Embraer) to establish joint ventures that included the commercial aircraft and
  services operations of Embraer, of which we were expected to acquire an 80 percent ownership stake for $4,200, as well as a joint venture to
  promote and develop new markets for the C-390 Millennium. In 2020, we exercised our contractual right to terminate these agreements based
  on Embraer’s failure to meet certain required closing conditions. Embraer has disputed our right to terminate the agreements, and the dispute is
  currently in arbitration. We cannot reasonably estimate a range of loss, if any, that may result from the arbitration, which we currently expect to
  be completed in late 2023 or early 2024.
  Note 22 – Segment and Revenue Information
  Our primary profitability measurements to review a segment’s operating results are Earnings/(loss) from operations and operating margins. We
  operate in four reportable segments: BCA, BDS, BGS and BCC. All other activities fall within Unallocated items, eliminations and other. See
  page 58 for the Summary of Business Segment Data, which is an integral part of this note.
  ```
  </details>

- **v4** · `BOEING_2022_10K` · PDF page **113** · column N/A · units
  - Quote: "We cannot reasonably estimate a range of loss, if any, that may result from the arbitration, which we currently expect to be completed in late 2023 or early 2024."

  <details><summary>Passage</summary>

  ```
  Multiple legal actions have been filed against us as a result of the October 29, 2018 accident of Lion Air Flight 610 and the March 10, 2019
  accident of Ethiopian Airlines Flight 302. During 2021, we entered into (i) a Deferred Prosecution Agreement with the U.S. Department of Justice
  that resolved the Department of Justice’s previously disclosed investigation into us regarding the evaluation of the 737 MAX by the Federal
  Aviation Administration (FAA) as well as (ii) a proposed settlement with plaintiffs in a shareholder derivative lawsuit that resulted in the Company
  receiving $219 in the second quarter of 2022. In September 2022, we settled a previously disclosed investigation by the Securities and
  Exchange Commission related to the 737 MAX accidents and consented to a civil penalty, which resulted in an earnings charge of $200 that was
  paid in October 2022. We cannot reasonably estimate a range of loss, if any, not covered by available insurance that we may incur as a result of
  any remaining pending lawsuits or other matters related to the accidents and the 737 MAX.
  During 2019, we entered into agreements with Embraer S.A. (Embraer) to establish joint ventures that included the commercial aircraft and
  services operations of Embraer, of which we were expected to acquire an 80 percent ownership stake for $4,200, as well as a joint venture to
  promote and develop new markets for the C-390 Millennium. In 2020, we exercised our contractual right to terminate these agreements based
  on Embraer’s failure to meet certain required closing conditions. Embraer has disputed our right to terminate the agreements, and the dispute is
  currently in arbitration. We cannot reasonably estimate a range of loss, if any, that may result from the arbitration, which we currently expect to
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. Multiple lawsuits have been filed against Boeing resulting from a 2018 Lion Air crash and a 2019 Ethiopian Airlines crash.
</details>

## 63. Does Boeing have an improving gross margin profile as of FY2022? If gross margin is not a useful metric for a company like this, then state that and explain why.

`financebench_id_00678` · filing `BOEING_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BOEING_2022_10K: code checks failed twice: context_787_loss: the quote is not on page 35. Copy it exactly from one line of the page

**Pages searched:** `BOEING_2022_10K` pages 5, 23, 30, 32, 35, 41, 51, 55, 56, 57, 59, 61

<details><summary>Gold answer</summary>

Yes. Boeing has an improving gross margin profile as of FY2022. Gross profit improved from $3,017 million in FY2021 to $3,502 million in FY2022. Gross margin % improved from 4.8% in FY2021 to 5.3% in FY2022.
</details>

## 64. Who are the primary customers of Boeing as of FY2022?

`financebench_id_01290` · filing `BOEING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's primary customers in FY2022 include the commercial airline industry worldwide, military and government entities for defense systems, and both commercial and defense customers for global services [v1, v2, v3]. Additionally, non-U.S. customers, including foreign military sales, accounted for approximately 41% of the company's revenues [v4].

- **v1** · `BOEING_2022_10K` · PDF page **3** · column N/A · units
  - Quote: "This segment develops, produces and markets commercial jet aircraft principally to the commercial airline industry worldwide."

  <details><summary>Passage</summary>

  ```
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
  Defense, Space & Security Segment
  This segment engages in the research, development, production and modification of manned and unmanned military aircraft and weapons
  ```
  </details>

- **v2** · `BOEING_2022_10K` · PDF page **3** · column N/A · units
  - Quote: "This segment engages in the research, development, production and modification of manned and unmanned military aircraft and weapons systems for strike, surveillance and mobility..."

  <details><summary>Passage</summary>

  ```
  This segment develops, produces and markets commercial jet aircraft principally to the commercial airline industry worldwide. We are a leading
  producer of commercial aircraft and offer a family of commercial jetliners designed to meet a broad spectrum of global passenger and cargo
  requirements of airlines. This family of commercial jet aircraft in production includes the 737 narrow-body model and the 767, 777 and 787 wide-
  body models. We ended production of the 747 wide-body model in 2022. Development continues on the 777X program and the 737-7 and 737-
  10 derivatives.
  Defense, Space & Security Segment
  This segment engages in the research, development, production and modification of manned and unmanned military aircraft and weapons
  systems for strike, surveillance and mobility, including fighter and trainer aircraft; vertical  lift, including rotorcraft and tilt-rotor aircraft; and
  commercial derivative aircraft, including anti-submarine and tanker aircraft. In addition, this segment engages in the research, development,
  production and modification of the following products and related services: strategic defense and intelligence systems, including strategic missile
  and defense systems, command, control, communications, computers, intelligence, surveillance and reconnaissance (C4ISR), cyber and
  information solutions, and intelligence systems, satellite systems, including government and commercial satellites and space exploration.
  Global Services Segment
  ```
  </details>

- **v3** · `BOEING_2022_10K` · PDF page **3** · column N/A · units
  - Quote: "This segment provides services to our commercial and defense customers worldwide."

  <details><summary>Passage</summary>

  ```
  systems for strike, surveillance and mobility, including fighter and trainer aircraft; vertical  lift, including rotorcraft and tilt-rotor aircraft; and
  commercial derivative aircraft, including anti-submarine and tanker aircraft. In addition, this segment engages in the research, development,
  production and modification of the following products and related services: strategic defense and intelligence systems, including strategic missile
  and defense systems, command, control, communications, computers, intelligence, surveillance and reconnaissance (C4ISR), cyber and
  information solutions, and intelligence systems, satellite systems, including government and commercial satellites and space exploration.
  Global Services Segment
  This segment provides services to our commercial and defense customers worldwide. BGS sustains aerospace platforms and systems with a full
  spectrum of products and services, including supply chain and logistics management, engineering, maintenance and modifications, upgrades
  and conversions, spare parts, pilot and maintenance training systems and services, technical and maintenance documents, and data analytics
  and digital services.
  Boeing Capital Segment
  BCC seeks to ensure that Boeing customers have the financing they need to buy and take delivery of their Boeing product, while managing
  overall financing exposure. BCC’s  portfolio consists  of equipment under operating leases, sales-type/finance leases, notes and other
  ```
  </details>

- **v4** · `BOEING_2022_10K` · PDF page **12** · column N/A · units
  - Quote: "In 2022, non-U.S. customers, which includes foreign military sales (FMS), accounted for approximately 41% of our revenues."

  <details><summary>Passage</summary>

  ```
  Table of Contents
  We derive a significant portion of our revenues from non-U.S. sales and are subject to the risks of doing business in other countries.
  In 2022, non-U.S. customers, which includes foreign military sales (FMS), accounted for approximately 41% of our revenues. We expect that
  non-U.S. sales will continue to account for a significant portion of our revenues for the foreseeable future. As a result, we are subject to risks of
  doing business internationally, including:
  • | changes in regulatory requirements or other executive branch actions, such as Executive Orders;
  • | changes in the global trade environment, including disputes with authorities in non-U.S. jurisdictions, including international trade
   | authorities, that could impact sales and/or delivery of products and services outside the U.S. and/or impose costs on our customers in
   | the form of tariffs, duties or penalties attributable to the importation of Boeing products and services;
  ```
  </details>

<details><summary>Gold answer</summary>

Boeing's primary customers as of FY2022 are a limited number of commercial airlines and the US government. The US government accounted for 40% of Boeing's total revenues in FY2022.
</details>

## 65. Is Boeing's business subject to cyclicality?

`financebench_id_00464` · filing `BOEING_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BOEING_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2022,, 2021,

**Pages searched:** `BOEING_2022_10K` pages 2, 3, 8, 12, 16, 55, 56, 57, 59, 61, 62, 118

<details><summary>Gold answer</summary>

Yes, Boeing's business is subject to cyclicality due to its exposure to the airline industry which is a cyclical industry.
</details>

## 66. What production rate changes is Boeing forecasting for FY2023?

`financebench_id_00494` · filing `BOEING_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing forecasts increasing 787 production to 5 per month, resuming 777X production, and gradually increasing 737 production rates in 2023 [v1, v2, v3]. These changes are based on market demand and supply chain capacity [v3]. The company aims to stabilize operations and meet customer demand through these adjustments [v1, v2, v3].

- **v1** · `BOEING_2022_10K` · PDF page **9** · column 2023 · units
  - Quote: "The 787 program is currently producing at low rates and we expect to gradually increase to 5 per month in 2023."

  <details><summary>Passage</summary>

  ```
  including a suspension of 787 deliveries from May 2021 to August 2022. We continue to conduct inspections and rework on built and stored 787
  aircraft. A number of our customers have contractual remedies, including compensation for late deliveries or rights to reject individual airplane
  deliveries based on delivery delays. Delays on the 737, 777X and 787 programs have resulted in, and may continue to result in, customers
  having the right to terminate orders, be compensated for late deliveries and/or substitute orders for other Boeing aircraft.
  We must minimize disruption caused by production changes, achieve operational stability and implement productivity improvements in order to
  meet customer demand and maintain our profitability. We have previously announced plans to adjust production rates on several of our
  commercial aircraft programs. The 787 program is currently producing at low rates and we expect to gradually increase to 5 per month in 2023.
  Production of the 777X is currently paused and is expected to resume in 2023. The 737 program has experienced operational and supply chain
  challenges stabilizing production at 31 per month. We plan to gradually increase 737 production rates based on market demand and supply
  chain capacity. In addition, we continue to seek opportunities to reduce the costs of building our aircraft, including working with our suppliers to
  reduce supplier costs, identifying and implementing productivity improvements and optimizing how we manage inventory.  If production rate
  changes at any of our
   | 7
  ```
  </details>

- **v2** · `BOEING_2022_10K` · PDF page **9** · column 2023 · units
  - Quote: "Production of the 777X is currently paused and is expected to resume in 2023."

  <details><summary>Passage</summary>

  ```
  aircraft. A number of our customers have contractual remedies, including compensation for late deliveries or rights to reject individual airplane
  deliveries based on delivery delays. Delays on the 737, 777X and 787 programs have resulted in, and may continue to result in, customers
  having the right to terminate orders, be compensated for late deliveries and/or substitute orders for other Boeing aircraft.
  We must minimize disruption caused by production changes, achieve operational stability and implement productivity improvements in order to
  meet customer demand and maintain our profitability. We have previously announced plans to adjust production rates on several of our
  commercial aircraft programs. The 787 program is currently producing at low rates and we expect to gradually increase to 5 per month in 2023.
  Production of the 777X is currently paused and is expected to resume in 2023. The 737 program has experienced operational and supply chain
  challenges stabilizing production at 31 per month. We plan to gradually increase 737 production rates based on market demand and supply
  chain capacity. In addition, we continue to seek opportunities to reduce the costs of building our aircraft, including working with our suppliers to
  reduce supplier costs, identifying and implementing productivity improvements and optimizing how we manage inventory.  If production rate
  changes at any of our
   | 7
  ```
  </details>

- **v3** · `BOEING_2022_10K` · PDF page **9** · column 2023 · units
  - Quote: "We plan to gradually increase 737 production rates based on market demand and supply chain capacity."

  <details><summary>Passage</summary>

  ```
  deliveries based on delivery delays. Delays on the 737, 777X and 787 programs have resulted in, and may continue to result in, customers
  having the right to terminate orders, be compensated for late deliveries and/or substitute orders for other Boeing aircraft.
  We must minimize disruption caused by production changes, achieve operational stability and implement productivity improvements in order to
  meet customer demand and maintain our profitability. We have previously announced plans to adjust production rates on several of our
  commercial aircraft programs. The 787 program is currently producing at low rates and we expect to gradually increase to 5 per month in 2023.
  Production of the 777X is currently paused and is expected to resume in 2023. The 737 program has experienced operational and supply chain
  challenges stabilizing production at 31 per month. We plan to gradually increase 737 production rates based on market demand and supply
  chain capacity. In addition, we continue to seek opportunities to reduce the costs of building our aircraft, including working with our suppliers to
  reduce supplier costs, identifying and implementing productivity improvements and optimizing how we manage inventory.  If production rate
  changes at any of our
   | 7
  ```
  </details>

<details><summary>Gold answer</summary>

Boeing forecasts an increase in the production rates for the 737, 777X and 787 aircrafts in 2023.
</details>

## 67. How does Boeing's effective tax rate in FY2022 compare to FY2021?

`financebench_id_00585` · filing `BOEING_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's effective tax rate in FY2022 was (0.6)%, which is lower than the 14.8% rate recorded in FY2021 [v1, v2]. This represents a significant decrease in the effective tax rate year-over-year.

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2017 return on assets (ROA) for Coca-Cola is 1.42%. This result is calculated by dividing the 2017 net income of $1,248 million by the average of the 2017 total assets ($87,896 million) and 2016 total assets ($87,270 million) [v1, v2, v3]. The computed value of 1.42% is derived directly from these reported figures [COMPUTED RESULT].

**Computation:** `net_income_2017 / avg(total_assets_2017, total_assets_2016) = 1.42%  where net_income_2017 = 1,248 (millions, FY2017), total_assets_2017 = $87,896 (millions, FY2017), total_assets_2016 = $87,270 (millions, FY2016)`

- **v1** · `COCACOLA_2017_10K` · PDF page **30** · column 2017 · millions
  - Quote: "Net income attributable to shareowners of The Coca-Cola Company \| 1,248"

  <details><summary>Passage</summary>

  ```
  our consolidated financial statements and the accompanying notes thereto contained in "Item 8. Financial Statements and Supplementary Data" of this report.
  Year Ended December 31, | 2017 | 2016 | 2015 | 2014 | 2013
  (In millions except per share data)
  SUMMARY OF OPERATIONS
  Net operating revenues | $35,410 | $41,863 | $44,294 | $45,998 | $46,854
  Net income from continuing operations | 1,182 | 6,550 | 7,366 | 7,124 | 8,626
  Net income attributable to shareowners of
    The Coca-Cola Company | 1,248 | 6,527 | 7,351 | 7,098 | 8,584
  PER SHARE DATA
  Basic net income from continuing operations | $0.28 | $1.51 | $1.69 | $1.62 | $1.94
  Basic net income | 0.29 | 1.51 | 1.69 | 1.62 | 1.94
  Diluted net income from continuing operations | 0.27 | 1.49 | 1.67 | 1.60 | 1.90
  Diluted net income | 0.29 | 1.49 | 1.67 | 1.60 | 1.90
  ```
  </details>

- **v2** · `COCACOLA_2017_10K` · PDF page **30** · column 2017 · millions
  - Quote: "Total assets \| $87,896"

  <details><summary>Passage</summary>

  ```
  Basic net income from continuing operations | $0.28 | $1.51 | $1.69 | $1.62 | $1.94
  Basic net income | 0.29 | 1.51 | 1.69 | 1.62 | 1.94
  Diluted net income from continuing operations | 0.27 | 1.49 | 1.67 | 1.60 | 1.90
  Diluted net income | 0.29 | 1.49 | 1.67 | 1.60 | 1.90
  Cash dividends | 1.48 | 1.40 | 1.32 | 1.22 | 1.12
  BALANCE SHEET DATA
  Total assets | $87,896 | $87,270 | $89,996 | $91,968 | $90,002
  Long-term debt | 31,182 | 29,684 | 28,311 | 19,010 | 19,101
  The Company's results are impacted by acquisitions and divestitures. Refer to "Item 7. Management's Discussion and Analysis of Financial Condition and Results of
  Operations" for additional information.
  ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS
  Overview
  The following Management's Discussion and Analysis of Financial Condition and Results of Operations ("MD&A") is intended to help the reader understand The Coca-Cola
  ```
  </details>

- **v3** · `COCACOLA_2017_10K` · PDF page **30** · column 2016 · millions
  - Quote: "Total assets \| $87,270"

  <details><summary>Passage</summary>

  ```
  Basic net income from continuing operations | $0.28 | $1.51 | $1.69 | $1.62 | $1.94
  Basic net income | 0.29 | 1.51 | 1.69 | 1.62 | 1.94
  Diluted net income from continuing operations | 0.27 | 1.49 | 1.67 | 1.60 | 1.90
  Diluted net income | 0.29 | 1.49 | 1.67 | 1.60 | 1.90
  Cash dividends | 1.48 | 1.40 | 1.32 | 1.22 | 1.12
  BALANCE SHEET DATA
  Total assets | $87,896 | $87,270 | $89,996 | $91,968 | $90,002
  Long-term debt | 31,182 | 29,684 | 28,311 | 19,010 | 19,101
  The Company's results are impacted by acquisitions and divestitures. Refer to "Item 7. Management's Discussion and Analysis of Financial Condition and Results of
  Operations" for additional information.
  ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS
  Overview
  The following Management's Discussion and Analysis of Financial Condition and Results of Operations ("MD&A") is intended to help the reader understand The Coca-Cola
  ```
  </details>

<details><summary>Gold answer</summary>

0.01
</details>

## 69. What is Coca Cola's FY2021 COGS % margin? Calculate what was asked by utilizing the line items clearly shown in the income statement.

`financebench_id_09724` · filing `COCACOLA_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Coca-Cola's FY2021 COGS % margin is 39.7%. This result is calculated by dividing the Cost of goods sold of 15,357 million by the Net Operating Revenues of $38,655 million as reported in the 2021 income statement [v1, v2].

**Computation:** `cogs_2021 / revenue_2021 = 39.7%  where cogs_2021 = 15,357 (millions, FY2021), revenue_2021 = $38,655 (millions, FY2021)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Coca-Cola's FY2022 dividend payout ratio is 79.82%. This is calculated by dividing the total cash dividends paid of $7,616 million [v1] by the net income attributable to shareholders of $9,542 million [v2]. The computed result of 79.82% reflects the proportion of earnings distributed as dividends for the fiscal year [COMPUTED RESULT].

**Computation:** `abs(dividends_paid_2022) / net_income_shareholders_2022 = 79.82%  where dividends_paid_2022 = (7,616) (millions, FY2022), net_income_shareholders_2022 = $9,542 (millions, FY2022)`

- **v1** · `COCACOLA_2022_10K` · PDF page **66** · column 2022 · millions
  - Quote: "Dividends \| (7,616)"

  <details><summary>Passage</summary>

  ```
  Net Cash Provided by (Used in) Investing Activities | (763) | (2,765) | (1,477)
  Financing Activities
  Issuances of debt | 3,972 | 13,094 | 26,934
  Payments of debt | (4,930) | (12,866) | (28,796)
  Issuances of stock | 837 | 702 | 647
  Purchases of stock for treasury | (1,418) | (111) | (118)
  Dividends | (7,616) | (7,252) | (7,047)
  Other financing activities | (1,095) | (353) | 310
  Net Cash Provided by (Used in) Financing Activities | (10,250) | (6,786) | (8,070)
  Effect of Exchange Rate Changes on Cash, Cash Equivalents, Restricted Cash and
    Restricted Cash Equivalents | (205) | (159) | 76
  Cash, Cash Equivalents, Restricted Cash and Restricted Cash Equivalents
  Net increase (decrease) in cash, cash equivalents, restricted cash and restricted cash
  ```
  </details>

- **v2** · `COCACOLA_2022_10K` · PDF page **63** · column 2022 · millions
  - Quote: "Net Income Attributable to Shareowners of The Coca-Cola Company \| $9,542"

  <details><summary>Passage</summary>

  ```
  Equity income (loss) — net | 1,472 | 1,438 | 978
  Other income (loss) — net | (262) | 2,000 | 841
  Income Before Income Taxes | 11,686 | 12,425 | 9,749
  Income taxes | 2,115 | 2,621 | 1,981
  Consolidated Net Income | 9,571 | 9,804 | 7,768
  Less: Net income (loss) attributable to noncontrolling interests | 29 | 33 | 21
  Net Income Attributable to Shareowners of The Coca-Cola Company | $9,542 $9,771 $7,747
  Basic Net Income Per Share 1 | $2.20 $2.26 $1.80
  Diluted Net Income Per Share 1 | $2.19 $2.25 $1.79
  Average Shares Outstanding — Basic | 4,328 | 4,315 | 4,295
  Effect of dilutive securities | 22 | 25 | 28
  Average Shares Outstanding — Diluted | 4,350 | 4,340 | 4,323
  1 Calculated based on net income attributable to shareowners of The Coca-Cola Company.
  ```
  </details>

<details><summary>Gold answer</summary>

0.8
</details>

## 71. Based on the information provided primarily in the balance sheet and the statement of income, what is FY2020 days payable outstanding (DPO) for Corning? DPO is defined as: 365 * (average accounts payable between FY2019 and FY2020) / (FY2020 COGS + change in inventory between FY2019 and FY2020). Round your answer to two decimal places.

`financebench_id_10130` · filing `CORNING_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2020 days payable outstanding (DPO) for Corning is 63.86 days. This value is computed using the accounts payable figures of 1,174 and 1,587, the cost of sales of 7,772, and the inventory values of 2,438 and 2,320 [v1, v2, v3, v4, v5]. The final result of 63.86 is derived directly from the provided calculation formula using these specific evidence values [COMPUTED RESULT].

**Computation:** `365 * avg(accounts_payable_2020, accounts_payable_2019) / (cost_of_sales_2020 + (inventory_2020 - inventory_2019)) = 63.86  where accounts_payable_2020 = 1,174 (millions, FY2020), accounts_payable_2019 = 1,587 (millions, FY2019), cost_of_sales_2020 = 7,772 (millions, FY2020), inventory_2020 = 2,438 (millions, FY2020), inventory_2019 = 2,320 (millions, FY2019)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average unadjusted operating income margin for Corning from FY2019 to FY2021 is 10.3%. This result is calculated by averaging the operating income margins for each year, derived from operating incomes of $1,306 million, $509 million, and $2,112 million against net sales of $11,503 million, $11,303 million, and $14,082 million respectively [v1, v2, v3, v4, v5, v6].

**Computation:** `avg(operating_income_2019 / net_sales_2019, operating_income_2020 / net_sales_2020, operating_income_2021 / net_sales_2021) = 10.3%  where operating_income_2019 = 1,306 (millions, FY2019), operating_income_2020 = 509 (millions, FY2020), operating_income_2021 = 2,112 (millions, FY2021), net_sales_2019 = 11,503 (millions, FY2019), net_sales_2020 = 11,303 (millions, FY2020), net_sales_2021 = 14,082 (millions, FY2021)`

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

- **v2** · `CORNING_2021_10K` · PDF page **65** · column 2020 · millions
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

- **v3** · `CORNING_2021_10K` · PDF page **65** · column 2021 · millions
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

- **v4** · `CORNING_2021_10K` · PDF page **65** · column 2019 · millions
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

- **v5** · `CORNING_2021_10K` · PDF page **65** · column 2020 · millions
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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** CORNING_2022_10K: verifier: answer_supported=no. The computation is incorrect. The change in the effective tax rate is 22.9% - 20.2% = 2.7 percentage points, or a percentage change of (22.9 - 20.2) / 20.2 = 13.36%. The provided computation (270.0%) is mathematically incorrect.

**Pages searched:** `CORNING_2022_10K` pages 24, 26, 32, 52, 58, 59, 60, 61, 62, 77, 79, 95

<details><summary>Gold answer</summary>

The effective tax rate of Corning has changed from 20% in FY2021 to 23% in FY 2022.
</details>

## 74. Does Corning have positive working capital based on FY2022 data? If working capital is not a useful or relevant metric for this company, then please state that and explain why.

`financebench_id_00005` · filing `CORNING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Corning has positive working capital based on FY2022 data. The company's total current assets of $7,453 million exceeded its total current liabilities of $5,175 million, resulting in a computed working capital of $2,278 million [v1, v2]. This metric is relevant for Corning as it indicates the company's ability to meet its short-term obligations with its short-term assets.

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Costco had total assets of $59,268 million at the end of FY2021. This figure is reported in the Consolidated Balance Sheets under the column for August 29, 2021 [v1]. The computed result confirms the total assets value as 59,268 million [COMPUTED RESULT].

**Computation:** `total_assets_2021 = 59,268 million  where total_assets_2021 = $59,268 (millions, FY2021)`

- **v1** · `COSTCO_2021_10K` · PDF page **38** · column August 29, 2021 · millions
  - Quote: "TOTAL ASSETS \| $59,268  $55,556"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 fixed asset turnover ratio for CVS Health is 17.98. This result is calculated by dividing the 2018 total revenues of $194,579 million by the average of the 2018 and 2017 property and equipment, net values of $11,349 million and $10,292 million, respectively [v1, v2, v3]. The computed ratio of 17.98 reflects the efficiency of the company's fixed assets in generating revenue for that fiscal year [v1, v2, v3].

**Computation:** `revenue_2018 / avg(ppe_2018, ppe_2017) = 17.98  where revenue_2018 = 194,579 (millions, FY2018), ppe_2018 = 11,349 (millions, FY2018), ppe_2017 = 10,292 (millions, FY2017)`

- **v1** · `CVSHEALTH_2018_10K` · PDF page **302** · column 2018 · millions
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

- **v2** · `CVSHEALTH_2018_10K` · PDF page **304** · column 2018 · millions
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

- **v3** · `CVSHEALTH_2018_10K` · PDF page **304** · column 2017 · millions
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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, CVS Health is not a capital-intensive business based on FY2022 data, as its net property and equipment of $12,873 million represents only 0.0399 of its total revenues of $322,467 million [v1, v2, COMPUTED RESULT]. This low ratio indicates that the company's operations rely less on heavy physical assets relative to its revenue generation. [v1, v2]

**Computation:** `ppe_net_2022 / total_revenues_2022 = 0.0399  where ppe_net_2022 = 12,873 (millions, FY2022), total_revenues_2022 = 322,467 (millions, FY2022), total_assets_2022 = 228,275 (millions, FY2022), capex_2022 = (2,727) (millions, FY2022)`

- **v1** · `CVSHEALTH_2022_10K` · PDF page **110** · column 2022 · millions
  - Quote: "Property and equipment, net \| 12,873"

  <details><summary>Passage</summary>

  ```
    Accounts receivable, net | 27,276 | 24,431
    Inventories | 19,090 | 17,760
    Assets held for sale | 908 | —
    Other current assets | 2,685 | 5,292
   | Total current assets | 65,682 | 60,008
    Long-term investments | 21,096 | 23,025
    Property and equipment, net | 12,873 | 12,896
    Operating lease right-of-use assets | 17,872 | 19,122
    Goodwill | 78,150 | 79,121
    Intangible assets, net | 24,754 | 29,026
    Separate accounts assets | 3,228 | 5,087
    Other assets | 4,620 | 4,714
  Total assets | $228,275  $232,999
  ```
  </details>

- **v2** · `CVSHEALTH_2022_10K` · PDF page **108** · column 2022 · millions
  - Quote: "Total revenues \| 322,467"

  <details><summary>Passage</summary>

  ```
  In millions, except per share amounts | 2022 | 2021 | 2020
  Revenues:
   Products | $226,616  $203,738  $190,688
   Premiums | 85,330 | 76,132 | 69,364
   Services | 9,683 | 11,042 | 7,856
   Net investment income | 838 | 1,199 | 798
  Total revenues | 322,467 | 292,111 | 268,706
  Operating costs:
   Cost of products sold | 196,892 | 175,803 | 163,981
   Benefit costs | 71,281 | 64,260 | 55,679
   Opioid litigation charges | 5,803 | — | —
   Loss on assets held for sale | 2,533 | — | —
   Store impairments | — | 1,358 | —
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, CVS Health requires an extensive asset base to operate, which is evident from its ROA of only 1.82% in 2022 and 3.39% in 2021, though it should be noted that a significant portion of this asset base is goodwill, and CVS's fixed assets/total assets ratio is on the lower side of 5.6%.
</details>

## 78. Has CVS Health reported any materially important ongoing legal battles from 2022, 2021 and 2020?

`financebench_id_01107` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, CVS Health reported materially important ongoing legal battles, specifically recording $5,803 million in opioid litigation charges in 2022 compared to no charges in 2021 or 2020 [v1, v2, v3]. The company concluded that settlement of opioid claims was probable, resulting in pre-tax charges of $5.2 billion and $99 million during the third and fourth quarters of 2022 [v4, v5]. Additionally, the company faced ongoing lawsuits and investigations regarding prescription processing practices and Medicare/Medicaid data submissions [v6, v8].

- **v1** · `CVSHEALTH_2022_10K` · PDF page **75** · column 2022 · millions
  - Quote: "Opioid litigation charges \| 5,803"

  <details><summary>Passage</summary>

  ```
    Services | 9,683 | 11,042 | 7,856 | (1,359) | (12.3)% | 3,186 | 40.6 %
    Net investment income | 838 | 1,199 | 798 | (361) | (30.1)% | 401 | 50.3 %
  Total revenues | 322,467 | 292,111 | 268,706 | 30,356 | 10.4 % | 23,405 | 8.7 %
  Operating costs:
    Cost of products sold | 196,892 | 175,803 | 163,981 | 21,089 | 12.0 % | 11,822 | 7.2 %
    Benefit costs | 71,281 | 64,260 | 55,679 | 7,021 | 10.9 % | 8,581 | 15.4 %
    Opioid litigation charges | 5,803 | — | — | 5,803 | 100.0 % | — | — %
    Loss on assets held for sale | 2,533 | — | — | 2,533 | 100.0 % | — | — %
    Store impairments | — | 1,358 | — | (1,358) | (100.0)% | 1,358 | 100.0 %
    Goodwill impairment | — | 431 | — | (431) | (100.0)% | 431 | 100.0 %
    Operating expenses | 38,212 | 37,066 | 35,135 | 1,146 | 3.1 % | 1,931 | 5.5 %
  Total operating costs | 314,721 | 278,918 | 254,795 | 35,803 | 12.8 % | 24,123 | 9.5 %
  Operating income | 7,746 | 13,193 | 13,911 | (5,447) | (41.3)% | (718) | (5.2)%
  ```
  </details>

- **v2** · `CVSHEALTH_2022_10K` · PDF page **75** · column 2021 · millions
  - Quote: "Opioid litigation charges \| —"

  <details><summary>Passage</summary>

  ```
    Services | 9,683 | 11,042 | 7,856 | (1,359) | (12.3)% | 3,186 | 40.6 %
    Net investment income | 838 | 1,199 | 798 | (361) | (30.1)% | 401 | 50.3 %
  Total revenues | 322,467 | 292,111 | 268,706 | 30,356 | 10.4 % | 23,405 | 8.7 %
  Operating costs:
    Cost of products sold | 196,892 | 175,803 | 163,981 | 21,089 | 12.0 % | 11,822 | 7.2 %
    Benefit costs | 71,281 | 64,260 | 55,679 | 7,021 | 10.9 % | 8,581 | 15.4 %
    Opioid litigation charges | 5,803 | — | — | 5,803 | 100.0 % | — | — %
    Loss on assets held for sale | 2,533 | — | — | 2,533 | 100.0 % | — | — %
    Store impairments | — | 1,358 | — | (1,358) | (100.0)% | 1,358 | 100.0 %
    Goodwill impairment | — | 431 | — | (431) | (100.0)% | 431 | 100.0 %
    Operating expenses | 38,212 | 37,066 | 35,135 | 1,146 | 3.1 % | 1,931 | 5.5 %
  Total operating costs | 314,721 | 278,918 | 254,795 | 35,803 | 12.8 % | 24,123 | 9.5 %
  Operating income | 7,746 | 13,193 | 13,911 | (5,447) | (41.3)% | (718) | (5.2)%
  ```
  </details>

- **v3** · `CVSHEALTH_2022_10K` · PDF page **75** · column 2020 · millions
  - Quote: "Opioid litigation charges \| —"

  <details><summary>Passage</summary>

  ```
    Services | 9,683 | 11,042 | 7,856 | (1,359) | (12.3)% | 3,186 | 40.6 %
    Net investment income | 838 | 1,199 | 798 | (361) | (30.1)% | 401 | 50.3 %
  Total revenues | 322,467 | 292,111 | 268,706 | 30,356 | 10.4 % | 23,405 | 8.7 %
  Operating costs:
    Cost of products sold | 196,892 | 175,803 | 163,981 | 21,089 | 12.0 % | 11,822 | 7.2 %
    Benefit costs | 71,281 | 64,260 | 55,679 | 7,021 | 10.9 % | 8,581 | 15.4 %
    Opioid litigation charges | 5,803 | — | — | 5,803 | 100.0 % | — | — %
    Loss on assets held for sale | 2,533 | — | — | 2,533 | 100.0 % | — | — %
    Store impairments | — | 1,358 | — | (1,358) | (100.0)% | 1,358 | 100.0 %
    Goodwill impairment | — | 431 | — | (431) | (100.0)% | 431 | 100.0 %
    Operating expenses | 38,212 | 37,066 | 35,135 | 1,146 | 3.1 % | 1,931 | 5.5 %
  Total operating costs | 314,721 | 278,918 | 254,795 | 35,803 | 12.8 % | 24,123 | 9.5 %
  Operating income | 7,746 | 13,193 | 13,911 | (5,447) | (41.3)% | (718) | (5.2)%
  ```
  </details>

- **v4** · `CVSHEALTH_2022_10K` · PDF page **175** · column N/A · units
  - Quote: "The Company has concluded that settlement of opioid claims by governmental entities and tribes is probable, and the loss related thereto could be reasonably estimated."

  <details><summary>Passage</summary>

  ```
  The Company has concluded that settlement of opioid claims by governmental entities and tribes is probable, and the loss related thereto could be reasonably
  estimated. As a result of that conclusion, and its assessment of certain other opioid-related claims including those for which the Company reached agreement in
  August and September 2022, the Company recorded pre-tax charges of $5.2 billion and $99 million during the three months ended September 30, 2022 and the
  three months ended December 31, 2022, respectively, of which $4.8 billion was recorded in other long-term liabilities on the consolidated balance sheet. In
  addition, the Company expects the cash impact in 2023 and 2024 to be less than $500 million in each year. Because loss contingencies are inherently
  unpredictable and unfavorable developments or resolutions can occur, the assessment requires judgments about future events. Moreover, the settlement is in its
  early phases, and there is no assurance that contingencies will be satisfied. The amount of ultimate loss may differ materially from this accrual.
  ```
  </details>

- **v5** · `CVSHEALTH_2022_10K` · PDF page **175** · column N/A · units
  - Quote: "the Company recorded pre-tax charges of $5.2 billion and $99 million during the three months ended September 30, 2022 and the three months ended December 31, 2022, respectively"

  <details><summary>Passage</summary>

  ```
  The Company has concluded that settlement of opioid claims by governmental entities and tribes is probable, and the loss related thereto could be reasonably
  estimated. As a result of that conclusion, and its assessment of certain other opioid-related claims including those for which the Company reached agreement in
  August and September 2022, the Company recorded pre-tax charges of $5.2 billion and $99 million during the three months ended September 30, 2022 and the
  three months ended December 31, 2022, respectively, of which $4.8 billion was recorded in other long-term liabilities on the consolidated balance sheet. In
  addition, the Company expects the cash impact in 2023 and 2024 to be less than $500 million in each year. Because loss contingencies are inherently
  unpredictable and unfavorable developments or resolutions can occur, the assessment requires judgments about future events. Moreover, the settlement is in its
  early phases, and there is no assurance that contingencies will be satisfied. The amount of ultimate loss may differ materially from this accrual.
  Because of the many uncertainties associated with any settlement arrangement or other resolution of all opioid-related litigation matters, including the
  uncertain scope of participation by governmental entities, and given that the Company continues to actively defend ongoing litigation for which it believes it
  ```
  </details>

- **v6** · `CVSHEALTH_2022_10K` · PDF page **175** · column N/A · units
  - Quote: "The Company is named as a defendant in a number of lawsuits and is subject to a number of investigations concerning its prescription processing practices"

  <details><summary>Passage</summary>

  ```
  cash flows.
  In January 2020, the DOJ served the Company with a DEA administrative subpoena. The subpoena seeks documents relating to practices with respect to
  prescription opioids and other controlled substances at CVS pharmacy locations concerning potential violations of the federal Controlled Substances Act and
  the federal False Claims Act. In January 2022, the DOJ served the Company with a CID regarding similar subjects, and the Company is providing documents
  and information in response to these matters.
  Prescription Processing Litigation and Investigations
  The Company is named as a defendant in a number of lawsuits and is subject to a number of investigations concerning its prescription processing practices,
  including the following:
  U.S. ex rel. Bassan et al. v. Omnicare, Inc. and CVS Health Corp. (U.S. District Court for the Southern District of New York). In December 2019, the U.S.
  Attorney’s Office for the Southern District of New York (the “SDNY”) filed a complaint-in-intervention in this previously sealed qui tam case. The complaint
  alleges that for certain non-skilled nursing facilities, Omnicare improperly filled prescriptions beyond one year where a valid prescription did not exist and that
  these dispensing events violated the federal False Claims Act. The Company is defending itself against these claims.
  U.S. ex rel. Gill et al. v. CVS Health Corp. et al. (U.S. District Court for the Northern District of Illinois). In July 2022, the Delaware Attorney General’s Office
  ```
  </details>

- **v8** · `CVSHEALTH_2022_10K` · PDF page **177** · column N/A · units
  - Quote: "The Company has received CIDs from the Civil Division of the DOJ in connection with a current investigation of the Company's patient chart review processes related to risk adjustment data submissions"

  <details><summary>Passage</summary>

  ```
  for prior contract years, the current contract year or future contract years. Any premium or fee refunds or adjustments resulting from regulatory audits, whether
  as a result of RADV, Public Exchange related or other audits by CMS, the OIG or otherwise, including audits of the Company’s MLR rebates, methodology
  and/or reports, could be material and could adversely affect the Company’s operating results, cash flows and/or financial condition.
  The RADV Audit Rule does not apply to the CMS Part C Improper Payment Measures audits nor the HHS-RADV programs.
  Medicare and Medicaid CIDs
  The Company has received CIDs from the Civil Division of the DOJ in connection with a current investigation of the Company’s patient chart review
  processes related to risk adjustment data submissions under Parts C and D of the Medicare program. The Company has been cooperating with the government
  and providing documents and information in response to these CIDs.
  In May 2017, the Company received a CID from the SDNY requesting documents and information concerning possible false claims submitted to Medicare in
  connection with reimbursements for prescription drugs under the Medicare Part D program. The Company has been cooperating with the government and
  providing documents and information in response to this CID.
  Stockholder Matters
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, CVS Health has been involved in multiple ongoing legal battles. Some notable legal dispute areas for CVS are: (1) usual and customary pricing litigation: where it's claimed that CVSâs retail pharmacies overcharged for prescription drugs; (2) PBM litigation and investigations: where it's claimed that that rebate agreements between the drug manufacturers and PBMs caused inflated prices for certain drug products; and (3) controlled substances litigation: legal matters around opioids for which CVS has agreed to pay up to $4.3 billion to claimants in remediation and $625 million to attorneys and fees
</details>

## 79. Has CVS Health paid dividends to common shareholders in Q2 of FY2022?

`financebench_id_01244` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, CVS Health paid dividends to common shareholders in Q2 of FY2022 because the company has paid cash dividends every quarter since becoming a public company and the quarterly cash dividend for 2022 was $0.55 per share [v1, v2].

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

- **v2** · `CVSHEALTH_2022_10K` · PDF page **68** · column N/A · units
  - Quote: "CVS Health Corporation has paid cash dividends every quarter since becoming a public company."

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
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, CVS paid a $ 0.55 dividend per share every quarter in FY2022
</details>

## 80. Does Foot Locker's new CEO have previous CEO experience in a similar company to Footlocker?

`financebench_id_00839` · filing `FOOTLOCKER_2022_8K_dated_2022-08-19` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Foot Locker's new CEO, Mary N. Dillon, has previous CEO experience in a similar company. She previously served as Chief Executive Officer of Ulta Beauty, Inc., which is described as a successful omni-channel retailer in the beauty and retail industry [v1, v2, v3, v4, v5]. This background aligns with Foot Locker's status as a retail company [v4, v5].

- **v1** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **2** · column August 19, 2022 · units
  - Quote: "Mary N. Dillon, 61, former Executive Chair and Chief Executive Officer of Ulta Beauty, Inc."

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

- **v2** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **2** · column August 19, 2022 · units
  - Quote: "Mary N. Dillon, 61, former Executive Chair and Chief Executive Officer of Ulta Beauty, Inc."

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

- **v3** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **2** · column August 19, 2022 · units
  - Quote: "She previously served as Chief Executive Officer and a member of the Board of Directors of Ulta from July 2013 through June 2021."

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

- **v4** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **30** · column August 19, 2022 · units
  - Quote: "Dillon has over 35 years of experience leading consumer-driven businesses in a diverse range of industries, from consumer-packaged goods to restaurants to telecom to beauty and retail."

  <details><summary>Passage</summary>

  ```
  forward, we are unanimous in our belief that Mary will be a tremendous addition to Foot Locker’s dynamic and diverse leadership team. Mary’s experience
  leading consumer-driven businesses and building robust brand portfolios, along with her commitment to culture, is deeply aligned with Foot Locker’s
  priorities and strategy.”
  Young added, “Today’s Board and leadership transitions are the culmination of a multi-year succession planning process which mirrors our track record of
  active planning for board succession and adherence to governance best practices. We are confident this will be a smooth transition as the Board and
  leadership team continue to focus on driving value for all Foot Locker stakeholders.”
  Dillon has over 35 years of experience leading consumer-driven businesses in a diverse range of industries, from consumer-packaged goods to restaurants
  to telecom to beauty and retail. She brings deep consumer marketing and digital transformation expertise, strong operational experience, a proven track
  record of shareholder value creation and a demonstrated commitment to leadership development. Most recently, she served as Executive Chair of Ulta
  Beauty, after having served as CEO for eight years, and was responsible for guiding the company as it became the leading beauty destination in the U.S.
  and a successful omni-channel retailer with a best-in-class loyalty program. This led to revenue CAGR of 16% and the tripling of the company’s market
  capitalization over her tenure. Previously, Dillon served as President, CEO and a member of the Board of Directors of U.S. Cellular, the Global Chief
  Marketing Officer of McDonald’s Corp., and held leadership roles at PepsiCo. Dillon also has extensive public company board experience. She received a
  ```
  </details>

- **v5** · `FOOTLOCKER_2022_8K_dated_2022-08-19` · PDF page **30** · column August 19, 2022 · units
  - Quote: "Most recently, she served as Executive Chair of Ulta Beauty, after having served as CEO for eight years, and was responsible for guiding the company as it became the leading beauty destination in the U.S. and a successful omni-channel retailer"

  <details><summary>Passage</summary>

  ```
  priorities and strategy.”
  Young added, “Today’s Board and leadership transitions are the culmination of a multi-year succession planning process which mirrors our track record of
  active planning for board succession and adherence to governance best practices. We are confident this will be a smooth transition as the Board and
  leadership team continue to focus on driving value for all Foot Locker stakeholders.”
  Dillon has over 35 years of experience leading consumer-driven businesses in a diverse range of industries, from consumer-packaged goods to restaurants
  to telecom to beauty and retail. She brings deep consumer marketing and digital transformation expertise, strong operational experience, a proven track
  record of shareholder value creation and a demonstrated commitment to leadership development. Most recently, she served as Executive Chair of Ulta
  Beauty, after having served as CEO for eight years, and was responsible for guiding the company as it became the leading beauty destination in the U.S.
  and a successful omni-channel retailer with a best-in-class loyalty program. This led to revenue CAGR of 16% and the tripling of the company’s market
  capitalization over her tenure. Previously, Dillon served as President, CEO and a member of the Board of Directors of U.S. Cellular, the Global Chief
  Marketing Officer of McDonald’s Corp., and held leadership roles at PepsiCo. Dillon also has extensive public company board experience. She received a
  Bachelor of Science in Marketing and Asian Studies from the University of Illinois at Chicago.
  Foot Locker, Inc. leads the celebration of sneaker and youth culture around the globe through a portfolio of brands including Foot Locker, Kids Foot
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. She was previous CEO of Ulta Beauty which means she had to manage a large retail company that has brick and mortar + online business. So yes she was a CEO in a similar company to Foot Locker before this.
</details>

## 81. Were there any board member nominees who had substantially more votes against joining than the other nominees?

`financebench_id_00822` · filing `FOOTLOCKER_2022_8K_dated-2022-05-20` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Richard A. Johnson received substantially more votes against his election than any other nominee, with 16,105,005 votes against [v3]. This figure is the maximum among all nominees, significantly exceeding the next highest count of 6,074,467 votes against Dona D. Young [v10]. The computed maximum of votes against any single nominee is 16,105,005 [COMPUTED RESULT].

**Computation:** `max(votes_against_drosos, votes_against_feldman, votes_against_johnson, votes_against_marmol, votes_against_nicosia, votes_against_oakland, votes_against_payne, votes_against_underhill, votes_against_walker, votes_against_young) = 16,105,005  where votes_against_drosos = 294,935 (units, FY2022), votes_against_feldman = 5,184,437 (units, FY2022), votes_against_johnson = 16,105,005 (units, FY2022), votes_against_marmol = 5,753,395 (units, FY2022), votes_against_nicosia = 4,827,808 (units, FY2022), votes_against_oakland = 4,524,393 (units, FY2022), votes_against_payne = 4,950,917 (units, FY2022), votes_against_underhill = 4,906,500 (units, FY2022), votes_against_walker = 4,419,340 (units, FY2022), votes_against_young = 6,074,467 (units, FY2022)`

- **v3** · `FOOTLOCKER_2022_8K_dated-2022-05-20` · PDF page **2** · column Votes Against · units
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

- **v10** · `FOOTLOCKER_2022_8K_dated-2022-05-20` · PDF page **2** · column Votes Against · units
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 cash conversion cycle (CCC) for General Mills is -3.70 days. This result is derived from the FY2019 cost of sales of 11,108.4 million, net sales of 16,865.2 million, and the average inventory, receivables, and payables figures from fiscal years 2018 and 2019 [v1, v2, v3, v4, v5, v6, v7, v8]. The calculation follows the provided formula using these specific line items to arrive at the final computed value of -3.70 [v1, v2, v3, v4, v5, v6, v7, v8].

**Computation:** `365 * avg(inventory_2018, inventory_2019) / cogs_2019 + 365 * avg(receivables_2018, receivables_2019) / revenue_2019 - 365 * avg(payables_2018, payables_2019) / (cogs_2019 + (inventory_2019 - inventory_2018)) = -3.70  where inventory_2019 = 1,559.3 (millions, FY2019), inventory_2018 = 1,642.2 (millions, FY2018), cogs_2019 = 11,108.4 (millions, FY2019), receivables_2019 = 1,679.7 (millions, FY2019), receivables_2018 = 1,684.2 (millions, FY2018), revenue_2019 = $16,865.2 (millions, FY2019), payables_2019 = $2,854.1 (millions, FY2019), payables_2018 = $2,746.2 (millions, FY2018)`

- **v1** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 26, 2019 · millions
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

- **v2** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 27, 2018 · millions
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

- **v3** · `GENERALMILLS_2019_10K` · PDF page **53** · column 2019 · millions
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

- **v4** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 26, 2019 · millions
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

- **v5** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 27, 2018 · millions
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

- **v6** · `GENERALMILLS_2019_10K` · PDF page **53** · column 2019 · millions
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

- **v7** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 26, 2019 · millions
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

- **v8** · `GENERALMILLS_2019_10K` · PDF page **55** · column May 27, 2018 · millions
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** General Mills's FY2020 working capital ratio is 0.68. This result is calculated by dividing the total current assets of $5,121.3 million by the total current liabilities of $7,491.5 million as reported in the consolidated balance sheets [v1, v2]. The computed ratio of 0.68 indicates that the company's current assets cover approximately 68% of its current liabilities [v1, v2].

**Computation:** `total_current_assets_2020 / total_current_liabilities_2020 = 0.68  where total_current_assets_2020 = 5,121.3 (millions, FY2020), total_current_liabilities_2020 = 7,491.5 (millions, FY2020)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2020 free cash flow for General Mills is 3,215.4 million USD. This is calculated by subtracting the capital expenditures of 460.8 million from the net cash provided by operating activities of 3,676.2 million [v1, v2]. The computed result confirms this difference is 3,215.4 million [COMPUTED RESULT].

**Computation:** `net_cash_operating_2020 - abs(capex_2020) = 3,215.4 million  where net_cash_operating_2020 = 3,676.2 (millions, FY2020), capex_2020 = (460.8) (millions, FY2020)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** GENERALMILLS_2022_10K: code checks failed twice: formula: unknown value name 'net_income_attributable_to_shareholders_2022' (names: [])

**Pages searched:** `GENERALMILLS_2022_10K` pages 18, 27, 28, 45, 46, 47, 48, 49, 69, 71, 86, 92

<details><summary>Gold answer</summary>

0.54
</details>

## 86. Are JnJ's FY2022 financials that of a high growth company?

`financebench_id_00956` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2022_10K: code checks failed twice: formula: unknown value name 'sales_2021' (names: [])

**Pages searched:** `JOHNSON_JOHNSON_2022_10K` pages 1, 4, 13, 27, 33, 35, 46, 47, 48, 49, 50, 87

<details><summary>Gold answer</summary>

No, JnJ's FY2022 financials are not of a high growth company as sales grew by 1.3% in FY2022.
</details>

## 87. What drove gross margin change as of FY2022 for JnJ? If gross margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00669` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2022_10K: code checks failed twice: formula: unknown value name 'gross_profit_2022' (names: [])

**Pages searched:** `JOHNSON_JOHNSON_2022_10K` pages 13, 16, 27, 35, 36, 46, 47, 48, 49, 50, 59, 87

<details><summary>Gold answer</summary>

For FY22, JnJ had changes in gross margin due to: One-time COVID-19 vaccine manufacturing exit related costs, Currency impacts in the Pharmaceutical segment, Commodity inflation in the MedTech and Consumer Health segments, partially offset by Supply chain benefits in the Consumer Health segment.
</details>

## 88. Roughly how many times has JnJ sold its inventory in FY2022? Calculate inventory turnover ratio for FY2022; if conventional inventory management is not meaningful for the company then state that and explain why.

`financebench_id_00711` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Johnson & Johnson sold its inventory approximately 2.72 times in FY2022. This inventory turnover ratio is derived from the cost of products sold of 31,089 million and the average of the 2022 inventory of 12,483 million and the 2021 inventory of 10,387 million [v1, v2, v3]. The metric is meaningful for this company as it maintains significant inventory levels reported on its balance sheet [v2, v3].

**Computation:** `cost_of_products_sold_2022 / avg(inventory_2022, inventory_2021) = 2.72  where cost_of_products_sold_2022 = 31,089 (millions, FY2022), inventory_2022 = 12,483 (millions, FY2022), inventory_2021 = 10,387 (millions, FY2021)`

- **v1** · `JOHNSON_JOHNSON_2022_10K` · PDF page **47** · column 2022 · millions
  - Quote: "Cost of products sold \| 31,089"

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
   Interest expense, net of portion capitalized (Note 4) | 276 | 183 | 201
  ```
  </details>

- **v2** · `JOHNSON_JOHNSON_2022_10K` · PDF page **46** · column 2022 · millions
  - Quote: "Inventories (Notes 1 and 3) \| 12,483"

  <details><summary>Passage</summary>

  ```
   | 2022 | 2021
  Assets
  Current assets
  Cash and cash equivalents (Notes 1 and 2) | $14,127 | 14,487
  Marketable securities (Notes 1 and 2) | 9,392 | 17,121
  Accounts receivable trade, less allowances for doubtful accounts $203 (2021, $230) | 16,160 | 15,283
  Inventories (Notes 1 and 3) | 12,483 | 10,387
  Prepaid expenses and other receivables | 3,132 | 3,701
  Total current assets | 55,294 | 60,979
  Property, plant and equipment, net (Notes 1 and 4) | 19,803 | 18,962
  Intangible assets, net (Notes 1 and 5) | 48,325 | 46,392
  Goodwill (Notes 1 and 5) | 45,231 | 35,246
  Deferred taxes on income (Note 8) | 9,123 | 10,223
  ```
  </details>

- **v3** · `JOHNSON_JOHNSON_2022_10K` · PDF page **46** · column 2021 · millions
  - Quote: "Inventories (Notes 1 and 3) \| 10,387"

  <details><summary>Passage</summary>

  ```
   | 2022 | 2021
  Assets
  Current assets
  Cash and cash equivalents (Notes 1 and 2) | $14,127 | 14,487
  Marketable securities (Notes 1 and 2) | 9,392 | 17,121
  Accounts receivable trade, less allowances for doubtful accounts $203 (2021, $230) | 16,160 | 15,283
  Inventories (Notes 1 and 3) | 12,483 | 10,387
  Prepaid expenses and other receivables | 3,132 | 3,701
  Total current assets | 55,294 | 60,979
  Property, plant and equipment, net (Notes 1 and 4) | 19,803 | 18,962
  Intangible assets, net (Notes 1 and 5) | 48,325 | 46,392
  Goodwill (Notes 1 and 5) | 45,231 | 35,246
  Deferred taxes on income (Note 8) | 9,123 | 10,223
  ```
  </details>

<details><summary>Gold answer</summary>

JnJ sold its inventory 2.7 times in FY2022.
</details>

## 89. Is growth in JnJ's adjusted EPS expected to accelerate in FY2023?

`financebench_id_00651` · filing `JOHNSON_JOHNSON_2022Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, growth in Johnson & Johnson's adjusted EPS is not expected to accelerate in FY2023. The midpoint of the expected growth for FY2023 is 3.5%, which is lower than the 3.6% growth achieved in FY2022 [v1, v2]. This represents a deceleration of 0.1 percentage points, as indicated by the computed difference of -10% (representing the relative change between the two rates) [v1, v2].

**Computation:** `fy2023_adjusted_eps_growth_midpoint - fy2022_adjusted_eps_growth = -10%  where fy2022_adjusted_eps_growth = 3.6% (units, FY2022), fy2023_adjusted_eps_growth_midpoint = 3.5% (units, FY2023)`

- **v1** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **2** · column % Change · units
  - Quote: "Adjusted EPS (diluted)1,4 \| $10.15 \| $9.80 \| 3.6%"

  <details><summary>Passage</summary>

  ```
  | Q4 | Full Year
   Non-GAAP* ($in Millions, except EPS) | 2022 | 2021 | % Change | 2022 | 2021 | % Change
   Operational Sales1,2 | 0.9% | 6.1%
   Adjusted Operational Sales1,3 | 0.8% | 6.2%
   Adjusted Net Earnings1,4 | $6,218 | $5,678 | 9.5% | $27,038 | $26,195 | 3.2%
   Adjusted EPS (diluted)1,4 | $2.35 | $2.13 | 10.3% | $10.15 | $9.80 | 3.6%
   1 Non-GAAP financial measure; refer to reconciliations of non-GAAP financial measures included in accompanying schedules
   2 Excludes the impact of translational currency
   3 Excludes the net impact of acquisitions and divestitures and translational currency
   4 Excludes intangible amortization expense and special items
   Note: values may have been rounded
  REGIONAL SALES RESULTS
  ```
  </details>

- **v2** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **5** · column Change vs. Prior Year / Mid-point · units
  - Quote: "Adjusted Operational EPS (Diluted)2,4/ Mid-point2,4 \| $10.40 – $10.60 / $10.50 \| Change vs. Prior Year / Mid-point \| 2.5% – 4.5% / 3.5%"

  <details><summary>Passage</summary>

  ```
  Johnson & Johnson does not provide GAAP financial measures on a forward-looking basis because the company
  is unable to predict with reasonable certainty the ultimate outcome of legal proceedings, unusual gains and
  losses, acquisition-related expenses and purchase accounting fair value adjustments without unreasonable
  effort. These items are uncertain, depend on various factors, and could be material to Johnson & Johnson's
  results computed in accordance with GAAP.
   | ($in Billions, except EPS) | January 2023
   | Adjusted Operational Sales1,2,5
   | 3.5% – 4.5% / 4.0%
   | Change vs. Prior Year / Mid-point
   | Operational Sales2,5/ Mid-point2,5 | $96.9B – $97.9B / $97.4B
   | Change vs. Prior Year / Mid-point | 4.5% – 5.5% / 5.0%
   | Estimated Reported Sales3,5/ Mid-point3,5 | $96.9B – $97.9B / $97.4B
   | Change vs. Prior Year / Mid-point | 4.5% – 5.5% / 5.0%
  ```
  </details>

<details><summary>Gold answer</summary>

No, rate of growth in adjusted EPS is expected to decelerate slightly from 3.6% in FY2022 to 3.5% in FY2023.
</details>

## 90. How did JnJ's US sales growth compare to international sales growth in FY2022?

`financebench_id_01484` · filing `JOHNSON_JOHNSON_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** JOHNSON_JOHNSON_2022Q4_EARNINGS: verifier: answer_supported=no. The computation is incorrect. The difference between 3.0% and (0.6)% is 3.6 percentage points, not 360%.

**Pages searched:** `JOHNSON_JOHNSON_2022Q4_EARNINGS` pages 1, 2, 3, 6, 8, 9, 10, 11, 13, 14, 19, 20

<details><summary>Gold answer</summary>

US sales increased 3.0% vs international sales decline of 0.6%.
</details>

## 91. Which business segment of JnJ will be treated as a discontinued operation from August 30, 2023 onward?

`financebench_id_01488` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The Consumer Health business segment of Johnson & Johnson will be treated as a discontinued operation from August 30, 2023 onward [v1]. This change occurred as a result of the completion of the exchange offer to finalize the separation of Kenvue Inc. [v1].

- **v1** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **4** · column August 30, 2023 · units
  - Quote: "As a result of the completion of the exchange offer, Johnson & Johnson will now present its Consumer Health business financial results as discontinued operations"

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2023_8K_dated-2023-08-30: code checks failed twice: formula: unknown value name 'gain_from_separation' (names: [])

**Pages searched:** `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` pages 2, 4, 6, 8, 12, 15, 16, 20, 21, 25, 26, 27

<details><summary>Gold answer</summary>

JnJ will make a gain of approximately $20 billion from the separation of its Consumer Health business segment.
</details>

## 93. What is the amount of the cash proceeds that JnJ realised from the separation of Kenvue (formerly Consumer Health business segment), as of August 30, 2023?

`financebench_id_01491` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2023_8K_dated-2023-08-30: code checks failed twice: formula: unknown value name 'cash_proceeds_from_separation' (names: [])

**Pages searched:** `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` pages 2, 4, 6, 8, 12, 14, 15, 16, 20, 25, 26, 27

<details><summary>Gold answer</summary>

JnJ realised $13.2 billion in cash proceeds from the separation of Kenvue.
</details>

## 94. Did JnJ's net earnings as a percent of sales increase in Q2 of FY2023 compared to Q2 of FY2022?

`financebench_id_01487` · filing `JOHNSON_JOHNSON_2023Q2_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Johnson & Johnson's net earnings as a percent of sales increased in Q2 of FY2023 compared to Q2 of FY2022. The computed difference between the two periods' net earnings margins is 0.1072% [v1, v2, v3, v4]. This increase is supported by the net earnings of $5,144 million and sales of $25,530 million in Q2 2023 versus $4,814 million and $24,020 million in Q2 2022 [v1, v2, v3, v4].

**Computation:** `(net_earnings_q2_2023 / sales_q2_2023) - (net_earnings_q2_2022 / sales_q2_2022) = 0.1072%  where net_earnings_q2_2023 = $5,144 (millions, Q2 FY2023), sales_q2_2023 = $25,530 (millions, Q2 FY2023), net_earnings_q2_2022 = $4,814 (millions, Q2 FY2022), sales_q2_2022 = $24,020 (millions, Q2 FY2022)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JPMORGAN_2021Q1_10Q: code checks failed twice: ccb_net_revenue_2021: the quote is not on page 160. Copy it exactly from one line of the page; cib_net_revenue_2021: the quote is not on page 160. Copy it exactly from one line of the page; cb_net_revenue_2021: the quote is not on page 160. Copy it exactly from one line of the page

**Pages searched:** `JPMORGAN_2021Q1_10Q` pages 4, 5, 23, 28, 31, 79, 81, 99, 102, 153, 160, 162

<details><summary>Gold answer</summary>

Corporate. Its net revenue was -$473 million.
</details>

## 96. If JPM went bankrupted by the end by 2021 Q1 and liquidated all of its assets to pay its shareholders, how much could each shareholder get?

`financebench_id_02119` · filing `JPMORGAN_2021Q1_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** If JPMorgan went bankrupt and liquidated all assets to pay shareholders at the end of Q1 2021, each shareholder could theoretically receive $92.73. This amount is calculated by dividing the total stockholders' equity of $280,714 million by the 3,027,128,112 common shares outstanding [v1, v2].

**Computation:** `total_stockholders_equity / common_shares_outstanding = 92.73  where total_stockholders_equity = 280,714 (millions, Q1 FY2021), common_shares_outstanding = 3,027,128,112 (units, Q1 FY2021)`

- **v1** · `JPMORGAN_2021Q1_10Q` · PDF page **81** · column March 31, 2021 · millions
  - Quote: "Total stockholders' equity \| 280,714"

  <details><summary>Passage</summary>

  ```
   Preferred stock ($1 par value; authorized 200,000,000 shares; issued 3,156,250 and 3,006,250 shares) | 31,563 | 30,063
   Common stock ($1 par value; authorized 9,000,000,000 shares; issued 4,104,933,895 shares) | 4,105 | 4,105
   Additional paid-in capital | 88,005 | 88,394
   Retained earnings | 248,151 | 236,990
   Accumulated other comprehensive income | 1,041 | 7,986
   Treasury stock, at cost (1,077,805,783 and 1,055,499,435 shares) | (92,151) | (88,184)
   Total stockholders’ equity | 280,714 | 279,354
   Total liabilities and stockholders’ equity | $3,689,336  $3,384,757
  (a) Prior-period amounts have been revised to conform with the current presentation. Refer to Note 1 for further information.
  (b) The following table presents information on assets and liabilities related to VIEs that are consolidated by the Firm at March 31, 2021, and December 31,
   | 2020. The assets of the consolidated VIEs are used to settle the liabilities of those entities. The holders of the beneficial interests generally do not have
   | recourse to the general credit of JPMorgan Chase. The assets and liabilities in the table below include third-party assets and liabilities of consolidated VIEs
   | and exclude intercompany balances that eliminate in consolidation. Refer to Note 13 for a further discussion
  ```
  </details>

- **v2** · `JPMORGAN_2021Q1_10Q` · PDF page **1** · column March 31, 2021 · units
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

**Status:** ANSWER · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The gross margin metric is not meaningful for JPMorgan because it is a financial services company that reports "Total net revenue" and "Total noninterest expense" rather than the cost of goods sold required to calculate gross margins [v1, v2]. Consequently, the concept of gross margin does not apply to its business model, and the provided evidence lists alternative metrics like the overhead ratio instead [v1, v2].

- **v1** · `JPMORGAN_2022_10K` · PDF page **46** · column 2022 · millions
  - Quote: "Total net revenue \| $128,695"

  <details><summary>Passage</summary>

  ```
  Financial
  THREE-YEAR SUMMARY OF CONSOLIDATED FINANCIAL HIGHLIGHTS (unaudited)
   As of or for the year ended December 31,
   (in millions, except per share, ratio, headcount data and where otherwise noted) | 2022 | 2021 | 2020
   Selected income statement data
   Total net revenue | $128,695 | $121,649 | $119,951
   Total noninterest expense | 76,140 | 71,343 | 66,656
   Pre-provision profit(a) | 52,555 | 50,306 | 53,295
   Provision for credit losses | 6,389 | (9,256) | 17,480
   Income before income tax expense | 46,166 | 59,562 | 35,815
   Income tax expense | 8,490 | 11,228 | 6,684
   | Net income | $37,676 | $48,334 | $29,131
  ```
  </details>

- **v2** · `JPMORGAN_2022_10K` · PDF page **46** · column 2022 · millions
  - Quote: "Total noninterest expense \| 76,140"

  <details><summary>Passage</summary>

  ```
  Financial
  THREE-YEAR SUMMARY OF CONSOLIDATED FINANCIAL HIGHLIGHTS (unaudited)
   As of or for the year ended December 31,
   (in millions, except per share, ratio, headcount data and where otherwise noted) | 2022 | 2021 | 2020
   Selected income statement data
   Total net revenue | $128,695 | $121,649 | $119,951
   Total noninterest expense | 76,140 | 71,343 | 66,656
   Pre-provision profit(a) | 52,555 | 50,306 | 53,295
   Provision for credit losses | 6,389 | (9,256) | 17,480
   Income before income tax expense | 46,166 | 59,562 | 35,815
   Income tax expense | 8,490 | 11,228 | 6,684
   | Net income | $37,676 | $48,334 | $29,131
   Earnings per share data
  ```
  </details>

<details><summary>Gold answer</summary>

Since JPM is a financial institution, gross margin is not a relevant metric.
</details>

## 98. In 2022 Q2, which of JPM's business segments had the highest net income?

`financebench_id_00394` · filing `JPMORGAN_2022Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The Corporate & Investment Bank segment had the highest net income in Q2 2022 with $3,725 million [v2]. This amount exceeds the net income of Consumer & Community Banking ($3,100 million), Asset & Wealth Management ($1,004 million), and Commercial Banking ($994 million) [v1, v3, v4]. The computed maximum value across these segments is 3,725 million [COMPUTED RESULT].

**Computation:** `max(ccb_net_income_q2_2022, cib_net_income_q2_2022, cb_net_income_q2_2022, awm_net_income_q2_2022) = 3,725 million  where ccb_net_income_q2_2022 = $3,100 (millions, Q2 FY2022), cib_net_income_q2_2022 = $3,725 (millions, Q2 FY2022), cb_net_income_q2_2022 = $994 (millions, Q2 FY2022), awm_net_income_q2_2022 = $1,004 (millions, Q2 FY2022)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, the risk JPM faced decreased in the second fiscal quarter of 2023 compared to the same period in the prior year. The average Total VaR was $47 million in Q2 2023, down from $54 million in Q2 2022 [v1, v2]. This decrease was predominantly driven by risk reductions impacting Credit Portfolio VaR and fixed income [v1, v2].

- **v1** · `JPMORGAN_2023Q2_10Q` · PDF page **85** · column Three months ended June 30, 2023 Avg. · millions
  - Quote: "Total VaR \| $47 \| $36 \| $56"

  <details><summary>Passage</summary>

  ```
   CIB VaR | 44 | 34 | 55 | 45 | 35 | 58 | 52 | 38 | 70
   CCB VaR | 9 | (d) | 6 | 14 | 11 | 6 | 15 | 5 | (d) | 4 | 6
   Corporate and other LOB VaR(c) | 13 | 11 | 15 | 15 | 13 | 17 | 10 | 9 | 11
   Diversification benefit to other VaR(a) | (7) | NM | NM | (8) | NM | NM | (3) | NM | NM
   Other VaR | 15 | 13 | 19 | 18 | 14 | 22 | 12 | 10 | 14
   Diversification benefit to CIB and other VaR(a) | (12) | NM | NM | (16) | NM | NM | (10) | NM | NM
   Total VaR | $47 | $36 | $56 | $47 | $37 | $57 | $54 | $41 | $71
  (a) Diversification benefit represents the difference between the portfolio VaR and the sum of its individual components. This reflects the non-additive nature
   | of VaR due to imperfect correlation across LOBs, Corporate, and risk types. For maximum and minimum VaR, diversification benefit is not meaningful as
   | the maximum and minimum VaR for each portfolio may have occurred on different trading days than the components.
  (b) Credit portfolio VaR includes the derivative CVA, hedges of the CVA and hedges of the retained loan portfolio, which are reported in principal transactions
   | revenue. This VaR does not include the retained loan portfolio, which is not reported at fair value. In the first quarter of 2022, in line with the Firm's
   | internal model governance, the credit risk component of CVA related to certain counterparties was removed from Credit Portfolio VaR due to the widening
  ```
  </details>

- **v2** · `JPMORGAN_2023Q2_10Q` · PDF page **85** · column Three months ended June 30, 2022 Avg. · millions
  - Quote: "Total VaR \| $47 \| $36 \| $56 \| $47 \| $37 \| $57 \| $54 \| $41 \| $71"

  <details><summary>Passage</summary>

  ```
   CIB VaR | 44 | 34 | 55 | 45 | 35 | 58 | 52 | 38 | 70
   CCB VaR | 9 | (d) | 6 | 14 | 11 | 6 | 15 | 5 | (d) | 4 | 6
   Corporate and other LOB VaR(c) | 13 | 11 | 15 | 15 | 13 | 17 | 10 | 9 | 11
   Diversification benefit to other VaR(a) | (7) | NM | NM | (8) | NM | NM | (3) | NM | NM
   Other VaR | 15 | 13 | 19 | 18 | 14 | 22 | 12 | 10 | 14
   Diversification benefit to CIB and other VaR(a) | (12) | NM | NM | (16) | NM | NM | (10) | NM | NM
   Total VaR | $47 | $36 | $56 | $47 | $37 | $57 | $54 | $41 | $71
  (a) Diversification benefit represents the difference between the portfolio VaR and the sum of its individual components. This reflects the non-additive nature
   | of VaR due to imperfect correlation across LOBs, Corporate, and risk types. For maximum and minimum VaR, diversification benefit is not meaningful as
   | the maximum and minimum VaR for each portfolio may have occurred on different trading days than the components.
  (b) Credit portfolio VaR includes the derivative CVA, hedges of the CVA and hedges of the retained loan portfolio, which are reported in principal transactions
   | revenue. This VaR does not include the retained loan portfolio, which is not reported at fair value. In the first quarter of 2022, in line with the Firm's
   | internal model governance, the credit risk component of CVA related to certain counterparties was removed from Credit Portfolio VaR due to the widening
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. It decreased.
</details>

## 100. What is Kraft Heinz's FY2019 inventory turnover ratio? Inventory turnover ratio is defined as: (FY2019 COGS) / (average inventory between FY2018 and FY2019). Round your answer to two decimal places. Please base your judgments on the information provided primarily in the balance sheet and the P&L statement.

`financebench_id_10499` · filing `KRAFTHEINZ_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Kraft Heinz's FY2019 inventory turnover ratio is 6.25. This result is computed by dividing the 2019 cost of products sold of 16,830 million by the average of the 2019 inventory of 2,721 million and the 2018 inventory of 2,667 million [v1, v2, v3]. The final calculated value is 6.25 [v1, v2, v3].

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's FY2020 asset turnover ratio is 1.33. This result is calculated by dividing the FY2020 total net sales of $65,398 million by the average of total assets from FY2020 ($50,710 million) and FY2019 ($47,528 million) [v1, v2, v3]. The computed value of 1.33 reflects the company's efficiency in generating revenue from its asset base during the fiscal year [COMPUTED RESULT].

**Computation:** `revenue_2020 / avg(total_assets_2020, total_assets_2019) = 1.33  where revenue_2020 = 65,398 (millions, FY2020), total_assets_2020 = 50,710 (millions, FY2020), total_assets_2019 = 47,528 (millions, FY2019)`

- **v1** · `LOCKHEEDMARTIN_2020_10K` · PDF page **67** · column 2020 · millions
  - Quote: "Total net sales \| 65,398"

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
  - Quote: "Total assets \| $50,710"

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
  - Quote: "Total assets \| $50,710  $47,528"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's FY2021 net working capital is 5,818 million USD. This figure is calculated by subtracting total current liabilities of 13,997 million from total current assets of 19,815 million as reported in the 2021 Consolidated Balance Sheets [v1, v2]. The resulting value of 5,818 million represents the company's short-term liquidity position for that fiscal year [COMPUTED RESULT].

**Computation:** `total_current_assets_2021 - total_current_liabilities_2021 = 5,818 million  where total_current_assets_2021 = 19,815 (millions, FY2021), total_current_liabilities_2021 = 13,997 (millions, FY2021)`

- **v1** · `LOCKHEEDMARTIN_2021_10K` · PDF page **68** · column 2021 · millions
  - Quote: "Total current assets \| 19,815 \| 19,378"

  <details><summary>Passage</summary>

  ```
  Current assets
    Cash and cash equivalents | $3,604  $3,160
    Receivables, net | 1,963 | 1,978
    Contract assets | 10,579 | 9,545
    Inventories | 2,981 | 3,545
    Other current assets | 688 | 1,150
   | Total current assets | 19,815 | 19,378
  Property, plant and equipment, net | 7,597 | 7,213
  Goodwill | 10,813 | 10,806
  Intangible assets, net | 2,706 | 3,012
  Deferred income taxes | 2,290 | 3,475
  Other noncurrent assets | 7,652 | 6,826
   | Total assets | $50,873  $50,710
  ```
  </details>

- **v2** · `LOCKHEEDMARTIN_2021_10K` · PDF page **68** · column 2021 · millions
  - Quote: "Total current liabilities \| 13,997 \| 13,933"

  <details><summary>Passage</summary>

  ```
  Current liabilities
    Accounts payable | $780  $880
    Salaries, benefits and payroll taxes | 3,108 | 3,163
    Contract liabilities | 8,107 | 7,545
    Current maturities of long-term debt | 6 | 500
    Other current liabilities | 1,996 | 1,845
   | Total current liabilities | 13,997 | 13,933
  Long-term debt, net | 11,670 | 11,669
  Accrued pension liabilities | 8,319 | 12,874
  Other noncurrent liabilities | 5,928 | 6,196
   | Total liabilities | 39,914 | 44,672
  Stockholders’ equity
   Common stock, $1 par value per share | 271 | 279
  ```
  </details>

<details><summary>Gold answer</summary>

$5818.00
</details>

## 103. What is Lockheed Martin's 2 year total revenue CAGR from FY2020 to FY2022 (in units of percents and round to one decimal place)? Provide a response to the question by primarily using the statement of income.

`financebench_id_03718` · filing `LOCKHEEDMARTIN_2022_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's 2-year total revenue CAGR from FY2020 to FY2022 is 0.4%. This growth rate is calculated based on total net sales of $65,398 million in 2020 and $65,984 million in 2022 as reported in the Consolidated Statements of Earnings [v1, v2].

**Computation:** `cagr(revenue_2020, revenue_2022) = 0.4%  where revenue_2020 = 65,398 (millions, FY2020), revenue_2022 = 65,984 (millions, FY2022)`

- **v1** · `LOCKHEEDMARTIN_2022_10K` · PDF page **63** · column 2020 · millions
  - Quote: "Total net sales \| 65,984 \| 67,044 \| 65,398"

  <details><summary>Passage</summary>

  ```
   | (in millions, except per share data)
   | Years Ended December 31,
   | 2022 | 2021 | 2020
   Net sales
    Products | $55,466  $56,435  $54,928
    Services | 10,518 | 10,609 | 10,470
   | Total net sales | 65,984 | 67,044 | 65,398
   Cost of sales
    Products | (49,577) | (50,273) | (48,996)
    Services | (9,280) | (9,463) | (9,371)
    Severance and other charges | (100) | (36) | (27)
    Other unallocated, net | 1,260 | 1,789 | 1,650
   | Total cost of sales | (57,697) | (57,983) | (56,744)
  ```
  </details>

- **v2** · `LOCKHEEDMARTIN_2022_10K` · PDF page **63** · column 2022 · millions
  - Quote: "Total net sales \| 65,984 \| 67,044 \| 65,398"

  <details><summary>Passage</summary>

  ```
   | (in millions, except per share data)
   | Years Ended December 31,
   | 2022 | 2021 | 2020
   Net sales
    Products | $55,466  $56,435  $54,928
    Services | 10,518 | 10,609 | 10,470
   | Total net sales | 65,984 | 67,044 | 65,398
   Cost of sales
    Products | (49,577) | (50,273) | (48,996)
    Services | (9,280) | (9,463) | (9,371)
    Severance and other charges | (100) | (36) | (27)
    Other unallocated, net | 1,260 | 1,789 | 1,650
   | Total cost of sales | (57,697) | (57,983) | (56,744)
  ```
  </details>

<details><summary>Gold answer</summary>

0.4%
</details>

## 104. Basing your judgments off of the balance sheet, what is the year end FY2018 amount of accounts payable for MGM Resorts? Answer in USD millions.

`financebench_id_04171` · filing `MGMRESORTS_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The year-end FY2018 accounts payable for MGM Resorts is 302.578 million USD. This figure is derived from the consolidated balance sheet, which reports accounts payable as 302,578 thousand dollars for the year 2018 [v1].

**Computation:** `accounts_payable_2018 = 302.578 million  where accounts_payable_2018 = 302,578 (thousands, FY2018)`

- **v1** · `MGMRESORTS_2018_10K` · PDF page **57** · column 2018 · thousands
  - Quote: "Accounts payable \| $302,578 \| $255,028"

  <details><summary>Passage</summary>

  ```
   | Other intangible assets, net | 3,944,463 | 3,877,960
   | Other long-term assets, net | 455,318 | 430,440
   | Total other assets | 6,954,040 | 7,148,228
   | $30,210,706 | $29,160,042
   | LIABILITIES AND STOCKHOLDERS' EQUITY
  Current liabilities
   | Accounts payable | $302,578 | $255,028
   | Construction payable | 311,793 | 474,807
   | Current portion of long-term debt | 43,411 | 158,042
   | Accrued interest on long-term debt | 140,046 | 135,785
   | Other accrued liabilities | 2,151,054 | 2,114,635
   | Total current liabilities | 2,948,882 | 3,138,297
  Deferred income taxes, net | 1,342,538 | 1,295,375
  ```
  </details>

<details><summary>Gold answer</summary>

$303.00
</details>

## 105. What is the FY2018 - FY2020 3 year average of capex as a % of revenue for MGM Resorts? Answer in units of percents and round to one decimal place. Please utilize information provided primarily within the statement of cash flows and the statement of income.

`financebench_id_03849` · filing `MGMRESORTS_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average of capital expenditures as a percentage of revenue for MGM Resorts from FY2018 to FY2020 is 7.9%. This figure is calculated using the capital expenditures of (1,486,843), (739,006), and (270,579) thousands and revenues of 11,763,096, 12,899,672, and 5,162,082 thousands for the respective years [v1, v2, v3, v4, v5, v6]. The computed result confirms this average is 7.9% [COMPUTED RESULT].

**Computation:** `avg(abs(capex_2018)/revenue_2018, abs(capex_2019)/revenue_2019, abs(capex_2020)/revenue_2020) = 7.9%  where capex_2018 = (1,486,843) (thousands, FY2018), capex_2019 = (739,006) (thousands, FY2019), capex_2020 = (270,579) (thousands, FY2020), revenue_2018 = 11,763,096 (thousands, FY2018), revenue_2019 = 12,899,672 (thousands, FY2019), revenue_2020 = 5,162,082 (thousands, FY2020)`

- **v1** · `MGMRESORTS_2020_10K` · PDF page **67** · column 2018 · thousands
  - Quote: "Capital expenditures, net of construction payable \| (1,486,843)"

  <details><summary>Passage</summary>

  ```
   | Income taxes receivable and payable, net | (216,250) | 1,259 | 14,120
   | Prepaid expenses and other | (37) | 7,567 | (8,656)
   | Accounts payable and accrued liabilities | (1,382,980) | 465,602 | 21,508
   | Other | (48,750) | (35,909) | (34,505)
   | Net cash provided by (used in) operating activities | (1,493,043) | 1,810,401 | 1,722,539
  Cash flows from investing activities
   | Capital expenditures, net of construction payable | (270,579) | (739,006) | (1,486,843)
   | Dispositions of property and equipment | 6,136 | 2,578 | 25,612
   | Proceeds from Mandalay Bay and MGM Grand Las Vegas transaction | 2,455,839 | — | —
   | Proceeds from Bellagio transaction | — | 4,151,499 | —
   | Proceeds from sale of Circus Circus Las Vegas and adjacent land | — | 652,333 | —
   | Proceeds from sale of business units and investment in unconsolidated affiliate | — | — | 163,616
   | Acquisition of Northfield, net of cash acquired | — | — | (1,034,534)
  ```
  </details>

- **v2** · `MGMRESORTS_2020_10K` · PDF page **67** · column 2019 · thousands
  - Quote: "Capital expenditures, net of construction payable \| (739,006)"

  <details><summary>Passage</summary>

  ```
   | Income taxes receivable and payable, net | (216,250) | 1,259 | 14,120
   | Prepaid expenses and other | (37) | 7,567 | (8,656)
   | Accounts payable and accrued liabilities | (1,382,980) | 465,602 | 21,508
   | Other | (48,750) | (35,909) | (34,505)
   | Net cash provided by (used in) operating activities | (1,493,043) | 1,810,401 | 1,722,539
  Cash flows from investing activities
   | Capital expenditures, net of construction payable | (270,579) | (739,006) | (1,486,843)
   | Dispositions of property and equipment | 6,136 | 2,578 | 25,612
   | Proceeds from Mandalay Bay and MGM Grand Las Vegas transaction | 2,455,839 | — | —
   | Proceeds from Bellagio transaction | — | 4,151,499 | —
   | Proceeds from sale of Circus Circus Las Vegas and adjacent land | — | 652,333 | —
   | Proceeds from sale of business units and investment in unconsolidated affiliate | — | — | 163,616
   | Acquisition of Northfield, net of cash acquired | — | — | (1,034,534)
  ```
  </details>

- **v3** · `MGMRESORTS_2020_10K` · PDF page **67** · column 2020 · thousands
  - Quote: "Capital expenditures, net of construction payable \| (270,579)"

  <details><summary>Passage</summary>

  ```
   | Income taxes receivable and payable, net | (216,250) | 1,259 | 14,120
   | Prepaid expenses and other | (37) | 7,567 | (8,656)
   | Accounts payable and accrued liabilities | (1,382,980) | 465,602 | 21,508
   | Other | (48,750) | (35,909) | (34,505)
   | Net cash provided by (used in) operating activities | (1,493,043) | 1,810,401 | 1,722,539
  Cash flows from investing activities
   | Capital expenditures, net of construction payable | (270,579) | (739,006) | (1,486,843)
   | Dispositions of property and equipment | 6,136 | 2,578 | 25,612
   | Proceeds from Mandalay Bay and MGM Grand Las Vegas transaction | 2,455,839 | — | —
   | Proceeds from Bellagio transaction | — | 4,151,499 | —
   | Proceeds from sale of Circus Circus Las Vegas and adjacent land | — | 652,333 | —
   | Proceeds from sale of business units and investment in unconsolidated affiliate | — | — | 163,616
   | Acquisition of Northfield, net of cash acquired | — | — | (1,034,534)
  ```
  </details>

- **v4** · `MGMRESORTS_2020_10K` · PDF page **65** · column 2018 · thousands
  - Quote: "5,162,082 \| 12,899,672 \| 11,763,096"

  <details><summary>Passage</summary>

  ```
  Revenues
   | Casino | $2,871,720 | $6,517,759 | $5,753,150
    Rooms | 830,382 | 2,322,579 | 2,212,573
   | Food and beverage | 696,040 | 2,145,247 | 1,959,021
   | Entertainment, retail and other | 518,991 | 1,477,200 | 1,412,860
   | Reimbursed costs | 244,949 | 436,887 | 425,492
   | 5,162,082 | 12,899,672 | 11,763,096
  Expenses
   | Casino | 1,701,783 | 3,623,899 | 3,199,775
    Rooms | 419,156 | 829,677 | 791,761
   | Food and beverage | 674,118 | 1,661,626 | 1,501,868
   | Entertainment, retail and other | 412,705 | 1,051,400 | 999,979
   | Reimbursed costs | 244,949 | 436,887 | 425,492
  ```
  </details>

- **v5** · `MGMRESORTS_2020_10K` · PDF page **65** · column 2019 · thousands
  - Quote: "5,162,082 \| 12,899,672 \| 11,763,096"

  <details><summary>Passage</summary>

  ```
  Revenues
   | Casino | $2,871,720 | $6,517,759 | $5,753,150
    Rooms | 830,382 | 2,322,579 | 2,212,573
   | Food and beverage | 696,040 | 2,145,247 | 1,959,021
   | Entertainment, retail and other | 518,991 | 1,477,200 | 1,412,860
   | Reimbursed costs | 244,949 | 436,887 | 425,492
   | 5,162,082 | 12,899,672 | 11,763,096
  Expenses
   | Casino | 1,701,783 | 3,623,899 | 3,199,775
    Rooms | 419,156 | 829,677 | 791,761
   | Food and beverage | 674,118 | 1,661,626 | 1,501,868
   | Entertainment, retail and other | 412,705 | 1,051,400 | 999,979
   | Reimbursed costs | 244,949 | 436,887 | 425,492
  ```
  </details>

- **v6** · `MGMRESORTS_2020_10K` · PDF page **65** · column 2020 · thousands
  - Quote: "5,162,082 \| 12,899,672 \| 11,763,096"

  <details><summary>Passage</summary>

  ```
  Revenues
   | Casino | $2,871,720 | $6,517,759 | $5,753,150
    Rooms | 830,382 | 2,322,579 | 2,212,573
   | Food and beverage | 696,040 | 2,145,247 | 1,959,021
   | Entertainment, retail and other | 518,991 | 1,477,200 | 1,412,860
   | Reimbursed costs | 244,949 | 436,887 | 425,492
   | 5,162,082 | 12,899,672 | 11,763,096
  Expenses
   | Casino | 1,701,783 | 3,623,899 | 3,199,775
    Rooms | 419,156 | 829,677 | 791,761
   | Food and beverage | 674,118 | 1,661,626 | 1,501,868
   | Entertainment, retail and other | 412,705 | 1,051,400 | 999,979
   | Reimbursed costs | 244,949 | 436,887 | 425,492
  ```
  </details>

<details><summary>Gold answer</summary>

7.9%
</details>

## 106. Has MGM Resorts paid dividends to common shareholders in FY2022?

`financebench_id_01254` · filing `MGMRESORTS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, MGM Resorts paid dividends to common shareholders in FY2022, totaling $4 million [v1, v2]. The company made four quarterly payments of $0.0025 per share in March, June, September, and December 2022 [v2]. The consolidated statement of cash flows confirms a cash outflow of $4,048 thousand for these dividends [v1].

- **v1** · `MGMRESORTS_2022_10K` · PDF page **62** · column 2022 · thousands
  - Quote: "Dividends paid to common shareholders \| (4,048)"

  <details><summary>Passage</summary>

  ```
   | Net borrowings (repayments) under bank credit facilities – maturities of 90 days or less | 1,148,276 | (2,096,217) | (1,595,089)
   | Issuance of long-term debt | — | 749,775 | 3,550,000
   | Repayment of long-term debt | (1,070,340) | — | (846,815)
   | Debt issuance costs | (1,367) | (18,726) | (62,348)
   | Proceeds from issuance of bridge loan facility | — | — | 1,304,625
   | Issuance of MGM Growth Properties Class A shares, net | — | 792,851 | 524,704
   | Dividends paid to common shareholders | (4,048) | (4,789) | (77,606)
   | Distributions to noncontrolling interest owners | (210,699) | (324,190) | (286,385)
   | Repurchases of common stock | (2,775,217) | (1,753,509) | (353,720)
   | Other | (110,907) | (159,290) | (53,939)
   | Net cash provided by (used in) financing activities | (3,024,302) | (2,814,095) | 2,103,427
  Effect of exchange rate on cash, cash equivalents, and restricted cash | 8,926 | (1,551) | 2,345
  Change in cash and cash equivalents classified as assets held for sale | (25,938) | — | —
  ```
  </details>

- **v2** · `MGMRESORTS_2022_10K` · PDF page **47** · column text · units
  - Quote: "In March 2022, June 2022, September 2022, and December 2022, we paid dividends of $0.0025 per share, totaling $4 million for 2022."

  <details><summary>Passage</summary>

  ```
   | Dividends, Distributions to Noncontrolling Interest Owners and Share Repurchases
   | In 2022, we repurchased and retired $2.8 billion of our common stock pursuant to our stock repurchase plans. In connection with those repurchases, the
  February 2020 $3.0 billion stock repurchase plan was completed. As of December 31, 2022, the remaining availability under the March 2022 $2.0 billion stock
  repurchase plan was $475 million. Additionally, in February 2023, we announced that the Board of Directors authorized a $2.0 billion stock repurchase plan. In
  2021, we repurchased and retired $1.8 billion of our common stock pursuant to our May 2018 $2.0 billion and February 2020 $3.0 billion stock repurchase
  plans. In connection with those repurchases, we completed our May 2018 $2.0 billion stock repurchase plan.
   | In March 2022, June 2022, September 2022, and December 2022, we paid dividends of $0.0025 per share, totaling $4 million for 2022. In March 2021,
  June 2021, September 2021, and December 2021, we paid dividends of $0.0025 per share, totaling $5 million for 2021.
   | 45
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. MGM maintained 0.01$ per share annual dividend through out FY 2022.
</details>

## 107. Which region had the Highest EBITDAR Contribution for MGM during FY2022?

`financebench_id_00382` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The region with the highest EBITDAR contribution for MGM during FY2022 was Las Vegas Strip Resorts, with $3,142,308 thousand [v1]. This amount exceeded the contributions from Regional Operations ($1,294,630 thousand) and MGM China, which reported a loss of $(203,136) thousand [v2, v3].

- **v1** · `MGMRESORTS_2022Q4_EARNINGS` · PDF page **13** · column Twelve months ended December 31, 2022 · thousands
  - Quote: "Las Vegas Strip Resorts \| $3,142,308"

  <details><summary>Passage</summary>

  ```
   | SUPPLEMENTAL DATA – NET REVENUES
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
  ```
  </details>

- **v2** · `MGMRESORTS_2022Q4_EARNINGS` · PDF page **13** · column Twelve months ended December 31, 2022 · thousands
  - Quote: "Regional Operations \| 1,294,630"

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

- **v3** · `MGMRESORTS_2022Q4_EARNINGS` · PDF page **13** · column Twelve months ended December 31, 2022 · thousands
  - Quote: "MGM China \| (203,136)"

  <details><summary>Passage</summary>

  ```
  | MGM RESORTS INTERNATIONAL AND SUBSIDIARIES
   | SUPPLEMENTAL DATA – NET REVENUES
   | (In thousands)
   | (Unaudited)
   | Three months ended | Twelve months ended
   | December 31, | December 31, | December 31, | December 31,
   | 2022 | 2021 | 2022 | 2021
  ```
  </details>

<details><summary>Gold answer</summary>

Las Vegas resorts contributed ~90% of company level EBITDAR during FY2022.
</details>

## 108. What was MGM's interest coverage ratio using FY2022 Adjusted EBIT as the numerator and annual Interest Expense as the denominator?

`financebench_id_01911` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MGMRESORTS_2022Q4_EARNINGS: extractor: The filing provides 'Adjusted EBITDAR' (Earnings Before Interest, Taxes, Depreciation, Amortization, and Rent) but does not provide a value for 'Adjusted EBIT' (Earnings Before Interest and Taxes). The definition of Adjusted EBITDAR on Page 7 explicitly states it excludes rent expense, which is a significant component not excluded in standard EBIT. Without a specific 'Adjusted EBIT' figure or the necessary components to derive it (specifically the rent expense to be added back to EBIT or subtracted from EBITDAR to get EBIT), the requested metric cannot be calculated using ONLY the provided pages.

**Pages searched:** `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 3, 4, 6, 7, 9, 11, 12, 13, 14, 15

<details><summary>Gold answer</summary>

As adjusted EBIT is negative, coverage ratio is zero
</details>

## 109. Which region had the worst topline performance for MGM during FY2022?

`financebench_id_01912` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MGMRESORTS_2022Q4_EARNINGS: code checks failed twice: formula: unknown value name 'las_vegas_strip_revenues_2021' (names: [])

**Pages searched:** `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15

<details><summary>Gold answer</summary>

MGM China experienced the worst topline performance amongst the other regions presented. Its revenue declined 44% in FY2022 whereas the other regions presented increased their revenues.
</details>

## 110. Which type of debt received the largest investment among the short term investments for MGM in H1 FY2023?

`financebench_id_00407` · filing `MGMRESORTS_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MGMRESORTS_2023Q2_10Q: extractor: The question asks for the 'largest investment' among short-term investments. The provided pages (specifically Page 11) list the fair value of short-term investments by type as of June 30, 2023. However, the question asks for the 'largest investment' which implies a flow (amount invested during the period) rather than a stock (balance at a point in time). The Statement of Cash Flows (Page 6) shows 'Investments and other' as a net figure of (216,485) but does not break down the specific types of debt investments made during H1 2023. The table on Page 11 only provides the ending balance, not the investment activity during the period. Therefore, the specific 'investment' amount for each type during H1 2023 cannot be determined from the provided pages.

**Pages searched:** `MGMRESORTS_2023Q2_10Q` pages 3, 4, 5, 6, 7, 8, 11, 18, 19, 36, 37, 38

<details><summary>Gold answer</summary>

the biggest short term investment is in corporate bonds (almost 82% of the total investment)
</details>

## 111. What is the FY2016 COGS for Microsoft? Please state answer in USD millions. Provide a response to the question by primarily using the statement of income.

`financebench_id_04700` · filing `MICROSOFT_2016_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2016 Cost of Goods Sold (COGS) for Microsoft is 32,780 million USD. This figure is reported as the "Total cost of revenue" in the company's 2016 Income Statement [v1]. The value is derived from the sum of product and service costs listed on page 52 of the filing [v1].

**Computation:** `cogs_2016 = 32,780 million  where cogs_2016 = 32,780 (millions, FY2016)`

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

<details><summary>Gold answer</summary>

$32780.00
</details>

## 112. Has Microsoft increased its debt on balance sheet between FY2023 and the FY2022 period?

`financebench_id_00552` · filing `MICROSOFT_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MICROSOFT_2023_10K: number check (G4) failed twice: numbers not in the evidence or the result: 2023,

**Pages searched:** `MICROSOFT_2023_10K` pages 7, 44, 58, 59, 60, 61, 62, 63, 87, 89, 91, 102

<details><summary>Gold answer</summary>

No. Microsoft decreased its debt by $2.5bn in FY 2023 vs FY 2022.
</details>

## 113. We want to calculate a financial metric. Please help us compute it by basing your answers off of the statement of income and the statement of cash flows. Here's the question: what is the FY2015 unadjusted EBITDA % margin for Netflix? Calculate unadjusted EBITDA using unadjusted operating income and D&A (from cash flow statement).

`financebench_id_04458` · filing `NETFLIX_2015_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 unadjusted EBITDA % margin for Netflix is 5.43%. This result is computed by adding the operating income of 305,826 (thousands) [v1] and depreciation and amortization of 62,283 (thousands) [v2], then dividing by the total revenues of $6,779,511 (thousands) [v3].

**Computation:** `(operating_income_2015 + d_and_a_2015) / revenues_2015 = 5.43%  where operating_income_2015 = 305,826 (thousands, FY2015), d_and_a_2015 = 62,283 (thousands, FY2015), revenues_2015 = $6,779,511 (thousands, FY2015)`

- **v1** · `NETFLIX_2015_10K` · PDF page **40** · column 2015 · thousands
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

- **v2** · `NETFLIX_2015_10K` · PDF page **42** · column 2015 · thousands
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

- **v3** · `NETFLIX_2015_10K` · PDF page **40** · column 2015 · thousands
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Netflix's year-end FY2017 total current liabilities were 5,466.312 million USD. This figure is derived from the Consolidated Balance Sheets, which report total current liabilities as 5,466,312 in thousands for the year 2017 [v1]. The computed result confirms this value as 5,466.312 million [COMPUTED RESULT].

**Computation:** `total_current_liabilities_2017 = 5,466.312 million  where total_current_liabilities_2017 = 5,466,312 (thousands, FY2017)`

- **v1** · `NETFLIX_2017_10K` · PDF page **45** · column 2017 · thousands
  - Quote: "Total current liabilities \| 5,466,312 \| 4,586,657"

  <details><summary>Passage</summary>

  ```
  Liabilities and Stockholders’ Equity
  Current liabilities:
   | Current content liabilities | $4,173,041 | $3,632,711
   | Accounts payable | 359,555 | 312,842
   | Accrued expenses | 315,094 | 197,632
   | Deferred revenue | 618,622 | 443,472
   | Total current liabilities | 5,466,312 | 4,586,657
  Non-current content liabilities | 3,329,796 | 2,894,654
  Long-term debt | 6,499,432 | 3,364,311
  Other non-current liabilities | 135,246 | 61,188
   | Total liabilities | 15,430,786 | 10,906,810
  Commitments and contingencies (Note 5)
  Stockholders’ equity:
  ```
  </details>

<details><summary>Gold answer</summary>

$5466.00
</details>

## 115. We need to calculate a reasonable approximation (or exact number if possible) of a financial metric. Basing your judgment by information plainly provided in the statement of income, what is Nike's three year average of cost of goods sold as a % of revenue from FY2016 to FY2018? Answer in units of percents and round to one decimal place.

`financebench_id_04302` · filing `NIKE_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Nike's three-year average cost of goods sold as a percentage of revenue from FY2016 to FY2018 is 55.1%. This result is derived from the cost of sales and revenues for the three fiscal years provided in the evidence [v1, v2, v3, v4, v5, v6]. The system computed this average directly as 55.1% [COMPUTED RESULT].

**Computation:** `avg(cost_of_sales_2016 / revenues_2016, cost_of_sales_2017 / revenues_2017, cost_of_sales_2018 / revenues_2018) = 55.1%  where cost_of_sales_2016 = 17,405 (millions, FY2016), revenues_2016 = 32,376 (millions, FY2016), cost_of_sales_2017 = 19,038 (millions, FY2017), revenues_2017 = 34,350 (millions, FY2017), cost_of_sales_2018 = 20,441 (millions, FY2018), revenues_2018 = 36,397 (millions, FY2018)`

- **v1** · `NIKE_2018_10K` · PDF page **46** · column 2016 · millions
  - Quote: "Cost of sales \| 17,405"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, Inc. Consolidated Statements of Income
   | Year Ended May 31,
  (In millions, except per share data) | 2018 | 2017 | 2016
  Revenues | $36,397 | $34,350 | $32,376
  Cost of sales | 20,441 | 19,038 | 17,405
  Gross profit | 15,956 | 15,312 | 14,971
  Demand creation expense | 3,577 | 3,341 | 3,278
  Operating overhead expense | 7,934 | 7,222 | 7,191
  Total selling and administrative expense | 11,511 | 10,563 | 10,469
  Interest expense (income), net | 54 | 59 | 19
  Other expense (income), net | 66 | (196) | (140)
  ```
  </details>

- **v2** · `NIKE_2018_10K` · PDF page **46** · column 2016 · millions
  - Quote: "Revenues \| $32,376"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, Inc. Consolidated Statements of Income
   | Year Ended May 31,
  (In millions, except per share data) | 2018 | 2017 | 2016
  Revenues | $36,397 | $34,350 | $32,376
  Cost of sales | 20,441 | 19,038 | 17,405
  Gross profit | 15,956 | 15,312 | 14,971
  Demand creation expense | 3,577 | 3,341 | 3,278
  Operating overhead expense | 7,934 | 7,222 | 7,191
  Total selling and administrative expense | 11,511 | 10,563 | 10,469
  Interest expense (income), net | 54 | 59 | 19
  ```
  </details>

- **v3** · `NIKE_2018_10K` · PDF page **46** · column 2017 · millions
  - Quote: "Cost of sales \| 19,038"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, Inc. Consolidated Statements of Income
   | Year Ended May 31,
  (In millions, except per share data) | 2018 | 2017 | 2016
  Revenues | $36,397 | $34,350 | $32,376
  Cost of sales | 20,441 | 19,038 | 17,405
  Gross profit | 15,956 | 15,312 | 14,971
  Demand creation expense | 3,577 | 3,341 | 3,278
  Operating overhead expense | 7,934 | 7,222 | 7,191
  Total selling and administrative expense | 11,511 | 10,563 | 10,469
  Interest expense (income), net | 54 | 59 | 19
  Other expense (income), net | 66 | (196) | (140)
  ```
  </details>

- **v4** · `NIKE_2018_10K` · PDF page **46** · column 2017 · millions
  - Quote: "Revenues \| $34,350"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, Inc. Consolidated Statements of Income
   | Year Ended May 31,
  (In millions, except per share data) | 2018 | 2017 | 2016
  Revenues | $36,397 | $34,350 | $32,376
  Cost of sales | 20,441 | 19,038 | 17,405
  Gross profit | 15,956 | 15,312 | 14,971
  Demand creation expense | 3,577 | 3,341 | 3,278
  Operating overhead expense | 7,934 | 7,222 | 7,191
  Total selling and administrative expense | 11,511 | 10,563 | 10,469
  Interest expense (income), net | 54 | 59 | 19
  ```
  </details>

- **v5** · `NIKE_2018_10K` · PDF page **46** · column 2018 · millions
  - Quote: "Cost of sales \| 20,441"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, Inc. Consolidated Statements of Income
   | Year Ended May 31,
  (In millions, except per share data) | 2018 | 2017 | 2016
  Revenues | $36,397 | $34,350 | $32,376
  Cost of sales | 20,441 | 19,038 | 17,405
  Gross profit | 15,956 | 15,312 | 14,971
  Demand creation expense | 3,577 | 3,341 | 3,278
  Operating overhead expense | 7,934 | 7,222 | 7,191
  Total selling and administrative expense | 11,511 | 10,563 | 10,469
  Interest expense (income), net | 54 | 59 | 19
  Other expense (income), net | 66 | (196) | (140)
  ```
  </details>

- **v6** · `NIKE_2018_10K` · PDF page **46** · column 2018 · millions
  - Quote: "Revenues \| $36,397"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NIKE, Inc. Consolidated Statements of Income
   | Year Ended May 31,
  (In millions, except per share data) | 2018 | 2017 | 2016
  Revenues | $36,397 | $34,350 | $32,376
  Cost of sales | 20,441 | 19,038 | 17,405
  Gross profit | 15,956 | 15,312 | 14,971
  Demand creation expense | 3,577 | 3,341 | 3,278
  Operating overhead expense | 7,934 | 7,222 | 7,191
  Total selling and administrative expense | 11,511 | 10,563 | 10,469
  Interest expense (income), net | 54 | 59 | 19
  ```
  </details>

<details><summary>Gold answer</summary>

55.1%
</details>

## 116. According to the details clearly outlined within the balance sheet, how much total current assets did Nike have at the end of FY2019? Answer in USD millions.

`financebench_id_03531` · filing `NIKE_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Nike had total current assets of 16,525 million USD at the end of FY2019 [v1]. This figure is explicitly listed in the Consolidated Balance Sheets under the "Total current assets" row for the year 2019 [v1].

**Computation:** `total_current_assets_2019 = 16,525 million  where total_current_assets_2019 = 16,525 (millions, FY2019)`

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

<details><summary>Gold answer</summary>

$16525.00
</details>

## 117. When primarily referencing the income statement and the statement of financial position, what is the FY2021 inventory turnover ratio for Nike? Inventory turnover ratio is defined as: (FY2021 COGS) / (average inventory between FY2020 and FY2021). Round your answer to two decimal places.

`financebench_id_04080` · filing `NIKE_2021_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2021 inventory turnover ratio for Nike is 3.46. This result is calculated by dividing the 2021 cost of sales of $24,576 million by the average of the 2021 and 2020 inventories ($6,854 million and $7,367 million, respectively) [v1, v2, v3]. The computed value of 3.46 is derived directly from these figures [COMPUTED RESULT].

**Computation:** `cost_of_sales_2021 / avg(inventories_2021, inventories_2020) = 3.46  where cost_of_sales_2021 = 24,576 (millions, FY2021), inventories_2021 = 6,854 (millions, FY2021), inventories_2020 = 7,367 (millions, FY2020)`

- **v1** · `NIKE_2021_10K` · PDF page **59** · column 2021 · millions
  - Quote: "Cost of sales \| 24,576"

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

- **v2** · `NIKE_2021_10K` · PDF page **61** · column 2021 · millions
  - Quote: "Inventories \| 6,854"

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

- **v3** · `NIKE_2021_10K` · PDF page **61** · column 2020 · millions
  - Quote: "Inventories \| 7,367"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Operations activities brought in the most cash flow for Nike in FY2023 with $5,841 million [v1]. This amount is higher than the $564 million from investing activities [v2] and the $(7,447) million used by financing activities [v3]. The computed maximum of these three values confirms that operations generated the highest cash flow at 5,841 million [COMPUTED RESULT].

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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, PayPal has positive working capital based on FY2022 data. The company's total current assets of $57,517 million exceeded its total current liabilities of $45,101 million, resulting in a computed working capital of $12,416 million [v1, v2]. This metric is relevant for PayPal as it reflects the company's short-term liquidity position derived from its balance sheet items.

**Computation:** `total_current_assets_2022 - total_current_liabilities_2022 = 12,416 million  where total_current_assets_2022 = 57,517 (millions, FY2022), total_current_liabilities_2022 = 45,101 (millions, FY2022)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** PepsiCo's capital expenditure for fiscal year 2021 was 4.62 billion USD. This figure is derived from the absolute value of the capital spending reported as (4,625) million in the Consolidated Statement of Cash Flows [v1]. The computed result confirms this amount as 4.62 billion [COMPUTED RESULT].

**Computation:** `abs(capital_spending_2021) = 4.62 billion  where capital_spending_2021 = (4,625) (millions, FY2021)`

- **v1** · `PEPSICO_2021_10K` · PDF page **63** · column 2021 · millions
  - Quote: "Capital spending \| (4,625)"

  <details><summary>Passage</summary>

  ```
   | Prepaid expenses and other current assets | 159 | 26 | (87)
    Accounts payable and other current liabilities | 1,762 | 766 | 735
    Income taxes payable | 30 | (159) | (287)
  Other, net | 375 | 164 | (196)
  Net Cash Provided by Operating Activities | 11,616 | 10,613 | 9,649
  Investing Activities
  Capital spending | (4,625) | (4,240) | (4,232)
  Sales of property, plant and equipment | 166 | 55 | 170
  Acquisitions, net of cash acquired, and investments in noncontrolled affiliates | (61) | (6,372) | (2,717)
  Divestitures and sales of investments in noncontrolled affiliates | 169 | 6 | 253
  Short-term investments, by original maturity:
    More than three months - purchases | — | (1,135) | —
    More than three months - maturities | 1,135 | — | 16
  ```
  </details>

<details><summary>Gold answer</summary>

$4.60
</details>

## 121. What are the geographies that Pepsico primarily operates in as of FY2022?

`financebench_id_01009` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** PepsiCo primarily operates in seven geographies as of FY2022: Frito-Lay North America, Quaker Foods North America, PepsiCo Beverages North America, Latin America, Europe, Africa, Middle East and South Asia, and Asia Pacific, Australia and New Zealand and China Region [v1, v2, v3, v4, v5, v6, v7]. These segments are explicitly listed in the company's 2022 10K filing as the distinct operating units for its beverage and convenient food businesses [v1, v2, v3, v4, v5, v6, v7].

- **v1** · `PEPSICO_2022_10K` · PDF page **5** · column N/A · units
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

- **v2** · `PEPSICO_2022_10K` · PDF page **5** · column N/A · units
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

- **v3** · `PEPSICO_2022_10K` · PDF page **5** · column N/A · units
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

- **v4** · `PEPSICO_2022_10K` · PDF page **5** · column N/A · units
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

- **v5** · `PEPSICO_2022_10K` · PDF page **6** · column N/A · units
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

- **v6** · `PEPSICO_2022_10K` · PDF page **6** · column N/A · units
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

- **v7** · `PEPSICO_2022_10K` · PDF page **6** · column N/A · units
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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2022_10K: extractor: The provided pages include a Table of Contents reference to 'Item 3. Legal Proceedings' on page 24, but the actual content of Item 3 (pages 24-25) is not included in the provided pages. Therefore, no evidence regarding specific legal battles for FY2022 or FY2021 can be extracted from the given text.

**Pages searched:** `PEPSICO_2022_10K` pages 2, 3, 4, 62, 63, 64, 65, 66, 67, 68, 99, 110

<details><summary>Gold answer</summary>

No, Pepsico is not involved in material legal battles.
</details>

## 123. What is the quantity of restructuring costs directly outlined in Pepsico's income statements for FY2022? If restructuring costs are not explicitly outlined then state 0.

`financebench_id_01328` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2022_10K: code checks failed twice: restructuring_costs_2022: the quote is not on page 62. Copy it exactly from one line of the page; no value passed the checks; give exact quotes, or answer not_found

**Pages searched:** `PEPSICO_2022_10K` pages 31, 46, 49, 62, 63, 64, 65, 66, 67, 68, 79, 110

<details><summary>Gold answer</summary>

Pepsico's restructuring costs in FY2022 amounted to $411 million .
</details>

## 124. What is the FY2022 unadjusted EBITDA less capex for PepsiCo? Define unadjusted EBITDA as unadjusted operating income + depreciation and amortization [from cash flow statement]. Answer in USD millions. Respond to the question by assuming the perspective of an investment analyst who can only use the details shown within the statement of cash flows and the income statement.

`financebench_id_03620` · filing `PEPSICO_2022_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2022_10K: code checks failed twice: formula: unknown value name 'operating_profit_2022' (names: [])

**Pages searched:** `PEPSICO_2022_10K` pages 47, 53, 62, 63, 64, 65, 66, 67, 103, 104, 110, 121

<details><summary>Gold answer</summary>

$9068.00
</details>

## 125. What is the FY2022 unadjusted EBITDA % margin for PepsiCo? Calculate unadjusted EBITDA using unadjusted operating income and D&A (from cash flow statement). Give a response to the question by relying on the details shown in the statement of cash flows and the P&L statement.

`financebench_id_04481` · filing `PEPSICO_2022_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2022 unadjusted EBITDA margin for PepsiCo is 16.5%. This is calculated by adding the operating profit of $11,512 million [v1] and depreciation and amortization of $2,763 million [v2], then dividing by the net revenue of $86,392 million [v3]. The resulting ratio of 16.5% represents the unadjusted EBITDA as a percentage of net revenue for the fiscal year.

**Computation:** `(operating_profit_2022 + depreciation_amortization_2022) / net_revenue_2022 = 16.5%  where operating_profit_2022 = 11,512 (millions, FY2022), depreciation_amortization_2022 = 2,763 (millions, FY2022), net_revenue_2022 = $86,392 (millions, FY2022)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The shareholder proposal for a congruency report on net-zero emissions policies was defeated [v1]. The vote resulted in 19,718,780 votes in favor, 977,228,788 votes against, and 23,200,321 abstentions [v2, v3, v4].

- **v1** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column N/A · units
  - Quote: "(8) The shareholder proposal regarding a congruency report on net-zero emissions policies was defeated:"

  <details><summary>Passage</summary>

  ```
  Broker Non-Votes | 172,969,325
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

- **v2** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column For · units
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

- **v3** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column Against · units
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

- **v4** · `PEPSICO_2023_8K_dated-2023-05-05` · PDF page **4** · column Abstain · units
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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** PepsiCo increased its unsecured five-year revolving credit agreement by $400,000,000 on May 26, 2023. This increase reflects the difference between the new agreement amount of $4,200,000,000 and the terminated old agreement amount of $3,800,000,000 [v1, v2].

**Computation:** `new_agreement_amount - old_agreement_amount = 400,000,000  where old_agreement_amount = $3,800,000,000 (units, FY2023), new_agreement_amount = $4,200,000,000 (units, FY2023)`

- **v1** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column N/A · units
  - Quote: "$3,800,000,000 five year unsecured revolving credit agreement"

  <details><summary>Passage</summary>

  ```
  certain conditions stated in the 2023 364 Day Credit Agreement, PepsiCo and its borrowing subsidiaries may borrow, prepay and reborrow amounts under
  the 2023 364 Day Credit Agreement at any time during the term of the 2023 364 Day Credit Agreement. Funds borrowed under the 2023 364 Day Credit
  Agreement may be used for general corporate purposes of PepsiCo and its subsidiaries. The 2023 364 Day Credit Agreement contains customary
  representations and warranties and events of default. In the ordinary course of their respective businesses, the lenders under the 2023 364 Day Credit
  Agreement and their affiliates have engaged, and may in the future engage, in commercial banking and/or investment banking transactions with PepsiCo
  and its affiliates.
   | Effective May 26, 2023, PepsiCo terminated the $3,800,000,000 five year unsecured revolving credit agreement, dated as of May 27, 2022, among
  PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent (the “2022 Five Year Credit Agreement”). There were no
  outstanding borrowings under the 2022 Five Year Credit Agreement at the time of its termination.
   | On May 26, 2023, PepsiCo entered into a new $4,200,000,000 five year unsecured revolving credit agreement (the “2023 Five Year Credit
  Agreement”) among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent. The 2023 Five Year Credit Agreement
  enables PepsiCo and its borrowing subsidiaries to borrow up to $4,200,000,000 in U.S. Dollars and/or Euros, including a $750,000,000 swing line
  subfacility for Euro-denominated borrowings permitted to be borrowed on a same day basis, subject to customary terms and conditions, and expires on
  ```
  </details>

- **v2** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column N/A · units
  - Quote: "$4,200,000,000 five year unsecured revolving credit agreement"

  <details><summary>Passage</summary>

  ```
  representations and warranties and events of default. In the ordinary course of their respective businesses, the lenders under the 2023 364 Day Credit
  Agreement and their affiliates have engaged, and may in the future engage, in commercial banking and/or investment banking transactions with PepsiCo
  and its affiliates.
   | Effective May 26, 2023, PepsiCo terminated the $3,800,000,000 five year unsecured revolving credit agreement, dated as of May 27, 2022, among
  PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent (the “2022 Five Year Credit Agreement”). There were no
  outstanding borrowings under the 2022 Five Year Credit Agreement at the time of its termination.
   | On May 26, 2023, PepsiCo entered into a new $4,200,000,000 five year unsecured revolving credit agreement (the “2023 Five Year Credit
  Agreement”) among PepsiCo, as borrower, the lenders party thereto, and Citibank, N.A., as administrative agent. The 2023 Five Year Credit Agreement
  enables PepsiCo and its borrowing subsidiaries to borrow up to $4,200,000,000 in U.S. Dollars and/or Euros, including a $750,000,000 swing line
  subfacility for Euro-denominated borrowings permitted to be borrowed on a same day basis, subject to customary terms and conditions, and expires on
  May 26, 2028. PepsiCo may also, upon the agreement of either the then existing lenders or of additional banks not currently party to the 2023 Five Year
  Credit Agreement, increase the commitments under the 2023 Five Year Credit Agreement to up to $4,950,000,000 in U.S. Dollars and/or Euros. PepsiCo
  may, once a year, request renewal of the 2023 Five Year Credit Agreement for an additional one year period. Subject to certain conditions stated in the 2023
  ```
  </details>

<details><summary>Gold answer</summary>

$400,000,000 increase.
</details>

## 128. As of May 26, 2023, what is the total amount Pepsico may borrow under its unsecured revolving credit agreements?

`financebench_id_00882` · filing `PEPSICO_2023_8K_dated-2023-05-30` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** As of May 26, 2023, PepsiCo may borrow a total of $8,400,000,000 under its unsecured revolving credit agreements. This amount is the sum of the new $4,200,000,000 364-day credit agreement and the new $4,200,000,000 five-year credit agreement entered into on that date [v1, v2].

**Computation:** `credit_line_364_day + credit_line_five_year = 8,400,000,000  where credit_line_364_day = $4,200,000,000 (units, FY2023), credit_line_five_year = $4,200,000,000 (units, FY2023)`

- **v1** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column May 26, 2023 · units
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

- **v2** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column May 26, 2023 · units
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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2023Q1_EARNINGS: code checks failed twice: guidance_reason: raw 'Given our strong start to the year, we now expect our full-year 2023 organic revenue to increase 8 percent (previously 6 percent) and core constant currency EPS to increase 9 percent (previously 8百分)' does not appear in its quote

**Pages searched:** `PEPSICO_2023Q1_EARNINGS` pages 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 16

<details><summary>Gold answer</summary>

Pepsico experienced a strong start to FY2023.
</details>

## 130. As of FY2023Q1, by how many percentage points did Pepsico raise full year guidance in respect of core constant currency EPS growth?

`financebench_id_01476` · filing `PEPSICO_2023Q1_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2023Q1_EARNINGS: code checks failed twice: new_guidance: the quote is not on page 3. Copy it exactly from one line of the page; old_guidance: the quote is not on page 3. Copy it exactly from one line of the page; no value passed the checks; give exact quotes, or answer not_found

**Pages searched:** `PEPSICO_2023Q1_EARNINGS` pages 1, 2, 3, 4, 8, 9, 10, 12, 13, 14, 15, 16

<details><summary>Gold answer</summary>

Pepsico raised full year guidance in respect of core constant currency EPS growth by 1 percentage point.
</details>

## 131. Did Pfizer grow its PPNE between FY20 and FY21?

`financebench_id_00302` · filing `PFIZER_2021_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Pfizer grew its Property, Plant, and Equipment (PPNE) between FY2020 and FY2021. The PPNE increased from 13,745 million in 2020 to 14,882 million in 2021 [v1, v2].

- **v1** · `PFIZER_2021_10K` · PDF page **59** · column 2020 · millions
  - Quote: "Property, plant and equipment \| 14,882 \| 13,745"

  <details><summary>Passage</summary>

  ```
  Inventories | 9,059 | 8,020
  Current tax assets | 4,266 | 3,264
  Other current assets | 3,820 | 3,646
   Total current assets | 59,693 | 35,067
  Equity-method investments | 16,472 | 16,856
  Long-term investments | 5,054 | 3,406
  Property, plant and equipment | 14,882 | 13,745
  Identifiable intangible assets | 25,146 | 28,337
  Goodwill | 49,208 | 49,556
  Noncurrent deferred tax assets and other noncurrent tax assets | 3,341 | 2,383
  Other noncurrent assets | 7,679 | 4,879
   Total assets | $181,476  $154,229
  Liabilities and Equity
  ```
  </details>

- **v2** · `PFIZER_2021_10K` · PDF page **59** · column 2021 · millions
  - Quote: "Property, plant and equipment \| 14,882 \| 13,745"

  <details><summary>Passage</summary>

  ```
  Inventories | 9,059 | 8,020
  Current tax assets | 4,266 | 3,264
  Other current assets | 3,820 | 3,646
   Total current assets | 59,693 | 35,067
  Equity-method investments | 16,472 | 16,856
  Long-term investments | 5,054 | 3,406
  Property, plant and equipment | 14,882 | 13,745
  Identifiable intangible assets | 25,146 | 28,337
  Goodwill | 49,208 | 49,556
  Noncurrent deferred tax assets and other noncurrent tax assets | 3,341 | 2,383
  Other noncurrent assets | 7,679 | 4,879
   Total assets | $181,476  $154,229
  Liabilities and Equity
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, change in PPNE was positive year over year
</details>

## 132. Were there any potential events that are not in Pfizer's standard business operations that substantially increased net income in 2019?

`financebench_id_00702` · filing `PFIZER_2021_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PFIZER_2021_10K: code checks failed twice: formula: unknown value name 'gain_consumer_healthcare_jv_2019' (names: [])

**Pages searched:** `PFIZER_2021_10K` pages 44, 57, 58, 59, 60, 61, 63, 81, 82, 100, 106

<details><summary>Gold answer</summary>

Yes, the gain on completion of Consumer Healthcare JV Transaction
</details>

## 133. What are three main companies acquired by Pfizer mentioned in this 10K report?

`financebench_id_02416` · filing `PFIZER_2021_10K` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The three main companies acquired by Pfizer mentioned in this 10K report are Array, Therachon, and Warner-Lambert [v1, v2, v3]. Array was acquired with a portfolio including Braftovi and Mektovi, while Therachon was acquired on July 1, 2019, for rare disease assets [v1, v2]. Warner-Lambert was acquired by Pfizer in 2000 and is noted in the context of asbestos-related legal proceedings [v3].

- **v1** · `PFIZER_2021_10K` · PDF page **71** · column 2019 · units
  - Quote: "Array's portfolio includes Braftovi (encorafenib) and Mektovi (binimetinib)..."

  <details><summary>Passage</summary>

  ```
  Notes to Consolidated Financial Statements
  Pfizer Inc. and Subsidiary Companies
  Array’s portfolio includes Braftovi (encorafenib) and Mektovi (binimetinib), a broad pipeline of targeted cancer medicines in different stages of R&D, as well as a portfolio of out-
  licensed medicines, which may generate milestones and royalties over time.
  The final allocation of the consideration transferred to the assets acquired and the liabilities assumed was completed in 2020. In connection with this acquisition, we recorded: (i) $6.3
  billion in Identifiable intangible assets, consisting of $2.0 billion of Developed technology rights with a useful life of 16 years, $2.8 billion of IPR&D and $1.5 billion of Licensing
  agreements and other ($1.2 billion for technology in development––indefinite-lived licensing agreements and $360 million for developed technology––finite-lived licensing agreements
  with a useful life of 10 years), (ii) $6.1 billion of Goodwill, (iii) $1.1 billion of net deferred tax liabilities and (iv) $451 million of assumed long-term debt, which was paid in full in 2019.
  In 2020, we recorded measurement period adjustments to the estimated fair values initially recorded in 2019, which resulted in a reduction in Identifiable intangible assets of
  ```
  </details>

- **v2** · `PFIZER_2021_10K` · PDF page **71** · column 2019 · units
  - Quote: "On July 1, 2019, we acquired all the remaining shares of Therachon..."

  <details><summary>Passage</summary>

  ```
  with a useful life of 10 years), (ii) $6.1 billion of Goodwill, (iii) $1.1 billion of net deferred tax liabilities and (iv) $451 million of assumed long-term debt, which was paid in full in 2019.
  In 2020, we recorded measurement period adjustments to the estimated fair values initially recorded in 2019, which resulted in a reduction in Identifiable intangible assets of
  approximately $900 million with a corresponding change to Goodwill and net deferred tax liabilities. The measurement period adjustments were recorded to better reflect market
  participant assumptions about facts and circumstances existing as of the acquisition date and did not have a material impact on our consolidated statement of income for the year
  ended December 31, 2020.
  Therachon
  On July 1, 2019, we acquired all the remaining shares of Therachon, a privately-held clinical-stage biotechnology company focused on rare diseases, with assets in development for
  the treatment of achondroplasia, a genetic condition and the most common form of short-limb dwarfism, for $340 million upfront, plus potential milestone payments of up to $470
  million contingent on the achievement of key milestones in the development and commercialization of the lead asset. We accounted for the transaction as an asset acquisition since
  the lead asset represented substantially all the fair value of the gross assets acquired. The total fair value of the consideration transferred for Therachon was $322 million, which
  consisted of $317 million of cash and our previous $5 million investment in Therachon. In connection with this asset acquisition, we recorded a charge of $337 million in Research and
  development expenses.
  B. Divestitures
  ```
  </details>

- **v3** · `PFIZER_2021_10K` · PDF page **102** · column N/A · units
  - Quote: "Warner-Lambert was acquired by Pfizer in 2000..."

  <details><summary>Passage</summary>

  ```
  A2. Legal Proceedings––Product Litigation
  We are defendants in numerous cases, including but not limited to those discussed below, related to our pharmaceutical and other products. Plaintiffs in these cases seek damages
  and other relief on various grounds for alleged personal injury and economic loss.
  Asbestos
  Between 1967 and 1982, Warner-Lambert owned American Optical Corporation (American Optical), which manufactured and sold respiratory protective devices and asbestos safety
  clothing. In connection with the sale of American Optical in 1982, Warner-Lambert agreed to indemnify the purchaser for certain liabilities, including certain asbestos-related and other
  claims. Warner-Lambert was acquired by Pfizer in 2000 and is a wholly owned subsidiary of Pfizer. Warner-Lambert is actively engaged in the defense of, and will continue to explore
  various means of resolving, these claims.
  Numerous lawsuits against American Optical, Pfizer and certain of its previously owned subsidiaries are pending in various federal and state courts seeking damages for alleged
  personal injury from exposure to products allegedly containing asbestos and other allegedly hazardous materials sold by Pfizer and certain of its previously owned subsidiaries.
  There also are a small number of lawsuits pending in various federal and state courts seeking damages for alleged exposure to asbestos in facilities owned or formerly owned by
  Pfizer or its subsidiaries.
  Effexor
  ```
  </details>

<details><summary>Gold answer</summary>

Trillium, Array, and Therachon
</details>

## 134. How much does Pfizer expect to pay to spin off Upjohn in the future in USD million?

`financebench_id_00283` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** Pfizer_2023Q2_10Q: code checks failed twice: formula: unknown value name 'total_expected_cost' (names: ['cost_incurred_to_date_pct'])

**Pages searched:** `Pfizer_2023Q2_10Q` pages 8, 9, 10, 11, 14, 16, 26, 34, 37, 38, 41, 45

<details><summary>Gold answer</summary>

77.78
</details>

## 135. For Pfizer, which geographic region had the biggest drop in Q22023 year over year revenues (on a percentage basis)?

`financebench_id_00724` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The geographic region with the biggest drop in Q2 2023 year-over-year revenues was Developed Rest of World, with a decline of 74.08% [v5, v6]. This is confirmed by the computed maximum percentage change across all regions, which is 74.0763% [COMPUTED RESULT]. The revenue for this region fell from $5,034 million in Q2 2022 to $1,305 million in Q2 2023 [v5, v6].

**Computation:** `max(abs((us_revenue_q2_2023 - us_revenue_q2_2022) / us_revenue_q2_2022), abs((dev_europe_revenue_q2_2023 - dev_europe_revenue_q2_2022) / dev_europe_revenue_q2_2022), abs((dev_row_revenue_q2_2023 - dev_row_revenue_q2_2022) / dev_row_revenue_q2_2022), abs((em_revenue_q2_2023 - em_revenue_q2_2022) / em_revenue_q2_2022)) = 74.0763%  where us_revenue_q2_2023 = $6,185 (millions, Q2 FY2023), us_revenue_q2_2022 = $11,222 (millions, Q2 FY2022), dev_europe_revenue_q2_2023 = 2,415 (millions, Q2 FY2023), dev_europe_revenue_q2_2022 = 5,480 (millions, Q2 FY2022), dev_row_revenue_q2_2023 = 1,305 (millions, Q2 FY2023), dev_row_revenue_q2_2022 = 5,034 (millions, Q2 FY2022), em_revenue_q2_2023 = 2,828 (millions, Q2 FY2023), em_revenue_q2_2022 = 6,006 (millions, Q2 FY2022)`

- **v5** · `Pfizer_2023Q2_10Q` · PDF page **38** · column July 2, 2023 · millions
  - Quote: "Developed Rest of World \| 1,305"

  <details><summary>Passage</summary>

  ```
  The following summarizes revenues by geographic area:
   | Three Months Ended | Six Months Ended
   | July 2, | July 3, | % | July 2, | July 3, | %
  (MILLIONS) | 2023 | 2022 | Change | 2023 | 2022 | Change
  United States | $6,185  $11,222 | (45)  $14,692  $20,140 | (27)
  Developed Europe | 2,415 | 5,480 | (56) | 5,236 | 11,569 | (55)
  Developed Rest of World | 1,305 | 5,034 | (74) | 3,778 | 8,320 | (55)
  Emerging Markets | 2,828 | 6,006 | (53) | 7,308 | 13,373 | (45)
  Revenues | $12,734  $27,742 | (54)  $31,015  $53,402 | (42)
  In May 2023, we and our collaboration partner, BioNTech, amended our contract with the EC to deliver COVID-19 vaccines to the EU. The amended
  agreement includes rephasing of delivery of doses annually through 2026 and an aggregate volume reduction, providing additional flexibility for EU member
  states. The EC will maintain access to future adapted COVID-19 vaccines and the ability to donate doses, in alignment with the original agreement. See Note
  13C.
  ```
  </details>

- **v6** · `Pfizer_2023Q2_10Q` · PDF page **38** · column July 3, 2022 · millions
  - Quote: "Developed Rest of World \| 5,034"

  <details><summary>Passage</summary>

  ```
  The following summarizes revenues by geographic area:
   | Three Months Ended | Six Months Ended
   | July 2, | July 3, | % | July 2, | July 3, | %
  (MILLIONS) | 2023 | 2022 | Change | 2023 | 2022 | Change
  United States | $6,185  $11,222 | (45)  $14,692  $20,140 | (27)
  Developed Europe | 2,415 | 5,480 | (56) | 5,236 | 11,569 | (55)
  Developed Rest of World | 1,305 | 5,034 | (74) | 3,778 | 8,320 | (55)
  Emerging Markets | 2,828 | 6,006 | (53) | 7,308 | 13,373 | (45)
  Revenues | $12,734  $27,742 | (54)  $31,015  $53,402 | (42)
  In May 2023, we and our collaboration partner, BioNTech, amended our contract with the EC to deliver COVID-19 vaccines to the EU. The amended
  agreement includes rephasing of delivery of doses annually through 2026 and an aggregate volume reduction, providing additional flexibility for EU member
  states. The EC will maintain access to future adapted COVID-19 vaccines and the ability to donate doses, in alignment with the original agreement. See Note
  13C.
  ```
  </details>

<details><summary>Gold answer</summary>

Developed Rest of the World
</details>

## 136. As of Q2'2023, is Pfizer spinning off any large business segments?

`financebench_id_02419` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** Pfizer_2023Q2_10Q: extractor: The filing states that the Upjohn spin-off was completed in November 2020. The only divestiture mentioned for Q2 2023 is an agreement to sell an 'early-stage rare disease gene therapy portfolio' to Alexion, which is a portfolio of assets, not a large business segment. The company's only reportable segment is Biopharma, and there is no evidence of a large business segment being spun off as of Q2 2023.

**Pages searched:** `Pfizer_2023Q2_10Q` pages 1, 8, 9, 10, 11, 13, 17, 34, 37, 38, 41, 45

<details><summary>Gold answer</summary>

Yes, it's spinning off Upjohn.
</details>

## 137. Which debt securities are registered to trade on a national securities exchange under Ulta Beauty's name as of FY2023?

`financebench_id_00746` · filing `ULTABEAUTY_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No debt securities are registered to trade on a national securities exchange under Ulta Beauty's name as of FY2023. The company's 10-K filing indicates that only Common stock is registered pursuant to Section 12(b) of the Act, while the section for securities registered pursuant to Section 12(g) explicitly states "None" [v1, v2]. Consequently, there are no debt securities listed for trading on a national exchange in this filing.

- **v1** · `ULTABEAUTY_2023_10K` · PDF page **1** · column N/A · units
  - Quote: "Securities registered pursuant to Section 12(b) of the Act: Title of each class \| Trading symbol \| Name of each exchange on which registered \| Common stock, par value $0.01 per share \| ULTA \| The NASDAQ Global Select Market"

  <details><summary>Passage</summary>

  ```
   | (State or other jurisdiction of | (I.R.S. Employer
   | incorporation or organization) | Identification No.)
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
  ```
  </details>

- **v2** · `ULTABEAUTY_2023_10K` · PDF page **1** · column N/A · units
  - Quote: "Securities registered pursuant to Section 12(g) of the Act: None"

  <details><summary>Passage</summary>

  ```
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
  Indicate by check mark whether the registrant has submitted electronically every Interactive Data File required to be submitted pursuant to Rule 405 of
  ```
  </details>

<details><summary>Gold answer</summary>

There are none
</details>

## 138. What are major acquisitions that Ulta Beauty has done in FY2023 and FY2022?

`financebench_id_00521` · filing `ULTABEAUTY_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023_10K: extractor: The Consolidated Statements of Cash Flows (Page 57) show 'Acquisitions, net of cash acquired' as '—' (zero) for both FY2023 and FY2022. The document does not list any specific major acquisitions for these periods.

**Pages searched:** `ULTABEAUTY_2023_10K` pages 5, 9, 10, 42, 54, 55, 56, 57, 58, 59, 100, 101

<details><summary>Gold answer</summary>

Ulta Beauty did not make any acquisitions in FY2023 and FY2022.
</details>

## 139. What drove the reduction in SG&A expense as a percent of net sales in FY2023?

`financebench_id_00601` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: extractor: The provided filing is for the Fourth Quarter and Full Year of Fiscal 2022 (ended January 28, 2023). It does not contain actual results for Fiscal 2023, only an outlook. Therefore, the drivers for the reduction in SG&A as a percent of net sales in FY2023 cannot be determined from this document.

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Lower marketing expenses and leverage of incentive compensation due to higher sales. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 140. What drove the increase in Ulta Beauty's merchandise inventories balance at end of FY2023?

`financebench_id_00603` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: extractor: The provided filing covers the fourth quarter and full year of fiscal 2022 (ended January 28, 2023). The question asks for the drivers of the merchandise inventories balance at the end of fiscal year 2023. The document does not contain financial results or explanations for fiscal year 2023 (which would end in early 2024). Therefore, the evidence is not found.

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Increase in Merchandise inventories balance was driven by the opening of 47 new stores. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 141. What percent of Ulta Beauty's total spend on stock repurchases for FY 2023 occurred in Q4 of FY2023?

`financebench_id_00605` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: extractor: The provided filing is for the fourth quarter of fiscal year 2022 (ended January 28, 2023). It does not contain actual financial results for fiscal year 2023 or Q4 of fiscal year 2023. The document only provides an outlook for FY2023 share repurchases, not actual spend data for that period.

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

36%. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 142. Did Ulta Beauty's wages expense as a percent of net sales increase or decrease in FY2023?

`financebench_id_00606` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023Q4_EARNINGS: extractor: The provided filing is for the fourth quarter and full year of fiscal 2022 (ended January 28, 2023). It does not contain actual financial results for fiscal year 2023, only forward-looking guidance. Additionally, the document does not break out 'wages expense' as a separate line item; it is included within 'Selling, general and administrative expenses'.

**Pages searched:** `ULTABEAUTY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9

<details><summary>Gold answer</summary>

Wages expense as a percent of net sales increased in FY2023. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 143. Among all of the derivative instruments that Verizon used to manage the exposure to fluctuations of foreign currencies exchange rates or interest rates, which one had the highest notional value in FY 2021?

`financebench_id_00859` · filing `VERIZON_2021_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The derivative instrument with the highest notional value for Verizon in FY 2021 was cross currency swaps, with a notional amount of $32,502 million [v2]. This exceeds the notional values of interest rate swaps ($19,779 million), forward starting interest rate swaps ($1,000 million), and foreign exchange forwards ($932 million) [v1, v3, v4].

- **v1** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Interest rate swaps \| $19,779"

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

- **v2** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Cross currency swaps \| 32,502"

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

- **v3** · `VERIZON_2021_10K` · PDF page **85** · column 2021 · millions
  - Quote: "Forward starting interest rate swaps \| 1,000"

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
  - Quote: "Foreign exchange forwards \| 932"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Verizon expected to pay $1,959 million for its retirees in the year corresponding to the 2024 column, based on the sum of $1,097 million in pension benefits and $862 million in health care and life benefits [v1, v2]. This total is the computed result of adding the specific values listed for that future period in the evidence [v1, v2].

**Computation:** `pension_benefits_2024 + health_care_life_2024 = 1,959 million  where pension_benefits_2024 = 1,097 (millions, 2024), health_care_life_2024 = 862 (millions, 2024)`

- **v1** · `VERIZON_2021_10K` · PDF page **94** · column 2024 · millions
  - Quote: "2024 \| 1,097 \| 862"

  <details><summary>Passage</summary>

  ```
  Estimated Future Benefit Payments
  The benefit payments to retirees are expected to be paid as follows:
   | (dollars in millions)
   Year | Pension Benefits | Health Care and Life
   2022 | $2,049  $906
   2023 | 1,648 | 883
   2024 | 1,097 | 862
   2025 | 1,066 | 850
   2026 | 1,034 | 840
   2027 to 2031 | 5,097 | 4,139
  Savings Plan and Employee Stock Ownership Plans
  We maintain four leveraged employee stock ownership plans (ESOP). We match a certain percentage of eligible employee contributions to
  certain savings plans with shares of our common stock from this ESOP. At December 31, 2021, the number of allocated shares of common
  ```
  </details>

- **v2** · `VERIZON_2021_10K` · PDF page **94** · column 2024 · millions
  - Quote: "2024 \| 1,097 \| 862"

  <details><summary>Passage</summary>

  ```
  Estimated Future Benefit Payments
  The benefit payments to retirees are expected to be paid as follows:
   | (dollars in millions)
   Year | Pension Benefits | Health Care and Life
   2022 | $2,049  $906
   2023 | 1,648 | 883
   2024 | 1,097 | 862
   2025 | 1,066 | 850
   2026 | 1,034 | 840
   2027 to 2031 | 5,097 | 4,139
  Savings Plan and Employee Stock Ownership Plans
  We maintain four leveraged employee stock ownership plans (ESOP). We match a certain percentage of eligible employee contributions to
  certain savings plans with shares of our common stock from this ESOP. At December 31, 2021, the number of allocated shares of common
  ```
  </details>

<details><summary>Gold answer</summary>

The estimated pension benefits were $1097 million, and the estimated health care and life insurance benefits were $862 million.
</details>

## 145. Does Verizon have a reasonably healthy liquidity profile based on its quick ratio for FY 2022? If the quick ratio is not relevant to measure liquidity, please state that and explain why.

`financebench_id_00216` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** VERIZON_2022_10K: verifier: answer_supported=partly. The final answer states the liquidity profile is 'reasonably healthy' based on a quick ratio of 0.54, but a quick ratio below 1.0 is generally considered a sign of potential liquidity issues (inability to cover all current liabilities with liquid assets), making the qualitative judgment 'reasonably healthy' subjective and potentially incorrect.

**Pages searched:** `VERIZON_2022_10K` pages 23, 26, 37, 42, 52, 54, 55, 56, 57, 58, 105, 106

<details><summary>Gold answer</summary>

No. The quick ratio was approximately 0.54 for Verizon. It indicated that Verizon does not have a healthy liquidity profile.
</details>

## 146. Is Verizon a capital intensive business based on FY 2022 data?

`financebench_id_00215` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Verizon is a capital intensive business based on FY 2022 data, as its capital expenditures represented 16.9% of its total operating revenues [v1, v2]. This high ratio indicates that the company must invest a significant portion of its revenue back into property, plant, and equipment to maintain operations [v1, v2, v3]. The computed result of 16.9% confirms this heavy reliance on capital investment [COMPUTED RESULT].

**Computation:** `abs(capital_expenditures_2022) / operating_revenues_2022 = 16.9%  where capital_expenditures_2022 = (23,087) (millions, FY2022), operating_revenues_2022 = 136,835 (millions, FY2022), property_plant_equipment_net_2022 = 107,434 (millions, FY2022)`

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

- **v3** · `VERIZON_2022_10K` · PDF page **56** · column 2022 · millions
  - Quote: "Property, plant and equipment, net \| 107,434"

  <details><summary>Passage</summary>

  ```
   | Accounts receivable, net | 24,506 | 23,846
   | Inventories | 2,388 | 3,055
   | Prepaid expenses and other | 8,358 | 6,906
   Total current assets | 37,857 | 36,728
   Property, plant and equipment | 307,689 | 289,897
   | Less Accumulated depreciation | 200,255 | 190,201
   Property, plant and equipment, net | 107,434 | 99,696
   Investments in unconsolidated businesses | 1,071 | 1,061
   Wireless licenses | 149,796 | 147,619
   Goodwill | 28,671 | 28,603
   Other intangible assets, net | 11,461 | 11,677
   Operating lease right-of-use assets | 26,130 | 27,883
   Other assets | 17,260 | 13,329
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. Verizon's capital intensity ratio was approximately 2.774729. This means that it took approximately $2.77 of assets to generate $1 of revenue and thus, Verizon can be considered capital intensive.
</details>

## 147. Has Verizon increased its debt on balance sheet between 2022 and the 2021 fiscal period?

`financebench_id_00566` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, Verizon did not increase its debt between the 2021 and 2022 fiscal periods. The total debt decreased by $229 million, falling from $150,868 million in 2021 to $150,639 million in 2022 [v1, v2]. This reduction is confirmed by the computed difference of -229 million [COMPUTED RESULT].

**Computation:** `total_debt_2022 - total_debt_2021 = -229 million  where total_debt_2022 = $150,639 (millions, FY2022), total_debt_2021 = $150,868 (millions, FY2021)`

- **v1** · `VERIZON_2022_10K` · PDF page **77** · column 2022 · millions
  - Quote: "Total debt \| $150,639  $150,868"

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
  - Quote: "Total debt \| $150,639  $150,868"

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** WALMART_2018_10K: number check (G4) failed twice: numbers not in the evidence or the result: 365

**Pages searched:** `WALMART_2018_10K` pages 17, 39, 40, 43, 57, 58, 59, 61, 62, 64, 69, 85

<details><summary>Gold answer</summary>

42.69
</details>

## 149. Based on the information provided primarily in the statement of income, what is the FY2018 - FY2019 change in unadjusted operating income % margin for Walmart? Answer in units of percents and round to one decimal place.

`financebench_id_04784` · filing `WALMART_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The change in Walmart's unadjusted operating income margin from FY2018 to FY2019 is 0.2%. This result is derived from the operating income of 21,957 million and net sales of 510,329 million in the 2019 column, compared to operating income of 20,437 million and net sales of 495,761 million in the 2018 column [v1, v2, v3, v4]. The computed difference between the two years' margins is exactly 0.2% [COMPUTED RESULT].

**Computation:** `(operating_income_2019 / net_sales_2019) - (operating_income_2018 / net_sales_2018) = 0.2%  where operating_income_2019 = 21,957 (millions, FY2019), operating_income_2018 = 20,437 (millions, FY2018), net_sales_2019 = 510,329 (millions, FY2019), net_sales_2018 = 495,761 (millions, FY2018)`

- **v1** · `WALMART_2019_10K` · PDF page **48** · column 2019 · millions
  - Quote: "Operating income \| 21,957 \| 20,437 \| 22,764"

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

- **v2** · `WALMART_2019_10K` · PDF page **48** · column 2018 · millions
  - Quote: "Operating income \| 21,957 \| 20,437 \| 22,764"

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

- **v3** · `WALMART_2019_10K` · PDF page **48** · column 2019 · millions
  - Quote: "Net sales \| $510,329 \| $495,761 \| $481,317"

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

- **v4** · `WALMART_2019_10K` · PDF page **48** · column 2018 · millions
  - Quote: "Net sales \| $510,329 \| $495,761 \| $481,317"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average unadjusted EBITDA margin for Walmart from FY2018 to FY2020 is 6.2%. This result is calculated by averaging the annual ratios of unadjusted operating income plus depreciation and amortization to net sales for the three fiscal years [v1, v2, v3, v4, v5, v6, v7, v8, v9]. The computed average of these three years' margins is explicitly provided as 6.2% [COMPUTED RESULT].

**Computation:** `avg((op_income_2018 + d_and_a_2018) / net_sales_2018, (op_income_2019 + d_and_a_2019) / net_sales_2019, (op_income_2020 + d_and_a_2020) / net_sales_2020) = 6.2%  where op_income_2018 = 20,437 (millions, FY2018), op_income_2019 = 21,957 (millions, FY2019), op_income_2020 = 20,568 (millions, FY2020), d_and_a_2018 = 10,529 (millions, FY2018), d_and_a_2019 = 10,678 (millions, FY2019), d_and_a_2020 = 10,987 (millions, FY2020), net_sales_2018 = $495,761 (millions, FY2018), net_sales_2019 = $510,329 (millions, FY2019), net_sales_2020 = $519,926 (millions, FY2020)`

- **v1** · `WALMART_2020_10K` · PDF page **51** · column 2018 · millions
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

- **v3** · `WALMART_2020_10K` · PDF page **51** · column 2020 · millions
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

- **v4** · `WALMART_2020_10K` · PDF page **56** · column 2018 · millions
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

- **v6** · `WALMART_2020_10K` · PDF page **56** · column 2020 · millions
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

- **v7** · `WALMART_2020_10K` · PDF page **51** · column 2018 · millions
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

- **v9** · `WALMART_2020_10K` · PDF page **51** · column 2020 · millions
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

<details><summary>Gold answer</summary>

6.2%
</details>
