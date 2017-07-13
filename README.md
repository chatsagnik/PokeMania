# PokeMania
This is an exploratory analysis of various Pokemon traits

## Source
Alberto Barradas' [dataset on Pokemon](https://www.kaggle.com/abcsds/pokemon) uploaded at Kaggle. 

## Features of the Dataset
* **#**: ID for each pokemon
* **Name**: Name of each pokemon
* **Type 1**: Each pokemon has a type, this determines weakness/resistance to attacks
* **Type 2**: Some pokemon are dual type and have 2
* **Total**: sum of all stats that come after this, a general guide to how strong a pokemon is
* **HP**: hit points, or health, defines how much damage a pokemon can withstand before fainting
* **Attack**: the base modifier for normal attacks (eg. Scratch, Punch)
* **Defense**: the base damage resistance against normal attacks
* **SP Atk**: special attack, the base modifier for special attacks (e.g. fire blast, bubble beam)
* **SP Atk**: the base damage resistance against special attacks
* **SP Atk**: determines which pokemon attacks first each round
* **Generation**: the generation this pokemon belongs to
* **Legendary**: True indicates this pokemon is legendary, False indicates it is not

## My Aims
* See how the average pokemon of a given type compates against average pokemon of other types. Draw inferences from this.
* See how the average dual-type pokemon stacks up against single-type pokemons. Draw inferences from this.
* Plot the distribution of dual-types across different generations.
* Find which types are most frequently grouped together in dual-type pokemons.
* Find which types are least frequently grouped together in dual-type pokemons.
* See how the average Legendary type Pokemon stack up against the average non-legendary type Pokemon.
* Given the base stats(HP, attack,defense,sp.attack,sp.def and speed) of a new Pokemon, try to predict which types it will most likely fall in.

## Results (plotting via matplotlib)

### Stat comparisons among various types
#### Hitpoint comparisons across various types
![Comparison of HP across Types ](/StatsComparisons/hp.png?raw=true)
#### Attack comparisons across various types
![Comparison of ATK across Types ](/StatsComparisons/atk.png?raw=true)
#### Defense comparisons across various types
![Comparison of DEF across Types ](/StatsComparisons/def.png?raw=true)
#### Special Attack comparisons across various types
![Comparison of SPATK across Types ](/StatsComparisons/spatk.png?raw=true)
#### Special Defense comparisons across various types
![Comparison of SPDEF across Types ](/StatsComparisons/spdef.png?raw=true)
#### Speed comparisons across various types
![Comparison of SPEED across Types ](/StatsComparisons/spd.png?raw=true)
