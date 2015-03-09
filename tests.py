import unittest, datetime, ns_gps_parser, pytz

class TestParseXML(unittest.TestCase):

    def test_parse_file(self):
        xml = open('test_location/test.xml').read()
        trein_locations = ns_gps_parser.parse_xml(xml)

        self.assertIsNotNone(trein_locations)
        self.assertEquals(len(trein_locations), 327)

        tl = trein_locations[0].trein_materieel_delen[0]

        self.assertEquals(tl.materieel_deel_nummer, 8615)
        self.assertEquals(tl.materieel_volgnummer, 1)
        self.assertEquals(tl.generatie_tijd, pytz.utc.localize(datetime.datetime(2015, 3, 9, 16, 43, 57)))
        self.assertEquals(tl.gps_datum_tijd, pytz.utc.localize(datetime.datetime(2015, 3, 9, 16, 43, 56)))
        self.assertEquals(tl.orientatie, 0)
        self.assertEquals(tl.bron_id, 0)
        self.assertEquals(tl.bron, 1)
        self.assertEquals(tl.fix, 1)
        self.assertEquals(tl.berichttype, 1)
        self.assertAlmostEquals(tl.longitude, 5.212845)
        self.assertAlmostEquals(tl.latitude, 52.0637616667)
        self.assertEquals(tl.snelheid, 138.0)
        self.assertEquals(tl.richting, 86.82)
        self.assertEquals(tl.rijrichting, 0)
        self.assertEquals(tl.hdop, 0.9)
        self.assertEquals(tl.aantal_satellieten, 9)

"""
<GeneratieTijd>1425919437</GeneratieTijd>
<GpsDatumTijd>2015-03-09T16:43:56</GpsDatumTijd>
<Orientatie>0</Orientatie><BronId>0</BronId><Bron>1</Bron><Fix>1</Fix><Berichttype>1</Berichttype><Longitude>5.212845</Longitude><Latitude>52.0637616667</Latitude><Snelheid>138</Snelheid><Richting></Richting><Rijrichting>0</Rijrichting><Hdop>0.9</Hdop><AantalSatelieten>9</AantalSatelieten></TreinMaterieelDelen><TreinMaterieelDelen xmlns="http://schemas.datacontract.org/2004/07/Cognos.Infrastructure.Models"><MaterieelDeelNummer>9427</MaterieelDeelNummer><Materieelvolgnummer>2</Materieelvolgnummer><GeneratieTijd>1425919441</GeneratieTijd><GpsDatumTijd>2015-03-09T16:44:00</GpsDatumTijd><Orientatie>0</Orientatie><BronId>0</BronId><Bron>1</Bron><Fix>1</Fix><Berichttype>1</Berichttype><Longitude>5.21351666667</Longitude><Latitude>52.0637866667</Latitude><Snelheid>138</Snelheid><Richting>86.74</Richting><Rijrichting>0</Rijrichting><Hdop>1.2</Hdop><AantalSatelieten>7</AantalSatelieten></TreinMaterieelDelen></TreinLocation><TreinLocation><TreinNummer xmlns="http://schemas.datacontract.org/2004/07/Cognos.Infrastructure.Models">12763</TreinNummer><TreinMaterieelDelen xmlns="http://schemas.datacontract.org/2004/07/Cognos.Infrastructure.Models"><MaterieelDeelNummer>8739</MaterieelDeelNummer><Materieelvolgnummer>2</Materieelvolgnummer><GeneratieTijd>1425919406</GeneratieTijd><GpsDatumTijd>2015-03-09T16:43:25</GpsDatumTijd><Orientatie>0</Orientatie><BronId>0</BronId><Bron>1</Bron><Fix>1</Fix><Berichttype>1</Berichttype><Longitude>4.87185</Longitude><Latitude>52.338805</Latitude><Snelheid>0</Snelheid><Richting>130.81</Richting><Rijrichting>0</Rijrichting><Hdop>0.9</Hdop><AantalSatelieten>9</AantalSatelieten></TreinMaterieelDelen>
"""
if __name__ == '__main__':
    unittest.main()
