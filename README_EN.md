\============================================

HOI4 BALANCE OF POWER GENERATOR

Version 1.0 | May 2026

\============================================

PURPOSE

\-------

This program creates modding files for the Balance of Power

mechanic in Hearts of Iron IV version 1.18.2 (It may also work on earlier versions, but I haven't tested it.))

WHAT IT GENERATES

\-----------------

- Main BoP file (common/bop/)
- Localisation in Russian and/or English (localisation/)
- code for GFX for side icons (interface/)
- Decision categories (common/decisions/categories/)
- Decisions (common/decisions/)
- Detailed README with installation instructions

HOW TO USE

\----------

1. Run BOP\_Generator.exe
1. Select interface language (1 - Russian, 2 - English)
1. Enter your country tag (e.g., GER) or press Enter
1. Follow the on-screen instructions
1. After completion, all files will be in the "generated\_bop" folder
1. Copy them into your mod folder
1. In common/national\_focus/YOUR\_TAG.txt add the activation code

(it will be shown at the end and saved in the generated README)

FILLING RULES

\-------------

- All values from -1.0 to 1.0 (game rejects others)
- min is always less than max (e.g.: -0.8 < -0.5)
- Ranges go without gaps (max of one = min of next)
- Ranges do not overlap
- Left side: from -1.0 to neutral
- Right side: from neutral to +1.0
- Neutral range strictly between sides
- All IDs must be unique
- Decimals: dot or comma (0.8 or 0,8)

CODE INPUT (on\_activate, on\_deactivate, decisions)

\--------------------------------------------------

- Press Enter on an empty line — field remains empty
- Type DONE (any case) and press Enter — finish input
- Enter code line by line, then DONE to finish

COMPATIBILITY

\-------------

- Hearts of Iron IV 1.18.2(It may also work on earlier versions, but I haven't tested it.)
- No Python installation required

AUTHOR

\------

Makarov Maximum(Discord: real\_maximum)

SUPPORT

\-------

GitHub: [https://github.com/RCGMaximum/Balance-of-Power-Generator] (You can put a star=))

LICENSE

\-------

GNU General Public License v3.0 (GPL-3.0)

Full text: see LICENSE.txt
