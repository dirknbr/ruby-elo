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

(491.7393820436823, 'Toulouse')
(471.5175198369161, 'Leinster')
(463.05373882349477, 'Northampton')
(435.50149732945147, 'Bordeaux')
(427.22314710699015, 'Harlequins')
(422.08086045263985, 'Rochelle')
(411.04301386019995, 'Saracens')
(404.42058562219955, 'Stormers')
(401.5146435594213, 'Clermont')
(401.1144929189108, 'Bayonne')
(401.0666872973635, 'Castres')
(400.38879611873006, 'Bulls')
(400.23488624997265, 'Benetton')
(399.9851390263065, 'Exeter')
(399.18314175532794, 'Sharks')
(390.01741764269366, 'Lyon')
(389.95657300174827, 'Glasgow')
(387.92739923646764, 'Bath')
(383.8120971895156, 'Toulon')
(381.2654320705041, 'Sale')
(381.14907129541183, 'Connacht')
(374.86637468334203, 'Leicester')
(374.0038806588734, 'Racing')
(373.21079736446137, 'Munster')
(365.31790037529976, 'Ulster')
(362.7668973723097, 'Bristol')
(361.1334211249548, 'Cardiff')
(344.50520598281076, 'Paris')

Last updated: Dec 2024

