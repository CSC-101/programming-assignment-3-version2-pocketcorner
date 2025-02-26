import build_data
import data
import county_demographics

#Part 1
# This function pulls the (2014) population data from a list of counties and sum them up as a single integer.
def population_total(lst:list[build_data.CountyDemographics]) -> int:
    pop_total = 0
    for attrib in lst:
        pop_total += attrib['Population']['2014 Population']
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


# def population_by_ethnicity(lst:list[data.CountyDemographics], eth_key:str) -> float:
#
# def population_below_poverty_level(lst:list[data.CountyDemographics]) -> float:
#
#
# #Part 4
# #Comment
# def percent_by_education(lst:list[data.CountyDemographics], edu_key:str) -> float:
#
# def percent_by_ethnicity(lst:list[data.CountyDemographics], eth_key:str) -> float:
#
# def percent_below_poverty_level(lst: list[data.CountyDemographics]) -> float:
#
#
# #Part 5
# #Comment
# def education_greater_than(lst:list[data.CountyDemographics], edu_key:str, thresh:float) -> list[data.CountyDemographics]:
#
# def education_less_than(lst: list[data.CountyDemographics], edu_key: str, thresh:float) -> list[data.CountyDemographics]:
#
#
# def ethnicity_greater_than(lst: list[data.CountyDemographics], eth_key: str, thresh:float) -> list[data.CountyDemographics]:
#
# def ethnicity_less_than(lst: list[data.CountyDemographics], eth_key: str, thresh:float) -> list[data.CountyDemographics]:
#
#
# def below_poverty_level_greater_than(lst:list[data.CountyDemographics], thresh:float) -> list[data.CountyDemographics]:
#
# def below_poverty_level_less_than(lst: list[data.CountyDemographics], thresh: float) -> list[data.CountyDemographics]:
