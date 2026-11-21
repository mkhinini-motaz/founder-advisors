# Tunisia: devices, networks, payments APIs and hosting

General information, not legal, tax or financial advice. Check the official text and a licensed professional before relying on it.

**As of 30 Sept 2026.** For the designer, the software architect and the data analyst. Items marked **(verify)** come from one secondary source. Legal constraints on data are in `tunisia-business-law.md` (INPDP) and are not repeated here.

## Devices and screens

- **Mobile OS:** Android **84.7%**, iOS 15.3% (March 2026). Tablets: Android 70%, iOS 29%. [1]
- **Vendors:** Samsung 26.7%, Apple 16.4%, Xiaomi 12.5%, Google 8.2%, then a long tail (May 2026). [2] Design and test for mid- and low-end Android first: a small screen (360 dp wide), modest RAM, an older Android version, and a system font size turned up.
- **All devices:** Windows 62.8%, Android 25.0%, iOS 4.5% of page views (Feb 2026). [3] Computers still matter for staff and back-office screens. Customers are on phones.

## Networks

- 4G covers over 91% for all three operators (Ooredoo, Orange, Tunisie Telecom). 5G launched commercially in **February 2025** and covered about 35% of the population by May 2026, but only about **18% of subscribers had an active 5G plan**. [4][5]
- Median speeds fell as usage grew: all users 31.7 Mbps, 4G alone 21.6 Mbps. [4] Treat the field as **4G with gaps**. Riders and couriers work on the move, in stairwells and on the edge of town.
- **Design for weak networks:** optimistic UI with a retry queue for field actions, small payloads, cached last-known state, and the phone call as the fallback wherever a live connection matters.

## Language and script

- Three scripts on one screen: Arabic (right-to-left), French and English (left-to-right). Numbers are **Latin digits in every language**. Tunisians write Latin digits with Arabic letters.
- In Arabic, mirror the layout (navigation, back arrows, progress direction). Do not mirror numbers, phone numbers, prices, maps, charts, media controls or brand logos.
- Arabic needs about 10–20% more line height, and it tolerates tight letter-spacing badly. Never fake bold or italic in Arabic. **(verify against the project's type scale)**
- Customer copy is often Tunisian Arabic (Arabic script or Latin letters). Interface labels stay in each locale's standard form unless the brief says otherwise.

## Payments (online)

- Cash on delivery is ~70% of e-commerce. Online payment is a minority path; design and architect for cash first. [6]
- **Konnect:** B2B-oriented API with ready-made modules; about **1.3%** on local cards and e-Dinar, about **2.9%** on international cards. [6]
- **Flouci:** simple web API; **1.5–2%**, payout in 24–48 h. [6]
- **ClicToPay** (SMT): the historic bank gateway, oriented to larger companies. **D17** (La Poste) and e-Dinar are wallets. [6]
- Recurring card billing is hard: Glovo's subscription (Prime) was still "planned" in November 2025 because recurring card payments needed work with the card network (SMT) and the central bank. [10] See `tunisia-market.md`.

## Hosting inside Tunisia

- Hosting abroad is a personal-data transfer needing INPDP authorisation (see `tunisia-business-law.md`). **Hosting inside Tunisia avoids the transfer filing for the hosting itself**, though foreign push, maps and SMS services still count. [7]
- Local providers: **TT Cloud** (Tunisie Télécom: VPS, virtual private cloud, backup, storage), Ooredoo Business Cloud, Orange/Topnet cloud, EO Data Center, SmartCloud Tunisia and others. [7][8][9] Compare them on managed databases, backups, SLA, the support language, and price in TND against a foreign cloud plus the filing. **(get quotes)**
- A foreign cloud is not illegal. It needs the written authorisation before real personal data goes there.

## Maps, SMS and push

- OpenStreetMap coverage of small towns is thin. Addresses are often descriptive ("behind the mosque"), so store the pin and a free-text landmark, not only a street address.
- SMS goes through operator APIs (for example Orange's API) or local aggregators. Push goes through Firebase (a foreign recipient). **(verify prices per SMS)**

## Sources

1. StatCounter, mobile OS Tunisia: https://gs.statcounter.com/os-market-share/mobile/tunisia
2. StatCounter, mobile vendors Tunisia: https://gs.statcounter.com/vendor-market-share/mobile/tunisia/mobile-tablet
3. StatCounter, all OS Tunisia: https://gs.statcounter.com/os-market-share/all/tunisia
4. THD.tn, 5G one year on (Ookla data): https://www.thd.tn/5g-en-tunisie-20-de-debit-median-en-moins-pour-lensemble-des-utilisateurs-la-4g-seule-recule-de-28/
5. Espace Manager, 5G coverage by operator: https://espacemanager.com/couverture-5g-tunisie-ooredoo-orange-tunisie-telecom/
6. Online payment in Tunisia 2026 (comparison): https://web6.tn/blog/paiement-en-ligne-tunisie-comparatif/ and https://mallatech.tn/en/blog/paiement-en-ligne-tunisie
7. Sovereign cloud in Tunisia 2026: https://web6.tn/blog/cloud-souverain-tunisie-entreprise/
8. TT Cloud: https://www.tuniscope.com/article/71874/tech/telephone/tt-cloud-290117
9. EO Data Center: https://www.eodatacenter.com/
10. Managers.tn, 6 Nov 2025, Glovo Tunisia's director general: https://managers.tn/2025/11/06/adrian-mayans-directeur-general-de-glovo-tunisie-dun-simple-service-de-livraison-a-un-acteur-cle-du-e-commerce/
