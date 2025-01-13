# International Rugby ELO ranking & Investec Cup

We use about 400 head to head games to calculate the ELO rating for the top 15
rugby nations in the world.

- data.py: get match data from rugbypass
- utils.py: some ELO functions
- calc_rating.py: use the match data to calculate ELO
- calc_rating_investec.py: use the match data to calculate ELO for Investec Cup (clubs)

I have updated the ELO function a bit to take into account the match score.

Note that the point difference is distributed as $N(5, 21.5^2)$

The ELO ranking is very similar to the [official ranking](https://www.world.rugby/tournaments/rankings/mru)

## Ranking 

605.3 Ireland
576.9 South Africa
570.6 New Zealand
523.9 France
447.0 England
433.2 Scotland
410.4 Fiji
380.0 Argentina
374.4 Australia
319.9 Wales
294.7 Italy
289.1 Samoa
275.6 Georgia
264.9 Japan
234.0 Tonga

Last updated: Nov 2024

## Investec ranking

(499.13667952691316, 'Toulouse')
(480.1041441796326, 'Leinster')
(449.76816583847256, 'Northampton')
(444.4828002908218, 'Bordeaux')
(415.98013844886043, 'Harlequins')
(413.75511171099134, 'Stormers')
(413.49423610992335, 'Rochelle')
(411.0471760455902, 'Castres')
(401.1144929189108, 'Bayonne')
(399.9583985166692, 'Saracens')
(399.49774000453016, 'Glasgow')
(398.3182723207659, 'Bath')
(395.05510584764534, 'Toulon')
(391.7858442720971, 'Sharks')
(391.123770475123, 'Clermont')
(391.0038360649362, 'Exeter')
(390.40830737050334, 'Bulls')
(390.01741764269366, 'Lyon')
(389.16063206959734, 'Benetton')
(384.5916166722179, 'Leicester')
(384.2954127079921, 'Munster')
(381.14907129541183, 'Connacht')
(373.841151552685, 'Bristol')
(371.9309059817123, 'Sale')
(364.4627136560915, 'Racing')
(361.1334211249548, 'Cardiff')
(357.790778967833, 'Paris')
(355.59265838642386, 'Ulster')

Last updated: Jan 2025

