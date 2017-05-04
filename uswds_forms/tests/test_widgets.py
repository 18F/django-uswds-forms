import datetime
from uswds_forms.date import SplitDateWidget

def test_split_date_widget_decompress():
    w = SplitDateWidget()
    d = datetime.date(2017, 5, 4)
    assert w.decompress(d) == [2017, 5, 4]
