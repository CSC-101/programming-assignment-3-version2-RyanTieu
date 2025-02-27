#Part 1
import data
import county_demographics
from data import CountyDemographics

#function takes in list of counties (CountyDemographics objects) and returns an integer corresponding to the sum of the 2014 population for all counties
def population_total(counties: list[data.CountyDemographics]) -> int:
    return sum(county.population.get("2014 Population", 0) for county in counties)

#Part 2
#function takes in list of counties (CountyDemographics objects) and a string corresponding to the state's abbreviation
#the function filters and returns a list of counties and their corresponding county demographics objects from the state of interest
def filter_by_state(counties: list[data.CountyDemographics], string: str) -> list[data.CountyDemographics]:
    return [value for value in counties if string in value.state == string]

#Part 3
#function takes in list of counties (CountyDemographics objects) and a string (bachelor) which corresponds to the type of education level of interest of a set of counties
#the function returns the total 2014 subpopulation for the given education level across counties (float)
def population_by_education(counties: list[CountyDemographics], bachelor: str) -> float:
    total_population = 0

    for county in counties:
        if bachelor in county.education:
            percentage = county.education.get(bachelor, 0) / 100  # Convert percentage to decimal
            total_population += county.population['2014 Population'] * percentage

    return total_population

#function takes in list of counties (CountyDemographics objects) and a string (race) which corresponds to a given ethnicity of interest of a set of counties
#the function returns the total 2014 subpopulation for a given ethnicity across counties (float)
def population_by_ethnicity(counties: list[CountyDemographics], race: str) -> float:
    race_count = 0
    for county in counties:
        if race in county.ethnicities:
            percent = county.ethnicities.get(race, 0) / 100
            race_count += county.population['2014 Population'] * percent

    return race_count

#function takes in list of counties (CountyDemographics objects) and a string (poverty) which corresponds to a given below poverty level of a set of counties
#the function returns the total 2014 subpopulation for a below poverty level across counties (float)
def population_below_poverty_level(counties: list[CountyDemographics], poverty: str) -> float:
    poverty_count = 0
    for county in counties:
        if poverty in county.income:
            percent = county.income.get('Persons Below Poverty Level', 0) / 100
            poverty_count += county.population["2014 Population"] * percent

    return poverty_count

#Part 4
#function takes in list of counties (CountyDemographics objects) and a string (percent_bachelor) which corresponds to the type of education level of interest of a set of counties
#the function calculates and returns the percentage of the population with a given education level
def percent_by_education(counties: list[CountyDemographics], percent_bachelor: str) -> float:
    pop = sum(county.population.get("2014 Population", 0) for county in counties if "2014 Population" in county.population)
    bachelor_pop = population_by_education(counties, percent_bachelor)
    if pop == 0:
        return 0.0

    return (bachelor_pop / pop) * 100

#function takes in list of counties (CountyDemographics objects) and a string (percent_ethnicity) which corresponds to the type of ethnicity of interest of a set of counties
#the function calculates and returns the percentage of the population of those corresponding ot the given ethnicity (float)
def percent_by_ethnicity(counties: list[CountyDemographics], percent_ethnicity:str) -> float:
    pop = sum(county.population.get("2014 Population", 0) for county in counties if "2014 Population" in county.population)
    ethnicity_pop = population_by_ethnicity(counties, percent_ethnicity)
    if pop == 0:
        return 0.0

    return (ethnicity_pop / pop) * 100

#function takes in list of counties (CountyDemographics objects) and a string (percent_poverty) which corresponds to the below poverty level of interest of a set of counties
#the function calculates and returns the percentage of the population of those corresponding ot the given below poverty level (float)
def percent_below_poverty_level(counties: list[CountyDemographics], percent_poverty) -> float:
    pop = sum(county.population.get("2014 Population", 0) for county in counties if "2014 Population" in county.population)
    poverty_pop = population_below_poverty_level(counties, percent_poverty)
    if pop == 0:
        return 0.0

    return(poverty_pop / pop) * 100

#Part 5
#___________________________________________________________________________________________________________________________________#
#both functions takes in list of counties (CountyDemographics objects), a string (education) corresponding to the education level of interest in a set of counties, and an upper/lower limit which represents a point of comparison for the counties whether to include in list or not(float)
#education_greater_than returns a list of counties that have a higher proportion of the population, that corresponds to the education level, than the upper limit(returns a list of CountyDemographic objects)
#education_less_than returns a list of counties that have a lower proportion of the population, that corresponds to the education level, than the lower limit(returns a list of CountyDemographic objects)

def education_greater_than(counties: list[data.CountyDemographics], education: str, lower_limit: float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.education.get(education, 0) > lower_limit]

def education_less_than(counties: list[data.CountyDemographics], education: str, upper_limit: float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.education.get(education, 0) < upper_limit]

#___________________________________________________________________________________________________________________________________#
#both functions takes in list of counties (CountyDemographics objects), a string (ethnicity) corresponding to the type of ethnicity of interest in a set of counties, and an upper/lower limit which represents a point of comparison for the counties whether to include in list or not(float)
#ethnicity_greater_than returns a list of counties that have a higher proportion of the population, that corresponds to the given ethnicity, than the lower limit(returns a list of CountyDemographic objects)
#ethnicity_less_than returns a list of counties that have a lower proportion of the population, that corresponds to the given ethnicity, than the upper limit(returns a list of CountyDemographic objects)

def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity: str, lower_limit: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity, 0) > lower_limit]

def ethnicity_less_than(counties: list[data.CountyDemographics], ethnicity: str, upper_limit: float) -> list[data.CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity, 0) < upper_limit]

#___________________________________________________________________________________________________________________________________#
#both functions takes in list of counties (CountyDemographics objects), a float(lower/upper limit) which represents a point of comparison for the counties whether to include in list or not
#below_poverty_level_greater_than returns a list of counties that have a higher proportion of the population, that corresponds to the given below poverty level, than the lower limit (returns a list of CountyDemographic objects)
#below_poverty_level_less_than returns a list of counties that have a lower proportion of the population, that corresponds to the given below poverty level, than the upper limit(returns a list of CountyDemographic objects)

def below_poverty_level_greater_than(counties: list[CountyDemographics], lower_limit:float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) > lower_limit]

def below_poverty_level_less_than(counties: list[CountyDemographics], upper_limit:float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) < upper_limit]
#___________________________________________________________________________________________________________________________________#









