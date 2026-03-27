# DA_Python

End-to-end data analysis project exploring layoffs in technology companies in the context of AI adoption.  
Focus: real-world data pipeline, statistical validation, and business-oriented insights.

→ **Live Dashboard:**  
https://public.tableau.com/app/profile/lenka.hanakova/viz/PropoutntechnologickchfiremvdobAI/Dashboard1?publish=yes  

→ **Project Article (methodology & context):**  
https://medium.com/@zpevakova.vero/propou%C5%A1t%C4%9Bn%C3%AD-technologick%C3%BDch-firem-v-%C3%A9%C5%99e-ai-1d5acb3e05de  

---

## What This Project Demonstrates

This project is not just a set of notebooks. It demonstrates the ability to:

- Work with **real-world, messy datasets**
- Combine **multiple data sources (structured + text-based)**
- Design a **data processing pipeline**
- Apply **statistical thinking to business problems**
- Deliver results via a **clear, interactive dashboard**

---

## Key Capabilities

- **Data acquisition & enrichment**
  - integration of external data sources
  - text enrichment via APIs

- **Data processing**
  - cleaning, normalization, and transformation
  - handling incomplete and inconsistent data

- **Feature engineering**
  - categorization of layoff reasons
  - structuring unstructured text into analyzable formats

- **Analysis**
  - hypothesis testing
  - trend identification across companies and time

- **Visualization**
  - building a Tableau dashboard for insight communication

---

## Tech Stack

- **Python** (core analysis)
- **Jupyter Notebook** (exploration & iteration)
- **pandas, SciPy** (data processing & statistics)
- **SQL** (data validation and structuring – workflow layer)
- **Apify** (data acquisition – article context)
- **OpenAI API** (text enrichment – article context)
- **Tableau** (final dashboard)
- **Figma** (dashboard design – article context)
- **Google Maps Platform API** (geolocation enrichment – article context)

---

## Analytical Workflow

1. **Data Acquisition**
   - collecting layoff datasets
   - enriching records with external sources and articles

2. **Data Preparation**
   - cleaning and standardizing data
   - merging multiple datasets

3. **Feature Engineering**
   - extracting and categorizing layoff reasons
   - transforming text data into structured variables

4. **Analysis**
   - statistical hypothesis testing
   - identifying patterns and trends

5. **Visualization**
   - translating analysis into a Tableau dashboard
   - enabling exploration of insights

---

## Key Insight Focus

The project investigates questions such as:

- Are layoffs increasing in correlation with AI adoption?
- What are the dominant reasons companies report for layoffs?
- How do layoffs vary across industries and time periods?

→ The answers are presented in the dashboard, not hardcoded in the repository.

---

## Repository Structure

The repository reflects an exploratory analytics workflow:

- `data_layoffs.ipynb` – core dataset processing  
- `duvody_v_layooffs.ipynb` – layoff reason analysis  
- `flitr_chybejicich_clanku.ipynb` – filtering missing article data  
- `kategorizace_duvodu_propusteni_15_05.ipynb` – categorization logic  
- `tabulka_pro_testovani.ipynb` – dataset preparation for testing  
- `zaloha_data_layoffs.ipynb` – backup work  
- `pocte_url_v_datasetu_nedele.py` – helper script  
- `data layoffs/` – dataset storage  

---

## Quick Start

```bash
git clone https://github.com/VerunkaZ/DA_Python.git
cd DA_Python
pip install jupyter pandas scipy
jupyter notebook
