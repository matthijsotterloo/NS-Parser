import xml.etree.cElementTree as ET
import datetime
import pytz


def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    trein_locations = map(TreinLocation.parse_trein_location, root.findall('TreinLocation'))
    return trein_locations

class TreinLocation(object):
    """
    TreinLocation beschrijft de locatie van een trein,
    Een trein kan uit meerdere materieeldelen bestaan die ieder een eigen GPS locatie heeft
    """

    trein_nummer = None # Correspondeert met het treinnummer uit InfoPlus DVS
    trein_materieel_delen = []

    def __init__(self):
        pass

    def get_lat_lon(self):
        return trein_materieel_delen[0].latitude, trein_materieel_delen[0].longitude

    def __repr__(self):
        return '<Trein %s:\t%s>' % (self.trein_nummer, ' '.join(map(repr, self.trein_materieel_delen)))

    @staticmethod
    def parse_trein_location(data):
        ns = 'http://schemas.datacontract.org/2004/07/Cognos.Infrastructure.Models'

        trein_location = TreinLocation()

        trein_location.trein_nummer = data.find('{%s}TreinNummer' % ns).text
        trein_location.trein_materieel_delen = map(TreinMaterieelDeel.parse_trein_materieel_deel, data.findall('{%s}TreinMaterieelDelen' % ns))

        return trein_location


class TreinMaterieelDeel(object):
    materieel_deel_nummer = None
    materieel_volgnummer = None
    generatie_tijd = None
    gps_datum_tijd = None
    orientatie = 0
    bron_id = None
    bron = None
    fix = 0
    berichttype = 0
    longitude = None
    latitude = None
    snelheid = 0
    richting = 0
    rijrichting = 0
    hdop = 0
    aantal_satellieten = 0

    def __repr__(self):
        return '%.5f,%.5f' % (self.latitude, self.longitude)

    @staticmethod
    def parse_trein_materieel_deel(data):
        ns = 'http://schemas.datacontract.org/2004/07/Cognos.Infrastructure.Models'

        deel = TreinMaterieelDeel()
        deel.materieel_deel_nummer = int(data.find('{%s}MaterieelDeelNummer' % ns).text)
        deel.materieel_volgnummer = int(data.find('{%s}Materieelvolgnummer' % ns).text)
        deel.generatie_tijd = pytz.utc.localize(datetime.datetime.utcfromtimestamp(int(data.find('{%s}GeneratieTijd' % ns).text)))

        if data.find('{%s}GpsDatumTijd' % ns).text is not None:
            deel.gps_datum_tijd = pytz.utc.localize(datetime.datetime.strptime(data.find('{%s}GpsDatumTijd' % ns).text[:19], '%Y-%m-%dT%H:%M:%S'))

        deel.orientatie = int(data.find('{%s}Orientatie' % ns).text)
        deel.bron_id = int(data.find('{%s}BronId' % ns).text)
        deel.bron = int(data.find('{%s}Bron' % ns).text)
        deel.fix = int(data.find('{%s}Fix' % ns).text)
        deel.berichttype = int(data.find('{%s}Berichttype' % ns).text)
        deel.longitude = float(data.find('{%s}Longitude' % ns).text)
        deel.latitude = float(data.find('{%s}Latitude' % ns).text)
        deel.snelheid = float(data.find('{%s}Snelheid' % ns).text)
        deel.richting = float(data.find('{%s}Richting' % ns).text)
        deel.rijrichting = int(data.find('{%s}Rijrichting' % ns).text)
        deel.hdop = float(data.find('{%s}Hdop' % ns).text)
        deel.aantal_satellieten = int(data.find('{%s}AantalSatelieten' % ns).text) # geen typo, spelfout zit in de XML spec

        return deel
