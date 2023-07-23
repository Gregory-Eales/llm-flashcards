import csv

def csv_to_anki(input_csv, output_txt):
    with open(input_csv, 'r') as csv_file, open(output_txt, 'w') as txt_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == 'concept':
                continue
            front = row[0]
            back = row[1]
            txt_file.write(f"{front};{back}\n")

csv_to_anki('data/mental-models.csv', 'data/anki-cards.txt')