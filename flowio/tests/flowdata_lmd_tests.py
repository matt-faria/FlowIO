import unittest
from flowio import FlowData


class FlowDataLMDTestCase(unittest.TestCase):
    def setUp(self):
        self.flow_data = FlowData('examples/fcs_files/coulter.lmd')
        
    def test_get_points(self):
        self.assertEqual(
            len(self.flow_data.events) / self.flow_data.channel_count,
            int(self.flow_data.text['tot']))

    def test_get_text(self):
        self.assertEqual(self.flow_data.text['cyt'], 'Cytomics FC 500')
