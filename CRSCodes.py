import urllib2
from bs4 import BeautifulSoup
import geocoder
import os

#full list of CRS Codes from CORPUS data http://nrodwiki.rockshore.net/index.php/Reference_Data#Downloading_CORPUS_Data
CRSCODES = ["AAP","AAT","ABA","ABC","ABD","ABE","ABF","ABH","ABL","ABO","ABR","ABW","ABY","ACB","ACC","ACG","ACH","ACK","ACL","ACM","ACN","ACR","ACT","ACY","ADC","ADD","ADK","ADL","ADM","ADN","ADR","ADS","ADV","ADW","AER","AFD","AFK","AFS","AFV","AGL","AGR","AGS","AGT","AGV","AHD","AHN","AHS","AHT","AHV","AIG","AIN","AIR","ALB","ALD","ALE","ALF","ALK","ALM","ALN","ALO","ALP","ALR","ALS","ALT","ALV","ALW","ALX","AMB","AMD","AMF","AMI","AML","AMM","AMO","AMR","AMS","AMT","AMW","AMY","ANC","AND","ANF","ANG","ANH","ANL","ANM","ANN","ANS","ANZ","AON","APB","APD","APF","APG","APN","APP","APS","APY","ARA","ARB","ARD","ARG","ARL","ARM","ARN","ARP","ARR","ART","ARU","ARW","ARZ","ASB","ASC","ASF","ASG","ASH","ASI","ASK","ASM","ASN","ASP","ASS","AST","ASY","ATB","ATH","ATL","ATM","ATN","ATO","ATR","ATS","ATT","ATW","ATY","AUD","AUG","AUI","AUK","AUL","AUR","AUW","AVF","AVI","AVM","AVN","AVP","AVY","AWK","AWL","AWM","AWT","AXM","AXP","AYH","AYL","AYP","AYR","AYS","AYW","BAA","BAB","BAC","BAD","BAE","BAG","BAH","BAI","BAJ","BAK","BAL","BAM","BAN","BAO","BAP","BAQ","BAR","BAS","BAT","BAU","BAV","BAW","BAX","BAY","BAZ","BBG","BBK","BBL","BBN","BBR","BBS","BBW","BBY","BCB","BCC","BCE","BCF","BCG","BCH","BCJ","BCK","BCN","BCS","BCU","BCV","BCW","BCY","BDA","BDB","BDC","BDD","BDF","BDG","BDH","BDI","BDK","BDL","BDM","BDN","BDQ","BDT","BDW","BDY","BDZ","BEA","BEB","BEC","BED","BEE","BEF","BEG","BEH","BEL","BEM","BEN","BEO","BEP","BER","BES","BET","BEU","BEV","BEW","BEX","BEY","BFA","BFC","BFD","BFE","BFF","BFL","BFN","BFP","BFQ","BFR","BGA","BGD","BGE","BGG","BGH","BGI","BGK","BGL","BGM","BGN","BGR","BGS","BHA","BHC","BHD","BHG","BHI","BHK","BHM","BHN","BHO","BHR","BHS","BIA","BIB","BIC","BID","BIF","BIG","BIH","BIK","BIL","BIN","BIO","BIP","BIR","BIS","BIT","BIW","BIY","BKA","BKC","BKD","BKG","BKH","BKI","BKJ","BKL","BKM","BKN","BKO","BKP","BKQ","BKR","BKS","BKT","BKV","BKW","BKZ","BLA","BLB","BLC","BLD","BLE","BLG","BLH","BLK","BLL","BLM","BLN","BLO","BLP","BLR","BLT","BLV","BLW","BLX","BLY","BLZ","BMA","BMB","BMC","BMD","BME","BMF","BMG","BMH","BMK","BML","BMM","BMN","BMO","BMP","BMR","BMS","BMT","BMV","BMY","BNA","BNC","BND","BNE","BNF","BNG","BNH","BNI","BNJ","BNK","BNL","BNM","BNO","BNP","BNR","BNS","BNT","BNU","BNV","BNW","BNX","BNY","BOA","BOB","BOC","BOD","BOE","BOG","BOH","BOK","BOM","BON","BOP","BOQ","BOR","BOT","BOU","BOX","BPB","BPK","BPL","BPN","BPO","BPS","BPT","BPW","BRA","BRC","BRD","BRE","BRF","BRG","BRH","BRI","BRJ","BRK","BRL","BRM","BRN","BRO","BRP","BRR","BRS","BRT","BRU","BRV","BRW","BRX","BRY","BRZ","BSB","BSC","BSD","BSE","BSG","BSH","BSI","BSJ","BSK","BSL","BSM","BSN","BSO","BSP","BSR","BSS","BSU","BSV","BSW","BSY","BTB","BTD","BTE","BTF","BTG","BTH","BTL","BTN","BTO","BTP","BTR","BTS","BTT","BTY","BUA","BUB","BUC","BUD","BUE","BUG","BUH","BUI","BUJ","BUK","BUL","BUM","BUO","BUR","BUS","BUT","BUU","BUW","BUX","BUY","BUZ","BVD","BWB","BWD","BWG","BWK","BWL","BWN","BWO","BWS","BWT","BWY","BXB","BXD","BXH","BXS","BXW","BXX","BXY","BYA","BYB","BYC","BYD","BYE","BYF","BYI","BYK","BYL","BYM","BYN","BYS","BZY","CAA","CAB","CAC","CAD","CAG","CAH","CAI","CAK","CAL","CAM","CAN","CAO","CAQ","CAR","CAS","CAT","CAU","CAW","CAY","CAZ","CBB","CBC","CBD","CBE","CBG","CBH","CBK","CBL","CBN","CBP","CBR","CBS","CBU","CBW","CBY","CBZ","CCB","CCC","CCH","CCN","CCR","CCT","CDB","CDD","CDF","CDI","CDN","CDO","CDQ","CDR","CDS","CDT","CDU","CDY","CEA","CED","CEF","CEH","CEI","CEL","CEM","CER","CES","CET","CEY","CFB","CFC","CFD","CFF","CFH","CFL","CFN","CFO","CFR","CFT","CFX","CGD","CGM","CGN","CGT","CGW","CHA","CHB","CHC","CHD","CHE","CHF","CHG","CHH","CHI","CHJ","CHK","CHL","CHM","CHN","CHO","CHP","CHR","CHS","CHT","CHU","CHV","CHW","CHX","CHY","CHZ","CIC","CIL","CIM","CIR","CIT","CKA","CKH","CKL","CKN","CKS","CKT","CKU","CKY","CLA","CLB","CLC","CLD","CLE","CLG","CLH","CLI","CLJ","CLK","CLL","CLM","CLN","CLO","CLP","CLQ","CLR","CLS","CLT","CLU","CLV","CLW","CLX","CLY","CLZ","CMB","CMC","CMD","CME","CMF","CMH","CMI","CMK","CML","CMN","CMO","CMP","CMR","CMT","CMY","CNA","CNE","CNF","CNG","CNK","CNL","CNM","CNN","CNO","CNP","CNR","CNS","CNW","CNY","COA","COB","COC","COE","COF","COH","COI","COK","COL","COM","CON","COO","COP","COQ","COR","COS","COT","COU","COV","COW","COX","COY","COZ","CPA","CPB","CPG","CPH","CPK","CPM","CPN","CPS","CPT","CPU","CPW","CPY","CRA","CRB","CRC","CRD","CRE","CRF","CRG","CRH","CRI","CRJ","CRK","CRL","CRM","CRN","CRO","CRP","CRQ","CRR","CRS","CRT","CRU","CRV","CRW","CRX","CRY","CRZ","CSA","CSB","CSD","CSE","CSG","CSH","CSK","CSL","CSM","CSN","CSO","CSQ","CSR","CSS","CST","CSW","CSY","CTB","CTE","CTF","CTH","CTK","CTL","CTM","CTN","CTO","CTR","CTT","CTW","CUA","CUB","CUD","CUF","CUH","CUL","CUM","CUP","CUW","CUX","CVO","CWB","CWC","CWD","CWE","CWH","CWL","CWM","CWN","CWS","CWT","CWU","CYA","CYB","CYH","CYK","CYM","CYN","CYP","CYS","CYT","DAG","DAK","DAL","DAM","DAN","DAR","DAT","DAW","DAX","DBB","DBC","DBD","DBE","DBG","DBL","DBP","DBR","DBY","DBZ","DCG","DCH","DCL","DCT","DCW","DDB","DDG","DDK","DDP","DEA","DEB","DED","DEE","DEN","DEP","DEW","DFD","DFE","DFI","DFL","DFP","DFR","DFZ","DGC","DGL","DGS","DGT","DGY","DHC","DHM","DHN","DHS","DHT","DID","DIE","DIG","DIJ","DIN","DIS","DKD","DKG","DKR","DKT","DLE","DLG","DLH","DLJ","DLK","DLM","DLO","DLR","DLS","DLT","DLW","DLY","DMC","DMD","DMF","DMG","DMH","DMK","DML","DMP","DMR","DMS","DMY","DND","DNG","DNL","DNM","DNN","DNO","DNS","DNT","DNY","DOC","DOD","DOE","DOL","DON","DOR","DOT","DOW","DOZ","DPD","DPS","DPT","DRA","DRD","DRF","DRG","DRI","DRM","DRN","DRO","DRT","DRU","DRY","DSL","DSM","DST","DSY","DTG","DTM","DTN","DTW","DUD","DUE","DUI","DUK","DUL","DUM","DUN","DUO","DUR","DUS","DUT","DUU","DVB","DVC","DVH","DVM","DVN","DVP","DVR","DVY","DWD","DWI","DWL","DWN","DWW","DYC","DYF","DYP","DZY","EAD","EAG","EAL","EAR","EAS","EBA","EBB","EBD","EBF","EBK","EBL","EBN","EBR","EBS","EBT","EBV","ECC","ECL","ECM","ECP","ECR","ECS","ECW","EDB","EDG","EDL","EDM","EDN","EDP","EDR","EDW","EDY","EDZ","EFD","EFF","EFL","EGF","EGG","EGH","EGN","EGR","EGT","EGY","EHC","EIG","EKB","EKL","ELD","ELE","ELG","ELM","ELN","ELO","ELP","ELR","ELS","ELW","ELY","EMA","EMD","EML","EMP","EMS","ENC","ENF","ENL","ENN","ENS","ENT","EPD","EPH","EPS","ERA","ERB","ERD","ERH","ERI","ERL","ERS","ESD","ESH","ESL","ESM","ESS","EST","ESW","ETC","ETL","EUS","EVE","EWD","EWE","EWR","EWW","EXC","EXD","EXG","EXM","EXN","EXQ","EXR","EXT","EYM","EYN","FAL","FAR","FAV","FAX","FAZ","FBY","FCN","FEA","FED","FEG","FEL","FEN","FER","FFA","FFD","FGH","FGT","FGW","FGY","FHM","FIL","FIN","FIT","FKC","FKE","FKG","FKH","FKK","FKW","FLD","FLE","FLF","FLI","FLM","FLN","FLS","FLT","FLW","FLX","FLZ","FML","FMR","FMT","FNB","FNC","FNH","FNI","FNN","FNR","FNT","FNV","FNW","FNY","FOB","FOC","FOD","FOG","FOH","FOK","FOR","FOT","FOX","FPK","FPX","FRA","FRB","FRD","FRE","FRF","FRH","FRI","FRL","FRM","FRN","FRO","FRR","FRS","FRT","FRW","FRY","FSB","FSG","FSK","FST","FTM","FTN","FTW","FWN","FWY","FXF","FXN","FYS","FZH","FZP","FZW","GAL","GAR","GBD","GBG","GBK","GBL","GBS","GCH","GCL","GCR","GCT","GCW","GDE","GDH","GDL","GDN","GDP","GEA","GER","GFD","GFF","GFN","GFY","GGJ","GGL","GGM","GGO","GGT","GGV","GIG","GIL","GIP","GIR","GKC","GKW","GLC","GLD","GLE","GLF","GLG","GLH","GLM","GLO","GLQ","GLR","GLS","GLT","GLY","GLZ","GMB","GMD","GMG","GMN","GMT","GMV","GMY","GNB","GNF","GNH","GNL","GNR","GNT","GNW","GOB","GOD","GOE","GOF","GOL","GOM","GOO","GOP","GOR","GOS","GOX","GOY","GOZ","GPK","GPO","GQL","GRA","GRB","GRC","GRF","GRH","GRK","GRL","GRM","GRN","GRO","GRP","GRS","GRT","GRV","GRY","GSB","GSC","GSD","GSL","GSN","GSO","GSP","GST","GSW","GSY","GTA","GTG","GTH","GTN","GTO","GTR","GTW","GTY","GUI","GUN","GUS","GVE","GVH","GWE","GWN","GWY","GXX","GYM","GYP","HAB","HAC","HAD","HAF","HAG","HAI","HAL","HAM","HAN","HAP","HAS","HAT","HAV","HAY","HAZ","HBB","HBC","HBD","HBF","HBN","HBP","HBY","HCB","HCH","HCN","HCR","HCT","HDB","HDE","HDF","HDG","HDH","HDL","HDM","HDN","HDW","HDY","HEB","HEC","HED","HEF","HEI","HEL","HEN","HER","HES","HEV","HEW","HEX","HEZ","HFD","HFE","HFN","HFS","HFX","HGD","HGF","HGG","HGI","HGM","HGN","HGR","HGS","HGT","HGY","HHB","HHD","HHE","HHL","HHY","HHZ","HIA","HIB","HID","HIG","HII","HIL","HIN","HIP","HIR","HIT","HKC","HKH","HKM","HKN","HKW","HLB","HLC","HLD","HLE","HLF","HLG","HLI","HLL","HLM","HLN","HLR","HLS","HLU","HLW","HLY","HMC","HMD","HME","HMK","HML","HMM","HMN","HMP","HMS","HMT","HMW","HMY","HNA","HNB","HNC","HND","HNF","HNG","HNH","HNK","HNL","HNT","HNW","HNX","HNY","HOC","HOD","HOH","HOK","HOL","HON","HOO","HOP","HOR","HOT","HOU","HOV","HOW","HOX","HOY","HOZ","HPA","HPD","HPE","HPK","HPL","HPN","HPQ","HPT","HRD","HRH","HRL","HRM","HRN","HRO","HRR","HRS","HRW","HRY","HSB","HSC","HSD","HSE","HSG","HSK","HSL","HST","HSW","HSY","HTC","HTE","HTF","HTH","HTM","HTN","HTO","HTR","HTW","HTY","HUB","HUD","HUL","HUN","HUP","HUR","HUS","HUT","HUU","HUY","HVF","HVH","HVN","HWA","HWB","HWC","HWD","HWE","HWF","HWH","HWI","HWK","HWM","HWN","HWO","HWT","HWU","HWV","HWW","HWX","HWY","HXM","HXX","HYB","HYC","HYD","HYH","HYK","HYL","HYM","HYN","HYR","HYS","HYT","HYW","IBM","IFD","IFI","IGD","ILK","ILM","ILN","IMP","IMW","INC","INE","ING","INH","INK","INP","INR","INS","INT","INV","IPS","IRL","IRV","ISL","ISP","IVR","IVY","JCH","JEQ","JHN","JOH","JOR","JSY","KBC","KBF","KBK","KBM","KBN","KBW","KBX","KBZ","KCG","KCK","KDB","KDG","KDR","KDY","KEB","KEH","KEI","KEL","KEM","KEN","KES","KET","KEY","KEZ","KGE","KGH","KGL","KGM","KGN","KGP","KGS","KGT","KGX","KID","KIL","KIN","KIR","KIT","KIV","KKB","KKD","KKH","KKM","KKN","KKS","KLB","KLD","KLF","KLL","KLM","KLN","KLY","KMH","KMK","KML","KMP","KMS","KNA","KND","KNE","KNF","KNG","KNI","KNL","KNN","KNO","KNR","KNS","KNT","KNU","KNW","KNY","KOL","KPA","KPT","KRK","KSL","KSN","KSW","KTH","KTL","KTN","KTW","KVD","KVP","KWB","KWD","KWG","KWK","KWL","KWN","KWR","KYK","KYL","KYN","LAB","LAC","LAD","LAG","LAI","LAK","LAM","LAN","LAP","LAR","LAS","LAU","LAW","LAY","LBG","LBK","LBN","LBO","LBR","LBS","LBT","LBZ","LCB","LCC","LCG","LCH","LCK","LCL","LCN","LCS","LDN","LDR","LDS","LDW","LDY","LEA","LEB","LED","LEE","LEG","LEH","LEI","LEL","LEM","LEN","LEO","LER","LES","LET","LEU","LEW","LEY","LFD","LFL","LFO","LGB","LGD","LGE","LGF","LGG","LGJ","LGK","LGM","LGN","LGO","LGS","LGW","LHA","LHD","LHE","LHL","LHM","LHO","LHR","LHS","LHW","LIC","LID","LIF","LIH","LIL","LIN","LIP","LIS","LIT","LIU","LIV","LJL","LJN","LKE","LLA","LLB","LLC","LLD","LLE","LLF","LLG","LLH","LLI","LLJ","LLK","LLL","LLM","LLN","LLO","LLR","LLS","LLT","LLV","LLW","LLY","LMH","LMR","LMS","LNB","LND","LNE","LNF","LNG","LNK","LNR","LNW","LNY","LNZ","LOB","LOC","LOE","LOF","LOH","LOO","LOS","LOT","LOW","LOY","LPG","LPO","LPR","LPT","LPW","LPY","LRB","LRD","LRG","LRH","LRK","LRR","LSK","LSM","LSN","LSQ","LST","LSW","LSY","LTG","LTH","LTI","LTK","LTL","LTM","LTN","LTP","LTR","LTS","LTT","LTV","LUA","LUB","LUD","LUT","LUX","LVC","LVG","LVJ","LVL","LVM","LVN","LVS","LVT","LWH","LWM","LWR","LWS","LWT","LWY","LYC","LYD","LYE","LYM","LYP","LYS","LYT","LZB","LZZ","MAC","MAE","MAG","MAH","MAI","MAJ","MAL","MAN","MAO","MAR","MAS","MAT","MAU","MAW","MAX","MAY","MBH","MBK","MBR","MCB","MCE","MCF","MCH","MCK","MCM","MCN","MCO","MCT","MCV","MCZ","MDB","MDE","MDG","MDL","MDM","MDN","MDQ","MDR","MDS","MDW","MDY","MEC","MEL","MEN","MEO","MEP","MER","MES","MET","MEV","MEW","MEX","MEY","MFA","MFF","MFH","MFL","MFT","MGM","MGN","MHD","MHM","MHR","MHS","MIA","MIC","MIE","MIF","MIH","MIJ","MIK","MIL","MIM","MIN","MIR","MIS","MIT","MKC","MKM","MKR","MKT","MLB","MLD","MLF","MLG","MLH","MLM","MLN","MLP","MLR","MLS","MLT","MLV","MLW","MLY","MMO","MNA","MNC","MNE","MNG","MNN","MNP","MNR","MNZ","MOB","MOG","MOM","MON","MOO","MOR","MOS","MOT","MOY","MPK","MPL","MPT","MRB","MRD","MRF","MRM","MRN","MRP","MRR","MRS","MRT","MRY","MSC","MSD","MSE","MSH","MSK","MSL","MSM","MSN","MSO","MSR","MSS","MST","MSW","MTA","MTB","MTC","MTE","MTG","MTH","MTL","MTM","MTN","MTO","MTP","MTS","MTV","MUB","MUF","MUI","MUK","MUL","MVL","MXZ","MYB","MYH","MYL","MYM","MYT","MZH","MZM","MZZ","NAN","NAR","NAY","NBA","NBC","NBE","NBG","NBM","NBN","NBR","NBS","NBT","NBW","NBY","NCE","NCK","NCL","NCM","NCO","NCT","NCX","NCZ","NDL","NEG","NEH","NEI","NEL","NEM","NEN","NES","NET","NEW","NEY","NFA","NFD","NFL","NFN","NGR","NGT","NHD","NHE","NHL","NHY","NIM","NIT","NLN","NLR","NLS","NLT","NLW","NMC","NMK","NMM","NMN","NMP","NMR","NMT","NNE","NNG","NNN","NNP","NNT","NOA","NOR","NOT","NOY","NPD","NPP","NPT","NQC","NQU","NQY","NRB","NRC","NRD","NRN","NRT","NRW","NSB","NSD","NSG","NSH","NTA","NTB","NTC","NTH","NTL","NTN","NTR","NUF","NUM","NUN","NUT","NVH","NVM","NVN","NVR","NWA","NWB","NWD","NWE","NWI","NWM","NWN","NWP","NWR","NWT","NWX","NWY","NXG","NXZ","NYN","OBN","OCK","OCM","OHL","OKE","OKL","OKM","OKN","OKS","OLD","OLF","OLM","OLT","OLW","OLY","OMS","OOS","OPK","ORE","ORN","ORP","ORR","OSM","OTF","OTL","OTP","OTR","OUD","OUN","OUS","OUT","OVE","OVR","OXF","OXN","OXP","OXS","OXT","PAD","PAI","PAL","PAN","PAR","PAT","PAW","PAZ","PBL","PBN","PBO","PBR","PBS","PBU","PBY","PCD","PCF","PCM","PCN","PDG","PDK","PDT","PDW","PEA","PEB","PEE","PEG","PEM","PEN","PER","PES","PET","PEV","PEW","PFL","PFM","PFR","PFT","PFY","PGF","PGM","PGN","PHG","PHM","PHR","PIL","PIN","PIT","PIZ","PKG","PKS","PKT","PLC","PLD","PLE","PLG","PLK","PLM","PLN","PLS","PLT","PLU","PLW","PLY","PMA","PMB","PMD","PMG","PMH","PMO","PMP","PMR","PMS","PMT","PMW","PNA","PNC","PNE","PNF","PNL","PNM","PNN","PNQ","PNR","PNS","PNW","PNY","PNZ","POI","POK","POL","POM","PON","POO","POP","POR","POT","PPD","PPK","PPL","PPR","PRA","PRB","PRE","PRF","PRH","PRK","PRL","PRM","PRN","PRO","PRP","PRR","PRS","PRT","PRU","PRW","PRY","PSC","PSE","PSH","PSL","PSN","PST","PSW","PTA","PTB","PTC","PTD","PTF","PTG","PTH","PTK","PTL","PTM","PTN","PTO","PTR","PTS","PTT","PTW","PUL","PUO","PUR","PUT","PWC","PWE","PWL","PWN","PWW","PWY","PYC","PYE","PYG","PYJ","PYL","PYN","PYP","PYT","QBR","QPK","QPW","QRB","QRD","QRP","QUI","QYD","RAD","RAI","RAM","RAN","RAU","RAV","RAY","RBR","RBS","RBU","RCA","RCC","RCD","RCE","RCF","RCM","RCR","RDA","RDB","RDC","RDD","RDF","RDG","RDH","RDL","RDM","RDN","RDR","RDS","RDT","RDU","RDW","RDZ","REB","REC","RED","REE","REG","REI","RET","RFD","RFY","RGL","RGP","RGT","RGW","RHA","RHD","RHF","RHG","RHI","RHL","RHM","RHO","RHU","RHW","RHY","RIA","RIC","RID","RIL","RIS","RKT","RLG","RLN","RLZ","RMB","RMC","RMD","RMF","RMI","RMK","RML","RMR","RMZ","RNF","RNH","RNM","RNR","ROB","ROC","ROE","ROG","ROL","ROM","ROO","ROR","ROS","ROT","ROW","RRB","RRD","RRM","RSB","RSG","RSH","RSS","RTC","RTH","RTM","RTN","RTR","RTY","RUA","RUE","RUF","RUG","RUN","RUS","RUT","RVB","RVN","RWC","RYB","RYD","RYE","RYH","RYK","RYN","RYP","RYR","RYS","SAA","SAB","SAC","SAD","SAE","SAF","SAG","SAH","SAJ","SAL","SAM","SAN","SAO","SAQ","SAR","SAS","SAT","SAU","SAV","SAW","SAX","SAY","SBE","SBF","SBJ","SBK","SBM","SBP","SBR","SBS","SBT","SBU","SBV","SBY","SCA","SCB","SCE","SCF","SCG","SCH","SCM","SCN","SCQ","SCR","SCS","SCT","SCU","SCY","SDA","SDB","SDC","SDD","SDE","SDF","SDG","SDH","SDI","SDK","SDL","SDM","SDN","SDP","SDR","SDT","SDW","SDY","SEA","SEB","SEC","SED","SEE","SEF","SEG","SEH","SEK","SEL","SEM","SEN","SER","SES","SET","SEV","SEZ","SFA","SFC","SFD","SFF","SFI","SFL","SFN","SFO","SFR","SFS","SGB","SGE","SGH","SGL","SGM","SGN","SGQ","SGR","SHA","SHB","SHC","SHD","SHE","SHF","SHG","SHH","SHI","SHJ","SHL","SHM","SHN","SHO","SHP","SHR","SHS","SHT","SHU","SHV","SHW","SHY","SHZ","SIA","SIC","SID","SIE","SIH","SIL","SIN","SIP","SIR","SIT","SIV","SJN","SJP","SJS","SKE","SKG","SKI","SKK","SKM","SKN","SKR","SKS","SKV","SKW","SLA","SLB","SLD","SLE","SLH","SLI","SLK","SLL","SLO","SLQ","SLR","SLS","SLT","SLV","SLW","SLY","SLZ","SMA","SMB","SMC","SMD","SMG","SMH","SMI","SMK","SML","SMM","SMN","SMO","SMP","SMQ","SMR","SMT","SMW","SMY","SNA","SND","SNE","SNF","SNG","SNH","SNI","SNK","SNL","SNN","SNO","SNP","SNR","SNS","SNT","SNW","SNY","SOA","SOB","SOC","SOE","SOF","SOG","SOH","SOI","SOK","SOL","SOM","SON","SOO","SOP","SOR","SOS","SOT","SOU","SOV","SOW","SOY","SOZ","SPA","SPB","SPC","SPE","SPF","SPH","SPI","SPK","SPL","SPM","SPN","SPO","SPP","SPR","SPS","SPT","SPU","SPW","SPX","SPY","SQE","SQH","SQU","SRA","SRB","SRC","SRD","SRE","SRF","SRG","SRH","SRI","SRL","SRN","SRO","SRR","SRS","SRT","SRU","SRW","SRY","SSC","SSD","SSE","SSF","SSM","SSS","SST","STA","STB","STC","STD","STE","STF","STG","STH","STI","STJ","STK","STL","STM","STN","STO","STP","STQ","STR","STS","STT","STU","STV","STW","STY","STZ","SUC","SUD","SUG","SUM","SUN","SUO","SUP","SUR","SUT","SUU","SUW","SUY","SVB","SVG","SVK","SVL","SVR","SVS","SWA","SWB","SWC","SWD","SWE","SWF","SWG","SWH","SWI","SWJ","SWK","SWL","SWM","SWN","SWO","SWP","SWR","SWS","SWT","SWX","SWY","SXB","SXY","SYA","SYB","SYD","SYH","SYL","SYS","SYT","SZZ","TAB","TAC","TAD","TAF","TAG","TAH","TAI","TAL","TAM","TAP","TAT","TAU","TAY","TBD","TBM","TBR","TBT","TBW","TBY","TDU","TEA","TED","TEE","TEM","TEN","TEO","TEY","TFC","TGM","TGS","THA","THB","THC","THD","THE","THH","THI","THL","THM","THO","THS","THT","THU","THW","TIB","TIL","TIM","TIP","TIR","TIS","TLB","TLC","TLH","TLK","TLS","TMC","TMF","TNA","TNF","TNH","TNN","TNP","TNS","TNW","TOB","TOD","TOK","TOL","TOM","TON","TOO","TOP","TOT","TPB","TPC","TPN","TPY","TQY","TRA","TRB","TRD","TRE","TRF","TRH","TRI","TRL","TRM","TRN","TRO","TRR","TRS","TRU","TRY","TTA","TTF","TTH","TTN","TTY","TUH","TUL","TUM","TUR","TUS","TUT","TVA","TVP","TWB","TWI","TWN","TWW","TWY","TYB","TYC","TYG","TYL","TYN","TYP","TYR","TYS","TYW","TZZ","UCK","UDD","UHA","UHL","UIG","ULC","ULL","ULP","ULV","UMB","UNI","UNV","UPH","UPL","UPM","UPT","UPW","URM","UTT","UTY","UWL","VAL","VIC","VIR","VPM","VTN","VXH","WAC","WAD","WAE","WAF","WAL","WAM","WAN","WAO","WAR","WAS","WAT","WAV","WBC","WBD","WBE","WBG","WBL","WBO","WBP","WBQ","WBR","WBY","WCB","WCF","WCH","WCK","WCL","WCM","WCP","WCR","WCT","WCX","WCY","WDA","WDB","WDD","WDE","WDH","WDI","WDL","WDM","WDN","WDO","WDR","WDS","WDT","WDU","WDY","WEA","WEB","WED","WEE","WEG","WEH","WEL","WEM","WEN","WEO","WER","WES","WET","WEY","WFD","WFF","WFH","WFI","WFJ","WFL","WFN","WFS","WFW","WGA","WGC","WGN","WGR","WGT","WGV","WGW","WHA","WHC","WHD","WHE","WHG","WHH","WHI","WHK","WHL","WHM","WHN","WHP","WHR","WHS","WHT","WHY","WIC","WID","WIH","WIJ","WIL","WIM","WIN","WIR","WIS","WIT","WIU","WIV","WJH","WJL","WKB","WKD","WKF","WKG","WKI","WKK","WKL","WKM","WLA","WLC","WLD","WLE","WLF","WLG","WLH","WLI","WLL","WLM","WLN","WLO","WLP","WLS","WLT","WLV","WLW","WLY","WMA","WMB","WMC","WMD","WME","WMG","WMI","WML","WMM","WMN","WMP","WMR","WMS","WMT","WMW","WNC","WND","WNE","WNF","WNG","WNH","WNI","WNL","WNM","WNN","WNP","WNR","WNS","WNT","WNW","WNY","WOB","WOD","WOF","WOH","WOK","WOL","WOM","WON","WOO","WOR","WOS","WOX","WOY","WPE","WPK","WPL","WPM","WPT","WRB","WRE","WRH","WRK","WRL","WRM","WRN","WRP","WRS","WRT","WRU","WRW","WRX","WRY","WSA","WSB","WSE","WSF","WSG","WSH","WSL","WSM","WSR","WST","WSU","WSW","WTA","WTB","WTC","WTE","WTF","WTG","WTH","WTI","WTL","WTM","WTN","WTO","WTP","WTR","WTS","WTT","WTW","WTY","WTZ","WVF","WVH","WVP","WWA","WWD","WWI","WWL","WWM","WWO","WWR","WWW","WXC","WXF","WYB","WYE","WYL","WYM","WYQ","WYT","XAA","XAB","XAC","XAD","XAE","XAF","XAG","XAH","XAI","XAJ","XAK","XAL","XAM","XAN","XAO","XAP","XAQ","XAR","XAS","XAT","XAU","XAV","XAW","XAX","XAY","XAZ","XBA","XBB","XBC","XBD","XBE","XBF","XBG","XBH","XBI","XBJ","XBK","XBL","XBM","XBN","XBO","XBP","XBQ","XBR","XBS","XBT","XBU","XBV","XBW","XBX","XBY","XBZ","XCA","XCB","XCC","XCD","XCE","XCF","XCG","XCH","XCI","XCJ","XCK","XCL","XCM","XCN","XCO","XCP","XCQ","XCR","XCS","XCT","XCU","XCV","XCW","XCX","XCY","XCZ","XDA","XDB","XDC","XDE","XDF","XDG","XDH","XDI","XDJ","XDK","XDL","XDM","XDN","XDO","XDP","XDQ","XDR","XDS","XDT","XDU","XDV","XDW","XDX","XDY","XEA","XEB","XEC","XED","XEE","XEF","XEG","XEH","XEI","XEJ","XEK","XEL","XEM","XEN","XEO","XEP","XEQ","XES","XET","XEU","XEV","XEW","XEX","XEY","XEZ","XFA","XFB","XFC","XFD","XFE","XFF","XFG","XFH","XFJ","XFK","XFL","XFM","XFN","XFO","XFQ","XFR","XFS","XFT","XFU","XFV","XFW","XFX","XFY","XFZ","XGA","XGB","XGC","XGD","XGE","XGF","XGG","XGH","XGI","XGJ","XGK","XGL","XGM","XGN","XGO","XGP","XGR","XGS","XGT","XGU","XGV","XGW","XGX","XGZ","XHA","XHB","XHC","XHD","XHE","XHF","XHG","XHH","XHI","XHJ","XHK","XHL","XHM","XHN","XHO","XHP","XHQ","XHR","XHS","XHT","XHU","XHV","XHW","XHX","XHY","XHZ","XIA","XIB","XIC","XID","XIE","XIF","XIL","XIM","XIP","XIQ","XIR","XIT","XIV","XIW","XJB","XJC","XJD","XJF","XJN","XJR","XJS","XJV","XKB","XKC","XKE","XKG","XKI","XKK","XKL","XKM","XKS","XKW","XKY","XLA","XLB","XLC","XLD","XLE","XLF","XLG","XLH","XLI","XLJ","XLK","XLL","XLM","XLO","XLP","XLQ","XLR","XLS","XLT","XLU","XLV","XLW","XLX","XLY","XLZ","XMA","XMB","XMC","XMD","XME","XMF","XMG","XMH","XMI","XMJ","XMK","XML","XMM","XMN","XMO","XMP","XMR","XMS","XMU","XMV","XMW","XMX","XNA","XNC","XND","XNE","XNF","XNJ","XNK","XNL","XNN","XNP","XNS","XNY","XOA","XOB","XOD","XOE","XOH","XOI","XOK","XOL","XOM","XON","XOO","XOP","XOR","XOS","XOT","XOU","XOW","XOX","XOY","XOZ","XPA","XPB","XPC","XPD","XPE","XPF","XPG","XPH","XPI","XPJ","XPK","XPM","XPN","XPO","XPQ","XPS","XPT","XPU","XPV","XPW","XPX","XPY","XPZ","XQC","XQS","XQW","XQY","XRA","XRD","XRE","XRF","XRH","XRJ","XRK","XRL","XRM","XRN","XRO","XRT","XSA","XSB","XSD","XSE","XSF","XSG","XSH","XSI","XSJ","XSK","XSL","XSM","XSN","XSO","XSP","XSQ","XSR","XSS","XSU","XSV","XSX","XSY","XSZ","XTA","XTB","XTC","XTE","XTG","XTH","XTJ","XTL","XTM","XTN","XTO","XTP","XTR","XTS","XTT","XTV","XTW","XTX","XUK","XUM","XUN","XUP","XVC","XVJ","XVR","XVS","XVT","XWA","XWB","XWD","XWE","XWF","XWG","XWH","XWI","XWJ","XWK","XWM","XWO","XWP","XWQ","XWR","XWS","XWT","XWU","XWV","XWW","XWX","XWY","XWZ","XXA","XXB","XXC","XXD","XXE","XXF","XXG","XXH","XXI","XXJ","XXK","XXL","XXM","XXN","XXO","XXP","XXQ","XXR","XXS","XXT","XXU","XXV","XXW","XXX","XXY","XXZ","XYA","XYB","XYC","XYD","XYE","XYJ","XYK","XYM","XYR","XYS","XYT","XYW","XYX","YAE","YAL","YAT","YEO","YET","YMH","YNW","YOK","YRD","YRK","YRM","YRT","YSM","YSR","YVB","YVJ","YVP","ZAA","ZAC","ZAD","ZAE","ZAF","ZAG","ZAH","ZAI","ZAJ","ZAL","ZAM","ZAN","ZAO","ZAP","ZAR","ZAS","ZAT","ZAW","ZBA","ZBB","ZBC","ZBD","ZBE","ZBF","ZBG","ZBH","ZBI","ZBJ","ZBK","ZBL","ZBM","ZBN","ZBO","ZBP","ZBQ","ZBR","ZBS","ZBT","ZBU","ZBV","ZBW","ZBX","ZBY","ZBZ","ZCA","ZCB","ZCC","ZCD","ZCE","ZCF","ZCG","ZCH","ZCI","ZCJ","ZCK","ZCL","ZCM","ZCN","ZCO","ZCP","ZCQ","ZCR","ZCS","ZCT","ZCU","ZCV","ZCW","ZCX","ZCY","ZDA","ZDB","ZDC","ZDD","ZDE","ZDH","ZDL","ZDO","ZDR","ZDW","ZDX","ZDZ","ZEA","ZEB","ZEC","ZED","ZEE","ZEF","ZEG","ZEH","ZEI","ZEK","ZEL","ZEM","ZEO","ZEP","ZER","ZES","ZET","ZEU","ZEV","ZFA","ZFB","ZFC","ZFD","ZFP","ZFR","ZFW","ZFZ","ZGA","ZGC","ZGE","ZGF","ZGG","ZGH","ZGN","ZGP","ZGR","ZGS","ZGW","ZHA","ZHB","ZHC","ZHD","ZHE","ZHF","ZHG","ZHH","ZHI","ZHJ","ZHL","ZHM","ZHN","ZHO","ZHP","ZHQ","ZHR","ZHS","ZHT","ZHU","ZHV","ZHW","ZHX","ZHY","ZHZ","ZIA","ZIB","ZIC","ZID","ZIE","ZIF","ZIG","ZIH","ZII","ZIJ","ZIK","ZIL","ZIM","ZIN","ZIO","ZIP","ZIQ","ZIR","ZIS","ZIT","ZIU","ZIV","ZIW","ZIX","ZIY","ZIZ","ZJA","ZJB","ZKB","ZKE","ZKG","ZKI","ZKN","ZKP","ZKT","ZKX","ZKY","ZLA","ZLB","ZLE","ZLG","ZLH","ZLN","ZLO","ZLP","ZLQ","ZLR","ZLS","ZLV","ZLW","ZLY","ZMA","ZMC","ZME","ZMG","ZMH","ZML","ZMM","ZMO","ZMP","ZMR","ZMU","ZMV","ZMY","ZNA","ZND","ZNE","ZNF","ZNG","ZNH","ZNK","ZNM","ZNN","ZNO","ZNP","ZNS","ZNW","ZOA","ZOC","ZON","ZOS","ZOV","ZOY","ZPA","ZPB","ZPC","ZPD","ZPE","ZPG","ZPI","ZPK","ZPL","ZPM","ZPO","ZPR","ZPS","ZPU","ZQB","ZQC","ZQS","ZQW","ZRA","ZRB","ZRC","ZRE","ZRG","ZRH","ZRL","ZRM","ZRO","ZRP","ZRS","ZRU","ZRV","ZRY","ZSA","ZSB","ZSC","ZSD","ZSE","ZSF","ZSG","ZSH","ZSI","ZSJ","ZSK","ZSL","ZSM","ZSN","ZSO","ZSP","ZSQ","ZSR","ZSS","ZST","ZSU","ZSV","ZSX","ZSY","ZSZ","ZTA","ZTB","ZTC","ZTG","ZTH","ZTL","ZTM","ZTN","ZTO","ZTP","ZTR","ZTT","ZTU","ZTW","ZTY","ZUB","ZUM","ZUP","ZUX","ZUY","ZVA","ZVI","ZVR","ZWA","ZWB","ZWC","ZWD","ZWE","ZWF","ZWG","ZWH","ZWI","ZWK","ZWL","ZWM","ZWN","ZWO","ZWP","ZWQ","ZWR","ZWS","ZWT","ZWU","ZWV","ZWW","ZWX","ZWY","ZWZ","ZXA","ZXB","ZXC","ZXD","ZXE","ZXF","ZXG","ZXH","ZXI","ZXJ","ZXK","ZXL","ZXM","ZXN","ZXO","ZXP","ZXQ","ZXR","ZXS","ZXT","ZXU","ZXV","ZXW","ZXX","ZXY","ZXZ","ZYA","ZYB","ZYC","ZYD","ZZA","ZZB","ZZC","ZZD","ZZE","ZZF","ZZG","ZZH","ZZI","ZZJ","ZZK","ZZL","ZZM","ZZN","ZZO","ZZP","ZZQ","ZZR","ZZS","ZZT","ZZU","ZZV","ZZW","ZZX","ZZY","ZZZ"]
#test list
#CRSCODES = ["CDS"]

filename = 'crscodes.csv'

if os.path.exists(filename):
    os.remove(filename)

f = open(filename,'w')
f.write('CRS,lat,lon,stationname,postcode,operator,address\n') #file header

#for each crs code
for crscode in CRSCODES:
    try:
        url = "http://www.nationalrail.co.uk/stations/" + crscode + "/details.html" #build url to get station details
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        soup = BeautifulSoup(the_page, "html.parser")

        #get address and station name
        addresses = soup.find_all('address')
        header = soup.find_all('h1')
        managedby = soup.findAll("p", { "class" : "managed-by" })

        #format operator
        operator = str(managedby[0].contents[1].contents[0])

        #format address
        address = str(addresses[0]).replace("<br/>",",")
        address = address.replace("<address>","")
        address = address.replace("</address>","")
        address = address.replace("<strong>","")
        address = address.replace("</strong>","")
        address = address.replace("\r\n","")
        address = address.replace("\n","")
        address = address.replace("                           ","")
        address = address.replace("                          ","")

        #format postcode
        list = address.split(', ');
        postcode = list[len(list)-1]

        #format station name
        stationname = str(header[0].contents[0])
        stationname = stationname[:-2]

    except:
        #error calling url. Continue to next crs code
        print 'Networkrail ERROR:' + crscode
        continue

    try:
        #geocode postcode. Try arcgis and then mapquest if arcgis fails.
        g = geocoder.arcgis(postcode)
        if not g.lat:
            g = geocoder.mapquest(postcode, key='PXstG2wqhxmTuWThW0lC6RhDWJ89DHTe')

        line = '"' + crscode +'", "'+ str(g.lat) +'", "'+ str(g.lng) +'", "'+stationname +'", "'\
               + postcode +'", "' + operator + '", "'+ address +'"'
        print line
        f.write(line+'\n')  # python will convert \n to os.linesep
    except:
        print 'geocoding ERROR:' + crscode
    continue

f.close()
