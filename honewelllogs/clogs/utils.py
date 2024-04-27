from .models import Customers, Clogs


def get_customer_by_msisdn(msisdn):
    try:
        customer = Customers.objects.get(msisdn=msisdn)
        return customer
    except Exception as e:
        return None


def insert_cdr_data(cdr_file_path):
    with open(cdr_file_path, 'r') as file:
        lines = file.readline()[1:]
        for line in lines:
            data = line.split(":")

            cust_msisdn = data[0]
            customer = get_customer_by_msisdn(cust_msisdn)
            if not customer:
                customer = Customers.objects.create(msisdn=cust_msisdn)
            Clogs.objetcs.create(
                customer=customer,
                imsi=data[0],
                imei=data[1],
                plan=data[2],
                call_type=data[3],
                corresp_type=data[4],
                corresp_isdn=data[5],
                duration=data[6],
                time=data[7],
                date=data[8]
            )
