# Evengelos Kontopantelis, David Reeves, Jose M Valderas, Stephen Campbell, Tim Doran, 2024.

import sys, csv, re

codes = [{"code":"14A7.12","system":"readv2"},{"code":"14A7.00","system":"readv2"},{"code":"7P24200","system":"readv2"},{"code":"G652.00","system":"readv2"},{"code":"F423600","system":"readv2"},{"code":"14AK.00","system":"readv2"},{"code":"G64z111","system":"readv2"},{"code":"662e.00","system":"readv2"},{"code":"4369B","system":"readv2"},{"code":"4369BN","system":"readv2"},{"code":"4389PP","system":"readv2"},{"code":"4360B","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('stroke-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["stroke---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["stroke---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["stroke---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
