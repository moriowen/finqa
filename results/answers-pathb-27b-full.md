# Answers with provenance: pathb-27b-full

Configuration: `pathb-27b-full`. One section per question, in dataset order. Status ANSWER = all checks passed; NOT_FOUND / AMBIGUOUS = the system abstained (the reason says which check failed). PDF page numbers are 1-based. `Judge` is the eval label against the gold answer (not visible to the system).

## 1. What is the FY2018 capital expenditure amount (in USD millions) for 3M? Give a response to the question by relying on the details shown in the cash flow statement.

`financebench_id_03029` · filing `3M_2018_10K` · metrics-generated

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `3M_2018_10K` pages 39, 43, 44, 47, 49, 56, 57, 58, 59, 60, 81, 83; `3M_2019_10K` pages 25, 43, 48, 56, 57, 58, 59, 60, 79, 81, 86, 103

<details><summary>Gold answer</summary>

$1577.00
</details>

## 2. Assume that you are a public equities analyst. Answer the following question by primarily using information that is shown in the balance sheet: what is the year end FY2018 net PPNE for 3M? Answer in USD billions.

`financebench_id_04672` · filing `3M_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The year-end FY2018 net PPNE for 3M is 8.74 billion USD. This figure is derived from the Consolidated Balance Sheet, which reports Property, plant and equipment — net as 8,738 million dollars for 2018 [v1].

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

**Reason:** 3M_2022_10K: code checks failed twice: purchases_of_pp_and_e_2022: the quote is not on page 52. Copy it exactly from one line of the page; formula: unknown value name 'net_sales_2022' (names: []) \| 3M_2023Q2_10Q: extractor: The provided filing is a 10-Q for the quarterly period ended June 30, 2023 (Q2 FY2023). It does not contain the full fiscal year 2022 (FY2022) data required to answer the question. The document only provides comparative data for the three and six months ended June 30, 2022, and balance sheet data as of December 31, 2022 (which is the end of FY2022, but the question asks for FY2022 data which typically implies income statement metrics like Capex or depreciation for the full year, or a specific FY2022 column which is not present for the full year in this 10-Q).

**Pages searched:** `3M_2022_10K` pages 2, 3, 37, 38, 39, 41, 48, 49, 50, 51, 52, 68; `3M_2023Q2_10Q` pages 1, 4, 5, 10, 14, 15, 54, 70, 71, 72, 73, 83

<details><summary>Gold answer</summary>

No, the company is managing its CAPEX and Fixed Assets pretty efficiently, which is evident from below key metrics: CAPEX/Revenue Ratio: 5.1% Fixed assets/Total Assets: 20% Return on Assets= 12.4%
</details>

## 4. What drove operating margin change as of FY2022 for 3M? If operating margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_01226` · filing `3M_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** 3M's operating margin decreased by 1.7% to 19.1% in FY2022, driven primarily by higher cost of sales and SG&A expenses due to special litigation costs for PFAS and Combat Arms Earplugs matters, alongside raw material and logistics inflation [v1, v2, v3, v8, v9, v10]. These negative impacts were partially offset by an 8.0% gain on business divestitures, though goodwill impairment expenses also reduced the margin [v6, v7]. Operating margin remains a useful metric for 3M as it effectively captures the net impact of these significant operational and one-time items on profitability [v1, v3].

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

**Reason:** 3M_2022_10K: code checks failed twice: formula: unknown value name 'safety_industrial_organic_2022' (names: []) \| 3M_2023Q2_10Q: extractor: The provided pages contain segment data for Q2 2022 and Q2 2023, but do not contain the full-year 2022 data required to determine which segment dragged down overall growth for the entire year 2022. Additionally, the Consumer segment data table is not included in the provided pages, preventing a complete analysis even for the available periods.

**Pages searched:** `3M_2022_10K` pages 3, 19, 21, 30, 32, 33, 48, 49, 50, 51, 52, 68; `3M_2023Q2_10Q` pages 4, 5, 7, 54, 55, 56, 64, 65, 66, 67, 68, 77

<details><summary>Gold answer</summary>

The consumer segment shrunk by 0.9% organically.
</details>

## 6. Does 3M have a reasonably healthy liquidity profile based on its quick ratio for Q2 of FY2023? If the quick ratio is not relevant to measure liquidity, please state that and explain why.

`financebench_id_00807` · filing `3M_2023Q2_10Q` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, 3M has a reasonably healthy liquidity profile with a quick ratio of 0.85 for Q2 of FY2023. This result is derived from cash and cash equivalents of $4,258 million, marketable securities of $56 million, and net accounts receivable of $4,947 million, divided by total current liabilities of $10,936 million [v1, v2, v3, v4]. The computed ratio of 0.85 indicates the company's ability to meet short-term obligations with its most liquid assets [v1, v2, v3, v4].

**Computation:** `(cash_and_cash_equivalents_q2_2023 + marketable_securities_current_q2_2023 + accounts_receivable_net_q2_2023) / total_current_liabilities_q2_2023 = 0.85  where cash_and_cash_equivalents_q2_2023 = $4,258 (millions, Q2 FY2023), marketable_securities_current_q2_2023 = 56 (millions, Q2 FY2023), accounts_receivable_net_q2_2023 = 4,947 (millions, Q2 FY2023), total_current_liabilities_q2_2023 = 10,936 (millions, Q2 FY2023)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** 3M_2023Q2_10Q: number check (G4) failed twice: numbers not in the evidence or the result: 2026,, 2030,

**Pages searched:** `3M_2023Q2_10Q` pages 1, 2, 4, 5, 6, 19, 27, 70, 71, 73, 85, 91

<details><summary>Gold answer</summary>

Following debt securities registered under 3M's name are listed to trade on the New York Stock Exchange: -1.500% Notes due 2026 (Trading Symbol: MMM26) -1.750% Notes due 2030 (Trading Symbol: MMM30) -1.500% Notes due 2031 (Trading Symbol: MMM31)
</details>

## 8. Does 3M maintain a stable trend of dividend distribution?

`financebench_id_01858` · filing `3M_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, 3M maintains a stable trend of dividend distribution, as evidenced by its 65th consecutive year of dividend increases in 2022 [v4]. The company's total declared and paid dividends per share rose steadily from $5.88 in 2020 to $5.92 in 2021 and $5.96 in 2022 [v1, v2, v3]. This consistent upward trajectory confirms a stable and growing commitment to shareholder returns.

- **v1** · `3M_2022_10K` · PDF page **69** · column 2020 · units
  - Quote: "total year declared and paid dividends of $5.96, $5.92, and $5.88 per share, respectively"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NOTE 8. Supplemental Equity and Comprehensive Income Information
  Common stock ($.01 par value per share) of 3 billion shares is authorized, with 944,033,056 shares issued as of December 31, 2022, 2021 and 2020. Preferred stock, without
  par value, of 10 million shares is authorized but unissued.
  Cash dividends declared and paid totaled $1.49, $1.48, and $1.47 per share for each quarter in 2022, 2021 and 2020, respectively, which resulted in total year declared and paid
  dividends of $5.96, $5.92, and $5.88 per share, respectively.
  Dividend to noncontrolling interest in 2022 of $29 million related to dividend paid by 3M India Limited, of which 3M’s effective ownership is75 percent.
  Changes in Accumulated Other Comprehensive Income (Loss) Attributable to 3M by Component
   | Defined Benefit
   | Cumulative | Pension and | Cash Flow Hedging | Total Accumulated
   | Translation | Postretirement Plans | Instruments, Unrealized | Other Comprehensive
  ```
  </details>

- **v2** · `3M_2022_10K` · PDF page **69** · column 2021 · units
  - Quote: "total year declared and paid dividends of $5.96, $5.92, and $5.88 per share, respectively"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NOTE 8. Supplemental Equity and Comprehensive Income Information
  Common stock ($.01 par value per share) of 3 billion shares is authorized, with 944,033,056 shares issued as of December 31, 2022, 2021 and 2020. Preferred stock, without
  par value, of 10 million shares is authorized but unissued.
  Cash dividends declared and paid totaled $1.49, $1.48, and $1.47 per share for each quarter in 2022, 2021 and 2020, respectively, which resulted in total year declared and paid
  dividends of $5.96, $5.92, and $5.88 per share, respectively.
  Dividend to noncontrolling interest in 2022 of $29 million related to dividend paid by 3M India Limited, of which 3M’s effective ownership is75 percent.
  Changes in Accumulated Other Comprehensive Income (Loss) Attributable to 3M by Component
   | Defined Benefit
   | Cumulative | Pension and | Cash Flow Hedging | Total Accumulated
   | Translation | Postretirement Plans | Instruments, Unrealized | Other Comprehensive
  ```
  </details>

- **v3** · `3M_2022_10K` · PDF page **69** · column 2022 · units
  - Quote: "total year declared and paid dividends of $5.96, $5.92, and $5.88 per share, respectively"

  <details><summary>Passage</summary>

  ```
  Table of Contents
  NOTE 8. Supplemental Equity and Comprehensive Income Information
  Common stock ($.01 par value per share) of 3 billion shares is authorized, with 944,033,056 shares issued as of December 31, 2022, 2021 and 2020. Preferred stock, without
  par value, of 10 million shares is authorized but unissued.
  Cash dividends declared and paid totaled $1.49, $1.48, and $1.47 per share for each quarter in 2022, 2021 and 2020, respectively, which resulted in total year declared and paid
  dividends of $5.96, $5.92, and $5.88 per share, respectively.
  Dividend to noncontrolling interest in 2022 of $29 million related to dividend paid by 3M India Limited, of which 3M’s effective ownership is75 percent.
  Changes in Accumulated Other Comprehensive Income (Loss) Attributable to 3M by Component
   | Defined Benefit
   | Cumulative | Pension and | Cash Flow Hedging | Total Accumulated
   | Translation | Postretirement Plans | Instruments, Unrealized | Other Comprehensive
  ```
  </details>

- **v4** · `3M_2022_10K` · PDF page **26** · column text · units
  - Quote: "This marked the 65th consecutive year of dividend increases for 3M."

  <details><summary>Passage</summary>

  ```
  3M’s businesses to respond to changes in the marketplace.
  Financial condition:
  Refer to the section entitled “Financial Condition and Liquidity” later in MD&A for a discussion of items impacting cash flows.
  In November 2018, 3M’s Board of Directors replaced the Company’s February 2016 repurchase program with a new repurchase program. This new program authorizes the
  repurchase of up to $10 billion of 3M’s outstanding common stock, with no pre-established end date. In 2022, the Company purchased $1.5 billion of its own stock, compared
  to $2.2 billion of stock purchases in 2021. As of December 31, 2022, approximately $4.2 billion remained available under the authorization. In February 2023, 3M’s Board of
  Directors declared a first-quarter 2023 dividend of $1.50 per share, an increase of 1 percent. This marked the 65th consecutive year of dividend increases for 3M.
  Raw materials:
  Refer to the section entitled “Raw materials” in Item 1 for discussion of 3M's sources and availability of raw materials in 2022.
  Pension and postretirement defined benefit/contribution plans:
  On a worldwide basis, 3M’s pension and postretirement plans were 96 percent funded at year-end 2022. The primary U.S. qualified pension plan, which is approximately 70
  percent of the worldwide pension obligation, was 97 percent funded and the international pension plans were 116 percent funded. The U.S. non-qualified pension plan is not
  funded due to tax considerations and other factors. Asset returns in 2022 for the primary U.S. qualified pension plan were -17.4 percent, as 3M strategically invests in both
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, not only they distribute the dividends on a routine basis, 3M has also been increasing the per share dividend for consecutive 65 years
</details>

## 9. What is the FY2019 fixed asset turnover ratio for Activision Blizzard? Fixed asset turnover ratio is defined as: FY2019 revenue / (average PP&E between FY2018 and FY2019). Round your answer to two decimal places. Base your judgments on the information provided primarily in the statement of income and the statement of financial position.

`financebench_id_02987` · filing `ACTIVISIONBLIZZARD_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 fixed asset turnover ratio for Activision Blizzard is 24.26. This result is calculated by dividing the total net revenues of $6,489 million for 2019 by the average of the property and equipment, net values of $253 million in 2019 and $282 million in 2018 [v1, v2, v3]. The computed ratio of 24.26 reflects the company's efficiency in generating revenue from its fixed assets during the fiscal year [COMPUTED RESULT].

**Computation:** `total_net_revenues_2019 / avg(ppe_net_2019, ppe_net_2018) = 24.26  where total_net_revenues_2019 = 6,489 (millions, FY2019), ppe_net_2019 = 253 (millions, FY2019), ppe_net_2018 = 282 (millions, FY2018)`

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

**Answer:** The FY2015 operating cash flow ratio for Adobe is 0.66. This is calculated by dividing the net cash provided by operating activities of $1,469,502 thousand by the total current liabilities of $2,213,556 thousand [v1, v2]. The computed result of this division is exactly 0.66 [COMPUTED RESULT].

**Computation:** `cash_from_operations_2015 / total_current_liabilities_2015 = 0.66  where cash_from_operations_2015 = 1,469,502 (thousands, FY2015), total_current_liabilities_2015 = 2,213,556 (thousands, FY2015)`

- **v1** · `ADOBE_2015_10K` · PDF page **63** · column November 27, 2015 · thousands
  - Quote: "Net cash provided by operating activities................................................................ 1,469,502"

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
  - Quote: "Total current liabilities.................................................................................................................... 2,213,556"

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

**Answer:** Adobe's year-over-year change in unadjusted operating income from FY2015 to FY2016 is 65.4%. This increase is calculated based on the operating income rising from 903,095 thousand in FY2015 to 1,493,602 thousand in FY2016 [v1, v2]. The computed result of 65.4% reflects the growth between these two fiscal years [COMPUTED RESULT].

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** ADOBE_2022_10K: verifier: answer_supported=partly. The final answer claims an 'improving' profile but only provides the FY2022 margin (34.64%) without calculating and comparing the margins for FY2021 and FY2020 to prove the trend. \| ADOBE_2022Q2_10Q: extractor: The provided filing is for the quarterly period ended June 2, 2023 (Q2 FY2023). The question asks for the operating margin profile as of FY2022. The document does not contain the full fiscal year 2022 data (only Q2 FY2022 and Q2 FY2023 are available in the income statement). Therefore, the evidence to determine the FY2022 profile is not found in the provided pages.

**Pages searched:** `ADOBE_2022_10K` pages 1, 3, 5, 23, 37, 38, 53, 54, 57, 88, 89, 90; `ADOBE_2022Q2_10Q` pages 1, 3, 4, 5, 8, 9, 23, 25, 26, 41, 42, 47

<details><summary>Gold answer</summary>

No the operating margins of Adobe have recently declined from 36.8% in FY 2021 to 34.6% in FY2022. A drop by 2.2% in a year.
</details>

## 15. Does Adobe have an improving Free cashflow conversion as of FY2022?

`financebench_id_00591` · filing `ADOBE_2022_10K` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** ADOBE_2022_10K: verifier: answer_supported=no. The formula used to calculate 'Free cashflow conversion' is incorrect. Free cash flow conversion is typically defined as Free Cash Flow divided by Net Income (or Revenue), not the ratio of (Operating Cash Flow + Capex) to Operating Cash Flow. Furthermore, Capex is an outflow, so it should be subtracted from Operating Cash Flow to calculate Free Cash Flow. \| ADOBE_2022Q2_10Q: extractor: The provided filing is a 10-Q for the second quarter of fiscal year 2023 (ending June 2, 2023), despite the user prompt stating 'Q2 of fiscal year 2022'. The document contains financial data for the six months ended June 2, 2023, and June 3, 2022. It does not contain the full fiscal year 2022 data (which would end in late 2022) required to calculate Free Cash Flow conversion for FY2022, nor does it contain FY2021 data to determine if the metric was 'improving' as of FY2022. Therefore, the evidence is not found.

**Pages searched:** `ADOBE_2022_10K` pages 3, 5, 6, 11, 39, 53, 54, 55, 57, 58, 90; `ADOBE_2022Q2_10Q` pages 2, 3, 4, 5, 6, 7, 8, 25, 26, 27, 54, 56

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

**Answer:** AES Corporation sold its inventory approximately 12.14 times in FY2022. This inventory turnover ratio is derived from the absolute cost of sales of 10,069 million and the average of the 2022 inventory of 1,055 million and the 2021 inventory of 604 million [v1, v2, v3]. The metric is meaningful for this company as it reports significant inventory values alongside its cost of sales [v1, v2, v3].

**Computation:** `abs(cost_of_sales_2022) / avg(inventory_2022, inventory_2021) = 12.14  where cost_of_sales_2022 = (10,069) (millions, FY2022), inventory_2022 = 1,055 (millions, FY2022), inventory_2021 = 604 (millions, FY2021)`

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

- **v3** · `AES_2022_10K` · PDF page **130** · column 2021 · millions
  - Quote: "Inventory \| 604"

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** AES_2022_10K: verifier: answer_supported=no. The net income for FY2022 is a loss of $(505) million, which should result in a negative ROA. The computation and final answer incorrectly state a positive 1.42%. \| AES_2021_10K: extractor: The provided filing is the 10-K for the fiscal year ended December 31, 2021. It contains data for FY2021, FY2020, and FY2019. It does not contain financial data for FY2022 (fiscal year ended December 31, 2022), which is required to calculate the FY2022 Return on Assets.

**Pages searched:** `AES_2022_10K` pages 1, 84, 127, 130, 132, 133, 135, 202, 207, 214, 215, 216, 217; `AES_2021_10K` pages 1, 2, 82, 129, 131, 132, 134, 192, 205, 212, 213, 214, 215

<details><summary>Gold answer</summary>

-0.02
</details>

## 19. What is Amazon's FY2017 days payable outstanding (DPO)? DPO is defined as: 365 * (average accounts payable between FY2016 and FY2017) / (FY2017 COGS + change in inventory between FY2016 and FY2017). Round your answer to two decimal places. Address the question by using the line items and information shown within the balance sheet and the P&L statement.

`financebench_id_06655` · filing `AMAZON_2017_10K` · metrics-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMAZON_2017_10K: code checks failed twice: formula: unknown value name 'cogs_2017' (names: []) \| AMAZON_2018_10K: extractor: The question requires the average accounts payable between FY2016 and FY2017, and the change in inventory between FY2016 and FY2017. The provided Balance Sheet (Page 39) only contains data for December 31, 2017 and December 31, 2018. It does not contain the FY2016 (December 31, 2016) values for Accounts Payable or Inventories. Therefore, the average and the change cannot be calculated using only the provided pages. \| AMAZON_2016_10K: extractor: The provided filing is Amazon's 10-K for fiscal year 2016. The question asks for FY2017 Days Payable Outstanding (DPO), which requires financial data for the fiscal year ended December 31, 2017 (specifically Accounts Payable, Cost of Sales, and Inventory for 2017). The provided pages only contain data up to December 31, 2016. Therefore, the necessary evidence for FY2017 is not present in the document.

**Pages searched:** `AMAZON_2017_10K` pages 1, 19, 20, 25, 37, 38, 39, 40, 41, 42, 46, 53; `AMAZON_2018_10K` pages 1, 19, 36, 37, 38, 39, 46, 51, 52, 76, 77, 78; `AMAZON_2016_10K` pages 1, 7, 18, 19, 36, 37, 38, 39, 41, 46, 48, 52

<details><summary>Gold answer</summary>

93.86
</details>

## 20. What is Amazon's year-over-year change in revenue from FY2016 to FY2017 (in units of percents and round to one decimal place)? Calculate what was asked by utilizing the line items clearly shown in the statement of income.

`financebench_id_08135` · filing `AMAZON_2017_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amazon's year-over-year change in revenue from FY2016 to FY2017 is 30.8%. This result is calculated using the total net sales of $135,987 million for 2016 and $177,866 million for 2017 [v1, v2]. The computed percentage increase is explicitly provided as 30.8% [COMPUTED RESULT].

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

**Answer:** Amazon's FY2019 net income attributable to shareholders is 11,588 million USD. This figure is directly reported as "Net income" for the year 2019 in the Consolidated Statements of Operations [v1]. The value is confirmed by the computed result derived from the evidence [v1].

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The key agenda of Amcor's 8-K filing dated July 1, 2022, was to report the substitution of Amcor Flexibles North America, Inc. as the issuer for Amcor Finance (USA), Inc. regarding its senior notes [v2, v4]. This action involved entering into supplemental indentures on June 30, 2022, where the Substitute Issuer assumed the covenants of the Former Issuer [v3, v4]. The filing specifically covered the Existing Notes and New Notes governed by the 2016 and 2019 Indentures [v2].

- **v2** · `AMCOR_2022_8K_dated-2022-07-01` · PDF page **2** · column N/A · units
  - Quote: "On June 30, 2022, Amcor Finance (USA), Inc. (the “Former Issuer”) and Amcor Flexibles North America, Inc. (the “Substitute Issuer”), each a wholly-owned subsidiary of Amcor plc (the “Company”),"

  <details><summary>Passage</summary>

  ```
  Item 8.01 | Other Events.
   | On June 30, 2022, Amcor Finance (USA), Inc. (the “Former Issuer”) and Amcor Flexibles North America, Inc. (the “Substitute Issuer”),
  each a wholly-owned subsidiary of Amcor plc (the “Company”), entered into a (i) Second Supplemental Indenture (the “Second Supplemental
  Indenture”) with the Trustee (as defined below) with respect to the Indenture, dated as of April 28, 2016 (as amended and/or supplemented to
  date, the “2016 Indenture” and, together with the Second Supplemental Indenture, the “2016 Indenture”), among the Former Issuer, the
  guarantors party thereto and Deutsche Bank Trust Company Americas, as trustee (the “Trustee”), governing the Former Issuer’s (a) 3.625%
  Guaranteed Senior Notes due 2026 (the “2026 Notes”) and (b) 4.500% Guaranteed Senior Notes due 2028 (the “2028 Notes” and, together with
  the 2026 Notes, the “Existing Notes”) and (ii) First Supplemental Indenture (the “First Supplemental Indenture” and, together with the Second
  ```
  </details>

- **v3** · `AMCOR_2022_8K_dated-2022-07-01` · PDF page **2** · column N/A · units
  - Quote: "entered into a (i) Second Supplemental Indenture (the “Second Supplemental Indenture”) with the Trustee (as defined below) with respect to the Indenture, dated as of April 28, 2016 (as amended and/or"

  <details><summary>Passage</summary>

  ```
  Item 8.01 | Other Events.
   | On June 30, 2022, Amcor Finance (USA), Inc. (the “Former Issuer”) and Amcor Flexibles North America, Inc. (the “Substitute Issuer”),
  each a wholly-owned subsidiary of Amcor plc (the “Company”), entered into a (i) Second Supplemental Indenture (the “Second Supplemental
  Indenture”) with the Trustee (as defined below) with respect to the Indenture, dated as of April 28, 2016 (as amended and/or supplemented to
  date, the “2016 Indenture” and, together with the Second Supplemental Indenture, the “2016 Indenture”), among the Former Issuer, the
  guarantors party thereto and Deutsche Bank Trust Company Americas, as trustee (the “Trustee”), governing the Former Issuer’s (a) 3.625%
  Guaranteed Senior Notes due 2026 (the “2026 Notes”) and (b) 4.500% Guaranteed Senior Notes due 2028 (the “2028 Notes” and, together with
  the 2026 Notes, the “Existing Notes”) and (ii) First Supplemental Indenture (the “First Supplemental Indenture” and, together with the Second
  Supplemental Indenture, the “Supplemental Indentures”) with the Trustee with respect to the Indenture, dated as of June 13, 2019 (as amended
  ```
  </details>

- **v4** · `AMCOR_2022_8K_dated-2022-07-01` · PDF page **2** · column N/A · units
  - Quote: "relating to the substitution of the Substitute Issuer for the Former Issuer and the assumption by the Substitute Issuer of the covenants of the Former Issuer under the Indentures."

  <details><summary>Passage</summary>

  ```
  Guaranteed Senior Notes due 2026 (the “2026 Notes”) and (b) 4.500% Guaranteed Senior Notes due 2028 (the “2028 Notes” and, together with
  the 2026 Notes, the “Existing Notes”) and (ii) First Supplemental Indenture (the “First Supplemental Indenture” and, together with the Second
  Supplemental Indenture, the “Supplemental Indentures”) with the Trustee with respect to the Indenture, dated as of June 13, 2019 (as amended
  and/or supplemented to date, the “2019 Indenture” and, together with the First Supplemental Indenture, the “2019 Indenture” and, together with
  the 2016 Indenture, the “Indentures”), among the Former Issuer, the guarantors party thereto and the Trustee, governing the Former Issuer’s
  (a) 3.625% Guaranteed Senior Notes due 2026 (the “New 2026 Notes”) and (b) 4.500% Guaranteed Senior Notes due 2028 (the “New 2028
  Notes” and, together with the New 2026 Notes, the “New Notes”), in each case, relating to the substitution of the Substitute Issuer for the Former
  Issuer and the assumption by the Substitute Issuer of the covenants of the Former Issuer under the Indentures. As disclosed in the Company’s
  Current Report on Form 8-K, filed with the Securities and Exchange Commission (the “SEC”) on June 17, 2019, the New Notes were issued in
  June 2019 following the completion of the Former Issuer’s exchange offer to certain eligible holders of the Existing Notes.
   | The foregoing description of the Supplemental Indentures does not purport to be complete and is subject to, and qualified in its entirety
  by, the full text of the (i) 2016 Indenture, which was included as Exhibit 4.7 to the Company’s Registration Statement on Form S-4 (File No. 333-
  230217), filed with the SEC on March 12, 2019 (the “Registration Statement”), including the supplemental indenture thereto, which was included
  ```
  </details>

<details><summary>Gold answer</summary>

Amcor Finance (USA), Inc. and Amcor Flexibles North America, Inc., entered into supplemental indentures relating to Guaranteed Senior Notes due 2026 and 2028. This involved the substitution of the Substitute Issuer (Amcor Flexibles North America) for the Former Issuer (Amcor Finance) and the assumption of covenants under the indentures. (In essence a novation agreement)
</details>

## 24. Has AMCOR's quick ratio improved or declined between FY2023 and FY2022? If the quick ratio is not something that a financial analyst would ask about a company like this, then state that and explain why.

`financebench_id_00799` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The quick ratio is not a meaningful metric for Amcor because the provided financial evidence does not include the necessary values for current assets or current liabilities required to calculate it [v2, v3, v4, v5]. While the document provides net debt and cash equivalents, it lacks the specific line items needed to assess short-term liquidity via the quick ratio [v2, v3, v4, v5]. Therefore, it is not possible to determine if the ratio improved or declined based on the available data.

- **v2** · `AMCOR_2023Q4_EARNINGS` · PDF page **14** · column June 30, 2022 · millions
  - Quote: "Net debt \| 5,715"

  <details><summary>Passage</summary>

  ```
  Reconciliation of net debt
   ($million) | June 30, 2022 | June 30, 2023
   Cash and cash equivalents | (775) | (689)
   Short-term debt | 136 | 80
   Current portion of long-term debt | 14 | 13
   Long-term debt excluding current portion | 6,340 | 6,653
   Net debt | 5,715 | 6,057
   | 14
  ```
  </details>

- **v3** · `AMCOR_2023Q4_EARNINGS` · PDF page **14** · column June 30, 2023 · millions
  - Quote: "Net debt \| 6,057"

  <details><summary>Passage</summary>

  ```
  Reconciliation of net debt
   ($million) | June 30, 2022 | June 30, 2023
   Cash and cash equivalents | (775) | (689)
   Short-term debt | 136 | 80
   Current portion of long-term debt | 14 | 13
   Long-term debt excluding current portion | 6,340 | 6,653
   Net debt | 5,715 | 6,057
   | 14
  ```
  </details>

- **v4** · `AMCOR_2023Q4_EARNINGS` · PDF page **14** · column June 30, 2022 · millions
  - Quote: "Cash and cash equivalents \| (775)"

  <details><summary>Passage</summary>

  ```
  (3) Includes the net gain on the sale of the Russian business and incremental restructuring and other costs attributable to group wide initiatives to
  offset divested earnings from the Russian business. Fiscal year 2022 includes impairment charges and restructuring and related expenses.
  (4) Amortization of acquired intangible assets from business combinations.
  (5) Reflects the impact of acquired, disposed, and ceased operations.
  Reconciliation of net debt
   ($million) | June 30, 2022 | June 30, 2023
   Cash and cash equivalents | (775) | (689)
   Short-term debt | 136 | 80
   Current portion of long-term debt | 14 | 13
   Long-term debt excluding current portion | 6,340 | 6,653
   Net debt | 5,715 | 6,057
   | 14
  ```
  </details>

- **v5** · `AMCOR_2023Q4_EARNINGS` · PDF page **14** · column June 30, 2023 · millions
  - Quote: "Cash and cash equivalents \| (689)"

  <details><summary>Passage</summary>

  ```
  (3) Includes the net gain on the sale of the Russian business and incremental restructuring and other costs attributable to group wide initiatives to
  offset divested earnings from the Russian business. Fiscal year 2022 includes impairment charges and restructuring and related expenses.
  (4) Amortization of acquired intangible assets from business combinations.
  (5) Reflects the impact of acquired, disposed, and ceased operations.
  Reconciliation of net debt
   ($million) | June 30, 2022 | June 30, 2023
   Cash and cash equivalents | (775) | (689)
   Short-term debt | 136 | 80
   Current portion of long-term debt | 14 | 13
   Long-term debt excluding current portion | 6,340 | 6,653
   Net debt | 5,715 | 6,057
   | 14
  ```
  </details>

<details><summary>Gold answer</summary>

The quick ratio has slightly improved from 0.67 times to 0.69 times between FY 2023 and FY 2022.(3.4% jump)
</details>

## 25. What are major acquisitions that AMCOR has done in FY2023, FY2022 and FY2021?

`financebench_id_01079` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMCOR_2023_10K: extractor: The provided pages contain the total dollar amount spent on business acquisitions in the Consolidated Statements of Cash Flows (Page 53), but they do not list the names or specific details of the major acquisitions made in FY2023, FY2022, or FY2021. \| AMCOR_2023Q2_10Q: extractor: The provided pages do not contain a list or description of major acquisitions made by Amcor in FY2021, FY2022, or FY2023. Page 8 shows a line item for 'Business acquisitions' of $(54) million for the six months ended December 31, 2022, but does not name the acquired companies. Page 34 mentions the sale of Russian facilities, not acquisitions. No other pages list specific acquisition names or details for the requested fiscal years. \| AMCOR_2023Q4_EARNINGS: extractor: The provided pages mention that Amcor completed 'three bolt-on acquisitions' during fiscal 2023 (Page 2) and list 'Business acquisitions and Investments in affiliated companies, and other' as a cash outflow of $(177) million for FY2023 and $(12) million for FY2022 (Page 9). However, the document does not name the specific companies acquired in FY2023, FY2022, or FY2021, nor does it provide a list of major acquisitions for these periods.

**Pages searched:** `AMCOR_2023_10K` pages 4, 6, 50, 51, 52, 53, 54, 55, 90, 102, 105, 107, 151; `AMCOR_2023Q2_10Q` pages 4, 5, 6, 7, 8, 9, 10, 25, 34, 36, 39, 42; `AMCOR_2023Q4_EARNINGS` pages 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14

<details><summary>Gold answer</summary>

Amcor completed these acquisitions during FY2023: -100% equity interest of a flexibles manufacturing company in the Czech Republic - 100% equity interest in a medical device packaging manufacturing site in Shanghai, China. -acquisition of a New Zealand-based leading manufacturer of state-of-the-art, automated protein packaging machines.
</details>

## 26. What industry does AMCOR primarily operate in?

`financebench_id_01148` · filing `AMCOR_2023_10K` · domain-relevant

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `AMCOR_2023_10K` pages 4, 5, 12, 14, 46, 50, 51, 52, 53, 54, 90, 105, 107; `AMCOR_2022_10K` pages 4, 5, 11, 29, 45, 49, 51, 52, 53, 87, 102, 104; `AMCOR_2021_10K` pages 7, 12, 21, 49, 51, 52, 53, 63, 88, 98, 103, 105

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMCOR_2023Q4_EARNINGS: extractor: The provided pages contain information about restructuring costs and activities (e.g., 'Restructuring, impairment and other related activities, net' in the income statement and 'material restructuring programs' in the non-GAAP reconciliation), but they do not contain a balance sheet or specific disclosure detailing the 'nature & purpose' of the 'restructuring liability' as of the Q2 FY2023 close (which would be December 31, 2022, or the quarter ended December 31, 2022). The document focuses on Q4 FY2023 (ended June 30, 2023) and full-year results, and does not provide the specific liability breakdown for the Q2 period.

**Pages searched:** `AMCOR_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14

<details><summary>Gold answer</summary>

87% of the total restructuring liability is related Employee liabilities.
</details>

## 29. What Was AMCOR's Adjusted Non GAAP EBITDA for FY 2023

`financebench_id_01928` · filing `AMCOR_2023Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Amcor's Adjusted Non-GAAP EBITDA for fiscal year 2023 was 2,018 million. This figure is reported in the "Adjusted non-GAAP results" table for the twelve months ended June 30, 2023 [v1]. The value represents a 5% decrease from the prior year's adjusted EBITDA of 2,117 million [v1].

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

**Answer:** The real change in sales for Amcor in FY 2023 versus FY 2022, excluding the impact of FX movements and other non-comparable items, was 0% [v1]. This is confirmed by the reported "Comparable constant currency ∆%" of "—" for Net sales, which the system computed as 0% [v1]. The document states that net sales were "in line with the prior year on a comparable constant currency basis" [v1].

**Computation:** `comparable_constant_currency_growth_pct = 0%  where comparable_constant_currency_growth_pct = — (units, FY2023)`

- **v1** · `AMCOR_2023Q4_EARNINGS` · PDF page **1** · column Comparable constant currency ∆% · units
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

**Answer:** The FY2015 depreciation and amortization margin for AMD is 4.18%. This is calculated by dividing the depreciation and amortization expense of $167 million [v1] by the net revenue of $3,991 million [v2].

**Computation:** `da_2015 / net_revenue_2015 = 4.18%  where da_2015 = 167 (millions, FY2015), net_revenue_2015 = $3,991 (millions, FY2015)`

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

**Reason:** AMD_2022_10K: code checks failed twice: formula: unknown value name 'total_current_liabilities_2022' (names: []) \| AMD_2022_annualreport: extractor: The provided pages do not contain the Consolidated Balance Sheet (referenced as Page 58 in the index on Page 113, but the page content is not included). Consequently, the specific line items required to calculate the quick ratio—specifically Accounts Receivable, Inventory, and Total Current Liabilities—are not available in the text. While Page 51 provides the aggregate value for 'Cash, cash equivalents and short-term investments' ($5.9 billion), it does not provide the necessary components to compute the quick ratio formula: (Cash + Short-term Investments + Accounts Receivable) / Current Liabilities.

**Pages searched:** `AMD_2022_10K` pages 1, 4, 5, 41, 43, 44, 51, 54, 56, 58, 60, 101; `AMD_2022_annualreport` pages 6, 7, 9, 10, 21, 49, 51, 52, 53, 60, 69, 113

<details><summary>Gold answer</summary>

Yes. The quick ratio is 1.57, calculated as (cash and cash equivalents+Short term investments+Accounts receivable, net+receivables from related parties)/ (current liabilities).
</details>

## 33. What are the major products and services that AMD sells as of FY22?

`financebench_id_00995` · filing `AMD_2022_10K` · domain-relevant

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `AMD_2022_10K` pages 4, 5, 6, 7, 8, 11, 43, 44, 54, 56, 58, 60; `AMD_2022_annualreport` pages 2, 4, 6, 9, 10, 11, 12, 13, 17, 51, 52, 69

<details><summary>Gold answer</summary>

AMD sells server microprocessors (CPUs) and graphics processing units (GPUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), and Adaptive System-on-Chip (SoC) products for data centers; CPUs, accelerated processing units (APUs) that integrate CPUs and GPUs, and chipsets for desktop and notebook personal computers; discrete GPUs, and semi-custom SoC products and development services; and embedded CPUs, GPUs, APUs, FPGAs, and Adaptive SoC products.
</details>

## 34. What drove revenue change as of the FY22 for AMD?

`financebench_id_01198` · filing `AMD_2022_10K` · domain-relevant

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `AMD_2022_10K` pages 4, 5, 9, 11, 43, 44, 54, 55, 56, 58, 60, 102; `AMD_2022_annualreport` pages 2, 3, 4, 5, 9, 10, 17, 51, 53, 65, 69, 114

<details><summary>Gold answer</summary>

In 2022, AMD reported Higher sales of their EPYC server processors, higher semi-custom product sales, and the inclusion of Xilinx embedded product sales
</details>

## 35. What drove operating margin change as of the FY22 for AMD? If operating margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00917` · filing `AMD_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** AMD_2022_10K: code checks failed twice: formula: unknown value name 'operating_income_2022' (names: []) \| AMD_2022_annualreport: code checks failed twice: formula: unknown value name 'operating_income_2022_text' (names: ['net_revenue_2022'])

**Pages searched:** `AMD_2022_10K` pages 4, 5, 8, 9, 43, 49, 54, 56, 58, 60, 73, 102; `AMD_2022_annualreport` pages 2, 6, 9, 10, 13, 14, 21, 51, 58, 81, 83, 105

<details><summary>Gold answer</summary>

The decrease in AMD's operating income was primarily driven by amortization of intangible assets associated with the Xilinx acquisition
</details>

## 36. Among operations, investing, and financing activities, which brought in the most (or lost the least) cash flow for AMD in FY22?

`financebench_id_01279` · filing `AMD_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Operating activities brought in the most cash flow for AMD in FY22 with $3,565 million [v1]. This amount is higher than the $1,999 million from investing activities [v2] and the $(3,264) million used in financing activities [v3]. The computed maximum of these three values confirms operating activities as the highest at 3,565 million [COMPUTED RESULT].

**Computation:** `max(operating_activities_2022, investing_activities_2022, financing_activities_2022) = 3,565 million  where operating_activities_2022 = $3,565 (millions, FY2022), investing_activities_2022 = 1,999 (millions, FY2022), financing_activities_2022 = (3,264) (millions, FY2022)`

- **v1** · `AMD_2022_annualreport` · PDF page **60** · column December 31, 2022 · millions
  - Quote: "Operating activities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| $3,565"

  <details><summary>Passage</summary>

  ```
  cash and cash equivalents held domestically was 73% as of December 31, 2022, and 91% as of December 25,
  2021.
  Our operating, investing and financing cash flow activities for 2022 and 2021 were as follows:
   | December 31, 2022  December 25, 2021
   | (In millions)
  Net cash provided by (used in):
  Operating activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $3,565 | $3,521
  Investing activities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,999 | (686)
  Financing activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | (3,264) | (1,895)
  Net increase in cash and cash equivalents . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $2,300 | $940
  Our aggregate principal debt obligations were $2.5 billion as of December 31, 2022, which consisted primarily of
  $1.5 billion of the Xilinx Notes assumed as part of the Xilinx acquisition and $1.0 billion of 3.924% Notes and
  4.393% Notes issued during the year, compared to $313 million as of December 25, 2021, respectively. We
  ```
  </details>

- **v2** · `AMD_2022_annualreport` · PDF page **60** · column December 31, 2022 · millions
  - Quote: "Investing activities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| 1,999"

  <details><summary>Passage</summary>

  ```
  2021.
  Our operating, investing and financing cash flow activities for 2022 and 2021 were as follows:
   | December 31, 2022  December 25, 2021
   | (In millions)
  Net cash provided by (used in):
  Operating activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $3,565 | $3,521
  Investing activities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,999 | (686)
  Financing activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | (3,264) | (1,895)
  Net increase in cash and cash equivalents . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $2,300 | $940
  Our aggregate principal debt obligations were $2.5 billion as of December 31, 2022, which consisted primarily of
  $1.5 billion of the Xilinx Notes assumed as part of the Xilinx acquisition and $1.0 billion of 3.924% Notes and
  4.393% Notes issued during the year, compared to $313 million as of December 25, 2021, respectively. We
  repaid $312 million of our 7.50% Senior Notes that matured in August 2022.
  ```
  </details>

- **v3** · `AMD_2022_annualreport` · PDF page **60** · column December 31, 2022 · millions
  - Quote: "Financing activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| (3,264)"

  <details><summary>Passage</summary>

  ```
  Our operating, investing and financing cash flow activities for 2022 and 2021 were as follows:
   | December 31, 2022  December 25, 2021
   | (In millions)
  Net cash provided by (used in):
  Operating activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $3,565 | $3,521
  Investing activities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,999 | (686)
  Financing activities  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | (3,264) | (1,895)
  Net increase in cash and cash equivalents . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $2,300 | $940
  Our aggregate principal debt obligations were $2.5 billion as of December 31, 2022, which consisted primarily of
  $1.5 billion of the Xilinx Notes assumed as part of the Xilinx acquisition and $1.0 billion of 3.924% Notes and
  4.393% Notes issued during the year, compared to $313 million as of December 25, 2021, respectively. We
  repaid $312 million of our 7.50% Senior Notes that matured in August 2022.
  On April 29, 2022, we entered into a revolving credit agreement (Revolving Credit Agreement) with Wells Fargo
  ```
  </details>

<details><summary>Gold answer</summary>

In 2022, AMD brought in the most cashflow from Operations
</details>

## 37. From FY21 to FY22, excluding Embedded, in which AMD reporting segment did sales proportionally increase the most?

`financebench_id_00563` · filing `AMD_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The Data Center segment experienced the highest proportional sales increase, with a computed maximum growth rate of 63.5896% [COMPUTED RESULT]. This increase is derived from the Data Center revenue rising from $3,694 million in FY2021 to $6,043 million in FY2022 [v1, v2]. In comparison, the Client segment revenue decreased from $6,887 million to $6,201 million [v3, v4], and the Gaming segment revenue increased from $5,607 million to $6,805 million [v5, v6].

**Computation:** `max((dc_2022 - dc_2021) / dc_2021, (client_2022 - client_2021) / client_2021, (gaming_2022 - gaming_2021) / gaming_2021) = 63.5896%  where dc_2021 = 3,694 (millions, FY2021), dc_2022 = 6,043 (millions, FY2022), client_2021 = 6,887 (millions, FY2021), client_2022 = 6,201 (millions, FY2022), gaming_2021 = 5,607 (millions, FY2021), gaming_2022 = 6,805 (millions, FY2022)`

- **v1** · `AMD_2022_annualreport` · PDF page **57** · column December 25, 2021 · millions
  - Quote: "Data Center \| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| $6,043 \| $3,694"

  <details><summary>Passage</summary>

  ```
  2021:
   | Year Ended
   | December 31,  December 25,
   | 2022 | 2021
   | (In millions)
    Net revenue:
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $6,043 | $3,694
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,201 | 6,887
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,805 | 5,607
   | Embedded | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 4,552 | 246
    Total net revenue  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $23,601 | $16,434
    Operating income (loss):
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $1,848 | $991
  ```
  </details>

- **v2** · `AMD_2022_annualreport` · PDF page **57** · column December 31, 2022 · millions
  - Quote: "Data Center \| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| $6,043 \| $3,694"

  <details><summary>Passage</summary>

  ```
  2021:
   | Year Ended
   | December 31,  December 25,
   | 2022 | 2021
   | (In millions)
    Net revenue:
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $6,043 | $3,694
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,201 | 6,887
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,805 | 5,607
   | Embedded | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 4,552 | 246
    Total net revenue  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $23,601 | $16,434
    Operating income (loss):
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $1,848 | $991
  ```
  </details>

- **v3** · `AMD_2022_annualreport` · PDF page **57** · column December 25, 2021 · millions
  - Quote: "Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| 6,201 \| 6,887"

  <details><summary>Passage</summary>

  ```
   | Year Ended
   | December 31,  December 25,
   | 2022 | 2021
   | (In millions)
    Net revenue:
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $6,043 | $3,694
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,201 | 6,887
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,805 | 5,607
   | Embedded | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 4,552 | 246
    Total net revenue  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $23,601 | $16,434
    Operating income (loss):
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $1,848 | $991
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,190 | 2,088
  ```
  </details>

- **v4** · `AMD_2022_annualreport` · PDF page **57** · column December 31, 2022 · millions
  - Quote: "Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| 6,201 \| 6,887"

  <details><summary>Passage</summary>

  ```
   | Year Ended
   | December 31,  December 25,
   | 2022 | 2021
   | (In millions)
    Net revenue:
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $6,043 | $3,694
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,201 | 6,887
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,805 | 5,607
   | Embedded | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 4,552 | 246
    Total net revenue  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $23,601 | $16,434
    Operating income (loss):
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $1,848 | $991
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,190 | 2,088
  ```
  </details>

- **v5** · `AMD_2022_annualreport` · PDF page **57** · column December 25, 2021 · millions
  - Quote: "Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| 6,805 \| 5,607"

  <details><summary>Passage</summary>

  ```
   | December 31,  December 25,
   | 2022 | 2021
   | (In millions)
    Net revenue:
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $6,043 | $3,694
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,201 | 6,887
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,805 | 5,607
   | Embedded | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 4,552 | 246
    Total net revenue  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $23,601 | $16,434
    Operating income (loss):
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $1,848 | $991
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,190 | 2,088
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 953 | 934
  ```
  </details>

- **v6** · `AMD_2022_annualreport` · PDF page **57** · column December 31, 2022 · millions
  - Quote: "Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \| 6,805 \| 5,607"

  <details><summary>Passage</summary>

  ```
   | December 31,  December 25,
   | 2022 | 2021
   | (In millions)
    Net revenue:
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $6,043 | $3,694
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,201 | 6,887
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 6,805 | 5,607
   | Embedded | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 4,552 | 246
    Total net revenue  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $23,601 | $16,434
    Operating income (loss):
   | Data Center | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | $1,848 | $991
   | Client  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1,190 | 2,088
   | Gaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 953 | 934
  ```
  </details>

<details><summary>Gold answer</summary>

Data Center
</details>

## 38. Did AMD report customer concentration in FY22?

`financebench_id_00757` · filing `AMD_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, AMD reported customer concentration in FY22, stating that one customer accounted for 16% of its consolidated net revenue for the year ended December 31, 2022 [v1]. The company noted that sales to this customer came from its Gaming segment and that losing this customer would have a material adverse effect on its business [v1].

- **v1** · `AMD_2022_annualreport` · PDF page **17** · column N/A · units
  - Quote: "One customer accounted for 16% of our consolidated net revenue for the year ended December 31, 2022."

  <details><summary>Passage</summary>

  ```
  customers in designing, testing and qualifying system designs that incorporate our products. We believe that our
  commitment to customer service and design support improves our customers’ time-to-market and fosters
  relationships that encourage customers to use the next generation of our products.
  We also work with our customers to create differentiated products that leverage our CPU, GPU and APU
  technology. Certain customers pay us non-recurring engineering fees for design and development services and a
  purchase price for the resulting products.
  One customer accounted for 16% of our consolidated net revenue for the year ended December 31, 2022. Sales to
  this customer consisted of sales of products from our Gaming segment. A loss of this customer would have a
  material adverse effect on our business.
   | 9
  ```
  </details>

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

**Answer:** American Express primarily operates in the United States, with its largest concentrations outside the U.S. located in the United Kingdom, Japan, the European Union, Australia, Canada, and Mexico [v1, v2]. The company's most significant credit risk concentration in 2022 was with individuals, of which the majority were in the United States [v2]. These geographic regions represent the areas with the largest concentration of credit exposure for the company as of December 31, 2022 [v1].

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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, American Express has an improving operating margin profile, with the margin increasing by 0.39% compared to the prior year [COMPUTED RESULT]. This improvement is based on total revenues net of interest expense of 52,862 million and total expenses of 41,095 million for the current period, versus 42,380 million in revenues and 33,110 million in expenses for the prior period [v1, v2, v3, v4]. Operating margin is a useful metric for this company as it reflects profitability after accounting for interest expenses and operating costs [v1, v3]. The computed result confirms a positive change in the margin between the two fiscal years [COMPUTED RESULT].

**Computation:** `((total_revenues_net_of_interest_expense_2022 - total_expenses_2022) / total_revenues_net_of_interest_expense_2022) - ((total_revenues_net_of_interest_expense_2021 - total_expenses_2021) / total_revenues_net_of_interest_expense_2021) = 0.39%  where total_revenues_net_of_interest_expense_2022 = 52,862 (millions, FY2022), total_revenues_net_of_interest_expense_2021 = 42,380 (millions, FY2021), total_expenses_2022 = 41,095 (millions, FY2022), total_expenses_2021 = 33,110 (millions, FY2021)`

- **v1** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2022 · millions
  - Quote: "Total revenues net of interest expense \| 52,862"

  <details><summary>Passage</summary>

  ```
   | Total interest income | 12,658 | 9,033 | 10,083
   Interest expense
    Deposits | 1,527 | 458 | 943
    Long-term debt and other | 1,236 | 825 | 1,155
   | Total interest expense | 2,763 | 1,283 | 2,098
   | Net interest income | 9,895 | 7,750 | 7,985
   Total revenues net of interest expense | 52,862 | 42,380 | 36,087
   Provisions for credit losses
    Card Member receivables | 627 | (73) | 1,015
    Card Member loans | 1,514 | (1,155) | 3,453
    Other | 41 | (191) | 262
   | Total provisions for credit losses | 2,182 | (1,419) | 4,730
   Total revenues net of interest expense after provisions for credit losses | 50,680 | 43,799 | 31,357
  ```
  </details>

- **v2** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2021 · millions
  - Quote: "Total revenues net of interest expense \| 42,380"

  <details><summary>Passage</summary>

  ```
   | Total interest income | 12,658 | 9,033 | 10,083
   Interest expense
    Deposits | 1,527 | 458 | 943
    Long-term debt and other | 1,236 | 825 | 1,155
   | Total interest expense | 2,763 | 1,283 | 2,098
   | Net interest income | 9,895 | 7,750 | 7,985
   Total revenues net of interest expense | 52,862 | 42,380 | 36,087
   Provisions for credit losses
    Card Member receivables | 627 | (73) | 1,015
    Card Member loans | 1,514 | (1,155) | 3,453
    Other | 41 | (191) | 262
   | Total provisions for credit losses | 2,182 | (1,419) | 4,730
   Total revenues net of interest expense after provisions for credit losses | 50,680 | 43,799 | 31,357
  ```
  </details>

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

- **v4** · `AMERICANEXPRESS_2022_10K` · PDF page **96** · column 2021 · millions
  - Quote: "Total expenses \| 33,110"

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

Performance is not measured through operating margin
</details>

## 42. What drove gross margin change as of the FY2022 for American Express? If gross margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00720` · filing `AMERICANEXPRESS_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Gross margin is not a useful metric for American Express because it is a financial services company where revenue is primarily derived from non-interest sources like discount revenue and interest income rather than the cost of goods sold typical of product-based businesses [v1, v2, v3, v4]. The provided financial statements for FY2022 list specific revenue and expense line items but do not calculate or report a gross margin figure, as the industry standard for such firms focuses on net interest income and operating expenses instead [v1, v5, v10]. Consequently, analyzing gross margin change is not applicable to this company's financial structure.

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

**Answer:** No, American Water Works does not have positive working capital for FY2022, as its total current assets of $1,250 million were less than its total current liabilities of $2,811 million [v1, v2]. The computed working capital is -$1,561 million, indicating a negative balance [COMPUTED RESULT]. This metric is relevant for the company, but the negative value reflects its specific capital structure and industry characteristics rather than a lack of utility for the metric itself.

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** BESTBUY_2024Q2_10Q: verifier: answer_supported=no. The computation of the absolute difference between the two percentages is mathematically incorrect. The difference between 23.2% and 22.1% is 1.1 percentage points, not 110.0%. Therefore, the conclusion that the margins are not consistent (fluctuating more than 2%) is incorrect based on the provided data.

**Pages searched:** `BESTBUY_2024Q2_10Q` pages 1, 3, 4, 5, 7, 8, 14, 15, 16, 17, 18, 19

<details><summary>Gold answer</summary>

Yes, the margins have been consistent, there has been a minor decline of 1.1% in gross margins between FY2022 and FY2023.
</details>

## 52. What are major acquisitions that Best Buy has done in FY2023, FY2022 and FY2021?

`financebench_id_01077` · filing `BESTBUY_2023_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BESTBUY_2023_10K: code checks failed twice: fy2022_acquisitions_text: the quote is not on page 4. Copy it exactly from one line of the page \| BESTBUY_2023_8K_dated-2023-04-12: extractor: The provided pages (Item 1.01, Item 1.02, Item 9.01, and the attached Credit Agreement) describe a new credit facility entered into on April 12, 2023, and the termination of a previous facility. They do not contain any information regarding major acquisitions made by Best Buy in FY2023, FY2022, or FY2021. \| BESTBUY_2023_8K_dated-2023-04-24: extractor: The provided pages (1 and 2 of the Form 8-K dated April 24, 2023) only contain the cover page and Item 5.02 regarding the departure of a director. They do not contain any information about acquisitions made by Best Buy in FY2023, FY2022, or FY2021.

**Pages searched:** `BESTBUY_2023_10K` pages 4, 21, 23, 39, 40, 42, 43, 44, 50, 66, 69; `BESTBUY_2023_8K_dated-2023-04-12` pages 2, 3, 4, 115, 135, 136, 143, 144, 145, 146, 147, 148; `BESTBUY_2023_8K_dated-2023-04-24` pages 1, 2

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

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `None`, verifier `None`

**Reason:** the question does not identify a company in the corpus: which company?

**Pages searched:** none

<details><summary>Gold answer</summary>

Yes, there was a decline of ~42% between FY2023 and Q2 of FY 2024.
</details>

## 55. Was there any change in the number of Best Buy stores between Q2 of FY2024 and FY2023?

`financebench_id_00460` · filing `BESTBUY_2024Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** BESTBUY_2024Q2_EARNINGS: extractor: The provided pages do not contain the number of Best Buy stores for Q2 FY2024 or FY2023. The document includes financial metrics such as revenue, operating income, and comparable sales, but does not list store counts. \| BESTBUY_2023Q4_EARNINGS: extractor: The provided pages do not contain data on the number of Best Buy stores for Q2 of FY2024 or FY2023. The document is an earnings release for Q4 FY2023 and includes financial statements, segment results, and guidance for FY2024, but does not list store counts for the requested periods.

**Pages searched:** `BESTBUY_2024Q2_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12; `BESTBUY_2023Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

<details><summary>Gold answer</summary>

Yes, there is decline in number stores by 1.32% from 982 stores in Q2 FY 2023 to 969 by the end of Q2 FY2024.
</details>

## 56. Which Best Buy product category performed the best (by top line) in the domestic (USA) Market during Q2 of FY2024?

`financebench_id_01902` · filing `BESTBUY_2024Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The product category that performed the best by top line in the domestic market during Q2 of FY2024 was Computing and Mobile Phones, which accounted for 41% of the revenue mix [v1]. This share was higher than Consumer Electronics at 30% [v2], Appliances at 16% [v3], Entertainment at 6% [v4], Services at 6% [v5], and Other at 1% [v6].

- **v1** · `BESTBUY_2024Q2_EARNINGS` · PDF page **9** · column July 29, 2023 · units
  - Quote: "Computing and Mobile Phones \| 41 %"

  <details><summary>Passage</summary>

  ```
  | BEST BUY CO., INC.
   | REVENUE CATEGORY SUMMARY
   | (Unaudited and subject to reclassification)
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  Domestic Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 41 % | 42 % | (6.4)% | (16.6)%
  Consumer Electronics | 30 % | 30 % | (5.7)% | (14.7)%
  Appliances | 16 % | 17 % | (16.1)% | (1.2)%
  Entertainment | 6 % | 5 % | 9.0 % | (9.2)%
  Services | 6 % | 5 % | 7.6 % | (8.5)%
  Other | 1 % | 1 % | 2.4 % | 15.6 %
    Total | 100 % | 100 % | (6.3)% | (12.7)%
  ```
  </details>

- **v2** · `BESTBUY_2024Q2_EARNINGS` · PDF page **9** · column July 29, 2023 · units
  - Quote: "Consumer Electronics \| 30 %"

  <details><summary>Passage</summary>

  ```
   | REVENUE CATEGORY SUMMARY
   | (Unaudited and subject to reclassification)
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  Domestic Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 41 % | 42 % | (6.4)% | (16.6)%
  Consumer Electronics | 30 % | 30 % | (5.7)% | (14.7)%
  Appliances | 16 % | 17 % | (16.1)% | (1.2)%
  Entertainment | 6 % | 5 % | 9.0 % | (9.2)%
  Services | 6 % | 5 % | 7.6 % | (8.5)%
  Other | 1 % | 1 % | 2.4 % | 15.6 %
    Total | 100 % | 100 % | (6.3)% | (12.7)%
   | Revenue Mix | Comparable Sales
  ```
  </details>

- **v3** · `BESTBUY_2024Q2_EARNINGS` · PDF page **9** · column July 29, 2023 · units
  - Quote: "Appliances \| 16 %"

  <details><summary>Passage</summary>

  ```
   | (Unaudited and subject to reclassification)
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  Domestic Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 41 % | 42 % | (6.4)% | (16.6)%
  Consumer Electronics | 30 % | 30 % | (5.7)% | (14.7)%
  Appliances | 16 % | 17 % | (16.1)% | (1.2)%
  Entertainment | 6 % | 5 % | 9.0 % | (9.2)%
  Services | 6 % | 5 % | 7.6 % | (8.5)%
  Other | 1 % | 1 % | 2.4 % | 15.6 %
    Total | 100 % | 100 % | (6.3)% | (12.7)%
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  ```
  </details>

- **v4** · `BESTBUY_2024Q2_EARNINGS` · PDF page **9** · column July 29, 2023 · units
  - Quote: "Entertainment \| 6 %"

  <details><summary>Passage</summary>

  ```
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  Domestic Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 41 % | 42 % | (6.4)% | (16.6)%
  Consumer Electronics | 30 % | 30 % | (5.7)% | (14.7)%
  Appliances | 16 % | 17 % | (16.1)% | (1.2)%
  Entertainment | 6 % | 5 % | 9.0 % | (9.2)%
  Services | 6 % | 5 % | 7.6 % | (8.5)%
  Other | 1 % | 1 % | 2.4 % | 15.6 %
    Total | 100 % | 100 % | (6.3)% | (12.7)%
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  International Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  ```
  </details>

- **v5** · `BESTBUY_2024Q2_EARNINGS` · PDF page **9** · column July 29, 2023 · units
  - Quote: "Services \| 6 %"

  <details><summary>Passage</summary>

  ```
   | Three Months Ended | Three Months Ended
  Domestic Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 41 % | 42 % | (6.4)% | (16.6)%
  Consumer Electronics | 30 % | 30 % | (5.7)% | (14.7)%
  Appliances | 16 % | 17 % | (16.1)% | (1.2)%
  Entertainment | 6 % | 5 % | 9.0 % | (9.2)%
  Services | 6 % | 5 % | 7.6 % | (8.5)%
  Other | 1 % | 1 % | 2.4 % | 15.6 %
    Total | 100 % | 100 % | (6.3)% | (12.7)%
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  International Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 45 % | 43 % | (2.4)% | (7.6)%
  ```
  </details>

- **v6** · `BESTBUY_2024Q2_EARNINGS` · PDF page **9** · column July 29, 2023 · units
  - Quote: "Other \| 1 %"

  <details><summary>Passage</summary>

  ```
  Domestic Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 41 % | 42 % | (6.4)% | (16.6)%
  Consumer Electronics | 30 % | 30 % | (5.7)% | (14.7)%
  Appliances | 16 % | 17 % | (16.1)% | (1.2)%
  Entertainment | 6 % | 5 % | 9.0 % | (9.2)%
  Services | 6 % | 5 % | 7.6 % | (8.5)%
  Other | 1 % | 1 % | 2.4 % | 15.6 %
    Total | 100 % | 100 % | (6.3)% | (12.7)%
   | Revenue Mix | Comparable Sales
   | Three Months Ended | Three Months Ended
  International Segment | July 29, 2023 | July 30, 2022 | July 29, 2023 | July 30, 2022
  Computing and Mobile Phones | 45 % | 43 % | (2.4)% | (7.6)%
  Consumer Electronics | 28 % | 29 % | (10.4)% | (4.8)%
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

**Answer:** The total revenue growth rate for Block from FY2019 to FY2020 is 101.5%. This figure is calculated by taking the difference between the FY2020 total net revenue of $9,497,578 thousand and the FY2019 total net revenue of $4,713,500 thousand, then dividing by the FY2019 revenue [v1, v2].

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

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Block generated $173.1 million in cash flow from operating activities in FY2020 [v1]. This figure is derived from the consolidated statements of cash flows, which report net cash provided by operating activities as 173,110 thousand for the year ended December 31, 2020 [v1].

**Computation:** `net_cash_operating_2020 = 173.1 million  where net_cash_operating_2020 = 173,110 (thousands, FY2020)`

- **v1** · `BLOCK_2021_10K` · PDF page **88** · column 2020 · thousands
  - Quote: "Net cash provided by operating activities \| 847,830 \| 173,110 \| 327,630"

  <details><summary>Passage</summary>

  ```
   | Settlements receivable | (346,217) | (547,484) | (326,596)
   | Purchases and originations of loans | (3,227,172) | (1,837,137) | (2,266,738)
   | Sales, principal payments, and forgiveness of loans | 3,067,344 | 1,505,406 | 2,168,682
   | Customers payable | 171,555 | 371,598 | 181,520
   | Settlements payable | 15,249 | 143,528 | 41,697
   | Other assets and liabilities | (61,983) | (185,308) | (47,480)
   | Net cash provided by operating activities | 847,830 | 173,110 | 327,630
  Cash flows from investing activities:
   | Purchase of marketable debt securities | (2,714,560) | (1,322,362) | (992,583)
   | Proceeds from maturities of marketable debt securities | 831,019 | 607,134 | 430,888
   | Proceeds from sale of marketable debt securities | 617,097 | 585,427 | 548,619
   | Purchase of marketable debt securities from customer funds | (488,851) | (642,252) | (311,499)
   | Proceeds from maturities of marketable debt securities from customer funds | 505,501 | 382,887 | 158,055
  ```
  </details>

<details><summary>Gold answer</summary>

$382.00
</details>

## 60. We need to calculate a financial metric by using information only provided within the balance sheet. Please answer the following question: what is Boeing's year end FY2018 net property, plant, and equipment (in USD millions)?

`financebench_id_10285` · filing `BOEING_2018_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing's year-end FY2018 net property, plant, and equipment is 12,645 million USD. This value is reported directly in the Consolidated Statements of Financial Position for the year ended December 31, 2018 [v1].

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

**Reason:** BOEING_2022_10K: number check (G4) failed twice: numbers not in the evidence or the result: 20%

**Pages searched:** `BOEING_2022_10K` pages 22, 24, 27, 29, 38, 41, 55, 56, 57, 59, 61, 83

<details><summary>Gold answer</summary>

Yes. Boeing has product and service categories that represent more than 20% of Boeing's revenue for FY2022. These categories are Commercial Airplanes which comprises 39% of total revenue, Defence which comprises 35% of total revenue and Services which comprises 26% of total revenue.
</details>

## 62. Has Boeing reported any materially important ongoing legal battles from FY2022?

`financebench_id_01091` · filing `BOEING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Boeing reported materially important ongoing legal battles in FY2022, including multiple actions related to the 737 MAX accidents and an arbitration dispute with Embraer over terminated agreements [v1, v3]. The company stated it cannot reasonably estimate the range of loss for the remaining pending lawsuits regarding the 737 MAX or the potential loss from the Embraer arbitration [v2, v4].

- **v1** · `BOEING_2022_10K` · PDF page **113** · column Note 21 · units
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

- **v2** · `BOEING_2022_10K` · PDF page **113** · column Note 21 · units
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

- **v3** · `BOEING_2022_10K` · PDF page **113** · column Note 21 · units
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

- **v4** · `BOEING_2022_10K` · PDF page **113** · column Note 21 · units
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

**Reason:** BOEING_2022_10K: code checks failed twice: context_787_loss: raw 'During the fourth quarter of 2021, we recorded a loss of $3.5 billion on the 787 program primarily due to rework driving longer delivery delays than were previously expected and associated customer考虑.' does not appear in its quote

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Boeing's business is subject to cyclicality. The company states that the airline industry has historically been cyclical and experienced significant profit swings [v1]. This is evidenced by the fluctuation in total revenues from 58,158 million to 66,608 million and the varying operating losses reported in the financial statements [v2, v3, v4, v5, v6, v7].

- **v1** · `BOEING_2022_10K` · PDF page **8** · column Item 1A. Risk Factors · units
  - Quote: "Historically, the airline industry has been cyclical and very competitive and has experienced significant profit swings and constant challenges to be more cost competitive."

  <details><summary>Passage</summary>

  ```
  Risks Related to Our Business and Operations
  We depend heavily on commercial airlines, subjecting us to unique risks.
  Market conditions have a significant impact on demand for our commercial aircraft and related services. The commercial aircraft market is
  predominantly driven by long-term trends in airline passenger and cargo traffic. The principal factors underlying long-term traffic growth are
  sustained economic growth and political stability both in developed and emerging markets. Demand for our commercial aircraft is further
  influenced by  airline  profitability,  availability of  aircraft financing, world trade policies, government-to-government relations, technological
  advances, price and other competitive factors, fuel prices, terrorism, pandemics, epidemics and environmental regulations. Historically, the
  airline industry has been cyclical and very competitive and has experienced significant profit swings and constant challenges to be more cost
  competitive. Significant deterioration in the global economic environment, the airline industry generally or the financial stability of one or more of
  our major customers could result in fewer new orders for aircraft or services, or could cause customers to seek to postpone or cancel contractual
  orders and/or payments to us, which could result in lower revenues, profitability and cash flows and a reduction in our contractual backlog. In
  addition, because our commercial aircraft backlog consists of aircraft scheduled for delivery over a period of several years, any of these
  macroeconomic, industry or customer impacts could unexpectedly affect deliveries over a long period.
  ```
  </details>

- **v2** · `BOEING_2022_10K` · PDF page **55** · column 2022 · millions
  - Quote: "Total revenues \| 66,608"

  <details><summary>Passage</summary>

  ```
   | The Boeing Company and Subsidiaries
   | Consolidated Statements of Operations
  (Dollars in millions, except per share data)
  Years ended December 31, | 2022 | 2021 | 2020
  Sales of products | $55,893 | $51,386 | $47,142
  Sales of services | 10,715 | 10,900 | 11,016
  Total revenues | 66,608 | 62,286 | 58,158
  Cost of products | (53,969) | (49,954) | (54,568)
  Cost of services | (9,109) | (9,283) | (9,232)
  Boeing Capital interest expense | (28) | (32) | (43)
  Total costs and expenses | (63,106) | (59,269) | (63,843)
   | 3,502 | 3,017 | (5,685)
  (Loss)/income from operating investments, net | (16) | 210 | 9
  ```
  </details>

- **v3** · `BOEING_2022_10K` · PDF page **55** · column 2021 · millions
  - Quote: "Total revenues \| 62,286"

  <details><summary>Passage</summary>

  ```
   | The Boeing Company and Subsidiaries
   | Consolidated Statements of Operations
  (Dollars in millions, except per share data)
  Years ended December 31, | 2022 | 2021 | 2020
  Sales of products | $55,893 | $51,386 | $47,142
  Sales of services | 10,715 | 10,900 | 11,016
  Total revenues | 66,608 | 62,286 | 58,158
  Cost of products | (53,969) | (49,954) | (54,568)
  Cost of services | (9,109) | (9,283) | (9,232)
  Boeing Capital interest expense | (28) | (32) | (43)
  Total costs and expenses | (63,106) | (59,269) | (63,843)
   | 3,502 | 3,017 | (5,685)
  (Loss)/income from operating investments, net | (16) | 210 | 9
  ```
  </details>

- **v4** · `BOEING_2022_10K` · PDF page **55** · column 2020 · millions
  - Quote: "Total revenues \| 58,158"

  <details><summary>Passage</summary>

  ```
   | The Boeing Company and Subsidiaries
   | Consolidated Statements of Operations
  (Dollars in millions, except per share data)
  Years ended December 31, | 2022 | 2021 | 2020
  Sales of products | $55,893 | $51,386 | $47,142
  Sales of services | 10,715 | 10,900 | 11,016
  Total revenues | 66,608 | 62,286 | 58,158
  Cost of products | (53,969) | (49,954) | (54,568)
  Cost of services | (9,109) | (9,283) | (9,232)
  Boeing Capital interest expense | (28) | (32) | (43)
  Total costs and expenses | (63,106) | (59,269) | (63,843)
   | 3,502 | 3,017 | (5,685)
  (Loss)/income from operating investments, net | (16) | 210 | 9
  ```
  </details>

- **v5** · `BOEING_2022_10K` · PDF page **55** · column 2022 · millions
  - Quote: "Loss from operations \| (3,547)"

  <details><summary>Passage</summary>

  ```
  Total costs and expenses | (63,106) | (59,269) | (63,843)
   | 3,502 | 3,017 | (5,685)
  (Loss)/income from operating investments, net | (16) | 210 | 9
  General and administrative expense | (4,187) | (4,157) | (4,817)
  Research and development expense, net | (2,852) | (2,249) | (2,476)
  Gain on dispositions, net | 6 | 277 | 202
  Loss from operations | (3,547) | (2,902) | (12,767)
  Other income, net | 1,058 | 551 | 447
  Interest and debt expense | (2,533) | (2,682) | (2,156)
  Loss before income taxes | (5,022) | (5,033) | (14,476)
  Income tax (expense)/benefit | (31) | 743 | 2,535
  Net loss | (5,053) | (4,290) | (11,941)
  Less: net loss attributable to noncontrolling interest | (118) | (88) | (68)
  ```
  </details>

- **v6** · `BOEING_2022_10K` · PDF page **55** · column 2021 · millions
  - Quote: "Loss from operations \| (2,902)"

  <details><summary>Passage</summary>

  ```
  Total costs and expenses | (63,106) | (59,269) | (63,843)
   | 3,502 | 3,017 | (5,685)
  (Loss)/income from operating investments, net | (16) | 210 | 9
  General and administrative expense | (4,187) | (4,157) | (4,817)
  Research and development expense, net | (2,852) | (2,249) | (2,476)
  Gain on dispositions, net | 6 | 277 | 202
  Loss from operations | (3,547) | (2,902) | (12,767)
  Other income, net | 1,058 | 551 | 447
  Interest and debt expense | (2,533) | (2,682) | (2,156)
  Loss before income taxes | (5,022) | (5,033) | (14,476)
  Income tax (expense)/benefit | (31) | 743 | 2,535
  Net loss | (5,053) | (4,290) | (11,941)
  Less: net loss attributable to noncontrolling interest | (118) | (88) | (68)
  ```
  </details>

- **v7** · `BOEING_2022_10K` · PDF page **55** · column 2020 · millions
  - Quote: "Loss from operations \| (12,767)"

  <details><summary>Passage</summary>

  ```
  Total costs and expenses | (63,106) | (59,269) | (63,843)
   | 3,502 | 3,017 | (5,685)
  (Loss)/income from operating investments, net | (16) | 210 | 9
  General and administrative expense | (4,187) | (4,157) | (4,817)
  Research and development expense, net | (2,852) | (2,249) | (2,476)
  Gain on dispositions, net | 6 | 277 | 202
  Loss from operations | (3,547) | (2,902) | (12,767)
  Other income, net | 1,058 | 551 | 447
  Interest and debt expense | (2,533) | (2,682) | (2,156)
  Loss before income taxes | (5,022) | (5,033) | (14,476)
  Income tax (expense)/benefit | (31) | 743 | 2,535
  Net loss | (5,053) | (4,290) | (11,941)
  Less: net loss attributable to noncontrolling interest | (118) | (88) | (68)
  ```
  </details>

<details><summary>Gold answer</summary>

Yes, Boeing's business is subject to cyclicality due to its exposure to the airline industry which is a cyclical industry.
</details>

## 66. What production rate changes is Boeing forecasting for FY2023?

`financebench_id_00494` · filing `BOEING_2022_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Boeing forecasts increasing the 787 production rate to 5 per month, resuming 777X production, and gradually increasing 737 production rates in 2023 [v1, v2, v3]. These changes are based on market demand and supply chain capacity [v3]. The company aims to stabilize operations and meet customer demand through these adjustments [v1, v2, v3].

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

**Answer:** The FY2017 return on assets (ROA) for Coca-Cola is 1.42%. This result is calculated by dividing the 2017 net income of $1,248 million by the average of the 2017 total assets ($87,896 million) and 2016 total assets ($87,270 million) [v1, v2, v3].

**Computation:** `net_income_2017 / avg(total_assets_2017, total_assets_2016) = 1.42%  where net_income_2017 = 1,248 (millions, FY2017), total_assets_2017 = 87,896 (millions, FY2017), total_assets_2016 = 87,270 (millions, FY2016)`

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

**Answer:** Coca-Cola's FY2021 COGS % margin is 39.7%. This is calculated by dividing the Cost of goods sold of $15,357 million by the Net Operating Revenues of $38,655 million as reported in the 2021 income statement [v1, v2].

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

**Answer:** Coca-Cola's FY2022 dividend payout ratio is 79.82%. This is calculated by dividing the total cash dividends paid of $7,616 million [v1] by the net income attributable to shareowners of $9,542 million [v2]. The computed result of 79.82% reflects the portion of earnings distributed as dividends [v1, v2].

**Computation:** `abs(dividends_paid_2022) / net_income_shareowners_2022 = 79.82%  where dividends_paid_2022 = (7,616) (millions, FY2022), net_income_shareowners_2022 = 9,542 (millions, FY2022)`

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

**Answer:** The FY2020 days payable outstanding (DPO) for Corning is 63.86 days. This result is derived from the accounts payable values of 1,174 and 1,587, the cost of sales of 7,772, and the inventory values of 2,438 and 2,320 [v1, v2, v3, v4, v5]. The calculation follows the provided formula using these specific figures to arrive at the computed result of 63.86 [v1, v2, v3, v4, v5].

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

**Answer:** The 3-year average unadjusted operating income margin for Corning is 10.3% [v1, v2, v3, v4, v5, v6]. This figure represents the average of the operating income to net sales ratios for the three fiscal years, calculated using the specific operating income and net sales values provided for each year [v1, v2, v3, v4, v5, v6].

**Computation:** `avg((operating_income_2019 / net_sales_2019), (operating_income_2020 / net_sales_2020), (operating_income_2021 / net_sales_2021)) = 10.3%  where operating_income_2019 = 1,306 (millions, FY2019), net_sales_2019 = $11,503 (millions, FY2019), operating_income_2020 = 509 (millions, FY2020), net_sales_2020 = $11,303 (millions, FY2020), operating_income_2021 = 2,112 (millions, FY2021), net_sales_2021 = $14,082 (millions, FY2021)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** CORNING_2022_10K: verifier: answer_supported=no. The computation is incorrect. The change in the effective tax rate is 22.9% - 20.2% = 2.7 percentage points, or a percentage change of (22.9 - 20.2) / 20.2 = 13.36%. The provided computation (270.0%) is mathematically incorrect. \| CORNING_2021_10K: extractor: The provided filing is the 10-K for fiscal year 2021. It contains the effective tax rate for FY2021 (20.5%) and FY2020 (17.8%), but does not contain any financial data or effective tax rate for FY2022. \| CORNING_2023Q2_10Q: extractor: The provided pages contain the effective tax rate for the six months ended June 30, 2023 (22.4%) and June 30, 2022 (22.6%), but do not contain the effective tax rate for the full fiscal years FY2021 or FY2022. The document is a 10-Q for Q2 2023 and does not include the full-year 2021 or 2022 data required to answer the question.

**Pages searched:** `CORNING_2022_10K` pages 24, 26, 32, 52, 58, 59, 60, 61, 62, 77, 79, 95; `CORNING_2021_10K` pages 2, 29, 49, 58, 59, 65, 67, 68, 69, 76, 86, 88; `CORNING_2023Q2_10Q` pages 3, 5, 6, 7, 9, 22, 23, 25, 32, 38, 39, 40

<details><summary>Gold answer</summary>

The effective tax rate of Corning has changed from 20% in FY2021 to 23% in FY 2022.
</details>

## 74. Does Corning have positive working capital based on FY2022 data? If working capital is not a useful or relevant metric for this company, then please state that and explain why.

`financebench_id_00005` · filing `CORNING_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Corning has positive working capital based on FY2022 data. The company's total current assets of $7,453 million exceeded its total current liabilities of $5,175 million, resulting in a computed working capital of $2,278 million [v1, v2]. This metric is relevant for Corning as it is a standard measure of short-term financial health for operating companies. The positive balance indicates the company has sufficient current assets to cover its current obligations.

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

**Answer:** The FY2018 fixed asset turnover ratio for CVS Health is 17.98. This result is calculated by dividing the total revenues of $194,579 million in 2018 by the average of the net property and equipment values of $11,349 million in 2018 and $10,292 million in 2017 [v1, v2, v3]. The computed ratio of 17.98 reflects the efficiency of the company's fixed assets in generating revenue for that fiscal year [COMPUTED RESULT].

**Computation:** `total_revenues_2018 / avg(ppe_net_2018, ppe_net_2017) = 17.98  where total_revenues_2018 = 194,579 (millions, FY2018), ppe_net_2018 = 11,349 (millions, FY2018), ppe_net_2017 = 10,292 (millions, FY2017)`

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** CVSHEALTH_2022_10K: code checks failed twice: formula: unknown value name 'total_revenues_2022' (names: [])

**Pages searched:** `CVSHEALTH_2022_10K` pages 1, 14, 68, 108, 109, 110, 111, 113, 142, 168, 191, 193

<details><summary>Gold answer</summary>

Yes, CVS Health requires an extensive asset base to operate, which is evident from its ROA of only 1.82% in 2022 and 3.39% in 2021, though it should be noted that a significant portion of this asset base is goodwill, and CVS's fixed assets/total assets ratio is on the lower side of 5.6%.
</details>

## 78. Has CVS Health reported any materially important ongoing legal battles from 2022, 2021 and 2020?

`financebench_id_01107` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** CVSHEALTH_2022_10K: code checks failed twice: stockholder_matters_ltc: raw 'Beginning in February 2019, multiple class action complaints, as well as a derivative complaint, were filed by putative plaintiffs against the Company and certain current and former officers and dirs.' does not appear in its quote \| CVSHEALTH_2021_10K: code checks failed twice: litigation_2021_erisa: raw 'In August and September 2020, two class actions under the Employee Retirement Income Security Act of 1974 (“ERISA”) were filed in the U.S. District Court for the District of Connecticut against CVS, A' does not appear in its quote \| CVSHEALTH_2020_10K: extractor: The provided filing is the 10-K for fiscal year 2020 (filed in 2021). It contains information regarding legal proceedings and regulatory risks up to the filing date (e.g., Page 26 mentions a December 2020 Supreme Court decision and general ongoing agreements), but it does not contain information about legal battles occurring in 2022, as that period is outside the scope of the document.

**Pages searched:** `CVSHEALTH_2022_10K` pages 3, 19, 20, 36, 75, 108, 109, 110, 111, 113, 175, 177; `CVSHEALTH_2021_10K` pages 20, 25, 37, 41, 75, 84, 105, 106, 107, 108, 110, 170; `CVSHEALTH_2020_10K` pages 26, 39, 44, 50, 73, 83, 103, 104, 105, 106, 108, 171

<details><summary>Gold answer</summary>

Yes, CVS Health has been involved in multiple ongoing legal battles. Some notable legal dispute areas for CVS are: (1) usual and customary pricing litigation: where it's claimed that CVSâs retail pharmacies overcharged for prescription drugs; (2) PBM litigation and investigations: where it's claimed that that rebate agreements between the drug manufacturers and PBMs caused inflated prices for certain drug products; and (3) controlled substances litigation: legal matters around opioids for which CVS has agreed to pay up to $4.3 billion to claimants in remediation and $625 million to attorneys and fees
</details>

## 79. Has CVS Health paid dividends to common shareholders in Q2 of FY2022?

`financebench_id_01244` · filing `CVSHEALTH_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, CVS Health paid dividends to common shareholders in Q2 of FY2022. The company has paid cash dividends every quarter since becoming a public company, and the quarterly cash dividend for 2022 was $0.55 per share [v1, v2].

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

**Answer:** Yes, Foot Locker's new CEO, Mary N. Dillon, has previous CEO experience at Ulta Beauty, Inc., which is a similar retailer in the beauty and personal care sector [v1, v3]. Foot Locker is described as a leading footwear and apparel retailer, while Ulta Beauty operates in a comparable retail environment focused on consumer goods [v2, v3]. Ms. Dillon served as CEO of Ulta Beauty from July 2013 through June 2021 before joining Foot Locker in September 2022 [v1, v3].

- **v1** · `FOOTLOCKER_2023_10K` · PDF page **18** · column Executive Name · units
  - Quote: "Mary N. Dillon \| Chief Executive Officer since September 2022. Previously, Ms. Dillon served as Chief Executive Officer of Ulta Beauty, Inc. from July 2013 through June 2021."

  <details><summary>Passage</summary>

  ```
  Not applicable.
  Item 4A. Information about our Executive Officers
  The following table provides information with respect to all persons serving as executive officers as of March 27, 2023,
  including business experience for the last five years.
   | Executive
  Name | Position | Age | Officer Since
  Mary N. Dillon | Chief Executive Officer since September 2022. Previously, Ms. Dillon served | 61 | 2022
   | as Chief Executive Officer of Ulta Beauty, Inc. from July 2013 through June
   | 2021.
  Franklin R. Bracken | Executive Vice President and Chief Commercial Officer since December | 50 | 2021
   | 2022. Previously, he served as Executive Vice President and Chief Operating
   | Officer from November 2021 through December 2022, Executive Vice
   | President and Chief Executive Officer — North America from July 2020
  ```
  </details>

- **v2** · `FOOTLOCKER_2023_10K` · PDF page **4** · column General · units
  - Quote: "Foot Locker, Inc. is a leading footwear and apparel retailer that unlocks the “inner sneakerhead” in all of us."

  <details><summary>Passage</summary>

  ```
  PART I
  Item 1. Business
  General
  Foot Locker, Inc., incorporated under the laws of the State of New York in 1989. Foot Locker, Inc. and its subsidiaries
  hereafter are referred to as the “Registrant,” “Company,” “we,” “our,” or “us.” Foot Locker, Inc. has  its corporate
  headquarters in New York.
  Foot Locker, Inc. is a leading footwear and apparel retailer that unlocks the “inner sneakerhead” in all of us. As of
  January 28, 2023, we operated 2,714 stores in 29 countries across North America, Europe, Australia, New Zealand,
  and Asia, and a franchised store presence in the Middle East and Asia. Foot Locker, Inc. has a strong history of sneaker
  authority that sparks discovery and ignites the power of sneaker culture through  its portfolio of brands, including
  Foot Locker, Kids Foot Locker, Champs Sports, WSS, and atmos.
  Ensuring that our customers can engage with us in the most convenient manner for them whether in our stores, on our
  website, or on our mobile application, is a high priority for us. We use our omni-channel capabilities to bridge the digital
  ```
  </details>

- **v3** · `FOOTLOCKER_2023_10K` · PDF page **18** · column Position · units
  - Quote: "Previously, Ms. Dillon served as Chief Executive Officer of Ulta Beauty, Inc. from July 2013 through June 2021."

  <details><summary>Passage</summary>

  ```
  Not applicable.
  Item 4A. Information about our Executive Officers
  The following table provides information with respect to all persons serving as executive officers as of March 27, 2023,
  including business experience for the last five years.
   | Executive
  Name | Position | Age | Officer Since
  Mary N. Dillon | Chief Executive Officer since September 2022. Previously, Ms. Dillon served | 61 | 2022
   | as Chief Executive Officer of Ulta Beauty, Inc. from July 2013 through June
   | 2021.
  Franklin R. Bracken | Executive Vice President and Chief Commercial Officer since December | 50 | 2021
   | 2022. Previously, he served as Executive Vice President and Chief Operating
   | Officer from November 2021 through December 2022, Executive Vice
   | President and Chief Executive Officer — North America from July 2020
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. She was previous CEO of Ulta Beauty which means she had to manage a large retail company that has brick and mortar + online business. So yes she was a CEO in a similar company to Foot Locker before this.
</details>

## 81. Were there any board member nominees who had substantially more votes against joining than the other nominees?

`financebench_id_00822` · filing `FOOTLOCKER_2022_8K_dated-2022-05-20` · novel-generated

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `None`, verifier `None`

**Reason:** the question does not identify a company in the corpus: which company?

**Pages searched:** none

<details><summary>Gold answer</summary>

Yes, his name is Richard A. Johnson
</details>

## 82. What is the FY2019 cash conversion cycle (CCC) for General Mills? CCC is defined as: DIO + DSO - DPO. DIO is defined as: 365 * (average inventory between FY2018 and FY2019) / (FY2019 COGS). DSO is defined as: 365 * (average accounts receivable between FY2018 and FY2019) / (FY2019 Revenue). DPO is defined as: 365 * (average accounts payable between FY2018 and FY2019) / (FY2019 COGS + change in inventory between FY2018 and FY2019). Round your answer to two decimal places. Address the question by using the line items and information shown within the income statement and the balance sheet.

`financebench_id_04103` · filing `GENERALMILLS_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2019 cash conversion cycle (CCC) for General Mills is -3.70 days. This result is derived from the FY2019 cost of sales of 11,108.4 million, net sales of 16,865.2 million, and the average inventory, receivables, and payables figures from fiscal years 2018 and 2019 [v1, v2, v3, v4, v5, v6, v7, v8]. The calculation follows the provided formula using these specific line items to arrive at the final computed value [v1, v2, v3, v4, v5, v6, v7, v8].

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

**Answer:** General Mills's FY2020 working capital ratio is 0.68. This result is calculated by dividing the total current assets of $5,121.3 million by the total current liabilities of $7,491.5 million as reported in the consolidated balance sheets [v1, v2]. The computed ratio of 0.68 indicates that the company had fewer current assets than current liabilities for that fiscal year [v1, v2].

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

**Answer:** The FY2020 free cash flow for General Mills is 3,215.4 million USD. This is calculated by subtracting the absolute value of capital expenditures (460.8 million) from the net cash provided by operating activities (3,676.2 million) [v1, v2]. The computed result confirms this difference is 3,215.4 million [COMPUTED RESULT].

**Computation:** `net_cash_provided_by_operating_activities_2020 - abs(purchases_of_land_buildings_and_equipment_2020) = 3,215.4 million  where net_cash_provided_by_operating_activities_2020 = 3,676.2 (millions, FY2020), purchases_of_land_buildings_and_equipment_2020 = (460.8) (millions, FY2020)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2022 retention ratio for General Mills is 54.03%. This is calculated by subtracting the absolute value of dividends paid ($1,244.5 million) from net earnings attributable to General Mills ($2,707.3 million) and dividing the result by the net earnings [v1, v2]. The computed result confirms that 54.03% of the net earnings were retained by the company in fiscal year 2022.

**Computation:** `(net_earnings_attributable_to_general_mills_2022 - abs(dividends_paid_2022)) / net_earnings_attributable_to_general_mills_2022 = 54.03%  where net_earnings_attributable_to_general_mills_2022 = $2,707.3 (millions, FY2022), dividends_paid_2022 = (1,244.5) (millions, FY2022)`

- **v1** · `GENERALMILLS_2023_10K` · PDF page **42** · column 2022 · millions
  - Quote: "Net earnings attributable to General Mills \| $2,707.3"

  <details><summary>Passage</summary>

  ```
  Earnings before income taxes and after-tax earnings from joint ventures | 3,140.5 | 3,209.6 | 2,857.4
  Income taxes | 612.2 | 586.3 | 629.1
  After-tax earnings from joint ventures | 81.3 | 111.7 | 117.7
  Net earnings, including earnings attributable to redeemable and
    noncontrolling interests | 2,609.6 | 2,735.0 | 2,346.0
  Net earnings attributable to redeemable and noncontrolling interests | 15.7 | 27.7 | 6.2
  Net earnings attributable to General Mills | $2,593.9  $2,707.3  $2,339.8
  Earnings per share — basic | $4.36  $4.46  $3.81
  Earnings per share — diluted | $4.31  $4.42  $3.78
  Dividends per share | $2.16  $2.04  $2.02
  See accompanying notes to consolidated financial statements.
   | 42
  ```
  </details>

- **v2** · `GENERALMILLS_2023_10K` · PDF page **46** · column 2022 · millions
  - Quote: "Dividends paid \| (1,244.5)"

  <details><summary>Passage</summary>

  ```
   Change in notes payable | (769.3) | 551.4 | 71.7
    Issuance of long-term debt | 2,324.4 | 2,203.7 | 1,576.5
    Payment of long-term debt | (1,421.7) | (3,140.9) | (2,609.0)
    Debt exchange participation incentive cash payment | - | - | (201.4)
    Proceeds from common stock issued on exercised options | 232.3 | 161.7 | 74.3
    Purchases of common stock for treasury | (1,403.6) | (876.8) | (301.4)
    Dividends paid | (1,287.9) | (1,244.5) | (1,246.4)
    Distributions to noncontrolling and redeemable interest holders | (15.7) | (129.8) | (48.9)
    Other, net | (62.6) | (28.0) | (30.9)
   | Net cash used by financing activities | (2,404.1) | (2,503.2) | (2,715.5)
  Effect of exchange rate changes on cash and cash equivalents | (12.0) | (58.0) | 72.5
  Increase (decrease) in cash and cash equivalents | 16.1 | (935.8) | (172.6)
  Cash and cash equivalents - beginning of year | 569.4 | 1,505.2 | 1,677.8
  ```
  </details>

<details><summary>Gold answer</summary>

0.54
</details>

## 86. Are JnJ's FY2022 financials that of a high growth company?

`financebench_id_00956` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, Johnson & Johnson's FY2022 financials do not reflect those of a high growth company, as total sales grew by only 1.2% and net earnings declined from the prior year [v1, v2, v3, v4]. While the MedTech segment saw a 1.4% increase, the overall company performance indicates modest growth rather than high growth [v5]. The computed sales growth rate of 1.2% further confirms this limited expansion [COMPUTED RESULT].

**Computation:** `(sales_2022 - sales_2021) / sales_2021 = 1.2%  where sales_2022 = 94,943 (millions, FY2022), sales_2021 = 93,775 (millions, FY2021), net_earnings_2022 = 17,941 (millions, FY2022), net_earnings_2021 = 20,878 (millions, FY2021), medtech_growth_rate = 1.4% (units, FY2022)`

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

- **v2** · `JOHNSON_JOHNSON_2022_10K` · PDF page **47** · column 2021 · millions
  - Quote: "Sales to customers \| 93,775"

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

- **v3** · `JOHNSON_JOHNSON_2022_10K` · PDF page **47** · column 2022 · millions
  - Quote: "Net earnings \| $17,941"

  <details><summary>Passage</summary>

  ```
   Interest income | (490) | (53) | (111)
   Interest expense, net of portion capitalized (Note 4) | 276 | 183 | 201
   Other (income) expense, net | 1,871 | 489 | 2,899
   Restructuring (Note 20) | 321 | 252 | 247
   Earnings before provision for taxes on income | 21,725 | 22,776 | 16,497
   Provision for taxes on income (Note 8) | 3,784 | 1,898 | 1,783
  Net earnings | $17,941 | 20,878 | 14,714
  Net earnings per share (Notes 1 and 15)
   | Basic | $6.83 | 7.93 | 5.59
   | Diluted | $6.73 | 7.81 | 5.51
   Average shares outstanding (Notes 1 and 15)
    Basic | 2,625.2 | 2,632.1 | 2,632.8
    Diluted | 2,663.9 | 2,674.0 | 2,670.7
  ```
  </details>

- **v4** · `JOHNSON_JOHNSON_2022_10K` · PDF page **47** · column 2021 · millions
  - Quote: "Net earnings \| 20,878"

  <details><summary>Passage</summary>

  ```
   Interest income | (490) | (53) | (111)
   Interest expense, net of portion capitalized (Note 4) | 276 | 183 | 201
   Other (income) expense, net | 1,871 | 489 | 2,899
   Restructuring (Note 20) | 321 | 252 | 247
   Earnings before provision for taxes on income | 21,725 | 22,776 | 16,497
   Provision for taxes on income (Note 8) | 3,784 | 1,898 | 1,783
  Net earnings | $17,941 | 20,878 | 14,714
  Net earnings per share (Notes 1 and 15)
   | Basic | $6.83 | 7.93 | 5.59
   | Diluted | $6.73 | 7.81 | 5.51
   Average shares outstanding (Notes 1 and 15)
    Basic | 2,625.2 | 2,632.1 | 2,632.8
    Diluted | 2,663.9 | 2,674.0 | 2,670.7
  ```
  </details>

- **v5** · `JOHNSON_JOHNSON_2022_10K` · PDF page **33** · column 2022 · units
  - Quote: "an increase of 1.4% from 2021"

  <details><summary>Passage</summary>

  ```
  MedTech Segment**
  The MedTech segment sales in 2022 were $27.4 billion, an increase of 1.4% from 2021, which included operational growth of 6.2% and a negative
  currency impact of 4.8%. U.S. sales were $13.4 billion, an increase of 5.4% as compared to the prior year. International sales were $14.1 billion, a decrease
  of 2.3% as compared to the prior year, which included operational growth of 6.9% and a negative currency impact of 9.2%. In 2022, the net impact of
  acquisitions and divestitures on the MedTech segment worldwide operational sales growth was a positive 0.1%.
   | Major MedTech Franchise Sales*:
   | Total | Operations | Currency
   (Dollars in Millions) | 2022 | 2021 | Change | Change | Change
  ```
  </details>

<details><summary>Gold answer</summary>

No, JnJ's FY2022 financials are not of a high growth company as sales grew by 1.3% in FY2022.
</details>

## 87. What drove gross margin change as of FY2022 for JnJ? If gross margin is not a useful metric for a company like this, then please state that and explain why.

`financebench_id_00669` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The gross margin for Johnson & Johnson decreased by 0.9% in FY2022 compared to FY2021 [v1, v2, v3, v4]. This decline occurred because the cost of products sold increased from 29,855 million to 31,089 million while sales increased from $93,775 million to $94,943 million [v5, v6, v3, v4]. Gross margin is a useful metric for this company as it measures the profitability of its core product sales [v1, v3].

**Computation:** `((gross_profit_2022 / sales_2022) - (gross_profit_2021 / sales_2021)) = -0.9%  where gross_profit_2022 = 63,854 (millions, FY2022), gross_profit_2021 = 63,920 (millions, FY2021), sales_2022 = $94,943 (millions, FY2022), sales_2021 = $93,775 (millions, FY2021), cost_of_products_sold_2022 = 31,089 (millions, FY2022), cost_of_products_sold_2021 = 29,855 (millions, FY2021)`

- **v1** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2022 · millions
  - Quote: "Gross Profit \| 63,854"

  <details><summary>Passage</summary>

  ```
  (Unaudited; in Millions Except Per Share Figures) | TWELVE MONTHS
   | 2022 | 2021 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $94,943 | 100.0 | $93,775 | 100.0 | 1.3
  Cost of products sold | 31,089 | 32.7 | 29,855 | 31.8 | 4.1
  Gross Profit | 63,854 | 67.3 | 63,920 | 68.2 | (0.1)
  Selling, marketing and administrative expenses | 24,765 | 26.1 | 24,659 | 26.3 | 0.4
  Research and development expense | 14,603 | 15.4 | 14,714 | 15.7 | (0.8)
  In-process research and development | 783 | 0.8 | 900 | 1.0
  Interest (income) expense, net | (214) | (0.2) | 130 | 0.1
  Other (income) expense, net | 1,871 | 2.0 | 489 | 0.5
  Restructuring | 321 | 0.3 | 252 | 0.3
  ```
  </details>

- **v2** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2021 · millions
  - Quote: "Gross Profit \| 63,920"

  <details><summary>Passage</summary>

  ```
  (Unaudited; in Millions Except Per Share Figures) | TWELVE MONTHS
   | 2022 | 2021 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $94,943 | 100.0 | $93,775 | 100.0 | 1.3
  Cost of products sold | 31,089 | 32.7 | 29,855 | 31.8 | 4.1
  Gross Profit | 63,854 | 67.3 | 63,920 | 68.2 | (0.1)
  Selling, marketing and administrative expenses | 24,765 | 26.1 | 24,659 | 26.3 | 0.4
  Research and development expense | 14,603 | 15.4 | 14,714 | 15.7 | (0.8)
  In-process research and development | 783 | 0.8 | 900 | 1.0
  Interest (income) expense, net | (214) | (0.2) | 130 | 0.1
  Other (income) expense, net | 1,871 | 2.0 | 489 | 0.5
  Restructuring | 321 | 0.3 | 252 | 0.3
  ```
  </details>

- **v3** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2022 · millions
  - Quote: "Sales to customers \| $94,943"

  <details><summary>Passage</summary>

  ```
  Johnson & Johnson and Subsidiaries
  Condensed Consolidated Statement of Earnings
  (Unaudited; in Millions Except Per Share Figures) | TWELVE MONTHS
   | 2022 | 2021 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $94,943 | 100.0 | $93,775 | 100.0 | 1.3
  Cost of products sold | 31,089 | 32.7 | 29,855 | 31.8 | 4.1
  Gross Profit | 63,854 | 67.3 | 63,920 | 68.2 | (0.1)
  Selling, marketing and administrative expenses | 24,765 | 26.1 | 24,659 | 26.3 | 0.4
  Research and development expense | 14,603 | 15.4 | 14,714 | 15.7 | (0.8)
  In-process research and development | 783 | 0.8 | 900 | 1.0
  Interest (income) expense, net | (214) | (0.2) | 130 | 0.1
  ```
  </details>

- **v4** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2021 · millions
  - Quote: "Sales to customers \| $93,775"

  <details><summary>Passage</summary>

  ```
  Johnson & Johnson and Subsidiaries
  Condensed Consolidated Statement of Earnings
  (Unaudited; in Millions Except Per Share Figures) | TWELVE MONTHS
   | 2022 | 2021 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $94,943 | 100.0 | $93,775 | 100.0 | 1.3
  Cost of products sold | 31,089 | 32.7 | 29,855 | 31.8 | 4.1
  Gross Profit | 63,854 | 67.3 | 63,920 | 68.2 | (0.1)
  Selling, marketing and administrative expenses | 24,765 | 26.1 | 24,659 | 26.3 | 0.4
  Research and development expense | 14,603 | 15.4 | 14,714 | 15.7 | (0.8)
  In-process research and development | 783 | 0.8 | 900 | 1.0
  Interest (income) expense, net | (214) | (0.2) | 130 | 0.1
  ```
  </details>

- **v5** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2022 · millions
  - Quote: "Cost of products sold \| 31,089"

  <details><summary>Passage</summary>

  ```
  Condensed Consolidated Statement of Earnings
  (Unaudited; in Millions Except Per Share Figures) | TWELVE MONTHS
   | 2022 | 2021 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $94,943 | 100.0 | $93,775 | 100.0 | 1.3
  Cost of products sold | 31,089 | 32.7 | 29,855 | 31.8 | 4.1
  Gross Profit | 63,854 | 67.3 | 63,920 | 68.2 | (0.1)
  Selling, marketing and administrative expenses | 24,765 | 26.1 | 24,659 | 26.3 | 0.4
  Research and development expense | 14,603 | 15.4 | 14,714 | 15.7 | (0.8)
  In-process research and development | 783 | 0.8 | 900 | 1.0
  Interest (income) expense, net | (214) | (0.2) | 130 | 0.1
  Other (income) expense, net | 1,871 | 2.0 | 489 | 0.5
  ```
  </details>

- **v6** · `JOHNSON_JOHNSON_2022Q4_EARNINGS` · PDF page **11** · column 2021 · millions
  - Quote: "Cost of products sold \| 29,855"

  <details><summary>Passage</summary>

  ```
  Condensed Consolidated Statement of Earnings
  (Unaudited; in Millions Except Per Share Figures) | TWELVE MONTHS
   | 2022 | 2021 | Percent
   | Percent | Percent | Increase
   | Amount | to Sales | Amount | to Sales | (Decrease)
  Sales to customers | $94,943 | 100.0 | $93,775 | 100.0 | 1.3
  Cost of products sold | 31,089 | 32.7 | 29,855 | 31.8 | 4.1
  Gross Profit | 63,854 | 67.3 | 63,920 | 68.2 | (0.1)
  Selling, marketing and administrative expenses | 24,765 | 26.1 | 24,659 | 26.3 | 0.4
  Research and development expense | 14,603 | 15.4 | 14,714 | 15.7 | (0.8)
  In-process research and development | 783 | 0.8 | 900 | 1.0
  Interest (income) expense, net | (214) | (0.2) | 130 | 0.1
  Other (income) expense, net | 1,871 | 2.0 | 489 | 0.5
  ```
  </details>

<details><summary>Gold answer</summary>

For FY22, JnJ had changes in gross margin due to: One-time COVID-19 vaccine manufacturing exit related costs, Currency impacts in the Pharmaceutical segment, Commodity inflation in the MedTech and Consumer Health segments, partially offset by Supply chain benefits in the Consumer Health segment.
</details>

## 88. Roughly how many times has JnJ sold its inventory in FY2022? Calculate inventory turnover ratio for FY2022; if conventional inventory management is not meaningful for the company then state that and explain why.

`financebench_id_00711` · filing `JOHNSON_JOHNSON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Johnson & Johnson sold its inventory approximately 2.72 times in FY2022. This inventory turnover ratio is calculated by dividing the cost of products sold of $31,089 million by the average of the beginning inventory of $10,387 million and the ending inventory of $12,483 million [v1, v2, v3]. The metric is meaningful for this company as it is a manufacturer with significant inventory holdings [v2, v3].

**Computation:** `cost_of_products_sold_2022 / avg(inventories_beginning_2022, inventories_ending_2022) = 2.72  where cost_of_products_sold_2022 = 31,089 (millions, FY2022), inventories_beginning_2022 = 10,387 (millions, FY2021), inventories_ending_2022 = 12,483 (millions, FY2022)`

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

- **v2** · `JOHNSON_JOHNSON_2022_10K` · PDF page **46** · column 2021 · millions
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

- **v3** · `JOHNSON_JOHNSON_2022_10K` · PDF page **46** · column 2022 · millions
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

<details><summary>Gold answer</summary>

JnJ sold its inventory 2.7 times in FY2022.
</details>

## 89. Is growth in JnJ's adjusted EPS expected to accelerate in FY2023?

`financebench_id_00651` · filing `JOHNSON_JOHNSON_2022Q4_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, growth in Johnson & Johnson's adjusted EPS is expected to accelerate in FY2023. The company projects a 12.5% growth rate at the mid-point for FY2023, which is a significant increase from the 5.0% growth rate at the mid-point for FY2022 [v1, v2]. This acceleration reflects updated guidance following the separation of the Kenvue business [v1].

- **v1** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **4** · column August 2023 · units
  - Quote: "Company expects 2023 Adjusted Reported Earnings Per Share (EPS) of $10.00 - $10.10, reflecting increased growth of 12.5% at the mid-point"

  <details><summary>Passage</summary>

  ```
  Exhibit 99.1
   | Johnson & Johnson Announces Updated Financials and 2023 Guidance Following Completion of the Kenvue
   | Separation
  •  Company expects increased 2023 Reported Sales Growth of 7.0% - 8.0%, Operational Sales Growth of 7.5% - 8.5%, and
   | Adjusted Operational Sales Growth of 6.2% - 7.2%; Figures exclude the COVID-19 Vaccine
  •  Company expects 2023 Adjusted Reported Earnings Per Share (EPS) of $10.00 - $10.10, reflecting increased growth of
   | 12.5% at the mid-point and Adjusted Operational EPS of $9.90 - $10.00, reflecting increased growth of 11.5% at the mid-
   | point
  •  Company reduced outstanding share count by approximately 191 million; 2023 guidance reflects only a partial-year benefit
   | of approximately 73.5 million shares or $0.28 benefit to EPS
  •  Company secured $13.2 billion in cash proceeds from the Kenvue debt offering and initial public offering and maintains 9.5%
   | of equity stake in Kenvue
  ```
  </details>

- **v2** · `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · PDF page **6** · column July 2023 · units
  - Quote: "Change vs. Prior Year / Mid-point \| 4.5% – 5.5% / 5.0%"

  <details><summary>Passage</summary>

  ```
  Change vs. Prior Year / Mid-point
  Operational Sales2,5 / Mid-point | $83.6B – $84.4B / $84.0B | $99.3B – $100.3B / $99.8B
  Change vs. Prior Year / Mid-point | 7.5% – 8.5% / 8.0% | 7.0% – 8.0% / 7.5%
  Reported Sales3,5 / Mid-point | $83.2B – $84.0B / $83.6B | $98.8B – $99.8B / $99.3B
  Change vs. Prior Year / Mid-point | 7.0% – 8.0% / 7.5% | 6.5% – 7.5% / 7.0%
  Adjusted Operational EPS (Diluted)2,4 / Mid-point | $9.90 – $10.00 / $9.95 | $10.60 – $10.70 / $10.65
  Change vs. Prior Year / Mid-point | 11.0% – 12.0% / 11.5% | 4.5% – 5.5% / 5.0%
  Adjusted EPS (Diluted)3,4 / Mid-point | $10.00 – $10.10 / $10.05 | $10.70 – $10.80 / $10.75
  Change vs. Prior Year / Mid-point | 12.0% – 13.0% / 12.5% | 5.5% – 6.5% / 6.0%
  Average Shares Outstanding (Diluted) | ~2,557.28 | 2,630.77
  1 Non-GAAP financial measure; excludes the net impact of acquisitions and divestitures
  2 Non-GAAP financial measure; excludes the impact of translational currency
  3 Calculated using Euro Average Rate: July 2023 = $1.09 (Illustrative purposes only)
  ```
  </details>

<details><summary>Gold answer</summary>

No, rate of growth in adjusted EPS is expected to decelerate slightly from 3.6% in FY2022 to 3.5% in FY2023.
</details>

## 90. How did JnJ's US sales growth compare to international sales growth in FY2022?

`financebench_id_01484` · filing `JOHNSON_JOHNSON_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** JOHNSON_JOHNSON_2022_10K: verifier: answer_supported=no. The computation is incorrect. The difference between a 3.0% increase and a 0.6% decrease is 3.6 percentage points (3.0% - (-0.6%) = 3.6%), not 240.0%. \| JOHNSON_JOHNSON_2022Q4_EARNINGS: verifier: answer_supported=no. The computation is incorrect. The difference between 3.0% and (0.6)% is 3.6 percentage points, not 360.0%. \| JOHNSON_JOHNSON_2023_8K_dated-2023-08-23: extractor: The provided document is a Form 8-K dated August 23, 2023, which reports on the completion of the Kenvue split-off. It does not contain the financial statements or sales data (US vs. International) for FY2022 required to answer the question.

**Pages searched:** `JOHNSON_JOHNSON_2022_10K` pages 28, 29, 30, 31, 33, 46, 47, 48, 49, 50, 81, 87; `JOHNSON_JOHNSON_2022Q4_EARNINGS` pages 1, 2, 3, 6, 8, 9, 10, 11, 13, 14, 19, 20; `JOHNSON_JOHNSON_2023_8K_dated-2023-08-23` pages 1, 2, 3

<details><summary>Gold answer</summary>

US sales increased 3.0% vs international sales decline of 0.6%.
</details>

## 91. Which business segment of JnJ will be treated as a discontinued operation from August 30, 2023 onward?

`financebench_id_01488` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2023Q1_EARNINGS: extractor: The provided pages mention the 'anticipated separation of the Company's Consumer Health business' (Page 6, Page 7) and list 'Consumer Health separation costs' (Page 21), but they do not state that any segment will be treated as a 'discontinued operation' starting from 'August 30, 2023'. The specific date and the accounting treatment of 'discontinued operation' are not present in the text. \| JOHNSON_JOHNSON_2023Q2_EARNINGS: extractor: The provided pages state that Johnson & Johnson intends to 'split off' Kenvue shares and mentions the separation of the Consumer Health business, but they do not explicitly state which business segment will be treated as a 'discontinued operation' from August 30, 2023 onward. The specific accounting treatment and date for discontinued operations are not present in the text.

**Pages searched:** `JOHNSON_JOHNSON_2023Q1_EARNINGS` pages 1, 2, 3, 5, 6, 7, 8, 10, 13, 16, 17, 21; `JOHNSON_JOHNSON_2023Q2_EARNINGS` pages 1, 3, 5, 6, 7, 8, 10, 11, 12, 16, 22, 23

<details><summary>Gold answer</summary>

The Consumer Health business segment will be treated as a discontinued operation from August 30, 2023 onward.
</details>

## 92. What is the amount of the gain accruing to JnJ as a result of the separation of its Consumer Health business segment, as of August 30, 2023?

`financebench_id_01490` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2023Q1_EARNINGS: extractor: The provided filing is for Q1 2023 (ended April 2, 2023) and does not contain financial data or specific gain amounts related to the separation of the Consumer Health business as of August 30, 2023. The document mentions separation costs of $300 million for Q1 2023 (Page 11, Page 21) and notes the anticipated separation in forward-looking statements (Page 6), but does not report a realized gain for the requested date. \| JOHNSON_JOHNSON_2023Q2_EARNINGS: extractor: The provided filing is for the second quarter of fiscal year 2023, with a release date of July 20, 2023. It does not contain financial data or information regarding the gain from the separation of the Consumer Health business as of August 30, 2023. The document only lists 'Consumer Health separation costs' (expenses) for the period ended July 2, 2023, not a gain accruing to the company as of the requested date.

**Pages searched:** `JOHNSON_JOHNSON_2023Q1_EARNINGS` pages 1, 2, 3, 5, 6, 7, 8, 10, 11, 16, 21, 22; `JOHNSON_JOHNSON_2023Q2_EARNINGS` pages 1, 3, 6, 7, 8, 10, 11, 12, 16, 22, 23, 24

<details><summary>Gold answer</summary>

JnJ will make a gain of approximately $20 billion from the separation of its Consumer Health business segment.
</details>

## 93. What is the amount of the cash proceeds that JnJ realised from the separation of Kenvue (formerly Consumer Health business segment), as of August 30, 2023?

`financebench_id_01491` · filing `JOHNSON_JOHNSON_2023_8K_dated-2023-08-30` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** JOHNSON_JOHNSON_2023Q1_EARNINGS: extractor: The provided filing is for Q1 2023 (ended April 2, 2023) and does not contain information regarding the cash proceeds from the separation of Kenvue as of August 30, 2023. Page 4 mentions the pricing of $7.75 Billion of Senior Notes issued by Kenvue Inc., but this is a debt issuance, not the cash proceeds from the separation, and the date is subsequent to the quarter but does not specify the August 30, 2023 proceeds. \| JOHNSON_JOHNSON_2023Q2_EARNINGS: extractor: The filing is dated July 20, 2023, and states that the separation of Kenvue is a future event ('intends to split off'). It does not contain information about cash proceeds realized as of August 30, 2023, nor does it cover that date.

**Pages searched:** `JOHNSON_JOHNSON_2023Q1_EARNINGS` pages 1, 3, 4, 5, 6, 7, 8, 10, 11, 16, 21, 22; `JOHNSON_JOHNSON_2023Q2_EARNINGS` pages 1, 3, 5, 6, 7, 8, 10, 11, 12, 16, 22, 23

<details><summary>Gold answer</summary>

JnJ realised $13.2 billion in cash proceeds from the separation of Kenvue.
</details>

## 94. Did JnJ's net earnings as a percent of sales increase in Q2 of FY2023 compared to Q2 of FY2022?

`financebench_id_01487` · filing `JOHNSON_JOHNSON_2023Q2_EARNINGS` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Johnson & Johnson's net earnings as a percent of sales increased in Q2 of FY2023 compared to Q2 of FY2022. The computed difference between the two periods' net earnings margins is 0.1072% [v1, v2, v3, v4]. This indicates that the ratio of net earnings to sales was higher in 2023 than in 2022.

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

**Reason:** JPMORGAN_2021Q1_10Q: code checks failed twice: ccb_net_revenue_2021: the quote is not on page 160. Copy it exactly from one line of the page; cib_net_revenue_2021: the quote is not on page 160. Copy it exactly from one line of the page; cb_net_revenue_2021: the quote is not on page 160. Copy it exactly from one line of the page \| JPMORGAN_2021Q2_10Q: extractor: The provided pages contain data for the three months ended June 30, 2021 (Q2 2021) and the six months ended June 30, 2021 (YTD Q2 2021). They do not contain a standalone table or data for the first quarter of 2021 (Q1 2021) alone. While Q1 data could theoretically be derived by subtracting Q2 from YTD, the pages do not explicitly state the Q1 values for each segment, and the instructions prohibit computing values not explicitly printed in the text. \| JPMORGAN_2021Q3_10Q: extractor: The provided pages contain financial data for the three months ended September 30, 2021 (Q3 2021) and the nine months ended September 30, 2021 (YTD 2021). They do not contain specific data for the first quarter (Q1) of 2021. While Q1 data could theoretically be derived by subtracting Q3 from YTD and then subtracting Q2 (which is also not provided), the pages do not contain the necessary Q2 data to isolate Q1 results for each segment.

**Pages searched:** `JPMORGAN_2021Q1_10Q` pages 4, 5, 23, 28, 31, 79, 81, 99, 102, 153, 160, 162; `JPMORGAN_2021Q2_10Q` pages 4, 23, 28, 32, 34, 38, 89, 90, 92, 113, 116, 169, 176, 179, 180; `JPMORGAN_2021Q3_10Q` pages 4, 22, 24, 29, 33, 35, 39, 91, 92, 94, 115, 118, 180, 183, 184

<details><summary>Gold answer</summary>

Corporate. Its net revenue was -$473 million.
</details>

## 96. If JPM went bankrupted by the end by 2021 Q1 and liquidated all of its assets to pay its shareholders, how much could each shareholder get?

`financebench_id_02119` · filing `JPMORGAN_2021Q1_10Q` · novel-generated

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** If JPMorgan went bankrupt and liquidated all assets to pay shareholders at the end of Q1 2021, each shareholder could theoretically receive $92.73. This amount is calculated by dividing the total stockholders' equity of $280,714 million by the 3,027,128,112 common shares outstanding [v1, v2]. This figure represents the book value per share based on the reported equity and share count [v1, v2].

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

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `JPMORGAN_2023Q1_10Q` pages 1, 4, 7, 28, 79, 81, 100, 103, 120, 157, 166, 167; `JPMORGAN_2022Q1_10Q` pages 1, 60, 61, 80, 82, 100, 102, 103, 104, 117, 120, 165; `JPMORGAN_2021Q1_10Q` pages 1, 4, 9, 28, 31, 79, 81, 99, 102, 119, 153, 162

<details><summary>Gold answer</summary>

Since JPM is a financial institution, gross margin is not a relevant metric.
</details>

## 98. In 2022 Q2, which of JPM's business segments had the highest net income?

`financebench_id_00394` · filing `JPMORGAN_2022Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** In Q2 2022, the Corporate & Investment Bank segment had the highest net income at $3,725 million [v2]. This amount exceeded the net income of Consumer & Community Banking ($3,100 million) [v1], Asset & Wealth Management ($1,004 million) [v4], and Commercial Banking ($994 million) [v3]. The computed maximum value across these segments is 3,725 million.

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

**Answer:** Yes, the risk JPM faced in the second fiscal quarter of 2023 decreased compared to the same period in the prior year. The average Total VaR for the three months ended June 30, 2023, was $47 million, which is lower than the $54 million average recorded for the same period in 2022 [v1, v2]. The document notes that average total VaR decreased for the three months ended June 30, 2023, compared with the same period in the prior year [v1, v2].

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

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `KRAFTHEINZ_2019_10K` pages 32, 50, 51, 52, 53, 54, 55, 77, 111, 112, 113, 114, 115, 116, 151; `KRAFTHEINZ_2020_10K` pages 23, 53, 54, 55, 56, 57, 67, 68, 72, 86, 113, 120; `KRAFTHEINZ_2018_10K` pages 62, 64, 65, 66, 76, 138, 139, 140, 141, 142, 143, 145, 146, 147, 171, 173, 175, 177, 179, 181, 203, 204, 205, 206, 207, 208, 209, 210, 211

<details><summary>Gold answer</summary>

6.25
</details>

## 101. We need to calculate a reasonable approximation (or exact number if possible) of a financial metric. Basing your judgment by information plainly provided in the balance sheet and the P&L statement, what is Lockheed Martin's FY2020 asset turnover ratio? Asset turnover ratio is defined as: FY2020 revenue / (average total assets between FY2019 and FY2020). Round your answer to two decimal places.

`financebench_id_04412` · filing `LOCKHEEDMARTIN_2020_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Lockheed Martin's FY2020 asset turnover ratio is 1.33. This is calculated by dividing the 2020 total net sales of $65,398 million by the average of total assets from 2020 ($50,710 million) and 2019 ($47,528 million) [v1, v2, v3]. The computed result based on these figures is exactly 1.33 [COMPUTED RESULT].

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

**Answer:** Lockheed Martin's FY2021 net working capital is 5,818 million USD. This figure is calculated by subtracting total current liabilities of 13,997 million from total current assets of 19,815 million as reported in the company's 2021 Consolidated Balance Sheets [v1, v2]. The resulting value of 5,818 million represents the company's short-term liquidity position for that fiscal year [v1, v2].

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

**Answer:** The year-end FY2018 accounts payable for MGM Resorts is 302.58 million USD. This figure is derived from the reported balance of $302,578 thousand found in the 2018 column of the Consolidated Balance Sheets [v1].

**Computation:** `accounts_payable_2018 = 302.58 million  where accounts_payable_2018 = 302,578 (thousands, FY2018)`

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

**Answer:** The 3-year average of capital expenditures as a percentage of revenue for MGM Resorts from FY2018 to FY2020 is 7.9%. This figure is calculated using the capital expenditures of $1,486,843 thousand, $739,006 thousand, and $270,579 thousand against revenues of $11,763,096 thousand, $12,899,672 thousand, and $5,162,082 thousand for the respective years [v1, v2, v3, v4, v5, v6].

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, MGM Resorts paid dividends to common shareholders in FY2022, totaling $4 million [v2]. The company made four quarterly payments of $0.0025 per share during the year [v2]. This is confirmed by the cash flow statement, which records dividends paid to common shareholders as $(4,048) thousand [v1].

**Computation:** `dividends_paid_common_2022 = -4,048 thousand  where dividends_paid_common_2022 = (4,048) (thousands, FY2022), dividend_description_2022 = In March 2022, June 2022, September 2022, and December 2022, we paid dividends of $0.0025 per share, totaling $4 million for 2022. (units, FY2022)`

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

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `MGMRESORTS_2022_10K` pages 40, 41, 43, 45, 59, 60, 61, 62, 64, 94, 99, 100; `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15; `MGMRESORTS_2023_8K_dated-2023-03-01` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

Las Vegas resorts contributed ~90% of company level EBITDAR during FY2022.
</details>

## 108. What was MGM's interest coverage ratio using FY2022 Adjusted EBIT as the numerator and annual Interest Expense as the denominator?

`financebench_id_01911` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MGMRESORTS_2022_10K: extractor: The filing provides 'Adjusted EBITDAR' (Earnings Before Interest, Taxes, Depreciation, Amortization, and Rent) but does not explicitly state 'Adjusted EBIT' (which would exclude Rent). While Adjusted EBIT could be calculated by subtracting Rent from Adjusted EBITDAR, the specific metric 'Adjusted EBIT' is not present in the text as a defined line item. The question asks for 'Adjusted EBIT' specifically. Without an explicit definition of 'Adjusted EBIT' in the document (e.g., whether it includes or excludes specific non-operating items beyond rent), the exact numerator cannot be confirmed solely from the provided text without making assumptions about the definition of 'Adjusted EBIT' versus 'Adjusted EBITDAR'. However, if we assume Adjusted EBIT = Adjusted EBITDAR - Rent, the formula would be (adjusted_ebitdar_2022 - triple_net_rent_2022) / interest_expense_2022. But strictly following the rule to use only values found, 'Adjusted EBIT' is not found. \| MGMRESORTS_2022Q4_EARNINGS: extractor: The filing provides 'Adjusted EBITDAR' (Earnings Before Interest, Taxes, Depreciation, Amortization, and Rent) but does not provide a metric labeled 'Adjusted EBIT' (which would exclude Rent). The definition of Adjusted EBITDAR on Page 7 explicitly includes the add-back of 'rent expense related to triple-net operating leases and ground leases'. Without a specific 'Adjusted EBIT' figure or the specific rent expense amount to subtract from Adjusted EBITDAR to derive Adjusted EBIT, the requested ratio cannot be calculated using ONLY the provided pages. \| MGMRESORTS_2023_8K_dated-2023-03-01: extractor: The provided document is a Form 8-K dated March 1, 2023, which reports the appointment of a new director. It explicitly states under Item 9.01 that financial statements are 'Not applicable'. The document does not contain the FY2022 Adjusted EBIT or annual Interest Expense required to calculate the interest coverage ratio.

**Pages searched:** `MGMRESORTS_2022_10K` pages 45, 59, 60, 61, 62, 64, 74, 83, 84, 94, 99, 100; `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 3, 4, 6, 7, 9, 11, 12, 13, 14, 15; `MGMRESORTS_2023_8K_dated-2023-03-01` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

As adjusted EBIT is negative, coverage ratio is zero
</details>

## 109. Which region had the worst topline performance for MGM during FY2022?

`financebench_id_01912` · filing `MGMRESORTS_2022Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MGMRESORTS_2022_10K: extractor: The provided pages contain consolidated revenue data by line item (Casino, Rooms, etc.) and total net revenues for FY2022, but they do not provide a breakdown of topline performance (revenue) by geographic region (e.g., Las Vegas Strip, Regional Operations, MGM China) for the fiscal year 2022. Page 7 describes the regions but does not list their specific 2022 revenues. Therefore, it is impossible to determine which region had the worst performance based solely on the provided text. \| MGMRESORTS_2022Q4_EARNINGS: code checks failed twice: formula: unknown value name 'las_vegas_strip_revenues_2021' (names: []) \| MGMRESORTS_2023_8K_dated-2023-03-01: extractor: The provided pages (Form 8-K dated March 1, 2023) contain information regarding the appointment of a new director and a press release. They do not contain financial statements, segment data, or topline performance metrics for FY2022 or any other period.

**Pages searched:** `MGMRESORTS_2022_10K` pages 7, 35, 37, 47, 48, 59, 60, 61, 62, 64, 65, 94; `MGMRESORTS_2022Q4_EARNINGS` pages 1, 2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15; `MGMRESORTS_2023_8K_dated-2023-03-01` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

MGM China experienced the worst topline performance amongst the other regions presented. Its revenue declined 44% in FY2022 whereas the other regions presented increased their revenues.
</details>

## 110. Which type of debt received the largest investment among the short term investments for MGM in H1 FY2023?

`financebench_id_00407` · filing `MGMRESORTS_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** MGMRESORTS_2023Q2_10Q: extractor: The question asks for the type of debt that received the largest *investment* (cash outflow) during H1 FY2023. The provided pages (specifically Page 11) list the *ending balances* of short-term investments by type (e.g., Corporate bonds, U.S. government securities) as of June 30, 2023, but do not provide the specific *cash flow* or *investment activity* for each type during the period. Page 6 shows a net line item 'Investments and other' of (216,485) but does not break down the investment amounts by security type. Therefore, it is impossible to determine which specific type of debt received the largest investment based solely on the provided pages.

**Pages searched:** `MGMRESORTS_2023Q2_10Q` pages 3, 4, 5, 6, 7, 8, 11, 18, 19, 36, 37, 38

<details><summary>Gold answer</summary>

the biggest short term investment is in corporate bonds (almost 82% of the total investment)
</details>

## 111. What is the FY2016 COGS for Microsoft? Please state answer in USD millions. Provide a response to the question by primarily using the statement of income.

`financebench_id_04700` · filing `MICROSOFT_2016_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2016 Cost of Goods Sold (COGS) for Microsoft is 32,780 million USD. This figure is reported as the "Total cost of revenue" for the year ended June 30, 2016, in the company's income statement [v1]. The value is derived from the sum of product and service costs listed in the financial statements [v1].

**Computation:** `cogs_fy2016 = 32,780 million  where cogs_fy2016 = 32,780 (millions, FY2016)`

- **v1** · `MICROSOFT_2016_10K` · PDF page **52** · column 2016 · millions
  - Quote: "Total cost of revenue \| 32,780 \| 33,038 \| 27,078"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, Microsoft did not increase its debt on the balance sheet between FY2022 and FY2023. The total debt decreased by 2,544 million, calculated from the sum of current and long-term debt in 2023 versus 2022 [v1, v2, v3, v4]. Specifically, the current portion of long-term debt rose from 2,749 million to 5,247 million, while long-term debt fell from 47,032 million to 41,990 million [v1, v2, v3, v4]. The net result of these changes was a reduction in total debt [COMPUTED RESULT].

**Computation:** `(current_portion_long_term_debt_2023 + long_term_debt_2023) - (current_portion_long_term_debt_2022 + long_term_debt_2022) = -2,544 million  where current_portion_long_term_debt_2023 = 5,247 (millions, FY2023), current_portion_long_term_debt_2022 = 2,749 (millions, FY2022), long_term_debt_2023 = 41,990 (millions, FY2023), long_term_debt_2022 = 47,032 (millions, FY2022)`

- **v1** · `MICROSOFT_2023_10K` · PDF page **60** · column 2023 · millions
  - Quote: "Current portion of long-term debt \| 5,247"

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

- **v2** · `MICROSOFT_2023_10K` · PDF page **60** · column 2022 · millions
  - Quote: "Current portion of long-term debt \| 2,749"

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

- **v3** · `MICROSOFT_2023_10K` · PDF page **60** · column 2023 · millions
  - Quote: "Long-term debt \| 41,990"

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

- **v4** · `MICROSOFT_2023_10K` · PDF page **60** · column 2022 · millions
  - Quote: "Long-term debt \| 47,032"

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2015 unadjusted EBITDA % margin for Netflix is 5.43%. This result is computed by adding the operating income of 305,826 thousand [v1] and depreciation and amortization of 62,283 thousand [v2], then dividing by the total revenues of $6,779,511 thousand [v3].

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

**Answer:** Netflix's year-end FY2017 total current liabilities were 5,466.312 million USD. This figure is derived from the Consolidated Balance Sheets, which report total current liabilities as 5,466,312 in thousands for the year 2017 [v1]. The computed result confirms this value converted to millions [v1].

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

**Computation:** `avg(cost_of_sales_2016 / revenue_2016, cost_of_sales_2017 / revenue_2017, cost_of_sales_2018 / revenue_2018) = 55.1%  where revenue_2016 = $32,376 (millions, FY2016), cost_of_sales_2016 = 17,405 (millions, FY2016), revenue_2017 = $34,350 (millions, FY2017), cost_of_sales_2017 = 19,038 (millions, FY2017), revenue_2018 = $36,397 (millions, FY2018), cost_of_sales_2018 = 20,441 (millions, FY2018)`

- **v1** · `NIKE_2018_10K` · PDF page **46** · column 2016 · millions
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

- **v2** · `NIKE_2018_10K` · PDF page **46** · column 2016 · millions
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

- **v3** · `NIKE_2018_10K` · PDF page **46** · column 2017 · millions
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

- **v4** · `NIKE_2018_10K` · PDF page **46** · column 2017 · millions
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

- **v5** · `NIKE_2018_10K` · PDF page **46** · column 2018 · millions
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

- **v6** · `NIKE_2018_10K` · PDF page **46** · column 2018 · millions
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

<details><summary>Gold answer</summary>

55.1%
</details>

## 116. According to the details clearly outlined within the balance sheet, how much total current assets did Nike have at the end of FY2019? Answer in USD millions.

`financebench_id_03531` · filing `NIKE_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Nike had total current assets of 16,525 million USD at the end of FY2019 [v1]. This figure is explicitly listed in the Consolidated Balance Sheets under the "Total current assets" row for the year 2019 [v1]. The value represents the sum of cash, short-term investments, accounts receivable, inventories, and prepaid expenses as reported in the document [v1].

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

**Answer:** The FY2021 inventory turnover ratio for Nike is 3.46. This result is calculated by dividing the 2021 Cost of Sales of $24,576 million [v1] by the average of the 2021 and 2020 inventories, which were $6,854 million and $7,367 million respectively [v2, v3]. The system computed this ratio as 3.46 based on these figures.

**Computation:** `cogs_2021 / avg(inventory_2021, inventory_2020) = 3.46  where cogs_2021 = 24,576 (millions, FY2021), inventory_2021 = 6,854 (millions, FY2021), inventory_2020 = 7,367 (millions, FY2020)`

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

**Answer:** Operations activities brought in the most cash flow for Nike in FY2023 with $5,841 million [v1]. This amount is higher than the $564 million from investing activities [v2] and the $(7,447) million used by financing activities [v3]. The computed maximum of these three values confirms that operations provided the highest cash inflow [COMPUTED RESULT].

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

**Answer:** Yes, PayPal has positive working capital based on FY2022 data. The company reported total current assets of $57,517 million and total current liabilities of $45,101 million, resulting in a computed working capital of $12,416 million [v1, v2]. This positive figure indicates that the company's short-term assets exceed its short-term obligations. Working capital is a relevant metric for PayPal as it reflects the company's ability to meet its immediate financial obligations using its liquid assets.

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

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `PEPSICO_2021_10K` pages 31, 47, 53, 54, 61, 62, 63, 64, 65, 66, 108, 119; `PEPSICO_2022_10K` pages 31, 47, 53, 62, 63, 64, 65, 66, 67, 99, 110, 121; `PEPSICO_2022Q4_EARNINGS` pages 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 24

<details><summary>Gold answer</summary>

$4.60
</details>

## 121. What are the geographies that Pepsico primarily operates in as of FY2022?

`financebench_id_01009` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `PEPSICO_2022_10K` pages 5, 6, 62, 63, 64, 65, 66, 67, 72, 110, 488, 489; `PEPSICO_2022Q4_EARNINGS` pages 1, 2, 3, 5, 6, 9, 10, 13, 17, 18, 22, 24; `PEPSICO_2023_8K_dated-2023-05-05` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

As of FY2022, Pepsico primarily operates in the following geographies: North America, Latin America, Europe, Africa, Middle East, South Asia, Asia Pacific, Australia, New Zealand and China.
</details>

## 122. Has Pepsico reported any materially important ongoing legal battles from FY2022 and FY2021?

`financebench_id_00735` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2022_10K: extractor: The provided pages include the Table of Contents referencing 'Item 3. Legal Proceedings' on page 24, but the actual content of Item 3 (pages 24-25) is not included in the provided pages. Therefore, no specific legal battles or their materiality can be confirmed from the given text. \| PEPSICO_2022Q4_EARNINGS: extractor: The provided pages contain a general risk factor mentioning 'potential liabilities and costs from litigation' (Page 24) and notes on impairment charges related to the SodaStream brand and Russia-Ukraine conflict (Page 9), but they do not contain specific details, descriptions, or financial quantification of any 'materially important ongoing legal battles' for FY2021 or FY2022. The document refers readers to the Form 10-K for additional information. \| PEPSICO_2021_10K: extractor: The provided pages cover the fiscal year ended December 25, 2021 (FY2021) and include a Table of Contents indicating 'Item 3. Legal Proceedings' is on page 24. However, the actual text of Item 3 (Legal Proceedings) is not included in the provided pages (which jump from Page 4 to Page 48). Furthermore, the filing is for FY2021, so it does not contain data for FY2022.

**Pages searched:** `PEPSICO_2022_10K` pages 2, 3, 4, 62, 63, 64, 65, 66, 67, 68, 99, 110; `PEPSICO_2022Q4_EARNINGS` pages 1, 5, 9, 13, 14, 15, 18, 19, 20, 21, 22, 24; `PEPSICO_2021_10K` pages 2, 3, 4, 48, 61, 62, 63, 64, 65, 66, 67, 108

<details><summary>Gold answer</summary>

No, Pepsico is not involved in material legal battles.
</details>

## 123. What is the quantity of restructuring costs directly outlined in Pepsico's income statements for FY2022? If restructuring costs are not explicitly outlined then state 0.

`financebench_id_01328` · filing `PEPSICO_2022_10K` · domain-relevant

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2022_10K: code checks failed twice: formula: unknown value name 'restructuring_and_impairment_charges_2022' (names: []) \| PEPSICO_2022Q4_EARNINGS: code checks failed twice: formula: unknown value name 'restructuring_and_impairment_charges_fy2022' (names: []) \| PEPSICO_2023_8K_dated-2023-05-05: extractor: The provided pages (1-5) of the Form 8-K dated May 5, 2023, contain only the cover page, securities registration information, and voting results from the 2023 Annual Meeting of Shareholders. They do not include PepsiCo's income statement or any financial data for FY2022, including restructuring costs.

**Pages searched:** `PEPSICO_2022_10K` pages 31, 46, 49, 62, 63, 64, 65, 66, 67, 68, 79, 110; `PEPSICO_2022Q4_EARNINGS` pages 3, 9, 10, 11, 13, 14, 18, 19, 20, 21, 22, 24; `PEPSICO_2023_8K_dated-2023-05-05` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

Pepsico's restructuring costs in FY2022 amounted to $411 million .
</details>

## 124. What is the FY2022 unadjusted EBITDA less capex for PepsiCo? Define unadjusted EBITDA as unadjusted operating income + depreciation and amortization [from cash flow statement]. Answer in USD millions. Respond to the question by assuming the perspective of an investment analyst who can only use the details shown within the statement of cash flows and the income statement.

`financebench_id_03620` · filing `PEPSICO_2022_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2022 unadjusted EBITDA less capex for PepsiCo is 9,068 million USD. This figure is derived by adding the operating profit of 11,512 million and depreciation and amortization of 2,763 million, then subtracting the absolute value of capital spending of 5,207 million [v1, v2, v3]. The calculation follows the provided definition of unadjusted EBITDA less capex using the specific values from the 2022 fiscal year [v1, v2, v3].

**Computation:** `operating_profit_2022 + depreciation_amortization_2022 - abs(capital_spending_2022) = 9,068 million  where operating_profit_2022 = 11,512 (millions, FY2022), depreciation_amortization_2022 = 2,763 (millions, FY2022), capital_spending_2022 = (5,207) (millions, FY2022)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2022 unadjusted EBITDA margin for PepsiCo is 16.52%. This is calculated by adding the operating profit of $11,512 million [v1] and depreciation and amortization of $2,763 million [v2], then dividing the sum by the net revenue of $86,392 million [v3]. The resulting ratio represents the unadjusted EBITDA as a percentage of net revenue for the fiscal year.

**Computation:** `(operating_profit_2022 + depreciation_amortization_2022) / net_revenue_2022 = 16.52%  where operating_profit_2022 = 11,512 (millions, FY2022), depreciation_amortization_2022 = 2,763 (millions, FY2022), net_revenue_2022 = $86,392 (millions, FY2022)`

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

**Answer:** PepsiCo increased its unsecured five-year revolving credit agreement by $400,000,000 on May 26, 2023. This increase resulted from terminating the previous $3,800,000,000 agreement and entering into a new $4,200,000,000 agreement [v1, v2]. The computed difference between the new and old amounts is exactly $400,000,000.

**Computation:** `new_agreement_amount - old_agreement_amount = 400,000,000  where old_agreement_amount = $3,800,000,000 (units, FY2023), new_agreement_amount = $4,200,000,000 (units, FY2023)`

- **v1** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column N/A · units
  - Quote: "Effective May 26, 2023, PepsiCo terminated the $3,800,000,000 five year unsecured revolving credit agreement"

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

- **v2** · `PEPSICO_2023_8K_dated-2023-05-30` · PDF page **2** · column N/A · units
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

$400,000,000 increase.
</details>

## 128. As of May 26, 2023, what is the total amount Pepsico may borrow under its unsecured revolving credit agreements?

`financebench_id_00882` · filing `PEPSICO_2023_8K_dated-2023-05-30` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** PEPSICO_2023Q2_EARNINGS: extractor: The provided pages do not contain information regarding the specific terms of PepsiCo's unsecured revolving credit agreements or the total borrowing capacity as of May 26, 2023. The document includes a Condensed Consolidated Balance Sheet (Page 9) showing debt obligations and a Condensed Consolidated Statement of Cash Flows (Page 8) showing debt activity, but does not detail the credit facility limits. \| PEPSICO_2023_8K_dated-2023-05-30: verifier: answer_supported=no. The computation incorrectly sums two separate descriptions of the same agreement. The text states that on May 26, 2023, PepsiCo entered into a 'new $4,200,000,000 364 day unsecured revolving credit agreement' and a 'new $4,200,000,000 five year unsecured revolving credit agreement'. However, the text clarifies that the 364-day agreement is a renewal of the 2022 364 Day Credit Agreement, and the five-year agreement is a renewal of the 2022 Five Year Credit Agreement. The question asks for the total amount PepsiCo may borrow under its unsecured revolving credit agreements as of that date. The text describes two distinct agreements (one 364-day and one five-year), each for $4.2 billion, totaling $8.4 billion. However, the evidence provided lists the same $4.2 billion figure twice for two different descriptions of the same transaction or two separate transactions. Looking closely at the text, there are two distinct agreements: the '2023 364 Day Credit Agreement' ($4.2B) and the '2023 Five Year Credit Agreement' ($4.2B). The sum of $8.4B is correct based on the text provided. \| PEPSICO_2023Q1_EARNINGS: extractor: The provided pages contain financial statements (Income Statement, Cash Flows, Balance Sheet) and earnings highlights for Q1 2023, but do not include the 'Debt and Liquidity' section or footnotes detailing the specific terms and total capacity of unsecured revolving credit agreements.

**Pages searched:** `PEPSICO_2023Q2_EARNINGS` pages 3, 4, 5, 6, 8, 9, 11, 12, 13, 15, 16, 19; `PEPSICO_2023_8K_dated-2023-05-30` pages 1, 2, 3, 4, 5, 9, 81, 85, 160, 163, 165, 172; `PEPSICO_2023Q1_EARNINGS` pages 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16

<details><summary>Gold answer</summary>

Total amount Pepsico may borrow under unsecured revolving credit agreements = $8,400,000,000.
</details>

## 129. As of FY2023Q1, why did Pepsico raise full year guidance for FY2023?

`financebench_id_01474` · filing `PEPSICO_2023Q1_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2023Q1_EARNINGS: code checks failed twice: strong_start_reason: raw 'Given our strong start to the year, we now expect our full-year 2023 organic revenue to increase 8 percent (previously 6 percent) and core constant currency EPS to increase 9 percent (previously 8%)' does not appear in its quote; investment_reason: raw 'Our results demonstrate that the investments we have made to become an even Faster, even Stronger, and even Better organization by Winning with pep+ are laying the foundation for durable and sustained' does not appear in its quote \| PEPSICO_2023Q2_EARNINGS: extractor: The provided document is the Q2 2023 earnings release (dated July 13, 2023). It states that guidance was raised based on Q2 performance. The question asks for the reason 'As of FY2023Q1'. The document does not contain information regarding the company's status or guidance decisions specifically as of the end of Q1 2023. The guidance raise occurred in Q2, not Q1. Therefore, the specific evidence for the state 'As of FY2023Q1' is not found in the text.

**Pages searched:** `PEPSICO_2023Q1_EARNINGS` pages 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 16; `PEPSICO_2023Q2_EARNINGS` pages 1, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 19

<details><summary>Gold answer</summary>

Pepsico experienced a strong start to FY2023.
</details>

## 130. As of FY2023Q1, by how many percentage points did Pepsico raise full year guidance in respect of core constant currency EPS growth?

`financebench_id_01476` · filing `PEPSICO_2023Q1_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PEPSICO_2023Q1_EARNINGS: code checks failed twice: new_guidance: the quote is not on page 3. Copy it exactly from one line of the page; previous_guidance: the quote is not on page 3. Copy it exactly from one line of the page; no value passed the checks; give exact quotes, or answer not_found \| PEPSICO_2023Q2_EARNINGS: code checks failed twice: formula: unknown value name 'new_guidance_value' (names: [])

**Pages searched:** `PEPSICO_2023Q1_EARNINGS` pages 1, 2, 3, 4, 8, 9, 10, 12, 13, 14, 15, 16; `PEPSICO_2023Q2_EARNINGS` pages 1, 2, 3, 4, 5, 9, 10, 11, 13, 16, 18, 19

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

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** PFIZER_2019_10K: verifier: answer_supported=no. The evidence for v2 (Gain on completion of Consumer Healthcare JV transaction) shows a value of (8,233) million, which is a negative number (a loss or a deduction), not a gain that increased net income. Therefore, the final answer is incorrect in stating it was a gain that increased net income. \| PFIZER_2020_10K: code checks failed twice: formula: unknown value name 'gain_consumer_healthcare_jv_2019' (names: [])

**Pages searched:** `PFIZER_2019_10K` pages 131, 150, 152, 154, 157, 158, 178, 183; `PFIZER_2020_10K` pages 61, 62, 63, 64, 65, 67, 85, 106, 108, 115

<details><summary>Gold answer</summary>

Yes, the gain on completion of Consumer Healthcare JV Transaction
</details>

## 133. What are three main companies acquired by Pfizer mentioned in this 10K report?

`financebench_id_02416` · filing `PFIZER_2021_10K` · novel-generated

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `PFIZER_2022_10K` pages 7, 52, 54, 55, 56, 57, 58, 59, 67, 106, 109; `PFIZER_2021_10K` pages 6, 57, 58, 59, 60, 61, 68, 71, 102, 109; `PFIZER_2020_10K` pages 49, 54, 61, 62, 63, 64, 65, 95, 113, 120

<details><summary>Gold answer</summary>

Trillium, Array, and Therachon
</details>

## 134. How much does Pfizer expect to pay to spin off Upjohn in the future in USD million?

`financebench_id_00283` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PFIZER_2022_10K: extractor: The document states that the Upjohn spin-off was completed in November 2020 (Page 60, 68). The $700 million figure mentioned on Page 33 refers to total expected separation costs, of which 85% has already been incurred through December 31, 2022. The document does not explicitly state a specific future payment amount remaining to be paid, only that the remaining costs (15% of $700 million) are expected to be incurred. Since the question asks for a specific future payment amount and the document only provides a total expected cost and a percentage incurred, the exact future payment amount is not explicitly stated as a single value, though it can be derived. However, the prompt asks for evidence and a formula. The evidence shows the total and the percentage incurred. The question asks 'How much does Pfizer expect to pay... in the future'. The document implies the remaining 15% is the future cost. I will provide the values to calculate the remaining amount. \| PFIZER_2021_10K: code checks failed twice: formula: unknown value name 'total_expected_costs' (names: ['costs_incurred_to_date_pct']) \| PFIZER_2020_10K: code checks failed twice: formula: unknown value name 'total_expected_costs' (names: ['costs_incurred_to_date'])

**Pages searched:** `PFIZER_2022_10K` pages 33, 54, 55, 56, 57, 58, 59, 60, 68, 73, 89; `PFIZER_2021_10K` pages 32, 57, 58, 59, 60, 61, 63, 71, 76, 110, 113; `PFIZER_2020_10K` pages 33, 61, 62, 63, 64, 65, 74, 75, 80, 105, 106

<details><summary>Gold answer</summary>

77.78
</details>

## 135. For Pfizer, which geographic region had the biggest drop in Q22023 year over year revenues (on a percentage basis)?

`financebench_id_00724` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The geographic region with the biggest drop in Q2 2023 year-over-year revenues was Developed Rest of World, which saw a 74% decline [v2]. This was followed by Developed Europe at 56% and Emerging Markets at 53% [v1, v3].

- **v1** · `PFIZER_2023Q2_EARNINGS` · PDF page **26** · column 2023 Total · units
  - Quote: "TOTAL INTERNATIONAL REVENUES \| $2,415  $5,480  (56%)  (55%)  $1,305  $5,034  (74%) \| (72%)  $2,828  $6,006  (53%)  (50%)"

  <details><summary>Passage</summary>

  ```
   | INTERNATIONAL REVENUES BY GEOGRAPHIC REGION
   | SECOND-QUARTER 2023 and 2022 - (UNAUDITED)
   | DEVELOPED EUROPE(h) | DEVELOPED REST OF WORLD(i) | EMERGING MARKETS(j)
   | % Change | % Change | % Change
   | 2023 | 2022 | 2023 | 2022 | 2023 | 2022
  (MILLIONS) | Total | Oper. | Total | Oper. | Total | Oper.
  TOTAL INTERNATIONAL REVENUES | $2,415  $5,480  (56%)  (55%)  $1,305  $5,034  (74%) | (72%)  $2,828  $6,006  (53%)  (50%)
   GLOBAL BIOPHARMACEUTICALS BUSINESS (BIOPHARMA)(b) | $2,274  $5,309  (57%)  (57%)  $1,281  $5,011  (74%) | (72%)  $2,768  $5,969  (54%)  (51%)
    Primary Care | $1,206  $4,184  (71%)  (70%)  $682  $4,368  (84%) | (83%)  $1,415  $4,638  (70%)  (69%)
   | Comirnaty direct sales and alliance revenues(c) | 546 | 2,465  (78%) | (77%) | 434 | 2,355 | (82%) | (80%) | 492 | 2,947  (83%) | (83%)
   | Paxlovid | 13 | 1,001  (99%) | (99%) | 27 | 1,729 | (98%) | (98%) | 102 | 930  (89%) | (89%)
   | Eliquis alliance revenues and direct sales | 323 | 377  (14%) | (14%) | 74 | 106 | (31%) | (25%) | 214 | 197 | 8% | 10%
   | Prevnar family(d) | 112 | 111 | 1% | 2% | 78 | 90 | (14%) | (7%) | 373 | 322 | 16% | 21%
  ```
  </details>

- **v2** · `PFIZER_2023Q2_EARNINGS` · PDF page **26** · column 2023 Total · units
  - Quote: "TOTAL INTERNATIONAL REVENUES \| $2,415  $5,480  (56%)  (55%)  $1,305  $5,034  (74%) \| (72%)  $2,828  $6,006  (53%)  (50%)"

  <details><summary>Passage</summary>

  ```
   | INTERNATIONAL REVENUES BY GEOGRAPHIC REGION
   | SECOND-QUARTER 2023 and 2022 - (UNAUDITED)
   | DEVELOPED EUROPE(h) | DEVELOPED REST OF WORLD(i) | EMERGING MARKETS(j)
   | % Change | % Change | % Change
   | 2023 | 2022 | 2023 | 2022 | 2023 | 2022
  (MILLIONS) | Total | Oper. | Total | Oper. | Total | Oper.
  TOTAL INTERNATIONAL REVENUES | $2,415  $5,480  (56%)  (55%)  $1,305  $5,034  (74%) | (72%)  $2,828  $6,006  (53%)  (50%)
   GLOBAL BIOPHARMACEUTICALS BUSINESS (BIOPHARMA)(b) | $2,274  $5,309  (57%)  (57%)  $1,281  $5,011  (74%) | (72%)  $2,768  $5,969  (54%)  (51%)
    Primary Care | $1,206  $4,184  (71%)  (70%)  $682  $4,368  (84%) | (83%)  $1,415  $4,638  (70%)  (69%)
   | Comirnaty direct sales and alliance revenues(c) | 546 | 2,465  (78%) | (77%) | 434 | 2,355 | (82%) | (80%) | 492 | 2,947  (83%) | (83%)
   | Paxlovid | 13 | 1,001  (99%) | (99%) | 27 | 1,729 | (98%) | (98%) | 102 | 930  (89%) | (89%)
   | Eliquis alliance revenues and direct sales | 323 | 377  (14%) | (14%) | 74 | 106 | (31%) | (25%) | 214 | 197 | 8% | 10%
   | Prevnar family(d) | 112 | 111 | 1% | 2% | 78 | 90 | (14%) | (7%) | 373 | 322 | 16% | 21%
  ```
  </details>

- **v3** · `PFIZER_2023Q2_EARNINGS` · PDF page **26** · column 2023 Total · units
  - Quote: "TOTAL INTERNATIONAL REVENUES \| $2,415  $5,480  (56%)  (55%)  $1,305  $5,034  (74%) \| (72%)  $2,828  $6,006  (53%)  (50%)"

  <details><summary>Passage</summary>

  ```
   | INTERNATIONAL REVENUES BY GEOGRAPHIC REGION
   | SECOND-QUARTER 2023 and 2022 - (UNAUDITED)
   | DEVELOPED EUROPE(h) | DEVELOPED REST OF WORLD(i) | EMERGING MARKETS(j)
   | % Change | % Change | % Change
   | 2023 | 2022 | 2023 | 2022 | 2023 | 2022
  (MILLIONS) | Total | Oper. | Total | Oper. | Total | Oper.
  TOTAL INTERNATIONAL REVENUES | $2,415  $5,480  (56%)  (55%)  $1,305  $5,034  (74%) | (72%)  $2,828  $6,006  (53%)  (50%)
   GLOBAL BIOPHARMACEUTICALS BUSINESS (BIOPHARMA)(b) | $2,274  $5,309  (57%)  (57%)  $1,281  $5,011  (74%) | (72%)  $2,768  $5,969  (54%)  (51%)
    Primary Care | $1,206  $4,184  (71%)  (70%)  $682  $4,368  (84%) | (83%)  $1,415  $4,638  (70%)  (69%)
   | Comirnaty direct sales and alliance revenues(c) | 546 | 2,465  (78%) | (77%) | 434 | 2,355 | (82%) | (80%) | 492 | 2,947  (83%) | (83%)
   | Paxlovid | 13 | 1,001  (99%) | (99%) | 27 | 1,729 | (98%) | (98%) | 102 | 930  (89%) | (89%)
   | Eliquis alliance revenues and direct sales | 323 | 377  (14%) | (14%) | 74 | 106 | (31%) | (25%) | 214 | 197 | 8% | 10%
   | Prevnar family(d) | 112 | 111 | 1% | 2% | 78 | 90 | (14%) | (7%) | 373 | 322 | 16% | 21%
  ```
  </details>

<details><summary>Gold answer</summary>

Developed Rest of the World
</details>

## 136. As of Q2'2023, is Pfizer spinning off any large business segments?

`financebench_id_02419` · filing `Pfizer_2023Q2_10Q` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** PFIZER_2023Q2_EARNINGS: extractor: The provided pages mention the establishment of a new segment (Business Innovation) and a proposed acquisition (Seagen), but contain no evidence of Pfizer spinning off any large business segments as of Q2 2023. \| Pfizer_2023Q2_10Q: extractor: The filing states that the Upjohn spin-off was completed in November 2020. The current period (Q2 2023) mentions an acquisition of Seagen and a divestiture of an early-stage gene therapy portfolio, but no large business segment spin-off is occurring in Q2 2023.

**Pages searched:** `PFIZER_2023Q2_EARNINGS` pages 1, 3, 4, 6, 8, 9, 10, 11, 13, 16, 20, 29; `Pfizer_2023Q2_10Q` pages 1, 8, 9, 10, 11, 13, 17, 34, 37, 38, 41, 45

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

**Reason:** ULTABEAUTY_2023_10K: extractor: The Consolidated Statements of Cash Flows (Page 57) show 'Acquisitions, net of cash acquired' as '—' (zero) for both FY2023 and FY2022. The document does not list any specific major acquisitions for these periods. \| ULTABEAUTY_2023_8K_dated-2023-06-07: extractor: The provided pages (Form 8-K dated June 7, 2023) contain information regarding the Annual Meeting of Stockholders, amendments to Bylaws and Certificate of Incorporation, and voting results. They do not contain financial statements, management discussion, or any section detailing acquisitions made by Ulta Beauty in FY2022 or FY2023. \| ULTABEAUTY_2023_8K_dated-2023-09-18: extractor: The provided 8-K filing (dated September 18, 2023) only reports on the appointment of Kecia L. Steelman as President and Chief Operating Officer. It does not contain financial statements, a discussion of acquisitions, or any data regarding major acquisitions for FY2023 or FY2022.

**Pages searched:** `ULTABEAUTY_2023_10K` pages 5, 9, 10, 42, 54, 55, 56, 57, 58, 59, 100, 101; `ULTABEAUTY_2023_8K_dated-2023-06-07` pages 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15; `ULTABEAUTY_2023_8K_dated-2023-09-18` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

Ulta Beauty did not make any acquisitions in FY2023 and FY2022.
</details>

## 139. What drove the reduction in SG&A expense as a percent of net sales in FY2023?

`financebench_id_00601` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `None`, verifier `None`

**Reason:** the question does not identify a company in the corpus: which company?

**Pages searched:** none

<details><summary>Gold answer</summary>

Lower marketing expenses and leverage of incentive compensation due to higher sales. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 140. What drove the increase in Ulta Beauty's merchandise inventories balance at end of FY2023?

`financebench_id_00603` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023_10K: extractor: The provided pages contain the balance sheet values for merchandise inventories for FY2023 and FY2022, and the cash flow statement shows the change in inventories as a cash outflow. However, the specific qualitative or quantitative drivers (e.g., specific product categories, strategic stockpiling, supply chain delays, or sales mix changes) that explain *why* the inventory balance increased are not explicitly stated in the provided text. The text mentions general strategies like 'dynamic inventory planning' and 'monitoring clearance and aged inventory' but does not attribute the specific FY2023 increase to a particular cause.

**Pages searched:** `ULTABEAUTY_2023_10K` pages 8, 9, 11, 34, 35, 42, 54, 55, 56, 57, 58, 79

<details><summary>Gold answer</summary>

Increase in Merchandise inventories balance was driven by the opening of 47 new stores. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 141. What percent of Ulta Beauty's total spend on stock repurchases for FY 2023 occurred in Q4 of FY2023?

`financebench_id_00605` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023_10K: extractor: The filing provides the total dollar amount of stock repurchases for FY2023 ($900,033 thousand) on the Cash Flow Statement (Page 57). However, the table on Page 32 detailing repurchases for the fourth quarter (13 weeks ended Jan 28, 2023) only provides the number of shares (722,457) and the average price paid ($454.20), but does not explicitly state the total dollar value spent in that quarter. While the dollar value could be estimated by multiplying shares by average price, the exact dollar amount spent in Q4 is not explicitly printed in the document, and the rules prohibit using external calculations or estimates not directly stated as a value in the text.

**Pages searched:** `ULTABEAUTY_2023_10K` pages 5, 8, 32, 33, 54, 55, 56, 57, 58, 59, 81, 101

<details><summary>Gold answer</summary>

36%. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 142. Did Ulta Beauty's wages expense as a percent of net sales increase or decrease in FY2023?

`financebench_id_00606` · filing `ULTABEAUTY_2023Q4_EARNINGS` · novel-generated

**Status:** NOT_FOUND · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `None`

**Reason:** ULTABEAUTY_2023_10K: extractor: The provided pages do not contain a specific line item for 'wages expense' or 'store payroll' in the Consolidated Statements of Income (Page 55) or the Cash Flow Statement (Page 57). While Page 38 mentions 'store payroll and benefits' as a factor in SG&A deleverage for fiscal 2022, it does not provide the specific dollar amount for wages expense for FY2023 or FY2022, nor does it break out wages as a separate line item in the financial tables. Therefore, the wages expense as a percent of net sales cannot be calculated from the given pages. \| ULTABEAUTY_2023_8K_dated-2023-06-07: extractor: The provided pages (1, 2, 5, 6, 7, 9, 11, 13, 15, 18, 22, 25) of the Form 8-K dated June 7, 2023, contain information regarding amendments to the Certificate of Incorporation and Bylaws, the results of the annual meeting of stockholders, and the exhibit index. They do not contain the financial statements, income statement, or any data regarding 'wages expense' or 'net sales' for FY2023 or any other period. \| ULTABEAUTY_2023_8K_dated-2023-09-18: extractor: The provided document is a Form 8-K dated September 18, 2023, which reports on the appointment of Kecia L. Steelman as President and Chief Operating Officer. It does not contain financial statements, income statement data, wages expense, or net sales figures for FY2023 or any other period required to calculate the wages expense as a percent of net sales.

**Pages searched:** `ULTABEAUTY_2023_10K` pages 10, 12, 17, 26, 34, 35, 38, 54, 55, 56, 57, 58; `ULTABEAUTY_2023_8K_dated-2023-06-07` pages 1, 2, 5, 6, 7, 9, 11, 13, 15, 18, 22, 25; `ULTABEAUTY_2023_8K_dated-2023-09-18` pages 1, 2, 3, 4, 5

<details><summary>Gold answer</summary>

Wages expense as a percent of net sales increased in FY2023. The answer here assumes FY2023 refers to the 12 months ended on January 28, 2023 (although the company refers to this period as its fiscal 2022.
</details>

## 143. Among all of the derivative instruments that Verizon used to manage the exposure to fluctuations of foreign currencies exchange rates or interest rates, which one had the highest notional value in FY 2021?

`financebench_id_00859` · filing `VERIZON_2021_10K` · novel-generated

**Status:** AMBIGUOUS · **Judge:** refusal · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Reason:** candidate filings give different answers

**Pages searched:** `VERIZON_2021_10K` pages 38, 47, 51, 52, 53, 54, 55, 63, 84, 85, 86, 87; `VERIZON_2022_10K` pages 40, 49, 50, 54, 55, 56, 57, 58, 66, 88, 90, 105

<details><summary>Gold answer</summary>

Cross currency swaps. Its notional value was $32,502 million.
</details>

## 144. As of FY 2021, how much did Verizon expect to pay for its retirees in 2024?

`financebench_id_02024` · filing `VERIZON_2021_10K` · novel-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Verizon expected to pay $1,959 million for its retirees in the year corresponding to the 2024 column, calculated by adding $1,097 million in pension benefits and $862 million in health care and life benefits [v1, v2]. This total represents the sum of the estimated future benefit payments for that specific year as listed in the document [v1, v2].

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

**Reason:** VERIZON_2022_10K: verifier: answer_supported=partly. The final answer states the liquidity profile is 'reasonably healthy' based on a quick ratio of 0.54, but a quick ratio below 1.0 is generally considered a sign of potential liquidity issues (inability to cover all current liabilities with liquid assets), making the qualitative judgment 'reasonably healthy' subjective and potentially inaccurate.

**Pages searched:** `VERIZON_2022_10K` pages 23, 26, 37, 42, 52, 54, 55, 56, 57, 58, 105, 106

<details><summary>Gold answer</summary>

No. The quick ratio was approximately 0.54 for Verizon. It indicated that Verizon does not have a healthy liquidity profile.
</details>

## 146. Is Verizon a capital intensive business based on FY 2022 data?

`financebench_id_00215` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** incorrect · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** Yes, Verizon is a capital intensive business based on FY 2022 data, as its capital expenditures represented 16.9% of its total operating revenues [v1, v2]. This high ratio indicates that the company must invest significantly in property, plant, and equipment to generate its revenue [v3]. The computed result of 16.9% confirms the substantial portion of revenue reinvested into capital assets [COMPUTED RESULT].

**Computation:** `abs(capex_2022) / revenue_2022 = 16.9%  where capex_2022 = (23,087) (millions, FY2022), revenue_2022 = 136,835 (millions, FY2022), pppe_gross_2022 = 307,689 (millions, FY2022)`

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
  - Quote: "Property, plant and equipment \| 307,689"

  <details><summary>Passage</summary>

  ```
   | Accounts receivable | 25,332 | 24,742
   | Less Allowance for credit losses | 826 | 896
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
  ```
  </details>

<details><summary>Gold answer</summary>

Yes. Verizon's capital intensity ratio was approximately 2.774729. This means that it took approximately $2.77 of assets to generate $1 of revenue and thus, Verizon can be considered capital intensive.
</details>

## 147. Has Verizon increased its debt on balance sheet between 2022 and the 2021 fiscal period?

`financebench_id_00566` · filing `VERIZON_2022_10K` · domain-relevant

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** No, Verizon did not increase its debt between the 2021 and 2022 fiscal periods. The total debt decreased by $229 million, dropping from $150,868 million in 2021 to $150,639 million in 2022 [v1, v2]. This reduction is confirmed by the computed difference of -229 million [COMPUTED RESULT].

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The FY2018 days payable outstanding (DPO) for Walmart is 42.69 days. This result is derived from the accounts payable values of 46,092 and 41,433, the cost of sales of 373,396, and the inventory values of 43,783 and 43,046 [v1, v2, v3, v4, v5]. The final figure of 42.69 is the exact computed result provided for the specified formula [COMPUTED RESULT].

**Computation:** `365 * avg(ap_2018, ap_2017) / (cogs_2018 + (inv_2018 - inv_2017)) = 42.69  where ap_2018 = 46,092 (millions, FY2018), ap_2017 = 41,433 (millions, FY2017), cogs_2018 = 373,396 (millions, FY2018), inv_2018 = 43,783 (millions, FY2018), inv_2017 = 43,046 (millions, FY2017)`

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

- **v3** · `WALMART_2018_10K` · PDF page **57** · column 2018 · millions
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

- **v4** · `WALMART_2018_10K` · PDF page **59** · column 2018 · millions
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

- **v5** · `WALMART_2018_10K` · PDF page **59** · column 2017 · millions
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

<details><summary>Gold answer</summary>

42.69
</details>

## 149. Based on the information provided primarily in the statement of income, what is the FY2018 - FY2019 change in unadjusted operating income % margin for Walmart? Answer in units of percents and round to one decimal place.

`financebench_id_04784` · filing `WALMART_2019_10K` · metrics-generated

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The change in Walmart's unadjusted operating income margin from FY2018 to FY2019 is 0.2%. This result is derived from the operating income and net sales figures for both fiscal years, which show a calculated difference of 0.2% between the two periods [v1, v2, v3, v4].

**Computation:** `(operating_income_2019 / net_sales_2019) - (operating_income_2018 / net_sales_2018) = 0.2%  where operating_income_2019 = 21,957 (millions, FY2019), net_sales_2019 = 510,329 (millions, FY2019), operating_income_2018 = 20,437 (millions, FY2018), net_sales_2018 = 495,761 (millions, FY2018)`

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

**Status:** ANSWER · **Judge:** correct · **Models:** answer `Qwen/Qwen3.5-27B-FP8`, verifier `google/gemma-4-12B-it`

**Answer:** The 3-year average unadjusted EBITDA margin for Walmart is 6.2%. This result is derived from the average of the ratios of operating income plus depreciation and amortization to net sales for the fiscal years represented by the provided data points [v1, v2, v3, v4, v5, v6, v7, v8, v9]. The system computed this specific average as 6.2% based on those values [COMPUTED RESULT].

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
