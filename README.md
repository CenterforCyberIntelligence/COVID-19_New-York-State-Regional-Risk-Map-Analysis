# New York State COVID-19 Analytics
### Regional Risk Mapping

This script aims to aid in providing an insight into each county's condition in New York as it pertains to the severity of the COVID-19 pandemic. Data analysis is divided by [Regional Councils](https://regionalcouncils.ny.gov/). Planners use these figures to quickly visualize the regions that are likely most at risk of local medical infrastructure becoming overwhelmed. This information is then used to make operational decisions.

Using publicly available information and insights gained from the New York State Department of Health, the generated figures reveal the current 14-day trend in COVID-19 cases (based on a seven-day rolling average) and provides insight into the potential for local medical infrastructure to be overwhelmed based on assessed ICU bed usage.

<br>

**ICU Capacity Calculations**

An important metric for determining if regions can "reopen" is whether hospitals can handle an increased load of new COVID-19 cases without having to resort to crisis standards of care. 

Although we would ideally be able to calculate actual real-time ICU load for every facility however we do not have access to all of this data. We are utilizing information provided by COVID Act Now to assist in understanding ICU usage.

> **What is ICU Headroom Usage?** For each county in New York, we know how many ICU Beds are available. Based on best available data, we estimate the number of beds currently occupied by non-COVID patients. Of the remaining ICU beds, we estimate the number that are needed by COVID cases, and represent this in a percentages. This number is used to assist in understanding whether there is likely enough capacity to absorb a wave of new COVID infections.

Not all New York State counties have ICU beds available, and not all counties with ICU beds report usage data. Where necessary, figures have been annotated. Where data is missing, we remove those records

Below is a basic description of how to read the figures.

* **Anything below the Yellow Line)** = 50% or less of available ICU headroom in use and less than 10 cases per 100k persons (7-day RA).
  * Any region falling into this area can likely handle a surge in cases of up to 50%.
* **Yellow Line** = between 50% and 60% ICU headroom in use and between 10 and 25 cases per 100k persons (7-day RA).
* **Orange Line** = between 60% and 70% ICU headroom in use and between 25 and 50 daily cases per 100k persons (7-day RA).
* **Red Line** = >70% ICU headroom in use and more than 50 daily cases per 100k persons (7-day RA).
  * Any region falling into this area is indicative of a significantly reduced surge capacity; these ICUs are likely highly utilized and could be overwhelmed quickly.

<br>

This project is based on data sourced from [COVID Act Now](https://www.covidactnow.org/).

We are utilizing data provided by the [COVID Act Now API](https://apidocs.covidactnow.org/).

---
This project is developed and maintained by [The Center for Cyber Intelligence](https://https://centerforcyberintelligence.org/)

**A very special thanks to Philippe Langlois for his exceptional contributions and assistance on this project. This project would not have been possible without his help.**

*This project is published under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-nc-sa/4.0/), which requires users to attribute the source and license type (CC BY-NC-SA 4.0) when sharing, remixing, transforming, or building upon this material. Our preferred attribution is The Center for Cyber Intelligence.*

<hr>

### Script Requirements
This script was developed using Python 3.9.1 - No testing has been conducted with prior or alternate versions of Python.

The following Python libraries are required for this script to run. 
* pandas
* matplotlib