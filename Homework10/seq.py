import urllib.request as ur
import flags
import os
import time

def getGifs():
    if not os.path.exists('flags'):
        os.makedirs('flags')
    url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    for item in flags.flags:
        name = item + '-lgflag.gif'
        ur.urlretrieve(url + name, 'flags/' + name)
    ur.urlcleanup()

def main():
    print('Starting sequential...')

    start = time.time()
    cpu = time.process_time()
    getGifs()
    end = time.time()-start
    cpuEnd = time.process_time()-cpu

    with open('seq.txt', 'w') as f:
        f.write(str(os.path.getsize('flags')) + ' bytes downloaded\n')
        f.write('It took ' + str(end) + ' seconds\n')
        f.write('It took the CPU ' + str(cpuEnd) + ' seconds\n')
    print('Finished')

if __name__ == "__main__":
    main()