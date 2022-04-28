from main import check_jobfolder_with_regex, check_ordernummer_met_regex_in


def test_check_jobfolder_with_regex():
    test = check_jobfolder_with_regex("202100", "2022")
    result = "202200"
    test2 = check_jobfolder_with_regex("202200", "2022")
    result2 = "202200"
    # assert test == result2
    assert test2 == result2


def test_check_ordernummer_met_regex_in():
    test = check_ordernummer_met_regex_in("2022012","202200234")
    result = "202200234"
    assert test == result