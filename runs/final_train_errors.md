# Error report: final on train

140 answerable and 29 unanswerable queries. Labels use the top 8 passages.

| Label | Count |
|---|---|
| wrong_section | 44 |
| partial_span | 9 |
| false_abstain | 11 |
| false_answer | 12 |
| hit | 76 |
| correct_abstain | 17 |

## wrong_section (44)

**Query:** Consider the Service Agreement between Theravance Biopharma UK Limited and Brett Haumann; What is the expiration date of this contract?

First relevant passage at rank: 23; recall@8: 0.00

Gold:
- `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [4382:4705]: The Executive's employment with the Company will commence on the Commencement Date and shall continue, subject to the remaining terms of this Agreement, until terminated by either party giving the other the following minimum advance written notice: 2.1.1 6 weeks' notice; 2.1.2 such other longer peri...

Returned:
1. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [31250:31750] score 4.49: one month of the Commencement Date then the Executive will be deemed to have agreed to its terms. 24.8 The Executive shall not be contractually entitled to receive any benefit from the Company which is not expressly provided for by this Agreement. 24.9 This Agreement may be executed in any number of...
2. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [10000:10500] score 2.87: is paid. Bonus entitlement does not accrue in the course of a year, and the Executive is not entitled to 5 payment of a bonus, or any pro rata portion of it, if the Executive leaves employment prior to the date that the bonus is paid. 9.3 The Executive shall not be eligible to be considered for any ...
3. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [31500:32000] score 2.77: .9 This Agreement may be executed in any number of counterparts, each of which, when executed and delivered, shall be an original, and all the counterparts together shall constitute one and the same agreement. 24.10 The Contracts (Rights of Third Parties) Act 1999 shall only apply to this Agreement ...

**Query:** Consider the Service Agreement between Theravance Biopharma UK Limited and Brett Haumann; Can this contract be terminated for convenience, and under what conditions?

First relevant passage at rank: 17; recall@8: 0.00

Gold:
- `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [18678:18997]: The Company may, in its sole and absolute discretion, terminate the Executive's employment under this Agreement at any time and with immediate effect by notifying the Executive that the Company is exercising its right under this clause 17 and that it will make a payment in l ieu of not ice ("PILON")...

Returned:
1. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [22000:22500] score 8.60: g any disciplinary matter involving the Executive or while any disciplinary procedure or regulatory investigation is outstanding. Any such suspension shall not constitute disciplinary action. During any period of suspension, the Company may impose the same conditions that apply to Garden Leave. 19. ...
2. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [22250:22750] score 8.34: e same conditions that apply to Garden Leave. 19. Garden Leave 19.1 Following service of notice to terminate the employment by either party, or if the Executive purports to terminate the employment in breach of contract, the Company may by written notice place the Executive on Garden Leave for the w...
3. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [3500:4000] score 7.93: aused, whether lawful or not, and "Termination Date" means the date of Termination. 1.2 In this Agreement, unless the context otherwise requires: 1.2.1 words in the singular include the plural and in the plural include the singular; 1.2.2 any phrase introduced by the terms "including", "include", "i...

**Query:** Consider the Service Agreement between Theravance Biopharma UK Limited and Brett Haumann; Is there a covenant not to sue included in this contract?

First relevant passage at rank: not in top 64; recall@8: 0.00

Gold:
- `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [27816:28397]: If the Executive's employment is terminated at any time by reason of any reconstruction or amalgamation of any Group Company, whether by winding up or otherwise, and the Executive is offered employment with any concern or undertaking involved in or resulting from the reconstruction or amalgamation o...

Returned:
1. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [2500:3000] score 8.21: ight and related rights, trademarks, trade names and domain names, rights in get-up, rights in goodwill or to sue for passing off, unfair competition rights, rights in designs, rights in computer software, database rights, topography rights, rights in confidential information (including know-how and...
2. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [2250:2750] score 6.09: ompany" means the Company and any group undertaking (as such term is defined in section 1161(5) of the Companies Act 2006) of the Company in any jurisdiction from time to time; "Intellectual Property Rights" means patents, rights to Inventions, copyright and related rights, trademarks, trade names a...
3. `THERAVANCEBIOPHARMA,INC_05_08_2020-EX-10.2-SERVICE AGREEMENT` [31250:31750] score 4.05: one month of the Commencement Date then the Executive will be deemed to have agreed to its terms. 24.8 The Executive shall not be contractually entitled to receive any benefit from the Company which is not expressly provided for by this Agreement. 24.9 This Agreement may be executed in any number of...

**Query:** Consider the Sponsorship Agreement between R. C. Boyd Enterprises, LLC and Cano Petroleum, Inc. for 'Honey Hole'; What is the expiration date of this contract?

First relevant passage at rank: 18; recall@8: 0.00

Gold:
- `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [3546:3655]: The term of this Agreement shall be one (1) year, commencing January 1, 2008 and ending on December 31, 2008.

Returned:
1. `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [7250:7750] score 4.73: agreements, either oral or in writing, between the parties with respect to the subject matter of this contract, and contains all of the covenants and agreements between the parties with respect to the subject matter. Each party to this contract acknowledges that no representations, inducements, prom...
2. `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [7500:8000] score 4.07: knowledges that no representations, inducements, promises, or agreements, orally or otherwise, have been made by any party, or anyone acting on behalf of any party, that are 2 not set forth in this contract, and that no agreement, statement, or promise not contained in this contract shall be valid o...
3. `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [7000:7500] score 3.95: l be paid to the Company at Southlake, Tarrant County, Texas. 18. Assignment. This Agreement may not be assigned by either party without the prior written consent of the other party. 19. Other Agreements. This Agreement supersedes any and all other agreements, either oral or in writing, between the ...

## partial_span (9)

**Query:** Consider the Cooperation Agreement between HPIL ENERGYTECH Inc. and GINARES GROUP AG for Renewable Energy Projects; Is there a cap on liability under this contract?

First relevant passage at rank: 7; recall@8: 0.50

Gold:
- `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [11380:11583]: GINARES agrees that the sole and exclusive remedy for money damages related to this Agreement and the transactions contemplated hereby shall be the rights to indemnification set forth in this Section 9.
- `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [12564:12768]: HPIL ET agrees that the sole and exclusive remedy for money damages relating to this Agreement and the transactions contemplated hereby shall be the rights to indemnification set forth in this Section 10.

Returned:
1. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [10500:11000] score 3.03: against and with respect to any claim, liability, obligations, loss, damage, assessment, judgment, cost and expense (including, without limitation, reasonable attorneys' and accountants' fees and costs and expenses reasonably incurred in investigating, preparing, defending against or prosecuting any...
2. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [8250:8750] score 2.93: l authority on the part of GINARES is required in connection with the consummation of the transactions contemplated by this Agreement. 7.3. Compliance With Other Instruments The execution, delivery and performance of this Agreement contemplated hereby will not result in a violation of, or default un...
3. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [17750:18250] score 2.92: eemed an original, but all of which together shall constitute one and the same Agreement. 7 20. No Reliance No third party is entitled to rely on any of the representations, warranties and agreements contained in this Agreement. The Parties assume no liability to any third party because of any relia...

**Query:** Consider the Supply Agreement between Florida Chemical Company, LLC and Flotek Chemistry, LLC for Terpene Products; Does this contract include any volume restrictions?

First relevant passage at rank: 7; recall@8: 0.16

Gold:
- `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [958:1076]: "Maximum Quantity" means [***] pounds of Terpene Product per Year, prorated for any partial Year included in the Term.
- `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [3210:3809]: FCC shall be obligated to accept all such purchase orders unless the amount ordered for a Year exceeds the Maximum Quantity, or orders for a particular quarter exceed [***] pounds or exceed the Flotek forecast for that quarter by more than 25%, provided, however, that, in such event, FCC shall commu...

Returned:
1. `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [12250:12750] score 4.92: party REGARDLESS OF THE NEGLIGENCE OF ANY OF THE INDEMNIFIED PARTIES. 17. Other Sales and Purchases. FCC will be permitted during the Term to sell terpene to other parties who will utilize or resale such terpene for oilfield solvent applications. Notwithstanding any of the terms of this Agreement, F...
2. `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [12500:13000] score 4.80: twithstanding any of the terms of this Agreement, Flotek shall not be restricted from purchasing any terpene-based product, including but not limited to, Terpene Product, from sources other than FCC. 18. Termination. (a) Either Flotek or FCC may terminate the Term immediately, upon a written notice ...
3. `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [7500:8000] score 3.63: being highly confidential in nature. The recipient party agrees to take all reasonable precaution to prevent disclosure of such information to third parties. The recipient party shall hold in confidence any technical or business information the recipient party may learn, observe or otherwise obtain ...

**Query:** Consider the Intellectual Property Agreement for COVID-19 Treatment Development between Marv Enterprises, LLC, Premier Biomedical, Inc., and Technology Health, Inc.; Does this contract include an exclusivity agreement?

First relevant passage at rank: 3; recall@8: 0.19

Gold:
- `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [3388:4736]: The licenses granted herein are exclusive worldwide licenses to: 1. make, have made, use, lease, sell and import Licensed Products for the legal purposes of researching, developing, manufacturing, assembling, distributing, and selling the Licensed Products; 2. make, have made, use and import machine...
- `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [12938:13072]: If THI does not make the obligatory payments as stated in 2(b) by the dates stated, the Exclusive License will revert back to Premier.
- `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [14754:15163]: If THI does not make the obligatory payments as stated in 3(a) by the dates stated, the Exclusive License will revert back to Premier, provided, however, that in such event, THI would still be entitled to a proportionate interest in any Covid-19 Licensed Products, such portion being equal to a fract...

Returned:
1. `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [1500:2000] score 6.38: rv and Premier expanded Premier's Exclusive License to include all the Applications listed in Appendix A via a Third Addendum to the 2010 Agreement executed by Marv and Premier on the Effective Date ("2020 Agreement"). WHEREAS, Marv has filed US provisional patent applications specifically related t...
2. `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [1250:1750] score 4.85: atents via an Agreement executed by Marv and Premier on May 12, 2010 ("2010 Agreement"). WHEREAS, Marv has subsequently filed numerous patent applications on subject matter related to the Issued Patents which are listed in Appendix A. WHEREAS, Marv and Premier expanded Premier's Exclusive License to...
3. `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [3000:3500] score 3.69: Agreement are not contradicted or revised here, the terms as stated in 2010 Agreement/2020 Agreement remain in full effect, are controlling, and apply to THI licensing of the Applications in Appendix A and the Licensed Products derived therefrom. (a) License - THI is granted the following rights to ...

**Query:** Consider the Promotion Agreement between Depomed, Inc. and King Pharmaceuticals, Inc. for Glumetza; Is there an anti-assignment clause in this contract?

First relevant passage at rank: 5; recall@8: 0.38

Gold:
- `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [28504:28839]: Except pursuant to Section 16.9 or in connection with the use of Third Party Sales Representatives, King shall not assign, subcontract or otherwise transfer or delegate any of its rights or obligations under this Agreement without the express written consent of Depomed, which consent may be withheld...
- `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [157751:157952]: This Agreement and the rights granted herein shall not be assignable by either party hereto without the prior written consent of the other party. Any attempted assignment without consent shall be void.

Returned:
1. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [77250:77750] score 6.87: Guidelines on Gifts to Physicians, the PhRMA Code on Interactions with Healthcare Providers, the Prescription Drug Marketing Act of 1987, as amended, and the rules and regulations promulgated thereunder, the ACCME Standards for Commercial Support of Continuing Medical Education, equal employment, no...
2. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [77500:78000] score 6.81: Continuing Medical Education, equal employment, non-discrimination and federal and state anti-kickback Legal Requirements, Legal Requirements with respect to submission of false claims to governmental or private health care payors, and all industry and professional standards, which may be applicable...
3. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [161000:161500] score 6.06: ivative or similar words refer to this entire Agreement; (iv) the terms "Article," "Section," "Exhibit," "Schedule," or "clause" refer to the specified Article, Section, Exhibit, Schedule, or clause of this Agreement; (v) "or" is disjunctive but not necessarily exclusive; and (vi) the term "includin...

## false_abstain (11)

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; What is the governing law for this contract?

First relevant passage at rank: 1; recall@8: 0.99

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [53956:54252]: This Agreement shall be governed by and interpreted in accordance with the laws of England and Wales and the parties to this Agreement submit to the exclusive jurisdiction of the Courts of England and Wales in relation to any claim, dispute or matter arising out of or relating to this Agreement.

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [53750:54250] score 7.08: EEMENT These terms and conditions constitute the entire agreement between the parties and supersede any other agreement whether written or oral previously entered into. 22 JURISDICTION AND CHOICE OF LAW This Agreement shall be governed by and interpreted in accordance with the laws of England and Wa...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [53500:54000] score 5.96: ompany which is for the time being a holding company of the Company or another subsidiary or affiliate of any such holding company as defined by the Companies Act 2006 (as amended) and "Group Companies" will be interpreted accordingly. 21 ENTIRE AGREEMENT These terms and conditions constitute the en...
3. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [45250:45750] score 3.50: aterials embodying these rights to the fullest extent permitted by law in any and all countries of the world. Insofar as such IPRs do not vest automatically by operation of law or under this Agreement, the Consultant holds legal title in these rights and inventions on trust for the Company. 15.6 To ...

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; Are there any exceptions to competitive restrictions in this contract?

First relevant passage at rank: 33; recall@8: 0.00

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [33572:34034]: save that nothing in this paragraph 13.2 shall prevent you from holding (with the prior written consent of the Company, which shall not be unreasonably delayed or withheld) up to three percent (3%) of the issued equity share capital of any company where those equity shares are listed on a recognised...

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [38250:38750] score 14.12: d or engaged in any capacity by any person, firm or company which engages in or provides Restricted Business or commercial activities competitive with the Restricted Business to Restricted Customers or Prospective Customers; (b) in the Restricted Territory, compete with the business of the Company o...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [38000:38500] score 11.98: that you will not during the Restricted Period (and in respect of sub-paragraph 14.2(f) below only, at any time): (a) in the Restricted Territory, compete with the business of the Company or any Group Company by being directly or indirectly employed or engaged in any capacity by any person, firm or ...
3. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [41000:41500] score 11.78: r restrictions or limitations as the case may be. 14.4 For the avoidance of doubt nothing in this paragraph 14 shall prevent you from having any dealings with any Prospective Customer or Restricted Customer in relation to any business which is not Restricted Businesses and which is not competitive w...

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; Does this contract include any right of first refusal, right of first offer, or right of first negotiation?

First relevant passage at rank: 18; recall@8: 0.00

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [6235:6531]: On or as soon as practicable following the Effective Date, it is intended that you will be granted an option under the Option Plan to acquire 107,417 ordinary shares in the capital of BTL ("Shares") (representing approximately 0.6% of the Company's issued share capital as at the Effective Date).
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [6533:7937]: In addition, and conditional on completion of a transaction on terms set out below, you will be granted a second option under the Option Plan, such option being one of: (a) an option to acquire 44,757 Shares (representing approximately 0.25% of the Company's issued share capital as at the Effective ...

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [29500:30000] score 13.83: concerning your employment should be taken up orally in the first instance with the CEO. If the grievance is not resolved to your satisfaction, you should then refer it to the Chairman. 12.3 The Company reserves the right to suspend you on full pay and benefits at any time for a reasonable period to...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [29250:29750] score 13.37: n the Schedule to this Agreement. 12 DISCIPLINARY, DISMISSAL AND GRIEVANCE PROCEDURES 12.1 A copy of the Company's disciplinary, dismissal and grievance procedures are set out in its employee handbook (the "Employee Handbook"). 12.2 Any grievance concerning your employment should be taken up orally ...
3. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [21250:21750] score 12.99: ; (ii) a material diminution in your Salary; (iii) a material change in the geographic location at which you provides services to the Company; or (iv) the material breach of this Agreement by the Company. "Good Reason Process" shall mean that (i) you reasonably determine in good faith that a "Good R...

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; How is intellectual property ownership assigned in this contract?

First relevant passage at rank: 3; recall@8: 0.79

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [44840:45359]: To the extent that such IPRs do not vest automatically in the Company by operation of law, you hereby assign and agree to assign to the Company all of your right, title and interest in any existing and future IPRs which may subsist in any Works for their full term of protection (including any extens...

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [48500:49000] score 9.11: t and at all times thereafter subject always to your obligations to third parties, you shall furnish such information and proper assistance to the Company or any Group Companies as it or they may reasonably require in connection with the Company's intellectual property (including without limitation ...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [48750:49250] score 7.66: tellectual property (including without limitation applying for, defending, maintaining and protecting such intellectual property) and in connection with litigation in which it is or they are or may become a party. This obligation on you shall include, without limitation, meeting with the Company or ...
3. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [44750:45250] score 6.87: .4 All IPRs subsisting in any Works shall be the exclusive property of the Company. 15.5 To the extent that such IPRs do not vest automatically in the Company by operation of law, you hereby assign and agree to assign to the Company all of your right, title and interest in any existing and future IP...

## false_answer (12)

**Query:** Consider the Agency Agreement between General Electric Capital Corporation and Duckwall-Alco Stores, Inc. for Equipment Leasing; What is the governing law for this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [11250:11355] score 4.31: and conditions of the lease contract are set forth in the Master Lease Agreement and Equipment Schedule.
2. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [11000:11355] score 3.13: appropriate Purchase Order/Sales Agreement Number. General Electric Capital Corporation will also require a complete set of Lease documentation prior to funding. These documents may include a Schedule and a Certificate of Acceptance. The full terms and conditions of the lease contract are set forth ...
3. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [0:500] score 0.00: Exhibit 10.26 AGENCY AGREEMENT THIS AGENCY AGREEMENT, dated November 9, 2005 ("Agreement"), between General Electric Capital Corporation, a Delaware corporation (together with its successors and assigns, if any, "Lessor"), and Duckwall-Alco Stores, Inc., a Kansas corporation (the "Company"). Capital...

**Query:** Consider the Sponsorship Agreement between R. C. Boyd Enterprises, LLC and Cano Petroleum, Inc. for 'Honey Hole'; What are the audit rights under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [7250:7750] score 4.73: agreements, either oral or in writing, between the parties with respect to the subject matter of this contract, and contains all of the covenants and agreements between the parties with respect to the subject matter. Each party to this contract acknowledges that no representations, inducements, prom...
2. `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [7500:8000] score 4.07: knowledges that no representations, inducements, promises, or agreements, orally or otherwise, have been made by any party, or anyone acting on behalf of any party, that are 2 not set forth in this contract, and that no agreement, statement, or promise not contained in this contract shall be valid o...
3. `CANOPETROLEUM,INC_12_13_2007-EX-10.1-Sponsorship Agreement.t` [7000:7500] score 3.95: l be paid to the Company at Southlake, Tarrant County, Texas. 18. Assignment. This Agreement may not be assigned by either party without the prior written consent of the other party. 19. Other Agreements. This Agreement supersedes any and all other agreements, either oral or in writing, between the ...

**Query:** Consider the Cooperation Agreement between HPIL ENERGYTECH Inc. and GINARES GROUP AG for Renewable Energy Projects; What are the audit rights under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [8500:9000] score 4.50: hereby will not result in a violation of, or default under, any instrument, judgment, order, writ, decree or contract known to GINARES, or an event that results in the creation of any lien, charge or encumbrance upon the Agreement. 7.4. Litigation There is no action, suit, proceeding or investigatio...
2. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [10000:10500] score 4.20: , judgment, order, writ, decree or contract known to HPIL ET, or an event that results in the creation of any lien, charge or encumbrance upon the Agreement. 8.4. Litigation There is no action, suit, proceeding or investigation pending or, to HPIL ET's knowledge, currently threatened that questions ...
3. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [8250:8750] score 2.93: l authority on the part of GINARES is required in connection with the consummation of the transactions contemplated by this Agreement. 7.3. Compliance With Other Instruments The execution, delivery and performance of this Agreement contemplated hereby will not result in a violation of, or default un...

**Query:** Consider the Marketing Agreement between Loop Industries, Inc. and Indorama Loop Technologies, LLC for Product Supply and Development; What are the audit rights under this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `Loop Industries, Inc. - Marketing Agreement.txt` [8500:9000] score 7.53: sed Contract that does not qualify as an Eligible Contract shall be a "Considered Contract." 2.3 Acceptance of Proposed Contracts. All Eligible Contracts shall be deemed accepted by the Joint Venture Company and become a Transferred Contract on the date Loop delivers the Proposed Contract Notice for...
2. `Loop Industries, Inc. - Marketing Agreement.txt` [30500:31000] score 7.05: of the Assignee all of the Assignor's right, title, and interest in, to, and under the Transferred Contract, together with its related rights, warranties, remedies, powers, and privileges (collectively, the "Assigned Rights"). The Assignee hereby accepts the Assigned Rights. b. The Assignor hereby d...
3. `Loop Industries, Inc. - Marketing Agreement.txt` [8750:9250] score 6.99: ate Loop delivers the Proposed Contract Notice for such Eligible Contract to the Joint Venture Company. In the event that the Proposed Contract Notice is a Considered Contract, the Joint Venture Company will have the right to review and determine whether to accept or reject the Considered Contract w...
