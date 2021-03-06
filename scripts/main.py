# -*- coding: utf-8 -*-
"""
This project is based on data sourced from COVID Act Now
(https://www.covidactnow.org/).

We are utilizing data provided by the COVID Act Now API
(https://apidocs.covidactnow.org/).

This notebook is developed and maintained by The Center for Cyber Intelligence
(https://https://centerforcyberintelligence.org/)

A very special thanks to Philippe Langlois for his exceptional contributions and assistance on this project. This
project would not have been possible without his help.

This project is published under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license
(https://creativecommons.org/licenses/by-nc-sa/4.0/), which requires users to attribute the source and license type
(CC BY-NC-SA 4.0) when sharing, remixing, transforming, or building upon this material. Our preferred attribution is
The Center for Cyber Intelligence.
"""

import os
from os import system, name

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import PercentFormatter

from modules import helper_functions
from modules import pptxGenerator


def create_StateOverview(cwd, historicData, todayDate):
    # Creates a County Level COVID-19 Risk Map

    try:

        plt.figure(figsize=(25, 13))

        ### Capital Region ###

        albanyCounty = historicData[historicData['county'] == "Albany County"]
        albanyCounty = albanyCounty[albanyCounty['metrics.icuHeadroomRatio'] != 0]
        albanyCounty = albanyCounty[albanyCounty['metrics.caseDensity'] != 0]
        x1 = albanyCounty['metrics.icuHeadroomRatio'].tail(1)
        y1 = albanyCounty['metrics.caseDensity'].tail(1)
        plt.plot(x1, y1, 'o', linewidth='1', label="Albany County")
        plt.annotate("Albany", xy=(x1.iloc[-1], y1.iloc[-1]))

        ColumbiaCounty = historicData[historicData['county'] == "Columbia County"]
        ColumbiaCounty = ColumbiaCounty[ColumbiaCounty['metrics.icuHeadroomRatio'] != 0]
        ColumbiaCounty = ColumbiaCounty[ColumbiaCounty['metrics.caseDensity'] != 0]
        x2 = ColumbiaCounty['metrics.icuHeadroomRatio'].tail(1)
        y2 = ColumbiaCounty['metrics.caseDensity'].tail(1)
        plt.plot(x2, y2, 'o', linewidth='1', label="Columbia County")
        plt.annotate("Columbia", xy=(x2.iloc[-1], y2.iloc[-1]))

        SaratogaCounty = historicData[historicData['county'] == "Saratoga County"]
        SaratogaCounty = SaratogaCounty[SaratogaCounty['metrics.icuHeadroomRatio'] != 0]
        SaratogaCounty = SaratogaCounty[SaratogaCounty['metrics.caseDensity'] != 0]
        x3 = SaratogaCounty['metrics.icuHeadroomRatio'].tail(1)
        y3 = SaratogaCounty['metrics.caseDensity'].tail(1)
        plt.plot(x3, y3, 'o', linewidth='1', label="Saratoga County")
        plt.annotate("Saratoga", xy=(x3.iloc[-1], y3.iloc[-1]))

        SchenectadyCounty = historicData[historicData['county'] == "Schenectady County"]
        SchenectadyCounty = SchenectadyCounty[SchenectadyCounty['metrics.icuHeadroomRatio'] != 0]
        SchenectadyCounty = SchenectadyCounty[SchenectadyCounty['metrics.caseDensity'] != 0]
        x4 = SchenectadyCounty['metrics.icuHeadroomRatio'].tail(1)
        y4 = SchenectadyCounty['metrics.caseDensity'].tail(1)
        plt.plot(x4, y4, 'o', linewidth='1', label="Schenectady County")
        plt.annotate("Schenectady", xy=(x4.iloc[-1], y4.iloc[-1]))

        RensselaerCounty = historicData[historicData['county'] == "Rensselaer County"]
        RensselaerCounty = RensselaerCounty[RensselaerCounty['metrics.icuHeadroomRatio'] != 0]
        RensselaerCounty = RensselaerCounty[RensselaerCounty['metrics.caseDensity'] != 0]
        x5 = RensselaerCounty['metrics.icuHeadroomRatio'].tail(1)
        y5 = RensselaerCounty['metrics.caseDensity'].tail(1)
        plt.plot(x5, y5, 'o', linewidth='1', label="Rensselaer County")
        plt.annotate("Rensselaer", xy=(x5.iloc[-1], y5.iloc[-1]))

        WarrenCounty = historicData[historicData['county'] == "Warren County"]
        WarrenCounty = WarrenCounty[WarrenCounty['metrics.icuHeadroomRatio'] != 0]
        WarrenCounty = WarrenCounty[WarrenCounty['metrics.caseDensity'] != 0]
        x6 = WarrenCounty['metrics.icuHeadroomRatio'].tail(1)
        y6 = WarrenCounty['metrics.caseDensity'].tail(1)
        plt.plot(x6, y6, 'o', linewidth='1', label="Warren County")
        plt.annotate("Warren", xy=(x6.iloc[-1], y6.iloc[-1]))

        ### Western New York ###

        alleganyCounty = historicData[historicData['county'] == "Allegany County"]
        alleganyCounty = alleganyCounty[alleganyCounty['metrics.icuHeadroomRatio'] != 0]
        alleganyCounty = alleganyCounty[alleganyCounty['metrics.caseDensity'] != 0]
        x7 = alleganyCounty['metrics.icuHeadroomRatio'].tail(1)
        y7 = alleganyCounty['metrics.caseDensity'].tail(1)
        plt.plot(x7, y7, 'o', linewidth='1', label="Allegany County")
        plt.annotate("Allegany", xy=(x7.iloc[-1], y7.iloc[-1]))

        chautauquaCounty = historicData[historicData['county'] == "Chautauqua County"]
        chautauquaCounty = chautauquaCounty[chautauquaCounty['metrics.icuHeadroomRatio'] != 0]
        chautauquaCounty = chautauquaCounty[chautauquaCounty['metrics.caseDensity'] != 0]
        x8 = chautauquaCounty['metrics.icuHeadroomRatio'].tail(1)
        y8 = chautauquaCounty['metrics.caseDensity'].tail(1)
        plt.plot(x8, y8, 'o', linewidth='1', label="Chautauqua County")
        plt.annotate("Chautauqua", xy=(x8.iloc[-1], y8.iloc[-1]))

        ErieCounty = historicData[historicData['county'] == "Erie County"]
        ErieCounty = ErieCounty[ErieCounty['metrics.icuHeadroomRatio'] != 0]
        ErieCounty = ErieCounty[ErieCounty['metrics.caseDensity'] != 0]
        x9 = ErieCounty['metrics.icuHeadroomRatio'].tail(1)
        y9 = ErieCounty['metrics.caseDensity'].tail(1)
        plt.plot(x9, y9, 'o', linewidth='1', label="Erie County")
        plt.annotate("Erie", xy=(x9.iloc[-1], y9.iloc[-1]))

        NiagaraCounty = historicData[historicData['county'] == "Niagara County"]
        NiagaraCounty = NiagaraCounty[NiagaraCounty['metrics.icuHeadroomRatio'] != 0]
        NiagaraCounty = NiagaraCounty[NiagaraCounty['metrics.caseDensity'] != 0]
        x10 = NiagaraCounty['metrics.icuHeadroomRatio'].tail(1)
        y10 = NiagaraCounty['metrics.caseDensity'].tail(1)
        plt.plot(x10, y10, 'o', linewidth='1', label="Niagara County")
        plt.annotate("Niagara", xy=(x10.iloc[-1], y10.iloc[-1]))

        ### Finger Lakes ###

        GeneseeCounty = historicData[historicData['county'] == "Genesee County"]
        GeneseeCounty = GeneseeCounty[GeneseeCounty['metrics.icuHeadroomRatio'] != 0]
        GeneseeCounty = GeneseeCounty[GeneseeCounty['metrics.caseDensity'] != 0]
        x11 = GeneseeCounty['metrics.icuHeadroomRatio'].tail(1)
        y11 = GeneseeCounty['metrics.caseDensity'].tail(1)
        plt.plot(x11, y11, 'o', linewidth='1', label="Genesee County")
        plt.annotate("Genesee", xy=(x11.iloc[-1], y11.iloc[-1]))

        MonroeCounty = historicData[historicData['county'] == "Monroe County"]
        MonroeCounty = MonroeCounty[MonroeCounty['metrics.icuHeadroomRatio'] != 0]
        MonroeCounty = MonroeCounty[MonroeCounty['metrics.caseDensity'] != 0]
        x12 = MonroeCounty['metrics.icuHeadroomRatio'].tail(1)
        y12 = MonroeCounty['metrics.caseDensity'].tail(1)
        plt.plot(x12, y12, 'o', linewidth='1', label="Monroe County")
        plt.annotate("Monroe", xy=(x12.iloc[-1], y12.iloc[-1]))

        OntarioCounty = historicData[historicData['county'] == "Ontario County"]
        OntarioCounty = OntarioCounty[OntarioCounty['metrics.icuHeadroomRatio'] != 0]
        OntarioCounty = OntarioCounty[OntarioCounty['metrics.caseDensity'] != 0]
        x13 = OntarioCounty['metrics.icuHeadroomRatio'].tail(1)
        y13 = OntarioCounty['metrics.caseDensity'].tail(1)
        plt.plot(x13, y13, 'o', linewidth='1', label="Ontario County")
        plt.annotate("Ontario", xy=(x13.iloc[-1], y13.iloc[-1]))

        WayneCounty = historicData[historicData['county'] == "Wayne County"]
        WayneCounty = WayneCounty[WayneCounty['metrics.icuHeadroomRatio'] != 0]
        WayneCounty = WayneCounty[WayneCounty['metrics.caseDensity'] != 0]
        x14 = WayneCounty['metrics.icuHeadroomRatio'].tail(1)
        y14 = WayneCounty['metrics.caseDensity'].tail(1)
        plt.plot(x14, y14, 'o', linewidth='1', label="Wayne County")
        plt.annotate("Wayne", xy=(x14.iloc[-1], y14.iloc[-1]))

        WyomingCounty = historicData[historicData['county'] == "Wyoming County"]
        WyomingCounty = WyomingCounty[WyomingCounty['metrics.icuHeadroomRatio'] != 0]
        WyomingCounty = WyomingCounty[WyomingCounty['metrics.caseDensity'] != 0]
        x15 = WyomingCounty['metrics.icuHeadroomRatio'].tail(1)
        y15 = WyomingCounty['metrics.caseDensity'].tail(1)
        plt.plot(x15, y15, 'o', linewidth='1', label="Wyoming County")
        plt.annotate("Wyoming", xy=(x15.iloc[-1], y15.iloc[-1]))

        ### Southern Tier ###

        BroomeCounty = historicData[historicData['county'] == "Broome County"]
        BroomeCounty = BroomeCounty[BroomeCounty['metrics.icuHeadroomRatio'] != 0]
        BroomeCounty = BroomeCounty[BroomeCounty['metrics.caseDensity'] != 0]
        x16 = BroomeCounty['metrics.icuHeadroomRatio'].tail(1)
        y16 = BroomeCounty['metrics.caseDensity'].tail(1)
        plt.plot(x16, y16, 'o', linewidth='1', label="Broome County")
        plt.annotate("Broome", xy=(x16.iloc[-1], y16.iloc[-1]))

        ChemungCounty = historicData[historicData['county'] == "Chemung County"]
        ChemungCounty = ChemungCounty[ChemungCounty['metrics.icuHeadroomRatio'] != 0]
        ChemungCounty = ChemungCounty[ChemungCounty['metrics.caseDensity'] != 0]
        x11 = ChemungCounty['metrics.icuHeadroomRatio'].tail(1)
        y11 = ChemungCounty['metrics.caseDensity'].tail(1)
        plt.plot(x11, y11, 'o', linewidth='1', label="Chemung County")
        plt.annotate("Chemung", xy=(x11.iloc[-1], y11.iloc[-1]))

        ChenangoCounty = historicData[historicData['county'] == "Chenango County"]
        ChenangoCounty = ChenangoCounty[ChenangoCounty['metrics.icuHeadroomRatio'] != 0]
        ChenangoCounty = ChenangoCounty[ChenangoCounty['metrics.caseDensity'] != 0]
        x18 = ChenangoCounty['metrics.icuHeadroomRatio'].tail(1)
        y18 = ChenangoCounty['metrics.caseDensity'].tail(1)
        plt.plot(x18, y18, 'o', linewidth='1', label="Chenango County")
        plt.annotate("Chenango", xy=(x18.iloc[-1], y18.iloc[-1]))

        SteubenCounty = historicData[historicData['county'] == "Steuben County"]
        SteubenCounty = SteubenCounty[SteubenCounty['metrics.icuHeadroomRatio'] != 0]
        SteubenCounty = SteubenCounty[SteubenCounty['metrics.caseDensity'] != 0]
        x19 = SteubenCounty['metrics.icuHeadroomRatio'].tail(1)
        y19 = SteubenCounty['metrics.caseDensity'].tail(1)
        plt.plot(x19, y19, 'o', linewidth='1', label="Steuben County")
        plt.annotate("Steuben", xy=(x19.iloc[-1], y19.iloc[-1]))

        TompkinsCounty = historicData[historicData['county'] == "Tompkins County"]
        TompkinsCounty = TompkinsCounty[TompkinsCounty['metrics.icuHeadroomRatio'] != 0]
        TompkinsCounty = TompkinsCounty[TompkinsCounty['metrics.caseDensity'] != 0]
        x20 = TompkinsCounty['metrics.icuHeadroomRatio'].tail(1)
        y20 = TompkinsCounty['metrics.caseDensity'].tail(1)
        plt.plot(x20, y20, 'o', linewidth='1', label="Tompkins County")
        plt.annotate("Tompkins", xy=(x20.iloc[-1], y20.iloc[-1]))

        ### Central New York ###

        CayugaCounty = historicData[historicData['county'] == "Cayuga County"]
        CayugaCounty = CayugaCounty[CayugaCounty['metrics.icuHeadroomRatio'] != 0]
        CayugaCounty = CayugaCounty[CayugaCounty['metrics.caseDensity'] != 0]
        x21 = CayugaCounty['metrics.icuHeadroomRatio'].tail(1)
        y21 = CayugaCounty['metrics.caseDensity'].tail(1)
        plt.plot(x21, y21, 'o', linewidth='1', label="Cayuga County")
        plt.annotate("Cayuga", xy=(x21.iloc[-1], y21.iloc[-1]))

        CortlandCounty = historicData[historicData['county'] == "Cortland County"]
        CortlandCounty = CortlandCounty[CortlandCounty['metrics.icuHeadroomRatio'] != 0]
        CortlandCounty = CortlandCounty[CortlandCounty['metrics.caseDensity'] != 0]
        x22 = CortlandCounty['metrics.icuHeadroomRatio'].tail(1)
        y22 = CortlandCounty['metrics.caseDensity'].tail(1)
        plt.plot(x22, y22, 'o', linewidth='1', label="Cortland County")
        plt.annotate("Cortland", xy=(x22.iloc[-1], y22.iloc[-1]))

        MadisonCounty = historicData[historicData['county'] == "Madison County"]
        MadisonCounty = MadisonCounty[MadisonCounty['metrics.icuHeadroomRatio'] != 0]
        MadisonCounty = MadisonCounty[MadisonCounty['metrics.caseDensity'] != 0]
        x23 = MadisonCounty['metrics.icuHeadroomRatio'].tail(1)
        y23 = MadisonCounty['metrics.caseDensity'].tail(1)
        plt.plot(x23, y23, 'o', linewidth='1', label="Madison County")
        plt.annotate("Madison", xy=(x23.iloc[-1], y23.iloc[-1]))

        OnondagaCounty = historicData[historicData['county'] == "Onondaga County"]
        OnondagaCounty = OnondagaCounty[OnondagaCounty['metrics.icuHeadroomRatio'] != 0]
        OnondagaCounty = OnondagaCounty[OnondagaCounty['metrics.caseDensity'] != 0]
        x24 = OnondagaCounty['metrics.icuHeadroomRatio'].tail(1)
        y24 = OnondagaCounty['metrics.caseDensity'].tail(1)
        plt.plot(x24, y24, 'o', linewidth='1', label="Onondaga County")
        plt.annotate("Onondaga", xy=(x24.iloc[-1], y24.iloc[-1]))

        OswegoCounty = historicData[historicData['county'] == "Oswego County"]
        OswegoCounty = OswegoCounty[OswegoCounty['metrics.icuHeadroomRatio'] != 0]
        OswegoCounty = OswegoCounty[OswegoCounty['metrics.caseDensity'] != 0]
        x25 = OswegoCounty['metrics.icuHeadroomRatio'].tail(1)
        y25 = OswegoCounty['metrics.caseDensity'].tail(1)
        plt.plot(x25, y25, 'o', linewidth='1', label="Oswego County")
        plt.annotate("Oswego", xy=(x25.iloc[-1], y25.iloc[-1]))

        ### Mohawk Valley ###

        FultonCounty = historicData[historicData['county'] == "Fulton County"]
        FultonCounty = FultonCounty[FultonCounty['metrics.icuHeadroomRatio'] != 0]
        FultonCounty = FultonCounty[FultonCounty['metrics.caseDensity'] != 0]
        x26 = FultonCounty['metrics.icuHeadroomRatio'].tail(1)
        y26 = FultonCounty['metrics.caseDensity'].tail(1)
        plt.plot(x26, y26, 'o', linewidth='1', label="Fulton County")
        plt.annotate("Fulton", xy=(x26.iloc[-1], y26.iloc[-1]))

        MontgomeryCounty = historicData[historicData['county'] == "Montgomery County"]
        MontgomeryCounty = MontgomeryCounty[MontgomeryCounty['metrics.icuHeadroomRatio'] != 0]
        MontgomeryCounty = MontgomeryCounty[MontgomeryCounty['metrics.caseDensity'] != 0]
        x21 = MontgomeryCounty['metrics.icuHeadroomRatio'].tail(1)
        y21 = MontgomeryCounty['metrics.caseDensity'].tail(1)
        plt.plot(x21, y21, 'o', linewidth='1', label="Montgomery County")
        plt.annotate("Montgomery", xy=(x21.iloc[-1], y21.iloc[-1]))

        OneidaCounty = historicData[historicData['county'] == "Oneida County"]
        OneidaCounty = OneidaCounty[OneidaCounty['metrics.icuHeadroomRatio'] != 0]
        OneidaCounty = OneidaCounty[OneidaCounty['metrics.caseDensity'] != 0]
        x28 = OneidaCounty['metrics.icuHeadroomRatio'].tail(1)
        y28 = OneidaCounty['metrics.caseDensity'].tail(1)
        plt.plot(x28, y28, 'o', linewidth='1', label="Oneida County")
        plt.annotate("Oneida", xy=(x28.iloc[-1], y28.iloc[-1]))

        OtsegoCounty = historicData[historicData['county'] == "Otsego County"]
        OtsegoCounty = OtsegoCounty[OtsegoCounty['metrics.icuHeadroomRatio'] != 0]
        OtsegoCounty = OtsegoCounty[OtsegoCounty['metrics.caseDensity'] != 0]
        x29 = OtsegoCounty['metrics.icuHeadroomRatio'].tail(1)
        y29 = OtsegoCounty['metrics.caseDensity'].tail(1)
        plt.plot(x29, y29, 'o', linewidth='1', label="Otsego County")
        plt.annotate("Otsego", xy=(x29.iloc[-1], y29.iloc[-1]))

        ### North Country ###

        ClintonCounty = historicData[historicData['county'] == "Clinton County"]
        ClintonCounty = ClintonCounty[ClintonCounty['metrics.icuHeadroomRatio'] != 0]
        ClintonCounty = ClintonCounty[ClintonCounty['metrics.caseDensity'] != 0]
        x30 = ClintonCounty['metrics.icuHeadroomRatio'].tail(1)
        y30 = ClintonCounty['metrics.caseDensity'].tail(1)
        plt.plot(x30, y30, 'o', linewidth='1', label="Clinton County")
        plt.annotate("Clinton", xy=(x30.iloc[-1], y30.iloc[-1]))

        FranklinCounty = historicData[historicData['county'] == "Franklin County"]
        FranklinCounty = FranklinCounty[FranklinCounty['metrics.icuHeadroomRatio'] != 0]
        FranklinCounty = FranklinCounty[FranklinCounty['metrics.caseDensity'] != 0]
        x31 = FranklinCounty['metrics.icuHeadroomRatio'].tail(1)
        y31 = FranklinCounty['metrics.caseDensity'].tail(1)
        plt.plot(x31, y31, 'o', linewidth='1', label="Franklin County")
        plt.annotate("Franklin", xy=(x31.iloc[-1], y31.iloc[-1]))

        JeffersonCounty = historicData[historicData['county'] == "Jefferson County"]
        JeffersonCounty = JeffersonCounty[JeffersonCounty['metrics.icuHeadroomRatio'] != 0]
        JeffersonCounty = JeffersonCounty[JeffersonCounty['metrics.caseDensity'] != 0]
        x32 = JeffersonCounty['metrics.icuHeadroomRatio'].tail(1)
        y32 = JeffersonCounty['metrics.caseDensity'].tail(1)
        plt.plot(x32, y32, 'o', linewidth='1', label="Jefferson County")
        plt.annotate("Jefferson", xy=(x32.iloc[-1], y32.iloc[-1]))

        LewisCounty = historicData[historicData['county'] == "Lewis County"]
        LewisCounty = LewisCounty[LewisCounty['metrics.icuHeadroomRatio'] != 0]
        LewisCounty = LewisCounty[LewisCounty['metrics.caseDensity'] != 0]
        x33 = LewisCounty['metrics.icuHeadroomRatio'].tail(1)
        y33 = LewisCounty['metrics.caseDensity'].tail(1)
        plt.plot(x33, y33, 'o', linewidth='1', label="Lewis County")
        plt.annotate("Lewis", xy=(x33.iloc[-1], y33.iloc[-1]))

        StLawrenceCounty = historicData[historicData['county'] == "St. Lawrence County"]
        StLawrenceCounty = StLawrenceCounty[StLawrenceCounty['metrics.icuHeadroomRatio'] != 0]
        StLawrenceCounty = StLawrenceCounty[StLawrenceCounty['metrics.caseDensity'] != 0]
        x34 = StLawrenceCounty['metrics.icuHeadroomRatio'].tail(1)
        y34 = StLawrenceCounty['metrics.caseDensity'].tail(1)
        plt.plot(x34, y34, 'o', linewidth='1', label="St. Lawrence County")
        plt.annotate("St. Lawrence", xy=(x34.iloc[-1], y34.iloc[-1]))

        ### Mid-Hudson ###

        DutchessCounty = historicData[historicData['county'] == "Dutchess County"]
        DutchessCounty = DutchessCounty[DutchessCounty['metrics.icuHeadroomRatio'] != 0]
        DutchessCounty = DutchessCounty[DutchessCounty['metrics.caseDensity'] != 0]
        x35 = DutchessCounty['metrics.icuHeadroomRatio'].tail(1)
        y35 = DutchessCounty['metrics.caseDensity'].tail(1)
        plt.plot(x35, y35, 'o', linewidth='1', label="Dutchess County")
        plt.annotate("Dutchess", xy=(x35.iloc[-1], y35.iloc[-1]))

        OrangeCounty = historicData[historicData['county'] == "Orange County"]
        OrangeCounty = OrangeCounty[OrangeCounty['metrics.icuHeadroomRatio'] != 0]
        OrangeCounty = OrangeCounty[OrangeCounty['metrics.caseDensity'] != 0]
        x36 = OrangeCounty['metrics.icuHeadroomRatio'].tail(1)
        y36 = OrangeCounty['metrics.caseDensity'].tail(1)
        plt.plot(x36, y36, 'o', linewidth='1', label="Orange County")
        plt.annotate("Orange", xy=(x36.iloc[-1], y36.iloc[-1]))

        PutnamCounty = historicData[historicData['county'] == "Putnam County"]
        PutnamCounty = PutnamCounty[PutnamCounty['metrics.icuHeadroomRatio'] != 0]
        PutnamCounty = PutnamCounty[PutnamCounty['metrics.caseDensity'] != 0]
        x37 = PutnamCounty['metrics.icuHeadroomRatio'].tail(1)
        y37 = PutnamCounty['metrics.caseDensity'].tail(1)
        plt.plot(x37, y37, 'o', linewidth='1', label="Putnam County")
        plt.annotate("Putnam", xy=(x37.iloc[-1], y37.iloc[-1]))

        RocklandCounty = historicData[historicData['county'] == "Rockland County"]
        RocklandCounty = RocklandCounty[RocklandCounty['metrics.icuHeadroomRatio'] != 0]
        RocklandCounty = RocklandCounty[RocklandCounty['metrics.caseDensity'] != 0]
        x38 = RocklandCounty['metrics.icuHeadroomRatio'].tail(1)
        y38 = RocklandCounty['metrics.caseDensity'].tail(1)
        plt.plot(x38, y38, 'o', linewidth='1', label="Rockland County")
        plt.annotate("Rockland", xy=(x38.iloc[-1], y38.iloc[-1]))

        SullivanCounty = historicData[historicData['county'] == "Sullivan County"]
        SullivanCounty = SullivanCounty[SullivanCounty['metrics.icuHeadroomRatio'] != 0]
        SullivanCounty = SullivanCounty[SullivanCounty['metrics.caseDensity'] != 0]
        x39 = SullivanCounty['metrics.icuHeadroomRatio'].tail(1)
        y39 = SullivanCounty['metrics.caseDensity'].tail(1)
        plt.plot(x39, y39, 'o', linewidth='1', label="Sullivan County")
        plt.annotate("Sullivan", xy=(x39.iloc[-1], y39.iloc[-1]))

        UlsterCounty = historicData[historicData['county'] == "Ulster County"]
        UlsterCounty = UlsterCounty[UlsterCounty['metrics.icuHeadroomRatio'] != 0]
        UlsterCounty = UlsterCounty[UlsterCounty['metrics.caseDensity'] != 0]
        x40 = UlsterCounty['metrics.icuHeadroomRatio'].tail(1)
        y40 = UlsterCounty['metrics.caseDensity'].tail(1)
        plt.plot(x40, y40, 'o', linewidth='1', label="Ulster County")
        plt.annotate("Ulster", xy=(x40.iloc[-1], y40.iloc[-1]))

        WestchesterCounty = historicData[historicData['county'] == "Westchester County"]
        WestchesterCounty = WestchesterCounty[WestchesterCounty['metrics.icuHeadroomRatio'] != 0]
        WestchesterCounty = WestchesterCounty[WestchesterCounty['metrics.caseDensity'] != 0]
        x41 = WestchesterCounty['metrics.icuHeadroomRatio'].tail(1)
        y41 = WestchesterCounty['metrics.caseDensity'].tail(1)
        plt.plot(x41, y41, 'o', linewidth='1', label="Westchester County")
        plt.annotate("Westchester", xy=(x41.iloc[-1], y41.iloc[-1]))

        ### New York City ###
        # TODO: Need to add New York City counties - Covid Act Now API should support this now.

        ### Long Island ###

        NassauCounty = historicData[historicData['county'] == "Nassau County"]
        NassauCounty = NassauCounty[NassauCounty['metrics.icuHeadroomRatio'] != 0]
        NassauCounty = NassauCounty[NassauCounty['metrics.caseDensity'] != 0]
        x42 = NassauCounty['metrics.icuHeadroomRatio'].tail(1)
        y42 = NassauCounty['metrics.caseDensity'].tail(1)
        plt.plot(x42, y42, 'o', linewidth='1', label="Nassau County")
        plt.annotate("Nassau", xy=(x42.iloc[-1], y42.iloc[-1]))

        SuffolkCounty = historicData[historicData['county'] == "Suffolk County"]
        SuffolkCounty = SuffolkCounty[SuffolkCounty['metrics.icuHeadroomRatio'] != 0]
        SuffolkCounty = SuffolkCounty[SuffolkCounty['metrics.caseDensity'] != 0]
        x43 = SuffolkCounty['metrics.icuHeadroomRatio'].tail(1)
        y43 = SuffolkCounty['metrics.caseDensity'].tail(1)
        plt.plot(x43, y43, 'o', linewidth='1', label="Suffolk County")
        plt.annotate("Suffolk", xy=(x43.iloc[-1], y43.iloc[-1]))

        ### Other Figure Details ###

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        # plt.legend(loc='best')
        plt.title('State Overview | County Level COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'State-Overview-County-Level_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'State Overview' figure.")
        print(f"Exception: {e}")


def create_regional_CapitalRegion(cwd, historicData, currentSummary, todayDate):
    # Capital Region Counties: Albany, Columbia, Greene, Saratoga, Schenectady, Rensselaer, Warren, Washington

    try:

        plt.figure(figsize=(15, 10))

        albanyCounty = historicData[historicData['county'] == "Albany County"]
        albanyCountySummary = currentSummary[currentSummary['county'] == "Albany County"]
        albanyCounty = albanyCounty[albanyCounty['metrics.icuHeadroomRatio'] != 0]
        albanyCounty = albanyCounty[albanyCounty['metrics.caseDensity'] != 0]
        albanyCountyMetrics = pd.json_normalize(albanyCountySummary['metrics'])
        albanyCountyActuals = pd.json_normalize(albanyCountySummary['actuals'])
        albanyPercentageICURemaining = (((albanyCountyActuals['icuBeds.capacity'] - (
                albanyCountyMetrics['icuHeadroomDetails.currentIcuCovid'] + albanyCountyMetrics[
            'icuHeadroomDetails.currentIcuNonCovid'])) / albanyCountyActuals['icuBeds.capacity']) * 100).values[0].astype(
            int)

        ColumbiaCounty = historicData[historicData['county'] == "Columbia County"]
        ColumbiaCounty = ColumbiaCounty.fillna(0)
        ColumbiaCountySummary = currentSummary[currentSummary['county'] == "Columbia County"]
        ColumbiaCountySummary = ColumbiaCountySummary.fillna(0)
        ColumbiaCounty = ColumbiaCounty[ColumbiaCounty['metrics.icuHeadroomRatio'] != 0]
        ColumbiaCounty = ColumbiaCounty[ColumbiaCounty['metrics.caseDensity'] != 0]
        ColumbiaCountyMetrics = pd.json_normalize(ColumbiaCountySummary['metrics'])
        ColumbiaCountyActuals = pd.json_normalize(ColumbiaCountySummary['actuals'])
        ColumbiaPercentageICURemaining = (((ColumbiaCountyActuals['icuBeds.capacity'] - (
                ColumbiaCountyMetrics['icuHeadroomDetails.currentIcuCovid'] + ColumbiaCountyMetrics[
            'icuHeadroomDetails.currentIcuNonCovid'])) / ColumbiaCountyActuals['icuBeds.capacity']) * 100).values[0].astype(
            int)

        SaratogaCounty = historicData[historicData['county'] == "Saratoga County"]
        SaratogaCounty = SaratogaCounty.fillna(0)
        SaratogaCountySummary = currentSummary[currentSummary['county'] == "Saratoga County"]
        SaratogaCountySummary = SaratogaCountySummary.fillna(0)
        SaratogaCounty = SaratogaCounty[SaratogaCounty['metrics.icuHeadroomRatio'] != 0]
        SaratogaCounty = SaratogaCounty[SaratogaCounty['metrics.caseDensity'] != 0]
        SaratogaCountyMetrics = pd.json_normalize(SaratogaCountySummary['metrics'])
        SaratogaCountyActuals = pd.json_normalize(SaratogaCountySummary['actuals'])
        SaratogaPercentageICURemaining = (((SaratogaCountyActuals['icuBeds.capacity'] - (
                SaratogaCountyMetrics['icuHeadroomDetails.currentIcuCovid'] + SaratogaCountyMetrics[
            'icuHeadroomDetails.currentIcuNonCovid'])) / SaratogaCountyActuals['icuBeds.capacity']) * 100).values[0].astype(
            int)

        SchenectadyCounty = historicData[historicData['county'] == "Schenectady County"]
        SchenectadyCounty = SchenectadyCounty.fillna(0)
        SchenectadyCountySummary = currentSummary[currentSummary['county'] == "Schenectady County"]
        SchenectadyCountySummary = SchenectadyCountySummary.fillna(0)
        SchenectadyCounty = SchenectadyCounty[SchenectadyCounty['metrics.icuHeadroomRatio'] != 0]
        SchenectadyCounty = SchenectadyCounty[SchenectadyCounty['metrics.caseDensity'] != 0]
        SchenectadyCountyMetrics = pd.json_normalize(SchenectadyCountySummary['metrics'])
        SchenectadyCountyActuals = pd.json_normalize(SchenectadyCountySummary['actuals'])
        SchenectadyPercentageICURemaining = (((SchenectadyCountyActuals['icuBeds.capacity'] - (
                SchenectadyCountyMetrics['icuHeadroomDetails.currentIcuCovid'] + SchenectadyCountyMetrics[
            'icuHeadroomDetails.currentIcuNonCovid'])) / SchenectadyCountyActuals['icuBeds.capacity']) * 100).values[
            0].astype(int)

        RensselaerCounty = historicData[historicData['county'] == "Rensselaer County"]
        RensselaerCounty = RensselaerCounty.fillna(0)
        RensselaerCountySummary = currentSummary[currentSummary['county'] == "Rensselaer County"]
        RensselaerCountySummary = RensselaerCountySummary.fillna(0)
        RensselaerCounty = RensselaerCounty[RensselaerCounty['metrics.icuHeadroomRatio'] != 0]
        RensselaerCounty = RensselaerCounty[RensselaerCounty['metrics.caseDensity'] != 0]
        RensselaerCountyMetrics = pd.json_normalize(RensselaerCountySummary['metrics'])
        RensselaerCountyActuals = pd.json_normalize(RensselaerCountySummary['actuals'])
        RensselaerPercentageICURemaining = (((RensselaerCountyActuals['icuBeds.capacity'] - (
                RensselaerCountyMetrics['icuHeadroomDetails.currentIcuCovid'] + RensselaerCountyMetrics[
            'icuHeadroomDetails.currentIcuNonCovid'])) / RensselaerCountyActuals['icuBeds.capacity']) * 100).values[
            0].astype(int)

        WarrenCounty = historicData[historicData['county'] == "Warren County"]
        WarrenCounty = WarrenCounty.fillna(0)
        WarrenCountySummary = currentSummary[currentSummary['county'] == "Warren County"]
        WarrenCountySummary = WarrenCountySummary.fillna(0)
        WarrenCounty = WarrenCounty[WarrenCounty['metrics.icuHeadroomRatio'] != 0]
        WarrenCounty = WarrenCounty[WarrenCounty['metrics.caseDensity'] != 0]
        WarrenCountyMetrics = pd.json_normalize(WarrenCountySummary['metrics'])
        WarrenCountyActuals = pd.json_normalize(WarrenCountySummary['actuals'])
        WarrenPercentageICURemaining = (((WarrenCountyActuals['icuBeds.capacity'] - (
                WarrenCountyMetrics['icuHeadroomDetails.currentIcuCovid'] + WarrenCountyMetrics[
            'icuHeadroomDetails.currentIcuNonCovid'])) / WarrenCountyActuals['icuBeds.capacity']) * 100).values[0].astype(
            int)

        plt.annotate("Greene and Washington counties do not have hospitals.", xy=(0.01, 1))

        # X/Y Metrics
        x1 = albanyCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = albanyCounty['metrics.caseDensity'].tail(14)

        x2 = ColumbiaCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = ColumbiaCounty['metrics.caseDensity'].tail(14)

        x3 = SaratogaCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = SaratogaCounty['metrics.caseDensity'].tail(14)

        x4 = SchenectadyCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = SchenectadyCounty['metrics.caseDensity'].tail(14)

        x5 = RensselaerCounty['metrics.icuHeadroomRatio'].tail(14)
        y5 = RensselaerCounty['metrics.caseDensity'].tail(14)

        x6 = WarrenCounty['metrics.icuHeadroomRatio'].tail(14)
        y6 = WarrenCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Albany County")
        plt.annotate(f"Albany: {albanyPercentageICURemaining}% ICU Remaining", xy=(x1.iloc[-1], y1.iloc[-1]), xytext=(3, 3),
                     textcoords='offset points')

        plt.plot(x2, y2, '.-', linewidth='1', label="Columbia County")
        plt.annotate(f"Columbia: {ColumbiaPercentageICURemaining}% ICU Remaining", xy=(x2.iloc[-1], y2.iloc[-1]),
                     xytext=(3, 3),
                     textcoords='offset points')

        plt.plot(x3, y3, '.-', linewidth='1', label="Saratoga County")
        plt.annotate(f"Saratoga: {SaratogaPercentageICURemaining}% ICU Remaining", xy=(x3.iloc[-1], y3.iloc[-1]),
                     xytext=(3, 3),
                     textcoords='offset points')

        plt.plot(x4, y4, '.-', linewidth='1', label="Schenectady County")
        plt.annotate(f"Schenectady: {SchenectadyPercentageICURemaining}% ICU Remaining", xy=(x4.iloc[-1], y4.iloc[-1]),
                     xytext=(3, 3), textcoords='offset points')

        plt.plot(x5, y5, '.-', linewidth='1', label="Rensselaer County")
        plt.annotate(f"Rensselaer: {RensselaerPercentageICURemaining}% ICU Remaining", xy=(x5.iloc[-1], y5.iloc[-1]),
                     xytext=(3, 3), textcoords='offset points')

        plt.plot(x6, y6, '.-', linewidth='1', label="Warren County")
        plt.annotate(f"Warren: {WarrenPercentageICURemaining}% ICU Remaining", xy=(x6.iloc[-1], y6.iloc[-1]), xytext=(3, 3),
                     textcoords='offset points')

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Capital Region | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Capital-Region_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Capital Region' regional figure.")
        print(f"Exception: {e}")


def create_regional_WesternNewYork(cwd, historicData, todayDate):
    # Western New York Region Counties: Allegany, Cattaraugus, Chautauqua, Erie, Niagara

    try:
        plt.figure(figsize=(15, 10))

        AlleganyCounty = historicData[historicData['county'] == "Allegany County"]
        AlleganyCounty = AlleganyCounty.fillna(0)
        AlleganyCounty = AlleganyCounty[AlleganyCounty['metrics.icuHeadroomRatio'] != 0]
        AlleganyCounty = AlleganyCounty[AlleganyCounty['metrics.caseDensity'] != 0]

        ChautauquaCounty = historicData[historicData['county'] == "Chautauqua County"]
        ChautauquaCounty = ChautauquaCounty.fillna(0)
        ChautauquaCounty = ChautauquaCounty[ChautauquaCounty['metrics.icuHeadroomRatio'] != 0]
        ChautauquaCounty = ChautauquaCounty[ChautauquaCounty['metrics.caseDensity'] != 0]

        ErieCounty = historicData[historicData['county'] == "Erie County"]
        ErieCounty = ErieCounty.fillna(0)
        ErieCounty = ErieCounty[ErieCounty['metrics.icuHeadroomRatio'] != 0]
        ErieCounty = ErieCounty[ErieCounty['metrics.caseDensity'] != 0]

        NiagaraCounty = historicData[historicData['county'] == "Niagara County"]
        NiagaraCounty = NiagaraCounty.fillna(0)
        NiagaraCounty = NiagaraCounty[NiagaraCounty['metrics.icuHeadroomRatio'] != 0]
        NiagaraCounty = NiagaraCounty[NiagaraCounty['metrics.caseDensity'] != 0]

        plt.annotate("There is insufficient data available for Cattaraugus County.", xy=(.01, 1))

        # X/Y Metrics
        x1 = AlleganyCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = AlleganyCounty['metrics.caseDensity'].tail(14)

        x2 = ChautauquaCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = ChautauquaCounty['metrics.caseDensity'].tail(14)

        x3 = ErieCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = ErieCounty['metrics.caseDensity'].tail(14)

        x4 = NiagaraCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = NiagaraCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Allegany County")
        plt.annotate("Allegany", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x2, y2, '.-', linewidth='1', label="Chautauqua County")
        plt.annotate("Chautauqua", xy=(x2.iloc[-1], y2.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Erie County")
        plt.annotate("Erie", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x4, y4, '.-', linewidth='1', label="Niagara County")
        plt.annotate("Niagara", xy=(x4.iloc[-1], y4.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Western New York | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Western-New-York_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Western New York' regional figure.")
        print(f"Exception: {e}")


def create_regional_FingerLakes(cwd, historicData, todayDate):
    # Finger Lakes Counties: Genesee, Livingston, Monroe, Ontario, Orleans, Seneca, Wayne, Wyoming, Yates
    try:
        plt.figure(figsize=(15, 10))

        GeneseeCounty = historicData[historicData['county'] == "Genesee County"]
        GeneseeCounty = GeneseeCounty.fillna(0)
        GeneseeCounty = GeneseeCounty[GeneseeCounty['metrics.icuHeadroomRatio'] != 0]
        GeneseeCounty = GeneseeCounty[GeneseeCounty['metrics.caseDensity'] != 0]

        MonroeCounty = historicData[historicData['county'] == "Monroe County"]
        MonroeCounty = MonroeCounty.fillna(0)
        MonroeCounty = MonroeCounty[MonroeCounty['metrics.icuHeadroomRatio'] != 0]
        MonroeCounty = MonroeCounty[MonroeCounty['metrics.caseDensity'] != 0]

        OntarioCounty = historicData[historicData['county'] == "Ontario County"]
        OntarioCounty = OntarioCounty.fillna(0)
        OntarioCounty = OntarioCounty[OntarioCounty['metrics.icuHeadroomRatio'] != 0]
        OntarioCounty = OntarioCounty[OntarioCounty['metrics.caseDensity'] != 0]

        WayneCounty = historicData[historicData['county'] == "Wayne County"]
        WayneCounty = WayneCounty.fillna(0)
        WayneCounty = WayneCounty[WayneCounty['metrics.icuHeadroomRatio'] != 0]
        WayneCounty = WayneCounty[WayneCounty['metrics.caseDensity'] != 0]

        WyomingCounty = historicData[historicData['county'] == "Wyoming County"]
        WyomingCounty = WyomingCounty.fillna(0)
        WyomingCounty = WyomingCounty[WyomingCounty['metrics.icuHeadroomRatio'] != 0]
        WyomingCounty = WyomingCounty[WyomingCounty['metrics.caseDensity'] != 0]

        plt.annotate("Seneca County does not have any hospitals.", xy=(.01, 1))
        plt.annotate("There is insufficient data available for Livingston, Orleans, and Yates counties.", xy=(.01, 3))

        # X/Y Metrics
        x1 = GeneseeCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = GeneseeCounty['metrics.caseDensity'].tail(14)

        x2 = MonroeCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = MonroeCounty['metrics.caseDensity'].tail(14)

        x3 = OntarioCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = OntarioCounty['metrics.caseDensity'].tail(14)

        x4 = WayneCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = WayneCounty['metrics.caseDensity'].tail(14)

        x5 = WyomingCounty['metrics.icuHeadroomRatio'].tail(14)
        y5 = WyomingCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Genesee County")
        plt.annotate("Genesee", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x2, y2, '.-', linewidth='1', label="Monroe County")
        plt.annotate("Monroe", xy=(x2.iloc[-1], y2.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Ontario County")
        plt.annotate("Ontario", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x4, y4, '.-', linewidth='1', label="Wayne County")
        plt.annotate("Wayne", xy=(x4.iloc[-1], y4.iloc[-1]))

        plt.plot(x5, y5, '.-', linewidth='1', label="Wyoming County")
        plt.annotate("Wyoming", xy=(x5.iloc[-1], y5.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Finger Lakes | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Finger-Lakes_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Finger Lakes' regional figure.")
        print(f"Exception: {e}")


def create_regional_SouthernTier(cwd, historicData, todayDate):
    # Southern Counties: Broome, Chemung, Chenango, Delaware, Schuyler, Steuben, Tioga, Tompkins

    try:
        plt.figure(figsize=(15, 10))

        BroomeCounty = historicData[historicData['county'] == "Broome County"]
        BroomeCounty = BroomeCounty[BroomeCounty['metrics.icuHeadroomRatio'] != 0]
        BroomeCounty = BroomeCounty[BroomeCounty['metrics.caseDensity'] != 0]

        ChemungCounty = historicData[historicData['county'] == "Chemung County"]
        ChemungCounty = ChemungCounty[ChemungCounty['metrics.icuHeadroomRatio'] != 0]
        ChemungCounty = ChemungCounty[ChemungCounty['metrics.caseDensity'] != 0]

        ChenangoCounty = historicData[historicData['county'] == "Chenango County"]
        ChenangoCounty = ChenangoCounty[ChenangoCounty['metrics.icuHeadroomRatio'] != 0]
        ChenangoCounty = ChenangoCounty[ChenangoCounty['metrics.caseDensity'] != 0]

        SteubenCounty = historicData[historicData['county'] == "Steuben County"]
        SteubenCounty = SteubenCounty[SteubenCounty['metrics.icuHeadroomRatio'] != 0]
        SteubenCounty = SteubenCounty[SteubenCounty['metrics.caseDensity'] != 0]

        TompkinsCounty = historicData[historicData['county'] == "Tompkins County"]
        TompkinsCounty = TompkinsCounty[TompkinsCounty['metrics.icuHeadroomRatio'] != 0]
        TompkinsCounty = TompkinsCounty[TompkinsCounty['metrics.caseDensity'] != 0]

        plt.annotate("Tioga County does not have any hospitals.", xy=(.01, 1))
        plt.annotate("There is insufficient data available for Delaware and Schuyler counties.", xy=(.01, 3))

        # X/Y Metrics
        x1 = BroomeCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = BroomeCounty['metrics.caseDensity'].tail(14)

        x2 = ChemungCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = ChemungCounty['metrics.caseDensity'].tail(14)

        x3 = ChenangoCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = ChenangoCounty['metrics.caseDensity'].tail(14)

        x6 = SteubenCounty['metrics.icuHeadroomRatio'].tail(14)
        y6 = SteubenCounty['metrics.caseDensity'].tail(14)

        x7 = TompkinsCounty['metrics.icuHeadroomRatio'].tail(14)
        y7 = TompkinsCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Broome County")
        plt.annotate("Genesee", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x2, y2, '.-', linewidth='1', label="Chemung County")
        plt.annotate("Chemung", xy=(x2.iloc[-1], y2.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Chenango County")
        plt.annotate("Chenango", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x6, y6, '.-', linewidth='1', label="Steuben County")
        plt.annotate("Steuben", xy=(x6.iloc[-1], y6.iloc[-1]))

        plt.plot(x7, y7, '.-', linewidth='1', label="Tompkins County")
        plt.annotate("Tompkins", xy=(x7.iloc[-1], y7.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Southern Tier | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Southern-Tier_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")

    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Southern Tier' regional figure.")
        print(f"Exception: {e}")


def create_regional_CentralNewYork(cwd, historicData, todayDate):
    # Central New York Counties: Cayuga, Cortland, Madison, Onondaga, Oswego

    try:
        plt.figure(figsize=(15, 10))

        CayugaCounty = historicData[historicData['county'] == "Cayuga County"]
        CayugaCounty = CayugaCounty[CayugaCounty['metrics.icuHeadroomRatio'] != 0]
        CayugaCounty = CayugaCounty[CayugaCounty['metrics.caseDensity'] != 0]

        CortlandCounty = historicData[historicData['county'] == "Cortland County"]
        CortlandCounty = CortlandCounty[CortlandCounty['metrics.icuHeadroomRatio'] != 0]
        CortlandCounty = CortlandCounty[CortlandCounty['metrics.caseDensity'] != 0]

        MadisonCounty = historicData[historicData['county'] == "Madison County"]
        MadisonCounty = MadisonCounty[MadisonCounty['metrics.icuHeadroomRatio'] != 0]
        MadisonCounty = MadisonCounty[MadisonCounty['metrics.caseDensity'] != 0]

        OnondagaCounty = historicData[historicData['county'] == "Onondaga County"]
        OnondagaCounty = OnondagaCounty[OnondagaCounty['metrics.icuHeadroomRatio'] != 0]
        OnondagaCounty = OnondagaCounty[OnondagaCounty['metrics.caseDensity'] != 0]

        OswegoCounty = historicData[historicData['county'] == "Oswego County"]
        OswegoCounty = OswegoCounty[OswegoCounty['metrics.icuHeadroomRatio'] != 0]
        OswegoCounty = OswegoCounty[OswegoCounty['metrics.caseDensity'] != 0]

        # X/Y Metrics
        x1 = CayugaCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = CayugaCounty['metrics.caseDensity'].tail(14)

        x2 = CortlandCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = CortlandCounty['metrics.caseDensity'].tail(14)

        x3 = MadisonCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = MadisonCounty['metrics.caseDensity'].tail(14)

        x4 = OnondagaCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = OnondagaCounty['metrics.caseDensity'].tail(14)

        x5 = OswegoCounty['metrics.icuHeadroomRatio'].tail(14)
        y5 = OswegoCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Cayuga County")
        plt.annotate("Cayuga", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x2, y2, '.-', linewidth='1', label="Cortland County")
        plt.annotate("Cortland", xy=(x2.iloc[-1], y2.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Madison County")
        plt.annotate("Madison", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x4, y4, '.-', linewidth='1', label="Onondaga County")
        plt.annotate("Onondaga", xy=(x4.iloc[-1], y4.iloc[-1]))

        plt.plot(x5, y5, '.-', linewidth='1', label="Oswego County")
        plt.annotate("Oswego", xy=(x5.iloc[-1], y5.iloc[-1]))

        plt.xlabel('ICU Capacity Utilized')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Central New York | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Central-New-York_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Central New York' regional figure.")
        print(f"Exception: {e}")


def create_regional_MohawkValley(cwd, historicData, todayDate):
    # Mohawk Valley Counties: Fulton, Herkimer, Montgomery, Oneida, Otsego, Schoharie

    try:

        plt.figure(figsize=(15, 10))

        FultonCounty = historicData[historicData['county'] == "Fulton County"]
        FultonCounty = FultonCounty[FultonCounty['metrics.icuHeadroomRatio'] != 0]
        FultonCounty = FultonCounty[FultonCounty['metrics.caseDensity'] != 0]

        MontgomeryCounty = historicData[historicData['county'] == "Montgomery County"]
        MontgomeryCounty = MontgomeryCounty[MontgomeryCounty['metrics.icuHeadroomRatio'] != 0]
        MontgomeryCounty = MontgomeryCounty[MontgomeryCounty['metrics.caseDensity'] != 0]

        OneidaCounty = historicData[historicData['county'] == "Oneida County"]
        OneidaCounty = OneidaCounty[OneidaCounty['metrics.icuHeadroomRatio'] != 0]
        OneidaCounty = OneidaCounty[OneidaCounty['metrics.caseDensity'] != 0]

        OtsegoCounty = historicData[historicData['county'] == "Otsego County"]
        OtsegoCounty = OtsegoCounty[OtsegoCounty['metrics.icuHeadroomRatio'] != 0]
        OtsegoCounty = OtsegoCounty[OtsegoCounty['metrics.caseDensity'] != 0]

        plt.annotate("There is insufficient data available for Herkimer and Schoharie counties.", xy=(.01, 1))

        # X/Y Metrics
        x1 = FultonCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = FultonCounty['metrics.caseDensity'].tail(14)

        x3 = MontgomeryCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = MontgomeryCounty['metrics.caseDensity'].tail(14)

        x4 = OneidaCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = OneidaCounty['metrics.caseDensity'].tail(14)

        x5 = OtsegoCounty['metrics.icuHeadroomRatio'].tail(14)
        y5 = OtsegoCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Fulton County")
        plt.annotate("Fulton", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Montgomery County")
        plt.annotate("Montgomery", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x4, y4, '.-', linewidth='1', label="Oneida County")
        plt.annotate("Oneida", xy=(x4.iloc[-1], y4.iloc[-1]))

        plt.plot(x5, y5, '.-', linewidth='1', label="Otsego County")
        plt.annotate("Otsego", xy=(x5.iloc[-1], y5.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.xticks(rotation=30)
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.legend(loc='best')
        plt.title('Mohawk Valley | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Mohawk-Valley_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Mohawk Valley' regional figure.")
        print(f"Exception: {e}")


def create_regional_NorthCountry(cwd, historicData, todayDate):
    # North Country Counties: Clinton, Essex, Franklin, Hamilton, Jefferson, Lewis, St. Lawrence

    try:
        plt.figure(figsize=(15, 10))

        ClintonCounty = historicData[historicData['county'] == "Clinton County"]
        ClintonCounty = ClintonCounty[ClintonCounty['metrics.icuHeadroomRatio'] != 0]
        ClintonCounty = ClintonCounty[ClintonCounty['metrics.caseDensity'] != 0]

        FranklinCounty = historicData[historicData['county'] == "Franklin County"]
        FranklinCounty = FranklinCounty[FranklinCounty['metrics.icuHeadroomRatio'] != 0]
        FranklinCounty = FranklinCounty[FranklinCounty['metrics.caseDensity'] != 0]

        JeffersonCounty = historicData[historicData['county'] == "Jefferson County"]
        JeffersonCounty = JeffersonCounty[JeffersonCounty['metrics.icuHeadroomRatio'] != 0]
        JeffersonCounty = JeffersonCounty[JeffersonCounty['metrics.caseDensity'] != 0]

        LewisCounty = historicData[historicData['county'] == "Lewis County"]
        LewisCounty = LewisCounty[LewisCounty['metrics.icuHeadroomRatio'] != 0]
        LewisCounty = LewisCounty[LewisCounty['metrics.caseDensity'] != 0]

        StLawrenceCounty = historicData[historicData['county'] == "St. Lawrence County"]
        StLawrenceCounty = StLawrenceCounty[StLawrenceCounty['metrics.icuHeadroomRatio'] != 0]
        StLawrenceCounty = StLawrenceCounty[StLawrenceCounty['metrics.caseDensity'] != 0]

        plt.annotate("Hamilton County does not have any hospitals.", xy=(.01, 1))
        plt.annotate("There is insufficient data available for Essex and Schuyler counties.", xy=(.01, 3))

        # X/Y Metrics
        x1 = ClintonCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = ClintonCounty['metrics.caseDensity'].tail(14)

        x3 = FranklinCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = FranklinCounty['metrics.caseDensity'].tail(14)

        x4 = JeffersonCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = JeffersonCounty['metrics.caseDensity'].tail(14)

        x5 = LewisCounty['metrics.icuHeadroomRatio'].tail(14)
        y5 = LewisCounty['metrics.caseDensity'].tail(14)

        x6 = StLawrenceCounty['metrics.icuHeadroomRatio'].tail(14)
        y6 = StLawrenceCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Clinton County")
        plt.annotate("Clinton", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Franklin County")
        plt.annotate("Franklin", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x4, y4, '.-', linewidth='1', label="Jefferson County")
        plt.annotate("Jefferson", xy=(x4.iloc[-1], y4.iloc[-1]))

        plt.plot(x5, y5, '.-', linewidth='1', label="Lewis County")
        plt.annotate("Lewis", xy=(x5.iloc[-1], y5.iloc[-1]))

        plt.plot(x6, y6, '.-', linewidth='1', label="St. Lawrence County")
        plt.annotate("St. Lawrence", xy=(x6.iloc[-1], y6.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('North Country | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'North-Country_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'North Country' regional figure.")
        print(f"Exception: {e}")


def create_regional_MidHudson(cwd, historicData, todayDate):
    # Mid-Hudson Counties: Dutchess, Orange, Putnam, Rockland, Sullivan, Ulster, Westchester

    try:
        plt.figure(figsize=(15, 10))

        DutchessCounty = historicData[historicData['county'] == "Dutchess County"]
        DutchessCounty = DutchessCounty[DutchessCounty['metrics.icuHeadroomRatio'] != 0]
        DutchessCounty = DutchessCounty[DutchessCounty['metrics.caseDensity'] != 0]

        OrangeCounty = historicData[historicData['county'] == "Orange County"]
        OrangeCounty = OrangeCounty[OrangeCounty['metrics.icuHeadroomRatio'] != 0]
        OrangeCounty = OrangeCounty[OrangeCounty['metrics.caseDensity'] != 0]

        PutnamCounty = historicData[historicData['county'] == "Putnam County"]
        PutnamCounty = PutnamCounty[PutnamCounty['metrics.icuHeadroomRatio'] != 0]
        PutnamCounty = PutnamCounty[PutnamCounty['metrics.caseDensity'] != 0]

        RocklandCounty = historicData[historicData['county'] == "Rockland County"]
        RocklandCounty = RocklandCounty[RocklandCounty['metrics.icuHeadroomRatio'] != 0]
        RocklandCounty = RocklandCounty[RocklandCounty['metrics.caseDensity'] != 0]

        SullivanCounty = historicData[historicData['county'] == "Sullivan County"]
        SullivanCounty = SullivanCounty[SullivanCounty['metrics.icuHeadroomRatio'] != 0]
        SullivanCounty = SullivanCounty[SullivanCounty['metrics.caseDensity'] != 0]

        UlsterCounty = historicData[historicData['county'] == "Ulster County"]
        UlsterCounty = UlsterCounty[UlsterCounty['metrics.icuHeadroomRatio'] != 0]
        UlsterCounty = UlsterCounty[UlsterCounty['metrics.caseDensity'] != 0]

        WestchesterCounty = historicData[historicData['county'] == "Westchester County"]
        WestchesterCounty = WestchesterCounty[WestchesterCounty['metrics.icuHeadroomRatio'] != 0]
        WestchesterCounty = WestchesterCounty[WestchesterCounty['metrics.caseDensity'] != 0]

        # X/Y Metrics
        x1 = DutchessCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = DutchessCounty['metrics.caseDensity'].tail(14)

        x2 = OrangeCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = OrangeCounty['metrics.caseDensity'].tail(14)

        x3 = PutnamCounty['metrics.icuHeadroomRatio'].tail(14)
        y3 = PutnamCounty['metrics.caseDensity'].tail(14)

        x4 = RocklandCounty['metrics.icuHeadroomRatio'].tail(14)
        y4 = RocklandCounty['metrics.caseDensity'].tail(14)

        x5 = SullivanCounty['metrics.icuHeadroomRatio'].tail(14)
        y5 = SullivanCounty['metrics.caseDensity'].tail(14)

        x6 = UlsterCounty['metrics.icuHeadroomRatio'].tail(14)
        y6 = UlsterCounty['metrics.caseDensity'].tail(14)

        x7 = WestchesterCounty['metrics.icuHeadroomRatio'].tail(14)
        y7 = WestchesterCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Dutchess County")
        plt.annotate("Dutchess", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x2, y2, '.-', linewidth='1', label="Orange County")
        plt.annotate("Orange", xy=(x2.iloc[-1], y2.iloc[-1]))

        plt.plot(x3, y3, '.-', linewidth='1', label="Putnam County")
        plt.annotate("Putnam", xy=(x3.iloc[-1], y3.iloc[-1]))

        plt.plot(x4, y4, '.-', linewidth='1', label="Rockland County")
        plt.annotate("Rockland", xy=(x4.iloc[-1], y4.iloc[-1]))

        plt.plot(x5, y5, '.-', linewidth='1', label="Sullivan County")
        plt.annotate("Sullivan", xy=(x5.iloc[-1], y5.iloc[-1]))

        plt.plot(x6, y6, '.-', linewidth='1', label="Ulster County")
        plt.annotate("Ulster", xy=(x6.iloc[-1], y6.iloc[-1]))

        plt.plot(x7, y7, '.-', linewidth='1', label="Westchester County")
        plt.annotate("Westchester", xy=(x7.iloc[-1], y7.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Mid-Hudson | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Mid-Hudson_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Mid-Hudson' regional figure.")
        print(f"Exception: {e}")


def create_regional_NewYorkCity(cwd, historicData, todayDate):
    # New York City Counties: Bronx, Kings, New York, Richmond, Queens
    # TODO: Pending available data
    print("     [9 of 10] >>> Support for NYC Pending Development <<<\n")


def create_regional_LongIsland(cwd, historicData, todayDate):
    # Long Island Counties: Nassau, Suffolk

    try:

        plt.figure(figsize=(15, 10))

        NassauCounty = historicData[historicData['county'] == "Nassau County"]
        NassauCounty = NassauCounty.fillna(0)
        NassauCounty = NassauCounty[NassauCounty['metrics.icuHeadroomRatio'] != 0]
        NassauCounty = NassauCounty[NassauCounty['metrics.caseDensity'] != 0]

        SuffolkCounty = historicData[historicData['county'] == "Suffolk County"]
        SuffolkCounty = SuffolkCounty.fillna(0)
        SuffolkCounty = SuffolkCounty[SuffolkCounty['metrics.icuHeadroomRatio'] != 0]
        SuffolkCounty = SuffolkCounty[SuffolkCounty['metrics.caseDensity'] != 0]

        # X/Y Metrics
        x1 = NassauCounty['metrics.icuHeadroomRatio'].tail(14)
        y1 = NassauCounty['metrics.caseDensity'].tail(14)

        x2 = SuffolkCounty['metrics.icuHeadroomRatio'].tail(14)
        y2 = SuffolkCounty['metrics.caseDensity'].tail(14)

        # Plot the as of date/time for the figure
        plt.annotate(f"As of: {helper_functions.get_FigureDateTime()}", xy=(2, 1))

        # Plot risk lines
        yellowLineX = [.50, 0]
        yellowLineY = [0, 10]
        plt.plot(yellowLineX, yellowLineY, '--', color='yellow', linewidth='3')

        OrangeLineX = [.60, 0]
        OrangeLineY = [0, 25]
        plt.plot(OrangeLineX, OrangeLineY, '--', color='orange', linewidth='3')

        redLineX = [.70, 0]
        redLineY = [0, 50]
        plt.plot(redLineX, redLineY, 'r--', linewidth='3')

        # Plot "Over Capacity" Box
        plt.gca().add_patch(Rectangle((1, -1), 2, 200, edgecolor='red', facecolor='none', lw=2, hatch='/'))

        # Set axis parameters
        plt.axis([0, 2.5, 0, 150])

        # Plot trend lines
        plt.plot(x1, y1, '.-', linewidth='1', label="Nassau County")
        plt.annotate("Nassau", xy=(x1.iloc[-1], y1.iloc[-1]))

        plt.plot(x2, y2, '.-', linewidth='1', label="Suffolk County")
        plt.annotate("Suffolk", xy=(x2.iloc[-1], y2.iloc[-1]))

        plt.xlabel('% ICU Beds w/ COVID-19 Patients')
        plt.ylabel('Daily Cases per 100k - 7 Day RA')
        plt.grid()
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
        plt.xticks(rotation=30)
        plt.legend(loc='best')
        plt.title('Long Island | Regional COVID-19 Risk Map')

        # Save Figure as Image
        fileName = f'Long-Island_Risk-Map_{todayDate}.png'
        filePath = os.path.join(cwd, 'Risk_Map_Images', todayDate, fileName)
        plt.tight_layout()
        plt.savefig(filePath)
        print(f"    Figured saved --> {filePath}\n")
    except Exception as e:
        print("\nAn unhandled exception was encountered while attempting to create the 'Long Island' regional figure.")
        print(f"Exception: {e}")


def main():
    # Clear the terminal screen (useful for testing multiple iterations)
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    print("*"*56)
    print("---> NYS Regional COVID-19 ICU Risk Assessment Tool <---")
    print("*" * 56)
    print("")
    print("Developed and maintained by: Chris Cooley")
    print("www.centerforcyberintelligence.org")
    print("-"*70)
    print("Support for this project provided by:")
    print("- Phil Langlois")
    print("- Aaron Cooley")
    print(">>> Support this project on Patreon @ www.patreon.com/chriscooley <<<")
    print("=" * 70)
    print("Data provided by: COVID Act Now")
    print("www.covidactnow.org")
    print("")
    print("+" * 70)
    print("")

    # Get current working directory
    print("[*] Setting up the working directory...")
    os.chdir("..")
    cwd = os.getcwd()
    print(f"    CWD --> {cwd}\n")

    # Get today's data
    print("[*] Getting today's date...")
    todayDate = helper_functions.get_Date()
    print(f"    Today's Date --> {todayDate}\n")

    # Set Figure Images Filepath
    print("[*] Setting a path to enable this script to save figure images...\n")
    helper_functions.set_ImageSavePath(cwd)

    # Grab the data frames
    print("[*] Grabbing time series and current summary data from COVID Act Now - (this may take some time)...\n")
    historicData = helper_functions.get_HistoricData()
    print("[*] --> [1 of 2] COMPLETE | Time series data converted to a Python pandas data frame...\n")
    currentSummary = helper_functions.get_currentSummary()
    print("[*] --> [2 of 2] COMPLETE | Current summary data converted to a Python pandas data frame...\n")

    # Save the data to the Google Drive
    helper_functions.drive_write_DataToFolder()

    # Create the figures
    print("*** Creating Analytical Figures ***\n")

    print("[1 of 11] Creating the State Overview figure...")
    create_StateOverview(cwd, historicData, todayDate)
    print("[2 of 11] Creating the Capital Region figure...")
    create_regional_CapitalRegion(cwd, historicData, currentSummary, todayDate)
    print("[3 of 11] Creating the Western New York figure...")
    create_regional_WesternNewYork(cwd, historicData, todayDate)
    print("[4 of 11] Creating the Finger Lakes figure...")
    create_regional_FingerLakes(cwd, historicData, todayDate)
    print("[5 of 11] Creating the Southern Tier figure...")
    create_regional_SouthernTier(cwd, historicData, todayDate)
    print("[6 of 11] Creating the Central New York figure...")
    create_regional_CentralNewYork(cwd, historicData, todayDate)
    print("[7 of 11] Creating the Mohawk Valley figure...")
    create_regional_MohawkValley(cwd, historicData, todayDate)
    print("[8 of 11] Creating the North Country figure...")
    create_regional_NorthCountry(cwd, historicData, todayDate)
    print("[9 of 11] Creating the New York City figure...")
    create_regional_NewYorkCity(cwd, historicData, todayDate)
    print("[10 of 11] Creating the Long Island figure...")
    create_regional_LongIsland(cwd, historicData, todayDate)
    print("[11 of 11] Creating the Mid-Hudson figure...")
    create_regional_MidHudson(cwd, historicData, todayDate)

    print("\n** Creating PowerPoint Presentation **\n")
    pptxGenerator.makePresentation()
    helper_functions.drive_write_ICUImagesToFolder()

    print("\n**************************")
    print("---> PROCESS COMPLETE <---")


main()
