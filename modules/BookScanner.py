import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass


class BookScanner():
    """A BookScanner takes a URL_list."""

    def __init__(self, url_list):
        """Initialize the TextContainer with text."""
        self.url_list = url_list
        self.filenames = []

    def download(self, url, filename):
        filename = str(filename) + ".txt"

        r = requests.get(url)
        
        if r.status_code == 404:
            print("404 Error")
            raise NotFoundException
        
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size = 1024):
                f.write(chunk)

        self.filenames.append(filename)

    def multi_download(self):
        workers = len(self.url_list)
        
        with ThreadPoolExecutor(workers) as executor:
            executor.map(self.download, self.url_list, range(len(self.url_list)))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        current_index = self.index

        if current_index < len(self.filenames):
            self.index += 1
            return self.filenames[current_index]
        else:
            raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, filename):
        vowels = ["A", "E", "I", "O", "U", "Y"]

        with open(filename) as input_file:
            text = input_file.read()

        words = text.split()
        number_of_words = len(words)

        number_of_vowels = 0

        for word in words:
            for letter in word:
                if letter.upper() in vowels:
                    number_of_vowels += 1

        score = round(number_of_vowels / number_of_words, 5)
        return score, filename

    def hardest_read(self):
        workers = multiprocessing.cpu_count()
        
        with ProcessPoolExecutor(workers) as executor:
            results = executor.map(self.avg_vowels, self.filenames)
            
        highest_avg = None

        for result in results:
            if highest_avg is None or highest_avg[0] < result[0]:
                highest_avg = result

        return highest_avg[1]
