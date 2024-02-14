import csv
from django.core.management.base import BaseCommand, CommandError
from householder_app.models import Person99
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import Person99 data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path.')

    def handle(self, *args, **options):
        path = options['csv_file_path']

        try:
            with open(path, 'r', encoding='latin-1') as csvfile:
            # with open(path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    Person99.objects.create(
                        ParentID=int(row['ParentID']),
                        BirthDate=parse_date(row['BirthDate']),
                        GenderId=int(row['GenderId']),
                        postalcode=row['postalcode'],
                        Provincename=row['Provincename'],
                        countyname=row['countyname'],
                        isurban=row['isurban'],

                        AmCrdtr_95=int(row['AmCrdtr_95']),
                        Amdbtr_95=int(row['Amdbtr_95']),
                        frstPrd_95=int(row['frstPrd_95']),
                        lstPrd_95=int(row['lstPrd_95']),
                        SmBnft_95=int(row['SmBnft_95']),
                        
                        AmCrdtr_96=int(row['AmCrdtr_96']),
                        Amdbtr_96=int(row['Amdbtr_96']),
                        frstPrd_96=int(row['frstPrd_96']),
                        lstPrd_96=int(row['lstPrd_96']),
                        SmBnft_96=int(row['SmBnft_96']),
                        
                        AmCrdtr_97=int(row['AmCrdtr_97']),
                        Amdbtr_97=int(row['Amdbtr_97']),
                        frstPrd_97=int(row['frstPrd_97']),
                        lstPrd_97=int(row['lstPrd_97']),
                        SmBnft_97=int(row['SmBnft_97']),
                        
                        AmCrdtr_98=int(row['AmCrdtr_98']),
                        Amdbtr_98=int(row['Amdbtr_98']),
                        frstPrd_98=int(row['frstPrd_98']),
                        lstPrd_98=int(row['lstPrd_98']),
                        SmBnft_98=int(row['SmBnft_98']),
                        
                        Card98_Rials=int(row['Card98_Rials']),
                        Card98_PaymentCount=int(row['Card98_PaymentCount']),

                        Card99_Rials=int(row['Card99_Rials']),
                        Card99PaymentCount=int(row['Card99PaymentCount']),
                        
                        IsBiamrKhas=int(row['IsBiamrKhas']),
                        IsMalool=int(row['IsMalool']),
                        IsBimePardaz_Sandoghha=int(row['IsBimePardaz_Sandoghha']),
                        IsBazneshaste_Sandoghha=int(row['IsBazneshaste_Sandoghha']),
                        
                        IsMaliati_Shaghel=int(row['IsMaliati_Shaghel']),
                        daramad_Total_Rials=int(row['daramad_Total_Rials']),
                        
                        Cars_Count=int(row['Cars_Count']),
                        CarsPrice_Sum=int(row['CarsPrice_Sum']),
                        
                        Trips_Count_AirNotPilgrimage=int(row['Trips_Count_AirNotPilgrimage']),
                        Trips_Count_NotAirNotPilgrimage=int(row['Trips_Count_NotAirNotPilgrimage']),
                        Trips_Count_AirPilgrimage=int(row['Trips_Count_AirPilgrimage']),
                        Trips_Count_NotAirPilgrimage=int(row['Trips_Count_NotAirPilgrimage']),
                        
                        HasMojavezSenfi=int(row['HasMojavezSenfi']),
                        Senf=row['Senf'],
                        HasBimeSalamat=int(row['HasBimeSalamat']),
                        BimeSalmat_Type=row['BimeSalmat_Type']
                    )

                self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % path))
        except FileNotFoundError:
            raise CommandError('File "%s" does not exist' % path)
        except Exception as e:
            print()
            raise CommandError('Error processing file: %s' % str(e))
