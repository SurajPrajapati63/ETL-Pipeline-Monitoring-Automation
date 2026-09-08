import os


def get_profile_name(file_name):

    return os.path.basename(file_name).split("_")[0]


def get_procedure_name(file_name):

    return os.path.basename(file_name).split("_")[1]