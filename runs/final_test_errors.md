# Error report: final on test

54 answerable and 16 unanswerable queries. Labels use the top 8 passages.

| Label | Count |
|---|---|
| wrong_section | 10 |
| partial_span | 5 |
| false_abstain | 3 |
| false_answer | 8 |
| hit | 36 |
| correct_abstain | 8 |

## wrong_section (10)

**Query:** Consider the Strategic Alliance Agreement between Information System Associates, Inc. and Rubicon Software Group plc; Are there any services to be provided after the termination of this contract?

First relevant passage at rank: 15; recall@8: 0.00

Gold:
- `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [12612:12792]: Each Party shall retain the financial records relating to all payments owed and/or paid under this Agreement for a period of six years from the date such payment obligation arose.

Returned:
1. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [8000:8500] score 8.85: Subject to the terms and conditions of this Agreement, Rubicon shall provide the Contract Services, as agreed between ISA to Rubicon in the relevant SOW, to ISA's reasonable satisfaction. The Contract Services shall be performed at the facilities and location reasonably designated by ISA (with appro...
2. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [7750:8250] score 8.81: gs or Documentation or additional distribution arrangements with third parties in the United States from the date hereof without the prior written approval of ISA, which approval shall not be unreasonably withheld. 3. RUBICON SERVICES. 3.1 Subject to the terms and conditions of this Agreement, Rubic...
3. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [11500:12000] score 8.22: profits (defined as gross revenues less costs directly incurred in the generation of such revenues) on projects for which Rubicon has provided Contract Services after ISA has recouped any directly attributable start-up costs with respect to such project up to a cumulative maximum of £100,000 of such...

**Query:** Consider the Strategic Alliance Agreement between Information System Associates, Inc. and Rubicon Software Group plc; Is there a covenant not to sue included in this contract?

First relevant passage at rank: not in top 64; recall@8: 0.00

Gold:
- `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [13844:13911]: Rubicon shall not contest ownership by ISA of any of the foregoing.
- `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [18173:18240]: ISA shall not contest ownership by Rubicon of any of the foregoing.
- `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [20121:20393]: Either Party may terminate this Agreement upon ten Business Day's Notice to the other Party in the event the other Party contests or challenges to a material degree any of the other Party's Intellectual Property rights referred to in Sections 5.1, and 5.3, respectively.

Returned:
1. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [7750:8250] score 4.88: gs or Documentation or additional distribution arrangements with third parties in the United States from the date hereof without the prior written approval of ISA, which approval shall not be unreasonably withheld. 3. RUBICON SERVICES. 3.1 Subject to the terms and conditions of this Agreement, Rubic...
2. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [13000:13500] score 4.23: etween ISA and Rubicon, all right, title and interest in and to Intellectual Property which is created by or provided by ISA, including, without limitation, as they may be part of or incorporated into any Contract Service or otherwise used by Rubicon, all goodwill associated therewith and the copyri...
3. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [12750:13250] score 4.02: om the date such payment obligation arose. 4.6 Purchase of Rubicon Shares. This Agreement is conditional upon ISA and Rubicon entering into the Share Subscription Agreement. 5. INTELLECTUAL PROPERTY. 5.1 ISA's Intellectual Property. As between ISA and Rubicon, all right, title and interest in and to...

**Query:** Consider the Marketing and Transportation Services Agreement between Purolator Courier Ltd. and Parcelway Courier Systems Canada Ltd. (Dynamex Inc.); Does this contract include an exclusivity agreement?

First relevant passage at rank: not in top 64; recall@8: 0.00

Gold:
- `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [7970:8101]: Dynamex agrees not to provide sameday delivery services for any other provider of next day or multiple day courier services.

Returned:
1. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [16250:16750] score 4.05: s hereto. 6.3 A party shall, for any loss, damage or delay to Freight while in its care, custody or control, forthwith pay to the other Party the actual damages suffered by such other Party. Such liability shall not exceed the other Party's contractual liability to its customers. The Parties acknowl...
2. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [16500:17000] score 3.89: other Party's contractual liability to its customers. The Parties acknowledge that their contract of carriage with their customers provides that liability for loss, damage or delay, including liability for consequential loss, is limited to Four Dollars and Forty One Cents ($4.41) per kilogram or Two...
3. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [43000:43500] score 3.55: rofessional and financial advisers who agree to be bound by this provision) unless required by law to do so or unless prior written consent is obtained from the other Party. 35.0 TRADE-MARKS 35.1 Each Party's trade-marks, distinctive colours and designs used in connection with the Services shall rem...

**Query:** Consider the Marketing and Transportation Services Agreement between Purolator Courier Ltd. and Parcelway Courier Systems Canada Ltd. (Dynamex Inc.); Can this contract be terminated for convenience, and under what conditions?

First relevant passage at rank: 10; recall@8: 0.00

Gold:
- `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [33227:33332]: Either Party may terminate this Agreement, without cause, by giving two (2) years written notice.

Returned:
1. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [39750:40250] score 8.99: rms or conditions of this Agreement shall not constitute a general waiver or relinquishment of any such terms or conditions but the same shall be and remain at all times in full force and effect. 26.0 HEADINGS AND CAPTIONS 26.1 Headings and captions are inserted for each section of this Agreement fo...
2. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [27500:28000] score 5.27: subcontract the Services to another operator or operators, acceptable to the other Party. Such Services shall be provided by such subcontractor/subcontractors on the same terms and conditions herein set out and will be continued to be provided during the period of any such strike or labour disruptio...
3. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [40000:40500] score 5.15: Headings and captions are inserted for each section of this Agreement for convenience only and in no way define, limit or describe the scope of intent of this Agreement, nor shall they have any effect in regard to its interpretation. 27.0 AMENDMENTS 27.1 Unless otherwise provided herein, this Agreem...

## partial_span (5)

**Query:** Consider the Promotion Agreement between Depomed, Inc. and King Pharmaceuticals, Inc. for Glumetza; Does this contract include any right of first refusal, right of first offer, or right of first negotiation?

First relevant passage at rank: 1; recall@8: 0.42

Gold:
- `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [144427:146183]: Depomed agrees to grant and hereby grants to King an exclusive option (exercisable at King's sole discretion by providing written notice of intent at any time, but in no event later than 180 days after the Effective Date) to obtain an exclusive license in the Territory to certain of Depomed's propri...
- `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [147380:147892]: Depomed shall notify King in writing in the event that Depomed desires to divest itself of its rights to the Product in the Territory (e.g., by asset sale or product license to a Third Party), or of its rights in the Territory to a product owned or controlled by Depomed containing metformin and anot...
- `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [148461:149594]: If King is interested in obtaining the Metformin Product Rights, it shall so notify Depomed in writing prior to the expiration of the Evaluation Period, and upon Depomed's receipt of such notice King and Depomed shall promptly commence good-faith negotiations, for a period of 30 days and such longer...

Returned:
1. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [147250:147750] score 20.03: to as the AcuForm technology and described in U.S. Patent Nos. 6,340,475 and 6,635,280. Section 13.2 Right of First Negotiation. Depomed shall notify King in writing in the event that Depomed desires to divest itself of its rights to the Product in the Territory (e.g., by asset sale or product licen...
2. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [147000:147500] score 18.90: the Territory (either directly or indirectly through a marketing partner) a product that (A) contains metformin as an active pharmaceutical ingredient and (B) uses Depomed's or its Affiliate's proprietary drug delivery technology currently referred to as the AcuForm technology and described in U.S. ...
3. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [144000:144500] score 17.18: closure by both parties, either party may make subsequent public disclosure of the contents of such statement without the further approval of the other party. The provisions of this Article 12 shall survive termination of the agreement and shall remain in effect until a date three years after the Te...

**Query:** Consider the Endorsement Agreement between ABG-Shaq, LLC and Papa John's International, Inc.; Is there a non-disparagement clause in this contract?

First relevant passage at rank: 6; recall@8: 0.33

Gold:
- `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [13350:13670]: PAPA JOHN'S shall not, during the Term or at any time thereafter: (I) defame or disparage CELEBRITY or the Personality Rights (or any portion thereof), nor shall PAPA JOHN'S place the CELEBRITY or the Personality Rights (or any portion thereof) in a negative light, whether in connection with this Ag...
- `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [61086:61257]: All Parties agree not to disparage or make derogatory comments, verbal or written, regarding the other Party during the Term of the Agreement, and for one year thereafter.

Returned:
1. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [60000:60500] score 9.18: esignated by the other Party, and to conduct such other discovery as the arbitrator deems appropriate. The award or decision rendered by the arbitrator shall be final, binding and conclusive and judgment may be entered upon such award by any court. 10. Confidentiality and Non-Disparagement. Each Par...
2. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [60250:60750] score 8.72: 10. Confidentiality and Non-Disparagement. Each Party shall hold all confidential information received pursuant to this Agreement, including the terms and conditions of this Agreement and CELEBRITY'S personal and/or business affairs, confidential and may only disclose them (i) with the prior written...
3. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [44750:45250] score 7.95: t (1) CELEBRITY's conviction or plea of guilty to a crime of moral turpitude; (2) CELEBRITY's or ABG's public malignment or disparagement of PAPA JOHN'S; (3) CELEBRITY or ABG intentionally makes any voluntary statement or commits any voluntary act that is or becomes generally known to the public whi...

**Query:** Consider the Endorsement Agreement between ABG-Shaq, LLC and Papa John's International, Inc.; Are there any services to be provided after the termination of this contract?

First relevant passage at rank: 3; recall@8: 0.15

Gold:
- `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [47413:48223]: Upon expiration or termination of this Agreement by PAPA JOHN'S (but not in the event of termination by ABG), and subject to PAPA JOHN'S ongoing compliance with the terms and conditions of this Agreement, PAPA JOHN'S shall have the following rights to use the Celebrity Endorsement solely as follows:...
- `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [51519:52259]: If this Agreement is terminated by ABG for any of the reasons provided in Section 7.B. above, then CELEBRITY shall be entitled to immediately vest in all of the RSUs for the eighteen (18) months following the effective date of termination (including, without limitation, any balance of unvested RSUs ...

Returned:
1. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [49250:49750] score 9.62: the Cash Payment for such Contract Year by a fraction, the numerator of which is the number of days elapsed in such Contract Year and the denominator of which is the total number of days in such Contract Year, and such amounts shall be immediately due as of the effective date of termination and paid...
2. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [24750:25250] score 9.36: cular Contract Year), then: (A) the same shall not result in a reduction in any amounts due and/or payable to ABG hereunder, and (B) PAPA JOHN'S shall be deemed to have waived its right to utilize those particular Services (e.g., Service Days that are allocated for a particular Contract Year may not...
3. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [51250:51750] score 8.92: fraction, the numerator of which is the number of days elapsed in such Contract Year and the denominator of which is the total number of days in such Contract Year, and such RSUs shall vest immediately as of the effective date of termination. b. Termination by ABG. If this Agreement is terminated by...

**Query:** Consider the Walabot HOME Reseller Agreement between Vayyar Imaging Ltd. and Inde Living Holdings, Inc.; Are there any services to be provided after the termination of this contract?

First relevant passage at rank: 1; recall@8: 0.50

Gold:
- `HealthcareIntegratedTechnologiesInc_20190812_8-K_EX-10.1_117` [15044:15960]: In addition to the foregoing, if, at the time of termination of this Agreement, Reseller shall have additional Product units in its inventory and is able to sell them to Customers and/or End Users (including, without limitation, any Product units for which Reseller has or is obligated to pay the Sup...

Returned:
1. `HealthcareIntegratedTechnologiesInc_20190812_8-K_EX-10.1_117` [14750:15250] score 5.85: is Agreement. Upon termination of this Agreement, the provisions in Sections 1, 6.5, 7, 8, 9, 10, 11, 12.3, 12.4, 13 (but solely to the extent stated in the last sentence of that section), and 14 shall remain in effect as necessary to carry out the purpose of those Sections after termination. In add...
2. `HealthcareIntegratedTechnologiesInc_20190812_8-K_EX-10.1_117` [15000:15500] score 5.67: urpose of those Sections after termination. In addition to the foregoing, if, at the time of termination of this Agreement, Reseller shall have additional Product units in its inventory and is able to sell them to Customers and/or End Users (including, without limitation, any Product units for which...
3. `HealthcareIntegratedTechnologiesInc_20190812_8-K_EX-10.1_117` [13750:14250] score 4.64: gating from any other remedies that any Party may have under the terms of this Agreement or at law, each Party shall have the right to terminate this Agreement forthwith upon the occurrence of any of the following: (i) the other Party is in material breach of its obligations hereunder and fails to r...

## false_abstain (3)

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; What is the expiration date of this contract?

First relevant passage at rank: 16; recall@8: 0.00

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [693:859]: Your employment shall commence on 26 September 2019 and shall continue unless and until either party gives notice to the other in accordance with paragraph 11 below.

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [28500:29000] score 3.25: withstanding the foregoing, no additional vesting of the Time-Based Equity Awards shall occur during the period between your Termination Date and the Accelerated Vesting Date. 11.9 Definitions. For purposes of this paragraph 11, the following terms shall have the following meanings: 9 "Accelerated V...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [37000:37500] score 3.18: hs from the Termination Date; "Restricted Territory" means anywhere in the United States or the United Kingdom or in any other country in which the Company or any Group Company conducts business or as of the date of termination of my employment relationship had plans to conduct business; and "Termin...
3. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [28000:28500] score 3.08: nation Date or (B) the Accelerated Vesting Date; provided that any termination or forfeiture of the unvested portion of such Time-Based Equity Awards that would otherwise occur on the Termination Date in the absence of this Agreement will be delayed until the Effective Date of the Settlement Agreeme...

**Query:** Consider the Business Affiliate Agreement between Dr. George D. Green and UNION DENTAL CORP.; What are the audit rights under this contract?

First relevant passage at rank: 20; recall@8: 0.00

Gold:
- `UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Aff` [3636:4076]: Make available, during normal business hours, at a Party=s offices all records, books, agreements, policies and procedures relating to the use and/or disclosure of Confidential Information that is subject to this Agreement, to the other Party within ten (10) days of a Party's written request, for th...

Returned:
1. `UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Aff` [8250:8750] score 1.78: ered by Business Affiliate. The provisions of this Paragraph 6 shall survive the termination of this Agreement for whatever reasons whatsoever. 7. Miscellaneous. a. Survival. The respective rights and obligations of Business Affiliate and UDC under the provisions of Sections 3(g) [Responsibilities o...
2. `UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Aff` [8000:8500] score 1.69: al, trial, appellate, judgment, post-judgment, execution, and alternative dispute resolution, which arise out of any use or disclosure of Confidential Information not specifically permitted by this Agreement or arise out of the services rendered by Business Affiliate. The provisions of this Paragrap...
3. `UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Aff` [12250:12750] score 1.69: tatus, the Parties hereby agree that both Business Affiliate and UDC shall have the right to participate in any discussions or negotiations Source: UNION DENTAL HOLDINGS, INC., 8-K/A, 2/4/2005 4 occurring with such agency or agencies, regardless of with whom or by whom such discussions or negotiatio...

**Query:** Consider the Joint Venture Agreement between Tate & Lyle Fermentation Products Ltd. and Igene Biotechnology, Inc. for Astaxanthin Production; What are the audit rights under this contract?

First relevant passage at rank: 22; recall@8: 0.00

Gold:
- `IGENEBIOTECHNOLOGYINC_05_13_2003-EX-1-JOINT VENTURE AGREEMEN` [62830:62977]: From time to time, each Party shall have the right to have its own internal or external auditors review the books and records of the Joint Venture.

Returned:
1. `IGENEBIOTECHNOLOGYINC_05_13_2003-EX-1-JOINT VENTURE AGREEMEN` [33250:33750] score 2.82: ssets by the Operating Company; (e) the sale, disposition or purchase of individual assets for in excess of $50,000; (f) approve the closing of any plant or facility of the Joint Venture; (g) approve any related-party contracts, except as contemplated in this Agreement; (h) approve any incurrence of...
2. `IGENEBIOTECHNOLOGYINC_05_13_2003-EX-1-JOINT VENTURE AGREEMEN` [33500:34000] score 2.82: ated in this Agreement; (h) approve any incurrence of indebtedness for borrowed money; (i) change the business purpose of the Joint Venture; (j) approve the discontinuance of any operations of the Joint Venture; (k) determine the annual business plan and budget (including capital expenditures) and a...
3. `IGENEBIOTECHNOLOGYINC_05_13_2003-EX-1-JOINT VENTURE AGREEMEN` [33750:34250] score 2.82: plan and budget (including capital expenditures) and any material variance from such plan and budget; (l) approve any contract or commitment for a period greater than twelve months; (m) approve any capacity increase at any manufacturing site; (n) determine budgets for continuing research concerning ...

## false_answer (8)

**Query:** Consider the Agency Agreement between General Electric Capital Corporation and Duckwall-Alco Stores, Inc. for Equipment Leasing; Is there a cap on liability under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [11250:11355] score 4.31: and conditions of the lease contract are set forth in the Master Lease Agreement and Equipment Schedule.
2. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [11000:11355] score 3.13: appropriate Purchase Order/Sales Agreement Number. General Electric Capital Corporation will also require a complete set of Lease documentation prior to funding. These documents may include a Schedule and a Certificate of Acceptance. The full terms and conditions of the lease contract are set forth ...
3. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [0:500] score 0.00: Exhibit 10.26 AGENCY AGREEMENT THIS AGENCY AGREEMENT, dated November 9, 2005 ("Agreement"), between General Electric Capital Corporation, a Delaware corporation (together with its successors and assigns, if any, "Lessor"), and Duckwall-Alco Stores, Inc., a Kansas corporation (the "Company"). Capital...

**Query:** Consider the Endorsement Agreement between ABG-Shaq, LLC and Papa John's International, Inc.; What are the audit rights under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [24750:25250] score 5.87: cular Contract Year), then: (A) the same shall not result in a reduction in any amounts due and/or payable to ABG hereunder, and (B) PAPA JOHN'S shall be deemed to have waived its right to utilize those particular Services (e.g., Service Days that are allocated for a particular Contract Year may not...
2. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [29250:29750] score 5.86: the Term, the following: A. Cash Payment. 1. PAPA JOHN'S shall pay ABG a cash payment of: One Million Two Hundred Fifty Thousand U.S. Dollars (USD$1,250,000) for Contract Year 1, One Million Three Hundred Seventy Five Thousand U.S. Dollars (USD$1,375,000) for Contract Year 2, and One Million Five Hu...
3. `PapaJohnsInternationalInc_20190617_8-K_EX-10.1_11707365_EX-1` [29500:30000] score 5.80: 375,000) for Contract Year 2, and One Million Five Hundred Thousand U.S. Dollars (USD$1,500,000) for Contract Year 3 (such cash payments for Contract Years 1-3 referred to herein as the "Cash Payment") for the services and rights provided hereunder. In addition to the Cash Payment and any other comp...

**Query:** Consider the Sponsorship Agreement between Excite, Inc. and Vitamin Shoppe Industries Inc. for Promotion on WebCrawler Channels; What are the insurance requirements under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `VITAMINSHOPPECOMINC_09_13_1999-EX-10.26-SPONSORSHIP AGREEMEN` [54000:54500] score 4.27: FOR ANY SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES, WHETHER BASED ON BREACH OF CONTRACT, TORT (INCLUDING NEGLIGENCE) OR OTHERWISE, WHETHER OR NOT THAT PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. EXCEPT UNDER SECTIONS 13(a) AND 13(b), THE LIABILITY OF EITHER PARTY FOR DAMAGES OR ALLEG...
2. `VITAMINSHOPPECOMINC_09_13_1999-EX-10.26-SPONSORSHIP AGREEMEN` [78500:79000] score 4.04: oducts Description Item # [*****] Estimated [*****] Estimated TOTALS in IMPS IMPS Contract Excite Integrated Links Excite Japan Sponsorsh
3. `VITAMINSHOPPECOMINC_09_13_1999-EX-10.26-SPONSORSHIP AGREEMEN` [78750:79250] score 3.94: Contract Excite Integrated Links Excite Japan Sponsorship/Promotion Positions #3b [*****] [*****] [*****] Excite Nutrition & Vitamins Sponsorship/Promotion Positions #3c [*****] [*****] [*****]

**Query:** Consider the Strategic Alliance Agreement between Information System Associates, Inc. and Rubicon Software Group plc; What are the insurance requirements under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [7750:8250] score 3.97: gs or Documentation or additional distribution arrangements with third parties in the United States from the date hereof without the prior written approval of ISA, which approval shall not be unreasonably withheld. 3. RUBICON SERVICES. 3.1 Subject to the terms and conditions of this Agreement, Rubic...
2. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [8000:8500] score 3.97: Subject to the terms and conditions of this Agreement, Rubicon shall provide the Contract Services, as agreed between ISA to Rubicon in the relevant SOW, to ISA's reasonable satisfaction. The Contract Services shall be performed at the facilities and location reasonably designated by ISA (with appro...
3. `DUOSTECHNOLOGIESGROUP,INC_04_21_2009-EX-10.1-STRATEGIC ALLIA` [9000:9500] score 3.95: he Contract Services as revised. All such Contract Services shall be executed under the terms and conditions of this Agreement and the applicable SOW (as revised by the change order). If any change order causes an increase or decrease in the cost of the Services to be performed or scheduled completi...
