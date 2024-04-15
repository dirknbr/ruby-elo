# International Rugby ELO ranking & Investec Cup

We use about 300 head to head games to calculate the ELO rating for the top 15
rugby nations in the world.

- data.py: get match data from rugbypass
- utils.py: some ELO functions
- calc_rating.py: use the match data to calculate ELO
- calc_rating_investec.py: use the match data to calculate ELO for Investec Cup (clubs)

I have updated the ELO function a bit to take into account the match score.

Note that the point difference is distributed as $N(5, 20^2)$

The ELO ranking is very similar to the [official ranking](https://www.world.rugby/tournaments/rankings/mru)

## Ranking 

(525.1923181277855, 'New Zealand')
(519.9448202174954, 'Ireland')
(501.59978945294995, 'South Africa')
(474.66536763052613, 'France')
(454.12017717364716, 'Scotland')
(433.493004415046, 'England')
(403.27046170830346, 'Australia')
(378.88084486591293, 'Wales')
(361.9215578609213, 'Fiji')
(359.11074359858026, 'Argentina')
(339.90522344396925, 'Samoa')
(337.13705592623586, 'Japan')
(320.0803308618492, 'Tonga')
(306.43724969682455, 'Georgia')
(284.2410550199534, 'Italy')

Last updated: Aug 2023

## Investec ranking

(457.15760654401663, 'Toulouse')
(455.67140586619104, 'Northampton')
(455.1200895523201, 'Leinster')
(438.3698304352811, 'Harlequins')
(426.18485736462475, 'Stormers')
(419.9052329720977, 'Bulls')
(418.3580513796452, 'Exeter')
(418.34180203280556, 'Bordeaux')
(408.3115196972937, 'Bath')
(403.1262071939254, 'Rochelle')
(401.1144929189108, 'Bayonne')
(391.64255850198896, 'Saracens')
(391.0547784168602, 'Glasgow')
(390.01741764269366, 'Lyon')
(381.14907129541183, 'Connacht')
(381.11749895349146, 'Ulster')
(380.575064428953, 'Sale')
(379.4258836917472, 'Bristol')
(373.2724727166619, 'Munster')
(372.791385818305, 'Racing')
(372.2013439243015, 'Leicester')
(362.79243753587525, 'Paris')
(361.1655699916433, 'Toulon')
(361.1334211249548, 'Cardiff')

Last updated: Apr 2024

