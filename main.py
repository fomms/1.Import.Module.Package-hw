from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from tqdm import tqdm
from time import sleep



if __name__ == '__main__':
    calculate_salary()
    get_employees()
    dt_obj = datetime.datetime.now()
    dt_string = dt_obj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print('Текущее время :', dt_string)

    for i in tqdm(range(100), ncols=80, ascii=True, desc='Total'):
        sleep(0.1)

