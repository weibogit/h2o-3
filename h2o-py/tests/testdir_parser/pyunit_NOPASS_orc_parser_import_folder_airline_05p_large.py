from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils


def import_folder():
    """
    This test will build a H2O frame from importing the bigdata/laptop/parser/orc/airlines_05p_orc_csv
    from and build another H2O frame from the multi-file orc parser using multiple orc files that are
    saved in the directory bigdata/laptop/parser/orc/airlines_05p_orc.  It will compare the two frames
    to make sure they are equal.
    :return: None if passed.  Otherwise, an exception will be thrown.
    """

    data_types = ['real','real','real','real','real','real','real','real','enum','real','enum','real','real','enum',
                  'real','real','enum','enum','real','enum','enum','real','enum','real','enum','enum','enum','enum',
                  'enum','enum','enum']

    multi_file_csv = h2o.import_file(path=pyunit_utils.locate("bigdata/laptop/parser/orc/pubdev_3200/air05_csv"),
                                     col_types=data_types)
    multi_file_csv.summary()
    csv_summary = h2o.frame(multi_file_csv.frame_id)["frames"][0]["columns"]

    multi_file_orc = h2o.import_file(path=pyunit_utils.locate("bigdata/laptop/parser/orc/pubdev_3200/air05_orc"),
                                     col_types=data_types)
    multi_file_orc.summary()
    orc_summary = h2o.frame(multi_file_orc.frame_id)["frames"][0]["columns"]

    pyunit_utils.compare_frame_summary(csv_summary, orc_summary)


if __name__ == "__main__":
    pyunit_utils.standalone_test(import_folder)
else:
    import_folder()
