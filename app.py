import streamlit as st
import webbrowser

st.set_page_config(page_title='r/ Python', page_icon='🐧', layout="centered", initial_sidebar_state="auto", menu_items=None)

# SIDEBAR START
with st.sidebar:
    st.header('Sedikit review sj')
    option = st.selectbox(' ', ['Algorithm', 'Basics Python', 'Cheatsheet', 'Classes (OOP)', 'Exercise'], index=1,label_visibility='collapsed')

    if option == 'Algorithm':
        menu = st.selectbox(
        "Choose algorithm: ",
        ["Recursive", "Searching", "Sorting", "Swap Variable"])

    elif option == 'Basics Python':
        menu = st.selectbox('Choose basics', ['Arithmetic Expression', 'Boolean Algebra','Conditional Statement (IF-ELSE)','Datatype (STR/INT/FLOAT)', 'Data Structure (List/Tuple/Set/Dict)','Function (DEF)', 'Input/Output','Looping (FOR/WHILE)','Modules'], index=3)

    elif option == 'Exercise':
        menu = st.selectbox('Choose difficulty', ['Pro', 'Pro Max', 'Super Pro Max'])

    with st.expander('Daftar Isi'):
        st.write('''
    - Algorithm
        - Recursive
        - Searching
        - Sorting
    - Basics Python
        - Arithmetic Expression
        - Boolean Algebra
        - Conditional Statement
        - Datatype
        - Data Structure
        - Function
        - Input/Output
        - Looping
        - Modules
    - Cheatsheet
    - Classes (OOP)
    - Excercise   
        - Pro
        - Pro Max
        - Super Pro Max
    ''')
    
    st.caption('''
    made with 😎, python, n streamlit by [/az](https://github.com/rhmdziz)
    update 29 April 2023 ''')
    # st.caption('maaf masih pemula 🙏')
# SIDEBAR END


# ALGORITHM
if option == 'Algorithm':

    # RECURSIVE ALGORITHM START
    if menu == 'Recursive':
        st.header('Recursive Algorithm w/ Python')
        st.write('''
        > Rekursif adalah algoritma yang memecahkan masalah dengan cara memecahnya menjadi submasalah yang lebih kecil, kemudian menyelesaikan setiap submasalah secara terpisah. Pada dasarnya, algoritma rekursif adalah algoritma yang :red[memanggil dirinya sendiri] untuk menyelesaikan masalah.

        Dalam implementasi algoritma rekursif, perlu diperhatikan bahwa setiap panggilan rekursif harus memiliki kasus dasar atau base case yang memberhentikan pemanggilan rekursif dan mengembalikan nilai tertentu secara langsung. Tanpa kasus dasar ini, algoritma akan terus memanggil dirinya sendiri sehingga menyebabkan stack overflow atau kehabisan memori.

        ##### Example 1
        ''')
        st.code('''
        def faktorial(n):
            if n == 0:
                return 1
            else:
                return n * faktorial(n-1) # memanggil dirinya sendiri
        ''')
        with st.expander('See code explanation'):
            st.write('''
            Seperti yg kita tahu, faktorial dari bilangan n didefinisikan sebagai hasil perkalian semua bilangan bulat positif yang kurang dari atau sama dengan n. Secara matematis, faktorial dapat ditulis sebagai `n! = 1 x 2 x 3 x ... x (n-1) x n.`

            Dalam implementasi kode di atas, terdapat dua kondisi dalam fungsi faktorial.
            1. Jika nilai n sama dengan 0, maka fungsi akan mengembalikan nilai 1 karena 0! = 1
            2. Jika nilai n tidak sama dengan 0, maka fungsi akan mengembalikan nilai n dikali dengan nilai faktorial dari n-1, sampai mendapatkan n = 0

            Contohnya, jika kita memanggil fungsi `faktorial(5)`, maka akan mengembalikan nilai `5 x 4 x 3 x 2 x 1 = 120`
            ''')
        st.write('''        
        ##### Example 2''')

        st.code('''
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return (fibonacci(n-1) + fibonacci(n-2))
        ''')
        with st.expander('See code explanation:'):
            st.write('''
            Fungsi `fibonacci` tersebut menerima satu parameter, yaitu `n`, yang merupakan bilangan bulat positif. Fungsi ini mengembalikan nilai dari bilangan Fibonacci ke-n.

            Pada setiap pemanggilan fungsi, pertama-tama akan diperiksa apakah nilai `n` kurang dari atau sama dengan 1. Jika ya, maka nilai n tersebut akan dikembalikan langsung sebagai hasil akhir fungsi, karena pada deret bilangan Fibonacci, bilangan ke-0 adalah 0 dan bilangan ke-1 adalah 1.

            Jika nilai `n` lebih besar dari 1, maka fungsi akan memanggil dirinya sendiri dengan parameter `n-1` dan `n-2` dan kemudian menjumlahkan kembali hasil dari kedua pemanggilan fungsi itu. Dengan cara ini, fungsi akan terus dipanggil secara rekursif sampai nilai n kurang dari atau sama dengan 1.

            Fungsi fibonacci digunakan di dalam program untuk menghasilkan tesktur deret bilangan Fibonacci sepanjang n. Program meminta user untuk memasukkan nilai n, kemudian mengeksekusi fungsi fibonacci sebanyak n kali dan menampilkan setiap nilai bilangan pada deret tersebut.
            ''')
        st.write('Fungsi `faktorial()` dan `fibonacci()` di atas merupakan contoh sederhana dari algoritma rekursif yang menghitung nilai faktorial dari sebuah bilangan bulat')
    # RECURSIVE ALGORITHM END
    
    # SEACRHING ALGORITHM START
    elif menu == 'Searching':
        st.header('Searching Algorithm w/ Python')
        st.write('Algoritma pencarian suatu nilai dari suatu data d/ bahasa Python')

        #  12, 11, 34, 45, 23, 56, 70, 82, 90, 91, 96
        data_col, key_col = st.columns([6,2])

        with data_col:
            data = st.text_input('For example input data here:', placeholder='separate with a comma (,)').replace(' ','')
            if data:
                data = list(map(int, data.split(',')))
                data.sort()

        with key_col:
            if data:
                key = st.selectbox('with key:', set(data))
            else:
                st.selectbox('with key:', ' ')

        if data and key:
            def linear_search(arr, x):
                result = []
                for i in range(len(arr)):
                    if x == arr[i]:
                        result.append(i)
                return result
                
            st.success(f'{key} berada di index ke {linear_search(data, key)} dari {data}')


        linear_tab, binary_tab, interpolation_tab = st.tabs(['Linear Search', 'Binary Search', 'Interpolation Search'])
        with linear_tab:            
            st.markdown('''
            ### Linear Search
            > Linear search adalah algoritma pencarian sederhana dimana kita :red[mencari] sebuah elemen dalam list secara berurutan :red[dari awal sampai akhir] list. Algoritma ini biasanya digunakan untuk data yang tidak diurutkan atau memiliki ukuran list yang relatif kecil.

            Cara kerja algoritma linear search adalah sebagai berikut:

            1. Pertama, algoritma akan memulai pencarian dari indeks pertama dalam list.
            2. Kemudian, algoritma akan membandingkan nilai pada indeks tersebut dengan nilai yang ingin dicari. Jika nilai tersebut sama dengan nilai yang ingin dicari, maka algoritma akan mengembalikan indeks tempat nilai tersebut ditemukan.
            3. Jika nilai pada indeks tersebut tidak sama dengan nilai yang ingin dicari, maka algoritma akan melanjutkan pencarian ke indeks berikutnya dalam list dan kembali ke langkah kedua.
            4. Prosedur ini akan terus dilakukan hingga nilai yang dicari ditemukan atau seluruh elemen dalam list telah dicari.
            5. Jika nilai yang dicari tidak ditemukan dalam list, maka algoritma akan mengembalikan nilai -1 atau pesan yang menunjukkan bahwa nilai tersebut tidak ditemukan dalam list.

            Walaupun algoritma linear search sederhana, namun ia dapat menjadi cukup lambat jika jumlah elemen dalam list sangat besar. Oleh karena itu, pada data yang besar dan terurut, sebaiknya menggunakan algoritma pencarian lainnya seperti binary search.''')
            with st.expander('See source code'):
                code = '''

                def linear_search(arr, x):
                    for i in range(len(arr)):
                        if x == arr[i]:
                            return i
                    return -1
                
                '''
                st.code(code)
            with st.expander('See source code w/ explanation'):
                code = '''
                def linear_search(arr, x):
                # def digunakan untuk mendefinisikan sebuah fungsi baru dengan nama linear_search.
                # arr adalah parameter pertama yang menerima array yang akan dicari.
                # x adalah parameter kedua yang menerima nilai yang akan dicari dalam array.

                    for i in range(len(arr)):
                    # Melakukan loop untuk setiap elemen dalam array arr.
                    # Karena fungsi ini menggunakan pendekatan linear search, setiap elemen dalam array akan dicek satu per satu dari awal hingga akhir array.

                        if x == arr[i]:
                            return i
                            # Memeriksa apakah nilai x yang dicari sama dengan nilai arr[i] saat ini.
                            # Jika sama, maka fungsi akan mengembalikan indeks dari elemen arr[i] di dalam array.
                    return -1
                    # Jika elemen tidak ditemukan dalam array, maka fungsi akan mengembalikan nilai -1
                
                '''
                st.code('def linear_search(arr, x):')
                st.write('''
                - `def` digunakan untuk mendefinisikan sebuah fungsi baru dengan nama `linear_search`.
                - `arr` adalah parameter pertama yang menerima array yang akan dicari.
                - `x` adalah parameter kedua yang menerima nilai yang akan dicari dalam array.
                ''')
                st.code('for i in range(len(arr)):')
                st.write('''
                - Melakukan loop untuk setiap elemen dalam array arr.
                - Karena fungsi ini menggunakan pendekatan linear search, setiap elemen dalam array akan dicek satu per satu dari awal hingga akhir array.
                ''')
                st.code('''
                if x == arr[i]:
                    return i''')
                st.write('''
                - Memeriksa apakah nilai x yang dicari sama dengan nilai arr[i] saat ini.
                - Jika sama, maka fungsi akan mengembalikan indeks dari elemen arr[i] di dalam array.''')
                st.code('return -1')
                st.write('- Jika elemen tidak ditemukan dalam array, maka fungsi akan mengembalikan nilai -1')

                st. write('Jadi, fungsi ini akan mengembalikan indeks elemen yang dicari dalam array atau nilai -1 jika elemen tidak ditemukan dalam array.')

        with binary_tab:
            st.markdown('''
            ### Binary Search
            > Binary search adalah algoritma pencarian yang digunakan untuk mencari nilai tertentu dalam suatu daftar yang terurut. Algoritma ini bekerja dengan :red[membagi daftar menjadi dua bagian] dan :red[memeriksa] apakah nilai yang dicari :red[berada di setengah kiri] atau :red[setengah kanan] dari daftar. Proses ini diulang-ulang hingga nilai yang dicari ditemukan atau jika daftar telah habis dibagi.

            Algoritma binary search dapat dijelaskan sebagai berikut:

            1. Tentukan nilai yang ingin dicari dalam daftar yang terurut.
            2. Tentukan batas awal dan batas akhir daftar yang akan dicari. Awalnya, batas awal adalah indeks pertama dari daftar dan batas akhir adalah indeks terakhir dari daftar.
            3. Hitung indeks tengah dari batas awal dan batas akhir dengan cara menjumlahkan batas awal dan batas akhir, kemudian dibagi 2. Indeks ini akan digunakan untuk membagi daftar menjadi dua bagian.
            4. Periksa nilai di posisi indeks tengah. Jika nilainya sama dengan nilai yang dicari, maka pencarian selesai dan indeks tersebut dikembalikan. Jika nilainya lebih kecil dari nilai yang dicari, maka batas awal digeser ke kanan dari indeks tengah. Jika nilainya lebih besar dari nilai yang dicari, maka batas akhir digeser ke kiri dari indeks tengah.
            5. Ulangi langkah 3-4 dengan menggunakan batas awal dan batas akhir yang baru. Proses ini diulang-ulang hingga nilai yang dicari ditemukan atau jika daftar telah habis dibagi.

            Dalam binary search, setiap iterasi daftar akan dibagi menjadi dua bagian sehingga jumlah elemen yang perlu diperiksa akan berkurang setengah pada setiap iterasi. Oleh karena itu, algoritma ini memiliki kompleksitas waktu ```O(log n)```, di mana ```n``` adalah jumlah elemen pada daftar yang terurut.

            Dalam Python, binary search dapat diimplementasikan menggunakan fungsi rekursif atau iteratif. Pada implementasi binary search secara rekursif, fungsi akan dipanggil kembali dengan daftar yang sudah dibagi menjadi dua setengah hingga nilai yang dicari ditemukan. Sedangkan pada implementasi binary search iteratif, perulangan dilakukan hingga nilai yang dicari ditemukan atau jika daftar telah habis dibagi.


            ''')
            
            with st.expander('See source code'):
                code = '''

                def binary_search(arr, x):
                    left = 0
                    right = len(arr) - 1
                    
                    while left <= right:
                        mid = (left + right) // 2
                        if arr[mid] == x:
                            return mid
                        elif arr[mid] < x:
                            left = mid + 1
                        else:
                            right = mid - 1
                            
                    return -1
                
                '''
                st.code(code)

            with st.expander('See source code w/ explanation'):
                st.code('def binary_search(arr, x):')
                st.write('''
                - `def` digunakan untuk mendefinisikan sebuah fungsi baru dengan nama `binary_search`
                - `arr` adalah parameter pertama yang menerima array yang akan dicari
                - `x` adalah parameter kedua yang menerima nilai yang akan dicari dalam array''')
                st.code('''
                left = 0
                right = len(arr) - 1''')
                st.write('''
                - Variabel `left` dan `right` digunakan untuk menentukan rentang pencarian pada array
                - `left` diinisialisasi dengan nilai 0, dan `right` diinisialisasi dengan nilai `len(arr) - 1`''')
                st.code('while left <= right:')
                st.write('- Looping while ini akan terus berjalan selama nilai left tidak melebihi nilai right. Ini menandakan bahwa rentang pencarian masih ada elemen yang belum di periksa')
                st.code('mid = (left + right) // 2')
                st.write('- Menghitung nilai tengah dari rentang pencarian dengan menggunakan formula `(left + right) // 2`. Nilai tengah ini digunakan untuk membagi rentang pencarian menjadi dua bagian')
                st.code('''
                if arr[mid] == x:
                    return mid''')
                st.write('''
                - Memeriksa apakah nilai `x` yang dicari sama dengan nilai `arr[mid]` pada posisi tengah array
                - Jika sama, maka fungsi akan mengembalikan indeks dari elemen `arr[mid]` di dalam array')
                ''')
                st.code('''
                elif arr[mid] < x:
                    left = mid + 1''')
                st.write('''
                - Jika nilai `x` yang dicari lebih besar dari nilai `arr[mid]` pada posisi tengah array, maka rentang pencarian dipindahkan ke setengah kanan array
                - `left` diperbarui dengan nilai `mid + 1` yang menunjukkan bahwa elemen sebelum posisi tengah sudah diperiksa dan tidak mengandung nilai yang dicari
                ''')
                st.code('''
                elif arr[mid] < x:
                    left = mid + 1''')
                st.write('''
                - Jika nilai `x` yang dicari lebih besar dari nilai `arr[mid]` pada posisi tengah array, maka rentang pencarian dipindahkan ke setengah kanan array
                - `left` diperbarui dengan nilai `mid + 1` yang menunjukkan bahwa elemen sebelum posisi tengah sudah diperiksa dan tidak mengandung nilai yang dicari')
                ''')
                st.code('''
                else:
                    right = mid - 1''')
                st.write('''
                - Jika nilai `x` yang dicari lebih kecil dari nilai `arr[mid]` pada posisi tengah array, maka rentang pencarian dipindahkan ke setengah kiri array.
                - `right` diperbarui dengan nilai `mid - 1` yang menunjukkan bahwa elemen setelah posisi tengah sudah diperiksa dan tidak mengandung nilai yang dicari.
                ''')
                st.code('return -1')
                st.write('- Jika elemen tidak ditemukan dalam array, maka fungsi akan mengembalikan nilai -1')

                st.write('Jadi, fungsi ini akan mengembalikan indeks elemen yang dicari dalam array atau nilai -1 jika elemen tidak ditemukan dalam array. Algoritma binary search ini bekerja dengan cara membagi rentang pencarian menjadi dua bagian setiap kali loop berjalan, sehingga kompleksitas waktu yang dibutuhkan untuk mencari elemen dalam array lebih efisien dibandingkan dengan algoritma pencarian linear search.')
        
        with interpolation_tab:
            st.markdown('''
            ### Interpolation Search

            > Interpolation search adalah algoritma pencarian yang digunakan untuk mencari elemen di dalam array yang terurut. Algoritma ini mencoba memperkirakan posisi elemen yang dicari berdasarkan nilai-nilai di dalam array.

            
            Berikut adalah algoritma Interpolation Search:

            1. Atur variabel awal `start` dan akhir `end` dari array.
            2. Selama `start` kurang dari atau sama dengan `end` dan elemen yang dicari berada di antara `start` dan `end`, lakukan:
                - Hitung posisi estimasi (pos) dengan rumus: 

                    ```pos = start + ((end-start) // (arr[end]-arr[start])) * (x - arr[start])```
                - Jika elemen di `pos` sama dengan elemen yang dicari, kembalikan `pos`.
                - Jika elemen di `pos` kurang dari elemen yang dicari, ubah `start` menjadi `pos + 1`.
                - Jika elemen di `pos` lebih besar dari elemen yang dicari, ubah `end` menjadi `pos - 1`.
            3. Jika elemen yang dicari tidak ditemukan, kembalikan -1.


            Perlu diingat bahwa Interpolation Search hanya efisien pada array yang terurut secara seragam dan terdistribusi secara merata. Jika array tidak terdistribusi secara merata, Interpolation Search mungkin tidak bekerja dengan baik.

            ''')
            with st.expander('See source code'):
                code = '''
                def interpolation_search(arr, x):
                    start = 0
                    end = len(arr) - 1

                    while start <= end and x >= arr[start] and x <= arr[end]:
                        pos = start + ((end-start) // (arr[end]-arr[start])) * (x - arr[start])
                        if arr[pos] == x:
                            return pos
                        if arr[pos] < x:
                            start = pos + 1
                        else:
                            end = pos - 1

                    return -1'''
                st.code(code)
            with st.expander('See source code w/ explanation'):
                st.code('def interpolation_search(arr, x):')
                st.write('''
                - ```def``` digunakan untuk mendefinisikan sebuah fungsi baru dengan nama ```interpolation_search```.
                - ```arr``` adalah parameter pertama yang menerima array yang akan dicari.
                - ```x``` adalah parameter kedua yang menerima nilai yang akan dicari dalam array.''')
                st.code('''
                    start = 0
                    end = len(arr) - 1''')
                st.write('- Variabel ```start``` dan ```end``` digunakan untuk menentukan rentang pencarian pada array. ```start``` diinisialisasi dengan nilai 0, dan ```end``` diinisialisasi dengan nilai len(arr) - 1.')
                st.code('while start <= end and x >= arr[start] and x <= arr[end]:')
                st.write('- Looping while ini akan terus berjalan selama nilai `start` tidak melebihi nilai `end` dan nilai `x` yang dicari berada dalam rentang pencarian `arr[start]` dan `arr[end]`.')
                st.code('pos = start + ((end-start) // (arr[end]-arr[start])) * (x - arr[start])')
                st.write('- Menentukan posisi tebakan awal (interpolated position) dengan menggunakan formula `(x-arr[start]) / (arr[end]-arr[start])`. Formula ini mengasumsikan bahwa nilai yang akan dicari `x` berada secara merata di seluruh rentang pencarian. Nilai ini kemudian dikonversi menjadi indeks dalam array.')
                st.code('''
                if arr[pos] == x:
                    return pos
                ''')
                st.write('''
                - Memeriksa apakah nilai x yang dicari sama dengan nilai arr[pos] pada posisi yang dihitung dengan formula di atas.
                - Jika sama, maka fungsi akan mengembalikan indeks dari elemen arr[pos] di dalam array.
                ''')
                st.code('''
                if arr[pos] < x:
                    start = pos + 1
                else:
                    end = pos - 1
                ''')
                st.write('''
                - Jika nilai `x` yang dicari lebih besar dari nilai `arr[pos]` pada posisi yang dihitung dengan formula di atas, maka rentang pencarian dipindahkan ke setengah kanan array.
                - `start` diperbarui dengan nilai `pos + 1` yang menunjukkan bahwa elemen sebelum posisi yang dihitung sudah diperiksa dan tidak mengandung nilai yang dicari.
                - Jika nilai `x` yang dicari lebih kecil dari nilai `arr[pos]` pada posisi yang dihitung dengan formula di atas, maka rentang pencarian dipindahkan ke setengah kiri array.
                - `end` diperbarui dengan nilai `pos - 1` yang menunjukkan bahwa elemen setelah posisi yang dihitung sudah diperiksa dan tidak mengandung nilai yang dicari.
                ''')
                st.code('return -1')
                st.write('- Jika elemen tidak ditemukan dalam array, maka fungsi akan mengembalikan nilai `-1`.')
                st.write('Jadi, fungsi ini akan mengembalikan indeks elemen yang dicari dalam array atau nilai -1 jika elemen tidak ditemukan dalam array. Algoritma interpolation search ini bekerja dengan mengasumsikan bahwa nilai yang dicari terdistribusi merata di seluruh rentang pencarian, sehingga kompleksitas waktu yang dibutuhkan untuk mencari elemen dalam array lebih')
    # SEARCHING ALGORITHM END


    # SORTING ALGORITHM START
    elif menu == 'Sorting':
        st.header('Sorting Algorithm w/ Python')
        st.write('Algoritma pengurutan suatu data d/ bahasa Python')
        data = st.text_input('For example input data here:', placeholder='separate with a comma (,)').replace(' ','')
        if data:
            data = list(map(int, data.split(',')))
            data.sort()
            st.success(data)

        bubble_tab, selection_tab, insertion_tab, merge_tab, quick_tab, heap_tab, tim_tab = st.tabs(['Bubble Sort', 'Selection Sort', 'Insertion Sort','Merge Sort', 'Quick Short', 'Heap Sort', 'Tim Sort'])
        with selection_tab:
            st.write('Soon yhh')
        with insertion_tab:
            st.write('Soon yhh')
        with merge_tab:
            st.write('Soon yhh')
        with quick_tab:
            st.write('Soon yhh')
        with heap_tab:
            st.write('Soon yhh')
        with tim_tab:
            st.write('''
            ### Tim Sort
            Pengurutan menggunakan function bawaan python yaitu `.sort()`
            ''')
            st.code('''
            a_list = [10,2,3,4,5,6]
            a_list.sort()

            print(a_list) # Output: [2, 3, 4, 5, 6, 10]
            ''')
        with bubble_tab:
            st.markdown('''
            ### Bubble Sort
            Bubble Sort adalah salah satu algoritma sorting yang sederhana dan mudah dipahami. Algoritma ini bekerja dengan :red[membandingkan setiap elemen] dari array secara berpasangan dan :red[menukar posisi] elemen jika urutannya tidak sesuai. Proses ini diulang sampai seluruh elemen pada array terurut dengan benar.

            Secara umum, Bubble Sort bekerja dengan cara:

            1. Membandingkan elemen pertama dan kedua dari array.
            2. Jika elemen pertama lebih besar dari elemen kedua, maka kedua elemen tersebut ditukar.
            3. Kemudian, membandingkan elemen kedua dan ketiga dari array, jika urutan salah, tukar posisi elemen tersebut.
            4. Lakukan langkah 2-3 sampai seluruh elemen pada array telah terurut dengan benar.
            
            Bubble Sort termasuk algoritma sorting dengan kompleksitas waktu yang relatif tinggi, yaitu `O(n^2)`. Hal ini membuat Bubble Sort kurang efisien untuk digunakan pada data dengan jumlah yang cukup besar. Namun, karena algoritma ini sederhana dan mudah dimengerti, sering digunakan sebagai algoritma dasar dalam pembelajaran algoritma sorting.''')
            with st.expander('See source code'):

                st.code('''
                def bubble_sort(arr):
                    n = len(arr)
                    for i in range(n):
                        for j in range(0, n-i-1):
                            if arr[j] > arr[j+1]:
                                arr[j], arr[j+1] = arr[j+1], arr[j]
                ''')
            with st.expander('See source code w/ explanation'):
                st.code('def bubble_sort(arr):')
                st.write('- Mendefinisikan sebuah fungsi bernama `bubble_sort` yang menerima satu parameter `arr`, yaitu array yang akan di-sort.')
                st.code('n = len(arr)')
                st.write('- Menghitung panjang dari array menggunakan fungsi `len(arr)` dan menyimpannya dalam variabel `n`. Variabel `n` digunakan untuk menentukan batas iterasi pada loop for dibawahnya.')
                st.code('for i in range(n):')
                st.write('- Loop for pertama dengan variabel `i` digunakan untuk melakukan iterasi sebanyak `n` kali. Pada setiap iterasi, loop for kedua akan memproses elemen-elemen pada array hingga elemen ke-`n-i-1` saja, karena elemen-elemen pada indeks lebih besar dari itu sudah terurut dengan benar selama iterasi sebelumnya.')
                st.code('''
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                ''')
                st.write('- Loop for kedua dengan variabel `j` digunakan untuk membandingkan elemen ke-`j` dan ke-`j+1` dari array. Jika urutan elemen tersebut salah, maka posisi keduanya akan ditukar menggunakan assignment statement `arr[j], arr[j+1] = arr[j+1], arr[j]`.')
                st.write('''
                - Setelah selesai melakukan iterasi pada loop for kedua, maka elemen dengan nilai terbesar akan berada pada akhir dari array. Oleh karena itu, pada setiap iterasi loop for pertama, jumlah elemen yang diproses pada loop for kedua akan berkurang seiring dengan bertambahnya iterasi.
                - Ketika iterasi loop for pertama selesai, maka array akan terurut secara ascending.
                
                Dengan begitu, algoritma Bubble Sort bekerja dengan membandingkan setiap pasangan elemen pada array dan menukar posisi jika urutannya salah. Proses ini diulang terus menerus hingga seluruh elemen pada array terurut dengan benar secara ascending.''')
    # SORTING ALGORITHM END


    # SWAP ALGORITHM START
    elif menu == 'Swap Variable':
        st.header('Swap Variable Algorithm w/ Python')
        st.write('''
        Bagaimana cara menukar value pada variable `a` dan `b`, tanpa mendeklarasikan ulang variablenya?

        Dari:
        ''')
        st.code('''
        a = 2
        b = 6
        ''')
        st.write('Menjadi:')
        st.code('''
        a = 6
        b = 2
        ''')
        st.write('''
        #### Menggunakan variable ke-3
        Variable ke-3 digunakan sebagai container sementara value variable utama
        ''')
        st.code('''
        a = 6
        b = 2

        print('Sebelum di-swap, nilai a adalah', a, 'dan b adalah', b )

        c = a
        a = b
        b = c

        print('Sesudah di-swap, nilai a adalah', a, 'dan b adalah', b )
        ''')
        st.write('''
        Algoritmanya bisa diibaratkan dengan ketika kita ingin menukar isi dari gelas A ke gelas B, tanpa harus membuang isi gelas dan mengisinya ulang
        1. Siapkan gelas A yang berisi cairan A, dan gelas B berisi cairan B
        2. Untuk menempatkan cairan A di gelas B dan cairan B di gelas A, kita siapkan gelas kosong yaitu C
        3. Tempatkan cairan A di gelas C, sehingga gelas A menjadi kosong dan gelas C berisi cairan A
        4. Pindahkan cairan B dari gelas B ke dalam gelas A, sehingga gelas B menjadi kosong
        5. Pindahkan cairan A dari gelas C tadi ke dalam gelas B
        6. Isinya sudah tertukar, ribet? Iya, cuma itulah bagaimana algoritma komputer bekerja.

        ---

        ##### Cara instan
        Kita juga bisa langsung swap variable dengan mendeklarasikannya kedua variabelnya bersamaan
        ''')
        st.code('''
        a = 2
        b = 6
        a, b = b, a
        ''')
        st.write('Bagaimana jika?')
        st.code('''
        a = 2
        b = 6

        a = b
        b = a
        ''')
        st.write('> Kode di ats tidak membuat variablenay ter-swap secara benar karena value `a` pada deklarasi `b` bukanlah value `a` awal, melainkan value `a` yang sudah terupdate menjadi value `b` awal ')
    # SWAP ALGORITHM END

# ALGORITHM END


# BASICS START
if option == 'Basics Python':

    # ARITHMETIC BASIC START
    if menu == 'Arithmetic Expression':
        st.header('Arithmetic Expression')
        st.write('Kita bisa melakukan operasi aritmetika dasar dengan simbol khusus')

        x = st.text_input('Coba di sini', placeholder='contoh: 2*4')
        if x:
            st.success(eval(x))
        else:
            st.text_input(' ', label_visibility='collapsed', disabled=True)

        st.write('''
            <table style='font-family: monospace;'>
                <tr>
                    <td>Operator</td>
                    <td>Fungsi</td>
                    <td>Contoh</td>
                    <td>Hasil</td>
                </tr>
                <tr>
                    <td align='center'>+</td>
                    <td>Addition</td>
                    <td align='center'>4+2</td>
                    <td align='center'>6</td>
                </tr>
                <tr>
                    <td align='center'>-</td>
                    <td>Subtraction</td>
                    <td align='center'>4-2</td>
                    <td align='center'>2</td>
                </tr>
                <tr>
                    <td align='center'>*</td>
                    <td>Multiplication</td>
                    <td align='center'>4*2</td>
                    <td align='center'>8</td>
                </tr>
                <tr>
                    <td align='center'>/</td>
                    <td>Division</td>
                    <td align='center'>4/2</td>
                    <td align='center'>2.0</td>
                </tr>
                <tr>
                    <td align='center'>%</td>
                    <td>Modulo</td>
                    <td align='center'>4%2</td>
                    <td align='center'>0</td>
                </tr>
                <tr>
                    <td align='center'>**</td>
                    <td>Exponent</td>
                    <td align='center'>4**2</td>
                    <td align='center'>16</td>
                </tr>
                <tr>
                    <td align='center'>//</td>
                    <td>Floor division</td>
                    <td align='center'>4//2</td>
                    <td align='center'>2</td>
                </tr>
            </table>
            ''', unsafe_allow_html=True)
        st.write('> Kita juga bisa menggunakan tanda kurung `( )` untuk mengelompokkan operasi agar dievaluasi terlebih dahulu sebelum melanjutkan ke operasi berikutnya')
    # ARITHMETIC BASIC END

    # BOOLEAN BASIC START
    elif menu == 'Boolean Algebra':
        st.header('Boolean Algebra')
        st.write('''
        > Boolean algebra adalah cabang matematika yang menggunakan nilai kebenaran (`True` atau `False`) untuk melakukan operasi logika.
        
        Di Python, kita dapat menggunakan operator logika seperti `and`, `or`, `not`, `in`, `is`, dan operator perbandingan seperti `==`, `!=`, `>`, `<`, `>=`, dan `>=`
        
        ---

        ##### and
        keduanya harus `True` agar keluaran `True`
        ''')
        st.code('''
        print(True and True) # Outputnya True
        print(True and False) # Outputnya False
        print(False and True) # Outputnya False
        print(False and False) # Outputnya False
        ''')
        st.write('''
        ---
        ##### or
        
        salah satu atau keduanya harus `True` agar keluaran `True`
        ''')
        st.code('''
        print(True or True) # Outputnya True
        print(True or False) # Outputnya True
        print(False or True) # Outputnya True
        print(False or False) # Outputnya False
        ''')
        st.write('''
        ---
        ##### not

        negasi
        ''')
        st.code('''
        print(not True) # Outputnya False
        print(not (False and True)) # Outputnya True
        ''')
        st.write('''
        ---
        ##### in
        
        `in` digunakan sebagai operator keanggotaan untuk menentukan apakah suatu nilai ada di dalam suatu `list`, `dict`, `tuple`, atau `sets`
        ''')
        st.code('''
        a_list = [1, 2, 3, 4, 5]
        print(2 in a_list) # Outputnya True
        print(3 not in a_list) # Outputnya False
        ''')
        st.write('''
        ---
        ##### is

        `is` digunakan untuk memeriksa apakah dua objek memiliki identitas yang sama atau tidak
        ''')
        st.code('''
        a_list = [1,2,3]
        b_list = [1,2,3]

        c_list = a_list

        print(a_list is b_list) # Outputnya False
        print(c_list is a_list) # Outputnya True
        ''')
        st.write('''
        ---
        ##### == dan !=
        `==` untuk sama dengan
        ''')
        st.code('''
        print(4 == 8/2) # Outputnya True
        print(3 == 3.2) # Outputnya False
        ''')
        st.write('''
        `!=` untuk tidak sama dengan
        ''')
        st.code('''
        print(4 != 8/2) # Outputnya False
        print(3 != 3.2) # Outputnya True
        ''')
        st.write('''
        ---
        ##### <, >,  =<, dan =>
        `<` untuk kurang dari, `=<` untuk kurang dari sama dengan
        ''')
        st.code('''
        print(3 < 7) # Outputnya True
        print(10 < 7) # Outputnya False
        print(3 =< 7) # Outputnya True
        print(7 =< 7) # Outputnya True
        ''')
        st.write('''
        `>` untuk lebih dari, `=>` untuk lebih dari sama dengan
        ''')
        st.code('''
        print(3 > 7) # Outputnya False
        print(10 > 7) # Outputnya True
        print(3 => 7) # Outputnya False
        print(7 => 7) # Outputnya True
        ''')
    # BOOLEAN BASIC END


    # CONDITIONAL BASIC START
    elif menu == 'Conditional Statement (IF-ELSE)':
        st.header('Conditional Statement')
        st.write('### IF - ELIF - ELSE')
        st.write('''
        > Struktur pengendali alur program yang digunakan untuk memeriksa kondisi tertentu sebelum menjalankan serangkaian pernyataan
        
        Pernyataan kondisional biasanya menggunakan kata kunci `if`, `else`, dan `elif` (singkatan dari `else if`) untuk mengevaluasi suatu kondisi dan melakukan tindakan yang sesuai.''')
        st.write('Dalam Python, pernyataan `if` digunakan untuk mengevaluasi kondisi tunggal, sedangkan pernyataan `elif` digunakan untuk mengevaluasi beberapa kondisi yang saling eksklusif. Pernyataan `else` digunakan sebagai default atau fallback ketika tidak ada kondisi yang terpenuhi.')
        st.code('''
        if kondisi1:
            pernyataan1
        elif kondisi2:
            pernyataan2
        elif kondisi3:
            pernyataan3
        else:
            pernyataan4
        ''')
        st.write('> *if bisa sendiri jg bisa ber 2 an sm else, tp jg bisa ber 3 / lebih gara2 elif*')
        st.write('##### Example 1')
        
        st.code('''
        nilai = 78.8

        if 90 < nilai <= 100:
            grade = 'A'
        elif 80 < nilai <= 90:
            grade = 'B'
        elif 70 < nilai <= 80:
            grade = 'C'
        elif 60 < nilai <= 70:
            grade = 'D'
        else:
            grade = 'E'
        ''')
        with st.expander('Show explanation'):
            st.write('''
            Program tersebut akan menerima input nilai numerik dalam variabel `nilai`, kemudian program akan memeriksa setiap kondisi dengan menggunakan statement `if` `elif` dan `else`. Jika `nilai` numerik berada di antara 90-100, maka `grade` yang diberikan adalah A, jika `nilai` berada di antara 80-90 maka `grade` yang diberikan adalah B, dan begitu seterusnya hingga `nilai` tidak memenuhi semua kondisi dan diberikan nilai huruf E.

            Maka dengan nilai `78.8` maka mendapatkan grade `C`
            ''')

        st.write('##### Example 2')
        st.code('''
        x = 9
        if x > 0:
            if x % 2 == 0:
                print("x adalah bilangan genap positif")
            else:
                print("x adalah bilangan ganjil positif")
        else:
            print("x bukan bilangan positif")
                ''')
        with st.expander('Show explanation'):
            st.write('''
            Program ini menggunakan **percabangan bersarang** atau *nested branch*, pertama-tama akan dicek apakah `x` lebih besar dari 0. Jika iya, maka akan masuk ke dalam kondisi kedua untuk mengecek apakah `x` adalah bilangan genap atau ganjil. Jika `x` habis dibagi dua, maka `x` adalah bilangan genap dan program akan mencetak pesan `x adalah bilangan genap positif`. Namun jika `x` tidak habis dibagi dua, maka `x` adalah bilangan ganjil dan program akan mencetak pesan `x adalah bilangan ganjil positif`.

            Jika kondisi pertama tidak terpenuhi (artinya x tidak lebih besar dari 0), maka program akan langsung mencetak pesan bahwa x bukan bilangan positif.''')
    # CONDITIONAL BASIC END

    # DATATYPE BASIC START
    elif menu == 'Datatype (STR/INT/FLOAT)':
        st.header('Datatype Basic i/ Python')
        st.write('Macam macam tipe data d/ Python')
        input_a = st.text_input('Cek type data: ')
        try:
            if input_a:
                input_a = eval(input_a)
                st.success(type(input_a))
        except:
                st.error('Error, mungkin terbaca variable, ingat jika kita ingin membuat string gunakan tanda petik (")', icon="🚨")
               
        string_tab, integer_tab, float_tab, bool_tab, complex_tab = st.tabs(['String', 'Integer', 'Float', 'Boolean', 'Complex'])
        with string_tab:
            st.write('### String')
            st.write('''> String (`str`) adalah tipe data yang digunakan untuk merepresentasikan teks atau urutan karakter. String dapat didefinisikan dengan menggunakan tanda kutip tunggal ('...') atau tanda kutip ganda ("...")''')
            # st.write('### Example')
            st.code('''
            nama = "John"
            umur = '20'
            alamat = "Jl. Melati No. 10"
            ''')
            st.write('''
            Pada contoh di atas, `nama`, `umur`, dan `alamat` adalah variabel yang berisi string.

            ##### Penjumlahan dan perkalian string
            Kita dapat melakukan operasi-operasi tertentu pada string seperti menggabungkan (+) dua string atau mengulang (*) string.
            ''')
            st.code('''
            var1 = 'Hello'
            var2 = 'World'
            result = var1 + ' ' + var2
            print(result) # Outputnya 'Hello World'
            ''')
            st.code('''
            var3 = 'ha'
            print(var3 * 3) # Outputnya 'hahaha'
            ''')
            st.write('''
            > *string tidak bisa dikurangi atau dibagi*

            Selain itu, string juga memiliki banyak method atau fungsi bawaan di dalamnya, seperti `lower()` untuk mengubah semua huruf dalam string menjadi huruf kecil, `upper()` untuk mengubah menjadi huruf besar, `replace()` untuk mengganti beberapa karakter dalam string dengan karakter lain, dan masih banyak lagi.''')
            st.code('''
            var1_lower = var1.lower() # var1 menjadi 'hello'
            var2_upper = var2.upper() # var2 menjadi 'world'
            ''')
        with integer_tab:
            st.write('''
            ### Integer
            > Integer (`int`) adalah tipe data yang digunakan untuk merepresentasikan bilangan bulat. Integer ditulis dalam bentuk angka, seperti `2`, `10`, atau `-7`
            ''')
            st.code('''
            a = 1
            b = 6
            ''')
            st.write('''
            ##### Operasi matematika
            Kita bisa melakukan operasi matematika dasar menggunakan integer, seperti penjumlahan, pengurangan, perkalian, dan pembagian.
            > *Setiap pembagian integer akan menghasilkan type data Float*
            ''')
            st.code('''
            a = 3 - 2
            print(a) # Outputnya 1

            b = a * 4
            print(b) # Outputnya 4

            print(4 / 2) # Outputnya 2.0 bukan 2
            ''')
            st.write('''
            ##### Operasi pembandingan integer
            Kita juga dapat melakukan operasi pembandingan pada integer, seperti lebih besar dari (>), lebih kecil dari (<), sama dengan (==), dan sebagainya''')
            st.code('''
            a = 2
            b = 3
            print(a <= b) # Outputnya True
            print(a == b) # Outputnya False
            ''')
        with float_tab:
            st.write('''
            ### Float
            > Float (`float`) adalah tipe data digunakan untuk merepresentasikan bilangan pecahan (desimal) dengan titik mengambang **bukan koma**. Float sering digunakan dalam operasi matematika atau ilmiah, di mana presisi angka desimal sangat penting, seperti `3.142857142857143`, `9.8`, etc.
            ''')
            st.code('''
            pi = 3.142857142857143
            ''')
            st.write('''
            Perlu diperhatikan bahwa karena komputer hanya dapat merepresentasikan angka secara terbatas, maka float memiliki keterbatasan dalam presisi. Oleh karena itu, float kadang-kadang dapat mengalami sedikit kesalahan pembulatan ketika melakukan operasi matematika yang kompleks.

            ##### Operasi matematika dan pembandingan float seperti pada integer
            ''')
            st.code('''
            a = 2.0
            b = 4
            c = 3.4

            print(a + b) # Output 6.0
            print(a + c) # Output 5.4
            print(b > c) # Outputnya True
            ''')
            st.write('> *Semua operasi yang bahkan salah satunya adalah float maka akan menghasilkan tipe data float kecuali operasi floor division (`//`)*')

        with bool_tab:
            st.write('''
            ### Boolean
            > Tipe data `bool` yang hanya memiliki dua nilai, yaitu True (benar) dan False (salah). Tipe data ini digunakan untuk merepresentasikan keadaan yang hanya memungkinkan ada dua opsi, seperti jika suatu kondisi terpenuhi atau tidak terpenuhi.
            
            Dalam Python, boolean diwakili oleh kata kunci `True` dan `False`, yang harus ditulis dengan huruf awal kapital''')
            st.code('''
            x = True
            y = False
            z = 1 < 2 # True
            ''')
            st.write('''
            ##### Operator logika boolean
            
            Operator `and`, keduanya harus `True` agar menghasilkan output `True`''')
            st.code('''
            print(True and True) # Outputnya True
            print(True and False) # Outputnya False
            print(False and True) # Outputnya False
            print(False and False) # Outputnya False
            ''')
            st.write('Operator `or`, salah satu atau keduanya harus `True` agar menghasilkan output `True`')
            st.code('''
            print(True or True) # Outputnya True
            print(True or False) # Outputnya True
            print(False or True) # Outputnya True
            print(False or False) # Outputnya False
            ''')
            st.write('Operator `not`, negasi')
            st.code('''
            print(not True) # Outputnya False
            print(not False) # Outputnya True
            print(True and not False) # Outputnya True
            
            ''')
            st.write('> *Selebihnya di tab boolean algebra*')
        with complex_tab:
            st.write('### Complex')
            st.write('> *Karena belum ada di materi jd SOON yhh*')
    # DATATYPE BASIC END

    # DATA STRUCTURE BASIC START
    elif menu == 'Data Structure (List/Tuple/Set/Dict)':
        st.header('Data Structure')
        list_tab, tuple_tab, sets_tab, dict_tab = st.tabs(['List', 'Tuple', 'Sets', 'Dictionary'])
        with list_tab:
            st.write('''
            ### List

            Jenis tipe data yang digunakan untuk menyimpan kumpulan nilai (elemen) dalam sebuah variabel. List didefinisikan dengan menggunakan tanda kurung siku `[]` dan elemen-elemennya dipisahkan oleh koma
            
            ''')
            st.code('''
            # membuat list kosong
            my_list = []

            # membuat list dengan beberapa elemen
            my_list = [1, 2, 3, "empat", "lima"]
            ''')
            st.write('''
            List memiliki beberapa karakteristik sebagai berikut:

            1. Dapat diakses menggunakan indeks: Setiap elemen dalam list dapat diakses menggunakan indeks yang dimulai dari nol. Misalnya, `my_list[0]` akan mengembalikan nilai pertama dalam list.

            2. :red[Mutable]: Artinya, setelah list dibuat, elemen-elemennya dapat diubah.

            3. Dapat berisi elemen dengan tipe data yang berbeda: Sebuah list di Python dapat berisi elemen dengan tipe data yang berbeda, seperti integer, float, string, dan sebagainya.

            4. Dapat digabungkan: Dua atau lebih list dapat digabungkan menjadi satu list menggunakan operator '`+`'.

            5. Dapat diurutkan: Elemen dalam list dapat diurutkan menggunakan fungsi `sort()`.

            6. Dapat dicari panjangnya: Panjang list dapat diperoleh menggunakan fungsi `len()`.

            7. Dapat diakses dengan slicing: Selain menggunakan indeks, elemen dalam list juga dapat diakses menggunakan slicing. Misalnya, `my_list[1:3]` akan menghasilkan sublist dari elemen kedua hingga keempat dalam list

            Beberapa built-in list di Python antara lain:

            1. `list.append(x)` : Menambahkan elemen x ke akhir list.
            2. `list.extend(iterable)` : Menggabungkan iterable (seperti list, tuple, atau string) ke dalam list.
            3. `list.insert(i, x)` : Memasukkan elemen x ke posisi i pada list.
            4. `list.remove(x)` : Menghapus elemen pertama yang memiliki nilai x.
            5. `list.pop([i])` : Menghapus dan mengembalikan elemen pada posisi i dari list. Jika i tidak diberikan, maka elemen terakhir akan dihapus dan dikembalikan.
            6. `list.index(x[, start[, end]])` : Mencari dan mengembalikan indeks pertama dari elemen dengan nilai x.
            7. `list.count(x)` : Menghitung jumlah kemunculan elemen dengan nilai x pada list.
            8. `list.sort(key=None, reverse=False)` : Mengurutkan elemen pada list.
            9. `list.reverse()` : Membalik urutan elemen pada list.
            10. `list.copy()` : Mengembalikan salinan dari list.
            Terdapat juga beberapa fungsi built-in pada Python yang dapat digunakan untuk memanipulasi list, seperti `sorted()`, `len()`, `max()`, `min()`, dan `sum()`.
            ''')

        with tuple_tab:
            st.write('''
            ### Tuple

            Jenis tipe data yang mirip dengan list, namun tidak dapat diubah setelah dibuat. Tuple didefinisikan dengan menggunakan tanda kurung biasa `()` dan elemen-elemennya dipisahkan oleh koma.
            ''')
            st.code('''
            # membuat tuple kosong
            my_tuple = ()

            # membuat tuple dengan beberapa elemen
            my_tuple = (1, 2, 3, "empat", "lima")
            ''')
            st.write('''
            Tuple memiliki beberapa karakteristik sebagai berikut:

            1. Dapat diakses menggunakan indeks: Setiap elemen dalam tuple dapat diakses menggunakan indeks yang dimulai dari nol. Misalnya, `my_tuple[0]` akan mengembalikan nilai pertama dalam tuple.

            2. :red[Immutable]: Artinya, setelah tuple dibuat, elemen-elemennya tidak dapat diubah. Jika kita mencoba mengubah nilai pada elemen tuple, Python akan menghasilkan error.

            3. Dapat berisi elemen dengan tipe data yang berbeda: Seperti list, sebuah tuple di Python dapat berisi elemen dengan tipe data yang berbeda, seperti integer, float, string, dan sebagainya.

            4. Dapat digabungkan: Dua atau lebih tuple dapat digabungkan menjadi satu tuple menggunakan operator '`+`'.

            5. Dapat diurutkan: Elemen dalam tuple dapat diurutkan menggunakan fungsi `sorted()`.

            6. Dapat dicari panjangnya: Panjang tuple dapat diperoleh menggunakan fungsi `len()`.

            7. Efisien dalam penggunaan memori: Karena tuple bersifat immutable, Python tidak perlu mengalokasikan ruang ekstra untuk menampung perubahan pada elemen tuple seperti pada list, sehingga tuple lebih efisien dalam penggunaan memori.

            Karena sifat-sifat tersebut, tuple sering digunakan untuk menyimpan data yang tidak perlu diubah setelah dibuat, misalnya koordinat dalam sebuah program grafis atau nama-nama bulan dalam sebuah program kalender.
            
            ''')
        with sets_tab:
            st.write('''
            ### Sets

            Sets merupakan salah satu tipe data koleksi atau container yang terdiri dari sekumpulan nilai atau elemen tanpa ada duplikat dan tidak berurutan.
            
            Set pada Python mirip dengan himpunan matematika, sehingga operasi yang dapat dilakukan pada set antara lain *union* (gabungan), *intersection* (irisan), *difference* (selisih), *symmetric difference* (beda simetris), *subset* (subhimpunan), dan *superset* (suprahimpunan).

            Kita dapat membuat set di Python dengan menggunakan tanda kurung kurawal (`{}`) dan memasukkan elemen-elemen set di dalamnya, dipisahkan dengan koma. Contohnya seperti ini:
            ''')
            st.code('''
            # Membuat set kosong
            my_set = set()

            # atau
            my_set = {}

            # Membuat set dengan beberapa elemen
            my_set = {1, 2, 3}

            ''')
            st.write('Kita juga dapat membuat set dari list atau tuple dengan menggunakan fungsi `set()`. Contohnya seperti ini:')
            st.code('''
            # Membuat set dari list
            my_list = [1, 2, 3]
            my_set = set(my_list)

            # Membuat set dari tuple
            my_tuple = (4, 5, 6)
            my_set = set(my_tuple)
            ''')
            st.write('''
            Set di Python bersifat :red[mutable] (dapat diubah), sehingga kita dapat menambahkan atau menghapus elemen di dalam set menggunakan method `add()` dan `remove()`
            ''')
            st.code('''
            # Membuat set
            my_set = {1, 2, 3}

            # Menambahkan elemen ke dalam set
            my_set.add(4)

            # Menghapus elemen dari set
            my_set.remove(2)            
            ''')
            st.write('Set juga mendukung penggunaan operator matematika seperti union, intersection, difference, dan symmetric difference. Contohnya seperti ini:')
            st.code('''
            # Membuat set
            set1 = {1, 2, 3, 4}
            set2 = {3, 4, 5, 6}

            # Union
            union_set = set1 | set2
            # atau bisa ditulis seperti ini:
            union_set = set1.union(set2)

            # Intersection
            intersection_set = set1 & set2
            # atau bisa ditulis seperti ini:
            intersection_set = set1.intersection(set2)

            # Difference
            difference_set = set1 - set2
            # atau bisa ditulis seperti ini:
            difference_set = set1.difference(set2)

            # Symmetric difference
            symmetric_difference_set = set1 ^ set2
            # atau bisa ditulis seperti ini:
            symmetric_difference_set = set1.symmetric_difference(set2)            
            ''')
        with dict_tab:
            st.write('''
            ### Dictionary

            Dictionary di Python adalah salah satu tipe data yang memungkinkan kita untuk menyimpan pasangan kunci (key) dan nilai (value). Setiap elemen di dalam dictionary terdiri atas sebuah key dan value yang berpasangan. Key haruslah unique dan immutable, sedangkan value bisa berupa objek apapun.

            kita dapat membuat dictionary dengan menggunakan tanda kurung kurawal (`{}`) dan memisahkan setiap pasangan key-value dengan tanda koma (,). Contohnya seperti ini:
            
            ''')
            st.code('''
            my_dict = {'nama': 'Azhira', 'umur': 18, 'pekerjaan': 'programmer'}          
            ''')
            st.write('Untuk mengakses nilai pada dictionary, gunakan key yang bersesuaian dengan nilai yang ingin kita akses. Contohnya seperti ini:')
            st.code('''
            print(my_dict['nama']) # Output: Azhira
            ''')
            st.write('''
            Kita juga dapat menambahkan atau mengubah nilai pada dictionary dengan cara yang sama seperti saat membuat dictionary. Contohnya seperti ini:
            ''')
            st.code('''
            my_dict['umur'] = 19 # Mengubah nilai umur dari 18 menjadi 19
            my_dict['alamat'] = 'Jakarta' # Menambahkan pasangan key-value baru  
            ''')
            st.write('''
            Selain itu, kita juga dapat menggunakan method-method built-in pada dictionary, seperti `keys()`, `values()`, dan `items()` untuk mengambil daftar key, daftar value, atau daftar pasangan key-value pada dictionary
            ''')
            st.code('''
            print(my_dict.keys()) # Output: dict_keys(['nama', 'umur', 'pekerjaan', 'alamat'])
            print(my_dict.values()) # Output: dict_values(['Azhira', 19, 'programmer', 'Jakarta'])
            print(my_dict.items()) # Output: dict_items([('nama', 'Azhira'), ('umur', 19), ('pekerjaan', 'programmer'), ('alamat', 'Jakarta')])

            ''')




    # DATA STRUCTURE BASIC END
    
    # FUNCTION BASIC START
    elif menu == 'Function (DEF)':
        st.header('Function')
        st.write('''
        > Function (fungsi) adalah blok kode yang dapat digunakan kembali dan melakukan tugas tertentu. Fungsi dapat dianggap sebagai blok kode yang melakukan tugas tertentu ketika dipanggil oleh program utama atau oleh fungsi lainnya.

        Fungsi di definisikan menggunakan kata kunci `def`, diikuti dengan nama fungsi dan tanda kurung yang berisi parameter masukan (jika ada) yang dipisahkan oleh tanda koma. Setelah itu, diikuti dengan tanda titik dua (`:`). Baris selanjutnya harus dimulai dengan indentasi (tab) untuk menunjukkan bahwa kita berada di dalam blok kode fungsi. Di dalam fungsi, kita dapat melakukan operasi apa pun yang ingin kita lakukan dengan kode.

        Contoh:
        ''')
        st.code('''
        def luas(panjang, lebar):
            luas = panjang * lebar
            return luas
        ''')
        with st.expander('See code explanation'):
            st.write('''
            1. Definisikan fungsi yang bernama `luas` dengan parameter `panjang` dan `lebar`
            2. Buat variable baru dengan nama `luas` yang menampung hasil perkalian dari `panjang` dan `lebar`
            3. Kembalikan `luas` sebagai hasil dari fungsi tsb
            
            ''')
        st.write('''
        Pada contoh di atas, `def` digunakan untuk mendefinisikan suatu fungsi dengan nama `luas`. Fungsi tersebut menerima dua parameter yaitu `panjang` dan `lebar`, kemudian melakukan perhitungan untuk menghasilkan nilai luas yang akan dikembalikan melalui kata kunci `return`
        
        Untuk memanggil fungsi tersebut dengan cara:
        ''')
        st.code('''
        print(luas(3,2)) # Outputnya 6
        
        print('Luas persegi dengan panjang 3 dan lebar 2 adalah', luas(3,2))
        # Outputnya Luas persegi dengan panjang 3 dan lebar 2 adalah 6
        ''')
        st.write('''
        ---
        #### Contoh contoh

        1. Mencari rata-rata dari suatu list
        ''')
        st.code('''
        def average(x):
            avg = sum(x)/len(x)
            return avg
        ''')
        st.write('2. Convert IDR to USD')
        st.code('''
        def usdToIdr(usd):
            idr = usd * 15000
            return idr
        ''')
        st.write('3. Square root')
        st.code('''
        import math
        def sqrt(x):
            x = math.sqrt(x)
            return x
        ''')
        st.write('4. Game batu, gunting, kertas')
        st.code('''
        import random

        def get_user_choice():
            valid_choices = ['rock', 'paper', 'scissors']
            choice = input("Choose rock, paper, or scissors: ")
            while choice.lower() not in valid_choices:
                print("Invalid choice. Please try again.")
                choice = input("Choose rock, paper, or scissors: ")
            return choice.lower()

        def get_computer_choice():
            choices = ['rock', 'paper', 'scissors']
            return random.choice(choices)

        def determine_winner(user_choice, computer_choice):
            if user_choice == computer_choice:
                return None
            elif user_choice == 'rock' and computer_choice == 'scissors':
                return 'user'
            elif user_choice == 'paper' and computer_choice == 'rock':
                return 'user'
            elif user_choice == 'scissors' and computer_choice == 'paper':
                return 'user'
            else:
                return 'computer'

        def play_game():
            print("Let's play rock-paper-scissors!")
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"Computer chose {computer_choice}")
            winner = determine_winner(user_choice, computer_choice)
            if winner is None:
                print("It's a tie!")
            else:
                print(f"{winner.capitalize()} wins!")

        play_game()

        
        ''', line_numbers=True)
        

    # FUNCTION BASIC END

    # INPUT OUTPUT BASIC START
    elif menu == 'Input/Output':
        st.header('Input/Output')
        st.write('''
        > Input di Python menggunakan fungsi `input()`
        
        Fungsi ini memungkinkan pengguna untuk memberikan masukan melalui keyboard, dan kemudian menyimpannya dalam variabel untuk digunakan dalam program selanjutnya
        
        Contoh penggunaannya adalah sebagai berikut:   
        ''')
        st.code('''
        nama = input("Masukkan nama Anda: ")
        umur = input("Berapa umur Anda  : ")
        ''')
        st.write('''
        ---
        > Output di Python menggunakan fungsi `print()`
        
        Fungsi ini menerima satu atau lebih argumen sebagai input dan mencetaknya ke console.
        
        Contoh penggunaannya adalah sebagai berikut:
        ''')
        st.code('''
        print('Halo', nama)
        ''')
        st.write('''
        ##### F-string
        Format print() yang digunakan untuk menggabungkan teks dengan variabel/nilai tertentu, dengan format `f'string text biasa {variable}'`

        ''')
        st.code('''
        print(f'Selamat pagi {nama}') # Tiap memasukkan variable menggunakan {}
        ''')
        st.write('''
        ---

        Selain itu, Python juga mendukung operasi file I/O, yang memungkinkan program untuk membaca dan menulis file. Untuk membuka file, kita dapat menggunakan fungsi`open()` dengan mode akses tertentu (seperti 'r' untuk membaca atau 'w' untuk menulis). Setelah mendapatkan objek file, kita dapat menggunakan metode `read()` dan `write()` untuk membaca dan menulis isi file tersebut.
        
        Contoh penggunaannya adalah sebagai berikut:
        ''')
        st.code('''
        # membuka file untuk membaca
        file_in = open("contoh.txt", "r")
        isi_file = file_in.read()
        print(isi_file)

        # membuka file untuk menulis
        file_out = open("hasil.txt", "w")
        file_out.write("Ini adalah contoh hasil penulisan ke file.")
        file_out.close()
        ''')
    # INPUT OUTPUT BASIC END

    # LOOPING BASIC START
    elif menu == 'Looping (FOR/WHILE)':
        st.header('Looping Basic i/ Python')
        st.write('''
        Sebuah konsep yang digunakan untuk melakukan perulangan terhadap satu atau beberapa bagian kode, dengan tujuan untuk menjalankan suatu proses secara berulang-ulang selama kondisi tertentu terpenuhi

        > *Jika kita tahu berapa kali perulangan yang dilakukan, gunakan `for` loop, jika tidak, gunakan `while` loop. Kita bisa menggunakan perulangan di dalam perulangan yang disebut `Nested loop`*
        ''')

        for_tab, while_tab, nested_tab = st.tabs(['For loop', 'While loop', 'Nested loop'])
        with for_tab:
            st.write('### For loop')
            st.write('''
            > `for` digunakan untuk melakukan iterasi atau pengulangan pada sebuah objek yang terdiri dari beberapa elemen seperti list, tuple, set, dan dictionary. For loop berguna untuk mengulangi suatu tindakan sebanyak i kali atau sebanyak elemen yang ada pada sebuah objek.

            Format dari for loop sbg berikut:
            ''')
            st.code('''
            for variable in object:
                # code blok yang akan diulang
            ''')
            with st.expander('See explanation:'):
                st.write('Buat perulangan `for` sebanyak isi dari `object` pada variabel yang bernama `variable` di tiapnya. Kode blok yang berada di dalam `for` lah yang akan diulang')
            st.write('''
            Pada bentuk ini, `variable` merupakan variabel yang akan memegang nilai dari setiap elemen pada `object`, sedangkan `object` adalah objek yang akan diiterasi oleh for loop.

            ---
            #### For in :red[range()]
            
            Dengan `for in range()` kita bisa dengan bebas mengatur berapa kali perulangan yang akan dilakukan

            Misal kita ingin mengulangi kata `halo` sebanyak 5 kali menggunakan for loop''')
            st.code('''
            for i in range(5):
                print('halo')
            ''')
            st.write('''
            ##### Variasi :red[range()]
            1. **range(x)**, dengan 1 argumen
            maka akan melakukan perulangan sebanyak `x`, dengan variabelnya berupa angka `0` sampai `x-1`            
            ''')
            st.code('''
            for i in range(10)
                print(i)
            # Berulang 10 kali, dengan output angka 0 sampai 9''')
            st.write('''
            2. **range(:red[x], :blue[y])**, dengan 2 argumen sebagai :red[*start*] dan :blue[*stop*], maka akan melakukan perulangan sebanyak `y-x`, dengan variabelnya berupa angka dimulai dari `x` dan diakhiri `y-1`
            ''')
            st.code('''
            for i in range(10, 16):
                print(i)
            # Berulang (16 - 10) kali dengan output i yaitu 10, 11, 12, 13, 14, 15''')
            st.write('''
            3. **range(:red[x], :blue[y], :green[z])**, dengan 3 argumen sebagai :red[*start*], :blue[*stop*], dan :green[*step*], maka akan melakukan perulangan sebanyak `(y-a)/z` (pembulatan ke bawah jika diperlukan), dengan variabelnya berupa angka yang dimulai dari `x` hingga `y` dengan langkah `z`''')
            st.code('''
            for i in range(0, 24, 3):
                print(i)
            # Berulang (24-0)/3 = 8 kali dengan output i yaitu 0, 3, 6, 9, 12, 15, 18, 21
            ''')
            st.write('''
            ---
            #### For in :red[list]
            Kita bisa mengakses suatu list dengan `for` dengan `object` nya yaitu list yang digunakan, sebagai contoh:
            ''')
            st.code('''
            a_list = [1,2,3,4,5,6]
            for i in a_list:
                print(i)
            # akan menampilkan tiap isi dari a_list yaitu 1, 2, 3, 4, 5, 6
            ''')
            st.code('''
            name_list = ['Azhira', 'Dhyss', 'Rahmad']
            for i in name_list:
                print('Halo', i)
            # akan menampilkan `Halo dan nama` yang didapet dari dalam name_list
            ''')
            st.write('##### Example 1')
            st.code('''
            a_list = [3, 4, 5, 6, 7, 8, 9]
            for i in a_list:
                if i % 2 == 0:
                    print(i, 'adalah bilangan genap')
                else:
                    print(i, 'adalah bilangan ganjil')
            ''')
            with st.expander('See code explanation'):
                st.write('''
                `for` digunakan untuk melakukan iterasi pada setiap elemen dalam list `a_list`. Pada setiap iterasi, variabel `i` akan menyimpan nilai dari elemen yang sedang diperiksa.

                Kemudian, pernyataan if digunakan untuk memeriksa apakah nilai `i` adalah bilangan genap atau ganjil. Jika nilai `i` dapat dibagi dengan 2 tanpa sisa (yaitu jika `i % 2 == 0`), maka program akan mencetak pesan bahwa bilangan tersebut adalah genap. Jika nilai i tidak dapat dibagi dengan 2 tanpa sisa (yaitu jika `i % 2 != 0`), maka program akan mencetak pesan bahwa bilangan tersebut adalah ganjil.
                ''')
            st.write('''
            Dalam hal ini, for digunakan untuk mengulang proses yang sama pada setiap elemen dalam list a_list, sehingga memungkinkan program untuk memeriksa setiap bilangan dalam list dan menentukan apakah bilangan tersebut genap atau ganjil.
            
            ##### For sebanyak isi list
            
            Kita bisa membuat perulangan sebanyak dari isi list dengan menggunakan `range(len())`. Function `len()` (baca: *length*) akan mengeluarkan panjang/isi dari suatu list
            
            ''')
            st.code('''
            name_list = ['Azhira', 'Dhyss', 'Rahmad', 'Brando']
            for i in range(len(name_list)):
                print('Bocil absen', i+1, 'adalah', name_list[i])
            ''')
            with st.expander('See output'):
                st.code('''
                Bocil absen 1 adalah Azhira
                Bocil absen 2 adalah Dhyss
                Bocil absen 3 adalah Rahmad
                Bocil absen 4 adalah Brando
                ''')
            with st.expander('See code explanation'):
                st.write('''
                `len(name_list)` dalam `range()` akan mengeluarkan nilia `4` karena jumlah isi dari list adalah 4, menjadi `range(4)`. Sehingga perulangan berlansung 4 kali dengan nilai i yaitu 0, 1, 2, 3.

                `i+1` karena saya mau absen dimulai dari angka 1 bukan 0.

                ''')
            
            st.write('''
            > *Selain list, for juga bisa digunakan untuk tuple, set, dan dictionary, konsepnya sama dan     tergantung fungsi penggunaan codenya*
            ''')
        with while_tab:
            st.write('''
            ### While loop

            > `while` digunakan untuk melakukan iterasi atau perulangan pada sebuah blok kode selama kondisi tertentu terpenuhi (baca: while, *selagi*)

            Sintaks dasar while loop di Python adalah sebagai berikut:
            
            ''')
            st.code('''
            while kondisi:
                # blok kode yang akan diulang
            ''')
            with st.expander('See code explanation'):
                st.write('Pertama program akan mengevaluasi kondisi yang diberikan. Jika kondisi tersebut menghasilkan nilai `True`, maka program akan memasuki blok kode yang terletak di bawahnya dan menjalankannya. Setelah blok kode tersebut selesai dijalankan, program akan kembali ke atas dan mengevaluasi kondisi lagi. Proses ini akan terus berulang sampai kondisi menghasilkan nilai `False`, sehingga program keluar dari while loop dan melanjutkan eksekusi kode setelahnya.')
            
            st.write('''
            > Konsep `while` seperti `if`, cuma dia akan melakukan `if` secara beruntun sampai mendapatkan nilai `False` dan berhenti

            Perlu diingat bahwa jika kondisi pada while loop tidak pernah menjadi `False`, maka program akan terjebak dalam **infinite loop** atau perulangan tak terbatas yang dapat menyebabkan program menjadi tidak responsif atau bahkan crash. Oleh karena itu, pastikan kondisi yang diberikan dapat dipenuhi dengan cukup cepat atau berikan batasan jumlah iterasi yang diizinkan agar program tidak mengalami infinite loop.

            ##### Example
            ''')
            st.code('''
            x = 1
            while x <= 10:
                print(x)
                x += 1
            ''')
            with st.expander('See code explanation'):
                st.write('''
                1. Deklarasikan variable `x` dengan nilai 1
                2. Selagi `x` kurang dari sama dengan 10, maka jalankan perulangan menampilkan `x` nya dan tambahkan 1 pada `x`

                Maka akan menampilkan angka 1 sampai 10
                    ''')
            st.write('''
            ##### while :red[True:]
            Untuk melakukan infinity loop kita bisa menggunakan `while True`, tetapi cara ini kurang disarankan, karena program tidak akan pernah berhenti selain diinterupsi.

            Kit bisa menghentikan suatu statement termasuk `while` dengan `break` 
            ''')
            st.code('''
            x = 1
            while True:
                print(x)
                if x == 5:
                    break # jika x sama dengan 5 maka infinty loop akan berhenti
                x += 1
            ''')
            st.write('> *Gmn klw while :red[False]? ya gak akan pernah jalan*')
        with nested_tab:
            st.write('''
            ### Nested loop

            > Nested loop merujuk pada penggunaan satu loop di dalam loop lain. Hal ini memungkinkan program untuk melakukan iterasi atau :red[perulangan di dalam perulangan], sehingga kita dapat melakukan tugas yang lebih kompleks.

            Pada nested loop, iterasi di dalam loop terluar dilakukan secara penuh sebelum melakukan iterasi pada loop dalam. Setiap kali iterasi pada loop terluar selesai dilakukan, program akan kembali ke awal iterasi pada loop dalam dan mengevaluasi elemen pertama lagi.
            
            Nested loop bisa berupa:
            ''')
            st.code('''
            for di dalam for
            while di dalam while
            for di dalam while
            while di dalam for
            ''')
            st.write('''
            ##### Example
            
            Kita disuruh buat program yang menampilkan
            ''')

            left_col, right_col = st.columns([3,7])

            with left_col:
                st.write('Soal')
                st.code('''
                2
                3
                4
                3
                4
                5
                4
                5
                6
                5
                6
                7   
                ''')
            with right_col:
                st.write('Dengan analisis')

                st.code('''
                2 # iterasi i ke 1, yaitu 2
                3 # i+1
                4 # i+=1
                3 # iterasi i ke 2, yaitu 3
                4 # i+1
                5 # i+=1
                4 # iterasi i ke 3, yaitu 4
                5 # i+1
                6 # i+=1
                5 # iterasi i ke 4, yaitu 5
                6 # i+1
                7 # i+=1
                
                ''')
            st.write('Maka kita bisa buat loop di dalam loop')
            st.code('''
            
            for i in range(2, 6):
                for j in range(3):
                    print(i)
                    i += 1
            ''')
            with st.expander('See code explanation'):
                st.code('for i in range(2, 6):')
                st.write('Buat 4 kali perulangan yang dimulai dari 2 dan diakhiri 5')
                st.code('for j in range(3):')
                st.write('Didalamnya buat 3 kali perulangan, gunakan nama variable yang berbeda')
                st.code('''
                print(i)
                i += 1''')
                st.write('''
                Tampilkan `i`, dan tambahkan `i` dengan 1 untuk tiap `j` yang berulang
                
                Maka akan menampilkan sesuai yang diperiintahkan''')
    # LOOPING BASIC END

    # MODULE BASIC START
    elif menu == 'Modules':
        st.header('Modules')
        st.write('''
        > `Module` adalah file yang berisi definisi `function`, `class`, dan `variable` yang dapat digunakan oleh program Python lainnya

        Modul memungkinkan kita untuk memisahkan kode yang sama dari kode utama sehingga kita hanya perlu menulis ulang satu kali. Misalnya, jika kita memiliki beberapa program Python yang membutuhkan fungsi umum seperti menghitung luas lingkaran, maka kita dapat membuat modul yang berisi definisi fungsi tersebut dan mengimpor modul tersebut ke dalam program-program lainnya.

        Untuk menggunakan modul, kita dapat mengimpor modul dengan menggunakan perintah `import` diikuti dengan nama module yang digunakan seperti:
        ''')
        st.code('''
        import math
        ''')
        st.write('''
        Kode tersebut akan mengimport module yang bernama `math` yang berisi kumpulan fungsi matematika, seperti:

        - `math.ceil(x)`, membulatkan bilangan x ke atas menjadi bilangan bulat terdekat.
        - `math.floor(x)`, membulatkan bilangan x ke bawah menjadi bilangan bulat terdekat.
        - `math.sqrt(x)`, mengembalikan akar kuadrat dari bilangan x.
        - `math.exp(x)`, mengembalikan nilai eksponensial dari bilangan x.
        - `math.log(x, base)`, mengembalikan logaritma basis base dari bilangan x. Jika base tidak diberikan, maka akan menggunakan logaritma natural (basis e).
        - `math.sin(x)`, `math.cos(x)`, `math.tan(x)`, menghitung nilai sin, cos, dan tan dari sudut x dalam radian.
        - `math.degrees(x)`, `math.radians(x)`, mengonversi sudut dari derajat ke radian dan sebaliknya

        Selain itu juga berisi konstanta seperti:

        - `math.pi`, konstanta pi (π) yang merupakan rasio keliling lingkaran dengan diameternya.
        - `math.e`. konstanta euler (e) yang merupakan bilangan konstan yang muncul di banyak rumus matematika.

        
        Berikut adalah beberapa contoh penggunaan modul `math`:

        1. Mencari panjang c dari segitiga dengan rumus pytagoras
        ''')
        st.code('''
        import math

        a = float(input('a: '))
        b = float(input('b: '))
        c = math.sqrt(a**2 + b**2)
        print('c:', c)
        ''')
        with st.expander('See code explanation'):
            st.write('''
            Kita mengimpor modul `math`, kemudian menghitung nilai dari akar kuadrat dari jumlah kuadrat dari variabel `a` dan `b` menggunakan fungsi `sqrt()` dari modul `math`
            ''')
        st.write('''
        2. Menggunakan konstanta `pi` untuk menghitung luas lingkaran
        ''')
        st.code('''
        import math

        r = float(input('r: '))
        a = math.pi * r * r
        print('a', a)
        ''')
        with st.expander('See code explanation'):
            st.write('''
            Kita mengimpor modul `math`, kemudian memanggil konstanta `pi` dari module `math` untuk menghitung luas lingkaran *instead* mengggunakan `22/7`
            ''')
        st.write('''
        Selain `math`, Python juga menyediakan banyak module yang memiliki fungsi yang berbeda-beda, seperti: `math`, `random`, `datetime`, `os`, `sys`, `re`, `numpy`, `request`, dan masih banyak lagi
        ''')
    # MODULE BASIC END
# BASICS END






# OOP START
elif option == 'Classes (OOP)':
    st.header('Classes (OOP)')
    st.image('https://media.giphy.com/media/QwagscIeqr3yPVwQKw/giphy.gif')
    st.write('''
    > *Khusus ~kmu~ OOP (Object Oriented Programming)*, selamat belajar mandiri
    
    > *:red[Contact me] if you need help tutor/assignment :red[jockey] on subjects related to python, :red[including OOP], such as Computational Thinking, Fundamental/Intermediate Programming, and Programming and Algorithm. Thank yu🎈🎈*
    ''')

    if st.button('Contact me'):
        url = 'https://www.instagram.com/thinkaboutziz'
        webbrowser.open_new_tab(url)
# OOP END


# CHEATSHEET
elif option == 'Cheatsheet':
    st.header('Python Cheatsheet v/ az')
    # st.write('The author does not need a cheat sheet')
    st.markdown('''
    1. Datatypes:
        - `string`, `str`, rangkaian huruf/angka sebagai 1 objek,`'-3'`, `'2.5'`, `'apple'`, etc.
        - `integer`, `int`, bilangan bulat, `-1`, `0`, `1`, `100`, etc.
        - `float`, pecahan/desimal, i.e. `3.14`, `2.7182818459045`, etc.
        - `boolean`, `bool`, `True` dan `False`
    2. Conditional Statement:
        - `if` jika
        - `elif` lain jika
        - `else` jika tidak
    3. Arithmetic Expression
        - `+`
        - `-`
        - `*`
        - `/`
        - `%` modulo, sisa bagi, `5 % 2` = `1`
        - `//` pembagian tp dibulatkan, `10 // 3` = `3`
        - `**` pangkat, `2 ** 4` = `16`
    4. Boolean Algebra
        - `and` keduanya harus True agar True
        - `or` salah satu atau keduanya harus benar agar True
        - `not` negasi
        - `in` di dalam suatu container
        - `==` equal to
        - `!=` not equal to
        - `<` lower than
        - `>` greater than
        - `<=` equal lower than
        - `>=` equal greater than
    
    
        ''')
# CHEATSHEET END




# EXERCISE
elif option == 'Exercise':
    if menu == 'Pro':
        st.write('''
        # Exercise 1
        1. Berikut adalah contoh yg benar dalam mendefinisikan list di Python

        \t a. dinoList = {"T-Rex", "Stegosaurus", "Velociraptor"} \n
        \t b. dinoList = ["T-Rex", "Stegosaurus", "Velociraptor"] \n
        \t c. dinoList = ("T-Rex", "Stegosaurus", "Velociraptor") \n
        \t d. dinoList = <"T-Rex", "Stegosaurus", "Velociraptor">
        ''')
        with st.expander('Show answer'):
            st.write('b')

