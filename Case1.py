import csv

def calculate_average(file_name):
    # Buka csv dan dia akan membaca datanya
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Tetapkan initial total ke 0
        total = 0
        # Tetapkan initial menghitung ke 0 
        count = 0
        # Pengulangan atas setiap baris data
        for row in csv_reader:
            # Tambahkan nilai di kedua kolom ke total
            total += float(row[1])
            # Kenaikan 
            count += 1
        # Menghitung rata rata 
        average = total / count
        # Membalikan nilai rata rata
        return average
    
if __name__ == "__main__":
    # Memanggil penghitungan rata rata fungsi dan mencetak hasilnya
    average = calculate_average("data.csv")
    print("Average value : {} ".format(average))