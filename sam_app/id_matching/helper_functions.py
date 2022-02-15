import fuzzymatcher as fm

"""Example helper functions - to be ignored"""

def checkDuplicateCompanyNameIdKeepFirst(df):
    """
    input: dataframe
    return: dataframe remove duplicates rows with same id and keep first
    """
    if df[df.duplicated(subset=['id', 'name'], keep=False)].shape[0] !=0:
        df= df.drop_duplicates(subset =["id","name"], keep='first')
    else:
        df=df
    return df

def checkDuplicateCompanyNameIdKeepLast(df):
    """
    input: dataframe
    return: dataframe remove duplicates rows with same name and id and keep first
    """
    if df[df.duplicated(subset=['id', 'name'], keep=False)].shape[0]!=0:
        df= df.drop_duplicates(subset =["id","name"], keep='last')
    else:
        df=df
    return df

def checkDuplicateCompanyNameKeepFirst(df):
    """
    input: dataframe
    return: dataframe remove duplicates rows with same name and keep first
    """
    if df[df.duplicated(subset=['name'], keep=False)].shape[0]!=0:
        df= df.drop_duplicates(subset ="name", keep='first')
    else:
        df=df
    return df

def checkDuplicateCompanyNameKeepLast(df):
    """
    input: dataframe
    return: dataframe remove duplicates rows with same name and keep last
    """
    if df[df.duplicated(subset=['name'], keep=False)].shape[0]!=0:
        df= df.drop_duplicates(subset ="name", keep='last')
    else:
        df=df
    return df

def checkDuplicateCompanyIdKeepFirst(df):
    """
    input: dataframe
    return: dataframe remove duplicates rows with same id and keep first
    """
    if df[df.duplicated(subset=['id'], keep=False)].shape[0]!=0:
        df=df.drop_duplicates(subset ="id", keep='first')
    else:
        df=df
    return df

def checkDuplicateCompanyIdKeepLast(df):
    """
    input: dataframe
    return: dataframe remove duplicates rows with same id and keep last
    """
    df=df
    if df[df.duplicated(subset=['id'], keep=False)].shape[0]!=0:
        df=df.drop_duplicates(subset =["id"], keep='last')
    else:
        df=df
    return df

def remove_start_end_spaces(df):
    """
    input: dataframe
    return: dataframe remove strip trailing space
    """
    df = df
    return df.str.strip()

def fuzzyMatcher(df_left,df_right,left_col,right_col):
    """
    INPUT: define columns left and right to match
    return: dataframe with match score and join of 2 dataframe on defined columns
    """
    # Columns to match on from df_left
    left_on = [left_col]
    # Columns to match on from df_right
    right_on = [right_col]
    # Now perform the match
    matched_results = fm.fuzzy_left_join(df_left, df_right,left_on,right_on)
    return matched_results

def clean_phase1(df):
    """
    input: dataframe
    return: dataframe with remove duplicates
    """
    ## cleaning 1: search duplicate on id and keep last
    df_clean1 = checkDuplicateCompanyIdKeepLast(df)
    ## cleaning 2: search duplicate on name and keep first
    df_clean2 = checkDuplicateCompanyNameKeepFirst(df_clean1)
    return df_clean2

def clean_phase2(df):
    """
    input: dataframe
    return: dataframe with remove duplicates
    """
    ## cleaning 3: search duplicates on company id and company name and keep first
    df_clean3 = checkDuplicateCompanyNameIdKeepFirst(df)
    ## cleaning 4: search duplicate on name and keep last
    df_clean4 = checkDuplicateCompanyNameKeepLast(df_clean3)
    return df_clean4