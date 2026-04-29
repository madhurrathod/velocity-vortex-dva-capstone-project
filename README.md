# NST DVA Capstone 2

## Project Title

Improving Bank Telemarketing Conversion Through Customer and Campaign Analytics

## Sector

Finance

## Problem Statement

A Portuguese banking institution runs direct marketing campaigns to promote term deposits. The core business problem is to identify which customer segments, contact patterns, and campaign conditions are associated with higher subscription rates so the bank can improve conversion efficiency and reduce wasted outreach effort.

## Dashboard Overview
<p align="center">
  <img src="./Demo Screenshots/Dashboard.png" width="90%"/>
</p>
Dashboard has working filters of Poutcome, Job, Age Group and Contact.

[Access Dashboard on Tableau Public](https://public.tableau.com/shared/YMYT9GZDP?:display_count=n&:origin=viz_share_link)

## Dataset

- Primary dataset: UCI Bank Marketing, `bank-additional-full.csv`
- Source: UCI Machine Learning Repository
- Records: `41,188`
- Fields: `20 input columns + 1 target column`
- Target variable: `y` indicating whether the client subscribed to a term deposit

## Backup Datasets

- Backup 1: `bank-full.csv` from the UCI Bank Marketing package
- Backup 2: `bank-additional.csv` from the UCI Bank Marketing package

## Team Structure

| Member |  Role |Ownership |
| --- | --- | --- |
| Madhur Rathod | Project Lead | repo coordination, QA, final integration,Tableau dashboard |
| Aaditya Mohan Samadhiya | Data Engineer | extraction, cleaning, processed outputs |
| Ambuj Vashistha | Analyst | EDA, hypothesis testing, KPI analysis |
| Himanshu Gulhane | Storytelling Lead | Tableau dashboard, Project Report, Presentation |

## Repository Structure

```text
data/
  raw/
  processed/
docs/
notebooks/
reports/
scripts/
tableau/
```

## Key Findings Snapshot

- Overall subscription rate is `11.27%`.
- `Cellular` contact converts at `14.74%`, versus `5.23%` for `telephone`.
- Clients with a previous successful campaign outcome convert at `65.11%`.
- Conversion drops sharply as repeated contacts increase: `13.04%` for one contact versus `3.11%` for `11+` contacts.
- Younger (`18-24`) and older (`65+`) segments respond much better than middle-age bands.

## Submission Notes

- Tableau-ready data is available in `data/processed/bank_marketing_tableau.csv`.
- Dashboard aggregation files are also saved in `data/processed/`.
- Update `tableau/dashboard_links.md` after publishing the dashboard on Tableau Public.
- The original capstone brief you shared mentions 5 members, while your team has 4. Confirm that with the mentor to avoid submission risk.


## Project Overview
| Field | Details |
| --- | --- |
| Project Title | Improving Bank Telemarketing Conversion Through Customer and Campaign Analytics |
| Sector | Finance |
| Institute | Newton School of Technology |
| Submission Date | April 28, 2026 |

