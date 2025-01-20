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

(505.9542827501957, 'Toulouse')
(487.7926950840963, 'Leinster')
(457.90570296924494, 'Northampton')
(452.9775848099902, 'Bordeaux')
(425.5060924578932, 'Harlequins')
(420.7281236979307, 'Castres')
(402.7950016270771, 'Rochelle')
(402.3458055220044, 'Stormers')
(401.1144929189108, 'Bayonne')
(400.6267465946475, 'Clermont')
(399.8598665524436, 'Benetton')
(399.4722478417764, 'Bulls')
(390.62972141630223, 'Bath')
(390.2774508643287, 'Saracens')
(390.01741764269366, 'Lyon')
(389.9717859954974, 'Glasgow')
(384.39051891490345, 'Toulon')
(383.2910597529287, 'Sharks')
(382.5954929144542, 'Sale')
(381.14907129541183, 'Connacht')
(379.98813504429313, 'Exeter')
(377.77401344893536, 'Leicester')
(376.1578755772197, 'Munster')
(375.87201984507846, 'Racing')
(366.6083594070669, 'Ulster')
(364.33817543316053, 'Bristol')
(361.1334211249548, 'Cardiff')
(348.72683849655994, 'Paris')

Last updated: Jan 2025

