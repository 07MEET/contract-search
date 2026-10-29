# Error report: baseline on train

140 answerable and 29 unanswerable queries. Labels use the top 8 passages.

| Label | Count |
|---|---|
| wrong_section | 114 |
| partial_span | 13 |
| false_answer | 29 |
| hit | 13 |

## wrong_section (114)

**Query:** Consider the Amendment No. 3 to Wireless Content License Agreement between Fox Mobile Entertainment, Inc. and Glu Mobile Inc.; What is the expiration date of this contract?

First relevant passage at rank: not in top 64; recall@8: 0.00

Gold:
- `GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content ` [598:989]: The rights granted hereunder shall be effective as of the Effective Date and shall expire on December 31, 2006 (the "Term"); provided, however, that with respect to each Property, including Robots, Kingdom of Heaven, Mr. and Mrs. Smith, In Her Shoes, Idiocracy (Oww My Balls) and Ice Age II, all righ...

Returned:
1. `GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content ` [0:500] score 89.43: AMENDMENT NO. 3 Dated as of February 19, 2007 Reference is hereby made to that certain fully executed Wireless Content License Agreement Number 12965 dated as of December 16, 2004, as amended November 11, 2005 and March 27, 2006 (the "Agreement"), between Fox Mobile Entertainment, Inc. ("Fox"), as A...
2. `GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content ` [1500:1902] score 75.05: e to all of the terms and conditions hereof. Glu Mobile Inc. ("Licensee") Fox Mobile Entertainment, Inc. ("Fox") By: /s/ Albert A. Pimentel By: /s/ Jamie Samson Name: Albert A. Pimentel Name: Jamie Samson Its: EVP and CFO Its: Senior Vice President Date: Date: Source: GLU MOBILE INC, S-1/A, 3/19/200...
3. `BONTONSTORESINC_04_20_2018-EX-99.3-AGENCY AGREEMENT.txt` [136000:136500] score 29.41: including e-mail addresses) set forth in the signature block of this Notice on or before [_], 2018.3 If no timely objection to the assumption and assignment of a Lease or Contract is received, the assumption and assignment of such Lease or Contract will become effective automatically pursuant to the...

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; What is the governing law for this contract?

First relevant passage at rank: 49; recall@8: 0.00

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [53956:54252]: This Agreement shall be governed by and interpreted in accordance with the laws of England and Wales and the parties to this Agreement submit to the exclusive jurisdiction of the Courts of England and Wales in relation to any claim, dispute or matter arising out of or relating to this Agreement.

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [0:500] score 46.25: Exhibit 10.11 DATED 26 September 2019 BicycleTX Ltd and Nigel Crockett ___________________________________________________ SERVICE AGREEMENT ___________________________________________________ THIS AGREEMENT is made on 26 September 2019 BETWEEN: (1) BICYCLETX LIMITED a company incorporated under the...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [56500:57000] score 35.31: any other way, including but not limited to by way of a merger. 19 THIS AGREEMENT has been executed and delivered as a deed by or on behalf of the parties on the date written at the top of page 1. Executed as a Deed by BICYCLETX LIMITED acting by a director: /s/ Kevin Lee (Director) in the presence ...
3. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [12000:12500] score 26.59: President or Chief Executive Officer) and the Chief Commercial Officer of King (or, if there is no such officer, its President or Chief Executive Officer). Section 1.39 "FDA" means the United States Food and Drug Administration or any successor agency performing comparable functions in the Territory...

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; Are there any exceptions to competitive restrictions in this contract?

First relevant passage at rank: not in top 64; recall@8: 0.00

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [33572:34034]: save that nothing in this paragraph 13.2 shall prevent you from holding (with the prior written consent of the Company, which shall not be unreasonably delayed or withheld) up to three percent (3%) of the issued equity share capital of any company where those equity shares are listed on a recognised...

Returned:
1. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [0:500] score 42.33: Exhibit 10.11 DATED 26 September 2019 BicycleTX Ltd and Nigel Crockett ___________________________________________________ SERVICE AGREEMENT ___________________________________________________ THIS AGREEMENT is made on 26 September 2019 BETWEEN: (1) BICYCLETX LIMITED a company incorporated under the...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [56500:57000] score 37.50: any other way, including but not limited to by way of a merger. 19 THIS AGREEMENT has been executed and delivered as a deed by or on behalf of the parties on the date written at the top of page 1. Executed as a Deed by BICYCLETX LIMITED acting by a director: /s/ Kevin Lee (Director) in the presence ...
3. `KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMEN` [12000:12500] score 31.31: President or Chief Executive Officer) and the Chief Commercial Officer of King (or, if there is no such officer, its President or Chief Executive Officer). Section 1.39 "FDA" means the United States Food and Drug Administration or any successor agency performing comparable functions in the Territory...

**Query:** Consider the Service Agreement between BicycleTX Ltd and Nigel Crockett for Chief Business Officer Position; Does this contract include any right of first refusal, right of first offer, or right of first negotiation?

First relevant passage at rank: not in top 64; recall@8: 0.00

Gold:
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [6235:6531]: On or as soon as practicable following the Effective Date, it is intended that you will be granted an option under the Option Plan to acquire 107,417 ordinary shares in the capital of BTL ("Shares") (representing approximately 0.6% of the Company's issued share capital as at the Effective Date).
- `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [6533:7937]: In addition, and conditional on completion of a transaction on terms set out below, you will be granted a second option under the Option Plan, such option being one of: (a) an option to acquire 44,757 Shares (representing approximately 0.25% of the Company's issued share capital as at the Effective ...

Returned:
1. `IGENEBIOTECHNOLOGYINC_05_13_2003-EX-1-JOINT VENTURE AGREEMEN` [39500:40000] score 52.65: the date Igene receives such notice. 11.3. In the event of a contradiction between the terms of this Article 11 and any Support Services Agreement, the terms of the Support Services Agreement shall govern. 12. RIGHT OF FIRST REFUSAL; TERMINATION OF THE JOINT VENTURE AFTER THE EFFECTIVE DATE. 12.1. R...
2. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [0:500] score 47.78: Exhibit 10.11 DATED 26 September 2019 BicycleTX Ltd and Nigel Crockett ___________________________________________________ SERVICE AGREEMENT ___________________________________________________ THIS AGREEMENT is made on 26 September 2019 BETWEEN: (1) BICYCLETX LIMITED a company incorporated under the...
3. `BICYCLETHERAPEUTICSPLC_03_10_2020-EX-10.11-SERVICE AGREEMENT` [56500:57000] score 44.39: any other way, including but not limited to by way of a merger. 19 THIS AGREEMENT has been executed and delivered as a deed by or on behalf of the parties on the date written at the top of page 1. Executed as a Deed by BICYCLETX LIMITED acting by a director: /s/ Kevin Lee (Director) in the presence ...

## partial_span (13)

**Query:** Consider the Cooperation Agreement between HPIL ENERGYTECH Inc. and GINARES GROUP AG for Renewable Energy Projects; Is there a cap on liability under this contract?

First relevant passage at rank: 8; recall@8: 0.29

Gold:
- `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [11380:11583]: GINARES agrees that the sole and exclusive remedy for money damages related to this Agreement and the transactions contemplated hereby shall be the rights to indemnification set forth in this Section 9.
- `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [12564:12768]: HPIL ET agrees that the sole and exclusive remedy for money damages relating to this Agreement and the transactions contemplated hereby shall be the rights to indemnification set forth in this Section 10.

Returned:
1. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [3500:4000] score 57.40: T THIS COOPERATION AGREEMENT ("Agreement") is signed this 5th day of January, 2015 (the "Closing Date"), by and between HPIL ENERGYTECH Inc., a Nevada (USA) corporation (hereafter "HPIL ET") and GINARES GROUP AG, a private company domiciled in Switzerland (hereafter "GINARES"). R E C I T A L S: The ...
2. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [0:500] score 53.60: COOPERATION AGREEMENT made by and between HPIL ENERGYTECH Inc. and GINARES GROUP AG January 5, 2015 Table of Contents 1. Term........................................................................................................................................... 2 2. Goals And Objectives.............
3. `HPILHOLDING_01_07_2015-EX-99.1-COOPERATION AGREEMENT.txt` [19500:20000] score 44.72: similar), nor shall such waiver constitute a continuing waiver unless otherwise expressly therein provided. THIS COOPERATION AGREEMENT has been entered into as of the date first set forth above. GINARES : GINARES GROUP AG, a private company domiciled in Switzerland. By: /s/ Peter Zu Sayn-Wittgenstei...

**Query:** Consider the Supply Agreement between Florida Chemical Company, LLC and Flotek Chemistry, LLC for Terpene Products; Does this contract include any volume restrictions?

First relevant passage at rank: 7; recall@8: 0.06

Gold:
- `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [958:1076]: "Maximum Quantity" means [***] pounds of Terpene Product per Year, prorated for any partial Year included in the Term.
- `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [3210:3809]: FCC shall be obligated to accept all such purchase orders unless the amount ordered for a Year exceeds the Maximum Quantity, or orders for a particular quarter exceed [***] pounds or exceed the Flotek forecast for that quarter by more than 25%, provided, however, that, in such event, FCC shall commu...

Returned:
1. `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [0:500] score 52.70: Exhibit 10.1 Information identified with "[***]" has been excluded from this exhibit because it is both not material and would likely cause competitive harm to the registrant if publicly disclosed. SUPPLY AGREEMENT This Supply Agreement (the "Agreement") is entered into as of February 28, 2019 by an...
2. `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [19000:19355] score 48.40: have executed this Agreement as of the date and year first set forth above. FLORIDA CHEMICAL COMPANY, LLC: By: /s/ Elizabeth T. Wilkinson Name: Elizabeth T. Wilkinson Title: Chief Financial Officer FLOTEK CHEMISTRY, LLC: By: /s/ Elizabeth T. Wilkinson Name: Elizabeth T. Wilkinson Title: Chief Financ...
3. `FLOTEKINDUSTRIESINCCN_05_09_2019-EX-10.1-SUPPLY AGREEMENT.tx` [4000:4500] score 29.37: en, Florida. Transportation shall be arranged by Flotek. All sales of Terpene Product subject to this Agreement shall be pursuant to the terms and conditions attached hereto as Exhibit B. (c) FCC shall invoice Flotek for Terpene Product at the time of shipment. Payment of FCC invoices shall be due w...

**Query:** Consider the Intellectual Property Agreement for COVID-19 Treatment Development between Marv Enterprises, LLC, Premier Biomedical, Inc., and Technology Health, Inc.; Does this contract include an exclusivity agreement?

First relevant passage at rank: 5; recall@8: 0.13

Gold:
- `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [3388:4736]: The licenses granted herein are exclusive worldwide licenses to: 1. make, have made, use, lease, sell and import Licensed Products for the legal purposes of researching, developing, manufacturing, assembling, distributing, and selling the Licensed Products; 2. make, have made, use and import machine...
- `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [12938:13072]: If THI does not make the obligatory payments as stated in 2(b) by the dates stated, the Exclusive License will revert back to Premier.
- `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [14754:15163]: If THI does not make the obligatory payments as stated in 3(a) by the dates stated, the Exclusive License will revert back to Premier, provided, however, that in such event, THI would still be entitled to a proportionate interest in any Covid-19 Licensed Products, such portion being equal to a fract...

Returned:
1. `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [0:500] score 51.03: Exhibit 10.2 INTELLECTUAL PROPERTY AGREEMENT This Intellectual Property Agreement (this "Agreement") is entered into on May 12, 2020 ("Effective Date"), concerning the pursuits set forth herein for the collective development, implementation and commercialization of a potential treatment for the COVI...
2. `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [14000:14500] score 50.39: an hourly rate to Mohammed Zulfiquar and his designees. (b). Premier may partner with other organizations as needed to effectuate the development of technology in the Field of Covid-19 Treatments. (c) Marv will have no direct role in the development of technology in the Field of Covid-19 Treatment o...
3. `PREMIERBIOMEDICALINC_05_14_2020-EX-10.2-INTELLECTUAL PROPERT` [500:1000] score 47.03: of the Commonwealth of Pennsylvania ("Marv"), Premier Biomedical, Inc. (OTC Pink: BIEI), a Nevada corporation ("Premier"), Technology Health, Inc. (OTC Pink: HALB), a Colorado corporation f/k/a Halberd Corporation ("THI"), Each shall be referred to as a "Party" and collectively as the "Parties." REC...

**Query:** Consider the Marketing and Transportation Services Agreement between Purolator Courier Ltd. and Parcelway Courier Systems Canada Ltd. (Dynamex Inc.); What is the expiration date of this contract?

First relevant passage at rank: 5; recall@8: 0.04

Gold:
- `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [3307:3509]: This Agreement shall be effective from the date first above written and shall continue indefinitely until terminated by either Party in accordance with the provisions of this Agreement.

Returned:
1. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [0:500] score 81.72: 1 EXHIBIT 10.4 MARKETING AND TRANSPORTATION SERVICES AGREEMENT THIS AGREEMENT made in duplicate this 20 day of November, 1995. B E T W E E N: PUROLATOR COURIER LTD. ("Purolator") - and - PARCELWAY COURIER SYSTEMS CANADA LTD
2. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [48500:49000] score 61.47: e written by their proper officers duly authorized on that behalf. PARCELWAY COURIER SYSTEMS CANADA LTD. Per: (ILLEGIBLE) 11/20/95 c/s ----------------------------- Per: c/s ----------------------------- PUROLATOR COURIER LTD. Per: (ILLEGIBL
3. `DYNAMEXINC_06_06_1996-EX-10.4-TRANSPORTATION SERVICES AGREEM` [500:1000] score 60.06: . a subsidiary of Dynamex Inc. ("Dynamex") WHEREAS Purolator inter alia, is licensed to provide courier services for compensation across Canada and the United States of America; AND WHEREAS Dynamex inter alia, is licensed to provide courier services for compensation across Canada and the United Stat...

## false_answer (29)

**Query:** Consider the Agency Agreement between General Electric Capital Corporation and Duckwall-Alco Stores, Inc. for Equipment Leasing; What is the governing law for this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [10500:11000] score 69.86: -Alco Stores, Inc. is ordering the following equipment as Agent for: General Electric Capital Corporation 311 North Bayshore Drive Safety Harbor, FL 34695 Attn: Teresa Schafer • All invoices should indicate that General Electric Capital Corporation is the "Sold to" party at the above address, and th...
2. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [10000:10500] score 62.79: presentatives to execute and deliver this Agreement on the date first above written. General Electric Capital Corporation Duckwall-Alco Stores, Inc. By: /s/ Susan Lyndon By: /s/ Richard A. Mansfield Title: Manager Portfolio Admin Title: V.P./CFO AGENCY AGREEMENT INSTRUCTIONS BEFORE EQUIPMENT IS ORDE...
3. `ALCOSTORESINC_12_14_2005-EX-10.26-AGENCY AGREEMENT.txt` [0:500] score 58.86: Exhibit 10.26 AGENCY AGREEMENT THIS AGENCY AGREEMENT, dated November 9, 2005 ("Agreement"), between General Electric Capital Corporation, a Delaware corporation (together with its successors and assigns, if any, "Lessor"), and Duckwall-Alco Stores, Inc., a Kansas corporation (the "Company"). Capital...

**Query:** Consider the Sponsorship Agreement between Jacksonville Jaguars, LLC and The ARC Group, Inc.; What is the governing law for this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `ArcGroupInc_20171211_8-K_EX-10.1_10976103_EX-10.1_Sponsorshi` [0:500] score 53.94: Exhibit 10.1 JACKSONVILLE JAGUARS SPONSORSHIP AGREEMENT This Sponsorship Agreement (this "Agreement") is entered into as of November 27, 2017 (the "Execution Date") by and between Jacksonville Jaguars, LLC, a Delaware limited liability company ("Club"), and The ARC Group, Inc., a Florida corporation...
2. `ArcGroupInc_20171211_8-K_EX-10.1_10976103_EX-10.1_Sponsorshi` [9000:9500] score 38.50: cuted counterpart by electronic transmission shall have the same effect as delivery of an original ink counterpart. IN WITNESS WHEREOF, each party has caused this Agreement to be executed in Jacksonville, Florida, by its duly authorized representative with the intent that it be binding as of the Exe...
3. `ArcGroupInc_20171211_8-K_EX-10.1_10976103_EX-10.1_Sponsorshi` [7000:7500] score 36.64: med by one of the other permissible methods of giving notice hereunder), one business day after being sent by a nationally recognized overnight courier, or three business days after being mailed by registered or certified mail, postage prepaid and return receipt requested, to the parties at the foll...

**Query:** Consider the Amendment No. 3 to Wireless Content License Agreement between Fox Mobile Entertainment, Inc. and Glu Mobile Inc.; What is the governing law for this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content ` [0:500] score 86.84: AMENDMENT NO. 3 Dated as of February 19, 2007 Reference is hereby made to that certain fully executed Wireless Content License Agreement Number 12965 dated as of December 16, 2004, as amended November 11, 2005 and March 27, 2006 (the "Agreement"), between Fox Mobile Entertainment, Inc. ("Fox"), as A...
2. `GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content ` [1500:1902] score 70.37: e to all of the terms and conditions hereof. Glu Mobile Inc. ("Licensee") Fox Mobile Entertainment, Inc. ("Fox") By: /s/ Albert A. Pimentel By: /s/ Jamie Samson Name: Albert A. Pimentel Name: Jamie Samson Its: EVP and CFO Its: Senior Vice President Date: Date: Source: GLU MOBILE INC, S-1/A, 3/19/200...
3. `DeltathreeInc_19991102_S-1A_EX-10.19_6227850_EX-10.19_Co-Bra` [26000:26500] score 27.43: Section 9.11 [Governing Law]. Governing Law. This Agreement shall be governed by, and construed in accordance with, the laws of the State of New York, without giving effect to the conflict of laws principles thereof. For purposes of this Source: DELTATHREE INC, S-1/A, 11/2/1999 Agreement, each party...

**Query:** Consider the Gas Franchise Agreement between the Town of Vinton and Roanoke Gas Company; What is the governing law for this contract?

Unanswerable (missing_clause), but the system answered.

Returned:
1. `RgcResourcesInc_20151216_8-K_EX-10.3_9372751_EX-10.3_Franchi` [0:500] score 62.52: Exhibit 10.3 GAS FRANCHISE AGREEMENT THIS AGREEMENT ("Agreement"), made and entered into this 17th day of November, 2015, by and between the TOWN OF VINTON, VIRGINIA, a Virginia municipal corporation ("Grantor"), and ROANOKE GAS COMPANY, a Virginia corporation ("Grantee"). WHEREAS, Grantor has revie...
2. `RgcResourcesInc_20151216_8-K_EX-10.3_9372751_EX-10.3_Franchi` [4000:4500] score 46.76: s (or any other address the party to be notified may have designated to the sender by like notice): Grantor: Grantee: Town of Vinton Roanoke Gas Company Attention: Town Manager Attention: President 311 S. Pollard Street 519 Kimball Avenue, N.E. Vinton, Virginia 24179 P.O. Box 13007 Roanoke, Virginia...
3. `RgcResourcesInc_20151216_8-K_EX-10.3_9372751_EX-10.3_Franchi` [1500:2000] score 46.21: ty of Salem ("Salem") and the Town of Vinton ("Vinton") (Grantor, Roanoke and Salem being hereinafter sometimes collectively referred to as the "localities" and singularly as a "locality") with fee provisions identical to this one, and that the total annual Franchise Fee to be paid to the three loca...
