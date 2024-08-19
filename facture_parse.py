#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import datetime
from dataclasses import dataclass

FACTURE_PATH = "/home/jguerinel/Perso/Docs/Documents/Maison/factures"
PRET_RESTANT = 10000.0

@dataclass
class Facture:
    """Class to keep track of a facture."""
    date: datetime
    origin: str
    desc: str
    account: str
    price: float
    
    def _to_list(self):
        return [self.date.strftime("%Y/%m/%d"), self.origin, self.desc, self.account, f_to_str(self.price)]
    
def convert_value(value: str) -> float:
    values = value.split("-")
    val = 0.0
    
    for idx, v in enumerate(values):
        val += float(v) / pow(100, idx)
    
    return val

def f_to_str(value: float) -> str:
    return str(value).replace(".", ",")

def totals(factures: list) -> tuple(float, float):
    total = sum([f.price for f in factures])
    
    due = total - PRET_RESTANT
    
    return total, due    

def load_factures_from(fpath: str) -> list:
    factures = []
    for path in os.listdir(fpath):
        full_path = os.path.join(fpath, path)
        if os.path.isfile(full_path) and full_path.endswith('.pdf'):
            values = path.replace('.pdf', '').split("_")

            f = Facture(datetime.datetime.strptime(values[0], '%Y-%m-%d'),
                        values[1],
                        values[2],
                        values[3],
                        convert_value(values[4]))
            
            factures.append(f)
    
    return factures

def write_into_file(filename: str, factures: list):
    header = ['date', 'origin', 'desc', 'account', 'price']
    
    print(f"Write {len(factures)} factures into {filename}")
    
    with open(filename, 'w', encoding='UTF8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        
        for f in factures:
            writer.writerow(f._to_list())
            
        writer.writerow([""])
        total, due = totals(factures)
        writer.writerow(["total:", f_to_str(total), "share:", f_to_str(due)])
    

if __name__ == '__main__':
    
    factures = load_factures_from(FACTURE_PATH)

    total, due = totals(factures)
    print(f"total={total}")
    print(f"due={due}")

    write_into_file(f'{FACTURE_PATH}_all.csv', factures)