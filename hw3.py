import build_data
import data
import county_demographics
import hw3_tests


#Part 1
# This function pulls the (2014) population data from a list of counties and sum them up as a single integer.
def population_total(lst:list[build_data.CountyDemographics]) -> int:
    pop_total = 0
    for attrib in lst:
        pop_total += attrib.population['2014 Population']
    return pop_total


#Part 2
#Comment
def filter_by_state(lst:list[build_data.CountyDemographics], abrv:str) -> list[build_data.CountyDemographics]:
    key_lst = []
    for county in lst:
        if county.state == abrv:
            key_lst.append(county)
    print(key_lst)
    return key_lst


#
# #Part 3
# #Comment
def population_by_education(lst:list[build_data.CountyDemographics], edu_key:str) -> float:
    pop_edu = 0
    for county in lst:
        if edu_key in county.education:
            pop_edu += county.education[edu_key]/100 * county.population['2014 Population']
    return pop_edu

def population_by_ethnicity(lst:list[build_data.CountyDemographics], eth_key:str) -> float:
    pop_eth = 0
    for county in lst:
        if eth_key in county.ethnicities:
            pop_eth += county.ethnicities[eth_key]/100 * county.population['2014 Population']
    return pop_eth

def population_below_poverty_level(lst:list[build_data.CountyDemographics]) -> float:
    pop_eth = 0
    for county in lst:
        pop_eth += county.income['Persons Below Poverty Level']/100 * county.population['2014 Population']
    return pop_eth


# #Part 4
# #Comment
def percent_by_education(lst:list[build_data.CountyDemographics], edu_key:str) -> float:
    tot_pop = population_total(lst)
    edu_pop = population_by_education(lst, edu_key)
    percent_edu = edu_pop/tot_pop
    return percent_edu

def percent_by_ethnicity(lst:list[data.CountyDemographics], eth_key:str) -> float:
    tot_pop = population_total(lst)
    eth_pop = population_by_ethnicity(lst, eth_key)
    percent_eth = eth_pop/tot_pop
    return percent_eth

def percent_below_poverty_level(lst: list[data.CountyDemographics]) -> float:
    tot_pop = population_total(lst)
    pov_pop = population_below_poverty_level(lst)
    percent_pov = pov_pop/tot_pop
    return percent_pov


# #Part 5
# #Comment
def education_greater_than(lst:list[build_data.CountyDemographics], edu_key:str, thresh:float) -> list[data.CountyDemographics]:
    great_list = []
    for county in lst:
        if edu_key in county.education:
            if county.education[edu_key] > thresh:
                great_list.append(county)
    return great_list

def education_less_than(lst: list[build_data.CountyDemographics], edu_key: str, thresh:float) -> list[data.CountyDemographics]:
    less_list = [county for county in lst if edu_key in county.education and county.education[edu_key] < thresh]
    return less_list


def ethnicity_greater_than(lst: list[build_data.CountyDemographics], eth_key: str, thresh:float) -> list[data.CountyDemographics]:
    great_list = [county for county in lst if eth_key in county.ethnicities and county.ethnicities[eth_key] > thresh]
    return great_list

def ethnicity_less_than(lst: list[data.CountyDemographics], eth_key: str, thresh:float) -> list[data.CountyDemographics]:
    less_list = [county for county in lst if eth_key in county.ethnicities and county.ethnicities[eth_key] < thresh]
    return less_list


def below_poverty_level_greater_than(lst:list[data.CountyDemographics], thresh:float) -> list[data.CountyDemographics]:
    great_list = [county for county in lst if county.income['Persons Below Poverty Level'] > thresh]
    return great_list

def below_poverty_level_less_than(lst: list[data.CountyDemographics], thresh: float) -> list[data.CountyDemographics]:
    less_list = [county for county in lst if county.income['Persons Below Poverty Level'] < thresh]
    return less_list