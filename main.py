#!python3

import re

verzamelmap = 202200  # jaar telt op met 00 01 02 etc...
ordernummermap = 202200123  # het  verzamelmap nummer  en dan 000 tm 999

basischeck_verzamelmap = r"\d{6}"
basischeck_ordernummermap = r"(\d{6})(\d{3})"

ordernummer = "202212345"
map_2022_12 = "202212"

basismap_check_regex = re.search(basischeck_verzamelmap, map_2022_12)
output_regex_search = basismap_check_regex.group()

# print(type(output_regex_search), output_regex_search)output_regex_search

basisordernummer_check_regex = re.search(basischeck_ordernummermap, ordernummer)
output_regex_search_order = basisordernummer_check_regex.group()


# if basisordernummer_check_regex.group(1) == output_regex_search:
#     print("ok", output_regex_search,basisordernummer_check_regex.group(1))
# else:
#     print("niet ok", output_regex_search, basisordernummer_check_regex.group(1))


# print(type(output_regex_search_order), output_regex_search_order)


def check_ordernummer_met_regex_in(Jobfolder, ordernummer):
    # input is string otherwise int will be made string
    regex_search = r"(\d{4})(\d{2})(\d{3})"  # geeft drie zoek groepen
    try:
        basisordernummer_check_regex = re.search(regex_search, ordernummer)
        output_regex_search_order = basisordernummer_check_regex.group()
        jaar = basisordernummer_check_regex.group(1)
        mapnr = basisordernummer_check_regex.group(2)

        if jaar + mapnr == Jobfolder and len(Jobfolder) == 6:

            # return 0,"check1", output_regex_search_order,jaar,mapnr
            return output_regex_search_order

        else:
            return "no_match"

    except AttributeError:
        print("AttributeError: no Match")


def check_jobfolder_with_regex(jobfolder_to_check, jaar):
    # jaar optie is optioneel
    jaar = jaar
    jaar_check = r"(2022)(\d{2})"
    basischeck_verzamelmap = r"\d{6}"  # geeft 6 digits
    jobfolder_is_zes_getallen = len(jobfolder_to_check)
    try:
        jaar_test = re.search(jaar_check, jobfolder_to_check)
        if jaar_test.group(1) == str(jaar) and jobfolder_is_zes_getallen == 6:

            basismap_check_regex = re.search(basischeck_verzamelmap, jobfolder_to_check)
            output_regex_search = basismap_check_regex.group()

            return output_regex_search
        else:
            print(f"vergelijk {jaar_test.group(1)}  met {jaar}")
            print(f'aantal posities (6) van folder = {jobfolder_is_zes_getallen}')
            return 1

    except AttributeError:
        print("AttributeError: no Match")
        return 2


if __name__ == '__main__':
    print(check_jobfolder_with_regex('202200', 2022))
    print(check_jobfolder_with_regex('202100', 2022))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
