import csv
from django.core.management.base import BaseCommand, CommandError
from myapp.models import Person99
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import Person99 data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path.')

    def handle(self, *args, **options):
        path = options['csv_file_path']

        try:
            # with open(path, 'r', encoding='utf-8') as csvfile:
            with open(path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    Person99.objects.create(
                        parent_id=int(row['parent_id']) if row['parent_id'] else None,
                        birth_date=parse_date(row['birth_date']),
                        gender_id=int(row['gender_id']),
                        postal_code=row['postal_code'],
                        province_name=row['province_name'],
                        county_name=row['county_name'],
                        is_urban=row['is_urban'].lower() in ['true', '1'],
                        am_creditor_95=int(row['am_creditor_95']),
                        am_debtor_95=int(row['am_debtor_95']),
                        first_prd_95=int(row['first_prd_95']),
                        last_prd_95=int(row['last_prd_95']),
                        sm_benefit_95=int(row['sm_benefit_95']),
                        am_creditor_96=int(row['am_creditor_96']),
                        am_debtor_96=int(row['am_debtor_96']),
                        first_prd_96=int(row['first_prd_96']),
                        last_prd_96=int(row['last_prd_96']),
                        sm_benefit_96=int(row['sm_benefit_96']),
                        am_creditor_97=int(row['am_creditor_97']),
                        am_debtor_97=int(row['am_debtor_97']),
                        first_prd_97=int(row['first_prd_97']),
                        last_prd_97=int(row['last_prd_97']),
                        sm_benefit_97=int(row['sm_benefit_97']),
                        am_creditor_98=int(row['am_creditor_98']),
                        am_debtor_98=int(row['am_debtor_98']),
                        first_prd_98=int(row['first_prd_98']),
                        last_prd_98=int(row['last_prd_98']),
                        sm_benefit_98=int(row['sm_benefit_98']),
                        card98_rials=int(row['card98_rials']),
                        card98_paymentcount=int(row['card98_paymentcount']),
                        card99_rials=int(row['card99_rials']),
                        card99_paymentcount=int(row['card99_paymentcount']),
                        is_bimar_khas=row['is_bimar_khas'].lower() in ['true', '1'],
                        is_malool=row['is_malool'].lower() in ['true', '1'],
                        is_bime_pardaz_sandoghha=row['is_bime_pardaz_sandoghha'].lower() in ['true', '1'],
                        is_bazneshaste_sandoghha=row['is_bazneshaste_sandoghha'].lower() in ['true', '1'],
                        is_maliati_shaghel=row['is_maliati_shaghel'].lower() in ['true', '1'],
                        daramad_total_rials=int(row['daramad_total_rials']),
                        cars_count=int(row['cars_count']),
                        cars_price_sum=int(row['cars_price_sum']),
                        trips_count_air_not_pilgrimage=int(row['trips_count_air_not_pilgrimage']),
                        trips_count_not_air_not_pilgrimage=int(row['trips_count_not_air_not_pilgrimage']),
                        trips_count_air_pilgrimage=int(row['trips_count_air_pilgrimage']),
                        trips_count_not_air_pilgrimage=int(row['trips_count_not_air_pilgrimage']),
                        has_mojavez_senfi=row['has_mojavez_senfi'].lower() in ['true', '1'],
                        senf=row['senf'] if row['senf'] else None,
                        has_bime_salamat=row['has_bime_salamat'].lower() in ['true', '1'],
                        bime_salamat_type=row['bime_salamat_type'] if row['bime_salamat_type'] else None,
                    )

                self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % path))
        except FileNotFoundError:
            raise CommandError('File "%s" does not exist' % path)
        except Exception as e:
            raise CommandError('Error processing file: %s' % str(e))
