import data
import county_demographics

#Part 1
#Comment
def population_total(lst:list[data.CountyDemographics]) -> int:


#Part 2
#Comment
def filter_by_state(lst:list[data.CountyDemographics], abrv:str) -> list[data.CountyDemographics]:

#Part 3
#Comment
def population_by_education(lst:list[data.CountyDemographics], edu_key:str) -> float:

def population_by_ethnicity(lst:list[data.CountyDemographics], eth_key:str) -> float:

def population_below_poverty_level(lst:list[data.CountyDemographics]) -> float:

#Part 4
#Comment
def percent_by_education(lst:list[data.CountyDemographics], edu_key:str) -> float:

def percent_by_ethnicity(lst:list[data.CountyDemographics], eth_key:str) -> float:

def percent_below_poverty_level(lst: list[data.CountyDemographics]) -> float:

#Part 5
#Comment
def education_greater_than(lst:list[data.CountyDemographics], edu_key:str, thresh:float) -> list[data.CountyDemographics]:

def education_less_than(lst: list[data.CountyDemographics], edu_key: str, thresh:float) -> list[data.CountyDemographics]:


def ethnicity_greater_than(lst: list[data.CountyDemographics], eth_key: str, thresh:float) -> list[data.CountyDemographics]:

def ethnicity_less_than(lst: list[data.CountyDemographics], eth_key: str, thresh:float) -> list[data.CountyDemographics]:


def below_poverty_level_greater_than(lst:list[data.CountyDemographics], thresh:float) -> list[data.CountyDemographics]:

def below_poverty_level_less_than(lst: list[data.CountyDemographics], thresh: float) -> list[data.CountyDemographics]:
