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

<div class='tableauPlaceholder' id='viz1777442907980' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;YM&#47;YMYT9GZDP&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;YMYT9GZDP' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;YM&#47;YMYT9GZDP&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1777442907980');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='2077px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

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

