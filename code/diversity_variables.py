

def dv_get_amtliche_behinderung(survey_data_frame):

    return survey_data_frame[ survey_data_frame["q21"] == "Ja" ]


def dv_get_beeintraechtigung(survey_data_frame):

    return survey_data_frame[ survey_data_frame["q18"] == "JA" ]


def dv_get_schwerbehinderung(survey_data_frame):

    schwerbehinderung = survey_data_frame[ (not survey_data_frame["q22"].isnull()) and (survey_data_frame["q22"] >= 50) ]

    # people with Schwerbehinderung have to have ticked Behinderung
    return schwerbehinderung and dv_get_amtliche_behinderung(survey_data_frame)


def dv_get_beeintraechtigung_oder_behinderung(survey_data_frame):

    return dv_get_beeintraechtigung(survey_data_frame) or dv_get_amtliche_behinderung(survey_data_frame)


def dv_set_beeintraechtigung_oder_behinderung(survey_data_frame):

    if 'dv_beeintraechtigung_oder_behinderung' in df.columns:

        return False

    else

        survey_data_frame['dv_beeintraechtigung_oder_behinderung'] = dv_get_beeintraechtigung_oder_behinderung(survey_data_frame)

    return True
