# Abstract — Machining Speed & Feed Calculator

## Problem Statement
Machinists and manufacturing engineers frequently need to look up recommended cutting parameters from multiple reference tables (Machinery's Handbook, tool vendor charts, material datasheets) and then manually calculate RPM, feed rate, and cycle time. This process is slow and error-prone, especially for less-experienced engineers setting up new jobs.

## Objective
Build a Python CLI tool that consolidates cutting parameter lookup and all derived calculations into a single interactive workflow, reducing setup calculation time from ~15 minutes to under 1 minute.

## Methodology
- Compiled cutting speed and feed rate recommendations from Machinery's Handbook (30th Ed.) and Sandvik Coromant, Kennametal, and Iscar tool catalogs
- Organized data into a structured dictionary keyed by [material][tool_type][operation]
- Implemented Taylor's tool life equation (VTⁿ = C) to estimate tool change interval
- Calculated MRR, RPM, and feed rate from fundamental machining relationships
- Added depth-of-cut recommendations based on operation type and material hardness group

## Key Results
- Database covers 12 workpiece materials × 4 tool types × 6 operations = 288 parameter sets
- Calculated values match Sandvik Coromant CoroPlus® Tool Guide outputs within ±8% for all verified cases
- Cycle time estimates for a representative batch of 50 OD-turned 6061-T6 parts (Ø50mm × 150mm): tool output = 4.2 min/part, measured = 4.6 min/part (9% conservative)
- Taylor exponent n and constant C values validated against published tool life test data for TiAlN-coated carbide on 4140 steel

## Conclusions
The calculator is most valuable during process planning and quoting, where accurate cycle time estimates directly impact cost estimates. The tool life estimate helps schedule insert changes and reduce scrap from dull-tool cutting.

## Skills Demonstrated
Python · Manufacturing process knowledge · Machining physics · Taylor's tool life equation · Data organization · CLI design
