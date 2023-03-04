from parser import *

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf
    # Wang_QC_Recognition_of_camouflage_targets_with_hyper-spectral_polarization_imaging_system.pdf
    file_parser = Parser('Zhai_H_Infrared_polarization_detection_method_for_weak_target_in_sky_background.pdf')
    pdf = file_parser.get_text()

    for page in pdf:
        print(page)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
